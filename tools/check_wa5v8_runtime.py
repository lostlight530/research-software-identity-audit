#!/usr/bin/env python3
"""Offline guard for the wa5v8 relocation, not a scientific validation."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "studies/osf-wa5v8"

def blob(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()

def main():
    manifest = json.loads((PROJECT / "path-migration-2026-11-25.json").read_text(encoding="utf-8"))
    records = manifest["records"]
    errors = []
    if (manifest.get("reporting_timezone") != "America/Los_Angeles" or
            [manifest.get(f"day{i}_reporting_date") for i in range(3)] !=
            ["2026-11-23", "2026-11-24", "2026-11-25"]):
        errors.append("incorrect Pacific reporting calendar")
    if len(records) != 13 or len({r["old_path"] for r in records}) != 13:
        errors.append("relocation inventory must retain exactly 13 distinct original paths")
    for row in records:
        old, new = row["old_path"], row["new_path"]
        if not old.startswith(("monitoring/2026-11-24/", "evidence/2026-11-24/")) or new != "studies/osf-wa5v8/day0/" + old:
            errors.append(f"unexpected relocation scope: {old}")
            continue
        if (ROOT / old).exists():
            errors.append(f"duplicate active old path: {old}")
        path = ROOT / new
        if not path.is_file() or blob(path) != row["relocated_git_blob_sha"]:
            errors.append(f"relocated file missing or changed: {new}")
        if old.endswith(".jsonl") and (row["disposition"] != "byte_preserved" or row["original_git_blob_sha"] != row["relocated_git_blob_sha"]):
            errors.append(f"source ledger identity changed: {old}")
    day1 = json.loads((PROJECT / "day1/contract/record.json").read_text(encoding="utf-8"))
    if day1.get("source_commit") != "c84a738a6fbf7b4ed96feeaada5158f6c9bb3a3e" or day1.get("source_pr") != 147 or day1.get("reporting_date") != "2026-11-24":
        errors.append("incorrect Day 1 contract source identity")
    moved = [r for r in day1["records"] if r["disposition"] == "physically_relocated_byte_identical"]
    if len(moved) != 1 or moved[0]["source_path"] != "contract/osf-approved-revision-2026-11-18.md" or moved[0]["current_path"] != "studies/osf-wa5v8/day1/contract/osf-approved-revision-2026-11-18.md":
        errors.append("incorrect Day 1 contract relocation")
    else:
        row = moved[0]
        path = ROOT / row["current_path"]
        if (ROOT / row["source_path"]).exists() or not path.is_file() or blob(path) != row["source_git_blob_sha"]:
            errors.append("Day 1 contract relocation lost original identity or duplicated old path")
    if len(day1["records"]) != 5 or day1.get("prospective_cells_added") != 0:
        errors.append("incorrect Day 1 contract scope")
    if not (PROJECT / "day1/README.md").is_file():
        errors.append("missing Day 1 navigation")
    print(json.dumps({"relocated_files": len(records), "source_ledgers": sum(r["old_path"].endswith(".jsonl") for r in records), "errors": errors, "scientific_interpretation_verified": False}, indent=2))
    return int(bool(errors))

if __name__ == "__main__":
    raise SystemExit(main())
