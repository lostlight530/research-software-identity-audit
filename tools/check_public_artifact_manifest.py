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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", default=DEFAULT,
                        help="Repository-relative artifact manifest (no rewriting)")
    args = parser.parse_args()
    try:
        result = verify(ROOT / args.manifest)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        result = {"manifest": args.manifest, "failed": 1, "errors": [str(exc)]}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return int(result["failed"] != 0)


if __name__ == "__main__":
    raise SystemExit(main())
