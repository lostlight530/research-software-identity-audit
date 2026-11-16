#!/usr/bin/env python3
"""One-time stage of a verified GitHub Actions artifact into a separate evidence branch.
Source data are public diagnostic projections, not provider raw bodies or OSF observations.
"""
import csv,hashlib,json,pathlib,re,shutil
from collections import Counter
from datetime import datetime, timezone
R=pathlib.Path.cwd()
A=R/"artifact-bundle"
RUN=43938763232
source=A/f"source-458-{RUN}"
repos=sorted(A.glob(f"repo-*-{RUN}"))
assert source.exists() and len(repos)==11,(source,len(repos))
S=R/"evidence/2026-11-17/02-full-selftest"
M=R/"monitoring/2026-11-17/02-full-selftest"
S.mkdir(parents=True,exist_ok=False)
M.mkdir(parents=True,exist_ok=False)
raw=(source/"evidence/source-attempts.jsonl").read_bytes()
comparison=json.loads((source/"comparison/comparison.json").read_text(encoding="utf8"))
rows=[json.loads(line) for line in raw.decode("utf8").splitlines() if line.strip()]
assert len(rows)==458 and len({(x["scope"],x["key"]) for x in rows})==458
assert hashlib.sha256(raw).hexdigest()==comparison["source_new_ledger_sha256"]
expected={"surface":34,"datacite_doi":102,"openaire_doi":102,"openalex_doi":102,"zenodo_version":67,"github_main":11,"github_releases":11,"rsd_software":11,"swh_origin":10,"rsd_issue":2,"rsd_person":1,"rsd_project":1,"workflowhub":4}
assert dict(Counter(x["scope"] for x in rows))==expected
for x in rows:
    assert x["started_at_utc"] and x["finished_at_utc"] and "selected_public_fields" in x
    assert "Authorization" not in x and "authorization_header" not in x
for name in ("source-attempts.jsonl","selected-fields.jsonl","summary.json","sha256-manifest.txt"):
    shutil.copyfile(source/"evidence"/name,S/name)
for name in ("comparison.json","request-delta.csv"):
    shutil.copyfile(source/"comparison"/name,M/name)
reports=[]
for path in repos:
    obj=json.loads((path/"result.json").read_text(encoding="utf8"))
    assert obj["repo"] in path.name and obj["result"]=="PASS" and not obj["failed_steps"]
    assert obj["study_cells_added"]==0
    reports.append(obj)
assert len({x["repo"] for x in reports})==11
assert sum(x["check_class"]=="REPO_RUNTIME_TESTS" for x in reports)==9
assert sum(x["check_class"]=="STRUCTURAL_ONLY" for x in reports)==2
assert comparison["new_prospective_cells"]==0
(M/"repository-results.json").write_text(json.dumps(reports,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
fig=comparison["selected_figures"]
n200=sum(x["http_status"]==200 and not x["failure"] for x in rows)
assert n200==451
record={
 "record_class":"complete_attempt_cohort_and_11_repo_selftest_diagnostic_NOT_prospective",
 "logical_date":"2026-11-17","timezone":"Asia/Shanghai",
 "run_id":RUN,
 "run_url":f"https://github.com/lostlight530/research-software-identity-audit/actions/runs/{RUN}",
 "source_start_utc":comparison["started_at_utc"],
 "source_end_utc":comparison["ended_at_utc"],
 "source_current_sha256":comparison["source_new_ledger_sha256"],
 "source_previous_sha256":comparison["source_previous_ledger_sha256"],
 "source_attempts":458,"http_200_no_failure":n200,
 "other_failure_or_partial":458-n200,
 "observed_study_objects":"RS01-RS10","control_is_rs11":False,
 "preregistered_layers":6,"units_per_eligible_timepoint":60,
 "operational_platforms":7,"possible_operational_checks_not_units":70,
 "supplementary_surfaces":34,"new_prospective_cells":0,
 "repository_tests":11,"runnable_tests_pass":9,"structural_only_pass":2,"failed_repo_jobs":0,
 "scope_counts":comparison["scope_counts"],
 "selected_figures":fig,
 "source_latest_raw_http_body_bytes_retained":False,
 "artifact_run_log_retention_days":30,
 "fix_prs":{"agent-foundations":440,"research-software-identity-audit":122},
 "postmerge_11_repo_success_run":43939409812,
 "limitations":[
   "same 102-key known DOI cohort not a global DOI universe",
   "partial request outcomes are preserved, not object absence",
   "SWH visit status not proof of a newly executed preservation visit",
   "HTTP 200 for OpenAlex is not exact canonical DOI match",
   "Zenodo version views/downloads are not unique humans or institutional adoption",
   "original third-party response bytes not retained, hashes and selected fields only",
   "two observatories are structural checks, not runnable scientific-validation suites",
   "the last 11-repository post-merge test is a separate job without redundant 458 external calls",
   "no declared OSF operational schedule offsets and no prospective cells",
 ]
}
(M/"record.json").write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
(M/"README.md").write_text(
f"# November 17 complete bounded 11-repository and 458-request diagnostic selftest\n\n"
f"**Source execution:** [GitHub Actions {RUN}]({record['run_url']}) / "
f"UTC {record['source_start_utc']} – {record['source_end_utc']}. "
"Same exact 458 keys as the November 15 complete source cohort. Original public provider HTTP bodies were **not** archived; client request clocks, response status/failed attempts, response SHA-256, length, locator and minimized selected fields were retained\n\n"
f"- **Source attempts:** 458/458; **HTTP 200 without failure:** {n200}; **failures/partial:** {458-n200}, preserve all seven supplementary exceptions\n"
f"- **Repositories:** 11/11 at pinned SHAs, **9 runnable validation jobs** plus **2 structural-only observatory checks**, all successful after two minimal README/index corrections. Individual logs retained in the expiring Actions artifacts; [machine repo summary](repository-results.json) is durable\n"
f"- **Zenodo RS01–RS10:** 60/60 version responses, {fig['zenodo_fixed60_version_views']} version views and {fig['zenodo_fixed60_version_downloads']} version downloads, no human usage claim\n"
f"- **DataCite:** {fig['datacite_findable']}/102 findable, **OpenAIRE:** {fig['openaire_positive_requests']}/102 positive DOI queries, **OpenAlex:** {fig['openalex_exact_canonical_doi_matches']}/102 exact canonical DOI matches and {fig['openalex_distinct_returned_work_ids']} distinct Work IDs\n"
f"- **ORCID:** {fig['orcid_groups']} groups / {fig['orcid_summaries']} work summaries, **SWH:** {fig['swh_full_latest_visits']}/10 latest origin statuses full. RSD issue #1871 changed to closed, upstream PR #1897 merged, no deployment verified\n"
f"- **Confirmed errors corrected:** [agent-foundations PR #440](https://github.com/lostlight530/agent-foundations/pull/440) and [CONTROL PR #122](https://github.com/lostlight530/research-software-identity-audit/pull/122), both merged. [Post-merge 11-repo rerun](https://github.com/lostlight530/research-software-identity-audit/actions/runs/43939409812) green\n\n"
"**Contract:** fixed RS01–RS10, CONTROL not RS11, 6 layers / 60 units per eligible scheduled point; 7 operational platforms / 70 possible checks, 34 supplementary URLs; **0 prospective cells**. No OSF, DOI, Release, original historical evidence, baseline, schema or schedule changed by this diagnostic evidence addition\n\n"
"[Actual 458 request ledger](../../../evidence/2026-11-17/02-full-selftest/source-attempts.jsonl) · [selected public fields](../../../evidence/2026-11-17/02-full-selftest/selected-fields.jsonl) · [request SHA-256 manifest](../../../evidence/2026-11-17/02-full-selftest/sha256-manifest.txt) · [exact-key comparison](comparison.json) · [per-request delta](request-delta.csv) · [repository results](repository-results.json) · [provenance](../../../evidence/2026-11-17/02-full-selftest/provenance.json)\n",encoding="utf8")
(S/"README.md").write_text(
"# 2026-11-17 bounded full source-attempt and repository selftest evidence\n\n"
"458 original public requests were attempted from one GitHub-hosted collector, but only minimized selected fields, original request URL/UTC client clocks/HTTP status, and SHA-256/byte length were deposited. Full HTTP response bodies are not published. This is not an OSF prospective dataset. See [monitoring interpretation](../../../monitoring/2026-11-17/02-full-selftest/README.md)\n",encoding="utf8")
(S/"provenance.json").write_text(json.dumps({
 "record_class":"public_evidence_provenance_diagnostic_not_prospective",
 "execution_run_id":RUN,"head_pr_test_branch_sha":"660aceefac924817404b3e3bf5e3c2e67811d8e6",
 "source_ledger_sha256":comparison["source_new_ledger_sha256"],
 "previous_ledger_sha256":comparison["source_previous_ledger_sha256"],
 "runner_source_start_utc":comparison["started_at_utc"],
 "runner_source_end_utc":comparison["ended_at_utc"],
 "origin_HTTP_body_bytes_retained":False,
 "authorization_headers_retained":False,
 "artifact_zip_retention_days":30,
 "collector_source":"monitoring/2026-11-13/01-full-institutional-recheck/collector.py",
 "comparator_source":"tools/temporary_full_source_compare_20261117.py (unmerged temporary PR #121)",
 "postmerge_fixed_main_test_run":43939409812,
 "capture_records_are_not_prospective":True
},indent=2)+"\n",encoding="utf8")
(S/"file-sha256-manifest.txt").write_text(
 "\n".join(hashlib.sha256((S/x).read_bytes()).hexdigest()+"  "+x for x in ("source-attempts.jsonl","selected-fields.jsonl","summary.json","sha256-manifest.txt","provenance.json"))+"\n",encoding="utf8")
idx=R/"monitoring/README.md"
link="- [2026-11-17 / 02-full-selftest](2026-11-17/02-full-selftest/README.md) — full 458-key source diagnostic and 11-repository pinned-SHA selftest, 451 nonfailed HTTP-200, seven retained partial/failed surfaces, matched Nov 15 deltas, 2 minimal fixed regressions and postmerge test success; 0 prospective cells"
text=idx.read_text(encoding="utf8")
assert "2026-11-17/01-bounded-identity-infrastructure-recheck/" in text
assert "2026-11-17/02-full-selftest/" not in text
idx.write_text(text.rstrip()+"\n\n"+link+"\n",encoding="utf8")
# Bounded secret scan, including query URLs from selected public endpoints.
bad=[]
p=re.compile(r"(?i)(?:ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9-]{25,}|Bearer\s+[A-Za-z0-9\-._~+/]{24,}|Authorization\s*:\s*Bearer)")
for folder in (S,M):
    for f in folder.rglob("*"):
        if f.is_file() and p.search(f.read_text(encoding="utf8")):bad.append(str(f))
assert not bad,bad
print("STAGED_DIAGNOSTIC="+json.dumps({"repo_checks":len(reports),"source_attempts":len(rows),"http_200":n200,"unknown":458-n200,"sha256":comparison["source_new_ledger_sha256"],"prospective":0},sort_keys=True))
