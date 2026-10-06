#!/usr/bin/env python3
"""Retrieve frozen-membership Zenodo first-version shards for the exploratory benchmark.

Observed Zenodo Records API contract used here:
- searchable: resource_type.type:software
- searchable: metadata.publication_date
- returned but not reliably searchable: metadata.relations.version.index
- all_versions=true keeps non-latest first versions retrievable

This script only retrieves and normalizes shard evidence. Benchmark cohort construction,
matching, and ranking live in aggregate_zenodo_new_family_benchmark.py so there is one
ranking implementation rather than two drifting copies.

Cohort membership is frozen with --created-cutoff. Platform statistics such as
stats.views remain live values observed during retrieval; they are not historical
values reconstructed at the membership cutoff.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

API = "https://zenodo.org/api/records"
UA = "research-software-identity-audit/zenodo-new-family-benchmark (+https://github.com/lostlight530/research-software-identity-audit)"


def fetch_json(url: str, retries: int = 8):
    last = None
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read()
                return json.loads(raw), raw, dict(resp.headers)
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code == 429 or 500 <= exc.code < 600:
                retry_after = exc.headers.get("Retry-After")
                delay = float(retry_after) if retry_after and retry_after.isdigit() else min(2 ** attempt, 60)
                time.sleep(delay)
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            time.sleep(min(2 ** attempt, 60))
    raise RuntimeError(f"request failed after {retries} attempts: {url}: {last}")


def total_value(value):
    if isinstance(value, dict):
        return int(value.get("value", 0))
    return int(value or 0)


def iter_dates(start: str, end: str):
    cur = date.fromisoformat(start)
    stop = date.fromisoformat(end)
    if stop < cur:
        raise ValueError(f"end date {end} precedes start date {start}")
    while cur <= stop:
        yield cur.isoformat()
        cur += timedelta(days=1)


def md(record):
    return record.get("metadata") or {}


def version_relation(record):
    rels = md(record).get("relations") or {}
    versions = rels.get("version") or []
    return versions[0] if versions else {}


def version_index(record):
    try:
        return int(version_relation(record).get("index"))
    except (TypeError, ValueError):
        return None


def family_id(record):
    if record.get("conceptrecid") is not None:
        return str(record["conceptrecid"])
    parent = version_relation(record).get("parent") or {}
    if parent.get("pid_value") is not None:
        return str(parent["pid_value"])
    return ""


def concept_doi(record):
    value = record.get("conceptdoi")
    if value:
        return str(value).lower()
    fid = family_id(record)
    return f"10.5281/zenodo.{fid}" if fid.isdigit() else ""


def record_doi(record):
    value = record.get("doi")
    if value:
        return str(value).lower()
    pids = record.get("pids") or {}
    return str((pids.get("doi") or {}).get("identifier") or "").lower()


def pubdate(record):
    return str(md(record).get("publication_date") or "")


def stat(record, key):
    try:
        return int((record.get("stats") or {}).get(key, 0) or 0)
    except (TypeError, ValueError):
        return 0


def save_raw(raw_dir: Path, day: str, page: int, raw: bytes, url: str, evidence, headers):
    path = raw_dir / day / f"page-{page:05d}.json.gz"
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wb") as fh:
        fh.write(raw)
    evidence.append({
        "path": str(path),
        "url": url,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "ratelimit_limit": headers.get("X-RateLimit-Limit"),
        "ratelimit_remaining": headers.get("X-RateLimit-Remaining"),
        "ratelimit_reset": headers.get("X-RateLimit-Reset"),
    })


def search_day(day: str, raw_dir: Path, evidence, created_cutoff: str):
    query = (
        "resource_type.type:software "
        f"AND metadata.publication_date:[{day} TO {day}] "
        f'AND created:[* TO "{created_cutoff}"]'
    )
    page = 1
    records = []
    reported_total_first = None
    reported_total_last = None
    size = 100

    while True:
        params = urllib.parse.urlencode({
            "q": query,
            "all_versions": "true",
            "page": page,
            "size": size,
            "sort": "mostrecent",
        })
        url = f"{API}?{params}"
        try:
            payload, raw, headers = fetch_json(url)
        except urllib.error.HTTPError as exc:
            # Current anonymous deployments may cap page size below 100.
            if exc.code == 400 and page == 1 and size != 25:
                size = 25
                continue
            raise

        save_raw(raw_dir, day, page, raw, url, evidence, headers)
        hits_obj = payload.get("hits") or {}
        hits = hits_obj.get("hits") or []
        reported = total_value(hits_obj.get("total"))
        if reported_total_first is None:
            reported_total_first = reported
        reported_total_last = reported

        for rec in hits:
            if pubdate(rec) != day:
                raise RuntimeError(
                    f"date-shard drift on {day}: record {rec.get('id')} publication_date={pubdate(rec)!r}"
                )
        records.extend(hits)

        next_url = (payload.get("links") or {}).get("next")
        if not next_url or not hits:
            break
        page += 1
        time.sleep(0.15)

    return records, {
        "date": day,
        "page_size": size,
        "pages": page,
        "records_retrieved": len(records),
        "reported_total_first": reported_total_first,
        "reported_total_last": reported_total_last,
        "total_changed_during_shard": reported_total_first != reported_total_last,
    }


def normalize(record):
    return {
        "family_id": family_id(record),
        "concept_doi": concept_doi(record),
        "first_record_id": str(record.get("id") or record.get("recid") or ""),
        "first_version_doi": record_doi(record),
        "first_publication_date": pubdate(record),
        "title": md(record).get("title") or record.get("title") or "",
        "is_last": bool(version_relation(record).get("is_last")),
        "views": stat(record, "views"),
        "unique_views": stat(record, "unique_views"),
        "downloads": stat(record, "downloads"),
        "unique_downloads": stat(record, "unique_downloads"),
        "version_views": stat(record, "version_views"),
        "version_unique_views": stat(record, "version_unique_views"),
        "version_downloads": stat(record, "version_downloads"),
        "version_unique_downloads": stat(record, "version_unique_downloads"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", required=True)
    ap.add_argument("--output", default="shard-output")
    ap.add_argument(
        "--created-cutoff",
        required=True,
        help="UTC cutoff that freezes benchmark membership; stats remain live at retrieval time.",
    )
    args = ap.parse_args()

    # Validate without changing the supplied ISO text used in provenance.
    datetime.fromisoformat(args.created_cutoff.replace("Z", "+00:00"))

    out = Path(args.output)
    raw_dir = out / "raw-first-version-pages"
    raw_dir.mkdir(parents=True, exist_ok=True)
    evidence = []
    shard_summaries = []
    by_family = {}
    duplicate_family_records = []
    run_started = datetime.now(timezone.utc).isoformat()

    for day in iter_dates(args.start, args.end):
        records, shard = search_day(day, raw_dir, evidence, args.created_cutoff)
        shard_summaries.append(shard)
        print(json.dumps(shard), flush=True)
        for rec in records:
            if version_index(rec) != 0:
                continue
            fid = family_id(rec)
            if not fid:
                raise RuntimeError(f"first-version record without family id: {rec.get('id')}")
            if fid in by_family:
                duplicate_family_records.append({
                    "family_id": fid,
                    "kept_record_id": str(by_family[fid].get("id")),
                    "duplicate_record_id": str(rec.get("id")),
                })
                if str(rec.get("id")) < str(by_family[fid].get("id")):
                    by_family[fid] = rec
            else:
                by_family[fid] = rec

    cohort = [normalize(rec) for rec in by_family.values()]
    cohort.sort(key=lambda x: (x["first_publication_date"], x["family_id"]))
    if not cohort:
        raise RuntimeError("eligible newborn software-family shard is empty")

    with (out / "cohort.csv").open("w", newline="", encoding="utf-8") as fh:
        fields = list(cohort[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(cohort)

    shard_summary = {
        "benchmark_class": "exploratory_new_zenodo_software_family_shard",
        "prospective_dataset_member": False,
        "start": args.start,
        "end": args.end,
        "created_cutoff": args.created_cutoff,
        "run_started_utc": run_started,
        "run_finished_utc": datetime.now(timezone.utc).isoformat(),
        "eligible_first_version_family_count": len(cohort),
        "duplicate_family_record_count": len(duplicate_family_records),
        "duplicates": duplicate_family_records,
        "shards": shard_summaries,
        "raw_evidence": evidence,
        "metric_snapshot_semantics": (
            "Membership is frozen by created_cutoff. stats.* values are live observations made during this "
            "retrieval interval and are not reconstructed historical values at the cutoff."
        ),
    }
    (out / "shard-summary.json").write_text(
        json.dumps(shard_summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "shard_start": args.start,
        "shard_end": args.end,
        "eligible_first_version_families": len(cohort),
        "raw_pages": len(evidence),
    }, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()