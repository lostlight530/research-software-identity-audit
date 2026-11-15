#!/usr/bin/env python3
"""Offline comparator for two date-specific 458-attempt public HTTP source ledgers."""
import csv
import hashlib
import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT=Path(__file__).resolve().parents[3]
EVENT="2026-11-15/02-full-institutional-source-recheck"
E=ROOT/"evidence"/EVENT
M=ROOT/"monitoring"/EVENT
P=ROOT/"evidence/2026-11-13/01-full-institutional-recheck/source-attempts.jsonl"
EXPECTED={"surface":34,"datacite_doi":102,"openaire_doi":102,"openalex_doi":102,
          "zenodo_version":67,"github_main":11,"github_releases":11,
          "rsd_software":11,"swh_origin":10,"rsd_issue":2,
          "rsd_person":1,"rsd_project":1,"workflowhub":4}
FIXED={"welcome-to-github","zero-entropy-lab","Axiom-0","reflective-continuum",
       "agent-foundations","auto-doc-engine","epistemic-pipeline","sci-render-kit",
       "china-agentic-observatory","agentic-frontier-observatory"}
def load(p):
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
def save(p,x):
    p.write_text(json.dumps(x,indent=2,ensure_ascii=False,sort_keys=True)+"\n",encoding="utf-8")
def ok(r):
    return r["http_status"]==200 and r["failure"] is None
def v(r,k):
    return r.get("selected_public_fields",{}).get(k)
def clock(t):
    d=datetime.fromisoformat(t.replace("Z","+00:00"))
    assert d.utcoffset() is not None
    return d.astimezone(timezone.utc)
def total_if_complete(items,k):
    if any(not ok(x) or not isinstance(v(x,k),int) for x in items):return None
    return sum(v(x,k) for x in items)
new=load(E/"source-attempts.jsonl")
old=load(P)
assert len(new)==len(old)==sum(EXPECTED.values())==458
assert dict(Counter(x["scope"] for x in new))==EXPECTED
before={(x["scope"],x["key"]):x for x in old}
assert len(before)==458
assert set(before)=={(x["scope"],x["key"]) for x in new}
for x in new:
    assert clock(x["started_at_utc"])<=clock(x["finished_at_utc"])
summary={}
changes=[]
for scope,count in sorted(EXPECTED.items()):
    cur=[r for r in new if r["scope"]==scope]
    states=Counter()
    for r in cur:
        p=before[(r["scope"],r["key"])]
        if not ok(r):
            rel="DEGRADED" if ok(p) else "UNRESOLVED"
        elif not ok(p):rel="RECOVERED"
        elif r["selected_public_fields"]!=p["selected_public_fields"]:
            rel="SELECTED_FIELDS_CHANGED"
        else:rel="SAME_SELECTED_FIELDS_NOT_SAME_ORIGIN_BYTES"
        states[rel]+=1
        changes.append([scope,r["key"],r["locator"],p["http_status"],r["http_status"],
                        p["failure"],r["failure"],rel,r["finished_at_utc"]])
    summary[scope]={"attempted":count,"http_200":sum(ok(x) for x in cur),
                    "failed_or_partial":sum(not ok(x) for x in cur),
                    "http_statuses":dict(Counter(str(x["http_status"]) for x in cur)),
                    "relations":dict(states)}
with (M/"request-delta-vs-2026-11-13.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(["scope","key","locator","previous_http","current_http",
                "previous_failure","current_failure","derived_relation","retrieved_at_utc"])
    w.writerows(changes)
def group(name):
    return [x for x in new if x["scope"]==name]
dc,oa,ax,ze,sw=(group(q) for q in
                   ["datacite_doi","openaire_doi","openalex_doi","zenodo_version","swh_origin"])
fixed=[r for r in ze if r["key"].split(":")[0] in FIXED]
assert len(fixed)==60
orcid=next(x for x in group("surface") if x["key"].startswith("16:"))
fig={
 "datacite_findable":sum(ok(r) and str(v(r,"state")).lower()=="findable" for r in dc),
 "openaire_positive_queries":sum(ok(r) and str(v(r,"result_total")).isdecimal()
                                and int(v(r,"result_total"))>0 for r in oa),
 "openalex_exact_canonical_matches":sum(ok(r) and v(r,"canonical_doi_exact_match") is True for r in ax),
 "openalex_distinct_returned_work_ids":len({v(r,"work_id") for r in ax if ok(r) and v(r,"work_id")}),
 "zenodo_fixed60_success_rows":sum(ok(r) for r in fixed),
 "zenodo_fixed60_version_views":total_if_complete(fixed,"version_views"),
 "zenodo_fixed60_version_downloads":total_if_complete(fixed,"version_downloads"),
 "zenodo_all67_success_rows":sum(ok(r) for r in ze),
 "orcid_groups":v(orcid,"groups") if ok(orcid) else None,
 "orcid_summaries":v(orcid,"summaries") if ok(orcid) else None,
 "swh_full_origin_latest_visits":sum(ok(r) and v(r,"status")=="full" for r in sw),
 "workflowhub_json_success":sum(ok(r) for r in group("workflowhub")),
 "rsd_issues":{r["key"]:(v(r,"state") if ok(r) else "UNKNOWN") for r in group("rsd_issue")}
}
ends=[clock(r["finished_at_utc"]) for r in new]
starts=[clock(r["started_at_utc"]) for r in new]
record={
 "record_class":"bounded_complete_458_attempt_cohort_diagnostic_not_prospective",
 "source_start_utc":min(starts).isoformat(),
 "source_end_utc":max(ends).isoformat(),
 "logical_date_asia_shanghai":max(ends).astimezone(ZoneInfo("Asia/Shanghai")).date().isoformat(),
 "sample":"RS01-RS10","control_is_rs11":False,
 "preregistered_layers":6,"preregistered_units_per_eligible_timepoint":60,
 "operational_platforms":7,"possible_platform_checks_not_units":70,
 "known_doi_inventory_size":102,"new_prospective_cells":0,
 "attempted":458,"http_200_no_failure":sum(ok(r) for r in new),
 "all_success":all(ok(r) for r in new),"scope_counts":summary,
 "diagnostic_fields":fig,"prior_2026_11_13_fixed_version_views":3849,
 "prior_2026_11_13_fixed_version_downloads":37,
 "prior_2026_11_13_orcid_groups":18,"prior_2026_11_13_orcid_summaries":117,
 "prior_2026_11_13_openaire_positive":94,
 "original_http_body_bytes_retained":False,
 "source": "GitHub Actions bounded read-only HTTP, GitHub token for public GitHub only",
 "limitations":["full attempt cohort is not full positive indexing census",
  "102 DOI known-list cohort is not global DOI completeness",
  "client UTC receipt is not first publication/indexing timestamp",
  "HTTP 200 can still mean noncanonical identity or challenge HTML",
  "failed, blocked, timeout and absent source fields are not proof of nonexistence",
  "raw response SHA256 does not reproduce original provider bytes",
  "no authenticated ORCID/RSD/OSF edits or institution endorsement",
  "no active declared prospective timepoint schedule; zero prospective cells"]
}
save(M/"record.json",record)
save(M/"comparison-vs-2026-11-13.json",{
 "derived_from":"exact 458 source keys from Nov 13 and Nov 15",
 "computed_utc":datetime.now(timezone.utc).isoformat(),
 "by_scope":summary,"current":fig,
 "old":{"zenodo_views":3849,"zenodo_downloads":37,"orcid_groups":18,
        "orcid_summaries":117,"openaire_positive":94},
 "not_original_http_byte_comparison":True,"new_prospective_cells":0})
save(E/"provenance.json",{
 "class":"source_attempt_provenance_not_prospective",
 "source_collector":"monitoring/2026-11-13/01-full-institutional-recheck/collector.py",
 "reconcile_script":"monitoring/"+EVENT+"/reconcile.py",
 "github_run_id":os.environ.get("GITHUB_RUN_ID"),
 "github_sha":os.environ.get("GITHUB_SHA"),
 "github_ref":os.environ.get("GITHUB_REF_NAME"),
 "capture_start_utc":record["source_start_utc"],
 "capture_end_utc":record["source_end_utc"],
 "source_ledger_sha256":hashlib.sha256((E/"source-attempts.jsonl").read_bytes()).hexdigest(),
 "prior_ledger_sha256":hashlib.sha256(P.read_bytes()).hexdigest(),
 "provider_raw_bytes_retained":False,"authorization_headers_retained":False})
with (E/"sha256-manifest.txt").open("w",encoding="utf-8") as f:
    for p in sorted(E.iterdir()):
        if p.is_file() and p.name not in {"sha256-manifest.txt","README.md"}:
            f.write(hashlib.sha256(p.read_bytes()).hexdigest()+"  "+p.name+"\n")
bad=", ".join(f"{k}={x['failed_or_partial']}" for k,x in summary.items() if x["failed_or_partial"])
if not bad:bad="none"
md=("# November 15 full bounded public-source attempt recapture\n\n"
    f"**UTC capture:** {record['source_start_utc']} – {record['source_end_utc']}\n\n"
    f"**Requests:** 458/458 expected, HTTP-200 with no recorded failure {record['http_200_no_failure']}/458; failed/partial by scope: {bad}\n\n"
    "## Scope\n\n"
    "34 existing supplementary URLs; 102 known DOI queries each at DataCite, OpenAIRE and OpenAlex; "
    "67 Zenodo versions; eleven GitHub main and releases, eleven RSD software entries, ten SWH origins, "
    "two RSD issues, RSD person/project, four WorkflowHub JSON. All endpoint attempts preserve actual per-request UTC clocks and status/errors.\n\n"
    "## Measured diagnostic fields (not study units)\n\n"
    f"- DataCite findable: {fig['datacite_findable']}/102\n"
    f"- OpenAIRE query positive: {fig['openaire_positive_queries']}/102 (not distinct software)\n"
    f"- OpenAlex exact canonical DOI matches: {fig['openalex_exact_canonical_matches']}/102; "
    f"distinct returned Work IDs: {fig['openalex_distinct_returned_work_ids']} (HTTP 200 alone is not canonical match)\n"
    f"- Zenodo fixed ten: {fig['zenodo_fixed60_version_views']} version views, "
    f"{fig['zenodo_fixed60_version_downloads']} downloads with {fig['zenodo_fixed60_success_rows']}/60 valid record responses; "
    "a null total means unavailable, not zero\n"
    f"- ORCID groups / summaries: {fig['orcid_groups']} / {fig['orcid_summaries']}; "
    f"SWH full latest origins: {fig['swh_full_origin_latest_visits']}/10; "
    f"WorkflowHub metadata successes: {fig['workflowhub_json_success']}/4\n\n"
    "## Evidence and limits\n\n"
    f"[Source attempts](../../../evidence/{EVENT}/source-attempts.jsonl) · "
    f"[source hashes](../../../evidence/{EVENT}/sha256-manifest.txt) · "
    f"[provenance](../../../evidence/{EVENT}/provenance.json) · "
    "[458-key changes](request-delta-vs-2026-11-13.csv) · "
    "[machine comparison](comparison-vs-2026-11-13.json)\n\n"
    "Original provider HTTP body bytes are NOT retained, only SHA-256, lengths, UTC receipts and minimized public fields. "
    "The captured full request cohort is not a full positive indexing census, nor authenticated platform/UI state. "
    "No changes to frozen OSF, RS01–RS10, baseline, schedule, Releases, DOI, or original historical evidence. "
    "Six layers / 60 eligible point units, seven operational platforms / 70 possible checks; **zero prospective cells**.\n")
(M/"README.md").write_text(md,encoding="utf-8")
(E/"README.md").write_text("# November 15 public attempt evidence\n\n458 bounded public HTTP source attempts with request UTC clocks, response status, SHA-256 and public fields. No original HTTP response bodies archived. See [monitoring record](../../../monitoring/"+EVENT+"/README.md). Failed requests are not object absence.\n",encoding="utf-8")
print("FULL_CAPTURE_COMPARISON="+json.dumps({"attempted":458,"http_200":record["http_200_no_failure"],
      "source_start_utc":record["source_start_utc"],"source_end_utc":record["source_end_utc"],
      "scope_counts":summary,"derived":fig,"new_prospective_cells":0},ensure_ascii=False))
