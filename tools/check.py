#!/usr/bin/env python3
"""Small, dependency-free contract checker for research-software-identity-audit."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_OBJECTS = [f"RS{i:02d}" for i in range(1, 11)]
EXPECTED_LAYERS = {
    "source_repository",
    "archival_repository",
    "identifier_registration",
    "author_registry",
    "preservation_archive",
    "discovery_graph",
}
EXPECTED_PLATFORMS = {
    "github",
    "zenodo",
    "datacite",
    "orcid",
    "software_heritage",
    "openaire",
    "openalex",
}
EXPECTED_PLATFORM_LAYERS = {
    "github": "source_repository",
    "zenodo": "archival_repository",
    "datacite": "identifier_registration",
    "orcid": "author_registry",
    "software_heritage": "preservation_archive",
    "openaire": "discovery_graph",
    "openalex": "discovery_graph",
}
OBS_STATES = {
    "observed",
    "not_found",
    "rate_limited",
    "unresolved",
    "partially_verified",
    "fully_verified",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def check_corpus() -> None:
    path = ROOT / "corpus/object-manifest.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    ids = [row["object_id"] for row in rows]
    repos = [row["source_repository"] for row in rows]
    if ids != EXPECTED_OBJECTS:
        fail(f"corpus IDs must be exactly RS01-RS10 in order; got {ids}")
    if len(set(repos)) != 10:
        fail("corpus repository URLs must be unique")
    if any(row.get("corpus_role") != "preregistered_sample" for row in rows):
        fail("every corpus row must remain preregistered_sample")
    if any(row.get("status") != "fixed" for row in rows):
        fail("every corpus row must remain fixed")


def yaml_ids(text: str) -> set[str]:
    return set(re.findall(r"^\s*- id:\s*([a-z0-9_]+)\s*$", text, flags=re.MULTILINE))


def check_layers_and_platforms() -> None:
    layers = yaml_ids(read_text("schema/infrastructure-layers.yaml"))
    platforms = yaml_ids(read_text("schema/platforms.yaml"))
    if layers != EXPECTED_LAYERS:
        fail(f"infrastructure layers drifted: {sorted(layers)}")
    if platforms != EXPECTED_PLATFORMS:
        fail(f"operational platforms drifted: {sorted(platforms)}")
    ptext = read_text("schema/platforms.yaml")
    # Check each concrete platform/layer pair, not just the IDs or discovery pair.
    pairs = re.findall(
        r"(?m)^  - id: ([a-z0-9_]+)\n    label: [^\n]*\n"
        r"    infrastructure_layer: ([a-z0-9_]+)\s*$",
        ptext,
    )
    if len(pairs) != len(EXPECTED_PLATFORM_LAYERS) or dict(pairs) != EXPECTED_PLATFORM_LAYERS:
        fail(f"operational platform-to-layer mapping drifted: {pairs}")
    if "preregistered_object_layer_units_per_timepoint: 60" not in ptext:
        fail("platform mapping must preserve 60 preregistered object-layer units")
    if "operational_platform_count: 7" not in ptext:
        fail("platform mapping must record seven operational platforms")


def check_schema() -> None:
    schema = json.loads(read_text("schema/observation.schema.json"))
    required = set(schema["required"])
    for field in ("observation_id", "object_id", "infrastructure_layer", "platform",
                  "observation_timepoint", "retrieval_timestamp", "attempt_status",
                  "observation_state", "evidence_refs"):
        if field not in required:
            fail(f"observation schema missing required field: {field}")
    obj_pattern = schema["properties"]["object_id"]["pattern"]
    if obj_pattern != "^RS(0[1-9]|10)$":
        fail("observation object_id pattern must reject RS11 and allow only RS01-RS10")
    layer_enum = set(schema["properties"]["infrastructure_layer"]["enum"])
    platform_enum = set(schema["properties"]["platform"]["enum"])
    if layer_enum != EXPECTED_LAYERS:
        fail("observation schema infrastructure-layer enum drifted")
    if platform_enum != EXPECTED_PLATFORMS:
        fail("observation schema platform enum drifted")
    if schema["properties"]["evidence_refs"].get("minItems") != 1:
        fail("observation schema must require at least one evidence ref")


def aware_timestamp(value: object, field: str, path: Path) -> datetime:
    """Require offset-aware clocks before cross-platform temporal comparison."""
    if not isinstance(value, str) or not value.strip():
        fail(f"{path}: {field} requires a nonempty ISO-8601 timestamp")
    try:
        clock = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        fail(f"{path}: invalid {field} timestamp: {value!r}")
    if clock.tzinfo is None or clock.utcoffset() is None:
        fail(f"{path}: {field} must carry a timezone offset")
    return clock


def validate_observation_record(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail(f"{path}: raw observation must be a JSON object")
    required = {
        "observation_id", "object_id", "infrastructure_layer", "platform",
        "observation_timepoint", "retrieval_timestamp", "attempt_status",
        "observation_state", "evidence_refs",
    }
    missing = sorted(required - data.keys())
    if missing:
        fail(f"{path}: missing fields {missing}")
    if data["object_id"] not in EXPECTED_OBJECTS:
        fail(f"{path}: object_id outside fixed corpus")
    if data["infrastructure_layer"] not in EXPECTED_LAYERS:
        fail(f"{path}: unknown infrastructure layer")
    if data["platform"] not in EXPECTED_PLATFORMS:
        fail(f"{path}: unknown platform")
    if data["infrastructure_layer"] != EXPECTED_PLATFORM_LAYERS[data["platform"]]:
        fail(f"{path}: platform/layer mismatch for {data['platform']}")
    if data["observation_state"] not in OBS_STATES:
        fail(f"{path}: unknown observation state")
    if data["attempt_status"] not in {"completed", "failed"}:
        fail(f"{path}: invalid attempt_status")
    if not isinstance(data["evidence_refs"], list) or not data["evidence_refs"]:
        fail(f"{path}: evidence_refs must be non-empty")
    if any(not isinstance(ref, str) or not ref.strip() or "EXAMPLE-DO-NOT-USE" in ref
           for ref in data["evidence_refs"]):
        fail(f"{path}: evidence_refs contains a blank/example-only locator")
    if data["attempt_status"] == "failed" and not data.get("failure_reason"):
        fail(f"{path}: failed attempt requires failure_reason")
    if data["attempt_status"] == "failed" and data["observation_state"] == "fully_verified":
        fail(f"{path}: failed attempt cannot itself be fully_verified")
    if (not isinstance(data["observation_timepoint"], str)
            or not data["observation_timepoint"].strip()
            or data["observation_timepoint"] == "TEMPLATE_ONLY"):
        fail(f"{path}: undeclared/example observation_timepoint")
    retrieved = aware_timestamp(data["retrieval_timestamp"], "retrieval_timestamp", path)
    released = data.get("release_event_timestamp")
    if released is not None:
        released = aware_timestamp(released, "release_event_timestamp", path)
    if data.get("dataset_phase") == "prospective":
        if data.get("retrospective_reconstruction") is True:
            fail(f"{path}: prospective records cannot be retrospective reconstructions")
        if released is None:
            fail(f"{path}: prospective records require a release event timestamp")
        if released > retrieved:
            fail(f"{path}: release event is later than the retrieval timestamp")


def validate_derived_record(path: Path) -> None:
    """Derived JSON is a calculation, not another platform request/observation."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail(f"{path}: derived record must be an object")
    if data.get("dataset_phase") != "prospective":
        fail(f"{path}: derived record requires dataset_phase=prospective")
    if not isinstance(data.get("derivation_id"), str) or not data["derivation_id"].strip():
        fail(f"{path}: derived record requires derivation_id")
    if (not isinstance(data.get("derivation_method_ref"), str)
            or not data["derivation_method_ref"].strip()):
        fail(f"{path}: derived record requires derivation_method_ref")
    derived_at = aware_timestamp(data.get("derived_at"), "derived_at", path)
    refs = data.get("input_observation_refs")
    if not isinstance(refs, list) or not refs:
        fail(f"{path}: derived record needs nonempty input_observation_refs")
    source_dir = (ROOT / "observations/raw").resolve()
    if len(refs) != len(set(ref for ref in refs if isinstance(ref, str))):
        fail(f"{path}: duplicate or invalid input refs")
    for ref in refs:
        if not isinstance(ref, str) or not ref.strip():
            fail(f"{path}: blank input observation ref")
        ref_path = (ROOT / ref).resolve()
        if (not ref_path.is_relative_to(source_dir)
                or ref_path.suffix != ".json" or not ref_path.is_file()):
            fail(f"{path}: input must resolve to existing raw observation JSON: {ref}")
        source = json.loads(ref_path.read_text(encoding="utf-8"))
        if not isinstance(source, dict):
            fail(f"{path}: source raw observation is not a JSON object: {ref}")
        observed_at = aware_timestamp(source.get("retrieval_timestamp"),
                                      "input.retrieval_timestamp", ref_path)
        if observed_at > derived_at:
            fail(f"{path}: derived_at precedes source retrieval for {ref}")


def check_observations() -> None:
    raw = ROOT / "observations/raw"
    raw_records = sorted(raw.rglob("*.json")) if raw.exists() else []
    if raw_records:
        # This is only a structural precondition: source evidence for actual
        # eligibility and scheduled timepoint coverage must still be reviewed.
        declarations = (list((ROOT / "schedule").glob("*.yaml"))
                        + list((ROOT / "schedule").glob("*.yml")))
        active: list[tuple[Path, datetime, set[str]]] = []
        for declaration in declarations:
            body = declaration.read_text(encoding="utf-8")
            if not re.search(r"""(?mi)^status:\s*["']?active["']?\s*$""", body):
                continue
            sid = re.search(r"""(?m)^schedule_id:\s*["']?([A-Za-z0-9_-]+)["']?\s*$""", body)
            declared = re.search(r"""(?m)^declared_at:\s*["']?([^"'\s#]+)["']?\s*$""", body)
            if not sid or not declared:
                fail(f"{declaration}: active schedule requires schedule_id and declared_at")
            timepoint_ids = set(re.findall(
                r"""(?m)^  - id:\s*["']?([A-Za-z0-9_-]+)["']?\s*$""", body
            ))
            if not timepoint_ids or "__TIMEPOINT_ID__" in timepoint_ids:
                fail(f"{declaration}: active schedule requires concrete timepoint IDs")
            active.append((declaration, aware_timestamp(declared.group(1), "declared_at", declaration), timepoint_ids))
        if not active:
            fail("prospective raw records require a dated active schedule declaration")
    for path in raw_records:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            fail(f"{path}: raw prospective observation must be a JSON object")
        if data.get("dataset_phase") != "prospective":
            fail(f"{path}: raw prospective records require dataset_phase=prospective")
        retrieval = aware_timestamp(data.get("retrieval_timestamp"), "retrieval_timestamp", path)
        if not any(declared_at <= retrieval for _, declared_at, _ in active):
            fail(f"{path}: no active schedule declaration predates retrieval")
        if not any(data.get("observation_timepoint") in ids and declared_at <= retrieval
                   for _, declared_at, ids in active):
            fail(f"{path}: observation_timepoint not governed by an active prior schedule")
        validate_observation_record(path)
    derived = ROOT / "observations/derived"
    if derived.exists():
        for path in derived.rglob("*.json"):
            validate_derived_record(path)


def check_baseline() -> None:
    manifest = read_text("baseline/2026-10-05/manifest.yaml")
    required_fragments = [
        'timestamp: "2026-10-05T23:59:59+08:00"',
        'executed_at_approx: "2026-10-06T00:33:54+08:00"',
        'generated_by: "Codex"',
        "object_count: 10",
        "preregistered_infrastructure_layer_count: 6",
        "object_layer_units_per_scheduled_timepoint: 60",
        "operational_platform_count: 7",
        "platform_checks_if_all_queried: 70",
        "family_views: 581",
        "family_unique_views: 556",
        "family_downloads: 7",
        "family_unique_downloads: 6",
        "latest_version_views: 15",
        "latest_version_unique_views: 13",
        "latest_version_downloads: 0",
        'software_heritage_october_content_identity: "NOT_VERIFIED"',
    ]
    for fragment in required_fragments:
        if fragment not in manifest:
            fail(f"baseline manifest missing invariant: {fragment}")

    stats = read_text("baseline/2026-10-05/zenodo-statistics.yaml")
    if "historical_backdating_permitted: false" not in stats:
        fail("Zenodo live counters must not be backdated")

    raw = read_text("baseline/2026-10-05/raw-reconciliation-record-2026-10-06.md")
    if "本轮采集时间：2026-10-06T00:33:54+08:00 前后" not in raw:
        fail("Codex raw record collection timestamp missing")
    if "latest_october_version_content_identity = NOT_VERIFIED" not in raw:
        fail("Codex raw record must preserve Software Heritage NOT_VERIFIED state")


def check_data_handling() -> None:
    text = read_text("DATA_HANDLING.md")
    for token in ("API keys", "cookies", "IP addresses", "ORCID", "Public does not mean historical"):
        if token not in text:
            fail(f"data-handling policy missing: {token}")



def check_canonical_object_mapping() -> None:
    expected = {
        "RS01": ("welcome-to-github", "23137203"),
        "RS02": ("zero-entropy-lab", "23137204"),
        "RS03": ("Axiom-0", "23137205"),
        "RS04": ("reflective-continuum", "23137206"),
        "RS05": ("agent-foundations", "23137207"),
        "RS06": ("auto-doc-engine", "23137215"),
        "RS07": ("epistemic-pipeline", "23137216"),
        "RS08": ("sci-render-kit", "23137219"),
        "RS09": ("china-agentic-observatory", "23137211"),
        "RS10": ("agentic-frontier-observatory", "23137214"),
    }

    with (ROOT / "baseline/2026-10-05/doi-map.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    observed = {
        row["object_id"]: (row["repository"], row["latest_version_doi_2026_10_04"].rsplit(".", 1)[-1])
        for row in rows
    }
    if observed != expected:
        fail(f"baseline DOI map drifted from fixed corpus: {observed}")

    delta_path = ROOT / "monitoring/2026-10-06/01-wave-01/zenodo-view-delta.csv"
    if delta_path.exists():
        with delta_path.open(encoding="utf-8", newline="") as handle:
            delta_rows = list(csv.DictReader(handle))
        ids = [row["object_id"] for row in delta_rows]
        if ids != EXPECTED_OBJECTS:
            fail("Wave 1 delta rows must use the canonical RS01-RS10 order")
        if sum(int(row["t0_views"]) for row in delta_rows) != 575:
            fail("Wave 1 T0 view total must be 575")
        if sum(int(row["t1_views"]) for row in delta_rows) != 616:
            fail("Wave 1 T1 view total must be 616")
        if sum(int(row["delta_views"]) for row in delta_rows) != 41:
            fail("Wave 1 view delta total must be 41")



def check_20261007_monitoring() -> None:
    base = ROOT / "monitoring/2026-10-07/01-facility-audit"
    summary_path = base / "record.yaml"
    snapshot_path = base / "cross-platform-snapshot.csv"
    swh_path = base / "software-heritage-routes.csv"

    for path in (summary_path, snapshot_path, swh_path, base / "mapping-reconciliation.md",
                 base / "source.md", base / "reconciliation.md",
                 base / "README.md"):
        if not path.is_file():
            fail(f"missing 2026-10-07 monitoring artifact: {path.relative_to(ROOT)}")

    with (ROOT / "corpus/object-manifest.csv").open(encoding="utf-8", newline="") as handle:
        manifest_rows = list(csv.DictReader(handle))
    canonical = {
        row["object_id"]: row["software_family"]
        for row in manifest_rows
    }

    with snapshot_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if [row["object_id"] for row in rows] != EXPECTED_OBJECTS:
        fail("2026-10-07 snapshot rows must remain RS01-RS10 in canonical order")
    observed = {row["object_id"]: row["repository"] for row in rows}
    if observed != canonical:
        fail(f"2026-10-07 snapshot object joins drifted from manifest: {observed}")
    if sum(int(row["family_views"]) for row in rows) != 695:
        fail("2026-10-07 Zenodo family views must sum to 695")
    if sum(int(row["family_unique_views"]) for row in rows) != 664:
        fail("2026-10-07 Zenodo family unique views must sum to 664")
    if sum(int(row["family_downloads"]) for row in rows) != 7:
        fail("2026-10-07 Zenodo family downloads must sum to 7")
    if any(int(row["orcid_source_summaries"]) != 5 for row in rows):
        fail("2026-10-07 fixed-corpus ORCID summaries must remain five per software family")

    with swh_path.open(encoding="utf-8", newline="") as handle:
        swh_rows = list(csv.DictReader(handle))
    if [row["object_id"] for row in swh_rows] != EXPECTED_OBJECTS:
        fail("2026-10-07 SWH rows must remain RS01-RS10 in canonical order")
    swh_observed = {row["object_id"]: row["repository"] for row in swh_rows}
    if swh_observed != canonical:
        fail("2026-10-07 SWH object joins drifted from manifest")
    if sum(row["zenodo_route_state"] == "resolved" for row in swh_rows) != 10:
        fail("2026-10-07 supplied Zenodo-origin SWH routes must retain ten resolved rows")
    if sum(row["github_route_state"] == "unresolved_connection_failure" for row in swh_rows) != 1:
        fail("2026-10-07 GitHub-origin SWH route must retain one unresolved connection failure")

    summary = summary_path.read_text(encoding="utf-8")
    for token in (
        'record_class: "pre_eligibility_monitoring"',
        "prospective_dataset_member: false",
        "preregistered_layer_count: 6",
        "operational_platform_count: 7",
        "possible_object_platform_checks: 70",
        "platform_checks_replace_preregistered_denominator: false",
        "family_views: 695",
        "family_unique_views: 664",
        "family_downloads: 7",
        "family_unique_downloads: 6",
        "supplied_total_zip_bytes: 29282855",
        "prior_preserved_total_zip_bytes: 29261316",
        "byte_difference: 21539",
        'byte_difference_interpretation: "UNRESOLVED"',
        "platform_matrix_materialized_here: false",
        'identifier: "SCR_029105"',
        "author_work_count: 41",
        "author_profile_cached_works_count: 30",
        "live_author_works_query_count: 40",
        'comparability_state: "PARTIAL"',
        '- "Scientific Computing and Data Management"',
        '- "Research Data Management Practices"',
        'identifier_assignment_state: "assigned"',
        'public_indexing_state: "pending"',
    ):
        if token not in summary:
            fail(f"2026-10-07 monitoring summary missing invariant: {token}")


def check_20261008_morning() -> None:
    base = ROOT / "monitoring/2026-10-08/01-morning-recheck"
    summary_path = base / "record.yaml"
    delta_path = base / "zenodo-view-delta.csv"
    agent_path = base / "agent-cohort.csv"

    for path in (
        base / "README.md",
        base / "source-01-morning-audit.md",
        base / "source-02-wave3-declaration.md",
        summary_path,
        delta_path,
        agent_path,
        base / "verification.md",
    ):
        if not path.is_file():
            fail(f"missing 2026-10-08 morning artifact: {path.relative_to(ROOT)}")

    with (ROOT / "corpus/object-manifest.csv").open(encoding="utf-8", newline="") as handle:
        manifest_rows = list(csv.DictReader(handle))
    canonical = {row["object_id"]: row["software_family"] for row in manifest_rows}

    with delta_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if [row["object_id"] for row in rows] != EXPECTED_OBJECTS:
        fail("2026-10-08 delta rows must remain RS01-RS10 in canonical order")
    if {row["object_id"]: row["repository"] for row in rows} != canonical:
        fail("2026-10-08 delta object joins drifted from canonical manifest")
    if sum(int(row["previous_family_views"]) for row in rows) != 695:
        fail("2026-10-08 prior family-view total must be 695")
    if sum(int(row["current_family_views"]) for row in rows) != 775:
        fail("2026-10-08 current family-view total must be 775")
    if sum(int(row["delta_family_views"]) for row in rows) != 80:
        fail("2026-10-08 family-view delta total must be 80")
    if sum(int(row["current_family_downloads"]) for row in rows) != 7:
        fail("2026-10-08 family downloads must sum to 7")

    with agent_path.open(encoding="utf-8", newline="") as handle:
        agent_rows = list(csv.DictReader(handle))
    expected_agent = {
        "RS10": ("agentic-frontier-observatory", "8"),
        "RS09": ("china-agentic-observatory", "9"),
        "RS05": ("agent-foundations", "10"),
        "RS07": ("epistemic-pipeline", "11"),
    }
    observed_agent = {
        row["object_id"]: (row["repository"], row["current_rank"])
        for row in agent_rows
    }
    if observed_agent != expected_agent:
        fail(f"2026-10-08 source-reported Agent owned rows drifted: {observed_agent}")
    if any(row["verification_class"] != "source_reported" for row in agent_rows):
        fail("Agent cohort rows must remain source_reported until independently rerun")

    summary = summary_path.read_text(encoding="utf-8")
    for token in (
        'record_class: "pre_eligibility_monitoring"',
        "prospective_dataset_member: false",
        'collection_window_start: "2026-10-08T08:12+08:00"',
        'collection_window_end: "2026-10-08T08:26+08:00"',
        "preregistered_units_per_scheduled_timepoint: 60",
        "possible_object_platform_checks: 70",
        "family_views: 775",
        "family_unique_views_sum: 733",
        "current_version_views: 70",
        "audit_runtime_in_fixed_corpus_totals: false",
        "groups_total: 14",
        "summaries_total: 56",
        "exact_release_pages_readable: 10",
        "fixed_corpus_dois_readable: 40",
        "fixed_corpus_resource_type_software: 40",
        "preserved_october_directory_swhids_readable: 10",
        "current_version_exact_doi_matches: 10",
        "live_works_query_count: 43",
        "author_profile_works_count: 41",
        "fixed_corpus_software_records_under_main_author: 40",
        'work_id: "W7220365356"',
        'work_id: "W7220737563"',
        'work_id: "W7220470293"',
        'work_id: "W7220380722"',
        'statistics_rest_fetch_state: "BLOCKED_UNEXPECTED_CONTENT_TYPE"',
        "source_reported_14_groups_independently_reconstructed: false",
        "source_reported_56_summaries_independently_reconstructed: false",
        "independent_full_rerun: false",
        'independent_verification_state: "UNRESOLVED"',
        'identifier: "SCR_029105"',
        'source_declared_observation_cutoff: "2026-10-08T08:35:00+08:00"',
        'source_declared_dataset_phase: "prospective"',
        "t0_zenodo_family_views: 575",
        "baseline_package_later_retrieved_family_views: 581",
        "t0_575_replaces_baseline_manifest_581: false",
        'repository_adjudicated_dataset_phase: "pre_eligibility_monitoring"',
        'source_defined_fixed_study_scope_count: 41',
        "live_works_query_count: 43",
        "package_bytes_t2_to_t3_equal: true",
        "bytewise_identity_t2_to_t3_independently_verified: false",
        "source_wave3_used_prior_display_order_for_rs06_rs10: true",
        'canonical_rs06: "auto-doc-engine"',
        'canonical_rs07: "epistemic-pipeline"',
        'canonical_rs09: "china-agentic-observatory"',
        'canonical_rs10: "agentic-frontier-observatory"',
        'state: "PARTIALLY_INDEPENDENTLY_VERIFIED_WITH_CONTRACT_RECONCILIATION"',
    ):
        if token not in summary:
            fail(f"2026-10-08 morning summary missing invariant: {token}")


def check_repository_governance() -> None:
    required_files = (
        "LICENSE",
        "LICENSING.md",
        "AUTHORS",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "CODE_OF_CONDUCT.md",
        "RELEASE_POLICY.md",
        "OPEN_RESEARCH.md",
        "RESEARCH_TEMPLATE.md",
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/ISSUE_TEMPLATE/bug_report.md",
        ".github/ISSUE_TEMPLATE/feature_request.md",
        ".github/ISSUE_TEMPLATE/research_correction.md",
    )
    for path in required_files:
        if not (ROOT / path).is_file():
            fail(f"missing repository governance file: {path}")

    license_text = read_text("LICENSE")
    if not license_text.startswith("MIT License"):
        fail("repository-owned material must retain the MIT license")

    cff = read_text("CITATION.cff")
    if 'name: "lightlost"' not in cff:
        fail("CITATION.cff software author must match the ten-repository template")
    if 'license: MIT' not in cff:
        fail("CITATION.cff must declare MIT")

    codemeta = json.loads(read_text("codemeta.json"))
    if codemeta.get("author", {}).get("name") != "lightlost":
        fail("CodeMeta software author must match the ten-repository template")
    if codemeta.get("license") != "https://spdx.org/licenses/MIT.html":
        fail("CodeMeta must use the SPDX MIT license URL")

    # Advisory drift guard: check current citation metadata consistency, without
    # implying any correction to an earlier immutable release tag.
    cff_version = re.search(r'^version:\s*"([^"]+)"\s*$', cff, flags=re.MULTILINE)
    cff_date = re.search(r"^date-released:\s*(\d{4}-\d{2}-\d{2})\s*$", cff, flags=re.MULTILINE)
    if cff_version is None or cff_date is None:
        fail("CITATION.cff needs a release version and release date")
    if codemeta.get("version") != cff_version.group(1):
        fail("live-main CodeMeta version differs from CITATION.cff version")
    if codemeta.get("datePublished") != cff_date.group(1):
        fail("live-main CodeMeta datePublished differs from CITATION.cff date-released")

    zenodo = json.loads(read_text(".zenodo.json"))
    creators = zenodo.get("creators", [])
    if not creators or creators[0].get("name") != "lightlost":
        fail(".zenodo.json creator must match the repository software-author template")
    if zenodo.get("license") != "MIT":
        fail(".zenodo.json must declare MIT")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check research-contract invariants without silently changing semantics."
    )
    parser.add_argument(
        "--mode",
        choices=("advisory", "strict"),
        default="advisory",
        help=(
            "advisory reports contract drift but exits 0; "
            "strict exits 1 when any contract check fails"
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    checks = [
        check_corpus,
        check_layers_and_platforms,
        check_schema,
        check_observations,
        check_baseline,
        check_data_handling,
        check_repository_governance,
        check_canonical_object_mapping,
        check_20261007_monitoring,
        check_20261008_morning,
    ]

    failures: list[str] = []
    for check in checks:
        try:
            check()
            print(f"PASS {check.__name__}")
        except (AssertionError, KeyError, ValueError, json.JSONDecodeError) as exc:
            message = f"{check.__name__}: {exc}"
            failures.append(message)
            prefix = "WARN" if args.mode == "advisory" else "FAIL"
            print(f"{prefix} {message}", file=sys.stderr)

    if not failures:
        print(f"PASS research contract checks ({args.mode})")
        return 0

    print(
        f"{len(failures)} contract check(s) reported in {args.mode} mode.",
        file=sys.stderr,
    )
    if args.mode == "advisory":
        print(
            "ADVISORY ONLY: findings do not block this commit or pull request.",
            file=sys.stderr,
        )
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
