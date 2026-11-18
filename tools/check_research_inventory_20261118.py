#!/usr/bin/env python3
"""Verify the pinned 2026-11-18 repository path/blob classification snapshot.

Pure stdlib, offline, read-only. Validates internal bookkeeping of a *dated
historical Git tree*, NOT original HTTP authenticity, historical retrievability,
or eligible preregistered timepoints. Later commits may modify those files
without retroactively changing the pinned snapshot.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = "docs/repository-inventory/2026-11-18"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or len(set(reader.fieldnames)) != len(reader.fieldnames):
            raise ValueError(f"bad CSV header: {path}")
        rows = list(reader)
    if any(None in row for row in rows):
        raise ValueError(f"extra CSV columns: {path}")
    return rows


def validate(root: Path = ROOT) -> list[str]:
    d = root / INVENTORY
    errors: list[str] = []
    try:
        snap = json.loads((d / "snapshot.json").read_text(encoding="utf-8"))
        files = read_csv(d / "tracked-file-classification.csv")
        events = read_csv(d / "dated-event-catalog.csv")
        calendar = read_csv(d / "first-day-through-nov18-calendar.csv")
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        return [f"missing or unparsable inventory: {type(exc).__name__}: {exc}"]

    if snap.get("record_class") != "repository_tree_snapshot_path_and_blob_inventory_not_prospective":
        errors.append("snapshot class is not a path-only historical inventory")
    if not re.fullmatch(r"[0-9a-f]{40}", str(snap.get("snapshot_main_sha", ""))):
        errors.append("invalid pinned source main SHA")
    if snap.get("tracked_blob_rows") != len(files):
        errors.append("tracked_blob_rows differs from CSV file count")
    if snap.get("dated_event_directories") != len(events):
        errors.append("dated event directory count differs from CSV")
    if snap.get("days_in_calendar") != len(calendar):
        errors.append("calendar row count differs from pinned snapshot")
    contract = snap.get("contract", {})
    for key, value in {
        "fixed_objects": 10, "layers": 6, "units_per_eligible_timepoint": 60,
        "operational_platforms": 7, "possible_checks_not_units": 70,
        "new_prospective_cells": 0, "control_is_rs11": False,
    }.items():
        if contract.get(key) != value or type(contract.get(key)) is not type(value):
            errors.append(f"frozen analytical boundary changed: {key}")
    paths: set[str] = set()
    planes = Counter()
    roles = Counter()
    observed: dict[str, dict[str, object]] = {}
    for line, row in enumerate(files, 2):
        p = row.get("source_path", "")
        if not p or p in paths or p.startswith("/") or "\\x00" in p or ".." in Path(p).parts:
            errors.append(f"duplicate/unsafe source path on row {line}: {p!r}")
        paths.add(p)
        if not re.fullmatch(r"[0-9a-f]{40}", row.get("source_git_blob_sha", "")):
            errors.append(f"invalid original Git blob SHA at {p}")
        if not str(row.get("bytes", "")).isdecimal():
            errors.append(f"missing/invalid Git blob length at {p}")
        if row.get("verification_scope") != "PATH_BLOB_ONLY_NOT_SOURCE_REVALIDATION":
            errors.append(f"source verification overclaim at {p}")
        category, role = row.get("classification_plane", ""), row.get("file_role", "")
        if not category or not role:
            errors.append(f"missing classification role at {p}")
        planes[category] += 1
        roles[role] += 1
        if re.match(r"^(monitoring|evidence)/\\d{4}-\\d{2}-\\d{2}/\\d{2}-", p):
            if row.get("rename_or_alias_action") not in {
                "PRESERVE_HISTORICAL_PATH_BLOB", "PRE_ELIGIBILITY_DIAGNOSTIC_ALIAS"
            }:
                errors.append(f"unjustified historical path rename at {p}")
            m = re.match(r"^((?:monitoring|evidence)/\\d{4}-\\d{2}-\\d{2}/\\d{2}-[^/]+)/(.+)$", p)
            if m:
                event = m.group(1)
                drow = observed.setdefault(event, {"count": 0, "readme": False, "yaml": False, "json": False})
                drow["count"] += 1
                drow["readme"] |= m.group(2) == "README.md"
                drow["yaml"] |= m.group(2) == "record.yaml"
                drow["json"] |= m.group(2) == "record.json"
    if dict(planes) != snap.get("planes"):
        errors.append("file classification_plane frequencies drift from snapshot")
    if dict(roles) != snap.get("roles"):
        errors.append("file_role frequencies drift from snapshot")
    indexed: set[str] = set()
    for row in events:
        p = row.get("event_dir", "")
        if p in indexed or p not in observed:
            errors.append(f"duplicate or ungrounded event directory: {p}")
            continue
        indexed.add(p)
        original = observed[p]
        if row.get("file_count") != str(original["count"]):
            errors.append(f"event file count drift: {p}")
        if row.get("readme_present") != ("YES" if original["readme"] else "NO"):
            errors.append(f"event README mismatch: {p}")
        format_ = "CONFLICT" if original["yaml"] and original["json"] else (
            "record.yaml" if original["yaml"] else "record.json" if original["json"] else "NONE"
        )
        if row.get("machine_record_variant") != format_:
            errors.append(f"event record variant mismatch: {p}")
        if row.get("prospective_claim") != "NOT_ASSERTED":
            errors.append(f"prospective promotion from path-only inventory: {p}")
    if indexed != set(observed):
        errors.append("event catalogue does not cover every dated source directory")
    if len(calendar) != 45:
        errors.append("calendar does not cover 2026-10-05 to 2026-11-18 inclusive")
    d0 = date(2026, 10, 5)
    for i, row in enumerate(calendar):
        current = (d0 + timedelta(days=i)).isoformat()
        if row.get("date_asia_shanghai_label") != current:
            errors.append(f"calendar date missing/misordered at row {i+2}")
        n = sum(x.startswith("monitoring/" + current + "/") for x in indexed)
        if row.get("monitoring_event_dirs") != str(n):
            errors.append(f"calendar event count mismatch for {current}")
        if row.get("interpretation_limit") != "NO_DIRECTORY_DOES_NOT_ESTABLISH_A_MISSED_SCHEDULED_POINT":
            errors.append(f"calendar overclaims missing scheduled timepoint at {current}")
    return errors


if __name__ == "__main__":
    results = validate()
    print(json.dumps({
        "check": "PINNED_PATH_CLASSIFICATION_ONLY",
        "errors": results,
        "passed": not results,
        "provider_byte_authenticity_verified": False,
        "new_prospective_cells": 0,
    }, ensure_ascii=False, indent=2))
    sys.exit(bool(results))
