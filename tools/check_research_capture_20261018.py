"""Read-only verifier for the public October 18 research field-extract package."""
from copy import deepcopy
from pathlib import Path
import csv
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
EVENT = "2026-10-18/03-independent-research-verification"


def read_corpus():
    with (ROOT / "corpus" / "object-manifest.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def verify_fields(fields, record):
    results = []

    def check(name, ok):
        results.append({"check": name, "passed": bool(ok)})

    objs = fields["fixed_objects"]
    corpus = read_corpus()
    by_id = {row["object_id"]: row for row in corpus}
    check("fixed corpus remains RS01-RS10",
          [o["object_id"] for o in objs] == [f"RS{i:02d}" for i in range(1, 11)])
    check("frozen manifest is unique and complete",
          len(corpus) == len(by_id) == 10 and
          len({r["software_family"] for r in corpus}) == 10)
    check("diagnostic only",
          record["record_class"] == "diagnostic_monitoring" and
          record["prospective_dataset_member"] is False)
    check("denominator",
          (record["fixed_corpus_size"], record["planned_layers"], record["planned_units"]) == (10, 6, 60))

    dois = fields["datacite_records"]
    check("DOI enumeration complete",
          len(dois) == len({d["doi"].lower() for d in dois}) ==
          fields["datacite_complete_query_count"] and fields["datacite_pages"] == 1)
    check("DOIs findable", all(d["state"] == "findable" for d in dois))
    check("ORCID match", all(
        d["matched_orcid_identifiers"] and
        all(n.rstrip("/").split("/")[-1] == "0009-0001-3617-0832"
            for n in d["matched_orcid_identifiers"])
        for d in dois))

    for o in objs:
        rid = o["object_id"]
        canonical = by_id.get(rid)
        check(rid + " frozen manifest identity",
              canonical is not None and
              o["repository"] == canonical["software_family"] and
              o["swh_origin_visit"]["origin"] == canonical["source_repository"] and
              o["github_release"]["html_url"].startswith(
                  canonical["source_repository"] + "/releases/tag/") and
              str(o["record_id"]) == o["doi"].rsplit(".", 1)[-1])
        check(rid + " release/DOI join",
              o["zenodo_version"] == o["github_release"]["tag_name"] ==
              "v2026.10-fourteen-day-evidence-checkpoint" and
              any(d["doi"].lower() == o["doi"].lower() and d["state"] == "findable"
                  for d in dois))
        check(rid + " origin visit (not tagged release proof)",
              o["swh_origin_visit"]["status"] == "full" and
              bool(o["swh_origin_visit"]["snapshot"]))
        check(rid + " discovery count", o["openaire_doi_result_count"] == 1)

    for k, total in record["zenodo_fixed_ten"].items():
        check("Zenodo sum " + k, sum(o["stats"][k] for o in objs) == total)

    check("query/profile separate",
          fields["openalex"]["profile_count"] == record["openalex"]["profile_count"] and
          len(fields["openalex"]["works"]) == fields["openalex"]["query_count"] ==
          record["openalex"]["query_count"])
    for key, a in fields["archives"].items():
        check(key + " reported archive digest consistency",
              a["size"] == a["expected_size"] and
              "md5:" + a["md5"] == a["provider_checksum"] and
              a["md5_matches"] and a["size_matches"])
    arc = fields["archives"]["zenodo_audit_fourth"]["embedded_metadata"]
    check("archived drift retained",
          arc["CITATION.cff"]["fields"]["version"] ==
          arc["codemeta.json"]["fields"]["version"] == "v2026.10-evidence-reconciliation")
    check("live correction separate",
          fields["current_metadata"]["citation_version"] ==
          fields["current_metadata"]["codemeta_version"] == "v2026.10-evidence-integrity")
    check("no offsets declared",
          fields["remote_schedule"]["files"] == ["README.md"] and
          fields["remote_schedule"]["concrete_offsets_declared"] is False)
    check("merged PRs",
          len(fields["github_merged_prs"]) == 7 and
          all(r["merged"] for r in fields["github_merged_prs"]))
    check("CI job evidence",
          len(fields["github_ci_jobs"]) == 2 and
          all(len(jobs) == 5 and all(j["conclusion"] == "success" for j in jobs)
              for jobs in fields["github_ci_jobs"].values()))
    check("OpenEBench no validation", fields["openebench"]["validated"] == 0)
    return results


def negative_regressions(fields, record):
    cases = []
    swapped = deepcopy(fields)
    left, right = swapped["fixed_objects"][5], swapped["fixed_objects"][8]
    # Swap entire repository-linked observations, retaining the valid RS labels.
    # The previous checker erroneously accepted this permutation.
    for key in list(left):
        if key != "object_id":
            left[key], right[key] = right[key], left[key]
    checks = verify_fields(swapped, record)
    cases.append({"check": "negative: permuted RS repository identities rejected",
                  "passed": any(not r["passed"] and
                                r["check"].endswith("frozen manifest identity")
                                for r in checks) and
                  next(r["passed"] for r in checks
                       if r["check"] == "fixed corpus remains RS01-RS10")})

    foreign = deepcopy(fields)
    foreign["fixed_objects"][0]["object_id"] = "RS11"
    cases.append({"check": "negative: foreign corpus ID rejected",
                  "passed": any(not r["passed"] for r in verify_fields(foreign, record))})
    wrong_digest = deepcopy(fields)
    wrong_digest["archives"]["zenodo_audit_fourth"]["md5"] = "0" * 32
    cases.append({"check": "negative: wrong reported ZIP digest rejected",
                  "passed": any(not r["passed"] for r in verify_fields(wrong_digest, record))})
    wrong_total = deepcopy(record)
    wrong_total["zenodo_fixed_ten"]["views"] += 1
    cases.append({"check": "negative: modified counter total rejected",
                  "passed": any(not r["passed"] for r in verify_fields(fields, wrong_total))})
    return cases


def verify():
    ep = ROOT / "evidence" / EVENT
    mp = ROOT / "monitoring" / EVENT
    fields = json.loads((ep / "field-extracts.json").read_text(encoding="utf-8"))
    record = json.loads((mp / "record.json").read_text(encoding="utf-8"))
    results = verify_fields(fields, record)
    results.extend(negative_regressions(fields, record))
    capture = json.loads((ep / "capture-manifest.json").read_text(encoding="utf-8"))
    for r in capture["requests"]:
        results.append({"check": "capture clock " + r["key"],
                        "passed": r["started_at"] <= r["finished_at"] and
                        bool(r.get("sha256")) and
                        r["raw_transport_publicly_retained"] is False})
    manifest = json.loads((ep / "artifact-manifest.json").read_text(encoding="utf-8"))
    for artifact in manifest["artifacts"]:
        path = ROOT / artifact["path"]
        ok = (path.is_file() and path.stat().st_size == artifact["bytes"] and
              hashlib.sha256(path.read_bytes()).hexdigest() == artifact["sha256"])
        results.append({"check": "artifact " + artifact["path"], "passed": ok})

    with (mp / "zenodo-family-statistics.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    by_repo = {row["repo"]: row for row in rows}
    check_csv = (len(rows) == len(by_repo) == len(fields["fixed_objects"]) == 10 and
                 all((r := by_repo.get(o["repository"])) is not None and
                     r["record_id"] == str(o["record_id"]) and
                     r["doi"].lower() == o["doi"].lower() and
                     all(int(r[k]) == o["stats"][k] for k in o["stats"])
                     for o in fields["fixed_objects"]))
    results.append({"check": "Zenodo CSV full repository identity/DOI/stats join",
                    "passed": check_csv})
    with (mp / "datacite-identifiers.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    csv_dois = {r["doi"].lower(): r for r in rows}
    results.append({"check": "DataCite CSV exact DOI/types/state join",
                    "passed": len(rows) == len(csv_dois) == len(fields["datacite_records"])
                    and all((r := csv_dois.get(d["doi"].lower())) is not None and
                            r["resource_type"] == d["resource_type"] and
                            r["client"] == d["client"] and r["state"] == d["state"]
                            for d in fields["datacite_records"])})
    return {"mode": "offline_read_only", "network_calls": 0,
            "checks": len(results), "failed": sum(not r["passed"] for r in results),
            "results": results}


if __name__ == "__main__":
    result = verify()
    print(json.dumps(result, indent=2))
    sys.exit(bool(result["failed"]))
