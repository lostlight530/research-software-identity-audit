"""Network-free regression tests for future bounded public source collection."""
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from public_source_transport import (
    DEFAULT_BODY_LIMIT, EDAM_OWL_BODY_LIMIT, complete_integer_total,
    read_bounded, response_limit, transport_state, request_timeout_seconds,
    complete_positive_count,
)


class PublicSourceTransportTests(unittest.TestCase):
    def test_edam_whole_3413870_bytes_are_not_truncated(self):
        body = b"E" * 3_413_870
        data, failure, cap = read_bounded(io.BytesIO(body), "surface", "15:EDAM")
        self.assertEqual(len(data), len(body))
        self.assertIsNone(failure)
        self.assertEqual(cap, EDAM_OWL_BODY_LIMIT)

    def test_normal_source_stays_bounded_to_two_megabytes(self):
        data, failure, cap = read_bounded(
            io.BytesIO(b"x" * (DEFAULT_BODY_LIMIT + 10)), "surface", "13:dkNET"
        )
        self.assertEqual(cap, DEFAULT_BODY_LIMIT)
        self.assertEqual(len(data), DEFAULT_BODY_LIMIT + 1)
        self.assertEqual(failure, "TRUNCATED_RESPONSE_LIMIT")

    def test_edam_oversize_is_still_partial(self):
        data, failure, cap = read_bounded(
            io.BytesIO(b"x" * (EDAM_OWL_BODY_LIMIT + 1)), "surface", "15:EDAM"
        )
        self.assertEqual(len(data), cap + 1)
        self.assertEqual(failure, "TRUNCATED_RESPONSE_LIMIT")


    def test_new_collector_help_is_executable_without_network(self):
        import subprocess
        proc = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parents[1] /
                                "tools/public_source_recheck.py"), "--help"],
            capture_output=True, text=True, check=False, timeout=15,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("--only-key", proc.stdout)
        self.assertIn("--only-scope", proc.stdout)

    def test_non_edam_key_cannot_inherit_ontology_exception(self):
        self.assertEqual(response_limit("surface", "14:InterLex"), DEFAULT_BODY_LIMIT)
        self.assertEqual(response_limit("zenodo_version", "15:EDAM"), DEFAULT_BODY_LIMIT)

    def test_blocked_and_not_found_are_not_identity_absence(self):
        self.assertEqual(transport_state(403, "HTTP_403"), "BLOCKED_OR_RATE_LIMITED")
        self.assertEqual(transport_state(429, "HTTP_429"), "BLOCKED_OR_RATE_LIMITED")
        self.assertEqual(transport_state(404, "HTTP_404"), "HTTP_404_NOT_PROOF_OF_ABSENCE")
        self.assertEqual(transport_state(None, "URLError"), "RETRIEVAL_UNRESOLVED")
        self.assertEqual(transport_state(200, "TRUNCATED_RESPONSE_LIMIT"), "PARTIAL_RESPONSE")
        self.assertEqual(transport_state(200, None), "HTTP_200_TRANSPORT_ONLY")

    def test_open_aire_timeout_is_explicit_and_host_specific(self):
        self.assertEqual(request_timeout_seconds("https://api.openaire.eu/search/software"), 15)
        self.assertEqual(request_timeout_seconds("https://zenodo.org/api/records/1"), 15)
        self.assertEqual(request_timeout_seconds("https://api.datacite.org/dois/example"), 10)
        self.assertEqual(request_timeout_seconds("https://api.openaire.eu.evil.invalid/a"), 10)

    def test_partial_doi_queries_must_not_claim_full_coverage(self):
        expected = {"a", "b"}
        rows = [
            {"key": "a", "http_status": 200, "failure": None,
             "selected_public_fields": {"result_total": "1"}},
            {"key": "b", "http_status": None, "failure": "TimeoutError",
             "selected_public_fields": {}},
        ]
        self.assertIsNone(complete_positive_count(
            rows, expected_keys=expected, field="result_total", mode="nonnegative_integer"))
        rows[1] = {"key": "b", "http_status": 200, "failure": None,
                   "selected_public_fields": {"result_total": "0"}}
        self.assertEqual(complete_positive_count(
            rows, expected_keys=expected, field="result_total", mode="nonnegative_integer"), 1)
        rows[1]["selected_public_fields"] = {}
        self.assertIsNone(complete_positive_count(
            rows, expected_keys=expected, field="result_total", mode="nonnegative_integer"))

    def test_openalex_exact_requires_full_boolean_evidence(self):
        wanted = {"a", "b"}
        rows = [
            {"key": "a", "http_status": 200, "failure": None,
             "selected_public_fields": {"canonical_doi_exact_match": True}},
            {"key": "b", "http_status": 200, "failure": None,
             "selected_public_fields": {"canonical_doi_exact_match": False}},
        ]
        self.assertEqual(complete_positive_count(
            rows, expected_keys=wanted, field="canonical_doi_exact_match", mode="boolean"), 1)
        rows[1]["selected_public_fields"]["canonical_doi_exact_match"] = None
        self.assertIsNone(complete_positive_count(
            rows, expected_keys=wanted, field="canonical_doi_exact_match", mode="boolean"))

    def test_complete_integer_total_requires_every_key_and_valid_counter(self):
        wanted = {"repo:1", "repo:2"}
        rows = [
            {"key": "repo:1", "http_status": 200, "failure": None,
             "selected_public_fields": {"version_views": 2}},
            {"key": "repo:2", "http_status": 200, "failure": None,
             "selected_public_fields": {"version_views": 5}},
        ]
        self.assertEqual(
            complete_integer_total(rows, expected_keys=wanted, field="version_views"), 7
        )
        self.assertIsNone(
            complete_integer_total(rows[:1], expected_keys=wanted, field="version_views")
        )
        for invalid in (None, -1, "0", True):
            broken = [dict(r) for r in rows]
            broken[1]["selected_public_fields"] = {"version_views": invalid}
            self.assertIsNone(complete_integer_total(
                broken, expected_keys=wanted, field="version_views"
            ))
        duplicate = rows + [rows[0]]
        self.assertIsNone(
            complete_integer_total(duplicate, expected_keys=wanted, field="version_views")
        )


if __name__ == "__main__":
    unittest.main()
