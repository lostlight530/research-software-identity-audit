#!/usr/bin/env python3
"""Aggregate Zenodo benchmark shards into a same-publication-date primary benchmark.

The primary comparison cohort shares the exact publication_date value exposed by
Zenodo for the target software families. This is date-resolution matching, not
sub-day age matching. The wider first-release window is retained only as secondary context.
Cohort membership is frozen by the shared `created_cutoff` recorded by retrieval
shards, while the selected `stats.*` ranking metric remains a live platform statistic
observed across a bounded retrieval interval rather than at one exact instant.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from datetime import datetime, timezone
from pathlib import Path


RANKING_METRICS = {
    "views": "version_views",
    "unique_views": "version_unique_views",
    "downloads": "version_downloads",
    "unique_downloads": "version_unique_downloads",
}


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


def rank_rows(rows, metric):
    ranked = [dict(row) for row in rows]
    ranked.sort(key=lambda x: (-x[metric], x["family_id"]))
    n = len(ranked)
    if n == 0:
        raise RuntimeError("cannot rank an empty cohort")
    values = [x[metric] for x in ranked]
    for item in ranked:
        v = item[metric]
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


def cohort_stats(ranked, metric):
    values = [x[metric] for x in ranked]
    result = {
        "concept_family_count": len(ranked),
        "ranking_metric": metric,
        "median_metric_value": statistics.median(values),
        "p75_metric_value_linear": quantile_linear(values, 0.75),
        "p90_metric_value_linear": quantile_linear(values, 0.90),
        "p95_metric_value_linear": quantile_linear(values, 0.95),
        "min_metric_value": min(values),
        "max_metric_value": max(values),
    }
    if metric == "views":
        result.update({
            "median_views": result["median_metric_value"],
            "p75_views_linear": result["p75_metric_value_linear"],
            "p90_views_linear": result["p90_metric_value_linear"],
            "p95_views_linear": result["p95_metric_value_linear"],
            "min_views": result["min_metric_value"],
            "max_views": result["max_metric_value"],
        })
    return result


def compact_neighbor(item, metric):
    return {
        "family_id": item["family_id"],
        "title": item["title"],
        "ranking_metric": metric,
        "metric_value": item[metric],
        "rank_min": item["rank_min"],
        "rank_max": item["rank_max"],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--targets", default="baseline/2026-10-05/doi-map.csv")
    ap.add_argument("--output", default="benchmark-output")
    ap.add_argument(
        "--metric",
        choices=tuple(RANKING_METRICS),
        default="views",
        help="Exploratory ranking metric. Default preserves the existing stats.views benchmark.",
    )
    ap.add_argument(
        "--primary-publication-date",
        help="Publication date for the same-date primary cohort; defaults to the shared target first publication date.",
    )
    args = ap.parse_args()

    root = Path(args.input)
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    cohort_files = sorted(root.glob("**/cohort.csv"))
    summary_files = sorted(root.glob("**/shard-summary.json"))
    if not cohort_files or not summary_files:
        raise RuntimeError(f"missing cohort or shard-summary files under {root}")

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
                    "version_downloads": as_int(row.get("version_downloads")),
                    "version_unique_downloads": as_int(row.get("version_unique_downloads")),
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

    window_rows = list(by_family.values())
    if not window_rows:
        raise RuntimeError("aggregated window cohort is empty")

    with open(args.targets, newline="", encoding="utf-8") as fh:
        target_manifest = list(csv.DictReader(fh))
    target_concepts = {r["concept_doi"].lower(): r for r in target_manifest}
    window_by_concept = {x["concept_doi"]: x for x in window_rows}
    missing = sorted(set(target_concepts) - set(window_by_concept))
    if missing:
        raise RuntimeError(f"target family missing from retrieval window: {missing}")

    observed_target_birth_dates = sorted({
        window_by_concept[concept]["first_publication_date"] for concept in target_concepts
    })
    if args.primary_publication_date:
        primary_publication_date = args.primary_publication_date
        off_date = sorted(
            concept for concept in target_concepts
            if window_by_concept[concept]["first_publication_date"] != primary_publication_date
        )
        if off_date:
            raise RuntimeError(
                f"targets do not all match primary publication date {primary_publication_date}: {off_date}"
            )
    else:
        if len(observed_target_birth_dates) != 1:
            raise RuntimeError(
                "targets do not share one first publication date; pass --primary-publication-date "
                "only after defining a justified matching rule"
            )
        primary_publication_date = observed_target_birth_dates[0]

    primary_rows = [
        row for row in window_rows if row["first_publication_date"] == primary_publication_date
    ]
    if not primary_rows:
        raise RuntimeError(f"no software families found for primary publication date {primary_publication_date}")

    primary = rank_rows(primary_rows, args.metric)
    window = rank_rows(window_rows, args.metric)
    primary_by_concept = {x["concept_doi"]: x for x in primary}
    window_ranked_by_concept = {x["concept_doi"]: x for x in window}

    missing_primary = sorted(set(target_concepts) - set(primary_by_concept))
    if missing_primary:
        raise RuntimeError(f"target family missing from same-publication-date primary cohort: {missing_primary}")

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

    shard_summaries.sort(key=lambda x: (x.get("start") or "", x.get("end") or ""))

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
        raise RuntimeError(f"expected one shared created_cutoff across shards, observed: {sorted(cutoffs)}")

    targets = []
    for concept, manifest in target_concepts.items():
        match = primary_by_concept[concept]
        window_match = window_ranked_by_concept[concept]
        higher = [x for x in primary if x[args.metric] > match[args.metric]]
        lower = [x for x in primary if x[args.metric] < match[args.metric]]
        targets.append({
            "object_id": manifest["object_id"],
            "repository": manifest["repository"],
            "concept_doi": manifest["concept_doi"],
            "match": match,
            "nearest_strictly_higher": [compact_neighbor(x, args.metric) for x in higher[-5:]],
            "nearest_strictly_lower": [compact_neighbor(x, args.metric) for x in lower[:5]],
            "secondary_window_rank": {
                "rank_min": window_match["rank_min"],
                "rank_max": window_match["rank_max"],
                "tie_count": window_match["tie_count"],
                "percentile_from_rank_min": window_match["percentile_from_rank_min"],
                "percentile_from_rank_max": window_match["percentile_from_rank_max"],
            },
        })
    targets.sort(key=lambda t: t["object_id"])

    target_metric_values = [t["match"][args.metric] for t in targets]
    target_total = sum(target_metric_values)
    shares = [v / target_total for v in target_metric_values] if target_total else [0.0] * len(target_metric_values)
    hhi = sum(s * s for s in shares)
    primary_stats = cohort_stats(primary, args.metric)
    window_stats = cohort_stats(window, args.metric)

    summary = {
        "benchmark_class": "exploratory_same_publication_date_zenodo_software_family",
        "prospective_dataset_member": False,
        "aggregated_at_utc": datetime.now(timezone.utc).isoformat(),
        "cohort_contract": {
            "resource_type": "software",
            "unit": "concept_family",
            "eligibility": "metadata.relations.version.index == 0 after all_versions retrieval",
            "primary_match_rule": "first_publication_date equals the shared target first_publication_date",
            "matching_resolution": "calendar_date",
            "primary_publication_date": primary_publication_date,
            "secondary_window_start": min(x["first_publication_date"] for x in window_rows),
            "secondary_window_end": max(x["first_publication_date"] for x in window_rows),
            "ranking_metric": f"stats.{args.metric}",
            "version_local_control": f"stats.{RANKING_METRICS[args.metric]}",
            "membership_created_cutoff_utc": next(iter(cutoffs)),
        },
        "metric_snapshot_semantics": (
            "Cohort membership is frozen by the shared created cutoff. The primary cohort is matched at Zenodo publication_date "
            f"calendar-date resolution. stats.{args.metric} is a live platform statistic observed across the shard retrieval interval, "
            "so reported ranks are bounded observed-snapshot ranks, not a reconstruction of one exact event-time instant."
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
            "ranking_metric": args.metric,
            "metric_total": target_total,
            "median_metric_value": statistics.median(target_metric_values),
            "min_metric_value": min(target_metric_values),
            "max_metric_value": max(target_metric_values),
            "median_vs_primary_cohort_median_multiplier": (
                statistics.median(target_metric_values) / primary_stats["median_metric_value"]
                if primary_stats["median_metric_value"] else None
            ),
            "floor_vs_primary_cohort_median_multiplier": (
                min(target_metric_values) / primary_stats["median_metric_value"]
                if primary_stats["median_metric_value"] else None
            ),
            "median_vs_secondary_window_median_multiplier": (
                statistics.median(target_metric_values) / window_stats["median_metric_value"]
                if window_stats["median_metric_value"] else None
            ),
            "floor_vs_secondary_window_median_multiplier": (
                min(target_metric_values) / window_stats["median_metric_value"]
                if window_stats["median_metric_value"] else None
            ),
            "hhi": hhi,
            "effective_repository_count": (1 / hhi) if hhi else None,
            "gini": gini(target_metric_values),
        },
        "shard_summaries": [
            {
                "start": x.get("start"),
                "end": x.get("end"),
                "created_cutoff": x.get("created_cutoff"),
                "run_started_utc": x.get("run_started_utc"),
                "run_finished_utc": x.get("run_finished_utc"),
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
        fields = list(window[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(window)
    with (out / "targets.csv").open("w", newline="", encoding="utf-8") as fh:
        fields = [
            "object_id", "repository", "concept_doi", "views", "unique_views",
            "downloads", "unique_downloads", "version_views", "version_unique_views",
            "version_downloads", "version_unique_downloads", "rank_min", "rank_max", "tie_count", "percentile_from_rank_min",
            "percentile_from_rank_max", "top_fraction_percent_from_rank_min",
            "top_fraction_percent_from_rank_max", "first_publication_date", "is_last",
            "secondary_window_rank_min", "secondary_window_rank_max",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for target in targets:
            match = target["match"]
            row = {
                "object_id": target["object_id"],
                "repository": target["repository"],
                "concept_doi": target["concept_doi"],
                "secondary_window_rank_min": target["secondary_window_rank"]["rank_min"],
                "secondary_window_rank_max": target["secondary_window_rank"]["rank_max"],
            }
            for key in fields:
                if key not in row:
                    row[key] = match.get(key)
            w.writerow(row)

    print(json.dumps({
        "primary_publication_date": primary_publication_date,
        "ranking_metric": args.metric,
        "primary_cohort_n": primary_stats["concept_family_count"],
        "primary_median_metric_value": primary_stats["median_metric_value"],
        "primary_p75_metric_value": primary_stats["p75_metric_value_linear"],
        "primary_p90_metric_value": primary_stats["p90_metric_value_linear"],
        "primary_p95_metric_value": primary_stats["p95_metric_value_linear"],
        "secondary_window_n": window_stats["concept_family_count"],
        "secondary_window_median_metric_value": window_stats["median_metric_value"],
        "targets": [
            {
                "repo": t["repository"],
                "metric_value": t["match"][args.metric],
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