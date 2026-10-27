"""Read-only repository path/ownership check for dated RSIA records.

Validates presentation envelopes and navigation only: it does not inspect
external sources, certify a historical claim, or create prospective cells.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}$")
EVENT_RE = re.compile(r"(\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)$")
MONITORING = ROOT / "monitoring"
EVIDENCE = ROOT / "evidence"
OFFLINE_ONLY_EVENTS = {"2026-10-24/03-offline-family-stat-replay"}



def _aware_clock(raw: object) -> datetime | None:
    """Parse a timestamp with an explicit UTC offset, rejecting naive clocks."""
    if not isinstance(raw, str):
        return None
    try:
        value = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        return value if value.utcoffset() is not None else None
    except ValueError:
        return None


def check_projection_ledger(event: Path, record: dict) -> list[str]:
    """Check local summary/CSV consistency, never origin response authenticity.

    Opt-in: earlier monitoring records with other schemas are not reclassified.
    A batch envelope is not an individual request time.
    """
    if "source_attempt_rows" not in record:
        if record.get("record_class") == "diagnostic_monitoring_selected_public_fields":
            return [f"{event.as_posix()}: diagnostic projection missing source_attempt_rows"]
        return []

    errors: list[str] = []
    label = event.as_posix()
    expected = record["source_attempt_rows"]
    if type(expected) is not int or expected < 0:
        errors.append(f"{label}: source_attempt_rows must be a nonnegative integer")
        return errors

    ledger = event / "source-attempts.csv"
    if not ledger.is_file():
        return [f"{label}: source_attempt_rows declared but source-attempts.csv missing"]

    required = {
        "attempt_id", "platform", "scope", "locator",
        "retrieval_batch_start_utc", "retrieval_batch_end_utc",
    }
    try:
        with ledger.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            absent = required - set(reader.fieldnames or [])
            if absent:
                return [f"{label}: source-attempts.csv missing columns: {sorted(absent)}"]
            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        return [f"{label}: source-attempts.csv unreadable: {exc}"]

    if len(rows) != expected:
        errors.append(
            f"{label}: source_attempt_rows={expected} but ledger has {len(rows)} rows"
        )

    start = _aware_clock(record.get("batch_start_utc"))
    end = _aware_clock(record.get("batch_end_utc"))
    if start is None or end is None or end < start:
        errors.append(f"{label}: invalid or unordered record batch envelope")

    ids: set[str] = set()
    for number, row in enumerate(rows, 2):
        if None in row:
            errors.append(f"{label}: malformed extra CSV fields on row {number}")
        if any(not isinstance(row.get(col), str) or not row[col].strip()
               for col in required):
            errors.append(f"{label}: missing required CSV field on row {number}")
            continue
        identifier = row["attempt_id"]
        if identifier in ids:
            errors.append(f"{label}: duplicate attempt_id {identifier!r}")
        ids.add(identifier)
        row_start = _aware_clock(row["retrieval_batch_start_utc"])
        row_end = _aware_clock(row["retrieval_batch_end_utc"])
        if row_start is None or row_end is None or row_end < row_start:
            errors.append(f"{label}: invalid or unordered row batch clock {identifier}")
        elif start is not None and end is not None and (
            row_start < start or row_end > end
        ):
            errors.append(f"{label}: row batch outside record envelope {identifier}")

    if (record.get("record_class", "").startswith("diagnostic")
            and (record.get("prospective_dataset_member") is not False
                 or record.get("prospective_cells_added") != 0)):
        errors.append(f"{label}: diagnostic projection may not declare prospective cells")
    return errors


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
    projection_records_checked = projection_rows_declared = 0

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
                parsed = json.loads((event / "record.json").read_text(encoding="utf-8"))
                if isinstance(parsed, dict) and "source_attempt_rows" in parsed:
                    projection_records_checked += 1
                    if type(parsed["source_attempt_rows"]) is int:
                        projection_rows_declared += parsed["source_attempt_rows"]
                    errors.extend(check_projection_ledger(event, parsed))
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
        "projection_records_checked": projection_records_checked,
        "projection_rows_declared": projection_rows_declared,
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
