#!/usr/bin/env python3
"""Aggregate Zenodo evidence shards into an age-matched primary benchmark.

The primary cohort matches the targets by first publication date. The wider
retrieval window is retained only as secondary context. Cohort membership is
frozen by the shared created cutoff; stats.views remains a live platform metric
observed across a bounded retrieval interval rather than one exact instant.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from datetime import datetime, timezone
from pathlib import Path


def as_int(value):
    return int(value or 0)


def as_bool(value):
    return str(value).lower() in {"1", "true", "yes"}


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


def rank_rows(rows):
    ranked = [dict(row) for row in rows]
    ranked.sort(key=lambda x: (-x["views"], x["family_id"]))
    n = len(ranked)
    if n == 0:
        raise RuntimeError("cannot rank an empty cohort")
    values = [x["views"] for x in ranked]
    for item in ranked:
        v = item["views"]
        greater = sum(1 for x in values if x > v)
        equal = sum(1 for x in values if x == v)
        item["rank_min"] = greater + 1
        item["rank_max"] = greater + equal
        item["tie_count"] = equal
        item["percentile_from_rank_min"] = round(100 * (n - item["rank_min"] + 1) / n, 4)
        item["percentile_from_rank_max"] = round(100 * (n - item["rank_max"] + 1) / n, 4)
        item["top_fraction_percent_from_rank_min"] = round(100 * item["rank_min"] / n, 4)
        item["top_fraction_percent_from_rank_max"] = round(100 * item["rank_max"] / n, 4)
    return ranked


def cohort_stats(ranked):
    values = [x["views"] for x in ranked]
    return {
        "concept_family_count": len(ranked),
        "median_views": statistics.median(values),
        "p75_views_linear": quantile_linear(values, 0.75),
        "p90_views_linear": quantile_linear(values, 0.90),
        "p95_views_linear": quantile_linear(values, 0.95),
        "min_views": min(values),
        "max_views": max(values),
    }


def compact_neighbor(item):
    return {
        "family_id": item["family_id"],
        "title": item["title"],
        "views": item["views"],
        "rank_min": item["rank_min"],
        "rank_max": item["rank_max"],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--targets", default="baseline/2026-10-05/doi-map.csv")
    ap.add_argument("--output", default="benchmark-output")
    ap.add_argument("--primary-birth-date")
    args = ap.parse_args()

    root = Path(args.input)
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    cohort_files = sorted(root.glob("**/cohort.csv"))
    summary_files = sorted(root.glob("**/shard-summary.json"))
    if not cohort_files:
        raise RuntimeError(f"no cohort.csv shard files under {root}")

    by_family = {}
    duplicate_cross_shard = []
    for path in cohort_files:
        with path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                fid = row["family_id"]
                normalized = {
                    "family_id": fid,
                    "concept_doi": row["concept_doi"].lower(),
                    "first_record_id": row["first_record_id"],
                    "first_version_doi": row["first_version_doi"].lower(),
                    "first_publication_date": row["first_publication_date"],
                    "title": row["title"],
                    "is_last": as_bool(row["is_last"]),
                    "views": as_int(row["views"]),
                    "unique_views": as_int(row["unique_views"]),
                    "downloads": as_int(row["downloads"]),
                    "unique_downloads": as_int(row["unique_downloads"]),
                    "version_views": as_int(row["version_views"]),
                    "version_unique_views": as_int(row["version_unique_views"]),
                }
                if fid in by_family:
                    duplicate_cross_shard.append({
                        "family_id": fid,
                        "first": by_family[fid]["first_record_id"],
                        "duplicate": normalized["first_record_id"],
                        "source": str(path),
                    })
                    if normalized["first_record_id"] < by_family[fid]["first_record_id"]:
                        by_family[fid] = normalized
                else:
                    by_family[fid] = normalized

    cohort = rank_rows(list(by_family.values()))
    n = len(cohort)

    with open(args.targets, newline="", encoding="utf-8") as fh:
        target_manifest = list(csv.DictReader(fh))
    target_concepts = {r["concept_doi"].lower(): r for r in target_manifest}
    cohort_by_concept = {x["concept_doi"]: x for x in cohort}
    missing = sorted(set(target_concepts) - set(cohort_by_concept))
    if missing:
        raise RuntimeError(f"target family missing from retrieval window: {missing}")

    target_birth_dates = sorted({
        cohort_by_concept[concept]["first_publication_date"] for concept in target_concepts
    })
    if args.primary_birth_date:
        primary_birth_date = args.primary_birth_date
        mismatched = sorted(
            concept for concept in target_concepts
            if cohort_by_concept[concept]["first_publication_date"] != primary_birth_date
        )
        if mismatched:
            raise RuntimeError(
                f"targets do not all match primary birth date {primary_birth_date}: {mismatched}"
            )
    else:
        if len(target_birth_dates) != 1:
            raise RuntimeError(
                "targets do not share one first publication date; define a justified "
                "--primary-birth-date before ranking"
            )
        primary_birth_date = target_birth_dates[0]

    primary = rank_rows([
        row for row in cohort if row["first_publication_date"] == primary_birth_date
    ])
    primary_by_concept = {x["concept_doi"]: x for x in primary}
    missing_primary = sorted(set(target_concepts) - set(primary_by_concept))
    if missing_primary:
        raise RuntimeError(
            f"target family missing from age-matched primary cohort: {missing_primary}"
        )

    targets = []
    for concept, manifest in target_concepts.items():
        match = primary_by_concept[concept]
        window_match = cohort_by_concept[concept]
        idx = primary.index(match)
        targets.append({
            "object_id": manifest["object_id"],
            "repository": manifest["repository"],
            "concept_doi": manifest["concept_doi"],
            "match": match,
            "nearest_above": [compact_neighbor(x) for x in primary[max(0, idx - 5):idx]],
            "nearest_below": [compact_neighbor(x) for x in primary[idx + 1:idx + 6]],
            "secondary_window_rank": {
                "rank_min": window_match["rank_min"],
                "rank_max": window_match["rank_max"],
                "tie_count": window_match["tie_count"],
                "percentile_from_rank_min": window_match["percentile_from_rank_min"],
                "percentile_from_rank_max": window_match["percentile_from_rank_max"],
            },
        })

    targets.sort(key=lambda t: t["object_id"])
    target_views = [t["match"]["views"] for t in targets]
    target_total = sum(target_views)
    shares = [v / target_total for v in target_views] if target_total else [0.0] * len(target_views)
    hhi = sum(s * s for s in shares)
    primary_stats = cohort_stats(primary)
    window_stats = cohort_stats(cohort)

    shard_summaries = []
    unstable_shards = []
    raw_page_count = 0
    cutoffs = set()
    retrieval_starts = []
    retrieval_finishes = []
    for path in summary_files:
        data = json.loads(path.read_text(encoding="utf-8"))
        shard_summaries.append(data)
        raw_page_count += len(data.get("raw_evidence") or [])
        if data.get("created_cutoff"):
            cutoffs.add(data["created_cutoff"])
        if data.get("run_started_utc"):
            retrieval_starts.append(data["run_started_utc"])
        if data.get("run_finished_utc"):
            retrieval_finishes.append(data["run_finished_utc"])
        for shard in data.get("shards") or []:
            if shard.get("total_changed_during_shard"):
                unstable_shards.append(shard)

    if unstable_shards:
        (out / "unstable-shards.json").write_text(
            json.dumps(unstable_shards, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        raise RuntimeError(
            f"{len(unstable_shards)} date shards changed hit totals during retrieval; "
            "rerun before reporting the benchmark"
        )
    if len(cutoffs) != 1:
        raise RuntimeError(
            f"expected one shared created cutoff across shards, observed: {sorted(cutoffs)}"
        )

    summary = {
        "benchmark_class": "exploratory_age_matched_zenodo_software_family",
        "prospective_dataset_member": False,
        "aggregated_at_utc": datetime.now(timezone.utc).isoformat(),
        "cohort_contract": {
            "resource_type": "software",
            "unit": "concept_family",
            "eligibility": "metadata.relations.version.index == 0 after all_versions retrieval",
            "primary_match_rule": "first_publication_date equals the shared target first_publication_date",
            "primary_birth_date": primary_birth_date,
            "secondary_window_start": min(x["first_publication_date"] for x in cohort),
            "secondary_window_end": max(x["first_publication_date"] for x in cohort),
            "ranking_metric": "stats.views (family cumulative)",
            "version_local_control": "stats.version_views",
            "membership_created_cutoff_utc": next(iter(cutoffs)),
        },
        "metric_snapshot_semantics": (
            "Cohort membership is frozen by the shared created cutoff. stats.views is a live "
            "platform statistic observed across the shard retrieval interval; ranks are bounded "
            "observed-snapshot ranks, not a reconstruction of one exact event-time instant."
        ),
        "retrieval_window_utc": {
            "start": min(retrieval_starts) if retrieval_starts else None,
            "end": max(retrieval_finishes) if retrieval_finishes else None,
        },
        "retrieval_strategy": "7 parallel date-range shards; daily publication-date queries; all_versions=true; client-side index==0",
        "shard_artifact_count": len(cohort_files),
        "raw_page_count": raw_page_count,
        "duplicate_cross_shard_count": len(duplicate_cross_shard),
        "duplicates": duplicate_cross_shard,
        "primary_cohort": primary_stats,
        "secondary_window_cohort": window_stats,
        "targets": targets,
        "target_portfolio": {
            "views_total": target_total,
            "median_views": statistics.median(target_views),
            "min_views": min(target_views),
            "max_views": max(target_views),
            "median_vs_primary_cohort_median_multiplier": (
                statistics.median(target_views) / primary_stats["median_views"]
                if primary_stats["median_views"] else None
            ),
            "floor_vs_primary_cohort_median_multiplier": (
                min(target_views) / primary_stats["median_views"]
                if primary_stats["median_views"] else None
            ),
            "median_vs_secondary_window_median_multiplier": (
                statistics.median(target_views) / window_stats["median_views"]
                if window_stats["median_views"] else None
            ),
            "hhi": hhi,
            "effective_repository_count": (1 / hhi) if hhi else None,
            "gini": gini(target_views),
        },
        "shard_summaries": [
            {
                "start": x.get("start"),
                "end": x.get("end"),
                "eligible_first_version_family_count": x.get("eligible_first_version_family_count"),
                "raw_page_count": len(x.get("raw_evidence") or []),
            }
            for x in shard_summaries
        ],
    }

    (out / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    with (out / "primary-cohort.csv").open("w", newline="", encoding="utf-8") as fh:
        fields = list(primary[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(primary)
    with (out / "window-cohort.csv").open("w", newline="", encoding="utf-8") as fh:
        fields = list(cohort[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(cohort)
    with (out / "targets.csv").open("w", newline="", encoding="utf-8") as fh:
        fields = [
            "object_id", "repository", "concept_doi", "views", "unique_views",
            "rank_min", "rank_max", "tie_count", "percentile_from_rank_min",
            "percentile_from_rank_max", "top_fraction_percent_from_rank_min",
            "top_fraction_percent_from_rank_max", "first_publication_date", "is_last",
            "secondary_window_rank_min", "secondary_window_rank_max",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for target in targets:
            row = {
                "object_id": target["object_id"],
                "repository": target["repository"],
                "concept_doi": target["concept_doi"],
                "secondary_window_rank_min": target["secondary_window_rank"]["rank_min"],
                "secondary_window_rank_max": target["secondary_window_rank"]["rank_max"],
            }
            for key in fields:
                if key not in row:
                    row[key] = target["match"].get(key)
            w.writerow(row)

    print(json.dumps({
        "primary_birth_date": primary_birth_date,
        "primary_cohort_n": primary_stats["concept_family_count"],
        "primary_median_views": primary_stats["median_views"],
        "primary_p75_views": primary_stats["p75_views_linear"],
        "primary_p90_views": primary_stats["p90_views_linear"],
        "primary_p95_views": primary_stats["p95_views_linear"],
        "secondary_window_n": window_stats["concept_family_count"],
        "secondary_window_median_views": window_stats["median_views"],
        "targets": [
            {
                "repo": t["repository"],
                "views": t["match"]["views"],
                "primary_rank": [t["match"]["rank_min"], t["match"]["rank_max"]],
                "primary_percentile_interval": [
                    t["match"]["percentile_from_rank_max"],
                    t["match"]["percentile_from_rank_min"],
                ],
                "secondary_window_rank": [
                    t["secondary_window_rank"]["rank_min"],
                    t["secondary_window_rank"]["rank_max"],
                ],
            }
            for t in targets
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
