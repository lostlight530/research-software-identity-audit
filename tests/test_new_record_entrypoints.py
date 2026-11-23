"""Offline regression tests for PR-only new dated evidence envelopes."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from check_new_record_entrypoints import check_new_events, dated_events

EVENT = "2026-11-24/01-synthetic-public-diagnostic"
M = f"monitoring/{EVENT}/"
E = f"evidence/{EVENT}/"
INDEX = f"- [diagnostic]({EVENT}/README.md)\n"


class NewRecordEntrypointTests(unittest.TestCase):
    def setUp(self):
        self.base = {"monitoring/README.md", "evidence/README.md"}
        self.current = self.base | {
            M + "README.md", M + "record.json",
            E + "README.md", E + "source-attempts.jsonl",
        }

    def check(self, index=INDEX):
        return check_new_events(self.base, self.current, index)

    def test_complete_new_monitoring_and_evidence_pass(self):
        result = self.check()
        self.assertEqual(result["failed"], 0)
        self.assertEqual(result["new_monitoring_events"], [EVENT])
        self.assertEqual(result["new_evidence_events"], [EVENT])
        self.assertEqual(result["network_calls"], 0)

    def test_monitoring_readme_missing_fails(self):
        self.current.remove(M + "README.md")
        self.assertIn("missing monitoring README.md", " ".join(self.check()["errors"]))

    def test_machine_record_missing_fails(self):
        self.current.remove(M + "record.json")
        self.assertIn("exactly one", " ".join(self.check()["errors"]))

    def test_competing_machine_records_fail(self):
        self.current.add(M + "record.yaml")
        self.assertIn("exactly one", " ".join(self.check()["errors"]))

    def test_yaml_only_machine_record_passes(self):
        self.current.remove(M + "record.json")
        self.current.add(M + "record.yaml")
        self.assertEqual(self.check()["failed"], 0)

    def test_missing_index_reference_fails(self):
        self.assertIn("missing monitoring/README.md", " ".join(self.check(index="")["errors"]))

    def test_evidence_readme_missing_fails(self):
        self.current.remove(E + "README.md")
        self.assertIn("missing evidence README.md", " ".join(self.check()["errors"]))

    def test_orphan_evidence_package_fails(self):
        self.current = self.base | {E + "README.md", E + "source.jsonl"}
        self.assertIn("lacks matching monitoring event", " ".join(self.check()["errors"]))

    def test_monitoring_without_evidence_allowed(self):
        self.current = self.base | {M + "README.md", M + "record.json"}
        self.assertEqual(self.check()["failed"], 0)

    def test_existing_records_are_not_retroactively_gated(self):
        self.base = self.current.copy()
        self.current.add(M + "correction-history.md")
        self.assertEqual(self.check(index="")["failed"], 0)
        self.assertEqual(self.check(index="")["new_monitoring_events"], [])

    def test_only_new_evidence_companion_requires_evidence_readme(self):
        self.base |= {M + "README.md", M + "record.json"}
        self.current = self.base | {E + "source.jsonl"}
        result = self.check(index="")
        self.assertEqual(result["new_monitoring_events"], [])
        self.assertIn("missing evidence README.md", " ".join(result["errors"]))

    def test_bad_date_is_not_misclassified_as_valid_dated_event(self):
        self.assertEqual(
            dated_events({"monitoring/2026-02-30/01-invalid/README.md",
                          "monitoring/2026-11-24/00-invalid/README.md"}, "monitoring"),
            set(),
        )


if __name__ == "__main__":
    unittest.main()
