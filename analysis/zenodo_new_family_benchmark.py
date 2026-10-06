#!/usr/bin/env python3
"""Exploratory Zenodo newborn-software-family benchmark.

This utility is deliberately separate from the preregistered prospective dataset.
It defines a cohort by first-version publication date and ranks concept families
by Zenodo family-cumulative views. Unknown/partial retrievals abort the run.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import math
import os
import statistics
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://zenodo.org/api/records"
UA = "research-software-identity-audit/zenodo-new-family-benchmark (+https://github.com/lostlight530/research-software-identity-audit)"


def fetch_json(url: str, retries: int = 7):
    last = None
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = resp.read()
                return json.loads(body), body, dict(resp.headers)
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


def version_relation(record):
    versions = ((record.get("relations") or {}).get("version") or [])
    return versions[0] if versions else {}


def first_version(record):
    rel = version_relation(record)
    try:
        return int(rel.get("index")) == 0
    except (TypeError, ValueError):
        return False


def family_id(record):
    for key in ("conceptrecid", "conceptid"):
        if record.get(key) is not None:
            return str(record[key])
    parent = version_relation(record).get("parent") or {}
    if parent.get("pid_value") is not None:
        return str(parent["pid_value"])
    return ""


def doi_of(record):
    doi = record.get("doi")
    if doi:
        return str(doi).lower()
    pids = record.get("pids") or {}
    d = pids.get("doi") or {}
    if d.get("identifier"):
        return str(d["identifier"]).lower()
    return ""


def concept_doi_of(record):
    v = record.get("conceptdoi")
    if v:
        return str(v).lower()
    rel = version_relation(record)
    parent = rel.get("parent") or {}
    # Numeric Zenodo parent identifiers map to concept DOI suffixes.
    pid = parent.get("pid_value")
    if pid and str(pid).isdigit():
        return f"10.5281/zenodo.{pid}"
    return ""


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
    s = sum(xs)
    if n == 0 or s == 0:
        return 0.0
    return (2 * sum((i + 1) * x for i, x in enumerate(xs)) / (n * s)) - (n + 1) / n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default="2026-09-16")
    ap.add_argument("--end", default="2026-10-06")
    ap.add_argument("--targets", default="baseline/2026-10-05/doi-map.csv")
    ap.add_argument("--output", default="benchmark-output")
    args = ap.parse_args()

    out = Path(args.output)
    raw_dir = out / "raw-pages"
    raw_dir.mkdir(parents=True, exist_ok=True)

    q = f"resource_type.type:software AND metadata.publication_date:[{args.start} TO {args.end}] AND relations.version.index:0"
    page = 1
    all_records = []
    raw_hashes = []
    reported_total = None

    while True:
        params = urllib.parse.urlencode({
            "q": q,
            "all_versions": "true",
            "page": page,
            "size": 25,
        })
        url = f"{API}?{params}"
        payload, raw, headers = fetch_json(url)

        raw_path = raw_dir / f"page-{page:05d}.json.gz"
        with gzip.open(raw_path, "wb") as fh:
            fh.write(raw)
        raw_hashes.append({
            "page": page,
            "url": url,
            "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw),
        })

        hits_obj = payload.get("hits") or {}
        hits = hits_obj.get("hits") or []
        if reported_total is None:
            reported_total = total_value(hits_obj.get("total"))

        all_records.extend(hits)
        next_link = (payload.get("links") or {}).get("next")
        if not next_link or not hits:
            break
        page += 1
        time.sleep(0.15)

    first = [r for r in all_records if first_version(r)]
    by_family = {}
    duplicates = []
    for rec in first:
        fid = family_id(rec)
        if not fid:
            raise RuntimeError(f"first-version record without family identifier: {rec.get('id') or rec.get('recid')}")
        if fid in by_family:
            duplicates.append(fid)
            # Keep deterministic winner but surface duplicate explicitly.
            prev = by_family[fid]
            prev_id = str(prev.get("id") or prev.get("recid") or "")
            cur_id = str(rec.get("id") or rec.get("recid") or "")
            if cur_id < prev_id:
                by_family[fid] = rec
        else:
            by_family[fid] = rec

    cohort = []
    for fid, rec in by_family.items():
        md = rec.get("metadata") or {}
        cohort.append({
            "family_id": fid,
            "concept_doi": concept_doi_of(rec),
            "first_record_id": str(rec.get("id") or rec.get("recid") or ""),
            "first_version_doi": doi_of(rec),
            "publication_date": md.get("publication_date"),
            "title": md.get("title") or rec.get("title"),
            "views": stat(rec, "views"),
            "unique_views": stat(rec, "unique_views"),
            "downloads": stat(rec, "downloads"),
            "unique_downloads": stat(rec, "unique_downloads"),
            "version_views": stat(rec, "version_views"),
            "version_unique_views": stat(rec, "version_unique_views"),
        })

    cohort.sort(key=lambda x: (-x["views"], x["family_id"]))
    n = len(cohort)
    if n == 0:
        raise RuntimeError("eligible first-version cohort is empty")

    views = [x["views"] for x in cohort]
    for item in cohort:
        v = item["views"]
        greater = sum(1 for x in views if x > v)
        equal = sum(1 for x in views if x == v)
        rank_min = greater + 1
        rank_max = greater + equal
        item["rank_min"] = rank_min
        item["rank_max"] = rank_max
        item["tie_count"] = equal
        item["percentile_from_rank_min"] = round(100 * (n - rank_min + 1) / n, 4)
        item["top_fraction_percent"] = round(100 * rank_min / n, 4)

    targets = []
    with open(args.targets, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            concept = row["concept_doi"].lower()
            suffix = concept.rsplit(".", 1)[-1]
            match = next((x for x in cohort if x["concept_doi"] == concept or x["family_id"] == suffix), None)
            targets.append({
                "object_id": row["object_id"],
                "repository": row["repository"],
                "concept_doi": row["concept_doi"],
                "match": match,
            })

    missing_targets = [t for t in targets if t["match"] is None]
    if missing_targets:
        raise RuntimeError("target families missing from cohort: " + ", ".join(t["repository"] for t in missing_targets))

    target_views = [t["match"]["views"] for t in targets]
    shares = [v / sum(target_views) for v in target_views] if sum(target_views) else [0] * len(target_views)
    hhi = sum(s * s for s in shares)

    summary = {
        "benchmark_class": "exploratory_new_zenodo_software_family",
        "prospective_dataset_member": False,
        "start": args.start,
        "end": args.end,
        "query": q,
        "all_versions": True,
        "raw_window_record_count": len(all_records),
        "api_reported_total": reported_total,
        "first_version_record_count": len(first),
        "exact_concept_family_count": n,
        "duplicate_first_version_family_ids": sorted(set(duplicates)),
        "ranking_metric": "stats.views (family cumulative)",
        "cohort": {
            "median_views": statistics.median(views),
            "p75_views_linear": quantile_linear(views, 0.75),
            "p90_views_linear": quantile_linear(views, 0.90),
            "p95_views_linear": quantile_linear(views, 0.95),
            "max_views": max(views),
            "min_views": min(views),
        },
        "targets": targets,
        "target_portfolio": {
            "views_total": sum(target_views),
            "median_views": statistics.median(target_views),
            "min_views": min(target_views),
            "max_views": max(target_views),
            "hhi": hhi,
            "effective_repository_count": (1 / hhi) if hhi else None,
            "gini": gini(target_views),
        },
        "raw_pages": raw_hashes,
    }

    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with open(out / "cohort.csv", "w", newline="", encoding="utf-8") as fh:
        fields = list(cohort[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(cohort)
    with open(out / "targets.csv", "w", newline="", encoding="utf-8") as fh:
        fields = ["object_id", "repository", "concept_doi", "views", "unique_views", "rank_min", "rank_max", "tie_count", "percentile_from_rank_min", "top_fraction_percent"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for t in targets:
            m = t["match"]
            w.writerow({k: (t.get(k) if k in t else m.get(k)) for k in fields})

    print(json.dumps({
        "cohort_n": n,
        "raw_records": len(all_records),
        "median": summary["cohort"]["median_views"],
        "p75": summary["cohort"]["p75_views_linear"],
        "p90": summary["cohort"]["p90_views_linear"],
        "p95": summary["cohort"]["p95_views_linear"],
        "targets": [
            {
                "repo": t["repository"],
                "views": t["match"]["views"],
                "rank": [t["match"]["rank_min"], t["match"]["rank_max"]],
                "percentile": t["match"]["percentile_from_rank_min"],
            }
            for t in targets
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
