#!/usr/bin/env python3
"""Retrieve evidence shards for the exploratory Zenodo birth-cohort benchmark.

Evidence-backed retrieval contract for the current Zenodo Records API:
- searchable: resource_type.type:software
- searchable: metadata.publication_date
- returned but not reliably searchable: metadata.relations.version.index
- all_versions=true so non-latest first versions remain retrievable

The retrieval unit is the concept family. Eligibility is determined client-side
from metadata.relations.version.index == 0 after date-sharded retrieval, with
first publication date in [start, end]. Ranking is performed by the separate
aggregator so the primary comparison can be age-matched to the target birth date.

The date window is sharded by day to stay below the search API's 10k result
window. Raw pages and hashes are retained. This is exploratory analysis, not a
preregistered prospective observation.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import math
import statistics
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


def quantile_linear(values, q):
    xs = sorted(values)
    if not xs:
        return None
    if len(xs) == 1:
        return float(xs[0])
    pos = (len(xs) - 1) * q
    lo = math.floor(pos)
    hi = math.ceil(pos)
    if lo == hi:
        return float(xs[lo])
    frac = pos - lo
    return xs[lo] * (1 - frac) + xs[hi] * frac


def gini(values):
    xs = sorted(float(x) for x in values if x >= 0)
    n = len(xs)
    total = sum(xs)
    if n == 0 or total == 0:
        return 0.0
    return (2 * sum((i + 1) * x for i, x in enumerate(xs)) / (n * total)) - (n + 1) / n


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


def search_day(day: str, raw_dir: Path, evidence, created_cutoff=None):
    query = (
        "resource_type.type:software "
        f"AND metadata.publication_date:[{day} TO {day}]"
    )
    if created_cutoff:
        query += f' AND created:[* TO "{created_cutoff}"]'
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

    # Live Zenodo can change during retrieval. We preserve both totals and
    # require only that every returned family is unique after global dedup.
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
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default="2026-09-16")
    ap.add_argument("--end", default="2026-10-06")
    ap.add_argument("--targets", default="baseline/2026-10-05/doi-map.csv")
    ap.add_argument("--output", default="benchmark-output")
    ap.add_argument("--shard-only", action="store_true")
    ap.add_argument("--created-cutoff", required=False)
    args = ap.parse_args()

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
                # Deterministic tie-break; duplicates remain explicitly reported.
                if str(rec.get("id")) < str(by_family[fid].get("id")):
                    by_family[fid] = rec
            else:
                by_family[fid] = rec

    cohort = [normalize(rec) for rec in by_family.values()]
    cohort.sort(key=lambda x: (-x["views"], x["family_id"]))
    n = len(cohort)
    if n == 0:
        raise RuntimeError("eligible newborn software-family cohort is empty")

    if args.shard_only:
        fields = list(cohort[0].keys())
        with open(out / "cohort.csv", "w", newline="", encoding="utf-8") as fh:
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
            "eligible_first_version_family_count": n,
            "duplicate_family_record_count": len(duplicate_family_records),
            "duplicates": duplicate_family_records,
            "shards": shard_summaries,
            "raw_evidence": evidence,
        }
        (out / "shard-summary.json").write_text(
            json.dumps(shard_summary, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(json.dumps({
            "shard_start": args.start,
            "shard_end": args.end,
            "eligible_first_version_families": n,
            "raw_pages": len(evidence),
        }, ensure_ascii=False), flush=True)
        return

    # Sanity-check the ten preregistered software families before ranking.
    target_rows = []
    with open(args.targets, newline="", encoding="utf-8") as fh:
        target_manifest = list(csv.DictReader(fh))

    target_concepts = {r["concept_doi"].lower(): r for r in target_manifest}
    found_target_concepts = {x["concept_doi"] for x in cohort if x["concept_doi"] in target_concepts}
    if len(found_target_concepts) != len(target_manifest):
        missing = sorted(set(target_concepts) - found_target_concepts)
        raise RuntimeError(f"target family missing from exact cohort: {missing}")

    views = [x["views"] for x in cohort]
    for item in cohort:
        v = item["views"]
        greater = sum(1 for x in views if x > v)
        equal = sum(1 for x in views if x == v)
        item["rank_min"] = greater + 1
        item["rank_max"] = greater + equal
        item["tie_count"] = equal
        item["percentile_from_rank_min"] = round(100 * (n - item["rank_min"] + 1) / n, 4)
        item["top_fraction_percent"] = round(100 * item["rank_min"] / n, 4)

    for manifest in target_manifest:
        concept = manifest["concept_doi"].lower()
        match = next(x for x in cohort if x["concept_doi"] == concept)
        idx = cohort.index(match)
        target_rows.append({
            "object_id": manifest["object_id"],
            "repository": manifest["repository"],
            "concept_doi": manifest["concept_doi"],
            "match": match,
            "nearest_above": [
                {"family_id": x["family_id"], "title": x["title"], "views": x["views"], "rank_min": x["rank_min"]}
                for x in cohort[max(0, idx - 5):idx]
            ],
            "nearest_below": [
                {"family_id": x["family_id"], "title": x["title"], "views": x["views"], "rank_min": x["rank_min"]}
                for x in cohort[idx + 1:idx + 6]
            ],
        })

    target_views = [t["match"]["views"] for t in target_rows]
    target_total = sum(target_views)
    shares = [v / target_total for v in target_views] if target_total else [0.0] * len(target_views)
    hhi = sum(s * s for s in shares)
    cohort_median = statistics.median(views)

    summary = {
        "benchmark_class": "exploratory_new_zenodo_software_family",
        "prospective_dataset_member": False,
        "run_started_utc": run_started,
        "run_finished_utc": datetime.now(timezone.utc).isoformat(),
        "cohort_contract": {
            "resource_type": "software",
            "first_publication_date_start": args.start,
            "first_publication_date_end": args.end,
            "unit": "concept_family",
            "eligibility_query": "client-side metadata.relations.version.index == 0",
            "ranking_metric": "stats.views (family cumulative)",
            "version_local_control": "stats.version_views",
        },
        "retrieval_strategy": "daily publication-date shards with all_versions=true, then client-side index==0 filter",
        "exact_concept_family_count": n,
        "duplicate_family_record_count": len(duplicate_family_records),
        "duplicates": duplicate_family_records,
        "shards": shard_summaries,
        "cohort": {
            "median_views": cohort_median,
            "p75_views_linear": quantile_linear(views, 0.75),
            "p90_views_linear": quantile_linear(views, 0.90),
            "p95_views_linear": quantile_linear(views, 0.95),
            "min_views": min(views),
            "max_views": max(views),
        },
        "targets": target_rows,
        "target_portfolio": {
            "views_total": target_total,
            "median_views": statistics.median(target_views),
            "min_views": min(target_views),
            "max_views": max(target_views),
            "median_vs_cohort_median_multiplier": (
                statistics.median(target_views) / cohort_median if cohort_median else None
            ),
            "floor_vs_cohort_median_multiplier": (
                min(target_views) / cohort_median if cohort_median else None
            ),
            "hhi": hhi,
            "effective_repository_count": (1 / hhi) if hhi else None,
            "gini": gini(target_views),
        },
        "raw_evidence": evidence,
    }

    (out / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    with open(out / "cohort.csv", "w", newline="", encoding="utf-8") as fh:
        fields = list(cohort[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(cohort)

    with open(out / "targets.csv", "w", newline="", encoding="utf-8") as fh:
        fields = [
            "object_id", "repository", "concept_doi", "views", "unique_views",
            "rank_min", "rank_max", "tie_count", "percentile_from_rank_min",
            "top_fraction_percent", "first_publication_date", "is_last",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for target in target_rows:
            row = {
                "object_id": target["object_id"],
                "repository": target["repository"],
                "concept_doi": target["concept_doi"],
            }
            for key in fields:
                if key not in row:
                    row[key] = target["match"].get(key)
            w.writerow(row)

    print(json.dumps({
        "cohort_n": n,
        "median_views": cohort_median,
        "p75_views": summary["cohort"]["p75_views_linear"],
        "p90_views": summary["cohort"]["p90_views_linear"],
        "p95_views": summary["cohort"]["p95_views_linear"],
        "targets": [
            {
                "repo": t["repository"],
                "views": t["match"]["views"],
                "rank": [t["match"]["rank_min"], t["match"]["rank_max"]],
                "percentile": t["match"]["percentile_from_rank_min"],
                "top_percent": t["match"]["top_fraction_percent"],
            }
            for t in target_rows
        ],
    }, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
