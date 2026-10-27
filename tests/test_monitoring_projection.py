"""Synthetic-only tests for bounded monitoring source ledger structural assurance."""
from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from check_record_paths import check_projection_ledger


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


if __name__ == "__main__":
    unittest.main()
