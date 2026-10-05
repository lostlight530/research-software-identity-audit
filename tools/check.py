#!/usr/bin/env python3
"""Small, dependency-free contract checker for research-software-identity-audit."""

from __future__ import annotations

import csv
import json
import re
import sys
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
    for platform in ("openaire", "openalex"):
        pattern = rf"- id: {platform}\n(?:.|\n)*?infrastructure_layer: discovery_graph"
        if not re.search(pattern, ptext):
            fail(f"{platform} must map to discovery_graph")
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


def validate_observation_record(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
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
    if data["observation_state"] not in OBS_STATES:
        fail(f"{path}: unknown observation state")
    if not isinstance(data["evidence_refs"], list) or not data["evidence_refs"]:
        fail(f"{path}: evidence_refs must be non-empty")
    if data["attempt_status"] == "failed" and not data.get("failure_reason"):
        fail(f"{path}: failed attempt requires failure_reason")


def check_observations() -> None:
    for base in (ROOT / "observations/raw", ROOT / "observations/derived"):
        if not base.exists():
            continue
        for path in base.rglob("*.json"):
            validate_observation_record(path)


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


def main() -> int:
    checks = [
        check_corpus,
        check_layers_and_platforms,
        check_schema,
        check_observations,
        check_baseline,
        check_data_handling,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print("PASS research contract checks")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        raise SystemExit(1)
