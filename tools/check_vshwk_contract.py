#!/usr/bin/env python3
"""Offline structural and provenance validator for the independent OSF VSHWK study."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
STUDY_REL = Path("studies/osf-vshwk")
EXPECTED_RESPONSE = "6afdcc7108de91a0f0cefd6c"
EXPECTED_LAYER_COUNTS = {
    "L1_source_repository": 4, "L2_workflow_registry": 3,
    "L3_archival_repository": 2, "L4_identifier_registration_resolution": 4,
    "L5_source_preservation": 2, "L6_testing_monitoring_execution": 2,
    "L7_researcher_attribution": 1, "L8_discovery_aggregation": 4,
}
EXPECTED_DESCRIPTION = """This study examines how a publicly documented open research workflow is represented, linked, versioned, and monitored across independently operated scholarly infrastructures.

The focal case is the Life Science Knowledge Workflow, associated with WorkflowHub record 2347, version 2.

The study examines eight predefined infrastructure layers: source repositories, workflow registries, archival repositories, identifier registration and resolution services, source-preservation services, workflow testing and monitoring services, researcher-attribution services, and scholarly discovery and aggregation services.

Records will be included only when exact identifiers or documented provenance relationships support their association with the focal workflow. Independent software assets within the same research ecosystem will not automatically be treated as components of the focal workflow.

The research adopts a longitudinal descriptive observational case-study design. It separates historical evidence from three prospective observation waves and examines workflow identity, version lineage, metadata consistency, provenance relationships, timestamped changes, infrastructure states, and unresolved cross-platform discrepancies.

The expected outcomes are a reproducible cross-infrastructure evidence map, a timestamped record of observable identity and metadata changes, and a bounded assessment of the capabilities and limitations of existing scholarly infrastructure.

The study does not infer causal relationships or claim that registration, archival availability, passing tests, researcher attribution, or public discovery independently establish scientific validity, institutional endorsement, adoption, or universal reproducibility."""


class ContractError(AssertionError):
    pass


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ContractError(f"{path}: invalid JSON: {exc}") from exc


def read_jsonl(path: Path):
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except Exception as exc:
            raise ContractError(f"{path}:{line_no}: invalid JSONL row: {exc}") from exc
    return rows


def clock(value: str, field: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{field}: timestamp required")
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError as exc:
        raise ContractError(f"{field}: invalid ISO-8601 timestamp {value!r}") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ContractError(f"{field}: timezone offset required")
    return parsed


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def validate(root: Path = ROOT) -> dict:
    study = root / STUDY_REL
    manifest = read_json(study / "contract/endpoints-v1.json")
    authority = manifest.get("authority", {})
    need(authority.get("registration_id") == "vshwk", "manifest authority must be OSF VSHWK")
    need(authority.get("latest_approved_response_id") == EXPECTED_RESPONSE,
         "manifest does not reference the approved VSHWK response")
    need(authority.get("reviews_state") == "approved", "VSHWK amendment is not marked approved")

    case = manifest.get("study_case", {})
    need(case.get("project_id") == 490, "current case must be WorkflowHub Project 490")
    need(case.get("independent_sample_count") == 1, "project-level independent sample count must be one")
    need(case.get("project_level_bundle_count_per_complete_cycle") == 8,
         "one project × eight layers must yield eight project-layer bundles")
    need(case.get("nested_lineage_bundle_count_per_complete_cycle") == 16,
         "two lineages × eight layers must yield sixteen nested bundles")
    expected_lineages = {
        "A": (2332, "welcome-to-github", "10.48546/workflowhub.workflow.2332.9"),
        "B": (2334, "zero-entropy-lab", "10.48546/workflowhub.workflow.2334.9"),
    }
    lineages = {x.get("id"): x for x in case.get("lineages", [])}
    need(set(lineages) == set(expected_lineages), "manifest must contain exactly lineages A and B")
    for key, (record, repo, doi) in expected_lineages.items():
        item = lineages[key]
        need((item.get("record"), item.get("repo"), item.get("doi")) == (record, repo, doi),
             f"lineage {key} identity anchor drifted")

    endpoints = manifest.get("endpoint_manifest", [])
    endpoint_ids = [x.get("endpoint_id") for x in endpoints]
    need(len(endpoint_ids) == manifest.get("coverage", {}).get("endpoints") == 22,
         "manifest v1 must declare exactly 22 endpoint locators")
    need(len(endpoint_ids) == len(set(endpoint_ids)), "manifest endpoint IDs must be unique")
    need(dict(Counter(x.get("layer") for x in endpoints)) == EXPECTED_LAYER_COUNTS,
         "manifest v1 eight-layer endpoint allocation drifted")
    need(manifest.get("coverage", {}).get("by_layer") == EXPECTED_LAYER_COUNTS,
         "manifest coverage.by_layer differs from endpoint rows")

    desc = (study / "public-project-description.md").read_text(encoding="utf-8").rstrip("\n")
    need(desc == EXPECTED_DESCRIPTION, "AUHJF Project Description mirror differs from owner-confirmed text")
    entry = (study / "README.md").read_text(encoding="utf-8")
    need("current VSHWK protocol authority" in entry and "project-level text" in entry,
         "Study 2 entrypoint must distinguish public Description from current protocol authority")
    need(EXPECTED_RESPONSE in entry, "Study 2 entrypoint must cite the approved response")
    crosswalk_path = study / "contract/endpoint-scope-crosswalk.md"
    need(crosswalk_path.is_file(), "missing endpoint scope crosswalk")
    crosswalk_text = crosswalk_path.read_text(encoding="utf-8")
    for required_surface in (
        "WorkflowHub-displayed testing metadata",
        "WorkflowHub creator information",
        "Research Software Directory",
        "nfdi.software",
    ):
        need(required_surface in crosswalk_text,
             f"scope crosswalk missing approved surface: {required_surface}")
    need((study / "cycles/record-template.md").is_file(), "missing cycle record template")

    cycle_dirs = sorted(p for p in (study / "cycles").glob("cycle-*") if p.is_dir())
    need(bool(cycle_dirs), "no VSHWK cycle package found")
    allowed_retrieval = set(manifest["method"]["endpoint_retrieval_state_vocabulary"])
    allowed_relationship = set(manifest["method"]["relationship_verification_state_vocabulary"])
    cycle_results = []
    incomplete_custody = []

    for directory in cycle_dirs:
        intent_path = directory / "precollection-intent.json"
        summary_path = directory / "cycle-summary.json"
        index_path = directory / "endpoint-outcome-index.jsonl"
        report_path = directory / "README.md"
        evidence_readme = directory / "evidence/README.md"
        # Exact historical orphan index introduced on 2026-11-24. No generic
        # exemption for incomplete cycle packages; preserved separately from
        # validated cycles, with the original index pinned by Git blob identity.
        gap_path = directory / "custody-gap.json"
        if directory.name == "cycle-2026-11-24-pst-01" and gap_path.is_file():
            gap = read_json(gap_path)
            need(gap.get("cycle_id") == directory.name and
                 gap.get("record_class") == "HISTORICAL_CUSTODY_GAP_NOT_VALIDATED_CYCLE" and
                 gap.get("status") == "BLOCKED_ORIGINAL_RECORDS_NOT_AVAILABLE" and
                 gap.get("eligible_prospective_cycle_verified") is False and
                 gap.get("primary_endpoint_attempts") is None and
                 gap.get("actual_acquisition_window_utc") is None and
                 gap.get("absence_inferred") is False,
                 f"{directory}: invalid historical custody-gap classification")
            need(gap.get("source_index_git_blob_sha") == "658d4b9384f1b511eb60a36163adb9f8a349dff1" and
                 git_blob_sha(evidence_readme.read_bytes()) == "658d4b9384f1b511eb60a36163adb9f8a349dff1",
                 f"{directory}: historical custody index Git blob mismatch")
            required = (intent_path, summary_path, index_path, report_path)
            if not all(path.is_file() for path in required):
                actual = {p.relative_to(directory).as_posix()
                          for p in directory.rglob("*") if p.is_file()}
                need(actual == {"evidence/README.md", "custody-gap.json"},
                     f"{directory}: partial recovery must not bypass cycle validation")
                expected_missing = ["precollection-intent.json","cycle-summary.json","endpoint-outcome-index.jsonl","README.md","evidence/github-attempts.jsonl","evidence/workflow-A-current-main.yml","evidence/workflow-B-current-main.yml","evidence/workflow-content-followup.json","evidence/registered-source-version-crosscheck.jsonl","evidence/external-attempts-batch-01.json","evidence/external-attempts-batch-02.json","evidence/external-error-followup.json"]
                need(gap.get("missing_paths") == expected_missing,
                     f"{directory}: custody-gap missing-path ledger drift")
                incomplete_custody.append({"cycle_id": directory.name,
                                           "status": gap["status"],
                                           "endpoint_rows": None,
                                           "counted_as_validated_cycle": False})
                continue
        for path in (intent_path, summary_path, index_path, report_path, evidence_readme):
            need(path.is_file(), f"{directory}: missing required artifact {path.name}")

        intent, summary = read_json(intent_path), read_json(summary_path)
        cycle_id = intent.get("cycle_id")
        need(cycle_id == directory.name, f"{directory}: cycle_id must match directory name")
        need(intent.get("study") == "OSF_VSHWK", f"{cycle_id}: wrong study identity")
        need(intent.get("latest_approved_schema_response") == EXPECTED_RESPONSE,
             f"{cycle_id}: wrong approved response anchor")
        need(intent.get("manifest_ref") == "studies/osf-vshwk/contract/endpoints-v1.json",
             f"{cycle_id}: manifest reference drifted")
        need(intent.get("manifest_version") == manifest.get("version"),
             f"{cycle_id}: manifest version mismatch")
        need(intent.get("case_project_id") == 490 and intent.get("lineages") == [2332, 2334],
             f"{cycle_id}: current case or lineages drifted")
        need(intent.get("status") == "INITIATED_PENDING_COLLECTION" and
             intent.get("collection_started") is False and
             intent.get("observation_records_at_intent_time") == 0,
             f"{cycle_id}: precollection snapshot must preserve its pre-acquisition state")

        declared = clock(intent.get("declared_at_utc"), f"{cycle_id}.declared_at_utc")
        reporting = intent.get("reporting_day", {})
        report_date, report_zone = reporting.get("date"), reporting.get("timezone")
        need(report_zone == "America/Los_Angeles", f"{cycle_id}: reporting zone must be America/Los_Angeles")
        need({"UTC", "Asia/Shanghai"}.issubset(set(intent.get("protocol_clock_zones", []))),
             f"{cycle_id}: UTC and Asia/Shanghai clocks are required")

        rows = read_jsonl(index_path)
        ids = [row.get("endpoint_id") for row in rows]
        need(len(ids) == len(set(ids)), f"{cycle_id}: duplicate endpoint IDs in outcome index")
        need(set(ids) == set(endpoint_ids),
             f"{cycle_id}: outcome index must account for each manifest endpoint exactly once")

        retrieval, relationship = Counter(), Counter()
        starts, ends = [], []
        endpoint_map = {item["endpoint_id"]: item for item in endpoints}
        for row in rows:
            eid, spec = row["endpoint_id"], endpoint_map[row["endpoint_id"]]
            need((row.get("layer"), row.get("platform"), row.get("scope")) ==
                 (spec.get("layer"), spec.get("platform"), spec.get("scope")),
                 f"{cycle_id}/{eid}: endpoint identity differs from manifest")
            state, relation = row.get("primary_retrieval_state"), row.get("relationship_verification_state")
            need(state in allowed_retrieval, f"{cycle_id}/{eid}: invalid retrieval state {state}")
            need(relation in allowed_relationship, f"{cycle_id}/{eid}: invalid relationship state {relation}")
            retrieval[state] += 1
            relationship[relation] += 1

            source_path = root / row.get("primary_source_path", "")
            need(source_path.is_file(), f"{cycle_id}/{eid}: primary source ledger missing")
            need(git_blob_sha(source_path.read_bytes()) == row.get("primary_source_blob_sha"),
                 f"{cycle_id}/{eid}: primary source Git blob SHA mismatch")

            if state == "NOT_QUERIED":
                need(bool(row.get("unattempted_reason")), f"{cycle_id}/{eid}: NOT_QUERIED requires a reason")
            else:
                start = clock(row.get("primary_attempt_start_utc"), f"{cycle_id}/{eid}.start")
                end = clock(row.get("primary_attempt_end_utc"), f"{cycle_id}/{eid}.end")
                need(start <= end and start >= declared, f"{cycle_id}/{eid}: invalid acquisition interval")
                starts.append(start)
                ends.append(end)
                pacific = start.astimezone(ZoneInfo(report_zone))
                need(pacific.date().isoformat() == report_date,
                     f"{cycle_id}/{eid}: reporting date does not match UTC acquisition clock")
                need(row.get("primary_attempt_start_pst") == pacific.isoformat(timespec="milliseconds"),
                     f"{cycle_id}/{eid}: Pacific reporting clock mismatch")
                need(row.get("primary_attempt_start_shanghai") ==
                     start.astimezone(ZoneInfo("Asia/Shanghai")).isoformat(timespec="milliseconds"),
                     f"{cycle_id}/{eid}: Asia/Shanghai clock mismatch")
            if state in {"ENDPOINT_ERROR", "ACCESS_BLOCKED", "RATE_LIMITED"}:
                need(row.get("absence_inferred") is False,
                     f"{cycle_id}/{eid}: endpoint failure must not infer global absence")

        need(summary.get("expected_endpoints") == len(endpoint_ids),
             f"{cycle_id}: summary expected endpoint count mismatch")
        need(summary.get("primary_endpoint_attempts") ==
             sum(n for state, n in retrieval.items() if state != "NOT_QUERIED"),
             f"{cycle_id}: summary primary attempt count mismatch")
        need(summary.get("primary_retrieval_statuses") == dict(retrieval),
             f"{cycle_id}: summary retrieval-state counts mismatch")
        need(summary.get("relationship_verification_statuses") == dict(relationship),
             f"{cycle_id}: summary relationship-state counts mismatch")
        expected_index = str(Path("studies/osf-vshwk") / "cycles" / directory.name /
                             "endpoint-outcome-index.jsonl")
        need(summary.get("endpoint_outcome_index") == expected_index,
             f"{cycle_id}: summary endpoint-index path mismatch")
        need(summary.get("intent_declared_at_utc") == intent.get("declared_at_utc"),
             f"{cycle_id}: summary / intent declaration clocks differ")
        need(summary.get("logical_day", {}).get("date") == report_date and
             summary.get("logical_day", {}).get("tz") == report_zone,
             f"{cycle_id}: summary reporting day differs from intent")

        recorded_layers = {x.get("layer"): x for x in summary.get("per_layer_classification", [])}
        need(set(recorded_layers) == set(EXPECTED_LAYER_COUNTS),
             f"{cycle_id}: summary must classify all eight layers")
        for layer in EXPECTED_LAYER_COUNTS:
            subset = [x for x in rows if x["layer"] == layer]
            expected = {
                "endpoint_count": len(subset),
                "retrieval_status_counts": dict(Counter(x["primary_retrieval_state"] for x in subset)),
                "relationship_verification_status_counts": dict(Counter(
                    x["relationship_verification_state"] for x in subset)),
            }
            for key, value in expected.items():
                need(recorded_layers[layer].get(key) == value, f"{cycle_id}/{layer}: {key} mismatch")

        units = summary.get("study_units", {})
        need(units.get("project_case_count") == 1 and units.get("project_layer_bundles") == 8 and
             units.get("nested_lineage_layer_bundles") == 16 and
             units.get("independent_statistical_samples_not_16") is True,
             f"{cycle_id}: analytical units / denominators drifted")

        ledgers = summary.get("source_ledgers", [])
        need(bool(ledgers), f"{cycle_id}: source ledger manifest is empty")
        for ledger in ledgers:
            path = root / ledger["path"]
            need(path.is_file(), f"{cycle_id}: source ledger missing: {ledger['path']}")
            need(git_blob_sha(path.read_bytes()) == ledger.get("git_blob_sha"),
                 f"{cycle_id}: source ledger Git blob mismatch: {ledger['path']}")
            count_rows = sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
            need(count_rows == ledger.get("rows"), f"{cycle_id}: source ledger row count mismatch")

        if starts:
            first = min(starts).isoformat(timespec="milliseconds").replace("+00:00", "Z")
            last = max(ends).isoformat(timespec="milliseconds").replace("+00:00", "Z")
            need(summary.get("capture_window_utc") == [first, last],
                 f"{cycle_id}: summary capture window differs from endpoint clocks")

        report_text = report_path.read_text(encoding="utf-8")
        need("CYCLE_ATTEMPTS_CLOSED_WITH_UNRESOLVED_RESULTS" in report_text,
             f"{cycle_id}: human report missing disposition")
        need("not global absence" in report_text.lower(),
             f"{cycle_id}: human report must state the absence-inference boundary")
        evidence_text = evidence_readme.read_text(encoding="utf-8")
        need("provider-origin HTTP" in evidence_text,
             f"{cycle_id}: evidence README missing provider-origin fidelity boundary")

        cycle_results.append({
            "cycle_id": cycle_id, "endpoint_rows": len(rows),
            "retrieval_statuses": dict(retrieval),
            "relationship_statuses": dict(relationship),
            "source_ledgers_verified": len(ledgers),
        })

    return {"manifest_version": manifest.get("version"),
            "manifest_endpoints": len(endpoint_ids), "cycles_validated": cycle_results,
            "incomplete_custody": incomplete_custody}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository checkout root")
    args = parser.parse_args()
    try:
        result = validate(args.root.resolve())
    except (ContractError, OSError, KeyError, TypeError, ValueError) as exc:
        print(f"VSHWK CONTRACT: FAIL — {exc}", file=sys.stderr)
        return 1
    print("VSHWK CONTRACT: PASS (structural validation; incomplete custody is not cycle completion)")
    if result["incomplete_custody"]:
        print("VSHWK CUSTODY: DEGRADED — historical original records not available")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
