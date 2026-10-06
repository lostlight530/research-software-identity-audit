#!/usr/bin/env python3
"""Exact exploratory benchmark for newborn Zenodo Software concept families.

Cohort contract:
- family first publication date in [start, end]
- unit = Zenodo concept family
- ranking metric = latest record family-cumulative stats.views

Retrieval strategy:
1) Search latest Software records by publication date, split by the officially
   searchable relations.version.count field.
2) count == 1 records are newborn on their publication date.
3) count >= 2 records are candidates; follow each record's links.versions and
   locate metadata.relations.version.index == 0 to establish family birth.
4) Abort on unresolved/missing target evidence; never impute.

This is exploratory analysis and is not a preregistered prospective observation.
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
from datetime import date, timedelta
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


def metadata(record):
    return record.get("metadata") or {}


def version_relation(record):
    rels = metadata(record).get("relations") or record.get("relations") or {}
    versions = rels.get("version") or []
    return versions[0] if versions else {}


def version_index(record):
    try:
        return int(version_relation(record).get("index"))
    except (TypeError, ValueError):
        return None


def family_id(record):
    for key in ("conceptrecid", "conceptid"):
        if record.get(key) is not None:
            return str(record[key])
    parent = version_relation(record).get("parent") or {}
    if parent.get("pid_value") is not None:
        return str(parent["pid_value"])
    return ""


def concept_doi(record):
    value = record.get("conceptdoi")
    if value:
        return str(value).lower()
    parent = version_relation(record).get("parent") or {}
    pid = parent.get("pid_value")
    if pid and str(pid).isdigit():
        return f"10.5281/zenodo.{pid}"
    return ""


def record_doi(record):
    if record.get("doi"):
        return str(record["doi"]).lower()
    pids = record.get("pids") or {}
    doi = pids.get("doi") or {}
    return str(doi.get("identifier") or "").lower()


def pubdate(record):
    return str(metadata(record).get("publication_date") or record.get("publication_date") or "")


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


def save_raw(raw_dir: Path, relpath: str, raw: bytes, url: str, evidence):
    path = raw_dir / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wb") as fh:
        fh.write(raw)
    evidence.append({
        "path": str(path),
        "url": url,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
    })


def search_pages(query: str, raw_dir: Path, raw_prefix: str, evidence):
    page = 1
    records = []
    reported_total = None
    while True:
        params = urllib.parse.urlencode({
            "q": query,
            "all_versions": "false",
            "page": page,
            "size": 25,
        })
        url = f"{API}?{params}"
        payload, raw, headers = fetch_json(url)
        save_raw(raw_dir, f"{raw_prefix}/page-{page:05d}.json.gz", raw, url, evidence)
        hits_obj = payload.get("hits") or {}
        hits = hits_obj.get("hits") or []
        if reported_total is None:
            reported_total = total_value(hits_obj.get("total"))
        records.extend(hits)
        next_url = (payload.get("links") or {}).get("next")
        if not next_url or not hits:
            break
        page += 1
        # Be polite; fetch_json also obeys Retry-After on 429.
        time.sleep(0.20)
    if reported_total is not None and len(records) != reported_total:
        raise RuntimeError(
            f"pagination mismatch for {query!r}: reported={reported_total}, retrieved={len(records)}"
        )
    return records


def fetch_versions(latest_record, raw_dir: Path, evidence):
    url = (latest_record.get("links") or {}).get("versions")
    if not url:
        raise RuntimeError(
            f"multi-version family {family_id(latest_record)} lacks links.versions"
        )

    page = 1
    versions = []
    current = url
    while current:
        # The versions endpoint may already include query parameters.
        parsed = urllib.parse.urlsplit(current)
        params = dict(urllib.parse.parse_qsl(parsed.query, keep_blank_values=True))
        params.setdefault("size", "25")
        params["page"] = str(page)
        current_url = urllib.parse.urlunsplit(
            (parsed.scheme, parsed.netloc, parsed.path, urllib.parse.urlencode(params), parsed.fragment)
        )
        payload, raw, headers = fetch_json(current_url)
        fid = family_id(latest_record) or str(latest_record.get("id") or "unknown")
        save_raw(raw_dir, f"versions/{fid}/page-{page:05d}.json.gz", raw, current_url, evidence)
        hits_obj = payload.get("hits") or {}
        hits = hits_obj.get("hits") or []
        versions.extend(hits)
        next_url = (payload.get("links") or {}).get("next")
        if not next_url or not hits:
            break
        current = next_url
        page += 1
        time.sleep(0.20)
    return versions


def normalize_latest(record, birth_record, birth_source):
    md = metadata(record)
    return {
        "family_id": family_id(record),
        "concept_doi": concept_doi(record),
        "latest_record_id": str(record.get("id") or record.get("recid") or ""),
        "latest_version_doi": record_doi(record),
        "latest_publication_date": pubdate(record),
        "first_record_id": str(birth_record.get("id") or birth_record.get("recid") or ""),
        "first_version_doi": record_doi(birth_record),
        "first_publication_date": pubdate(birth_record),
        "birth_source": birth_source,
        "title": md.get("title") or record.get("title") or "",
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
    args = ap.parse_args()

    out = Path(args.output)
    raw_dir = out / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    evidence = []

    latest_single = []
    latest_multi = []
    shard_counts = []

    for day in iter_dates(args.start, args.end):
        q_single = (
            f"resource_type.type:software AND publicationdate:{day} "
            "AND relations.version.count:1"
        )
        q_multi = (
            f"resource_type.type:software AND publicationdate:{day} "
            "AND relations.version.count:[2 TO *]"
        )
        singles = search_pages(q_single, raw_dir, f"latest/single/{day}", evidence)
        multis = search_pages(q_multi, raw_dir, f"latest/multi/{day}", evidence)
        latest_single.extend(singles)
        latest_multi.extend(multis)
        shard_counts.append({"date": day, "single": len(singles), "multi": len(multis)})
        print(json.dumps({"date": day, "single": len(singles), "multi": len(multis)}), flush=True)

    latest_by_family = {}
    source_class = {}
    for rec in latest_single:
        fid = family_id(rec)
        if not fid:
            raise RuntimeError(f"single-version record without family id: {rec.get('id')}")
        latest_by_family[fid] = rec
        source_class[fid] = "single"
    for rec in latest_multi:
        fid = family_id(rec)
        if not fid:
            raise RuntimeError(f"multi-version record without family id: {rec.get('id')}")
        if fid in latest_by_family and latest_by_family[fid].get("id") != rec.get("id"):
            raise RuntimeError(f"family {fid} appeared in both single and multi latest sets")
        latest_by_family[fid] = rec
        source_class[fid] = "multi"

    cohort = []
    excluded_old_families = []
    unresolved = []

    for fid, latest in latest_by_family.items():
        if source_class[fid] == "single":
            birth = latest
            birth_source = "version_count_1"
        else:
            versions = fetch_versions(latest, raw_dir, evidence)
            firsts = [v for v in versions if version_index(v) == 0]
            if len(firsts) != 1:
                unresolved.append({
                    "family_id": fid,
                    "reason": "expected_exactly_one_version_index_0",
                    "observed_first_count": len(firsts),
                    "version_records_retrieved": len(versions),
                })
                continue
            birth = firsts[0]
            birth_source = "links.versions_index_0"

        first_date = pubdate(birth)
        if not first_date:
            unresolved.append({"family_id": fid, "reason": "missing_first_publication_date"})
            continue

        if args.start <= first_date <= args.end:
            cohort.append(normalize_latest(latest, birth, birth_source))
        else:
            excluded_old_families.append({
                "family_id": fid,
                "concept_doi": concept_doi(latest),
                "title": metadata(latest).get("title") or latest.get("title") or "",
                "latest_publication_date": pubdate(latest),
                "first_publication_date": first_date,
            })

    if unresolved:
        (out / "unresolved.json").write_text(
            json.dumps(unresolved, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        raise RuntimeError(f"unresolved family birth evidence for {len(unresolved)} families")

    # A latest-only family should be unique in the cohort.
    ids = [x["family_id"] for x in cohort]
    if len(ids) != len(set(ids)):
        raise RuntimeError("duplicate concept family in final cohort")

    cohort.sort(key=lambda x: (-x["views"], x["family_id"]))
    n = len(cohort)
    if n == 0:
        raise RuntimeError("eligible newborn software-family cohort is empty")

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

    target_rows = []
    with open(args.targets, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            concept = row["concept_doi"].lower()
            suffix = concept.rsplit(".", 1)[-1]
            match = next(
                (x for x in cohort if x["concept_doi"] == concept or x["family_id"] == suffix),
                None,
            )
            if match is None:
                raise RuntimeError(f"target family missing from cohort: {row['repository']} {concept}")
            index = cohort.index(match)
            above = cohort[max(0, index - 5):index]
            below = cohort[index + 1:index + 6]
            target_rows.append({
                "object_id": row["object_id"],
                "repository": row["repository"],
                "concept_doi": row["concept_doi"],
                "match": match,
                "nearest_above": [
                    {"family_id": x["family_id"], "title": x["title"], "views": x["views"], "rank_min": x["rank_min"]}
                    for x in above
                ],
                "nearest_below": [
                    {"family_id": x["family_id"], "title": x["title"], "views": x["views"], "rank_min": x["rank_min"]}
                    for x in below
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
        "cohort_contract": {
            "resource_type": "software",
            "first_publication_date_start": args.start,
            "first_publication_date_end": args.end,
            "unit": "concept_family",
            "ranking_metric": "latest_record.stats.views_family_cumulative",
        },
        "retrieval_strategy": "latest_only_daily_shards_plus_versions_for_multiversion_families",
        "latest_candidate_family_count": len(latest_by_family),
        "single_version_candidate_count": len(latest_single),
        "multi_version_candidate_count": len(latest_multi),
        "excluded_pre_window_family_count": len(excluded_old_families),
        "exact_concept_family_count": n,
        "shard_counts": shard_counts,
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
    (out / "excluded-old-families.json").write_text(
        json.dumps(excluded_old_families, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
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
            "top_fraction_percent", "first_publication_date", "latest_publication_date",
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
        "candidate_families": len(latest_by_family),
        "excluded_old_families": len(excluded_old_families),
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
