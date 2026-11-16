#!/usr/bin/env python3
"""One-off comparator for exact 458 keyed public source attempts.
Only compares dated diagnostic captures. No research observation is created.
"""
import argparse,csv,hashlib,json,pathlib
from collections import Counter
from datetime import datetime,timezone
p=argparse.ArgumentParser();p.add_argument("--previous",required=True);p.add_argument("--current",required=True);p.add_argument("--output",required=True);a=p.parse_args()
old_path=pathlib.Path(a.previous);cur_path=pathlib.Path(a.current);out=pathlib.Path(a.output);out.mkdir(parents=True,exist_ok=True)
def load(path):return [json.loads(x) for x in path.read_text(encoding="utf8").splitlines() if x.strip()]
old=load(old_path);cur=load(cur_path)
expected={"surface":34,"datacite_doi":102,"openaire_doi":102,"openalex_doi":102,"zenodo_version":67,"github_main":11,"github_releases":11,"rsd_software":11,"swh_origin":10,"rsd_issue":2,"rsd_person":1,"rsd_project":1,"workflowhub":4}
assert len(old)==len(cur)==sum(expected.values())==458
assert dict(Counter(q["scope"] for q in cur))==expected
before={(q["scope"],q["key"]):q for q in old}
after={(q["scope"],q["key"]):q for q in cur}
assert len(before)==len(after)==458 and set(before)==set(after)
def ts(v):
    q=datetime.fromisoformat(v.replace("Z","+00:00"))
    assert q.utcoffset() is not None
    return q.astimezone(timezone.utc)
def ok(q):return q["http_status"]==200 and q["failure"] is None
def val(q,key):return q.get("selected_public_fields",{}).get(key)
for q in cur:assert ts(q["started_at_utc"])<=ts(q["finished_at_utc"])
comp=[];scopes={}
for scope,count in expected.items():
    rows=[q for q in cur if q["scope"]==scope]
    outcomes=Counter()
    for q in rows:
        prev=before[(scope,q["key"])]
        status=("UNRESOLVED" if not ok(prev) else "DEGRADED") if not ok(q) else ("RECOVERED" if not ok(prev) else ("SELECTED_FIELDS_CHANGED" if q["selected_public_fields"]!=prev["selected_public_fields"] else "SAME_SELECTED_FIELDS_NOT_SAME_ORIGIN_BYTES"))
        outcomes[status]+=1
        comp.append({"scope":scope,"key":q["key"],"locator":q["locator"],"old_http":prev["http_status"],"current_http":q["http_status"],"old_failure":prev["failure"],"current_failure":q["failure"],"relation":status,"retrieved_at_utc":q["finished_at_utc"]})
    scopes[scope]={"attempted":count,"http_200_without_failure":sum(ok(q) for q in rows),"failed_or_partial":sum(not ok(q) for q in rows),"relation_counts":dict(outcomes),"http_statuses":dict(Counter(str(q["http_status"]) for q in rows))}
with (out/"request-delta.csv").open("w",newline="",encoding="utf8") as f:
    w=csv.DictWriter(f,fieldnames=["scope","key","locator","old_http","current_http","old_failure","current_failure","relation","retrieved_at_utc"],lineterminator="\n");w.writeheader();w.writerows(comp)
fix={"welcome-to-github","zero-entropy-lab","Axiom-0","reflective-continuum","agent-foundations","auto-doc-engine","epistemic-pipeline","sci-render-kit","china-agentic-observatory","agentic-frontier-observatory"}
zen=[q for q in cur if q["scope"]=="zenodo_version" and q["key"].split(":")[0] in fix]
assert len(zen)==60
def complete_sum(rows,field):
    if any(not ok(q) or not isinstance(val(q,field),int) for q in rows):return None
    return sum(val(q,field) for q in rows)
dc=[q for q in cur if q["scope"]=="datacite_doi"]
op=[q for q in cur if q["scope"]=="openaire_doi"]
ax=[q for q in cur if q["scope"]=="openalex_doi"]
o=next(q for q in cur if q["scope"]=="surface" and q["key"].startswith("16:"))
sw=[q for q in cur if q["scope"]=="swh_origin"]
fig={"datacite_findable":sum(ok(q) and str(val(q,"state")).lower()=="findable" for q in dc),
     "openaire_positive_requests":sum(ok(q) and str(val(q,"result_total")).isdecimal() and int(val(q,"result_total"))>0 for q in op),
     "openalex_exact_canonical_doi_matches":sum(ok(q) and val(q,"canonical_doi_exact_match") is True for q in ax),
     "openalex_distinct_returned_work_ids":len({val(q,"work_id") for q in ax if ok(q) and val(q,"work_id")}),
     "zenodo_fixed60_success":sum(ok(q) for q in zen),
     "zenodo_fixed60_version_views":complete_sum(zen,"version_views"),
     "zenodo_fixed60_version_downloads":complete_sum(zen,"version_downloads"),
     "orcid_groups":val(o,"groups") if ok(o) else None,
     "orcid_summaries":val(o,"summaries") if ok(o) else None,
     "swh_full_latest_visits":sum(ok(q) and val(q,"status")=="full" for q in sw),
     "rsd_issues":{q["key"]:val(q,"state") if ok(q) else "UNKNOWN" for q in cur if q["scope"]=="rsd_issue"}}
times=[ts(q["started_at_utc"]) for q in cur]+[ts(q["finished_at_utc"]) for q in cur]
result={"record_class":"temporary_pr_timestamped_458_request_diagnostic_NOT_PROSPECTIVE",
    "started_at_utc":min(times).isoformat(),"ended_at_utc":max(times).isoformat(),
    "requests":len(cur),"previous_requests":len(old),"identical_key_cohort":True,
    "new_prospective_cells":0,"source_previous_ledger_sha256":hashlib.sha256(old_path.read_bytes()).hexdigest(),
    "source_new_ledger_sha256":hashlib.sha256(cur_path.read_bytes()).hexdigest(),
    "scope_counts":scopes,"selected_figures":fig,
    "limits":["Totals use null if any fixed-version record is unavailable; do not turn missing into zero",
              "HTTP 200 does not imply canonical DOI match; source raw bytes not retained",
              "No first-index timestamp, no causal attribution, no human visitor count",
              "Origin retrieval UTC clocks are client recorded, raw HTTP bodies only hashed",
              "No new release, OSF write, account interaction or planned observation timepoint"]}
(out/"comparison.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
print("SELFTEST_COHORT="+json.dumps({"attempted":len(cur),"http_200_no_failure":sum(ok(q) for q in cur),"current_source_window":[result["started_at_utc"],result["ended_at_utc"]],"figures":fig,"failures_by_scope":{k:v["failed_or_partial"] for k,v in scopes.items() if v["failed_or_partial"]},"new_prospective_cells":0},ensure_ascii=False))
