#!/usr/bin/env python3
"""Read-only replay of retained Zenodo family and URL-shape selected fields.

This checks joins and arithmetic in already committed CSV evidence. It does not
fetch Zenodo, certify origin freshness, count people, or amend the OSF contract.
"""
import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "monitoring/2026-10-24/02-morning-infrastructure-and-zenodo-family-rollup"


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError(f"{path}: no CSV header")
        rows = list(reader)
    if any(None in row or None in row.values() for row in rows):
        raise ValueError(f"{path}: malformed CSV row")
    return rows


def numeric(row, field, errors, context):
    try:
        value = int(row[field])
        if value < 0:
            raise ValueError("negative")
        return value
    except (KeyError, ValueError, TypeError):
        errors.append(f"{context}: invalid {field}")
        return 0


def run(directory):
    issues = []
    corpus = read_csv(ROOT / "corpus/object-manifest.csv")
    expected = {r["object_id"]: (r["software_family"], "preregistered_sample") for r in corpus}
    expected["CONTROL"] = ("research-software-identity-audit", "separate_research_control")
    expected["PILOT"] = ("life-science-ecosystem-lab", "independent_pilot")
    expected_ids = set(expected)
    if set(r["object_id"] for r in corpus) != {f"RS{i:02d}" for i in range(1, 11)}:
        issues.append("frozen corpus manifest is not exactly RS01-RS10")

    family_rows = read_csv(directory / "zenodo-family-rollup.csv")
    version_rows = read_csv(directory / "zenodo-version-evidence.csv")
    pair_families = read_csv(directory / "zenodo-query-shape-family-comparison.csv")
    pair_versions = read_csv(directory / "zenodo-query-shape-version-comparison.csv")

    def unique_map(rows, key_columns, label):
        mapped = {}
        for r in rows:
            try:
                key = tuple(r[k] for k in key_columns)
            except KeyError as exc:
                issues.append(f"{label}: missing key column {exc}")
                continue
            if key in mapped:
                issues.append(f"{label}: duplicate key {key}")
            mapped[key] = r
        return mapped

    fam = unique_map(family_rows, ["object_id"], "family")
    pfam = unique_map(pair_families, ["object_id"], "shape_family")
    vers = unique_map(version_rows, ["object_id", "record_id"], "version")
    pvers = unique_map(pair_versions, ["object_id", "version_record_id"], "shape_version")
    if set(fam) != {(x,) for x in expected_ids}:
        issues.append("family rows must represent exactly RS01-RS10 + CONTROL + PILOT")
    if set(pfam) != set(fam):
        issues.append("dual-shape family identities differ from family rollup")
    if {x[0] for x in vers} != set(expected_ids):
        issues.append("version evidence has missing or extra family identities")
    if set(vers) != set(pvers):
        issues.append("regular version IDs differ from dual-shape version IDs")

    ids_across_families = set()
    sum_regular = sum_diagnostic = sum_downloads = 0
    for (oid,), family in sorted(fam.items()):
        context = f"{oid} family"
        if oid not in expected:
            issues.append(f"{context}: unexpected identity")
            continue
        repo, role = expected[oid]
        if family.get("repository") != repo or family.get("role") != role:
            issues.append(f"{context}: repository or role mismatch")
        attached = [v for (id_, _), v in vers.items() if id_ == oid]
        expected_count = numeric(family, "version_count", issues, context)
        if expected_count != len(attached):
            issues.append(f"{context}: version_count does not match evidence rows")
        concept = family.get("concept_doi")
        source = family.get("source_url")
        sum_view = sum(numeric(v, "version_views", issues, context) for v in attached)
        sum_down = sum(numeric(v, "version_downloads", issues, context) for v in attached)
        for key, wanted in [
            ("family_total_views", sum_view), ("sum_version_views", sum_view),
            ("attached_family_views", sum_view), ("family_total_downloads", sum_down),
            ("sum_version_downloads", sum_down), ("attached_family_downloads", sum_down),
        ]:
            if numeric(family, key, issues, context) != wanted:
                issues.append(f"{context}: {key} differs from version-specific sum")
        if family.get("views_reconciliation") != "match" or family.get("downloads_reconciliation") != "match":
            issues.append(f"{context}: retained reconciliation does not say match")
        for v in attached:
            record_id = v.get("record_id")
            if not record_id or v.get("version_doi") != f"10.5281/zenodo.{record_id}":
                issues.append(f"{context}: version DOI or version record ID mismatch")
            if record_id in ids_across_families:
                issues.append(f"{context}: shared version record ID across distinct concepts")
            ids_across_families.add(record_id)
            if v.get("repository") != repo or v.get("concept_doi") != concept or v.get("source_url") != source:
                issues.append(f"{context}: version identity or source locator mismatch")
            for field, attached_key in [
                ("family_views_attached_do_not_sum", "family_total_views"),
                ("family_unique_views_attached_do_not_sum", "family_unique_views_source_attached"),
                ("family_downloads_attached_do_not_sum", "family_total_downloads"),
                ("family_unique_downloads_attached_do_not_sum", "family_unique_downloads_source_attached"),
            ]:
                if v.get(field) != family.get(attached_key):
                    issues.append(f"{context}: {field} differs within family")
            p = pvers.get((oid, record_id))
            if p:
                for lhs, rhs in [
                    ("repository", "repository"), ("version_doi", "version_doi"),
                    ("version_tag", "release_tag"), ("regular_source_url", "source_url"),
                    ("regular_version_views", "version_views"),
                ]:
                    if p.get(lhs) != v.get(rhs):
                        issues.append(f"{context}: dual-shape version {record_id} {lhs} mismatch")
                p_diff = numeric(p, "diagnostic_version_views", issues, context) - numeric(p, "regular_version_views", issues, context)
                if p_diff != int_or_error(p, "field_difference_not_confirmed_visit_increase", issues, context):
                    issues.append(f"{context}: version comparison delta mismatch")

        p = pfam.get((oid,))
        if p:
            for lhs, rhs in [
                ("repository", "repository"), ("role", "role"), ("concept_doi", "concept_doi"),
                ("versions_count", "version_count"), ("regular_source_url", "source_url"),
                ("regular_unduplicated_by_family_total_views", "family_total_views"),
            ]:
                if p.get(lhs) != family.get(rhs):
                    issues.append(f"{context}: family comparison {lhs} mismatch")
            diag = numeric(p, "diagnostic_unduplicated_by_family_total_views", issues, context)
            diagnostic_versions = sum(numeric(pvers[(oid, v["record_id"])], "diagnostic_version_views", issues, context)
                                      for v in attached if (oid, v["record_id"]) in pvers)
            if diag != diagnostic_versions:
                issues.append(f"{context}: diagnostic family views not explained by version fields")
            if diag - sum_view != int_or_error(p, "field_difference_not_confirmed_visit_increase", issues, context):
                issues.append(f"{context}: family comparison delta mismatch")
            if not p.get("diagnostic_source_url") or p.get("diagnostic_source_url") == source:
                issues.append(f"{context}: diagnostic URL not distinct from regular URL")
            for v in attached:
                q = pvers.get((oid, v["record_id"]))
                if q and q.get("diagnostic_source_url") != p.get("diagnostic_source_url"):
                    issues.append(f"{context}: inconsistent diagnostic URL in version rows")
            sum_diagnostic += diag
        sum_regular += sum_view
        sum_downloads += sum_down

    report = {
        "check": "retained_zenodo_family_and_query_shape_offline",
        "result": "PASS" if not issues else "FAIL",
        "fixed_preregistered_objects": 10,
        "families_returned": len(fam),
        "version_evidence_rows": len(vers),
        "dual_shape_version_rows": len(pvers),
        "regular_family_views": sum_regular,
        "diagnostic_family_views": sum_diagnostic,
        "source_field_difference": sum_diagnostic - sum_regular,
        "regular_family_downloads": sum_downloads,
        "source_conflict": "UNRESOLVED_TWO_URL_REPRESENTATIONS" if sum_diagnostic != sum_regular else "NO_FIELD_DIFFERENCE_IN_RETAINED_ROWS",
        "claims_not_proven": ["uncached_origin_response", "incremental_real_visits", "globally_deduplicated_people"],
        "errors": issues,
    }
    return report


def int_or_error(row, field, issues, context):
    try:
        return int(row[field])
    except (KeyError, ValueError, TypeError):
        issues.append(f"{context}: invalid signed {field}")
        return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=DEFAULT)
    args = parser.parse_args()
    try:
        result = run(args.directory)
    except (OSError, ValueError, csv.Error) as exc:
        result = {"result": "FAIL", "errors": [f"{type(exc).__name__}: {exc}"]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["result"] == "PASS" else 1)


if __name__ == "__main__":
    main()
