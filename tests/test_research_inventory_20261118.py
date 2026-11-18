"""Offline regressions for historical Git-blob/path taxonomy (not source verification)."""
from __future__ import annotations

import csv
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from check_research_inventory_20261118 import INVENTORY, validate


class PinnedInventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        target = self.root / INVENTORY
        target.parent.mkdir(parents=True)
        shutil.copytree(ROOT / INVENTORY, target)
        self.directory = target

    def test_valid_pinned_path_snapshot(self):
        self.assertEqual(validate(self.root), [])

    def test_duplicate_source_path_is_rejected(self):
        path = self.directory / "tracked-file-classification.csv"
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(lines + [lines[1]]) + "\n", encoding="utf-8")
        self.assertTrue(any("duplicate" in e or "blob_rows" in e for e in validate(self.root)))

    def test_prospective_eligibility_cannot_be_inferred_from_folder(self):
        path = self.directory / "dated-event-catalog.csv"
        data = path.read_text(encoding="utf-8")
        self.assertIn("NOT_ASSERTED", data)
        path.write_text(data.replace("NOT_ASSERTED", "PROSPECTIVE", 1), encoding="utf-8")
        self.assertTrue(any("prospective promotion" in e for e in validate(self.root)))

    def test_changed_frozen_denominator_is_detected(self):
        path = self.directory / "snapshot.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["contract"]["units_per_eligible_timepoint"] = 70
        path.write_text(json.dumps(value), encoding="utf-8")
        self.assertTrue(any("frozen analytical boundary" in e for e in validate(self.root)))

    def test_missing_day_is_detected(self):
        path = self.directory / "first-day-through-nov18-calendar.csv"
        rows = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(rows[:-1]) + "\n", encoding="utf-8")
        self.assertTrue(any("calendar" in e for e in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
