from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.check_vshwk_contract import ContractError, validate


class VshwkContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        shutil.copytree(ROOT / "studies" / "osf-vshwk",
                        self.root / "studies" / "osf-vshwk")

    def tearDown(self):
        self.tmp.cleanup()

    def test_current_study_package_passes(self):
        result = validate(self.root)
        self.assertEqual(result["manifest_endpoints"], 22)
        self.assertEqual(len(result["cycles_validated"]), 2)
        self.assertEqual({item["cycle_id"] for item in result["cycles_validated"]}, {
            "cycle-2026-11-23-pst-01", "cycle-2026-11-25-pst-01"
        })
        self.assertTrue(all(item["endpoint_rows"] == 22 for item in result["cycles_validated"]))
        self.assertEqual(len(result["incomplete_custody"]), 1)
        self.assertIsNone(result["incomplete_custody"][0]["endpoint_rows"])
        self.assertFalse(result["incomplete_custody"][0]["counted_as_validated_cycle"])

    def test_unclassified_orphan_is_rejected(self):
        path = self.root / "studies/osf-vshwk/cycles/cycle-2026-11-24-pst-01/custody-gap.json"
        path.unlink()
        with self.assertRaisesRegex(ContractError, "missing required artifact"):
            validate(self.root)

    def test_partial_recovery_is_not_exempted(self):
        path = self.root / "studies/osf-vshwk/cycles/cycle-2026-11-24-pst-01/precollection-intent.json"
        path.write_text("{}\n", encoding="utf-8")
        with self.assertRaisesRegex(ContractError, "partial recovery"):
            validate(self.root)

    def test_historical_custody_index_mutation_is_rejected(self):
        path = self.root / "studies/osf-vshwk/cycles/cycle-2026-11-24-pst-01/evidence/README.md"
        with path.open("a", encoding="utf-8") as handle:
            handle.write("\n")
        with self.assertRaisesRegex(ContractError, "custody index Git blob mismatch"):
            validate(self.root)

    def test_duplicate_endpoint_row_is_rejected(self):
        path = (self.root / "studies/osf-vshwk/cycles/"
                "cycle-2026-11-23-pst-01/endpoint-outcome-index.jsonl")
        first_row = path.read_text(encoding="utf-8").splitlines()[0]
        with path.open("a", encoding="utf-8") as handle:
            handle.write(first_row + "\n")
        with self.assertRaisesRegex(ContractError, "duplicate endpoint IDs"):
            validate(self.root)

    def test_raw_source_ledger_mutation_is_rejected(self):
        path = (self.root / "studies/osf-vshwk/cycles/"
                "cycle-2026-11-23-pst-01/evidence/github-attempts.jsonl")
        with path.open("a", encoding="utf-8") as handle:
            handle.write("\n")
        with self.assertRaisesRegex(ContractError, "Git blob"):
            validate(self.root)

    def test_public_description_drift_is_rejected(self):
        path = self.root / "studies/osf-vshwk/public-project-description.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nExtra sentence.\n",
                        encoding="utf-8")
        with self.assertRaisesRegex(ContractError, "Description mirror differs"):
            validate(self.root)

    def test_summary_denominator_drift_is_rejected(self):
        path = (self.root / "studies/osf-vshwk/cycles/"
                "cycle-2026-11-23-pst-01/cycle-summary.json")
        data = json.loads(path.read_text(encoding="utf-8"))
        data["primary_endpoint_attempts"] = 21
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ContractError, "primary attempt count mismatch"):
            validate(self.root)


if __name__ == "__main__":
    unittest.main()
