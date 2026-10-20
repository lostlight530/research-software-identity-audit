"""Offline, read-only verification of the October 20 diagnostic field extracts."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
EVENT = "2026-10-20/01-independent-research-recheck"


def verify_fields(fields, record):
    results = []
    def check(name, passed):
        results.append({"check": name, "passed": bool(passed)})
    objs = fields["fixed_objects"]
    check("RS01-RS10 only", [o["object_id"] for o in objs] == [f"RS{i:02d}" for i in range(1, 11)])
    check("diagnostic only", record["record_class"] == "diagnostic_monitoring" and record["prospective_dataset_member"] is False)
    check("six layers sixty cells", (record["fixed_corpus_size"], record["analytical_layers"], record["planned_object_layer_units"], record["operational_platforms"]) == (10, 6, 60, 7))
    dc = fields["datacite_records"]
    check("complete distinct DOI page", len(dc) == len({d["doi"] for d in dc}) == record["datacite_count"] == fields["datacite_enumeration_meta"]["total"] and fields["datacite_enumeration_meta"]["totalPages"] == 1)
    check("findable and exact ORCID", all(d["state"] == "findable" and d["matched_orcid_identifiers"] and all(n.rstrip("/").split("/")[-1] == "0009-0001-3617-0832" for n in d["matched_orcid_identifiers"]) for d in dc))
    check("DOI types", dict(Counter(d["resource_type"] for d in dc)) == record["datacite_types"])
    doi_ids = {d["doi"].lower() for d in dc}
    version_ids = []
    for o in objs:
        name = o["object_id"]
        v = o["versions"]
        version_ids.extend(x["doi"].lower() for x in v["records"])
        check(name + " complete versions", v["reported_total"] == len(v["records"]) == 4 and v["has_next"] is False)
        check(name + " all version and concept DOI joins", all(x["doi"].lower() in doi_ids for x in v["records"]) and o["concept_doi"].lower() in doi_ids)
        check(name + " latest release identity", o["version"] == o["latest_github_release"]["tag"] == "v2026.10-fourteen-day-evidence-checkpoint")
        check(name + " origin full", o["swh"]["status"] == "full" and bool(o["swh"]["snapshot"]))
        s = o["swh"]
        if s["checkpoint_chain_verified"]:
            check(name + " checkpoint chain", s["checkpoint_tag"] is not None and s["checkpoint_tag"]["target"] == o["github_checkpoint_commit"] == s["checkpoint_revision_id"] and s["checkpoint_revision_status"] == s["checkpoint_directory_status"] == 200 and bool(s["checkpoint_directory"]))
        else:
            check(name + " unresolved checkpoint retained", s["checkpoint_revision_status"] == 404 and s["checkpoint_directory"] is None and s["checkpoint_tag"] is None)
        a = o["openalex_doi_route"]
        check(name + " concept route not version Work", a["returned_doi"].lower() == "https://doi.org/" + o["concept_doi"].lower() and a["returns_exact_version_doi"] is False)
        check(name + " OpenAIRE DOI hit", o["openaire_hits"] == 1)
    check("forty distinct version records", len(version_ids) == len(set(version_ids)) == record["complete_fixed_version_records"] == 40)
    check("two verified checkpoint chains", sum(o["swh"]["checkpoint_chain_verified"] for o in objs) == record["swh"]["checkpoint_tag_commit_directory_chains"] == 2)
    check("eight unresolved revisions", sum(o["swh"]["checkpoint_revision_status"] == 404 for o in objs) == record["swh"]["checkpoint_revision_404"] == 8)
    for k, total in record["zenodo_fixed_ten"].items():
        check("family/version sum " + k, sum(o["stats"][k] for o in objs) == total)
    page = fields["user_page_zenodo_comparison"]
    check("12 original joined page values", len(page) == record["user_page_matches"] == 12)
    for row in page:
        check("page/API " + row["title"], row["matches"] and row["page_unique_views"] == row["api_unique_views"] == int(row["pasted_number"][:-1]) and row["page_unique_downloads"] == row["api_unique_downloads"] == int(row["pasted_number"][-1]))
    check("OpenAlex query coverage", len(fields["openalex_works"]) == len({w["id"] for w in fields["openalex_works"]}) == record["openalex"]["query_count"] == 32)
    check("OpenAlex API profile separate", record["openalex"]["profile_count"] == 32 and fields["user_openalex"]["profile_count"] == 30)
    check("OpenAlex types", dict(Counter(w["type"] for w in fields["openalex_works"])) == record["openalex"]["types"])
    for k, a in fields["archive_verification"].items():
        check(k + " retained-byte provider match", a["size"] == a["provider_size"] and "md5:" + a["md5"] == a["provider_checksum"] and a["matches_provider"] and a["new_download_performed"] is False and a["archive_code_executed"] is False)
    check("no schedule invented", fields["remote_schedule"]["offsets_declared"] is False and fields["remote_schedule"]["files"] == ["README.md"])
    check("no OpenEBench validation invented", fields["openebench"]["validated"] == 0)
    check("separate Dashboard view/download sums", sum(w["views"] for w in fields["user_workflowhub_dashboard"]) == 3950 and sum(w["downloads"] for w in fields["user_workflowhub_dashboard"]) == 421)
    return results


def verify():
    ep = ROOT / "evidence" / EVENT
    mp = ROOT / "monitoring" / EVENT
    fields = json.loads((ep / "field-extracts.json").read_text(encoding="utf-8"))
    record = json.loads((mp / "record.json").read_text(encoding="utf-8"))
    results = verify_fields(fields, record)
    capture = json.loads((ep / "capture-manifest.json").read_text(encoding="utf-8"))
    requests = capture["requests"]
    results.append({"check": "all attempts and statuses retained", "passed": len(requests) == record["requests"] and dict(Counter(str(r["status"]) for r in requests)) == record["status_counts"]})
    for r in requests:
        results.append({"check": "source identity/clock " + r["key"], "passed": r["started_at"] <= r["finished_at"] and len(r.get("sha256", "")) == 64 and r["raw_transport_publicly_retained"] is False})
    for a in json.loads((ep / "artifact-manifest.json").read_text(encoding="utf-8"))["artifacts"]:
        p = ROOT / a["path"]
        results.append({"check": "artifact " + a["path"], "passed": p.is_file() and p.stat().st_size == a["bytes"] and hashlib.sha256(p.read_bytes()).hexdigest() == a["sha256"]})
    for filename, count in [("datacite-identifiers.csv", record["datacite_count"]), ("zenodo-family-statistics.csv", 10), ("user-page-api-reconciliation.csv", 12)]:
        with (mp / filename).open(encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f))
        results.append({"check": "CSV count " + filename, "passed": len(rows) == count})
    return {"mode": "offline_read_only", "network_calls": 0, "checks": len(results), "failed": sum(not r["passed"] for r in results), "results": results}


if __name__ == "__main__":
    result = verify()
    print(json.dumps(result, indent=2))
    sys.exit(bool(result["failed"]))
