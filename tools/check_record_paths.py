"""Read-only repository path/ownership check for dated RSIA records.

Validates presentation envelopes and navigation only: it does not inspect
external sources, certify a historical claim, or create prospective cells.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}$")
EVENT_RE = re.compile(r"(\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)$")
MONITORING = ROOT / "monitoring"
EVIDENCE = ROOT / "evidence"
OFFLINE_ONLY_EVENTS = {"2026-10-24/03-offline-family-stat-replay"}


def valid_date(s: str) -> bool:
    try:
        return bool(DATE_RE.fullmatch(s) and date.fromisoformat(s).isoformat() == s)
    except ValueError:
        return False


def scan(base: Path, errors: list[str]) -> list[Path]:
    events: list[Path] = []
    for folder in sorted(base.iterdir()):
        if not folder.is_dir() or not valid_date(folder.name):
            # monitoring/coverage is documentary indexing, not a dated event.
            if folder.is_dir() and folder.name not in ({"coverage"} if base == MONITORING else set()):
                errors.append(f"Undeclared non-date event directory: {folder.relative_to(ROOT)}")
            continue
        for event in sorted(folder.iterdir()):
            if not event.is_dir():
                errors.append(f"Loose file inside date folder: {event.relative_to(ROOT)}")
                continue
            match = EVENT_RE.fullmatch(event.name)
            if not match or int(match.group(1)) == 0:
                errors.append(f"Invalid event ordinal or kebab name: {event.relative_to(ROOT)}")
                continue
            if not (event / "README.md").is_file():
                errors.append(f"Missing record entrypoint: {event.relative_to(ROOT)}")
            events.append(event)
    return events


def check() -> dict:
    errors: list[str] = []
    monitoring = scan(MONITORING, errors)
    evidence = scan(EVIDENCE, errors)
    index = (MONITORING / "README.md").read_text(encoding="utf-8")
    monitored = {x.relative_to(MONITORING).as_posix() for x in monitoring}
    yaml_count = json_count = offline_count = 0

    dates = sorted({p.parts[-2] for p in monitoring})
    for dt in dates:
        ordinals = sorted(int(p.name[:2]) for p in monitoring if p.parts[-2] == dt)
        if ordinals != list(range(1, len(ordinals) + 1)):
            errors.append(f"Monitoring event numbering not consecutive on {dt}: {ordinals}")

    for event in monitoring:
        rel = event.relative_to(MONITORING).as_posix()
        if rel + "/" not in index:
            errors.append(f"Missing monitoring index reference: {rel}")
        yaml = (event / "record.yaml").is_file()
        jsn = (event / "record.json").is_file()
        if yaml and jsn:
            errors.append(f"Competing machine record formats in one event: {rel}")
        elif yaml:
            yaml_count += 1
        elif jsn:
            json_count += 1
            try:
                json.loads((event / "record.json").read_text(encoding="utf-8"))
            except (ValueError, UnicodeError) as e:
                errors.append(f"Malformed machine JSON record in {rel}: {e}")
        elif rel in OFFLINE_ONLY_EVENTS:
            offline_count += 1
        else:
            errors.append(f"Missing record.yaml / record.json in monitoring: {rel}")

    orphan_evidence = []
    for event in evidence:
        rel = event.relative_to(EVIDENCE).as_posix()
        if rel not in monitored:
            orphan_evidence.append(rel)
            errors.append(f"Evidence does not match a monitoring event identity: {rel}")

    # New navigation files must resolve within the checked-out repository.
    new_readmes = [
        MONITORING / "2026-10-06/01-wave-01/README.md",
        MONITORING / "2026-10-06/02-openaire-link-attempt/README.md",
        MONITORING / "2026-10-06/03-reconciliation/README.md",
        EVIDENCE / "2026-10-10/01-zenodo-surge-recheck/README.md",
    ]
    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for doc in new_readmes:
        for link in link_pattern.findall(doc.read_text(encoding="utf-8")):
            url = link.split("#", 1)[0]
            if not url or url.startswith(("https://", "http://", "mailto:")):
                continue
            resolved = (doc.parent / url).resolve()
            if not resolved.is_relative_to(ROOT.resolve()) or not resolved.exists():
                errors.append(f"Broken new entrypoint link: {doc.relative_to(ROOT)} -> {url}")

    return {
        "mode": "offline_path_and_ownership_check",
        "monitoring_event_directories": len(monitoring),
        "evidence_companion_directories": len(evidence),
        "monitoring_yaml_records": yaml_count,
        "monitoring_json_records": json_count,
        "offline_only_events_without_machine_record": offline_count,
        "missing_entrypoints": sum("Missing record entrypoint" in x for x in errors),
        "orphan_evidence": orphan_evidence,
        "errors": errors,
        "failed": len(errors),
        "network_calls": 0,
        "new_prospective_cells": 0,
        "scientific_interpretation_verified": False,
    }


if __name__ == "__main__":
    try:
        result = check()
    except Exception as exc:
        result = {"mode": "offline_path_and_ownership_check",
                  "failed": 1,
                  "errors": [f"{type(exc).__name__}: {exc}"],
                  "network_calls": 0, "new_prospective_cells": 0,
                  "scientific_interpretation_verified": False}
    print(json.dumps(result, indent=2))
    sys.exit(bool(result["failed"]))
