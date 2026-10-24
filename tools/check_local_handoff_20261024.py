"""Offline transfer-integrity audit for the attributed 2026-10-24 local handoff.

This checks committed bytes, package membership, public request projections, and
fixed object identities. It does not make network calls, authenticate original
HTTP responses, or validate historical scholarly interpretations.
"""
from __future__ import annotations

import base64
import csv
import gzip
import hashlib
import io
import json
import re
import sys
import tarfile
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = "evidence/2026-10-24/04-local-history-evidence-handoff"
MONITORING = "monitoring/2026-10-24/04-local-history-evidence-handoff"
SHA256 = re.compile(r"^[a-f0-9]{64}$")
MAX_TAR_BYTES = 64 * 1024 * 1024


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_file(relative: str) -> Path:
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise ValueError(f"Invalid repository-relative locator: {relative!r}")
    parts = Path(relative)
    if parts.is_absolute() or ".." in parts.parts:
        raise ValueError(f"Escaping repository-relative locator: {relative!r}")
    resolved = (ROOT / parts).resolve()
    if not resolved.is_relative_to(ROOT.resolve()) or not resolved.is_file():
        raise ValueError(f"Unresolvable committed file: {relative!r}")
    return resolved


def load_json(relative: str) -> dict:
    return json.loads(safe_file(relative).read_text(encoding="utf-8"))


def decode_gzip(encoded: str, expected_digest: str, limit: int = MAX_TAR_BYTES) -> bytes:
    zipped = base64.b64decode(encoded, validate=True)
    if digest(zipped) != expected_digest:
        raise ValueError("Compressed SHA256 mismatch")
    with gzip.GzipFile(fileobj=io.BytesIO(zipped)) as fh:
        unpacked = fh.read(limit + 1)
    if len(unpacked) > limit:
        raise ValueError("Exceeds bounded decompressed-byte limit")
    return unpacked


def run() -> dict:
    failures = []
    checks = 0

    def require(condition: bool, detail: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(detail)

    record = load_json(f"{MONITORING}/record.json")
    capture = load_json(f"{EVIDENCE}/capture-manifest.json")
    manifest = load_json(f"{EVIDENCE}/artifact-manifest.json")
    extract = load_json(f"{MONITORING}/canonical-current-field-extracts.json")

    require(record.get("record_class") == "retrospective_local_evidence_handoff",
            "Retrospective record classification changed")
    require(record.get("prospective_cells_added") == 0,
            "Historical handoff improperly changes prospective cells")
    require(record.get("frozen_layers") == 6 and record.get("contracted_platforms") == 7,
            "Frozen-layer/operational-platform boundary changed")
    require(record.get("source_artifacts") == 4267 and record.get("attempt_rows") == 4444
            and record.get("public_unique_payloads") == 1162,
            "Handoff published-summary cardinality changed")

    # Read the frozen corpus rather than hardcoding names into an external authority.
    with safe_file("corpus/object-manifest.csv").open(encoding="utf-8", newline="") as fh:
        corpus = list(csv.DictReader(fh))
    canonical = {r["object_id"]: r["software_family"] for r in corpus}
    observed = {r.get("object_id"): r.get("repository")
                for r in extract.get("fixed_objects", [])}
    require(len(canonical) == len(observed) == 10 and canonical == observed,
            "Extract no longer joins exactly the canonical RS01-RS10 corpus")
    require(all(r["corpus_role"] == "preregistered_sample" for r in corpus),
            "Corpus role has drifted")

    entries = manifest.get("artifacts", [])
    require(manifest.get("algorithm") == "SHA256" and len(entries) == 28,
            "Artifact manifest algorithm or 28-listed-object cardinality drift")
    require(manifest.get("excludes") == ["artifact-manifest.json"],
            "Artifact manifest exclusion contract drift")
    listed_paths = set()
    for item in entries:
        path = item["path"]
        require(path not in listed_paths, f"Duplicate manifest path: {path}")
        listed_paths.add(path)
        data = safe_file(path).read_bytes()
        require(len(data) == item["bytes"] and digest(data) == item["sha256"],
                f"Artifact byte/hash mismatch: {path}")

    # Preserve field boundaries for public request-attempt projections.
    allowed_fields = set(capture["allowed_fields"])
    allowed_hosts = set(capture["allowed_public_hosts"])
    allowed_keys = set(capture["allowed_query_keys"])
    expected_fields = {"source_artifact", "source_index", "public_endpoint",
                       "started_at", "finished_at", "http_status",
                       "response_sha256", "response_bytes"}
    require(allowed_fields == expected_fields, "Public projection field contract drift")
    attempt_files = capture.get("attempt_files", [])
    require(len(attempt_files) == 8, "Unexpected number of attempt projections")
    attempt_rows = 0
    unknown_endpoints = 0
    for location in attempt_files:
        require(location in listed_paths, f"Attempt projection not in artifact manifest: {location}")
        for line in safe_file(location).read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            entry = json.loads(line)
            attempt_rows += 1
            require(set(entry) == allowed_fields, f"Unexpected keys in {location}:{attempt_rows}")
            request_url = entry["public_endpoint"]
            if request_url is None:
                # Historical projection deliberately omitted an unsuitable locator.
                # Preserve the attempt without fabricating an origin URL.
                unknown_endpoints += 1
                continue
            require(isinstance(request_url, str),
                    f"Unexpected endpoint field type: {location}:{attempt_rows}")
            parsed = urlsplit(request_url)
            require(parsed.scheme == "https" and parsed.hostname in allowed_hosts
                    and not parsed.username and not parsed.password,
                    f"Public endpoint outside allowed host contract: {location}:{attempt_rows}")
            require(all(k in allowed_keys for k, _ in parse_qsl(parsed.query, keep_blank_values=True)),
                    f"Unexpected public URL query key: {location}:{attempt_rows}")
    require(attempt_rows == capture.get("source_rows") == record["attempt_rows"] == 4444,
            "Attempt projection row count mismatch")
    require(unknown_endpoints == 21,
            "Missing public endpoint count changed; do not infer absent original requests")
    require(capture.get("source_rows_not_claimed_as_distinct_requests") is True,
            "Duplicate attempt row warning missing")

    # Transfer verification: every compressed byte and every content-addressed tar member.
    archive_parts = [f"{EVIDENCE}/source-bundle-part-{i:02d}.json" for i in range(1, 15)]
    all_members = set()
    member_count = 0
    for path in archive_parts:
        require(path in listed_paths, f"Archive part missing from manifest: {path}")
        part = load_json(path)
        require(part.get("format") == "gzip-tar-base64-v1",
                f"Archive encoding contract drift: {path}")
        content = decode_gzip(part["data_base64"], part["gzip_sha256"])
        with tarfile.open(fileobj=io.BytesIO(content), mode="r:") as tar:
            members = tar.getmembers()
            require(len(members) == part.get("member_count"),
                    f"Declared member count differs: {path}")
            for member in members:
                require(member.isfile(), f"Non-regular tar member: {path}:{member.name}")
                match = re.fullmatch(r"objects/([a-f0-9]{64})\.bin", member.name)
                require(match is not None, f"Unexpected tar object locator: {path}:{member.name}")
                if match is None or not member.isfile():
                    continue
                obj = tar.extractfile(member)
                body = obj.read() if obj else b""
                require(digest(body) == match.group(1),
                        f"Content-addressed payload mismatch: {path}:{member.name}")
                require(member.name not in all_members,
                        f"Duplicate content object across parts: {member.name}")
                all_members.add(member.name)
                member_count += 1
    require(member_count == record["public_unique_payloads"] == 1162,
            "Content-addressed object cardinality mismatch")

    ledger = load_json(f"{EVIDENCE}/local-source-ledger.json")
    require(ledger.get("format") == "gzip-csv-base64-v1", "Ledger encoding drift")
    ledger_bytes = decode_gzip(ledger["data_base64"], ledger["gzip_sha256"])
    rows = list(csv.DictReader(io.StringIO(ledger_bytes.decode("utf-8"))))
    require(len(rows) == ledger.get("rows") == record["source_artifacts"] == 4267,
            "Local source ledger cardinality mismatch")
    dispositions = record.get("dispositions", {})
    if dispositions:
        require(sum(dispositions.values()) == len(rows),
                "Source disposition totals do not reconcile to ledger rows")

    require(record.get("latest_capture_summary", {}).get("prospective_dataset_member") is False,
            "Prior source capture has become prospective")
    return {"mode": "offline_read_only_transport_integrity",
            "package": "2026-10-24/04-local-history-evidence-handoff",
            "checks": checks, "failed": len(failures), "failures": failures[:30],
            "listed_artifact_files": len(entries), "manifest_file_self_excluded": 1, "attempt_rows": attempt_rows,
            "redacted_or_unavailable_public_endpoint_rows": unknown_endpoints,
            "payloads": member_count, "ledger_rows": len(rows),
            "new_live_requests": 0, "scientific_interpretation_verified": False}


if __name__ == "__main__":
    try:
        result = run()
    except Exception as exc:
        result = {"mode": "offline_read_only_transport_integrity",
                  "failed": 1, "failures": [f"{type(exc).__name__}: {exc}"],
                  "new_live_requests": 0, "scientific_interpretation_verified": False}
    print(json.dumps(result, indent=2))
    sys.exit(bool(result["failed"]))
