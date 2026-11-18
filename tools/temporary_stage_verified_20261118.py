#!/usr/bin/env python3
"""One-time source projection + pinned 11-repository selftest evidence deposit.
Run only on an isolated, explicitly temporary PR branch; never on main.
Historical source files, original OSF, baseline and all prospectives stay untouched.
"""
import csv
import hashlib
import json
import pathlib
import re
import shutil
from collections import Counter
from datetime import datetime, timezone

ROOT=pathlib.Path.cwd()
A=ROOT/"artifact-bundle"
RUN=44337384660
S=ROOT/"evidence/2026-11-18/01-complete-identity-infrastructure-diagnostic"
M=ROOT/"monitoring/2026-11-18/01-complete-identity-infrastructure-diagnostic"
assert A.is_dir() and not S.exists() and not M.exists()
source=A/f"source-458-{RUN}"
repos=sorted(A.glob(f"repo-*-{RUN}"))
assert source.is_dir() and len(repos)==11,(source,len(repos))
summary=json.loads((source/"evidence/summary.json").read_text(encoding="utf8"))
comparison=json.loads((source/"comparison/comparison.json").read_text(encoding="utf8"))
raw=(source/"evidence/source-attempts.jsonl").read_bytes()
rows=[json.loads(s) for s in raw.splitlines() if s.strip()]
expected={"surface":34,"datacite_doi":102,"openaire_doi":102,"openalex_doi":102,
"zenodo_version":67,"github_main":11,"github_releases":11,"rsd_software":11,
"swh_origin":10,"rsd_issue":2,"rsd_person":1,"rsd_project":1,"workflowhub":4}
assert len(rows)==458 and len(set((r["scope"],r["key"]) for r in rows))==458
assert dict(Counter(r["scope"] for r in rows))==expected
assert summary["full_cohort"] is True and summary["attempted_requests"]==458
assert comparison["identical_key_cohort"] is True
assert comparison["source_new_ledger_sha256"]==hashlib.sha256(raw).hexdigest()
previous=ROOT/"evidence/2026-11-17/02-full-selftest/source-attempts.jsonl"
assert previous.is_file()
assert comparison["source_previous_ledger_sha256"]==hashlib.sha256(previous.read_bytes()).hexdigest()
assert { (r["scope"],r["key"]) for r in rows } == {
 (r["scope"],r["key"]) for r in (json.loads(s) for s in previous.read_bytes().splitlines() if s.strip())}
for r in rows:
    assert r.get("started_at_utc") and r.get("finished_at_utc")
    a=datetime.fromisoformat(r["started_at_utc"].replace("Z","+00:00"))
    b=datetime.fromisoformat(r["finished_at_utc"].replace("Z","+00:00"))
    assert a.utcoffset() is not None and b.utcoffset() is not None and a<=b
    assert "Authorization" not in r and "authorization_header" not in r
n200=sum(r["http_status"]==200 and r["failure"] is None for r in rows)
bad=Counter(r["scope"] for r in rows if not(r["http_status"]==200 and r["failure"] is None))
assert sum(bad.values())==458-n200
assert summary["derived_diagnostic_not_study_units"]["zenodo_total_version_views_fixed_ten"] is None
assert summary["derived_diagnostic_not_study_units"]["zenodo_total_version_downloads_fixed_ten"] is None
reports=[]
for p in repos:
    r=json.loads((p/"result.json").read_text(encoding="utf8"))
    assert r["repo"] in p.name and r["result"]=="PASS" and r["failed_steps"]==0
    assert r["study_cells_added"]==0 and r["observed_sha"]==r["expected_sha"]
    reports.append(r)
assert len({r["repo"] for r in reports})==11
assert Counter(r["check_class"] for r in reports)=={"REPO_RUNTIME_TESTS":9,"STRUCTURAL_ONLY":2}
S.mkdir(parents=True)
M.mkdir(parents=True)
for name in ["source-attempts.jsonl","selected-fields.jsonl","summary.json","sha256-manifest.txt"]:
    shutil.copyfile(source/"evidence"/name,S/name)
for name in ["comparison.json","request-delta.csv"]:
    shutil.copyfile(source/"comparison"/name,M/name)
(M/"repository-results.json").write_text(json.dumps(sorted(reports,key=lambda r:r["repo"]),indent=2,ensure_ascii=False)+"\n",encoding="utf8")
fig=summary["derived_diagnostic_not_study_units"]
record={
 "record_class":"complete_attempt_cohort_and_11_repo_selftest_diagnostic_NOT_prospective",
 "logical_date":"2026-11-18","timezone":"Asia/Shanghai",
 "run_id":RUN,"run_url":f"https://github.com/lostlight530/research-software-identity-audit/actions/runs/{RUN}",
 "source_start_utc":summary["start_utc"],"source_end_utc":summary["end_utc"],
 "source_current_sha256":comparison["source_new_ledger_sha256"],
 "source_previous_sha256":comparison["source_previous_ledger_sha256"],
 "source_attempts":458,"http_200_no_failure":n200,
 "other_failure_or_partial":458-n200,"failure_count_by_scope":dict(bad),
 "fixed_objects":"RS01-RS10","control_is_rs11":False,
 "preregistered_layers":6,"units_per_eligible_timepoint":60,
 "operational_platforms":7,"possible_operational_checks_not_units":70,
 "supplementary_surfaces":34,"new_prospective_cells":0,
 "repo_selftests":11,"runnable_suites":9,"structural_only":2,"failed_repo_jobs":0,
 "scope_counts":comparison["scope_counts"],
 "diagnostic_fields":fig,
 "origin_http_body_bytes_retained":False,
 "runner_artifact_retention_days":30,
 "historical_provider_state_backdated":False,
 "limitations":[
  "58? no: exact failure count is derived by source status; never treat action success as provider success",
  "Zenodo fixed-version aggregate null because version requests were incomplete",
  "403/404/500/timeout/URLError are not software absence or failed scholarly identity",
  "OpenAlex exact DOI is not same as HTTP 200; Work IDs are not DOI counts",
  "openAIRE positive DOI queries are not distinct software works",
  "GitHub main ahead counts are not GitHub releases",
  "two observatories are structural-only, not scientific runtime tests",
  "no original provider HTTP bodies, only client receipts, digests, minimised public fields",
  "no OSF prospective eligibility or declared operational schedule offsets inferred"]
}
record["limitations"][0]="Source attempts "+str(len(rows))+"; exactly "+str(458-n200)+" failed/partial, no fabricated zero or success"
(M/"record.json").write_text(json.dumps(record,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
m=record
(M/"README.md").write_text(
"# 2026-11-18 complete pinned repository and public identity-infrastructure diagnostic\n\n"
+f"**Execution:** [GitHub Actions {RUN}]({record['run_url']}); client UTC start/end "
+f"{m['source_start_utc']} – {m['source_end_utc']}. "
+"All 458 exact source keys match November 17. This is a NEW diagnostic retrieval, not a historical reconstruction or a registered prospective wave.\n\n"
+f"- **11 pinned repositories:** {len(reports)}/11 successful (**9 runnable suites; 2 structural-only observatories**). Green CI is not an external indexing assertion\n"
+f"- **Source attempts:** 458/458; HTTP-200 without recorded failure **{n200}**; failed/partial **{458-n200}**. Zenodo version requests **{bad['zenodo_version']}/67** failed/partial; supplementary surface **{bad['surface']}/34**; retain raw failure/error classes rather than infer absence\n"
+f"- **DataCite** 102 known requests succeeded; **OpenAIRE** {fig['openaire_successful_transport_queries']}/102 succeeded with {fig['openaire_positive_exact_doi_queries']} positive DOI queries; **OpenAlex** {fig['openalex_exact_canonical_doi_matches']} exact canonical DOI matches and {fig['openalex_distinct_returned_work_ids']} distinct Work IDs; **ORCID** {fig['orcid_public_work_groups']} groups/{fig['orcid_public_work_summaries']} work summaries\n"
+"- **Zenodo RS01–RS10 60-version views/download totals = UNKNOWN/null**, not zero and not directly comparable to the prior complete 60-version series. The 67-key API diagnostic was incomplete. **SWH** latest-origin retrieval is status, not proof a new preservation visit was executed\n"
+"- **Interaction:** RSD #1871 previously closed and PR #1897 merged, not new on this capture; rseng/software #498 remains open, unmerged; no live UI deployment/review/endorsement proven\n\n"
+"[Original request receipt projections](../../../evidence/2026-11-18/01-complete-identity-infrastructure-diagnostic/source-attempts.jsonl) · "
+"[per-request changes versus Nov17](request-delta.csv) · [scope comparisons](comparison.json) · "
+"[11-repository check results](repository-results.json) · "
+"[source hashes/provenance](../../../evidence/2026-11-18/01-complete-identity-infrastructure-diagnostic/provenance.json) · "
+"[pinned historical path taxonomy](../../../docs/repository-inventory/2026-11-18/README.md)\n\n"
+"**Contract unchanged:** fixed RS01–RS10, CONTROL != RS11; six layers/60 units per eligible timepoint; seven operational platforms/70 possible checks, 34 supplementary surfaces; **0 new prospective cells**, no OSF edit, Release or DOI.\n",
encoding="utf8")
S.joinpath("README.md").write_text(
"# 2026-11-18 bounded source attempt projections (not original provider HTTP body bytes)\n\n"
"All 458 exact requests have client UTC clocks, source locators, response SHA-256, error/status and minimised fields. "
"Requests with HTTP 500, 403/404 or timeout are retained as failures; missing version counters remain null. "
"Historical original responses are not retroactively rewritten. "
"See [owning monitoring record](../../../monitoring/2026-11-18/01-complete-identity-infrastructure-diagnostic/README.md).\n",
encoding="utf8")
S.joinpath("provenance.json").write_text(json.dumps({
 "record_class":"new_provider_request_attempt_provenance_diagnostic_NOT_PROSPECTIVE",
 "source_workflow_run_id":RUN,
 "source_run_url":record["run_url"],
 "source_collector":"tools/public_source_recheck.py@temporary PR #125 (code exists in CONTROL main)",
 "comparator":"tools/temporary_full_source_compare_20261118.py@temporary PR #125 (intentionally unmerged)",
 "source_ledger_sha256":record["source_current_sha256"],
 "prior_2026_11_17_ledger_sha256":record["source_previous_sha256"],
 "capture_start_utc":record["source_start_utc"],"capture_end_utc":record["source_end_utc"],
 "source_attempt_count":458,"provider_http_raw_body_bytes_retained":False,
 "authorization_headers_retained":False,
 "artifact_zip_retention_days":30,
 "osf_write_attempted":False,"new_prospective_cells":0
},indent=2,ensure_ascii=False)+"\n",encoding="utf8")
S.joinpath("file-sha256-manifest.txt").write_text("".join(
 hashlib.sha256((S/name).read_bytes()).hexdigest()+"  "+name+"\n" for name in
 ("source-attempts.jsonl","selected-fields.jsonl","summary.json","sha256-manifest.txt","provenance.json")
),encoding="utf8")
index=ROOT/"monitoring/README.md"
old=index.read_text(encoding="utf8")
link="- [2026-11-18 / 01-complete-identity-infrastructure-diagnostic](2026-11-18/01-complete-identity-infrastructure-diagnostic/README.md) — pinned 11-repo full selftest and matched 458-key source diagnostic; 402 source requests HTTP200/no failure, 56 failed/partial including 46 Zenodo version attempts; comparison to Nov17 retains unknown, zero prospective cells"
assert "2026-11-18/01-complete-identity-infrastructure-diagnostic" not in old
index.write_text(old.rstrip()+"\n\n"+link+"\n",encoding="utf8")
# Guard against accidental inclusion of confidential bearer tokens in future records
bad=re.compile(r"(?i)(?:ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}|Authorization\\s*:\\s*Bearer\\s+[A-Za-z0-9._~-]{20,})")
for parent in (S,M):
    for f in parent.rglob("*"):
        if f.is_file() and bad.search(f.read_text(encoding="utf8")):
            raise RuntimeError("prohibited token-like material found: "+str(f))
print("STAGED_NOV18="+json.dumps({"source_458":len(rows),"ok_http":n200,"fail_partial":458-n200,
 "repo_suites":len(reports),"source_sha":record["source_current_sha256"],"new_prospective_cells":0},sort_keys=True))
