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



def check_surface_id_reconciliation(event: Path, record: dict, root: Path = ROOT) -> list[str]:
    """Replay one explicitly derived surface-ID join against retained CSV inputs.

    Checks source Git-blob identity and row-level referential integrity, not
    original HTTP responses, platform freshness, or scientific truth.
    """
    errors: list[str] = []
    label = event.as_posix()
    if record.get("record_class") != (
        "retrospective_machine_column_semantics_reconciliation_not_new_platform_capture"
    ):
        return errors

    def error(message: str) -> None:
        errors.append(f"{label}: {message}")

    def input_file(key: str) -> Path | None:
        relative = record.get(key)
        if not isinstance(relative, str) or not relative.startswith("monitoring/"):
            error(f"{key} must name a monitored repository-relative file")
            return None
        path = (root / relative).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            error(f"{key} is missing or escapes the repository: {relative}")
            return None
        return path

    source = input_file("source_attempts_path")
    dictionary = input_file("source_results_path")
    output = event / "source-attempts-derived-surface-join.csv"
    if not output.is_file():
        error("derived join CSV missing")
        return errors
    if source is None or dictionary is None:
        return errors

    import hashlib

    for field, path in (("source_attempts_blob_sha", source),
                        ("source_results_blob_sha", dictionary)):
        raw = path.read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
        if record.get(field) != actual:
            error(f"{field} does not match retained Git blob bytes")

    try:
        def rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
            with path.open(encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)
                return list(reader.fieldnames or []), list(reader)

        raw_header, raw_rows = rows(source)
        lookup_header, lookup_rows = rows(dictionary)
        derived_header, derived_rows = rows(output)
    except (OSError, UnicodeError, csv.Error) as exc:
        error(f"CSV read failure: {exc}")
        return errors

    if not {"attempt_id", "platform"}.issubset(raw_header):
        error("source CSV must retain attempt_id and original numeric platform column")
        return errors
    if not {"surface", "name"}.issubset(lookup_header):
        error("surface dictionary must retain surface and name")
        return errors
    required = {
        "source_row_ordinal", "source_attempt_key", "original_platform_column_numeric_value",
        "derived_surface_id", "derived_surface_name", "operational_platform_if_core",
        "core_or_supplementary_class", "source_package_date_label",
        "derivation_provenance_class",
    }
    if not required.issubset(derived_header):
        error(f"derived join missing columns: {sorted(required - set(derived_header))}")
        return errors

    if len(raw_rows) != record.get("original_attempt_rows"):
        error("original_attempt_rows does not match retained source CSV")
    if len(lookup_rows) != record.get("surface_dictionary_rows"):
        error("surface_dictionary_rows does not match source dictionary")
    if len(derived_rows) != record.get("normalized_output_rows"):
        error("normalized_output_rows does not match derived CSV")
    if len(derived_rows) != len(raw_rows):
        error("derived row count differs from retained source attempts")

    dictionary_by_id: dict[str, str] = {}
    for entry in lookup_rows:
        ident, name = entry.get("surface"), entry.get("name")
        if not ident or not ident.isdecimal() or not name or ident in dictionary_by_id:
            error(f"invalid or duplicate source surface ID: {ident!r}")
        else:
            dictionary_by_id[ident] = name

    core_map = record.get("core_mapping")
    if not isinstance(core_map, dict) or set(core_map.values()) != {
        "github", "zenodo", "datacite", "orcid", "software_heritage", "openaire", "openalex"
    } or len(core_map) != 7:
        error("core_mapping must contain exactly seven distinct operational platforms")
        return errors

    counts: dict[str, int] = {}
    keys: set[str] = set()
    for ordinal, (src, derived) in enumerate(zip(raw_rows, derived_rows), 1):
        attempt, surface = src.get("attempt_id"), src.get("platform")
        if not attempt or attempt in keys:
            error(f"blank or duplicate retained attempt key at row {ordinal}")
        keys.add(attempt)
        counts[surface] = counts.get(surface, 0) + 1
        if surface not in dictionary_by_id:
            error(f"unknown original surface {surface!r} at row {ordinal}")
            continue
        core = core_map.get(surface, "")
        expected = {
            "source_row_ordinal": str(ordinal),
            "source_attempt_key": attempt,
            "original_platform_column_numeric_value": surface,
            "derived_surface_id": surface,
            "derived_surface_name": dictionary_by_id[surface],
            "operational_platform_if_core": core,
            "core_or_supplementary_class": (
                "CORE_PLATFORM_SURFACE_ONLY_NOT_A_NEW_UNIT"
                if core else "SUPPLEMENTARY_OR_STANDARDS_SURFACE"
            ),
            "source_package_date_label": record.get("source_package_date_label"),
            "derivation_provenance_class": (
                "DERIVED_FROM_EXISTING_PUBLIC_LEDGER_NOT_NEW_HTTP_REQUEST"
            ),
        }
        for field, value in expected.items():
            if derived.get(field) != value:
                error(f"derived row {ordinal} field {field} does not match source join")

    if record.get("source_surface_counts") != counts:
        error("source_surface_counts does not match retained source attempt frequencies")
    if record.get("distinct_attempt_keys") != len(keys):
        error("distinct_attempt_keys differs from retained source")
    if record.get("distinct_surface_ids_used") != len(counts):
        error("distinct_surface_ids_used differs from retained source")
    if (record.get("not_prospective") is not True
            or record.get("prospective_cells_added") != 0
            or record.get("new_http_requests_to_reconstruct_old_2026_11_02_attempts") != 0):
        error("derived reconciliation must not be labelled as prospective or a new capture")
    return errors


def check_bounded_surface_ledger(event: Path, record: dict) -> list[str]:
    """Check Nov-style selected-field surface ledgers against their own summaries.

    Source-level access errors remain errors, not evidence of absent resources.
    This checks only retained CSV/JSON consistency, not original HTTP transport
    authenticity, extractor freshness, or scientific validity.
    """
    if record.get("record_class") != "bounded_diagnostic_source_access_not_prospective":
        return []

    label = event.as_posix()
    errors: list[str] = []

    def error(reason: str) -> None:
        errors.append(f"{label}: {reason}")

    data = record.get("supplementary_surfaces")
    newer = isinstance(data, dict)
    if newer:
        count = data.get("attempt_count")
        extracted = data.get("extractor_representations")
        failures = data.get("errors")
        receipts = data.get("receipts")
        error_ids = data.get("error_surface_ids")
    else:
        count = record.get("surface_url_attempt_count")
        extracted = record.get("surface_extracted_representations")
        failures = record.get("surface_errors")
        receipts = record.get("receipt_ids")
        original_errors = record.get("error_rows")
        error_ids = ([x.get("id") for x in original_errors]
                     if isinstance(original_errors, list)
                     and all(isinstance(x, dict) for x in original_errors)
                     else None)

    if (type(count) is not int or count < 1
            or type(extracted) is not int or extracted < 0
            or type(failures) is not int or failures < 0
            or extracted + failures != count):
        error("invalid declared surface attempt/extraction/error totals")
        return errors
    if (not isinstance(receipts, list) or not receipts
            or not all(isinstance(x, str) and x for x in receipts)
            or len(set(receipts)) != len(receipts)):
        error("invalid or duplicate declared extractor receipts")
        return errors
    if (not isinstance(error_ids, list)
            or any(type(x) is not int for x in error_ids)
            or len(set(error_ids)) != failures):
        error("declared error surface IDs do not match error total")
        return errors

    contract = record.get("contract")
    if (not isinstance(contract, dict)
            or contract.get("prospective_cells_added") != 0
            or contract.get("prospective_dataset_member") is not False):
        error("diagnostic surface ledger cannot declare prospective observations")

    path = event / "surface-access-recheck.csv"
    if not path.is_file():
        error("surface-access-recheck.csv missing")
        return errors
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            required = {
                "surface_id", "surface_name", "exact_source_locator",
                "access_state", "extractor_acquired_at_utc_day",
                "error_type", "http_status_if_reported",
                "tool_receipt_id", "provenance_class",
            }
            if not required.issubset(reader.fieldnames or []):
                error(f"surface ledger missing columns: {sorted(required - set(reader.fieldnames or []))}")
                return errors
            rows = list(reader)
            has_client_clock = "client_batch_started_utc" in (reader.fieldnames or [])
            if has_client_clock != ("client_batch_finished_utc" in (reader.fieldnames or [])):
                error("client batch clock columns must appear together")
                return errors
    except (OSError, UnicodeError, csv.Error) as exc:
        error(f"surface ledger unreadable: {exc}")
        return errors

    if len(rows) != count:
        error(f"declared surface attempt count {count} != CSV rows {len(rows)}")

    found_errors: set[int] = set()
    found_ids: list[int] = []
    found_receipts: set[str] = set()
    success_count = 0
    current_day = record.get("logical_date")
    try:
        current_date = date.fromisoformat(current_day)
    except (TypeError, ValueError):
        error("missing or invalid logical_date")
        current_date = None
    daily_counts = {"current": 0, "previous": 0, "older": 0}
    batch_pairs = data.get("batch_window_utc") if newer else None
    receipt_pairs: dict[str, tuple[datetime, datetime]] = {}
    if has_client_clock:
        if (not isinstance(batch_pairs, list)
                or len(batch_pairs) != len(receipts)):
            error("client batch window/receipt length mismatch")
        else:
            for receipt, pair in zip(receipts, batch_pairs):
                if not isinstance(pair, list) or len(pair) != 2:
                    error("invalid declared client batch window")
                    continue
                start, end = _aware_clock(pair[0]), _aware_clock(pair[1])
                if start is None or end is None or end < start:
                    error("invalid or unordered declared client batch window")
                else:
                    receipt_pairs[receipt] = (start, end)

    for n, row in enumerate(rows, 2):
        if None in row:
            error(f"extra CSV fields at row {n}")
        ident = row.get("surface_id", "")
        if not isinstance(ident, str) or not ident.isdecimal():
            error(f"invalid surface ID at row {n}")
            continue
        sid = int(ident)
        found_ids.append(sid)
        if (not row.get("surface_name") or
                not str(row.get("exact_source_locator", "")).startswith(("https://", "http://")) or
                not row.get("provenance_class")):
            error(f"missing surface name/source/provenance at ID {sid}")
        receipt = row.get("tool_receipt_id", "")
        if receipt:
            found_receipts.add(receipt)
        state = row.get("access_state")
        if state == "ERROR":
            found_errors.add(sid)
            if not row.get("error_type"):
                error(f"ERROR without error_type for surface {sid}")
            if row.get("extractor_acquired_at_utc_day"):
                error(f"ERROR with extracted acquisition day for surface {sid}")
        elif state == "EXTRACTED":
            success_count += 1
            if row.get("error_type"):
                error(f"EXTRACTED with error_type for surface {sid}")
            value = row.get("extractor_acquired_at_utc_day", "")
            if (not isinstance(value, str)
                    or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T00:00:00Z", value)):
                error(f"invalid extractor UTC-day acquisition label for surface {sid}")
            else:
                acquired = _aware_clock(value)
                if acquired is None:
                    error(f"invalid extractor acquisition date for surface {sid}")
                elif current_date is not None:
                    day = acquired.date()
                    if day == current_date:
                        daily_counts["current"] += 1
                    elif day == current_date.fromordinal(current_date.toordinal() - 1):
                        daily_counts["previous"] += 1
                    else:
                        daily_counts["older"] += 1
        else:
            error(f"invalid access_state {state!r} at surface {sid}")

        if has_client_clock:
            start = _aware_clock(row.get("client_batch_started_utc"))
            end = _aware_clock(row.get("client_batch_finished_utc"))
            if start is None or end is None or end < start:
                error(f"invalid or unordered row client batch clock for surface {sid}")
            elif receipt not in receipt_pairs or (start, end) != receipt_pairs[receipt]:
                error(f"row client batch clock/receipt mismatch for surface {sid}")

    if found_ids != list(range(1, count + 1)):
        error("surface IDs must enumerate 1..attempt_count in order")
    if found_errors != set(error_ids):
        error("CSV error surface IDs differ from machine summary")
    if success_count != extracted or len(found_errors) != failures:
        error("CSV extracted/error state counts differ from machine summary")
    if found_receipts != set(receipts):
        error("CSV extractor receipts differ from machine summary")

    if newer:
        # Forward-compatible, date-neutral buckets for monitoring after Nov 5.
        # Historical records retain their original date-named fields below.
        buckets = data.get("acquisition_day_bucket_counts")
        if buckets is not None:
            expected = {
                "logical_utc_day": daily_counts["current"],
                "previous_utc_day": daily_counts["previous"],
                "older_utc_day": daily_counts["older"],
            }
            if (not isinstance(buckets, dict)
                    or set(buckets) != set(expected)
                    or any(type(v) is not int for v in buckets.values())
                    or buckets != expected):
                error("acquisition_day_bucket_counts differs from CSV UTC-day rows")
        for key, label_key in (
            ("acquired_utc_day_nov5_count", "current"),
            ("acquired_utc_day_nov4_count", "previous"),
            ("older_acquisition_count", "older"),
        ):
            # These dated keys are legacy report fields, not a generic date schema.
            if key in data and data[key] != daily_counts[label_key]:
                error(f"{key} differs from CSV acquisition-day rows")
    else:
        if (current_date is not None
                and "utc_day_2026_11_04_extractor_acquired_surface_ids" in record):
            actual = {
                int(row["surface_id"]) for row in rows
                if row.get("extractor_acquired_at_utc_day") == "2026-11-04T00:00:00Z"
                and str(row.get("surface_id", "")).isdecimal()
            }
            if actual != set(record["utc_day_2026_11_04_extractor_acquired_surface_ids"]):
                error("declared Nov 4 UTC-day surface IDs differ from CSV")
        start = _aware_clock(record.get("surface_batch_client_started_utc"))
        end = _aware_clock(record.get("surface_batch_client_finished_utc"))
        if start is None or end is None or end < start:
            error("invalid or unordered declared surface client batch envelope")

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
                if isinstance(parsed, dict):
                    errors.extend(check_surface_id_reconciliation(event, parsed))
                    errors.extend(check_bounded_surface_ledger(event, parsed))
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
