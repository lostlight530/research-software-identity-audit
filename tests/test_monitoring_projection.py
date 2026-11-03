"""Synthetic-only tests for bounded monitoring source ledger structural assurance."""
from __future__ import annotations

import csv
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from check_record_paths import check_projection_ledger, check_surface_id_reconciliation


class BoundedProjectionLedgerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.event = Path(self.temp.name) / "monitoring/2026-10-27/01-synthetic"
        self.event.mkdir(parents=True)
        self.record = {
            "record_class": "diagnostic_monitoring_selected_public_fields",
            "source_attempt_rows": 2,
            "batch_start_utc": "2026-10-27T15:23:29Z",
            "batch_end_utc": "2026-10-27T15:23:32Z",
            "prospective_dataset_member": False,
            "prospective_cells_added": 0,
        }
        self.rows = [
            {
                "attempt_id": "github-01", "platform": "GitHub", "scope": "RS01",
                "locator": "https://api.github.com/repos/example/repo/releases",
                "retrieval_batch_start_utc": "2026-10-27T15:23:29Z",
                "retrieval_batch_end_utc": "2026-10-27T15:23:30Z",
            },
            {
                "attempt_id": "openalex-01", "platform": "OpenAlex",
                "scope": "RESEARCHER",
                "locator": "https://api.openalex.org/authors/example",
                "retrieval_batch_start_utc": "2026-10-27T15:23:30+00:00",
                "retrieval_batch_end_utc": "2026-10-27T15:23:31+00:00",
            },
        ]
        self.write_csv()

    def write_csv(self):
        with (self.event / "source-attempts.csv").open(
            "w", encoding="utf-8", newline=""
        ) as handle:
            writer = csv.DictWriter(handle, fieldnames=list(self.rows[0]))
            writer.writeheader()
            writer.writerows(self.rows)

    def errors(self):
        return check_projection_ledger(self.event, self.record)

    def test_valid_bounded_projection(self):
        self.assertEqual(self.errors(), [])

    def test_missing_ledger_is_not_silently_ignored(self):
        (self.event / "source-attempts.csv").unlink()
        self.assertIn("missing", " ".join(self.errors()))

    def test_row_count_matches_declared_rows(self):
        self.rows.pop()
        self.write_csv()
        self.assertIn("source_attempt_rows=2", " ".join(self.errors()))

    def test_duplicate_attempt_id_is_rejected(self):
        self.rows[1]["attempt_id"] = "github-01"
        self.write_csv()
        self.assertIn("duplicate attempt_id", " ".join(self.errors()))

    def test_required_column_not_silently_dropped(self):
        csv_path = self.event / "source-attempts.csv"
        content = csv_path.read_text(encoding="utf-8")
        csv_path.write_text(content.replace("attempt_id,", "attempt_key,", 1),
                            encoding="utf-8")
        self.assertIn("missing columns", " ".join(self.errors()))

    def test_naive_and_reversed_batch_clocks_rejected(self):
        self.rows[0]["retrieval_batch_start_utc"] = "2026-10-27T15:23:29"
        self.rows[1]["retrieval_batch_end_utc"] = "2026-10-27T15:23:20Z"
        self.write_csv()
        self.assertGreaterEqual(" ".join(self.errors()).count("invalid or unordered"), 2)

    def test_row_cannot_claim_time_outside_batch(self):
        self.rows[0]["retrieval_batch_start_utc"] = "2026-10-27T15:23:28Z"
        self.write_csv()
        self.assertIn("outside record envelope", " ".join(self.errors()))

    def test_diagnostic_is_not_prospective(self):
        self.record["prospective_cells_added"] = 60
        self.assertIn("may not declare prospective", " ".join(self.errors()))

    def test_missing_opt_in_count_for_this_record_class_is_rejected(self):
        del self.record["source_attempt_rows"]
        self.assertIn("missing source_attempt_rows", " ".join(self.errors()))

    def test_legacy_records_are_unmodified_and_unchecked(self):
        self.assertEqual(check_projection_ledger(self.event, {"record_class": "legacy"}), [])


class SyntheticSurfaceReconciliationTests(unittest.TestCase):
    """No network or historical source rewrites: validate a tiny synthetic join."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        source_dir = self.root / "monitoring/2026-11-02/01-source"
        self.event = self.root / "monitoring/2026-11-03/02-derived"
        source_dir.mkdir(parents=True)
        self.event.mkdir(parents=True)
        self.original = source_dir / "source-attempts.csv"
        self.dictionary = source_dir / "platform-results.csv"
        self.derived = self.event / "source-attempts-derived-surface-join.csv"
        self.original.write_text(
            "attempt_id,platform\nfirst,18\nsecond,1\n", encoding="utf-8"
        )
        self.dictionary.write_text(
            "surface,name\n18,DataCite\n1,WorkflowHub\n", encoding="utf-8"
        )
        self.derived.write_text(
            "source_row_ordinal,source_attempt_key,original_platform_column_numeric_value,"
            "derived_surface_id,derived_surface_name,operational_platform_if_core,"
            "core_or_supplementary_class,source_package_date_label,"
            "derivation_provenance_class\n"
            "1,first,18,18,DataCite,datacite,CORE_PLATFORM_SURFACE_ONLY_NOT_A_NEW_UNIT,"
            "2026-11-02,DERIVED_FROM_EXISTING_PUBLIC_LEDGER_NOT_NEW_HTTP_REQUEST\n"
            "2,second,1,1,WorkflowHub,,SUPPLEMENTARY_OR_STANDARDS_SURFACE,"
            "2026-11-02,DERIVED_FROM_EXISTING_PUBLIC_LEDGER_NOT_NEW_HTTP_REQUEST\n",
            encoding="utf-8",
        )
        def blob_sha(path):
            raw = path.read_bytes()
            return hashlib.sha1(
                b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw
            ).hexdigest()

        self.record = {
            "record_class": (
                "retrospective_machine_column_semantics_reconciliation_not_new_platform_capture"
            ),
            "source_attempts_path": self.original.relative_to(self.root).as_posix(),
            "source_results_path": self.dictionary.relative_to(self.root).as_posix(),
            "source_attempts_blob_sha": blob_sha(self.original),
            "source_results_blob_sha": blob_sha(self.dictionary),
            "original_attempt_rows": 2,
            "surface_dictionary_rows": 2,
            "normalized_output_rows": 2,
            "distinct_attempt_keys": 2,
            "distinct_surface_ids_used": 2,
            "source_surface_counts": {"18": 1, "1": 1},
            "source_package_date_label": "2026-11-02",
            "core_mapping": {
                "16": "orcid", "17": "zenodo", "18": "datacite",
                "22": "openalex", "23": "openaire",
                "29": "software_heritage", "30": "github",
            },
            "not_prospective": True,
            "prospective_cells_added": 0,
            "new_http_requests_to_reconstruct_old_2026_11_02_attempts": 0,
        }

    def errors(self):
        return check_surface_id_reconciliation(self.event, self.record, self.root)

    def test_valid_derived_surface_join(self):
        self.assertEqual(self.errors(), [])

    def test_joined_name_cannot_drift_from_source(self):
        self.derived.write_text(
            self.derived.read_text(encoding="utf-8").replace(
                ",DataCite,datacite,", ",WrongDataCite,datacite,"
            ),
            encoding="utf-8",
        )
        self.assertIn("derived_surface_name", " ".join(self.errors()))

    def test_source_bytes_must_match_recorded_git_blob(self):
        self.original.write_text(
            self.original.read_text(encoding="utf-8") + "third,18\n",
            encoding="utf-8",
        )
        self.assertIn("source_attempts_blob_sha", " ".join(self.errors()))

    def test_missing_source_surface_is_not_silently_joined(self):
        self.dictionary.write_text("surface,name\n18,DataCite\n", encoding="utf-8")
        self.assertIn("unknown original surface", " ".join(self.errors()))

    def test_derived_cannot_declare_prospective_cells(self):
        self.record["prospective_cells_added"] = 60
        self.assertIn("must not be labelled as prospective", " ".join(self.errors()))

    def test_legacy_records_not_captured_by_specific_guard(self):
        self.assertEqual(
            check_surface_id_reconciliation(
                self.event, {"record_class": "other_monitoring"}, self.root
            ),
            [],
        )


if __name__ == "__main__":
    unittest.main()
