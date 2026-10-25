"""Synthetic, offline guard tests; never treated as research observations."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import check as audit


def valid_record(**changes):
    record = {
        "observation_id": "SYNTHETIC-TEST-ONLY",
        "object_id": "RS01",
        "platform": "github",
        "infrastructure_layer": "source_repository",
        "observation_timepoint": "SYNTHETIC-T0",
        "dataset_phase": "prospective",
        "retrospective_reconstruction": False,
        "release_event_timestamp": "2026-10-15T08:00:00+08:00",
        "retrieval_timestamp": "2026-10-15T09:00:00+08:00",
        "attempt_status": "completed",
        "observation_state": "observed",
        "evidence_refs": ["evidence/SYNTHETIC-TEST-ONLY"],
    }
    record.update(changes)
    return record


class ObservationSemanticTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "test.json"

    def check(self, **changes):
        self.path.write_text(json.dumps(valid_record(**changes)), encoding="utf-8")
        audit.validate_observation_record(self.path)

    def test_platform_mapping_matches_repository_contract(self):
        audit.check_layers_and_platforms()

    def test_platform_mapping_rejects_mutated_layer(self):
        original = audit.read_text

        def mutated(path):
            source = original(path)
            if path == "schema/platforms.yaml":
                return source.replace(
                    "infrastructure_layer: archival_repository",
                    "infrastructure_layer: author_registry", 1
                )
            return source

        with patch.object(audit, "read_text", side_effect=mutated):
            with self.assertRaisesRegex(AssertionError, "platform-to-layer mapping drifted"):
                audit.check_layers_and_platforms()

    def test_well_formed_synthetic(self):
        self.check()

    def test_all_platform_layer_pairs(self):
        for platform, layer in audit.EXPECTED_PLATFORM_LAYERS.items():
            with self.subTest(platform=platform):
                self.check(platform=platform, infrastructure_layer=layer)

    def test_rejects_cross_layer_swap(self):
        with self.assertRaisesRegex(AssertionError, "platform/layer mismatch"):
            self.check(platform="zenodo")

    def test_rejects_invalid_attempt_status(self):
        with self.assertRaisesRegex(AssertionError, "invalid attempt_status"):
            self.check(attempt_status="unknown")

    def test_failed_needs_reason(self):
        with self.assertRaisesRegex(AssertionError, "requires failure_reason"):
            self.check(attempt_status="failed", observation_state="unresolved")

    def test_failed_cannot_claim_full_verification(self):
        with self.assertRaisesRegex(AssertionError, "cannot itself be fully_verified"):
            self.check(attempt_status="failed", observation_state="fully_verified",
                       failure_reason="timeout")

    def test_failed_rate_limit_stays_valid_outcome(self):
        self.check(attempt_status="failed", observation_state="rate_limited",
                   failure_reason="429 received")

    def test_naive_retrieval_clock_rejected(self):
        with self.assertRaisesRegex(AssertionError, "timezone offset"):
            self.check(retrieval_timestamp="2026-10-15T09:00:00")

    def test_invalid_release_clock_rejected(self):
        with self.assertRaisesRegex(AssertionError, "invalid release_event_timestamp"):
            self.check(release_event_timestamp="not-a-date")

    def test_release_after_retrieval_rejected(self):
        with self.assertRaisesRegex(AssertionError, "later than"):
            self.check(release_event_timestamp="2026-10-16T08:00:00+08:00")

    def test_prospective_needs_event_time(self):
        with self.assertRaisesRegex(AssertionError, "require a release event timestamp"):
            self.check(release_event_timestamp=None)

    def test_retrospective_cannot_be_prospective(self):
        with self.assertRaisesRegex(AssertionError, "cannot be retrospective"):
            self.check(retrospective_reconstruction=True)

    def test_no_blank_or_example_evidence_refs(self):
        for refs in ([""], ["evidence/EXAMPLE-DO-NOT-USE"]):
            with self.subTest(refs=refs):
                with self.assertRaisesRegex(AssertionError, "blank/example-only"):
                    self.check(evidence_refs=refs)

    def test_no_template_timepoint(self):
        with self.assertRaisesRegex(AssertionError, "example observation_timepoint"):
            self.check(observation_timepoint="TEMPLATE_ONLY")

    def test_raw_preflight_requires_active_schedule(self):
        root = Path(self.temp.name)
        (root / "observations/raw").mkdir(parents=True)
        (root / "schedule").mkdir()
        record = root / "observations/raw/observation.json"
        record.write_text(json.dumps(valid_record()), encoding="utf-8")
        previous = audit.ROOT
        try:
            audit.ROOT = root
            with self.assertRaisesRegex(AssertionError, "active schedule"):
                audit.check_observations()
            schedule = root / "schedule/specification.yaml"
            schedule.write_text(
                'schedule_id: "SYNTHETIC"\nstatus: "active"\n'
                'declared_at: "2026-10-15T10:00:00+08:00"\n',
                encoding="utf-8",
            )
            with self.assertRaisesRegex(AssertionError, "predates retrieval"):
                audit.check_observations()
            schedule.write_text(
                'schedule_id: "SYNTHETIC"\nstatus: "active"\n'
                'declared_at: "2026-10-15T07:00:00+08:00"\n',
                encoding="utf-8",
            )
            audit.check_observations()
            record.write_text(json.dumps(valid_record(dataset_phase="historical_baseline")),
                              encoding="utf-8")
            with self.assertRaisesRegex(AssertionError, "dataset_phase=prospective"):
                audit.check_observations()
        finally:
            audit.ROOT = previous


if __name__ == "__main__":
    unittest.main()
