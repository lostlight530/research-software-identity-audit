"""Synthetic byte-integrity tests for the read-only manifest verifier."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import check_public_artifact_manifest as verifier


class PublicArtifactManifestTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "evidence").mkdir()
        self.payload = self.root / "evidence/test.json"
        self.payload.write_bytes(b'{"foo": 1}\n')
        self.manifest = self.root / "evidence/artifact-manifest.json"

    def write_manifest(self, **changes):
        row = {
            "path": "evidence/test.json",
            "bytes": self.payload.stat().st_size,
            "sha256": hashlib.sha256(self.payload.read_bytes()).hexdigest(),
        }
        row.update(changes)
        self.manifest.write_text(json.dumps({"files": [row]}), encoding="utf-8")

    def test_valid_byte_manifest(self):
        self.write_manifest()
        self.assertEqual(verifier.verify(self.manifest, self.root)["failed"], 0)

    def test_detects_altered_bytes(self):
        self.write_manifest()
        self.payload.write_bytes(b"tampered bytes")
        result = verifier.verify(self.manifest, self.root)
        self.assertGreaterEqual(result["failed"], 1)
        self.assertIn("SHA-256 mismatch", " ".join(result["errors"]))

    def test_missing_file_is_error(self):
        self.write_manifest()
        self.payload.unlink()
        self.assertIn("missing file", str(verifier.verify(self.manifest, self.root)["errors"]))

    def test_reject_path_traversal(self):
        self.write_manifest(path="../test.json")
        self.assertIn("traversal", str(verifier.verify(self.manifest, self.root)["errors"]))

    def test_reject_self_manifest(self):
        self.write_manifest(path="evidence/artifact-manifest.json")
        self.assertIn("self-referential",
                      str(verifier.verify(self.manifest, self.root)["errors"]))

    def test_reject_duplicate_paths(self):
        self.write_manifest()
        manifest = json.loads(self.manifest.read_text(encoding="utf-8"))
        manifest["files"].append(dict(manifest["files"][0]))
        self.manifest.write_text(json.dumps(manifest), encoding="utf-8")
        self.assertIn("duplicate", str(verifier.verify(self.manifest, self.root)["errors"]))

    def test_supports_legacy_artifacts_key(self):
        self.write_manifest()
        self.manifest.write_text(
            self.manifest.read_text(encoding="utf-8").replace('"files"', '"artifacts"'),
            encoding="utf-8",
        )
        self.assertEqual(verifier.verify(self.manifest, self.root)["failed"], 0)

    def test_rejects_dual_entry_list(self):
        self.write_manifest()
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        data["artifacts"] = data["files"]
        self.manifest.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "exactly one"):
            verifier.verify(self.manifest, self.root)


    def test_discovery_finds_later_manifest_and_checks_its_bytes(self):
        self.write_manifest()
        later = self.root / "evidence/2026-10-26/01-review/artifact-manifest.json"
        later.parent.mkdir(parents=True)
        later.write_text(json.dumps({"files": [{
            "path": "evidence/test.json",
            "bytes": self.payload.stat().st_size,
            "sha256": hashlib.sha256(self.payload.read_bytes()).hexdigest(),
        }]}), encoding="utf-8")
        result = verifier.verify_all(self.root)
        self.assertEqual(result["manifest_count"], 2)
        self.assertEqual(result["artifact_rows"], 2)
        self.assertEqual(result["failed"], 0)
        self.assertEqual(result["failed_manifests"], 0)

        # A newly discovered manifest must not be silently ignored by the
        # previously single-manifest CI entry point.
        later.write_text(json.dumps({"files": [{
            "path": "evidence/test.json",
            "bytes": self.payload.stat().st_size,
            "sha256": "0" * 64,
        }]}), encoding="utf-8")
        result = verifier.verify_all(self.root)
        self.assertEqual(result["manifest_count"], 2)
        self.assertEqual(result["failed_manifests"], 1)
        self.assertGreater(result["failed"], 0)
        self.assertTrue(any("SHA-256 mismatch" in " ".join(item["errors"])
                            for item in result["results"]))

    def test_all_manifest_discovery_fails_closed_on_empty_evidence(self):
        result = verifier.verify_all(self.root)
        self.assertEqual(result["manifest_count"], 0)
        self.assertNotEqual(result["failed"], 0)

    def test_all_manifest_discovery_does_not_edit_original_data(self):
        self.write_manifest()
        before = self.payload.read_bytes()
        manifest_before = self.manifest.read_bytes()
        verifier.verify_all(self.root)
        self.assertEqual(self.payload.read_bytes(), before)
        self.assertEqual(self.manifest.read_bytes(), manifest_before)


if __name__ == "__main__":
    unittest.main()
