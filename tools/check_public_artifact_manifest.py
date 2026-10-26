#!/usr/bin/env python3
"""Verify byte-level Git-tracked public artifact manifests without touching source files.

The manifest describes *published artifact bytes* only. It never proves that a
third-party HTTP response was authentic, current, complete, or locally replayed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ("evidence/2026-10-25/02-independent-institutional-recheck/"
           "artifact-manifest.json")


def verify(manifest_path: Path, root: Path = ROOT) -> dict:
    root = root.resolve()
    manifest_path = manifest_path.resolve()
    if not manifest_path.is_relative_to(root):
        raise ValueError("manifest outside repository root")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    # Historical manifests use 'artifacts', while newer projections use 'files'.
    if ("files" in manifest) == ("artifacts" in manifest):
        raise ValueError("expected exactly one of files/artifacts")
    rows = manifest.get("files", manifest.get("artifacts"))
    if not isinstance(rows, list) or not rows:
        raise ValueError("manifest requires a nonempty artifact list")
    seen: set[str] = set()
    errors: list[str] = []
    for i, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            errors.append(f"row {i}: not an object")
            continue
        rel, expected_bytes, expected_hash = (
            row.get("path"), row.get("bytes"), row.get("sha256")
        )
        if not isinstance(rel, str) or not rel or "\\" in rel:
            errors.append(f"row {i}: invalid relative path")
            continue
        relative = Path(rel)
        if relative.is_absolute() or ".." in relative.parts or relative.as_posix() != rel:
            errors.append(f"row {i}: invalid path traversal/normalization")
            continue
        if rel in seen:
            errors.append(f"row {i}: duplicate path {rel}")
            continue
        seen.add(rel)
        resolved = (root / relative).resolve()
        if not resolved.is_relative_to(root) or resolved == manifest_path:
            errors.append(f"row {i}: external or self-referential artifact {rel}")
            continue
        if not isinstance(expected_bytes, int) or isinstance(expected_bytes, bool) or expected_bytes < 0:
            errors.append(f"row {i}: invalid byte length for {rel}")
            continue
        if not isinstance(expected_hash, str) or len(expected_hash) != 64 or any(
            char not in "0123456789abcdef" for char in expected_hash
        ):
            errors.append(f"row {i}: invalid lowercase SHA-256 for {rel}")
            continue
        if not resolved.is_file():
            errors.append(f"row {i}: missing file {rel}")
            continue
        # Stream large evidence bundles; never load or execute archived members.
        size, digest = 0, hashlib.sha256()
        with resolved.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                size += len(block)
                digest.update(block)
        if size != expected_bytes:
            errors.append(f"row {i}: byte length mismatch {rel}: {size} != {expected_bytes}")
        if digest.hexdigest() != expected_hash:
            errors.append(f"row {i}: SHA-256 mismatch {rel}")
    return {
        "manifest": manifest_path.relative_to(root).as_posix(),
        "artifact_rows": len(rows),
        "unique_paths": len(seen),
        "failed": len(errors),
        "errors": errors,
        "scope": "published file integrity only; not source authenticity",
    }



def discover_manifests(root: Path = ROOT) -> list[Path]:
    """Discover dated published-artifact manifests without relying on one cutoff day."""
    return sorted((root.resolve() / "evidence").rglob("artifact-manifest.json"))


def verify_all(root: Path = ROOT) -> dict:
    """Read-only integrity check of every discovered public artifact manifest."""
    root = root.resolve()
    paths = discover_manifests(root)
    if not paths:
        return {
            "mode": "all",
            "manifest_count": 0,
            "artifact_rows": 0,
            "failed_manifests": 0,
            "failed": 1,
            "errors": ["no evidence artifact manifests discovered"],
            "results": [],
            "scope": "published file integrity only; not source authenticity",
        }
    results = []
    for path in paths:
        try:
            result = verify(path, root)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            result = {
                "manifest": path.relative_to(root).as_posix(),
                "artifact_rows": 0,
                "failed": 1,
                "errors": [str(exc)],
            }
        results.append(result)
    return {
        "mode": "all",
        "manifest_count": len(paths),
        "artifact_rows": sum(item.get("artifact_rows", 0) for item in results),
        "failed_manifests": sum(bool(item["failed"]) for item in results),
        "failed": sum(item["failed"] for item in results),
        "results": results,
        "scope": "published file integrity only; not source authenticity",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    selector = parser.add_mutually_exclusive_group()
    selector.add_argument("--manifest", default=None,
                          help="One repository-relative artifact manifest (default: October 25)")
    selector.add_argument("--all", action="store_true",
                          help="Verify all evidence/**/artifact-manifest.json files")
    args = parser.parse_args()
    if args.all:
        result = verify_all(ROOT)
    else:
        selected = args.manifest or DEFAULT
        try:
            result = verify(ROOT / selected)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            result = {"manifest": selected, "failed": 1, "errors": [str(exc)]}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return int(result["failed"] != 0)


if __name__ == "__main__":
    raise SystemExit(main())
