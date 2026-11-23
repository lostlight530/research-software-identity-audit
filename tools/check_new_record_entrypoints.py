#!/usr/bin/env python3
"""PR-only, offline guard for newly introduced dated record entrypoints.

This narrow *new package* gate does not validate historic evidence, rewrite
older records, declare schedule offsets, or change the broad advisory suite.
"""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SHA_RE = re.compile(r"[0-9a-fA-F]{40}\Z")
DAY_RE = re.compile(r"\d{4}-\d{2}-\d{2}\Z")
EVENT_RE = re.compile(r"(0[1-9]|[1-9][0-9])-[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def dated_events(paths: set[str], top: str) -> set[str]:
    """Return canonical date/event pairs, not a count of arbitrary file paths."""
    found: set[str] = set()
    for path in paths:
        parts = path.split("/")
        if len(parts) < 4 or parts[0] != top:
            continue
        if not DAY_RE.fullmatch(parts[1]) or not EVENT_RE.fullmatch(parts[2]):
            continue
        try:
            date.fromisoformat(parts[1])
        except ValueError:
            continue
        found.add(f"{parts[1]}/{parts[2]}")
    return found


def check_new_events(base: set[str], head: set[str], index: str) -> dict:
    """Check only newly introduced dated packages, never old legacy folders."""
    base_monitoring = dated_events(base, "monitoring")
    head_monitoring = dated_events(head, "monitoring")
    new_monitoring = head_monitoring - base_monitoring
    new_evidence = dated_events(head, "evidence") - dated_events(base, "evidence")
    errors: list[str] = []
    for event in sorted(new_monitoring | new_evidence):
        monitoring_prefix = f"monitoring/{event}/"
        evidence_prefix = f"evidence/{event}/"
        if event in new_monitoring:
            if monitoring_prefix + "README.md" not in head:
                errors.append(f"{event}: missing monitoring README.md")
            record_paths = [monitoring_prefix + name for name in ("record.json", "record.yaml")]
            if sum(path in head for path in record_paths) != 1:
                errors.append(f"{event}: require exactly one monitoring record.json or record.yaml")
            if f"{event}/" not in index:
                errors.append(f"{event}: missing monitoring/README.md index reference")
        if event in new_evidence:
            if evidence_prefix + "README.md" not in head:
                errors.append(f"{event}: missing evidence README.md")
            if event not in head_monitoring:
                errors.append(f"{event}: evidence event lacks matching monitoring event")
    return {
        "mode": "pr_new_dated_record_entrypoints_only",
        "new_monitoring_events": sorted(new_monitoring),
        "new_evidence_events": sorted(new_evidence),
        "failed": len(errors),
        "errors": errors,
        "network_calls": 0,
        "existing_events_reclassified": 0,
        "scientific_interpretation_verified": False,
    }


def _tracked_paths(root: Path, *, base: str | None) -> set[str]:
    cmd = (
        ["git", "ls-tree", "-r", "--name-only", "-z", base, "--", "monitoring", "evidence"]
        if base else ["git", "ls-files", "-z", "--", "monitoring", "evidence"]
    )
    data = subprocess.run(cmd, cwd=root, check=True, capture_output=True).stdout
    return {path.decode("utf-8") for path in data.split(b"\0") if path}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="PR base commit SHA (40 hex digits)")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    if not SHA_RE.fullmatch(args.base):
        parser.error("--base must be an exact Git commit SHA")
    root = args.root.resolve()
    try:
        before = _tracked_paths(root, base=args.base)
        current = _tracked_paths(root, base=None)
        index = (root / "monitoring/README.md").read_text(encoding="utf-8")
        result = check_new_events(before, current, index)
    except (subprocess.CalledProcessError, OSError, UnicodeError) as exc:
        result = {
            "mode": "pr_new_dated_record_entrypoints_only",
            "failed": 1,
            "errors": [f"{type(exc).__name__}: {exc}"],
            "network_calls": 0,
        }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(bool(result["failed"]))


if __name__ == "__main__":
    raise SystemExit(main())
