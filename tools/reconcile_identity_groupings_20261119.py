#!/usr/bin/env python3
"""Reconcile the 2026-11-19 public-source recapture without changing study units."""
from __future__ import annotations
import argparse, csv, hashlib, json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

FIXED={"welcome-to-github","zero-entropy-lab","Axiom-0","reflective-continuum","agent-foundations","auto-doc-engine","epistemic-pipeline","sci-render-kit","china-agentic-observatory","agentic-frontier-observatory"}
CONTROL="research-software-identity-audit"
SUPPLEMENTARY="life-science-ecosystem-lab"

def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

def read_csv(path):
    with path.open(encoding="utf-8-sig",newline="") as stream:
        return list(csv.DictReader(stream))

def write_csv(path,fields,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,extrasaction="ignore",lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key:csv_value(row.get(key)) for key in fields})

def csv_value(value):
    if isinstance(value,(list,dict)): return json.dumps(value,ensure_ascii=False,sort_keys=True)
    return "" if value is None else value

def as_int(value):
    try: return int(value)
    except (TypeError,ValueError): return None

def role(repository):
    if repository in FIXED: return "FIXED_RS01_RS10"
    if repository==CONTROL: return "CONTROL_NOT_RS11"
    if repository==SUPPLEMENTARY: return "SUPPLEMENTARY_NOT_SAMPLE"
    return "UNCLASSIFIED"

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input",required=True,type=Path)
    parser.add_argument("--previous",required=True,type=Path)
    parser.add_argument("--versions",required=True,type=Path)
    parser.add_argument("--surface-registry",required=True,type=Path)
    parser.add_argument("--output",required=True,type=Path)
    parser.add_argument("--logical-date",default="2026-11-19")
    args=parser.parse_args()
    if args.output.exists() and any(args.output.iterdir()): parser.error("output must be new or empty")
    args.output.mkdir(parents=True,exist_ok=True)
    current=read_jsonl(args.input/"source-attempts.jsonl")
    previous=read_jsonl(args.previous)
    versions=read_csv(args.versions)
    surfaces=read_csv(args.surface_registry)
    current_by_key={(r["scope"],r["key"]):r for r in current}
    previous_by_key={(r["scope"],r["key"]):r for r in previous}
    if len(current)!=458 or len(current_by_key)!=458: raise SystemExit("expected 458 unique current requests")
    if set(current_by_key)!=set(previous_by_key): raise SystemExit("current and Nov18 request keys differ")
    if len(versions)!=67 or len({r["doi"] for r in versions})!=67: raise SystemExit("67-version inventory mismatch")
    if len(surfaces)!=34: raise SystemExit("34-surface registry mismatch")
    version_by_doi={r["doi"].lower():r for r in versions}
    scope_counts=Counter(r["scope"] for r in current)
    expected={"surface":34,"datacite_doi":102,"openaire_doi":102,"openalex_doi":102,"zenodo_version":67,"github_main":11,"github_releases":11,"rsd_software":11,"swh_origin":10,"rsd_issue":2,"rsd_person":1,"rsd_project":1,"workflowhub":4}
    if dict(scope_counts)!=expected: raise SystemExit("source cohort scope drift: "+repr(dict(scope_counts)))

    # Request-level comparison. A digest change alone is not a semantic change.
    delta=[]; delta_counts=defaultdict(Counter)
    for key,now in sorted(current_by_key.items()):
        old=previous_by_key[key]; scope=key[0]
        transport=(now.get("http_status")!=old.get("http_status") or now.get("failure")!=old.get("failure"))
        selected=now.get("selected_public_fields")!=old.get("selected_public_fields")
        digest=now.get("raw_sha256")!=old.get("raw_sha256")
        delta_counts[scope]["attempted"]+=1
        delta_counts[scope]["transport_changed"]+=int(transport)
        delta_counts[scope]["selected_fields_changed"]+=int(selected)
        delta_counts[scope]["response_digest_changed"]+=int(digest)
        delta.append({"scope":scope,"key":key[1],"previous_http_status":old.get("http_status"),"current_http_status":now.get("http_status"),"previous_failure":old.get("failure"),"current_failure":now.get("failure"),"transport_changed":transport,"selected_fields_changed":selected,"response_digest_changed":digest,"previous_sha256":old.get("raw_sha256"),"current_sha256":now.get("raw_sha256")})
    write_csv(args.output/"request-delta-vs-2026-11-18.csv",["scope","key","previous_http_status","current_http_status","previous_failure","current_failure","transport_changed","selected_fields_changed","response_digest_changed","previous_sha256","current_sha256"],delta)

    # All 34 supplementary surfaces.
    surface_rows=[]
    for index,item in enumerate(surfaces,1):
        key=f"{index:02d}:{item['surface']}"; row=current_by_key[("surface",key)]; fields=row.get("selected_public_fields") or {}
        surface_rows.append({"surface_row":index,"surface":item["surface"],"source_locator":item["source_locator"],"http_status":row.get("http_status"),"failure":row.get("failure"),"transport_state":row.get("transport_state"),"response_bytes_read":row.get("response_bytes_read"),"response_sha256":row.get("raw_sha256"),"semantic_identity_status":fields.get("semantic_identity_status") or ("SELECTED_FIELDS_AVAILABLE" if fields else "NOT_VERIFIED_BY_THIS_EXTRACTOR"),"selected_public_fields":fields})
    write_csv(args.output/"surface-results.csv",["surface_row","surface","source_locator","http_status","failure","transport_state","response_bytes_read","response_sha256","semantic_identity_status","selected_public_fields"],surface_rows)

    # DataCite exact DOI state and resource-type projection.
    datacite_rows=[]
    for row in current:
        if row["scope"]!="datacite_doi": continue
        fields=row.get("selected_public_fields") or {}
        datacite_rows.append({"doi":row["key"],"http_status":row.get("http_status"),"failure":row.get("failure"),"returned_doi":fields.get("doi"),"state":fields.get("state"),"registered":fields.get("registered"),"resource_type":fields.get("resource_type")})
    write_csv(args.output/"datacite-doi-state.csv",["doi","http_status","failure","returned_doi","state","registered","resource_type"],datacite_rows)

    # OpenAIRE exact DOI query -> result ID projection.
    openaire_rows=[r for r in current if r["scope"]=="openaire_doi"]
    query_rows=[]; result_to_dois=defaultdict(set); result_meta=defaultdict(lambda:{"types":set(),"titles":set(),"original_ids":set(),"sources":set(),"hosts":set()}); doi_to_ids={}
    for row in openaire_rows:
        f=row.get("selected_public_fields") or {}; results=f.get("results") or []
        ids=sorted({item.get("id") for item in results if item.get("id")})
        doi=row["key"].lower(); doi_to_ids[doi]=ids
        complete=bool(f.get("result_page_complete")) if row.get("http_status")==200 and row.get("failure") is None else False
        query_rows.append({"queried_doi":doi,"http_status":row.get("http_status"),"failure":row.get("failure"),"result_total":f.get("result_total"),"returned_result_count":f.get("returned_result_count"),"page":f.get("page"),"page_size":f.get("page_size"),"result_page_complete":complete,"distinct_result_ids":ids})
        if complete:
            for item in results:
                rid=item.get("id")
                if not rid: continue
                result_to_dois[rid].add(doi)
                for field,target in [("type","types"),("title","titles"),("original_id","original_ids"),("collected_from","sources"),("hosted_by","hosts")]:
                    if item.get(field) is not None: result_meta[rid][target].add(str(item[field]))
    write_csv(args.output/"openaire-doi-query-results.csv",["queried_doi","http_status","failure","result_total","returned_result_count","page","page_size","result_page_complete","distinct_result_ids"],query_rows)

    result_rows=[]
    for rid,doi_set in sorted(result_to_dois.items()):
        meta=result_meta[rid]; repos=sorted({version_by_doi[d]["repository"] for d in doi_set if d in version_by_doi})
        result_rows.append({"openaire_result_id":rid,"type":sorted(meta["types"]),"titles":sorted(meta["titles"]),"original_ids":sorted(meta["original_ids"]),"collected_from":sorted(meta["sources"]),"hosted_by":sorted(meta["hosts"]),"matched_query_doi_count":len(doi_set),"queried_dois":sorted(doi_set),"zenodo_repositories":repos,"zenodo_repository_count":len(repos),"cross_repository_result":len(repos)>1})
    write_csv(args.output/"openaire-result-id-groups.csv",["openaire_result_id","type","titles","original_ids","collected_from","hosted_by","matched_query_doi_count","queried_dois","zenodo_repositories","zenodo_repository_count","cross_repository_result"],result_rows)

    # Twelve Zenodo software families: aggregation and split are distinct directions.
    repo_rows=[]
    for repository in sorted({r["repository"] for r in versions}):
        repo_versions=[r for r in versions if r["repository"]==repository]
        repo_result_to_dois=defaultdict(set); complete_n=positive=occurrences=split_n=0; split_dois=[]
        for version in repo_versions:
            doi=version["doi"].lower()
            q=next((x for x in query_rows if x["queried_doi"]==doi),None)
            if not q or not q["result_page_complete"]: continue
            complete_n+=1; occurrences+=as_int(q["returned_result_count"]) or 0; positive+=int((as_int(q["result_total"]) or 0)>0)
            ids=q["distinct_result_ids"]
            if len(ids)>1: split_n+=1; split_dois.append(doi)
            for rid in ids: repo_result_to_dois[rid].add(doi)
        aggregate_ids=sorted(rid for rid,ds in repo_result_to_dois.items() if len(ds)>1)
        repo_rows.append({"repository":repository,"object_role":role(repository),"version_doi_count":len(repo_versions),"complete_doi_queries":complete_n,"unresolved_or_incomplete_queries":len(repo_versions)-complete_n,"positive_doi_queries":positive,"returned_result_occurrences":occurrences,"distinct_openaire_result_ids":len(repo_result_to_dois),"aggregate_result_id_count":len(aggregate_ids),"aggregate_result_ids":aggregate_ids,"split_doi_query_count":split_n,"split_doi_queries":split_dois})
    write_csv(args.output/"openaire-12-repository-grouping.csv",["repository","object_role","version_doi_count","complete_doi_queries","unresolved_or_incomplete_queries","positive_doi_queries","returned_result_occurrences","distinct_openaire_result_ids","aggregate_result_id_count","aggregate_result_ids","split_doi_query_count","split_doi_queries"],repo_rows)

    # OpenAlex DOI-to-Work mapping. One returned Work per exact DOI endpoint is not a multi-Work split.
    openalex_rows=[r for r in current if r["scope"]=="openalex_doi"]
    openalex_by_doi={}; work_to_dois=defaultdict(set)
    for row in openalex_rows:
        f=row.get("selected_public_fields") or {}; doi=row["key"].lower(); wid=f.get("work_id")
        if wid: work_to_dois[wid].add(doi)
        openalex_by_doi[doi]={"work_id":wid,"returned_primary_doi":f.get("doi"),"type":f.get("type"),"exact_match":f.get("canonical_doi_exact_match"),"http_status":row.get("http_status"),"failure":row.get("failure")}
    work_rows=[]
    for wid,doi_set in sorted(work_to_dois.items()):
        repos=sorted({version_by_doi[d]["repository"] for d in doi_set if d in version_by_doi})
        work_rows.append({"openalex_work_id":wid,"queried_doi_count":len(doi_set),"queried_dois":sorted(doi_set),"zenodo_repositories":repos,"zenodo_repository_count":len(repos),"multiple_doi_queries_same_work":len(doi_set)>1})
    write_csv(args.output/"openalex-work-id-groups.csv",["openalex_work_id","queried_doi_count","queried_dois","zenodo_repositories","zenodo_repository_count","multiple_doi_queries_same_work"],work_rows)

    # Zenodo per-version API projection; aggregate fixed-ten metrics only when all 60 are complete.
    zenodo_rows=[]
    for version in versions:
        key=version["repository"]+":"+version["record_id"]; row=current_by_key[("zenodo_version",key)]; f=row.get("selected_public_fields") or {}
        zenodo_rows.append({"repository":version["repository"],"object_role":role(version["repository"]),"record_id":version["record_id"],"doi":version["doi"],"version":version["version"],"version_index":version["version_index"],"is_latest":version["is_latest"],"http_status":row.get("http_status"),"failure":row.get("failure"),"api_returned_doi":f.get("doi"),"conceptdoi":f.get("conceptdoi"),"version_views":f.get("version_views"),"version_downloads":f.get("version_downloads"),"family_views_attached":f.get("family_views_attached"),"family_downloads_attached":f.get("family_downloads_attached")})
    write_csv(args.output/"zenodo-67-version-records.csv",["repository","object_role","record_id","doi","version","version_index","is_latest","http_status","failure","api_returned_doi","conceptdoi","version_views","version_downloads","family_views_attached","family_downloads_attached"],zenodo_rows)

    openalex_repo_rows=[]
    for repository in sorted({r["repository"] for r in versions}):
        repo_versions=[r for r in versions if r["repository"]==repository]; work_dois=defaultdict(set); successful=exact=missing=version_primary=concept_primary=0
        for version in repo_versions:
            doi=version["doi"].lower(); item=openalex_by_doi.get(doi,{})
            successful+=int(item.get("http_status")==200 and item.get("failure") is None)
            exact+=int(item.get("exact_match") is True)
            if not item.get("work_id"): missing+=1
            else: work_dois[item["work_id"]].add(doi)
            primary=(item.get("returned_primary_doi") or "").lower().replace("https://doi.org/","")
            version_primary+=int(primary==doi)
            zrow=next((z for z in zenodo_rows if z["doi"].lower()==doi),{})
            concept=(zrow.get("conceptdoi") or "").lower().replace("https://doi.org/","")
            concept_primary+=int(bool(concept) and primary==concept)
        shared=sorted(wid for wid,ds in work_dois.items() if len(ds)>1)
        openalex_repo_rows.append({"repository":repository,"object_role":role(repository),"version_doi_count":len(repo_versions),"successful_doi_queries":successful,"missing_work_responses":missing,"exact_version_doi_primary_matches":exact,"distinct_work_ids":len(work_dois),"work_ids_shared_by_multiple_version_doi_queries":len(shared),"shared_work_ids":shared,"version_primary_doi_matches":version_primary,"concept_primary_doi_matches":concept_primary})
    write_csv(args.output/"openalex-12-repository-version-grouping.csv",["repository","object_role","version_doi_count","successful_doi_queries","missing_work_responses","exact_version_doi_primary_matches","distinct_work_ids","work_ids_shared_by_multiple_version_doi_queries","shared_work_ids","version_primary_doi_matches","concept_primary_doi_matches"],openalex_repo_rows)

    # Platform summary and prior-comparable fields.
    orcid_row=current_by_key[("surface","16:ORCID")]; orcid=orcid_row.get("selected_public_fields") or {}
    profile_row=current_by_key[("surface","22:OpenAlex")]; profile=profile_row.get("selected_public_fields") or {}
    datacite_states=Counter(r["state"] or "UNKNOWN" for r in datacite_rows); datacite_types=Counter(r["resource_type"] or "UNKNOWN" for r in datacite_rows)
    openalex_exact=sum(x["exact_match"] is True for x in openalex_by_doi.values())
    openalex_success=sum(x["http_status"]==200 and x["failure"] is None for x in openalex_by_doi.values())
    openaire_complete=sum(x["result_page_complete"] for x in query_rows)
    openaire_positive=sum((as_int(x["result_total"]) or 0)>0 for x in query_rows if x["result_page_complete"])
    zenodo_success=sum(r["http_status"]==200 and r["failure"] is None for r in zenodo_rows)
    fixed_zenodo=[r for r in zenodo_rows if r["object_role"]=="FIXED_RS01_RS10"]
    fixed_complete=len(fixed_zenodo)==60 and all(r["http_status"]==200 and r["failure"] is None and type(r["version_views"]) is int and type(r["version_downloads"]) is int for r in fixed_zenodo)
    summary={
      "record_class":"bounded_public_infrastructure_recheck_not_prospective","logical_date":args.logical_date,"generated_at_utc":datetime.now(timezone.utc).isoformat(),
      "fixed_corpus":"RS01-RS10","control_is_rs11":False,"preregistered_layers":6,"eligible_units_per_scheduled_timepoint":60,"operational_platforms":7,"possible_platform_checks_not_units":70,
      "supplementary_surfaces":34,"known_doi_inventory":102,"zenodo_version_inventory":67,"source_attempts":len(current),"source_request_keys_identical_to_2026-11-18":True,"new_prospective_cells":0,"osf_write_attempted":False,
      "scope_counts":{s:{"attempted":n,"http_200_without_failure":sum(r["http_status"]==200 and r["failure"] is None for r in current if r["scope"]==s),"failed_or_partial":sum(r["failure"] is not None for r in current if r["scope"]==s)} for s,n in sorted(scope_counts.items())},
      "supplementary_surface_http_200":sum(r["http_status"]==200 and r["failure"] is None for r in surface_rows),"supplementary_surface_failures_or_partial":sum(r["failure"] is not None for r in surface_rows),
      "datacite":{"requests":len(datacite_rows),"http_200":sum(r["http_status"]==200 and r["failure"] is None for r in datacite_rows),"states":dict(datacite_states),"resource_types":dict(datacite_types)},
      "openaire":{"doi_queries":len(query_rows),"complete_queries":openaire_complete,"positive_complete_queries":openaire_positive,"distinct_result_ids":len(result_to_dois),"result_occurrences":sum(as_int(r["returned_result_count"]) or 0 for r in query_rows if r["result_page_complete"]),"zenodo_repository_families":len(repo_rows),"repository_grouping_complete":openaire_complete==102,"aggregate_result_ids_within_repository":sum(as_int(r["aggregate_result_id_count"]) or 0 for r in repo_rows),"split_doi_queries_within_repository":sum(as_int(r["split_doi_query_count"]) or 0 for r in repo_rows)},
      "openalex":{"doi_queries":len(openalex_rows),"successful_queries":openalex_success,"exact_canonical_doi_matches":openalex_exact,"distinct_work_ids":len(work_to_dois),"author_profile_works_count":profile.get("works_count"),"author_profile_cited_by_count":profile.get("cited_by_count"),"zenodo_repository_families":len(openalex_repo_rows)},
      "orcid":{"http_status":orcid_row.get("http_status"),"groups":orcid.get("groups"),"work_summaries":orcid.get("summaries"),"source_counts":orcid.get("source_counts")},
      "zenodo":{"version_requests":len(zenodo_rows),"http_200":zenodo_success,"fixed_ten_version_rows":len(fixed_zenodo),"fixed_ten_complete":fixed_complete,"fixed_ten_version_views":sum(r["version_views"] for r in fixed_zenodo) if fixed_complete else None,"fixed_ten_version_downloads":sum(r["version_downloads"] for r in fixed_zenodo) if fixed_complete else None,"family_counts":dict(Counter(r["repository"] for r in zenodo_rows))},
      "workflowhub":[{"key":r["key"],**(r.get("selected_public_fields") or {})} for r in current if r["scope"]=="workflowhub"],
      "limits":["OpenAIRE aggregate: one result ID matches multiple queried DOI values within a repository family","OpenAIRE split: one exact DOI query returns multiple distinct result IDs","only complete OpenAIRE result pages enter grouping","OpenAlex exact DOI matches and Work IDs are not equivalent to distinct software objects","HTTP 200 is transport success, not proof of indexing identity or independent adoption","403/404/timeout/truncation remain unresolved or blocked, never absence","no original provider HTTP bodies retained; SHA-256, byte length, clocks and selected fields only","no OSF write, schedule change, new Release, new DOI or prospective study cell"]}
    summary["comparison_to_2026-11-18"]={scope:dict(counts) for scope,counts in sorted(delta_counts.items())}
    (args.output/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    maintainer_context={"record_class":"maintainer_supplied_context_not_provider_capture","source_capture_time":None,"received_in_conversation_logical_date":args.logical_date,
      "openaire":"12 repository families; generally one aggregate and one split, some two splits",
      "openalex":"34; 8 and 9 version split (maintainer wording retained verbatim; exact counting unit not further specified)",
      "datacite_orcid":"maintainer reports no change",
      "interpretation":"These statements are comparison context, not independently timestamped provider evidence; API recapture and identity grouping outputs are separate."}
    (args.output/"maintainer-context.json").write_text(json.dumps(maintainer_context,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    readme=(
      "# 2026-11-19 complete public identity-infrastructure recheck\n\n"
      "**Class:** future-only public diagnostic, not prospective research observation. The 458 request keys match the 2026-11-18 cohort. Per-request clocks are in the source ledger; capture summary is in summary.json.\n\n"
      "## Scope\n\n"
      "- 34 supplementary institution/service/standard surfaces\n"
      "- 102 exact DOI keys queried independently against DataCite, OpenAIRE and OpenAlex (306 requests)\n"
      "- 67 individually versioned Zenodo records: 60 across RS01-RS10, 5 CONTROL, 2 supplementary LSEL\n"
      "- 11 GitHub main, 11 GitHub Releases, 11 RSD software, 10 Software Heritage origins, 2 RSD issues, 1 RSD person, 1 RSD project and 4 WorkflowHub records\n\n"
      "Fixed corpus RS01-RS10; CONTROL is not RS11; six layers and 60 units per eligible scheduled timepoint remain frozen. Seven operational platforms/70 possible checks are a separate denominator. New prospective cells: 0.\n\n"
      "## OpenAIRE aggregation and split\n\n"
      "openaire-doi-query-results.csv preserves each DOI query, API total, returned count, page completeness and result IDs. openaire-result-id-groups.csv maps each result ID to queried DOI values. openaire-12-repository-grouping.csv provides the twelve Zenodo-family grouping view.\n\n"
      "Aggregation means one result ID is returned for multiple DOI queries within a repository family. Split means one DOI query returns multiple distinct result IDs. A completed zero-result query differs from an unsuccessful request. Only complete result pages enter group summaries.\n\n"
      "## OpenAlex and remaining platforms\n\n"
      "openalex-work-id-groups.csv maps Work IDs to queried DOI values; openalex-12-repository-version-grouping.csv maps version DOI queries per family. One exact DOI endpoint returns one Work projection; multiple DOI versions resolving to one Work are shared Work mappings, not a multi-Work split. Author-profile works_count remains distinct from DOI exact matches and distinct Work IDs.\n\n"
      "datacite-doi-state.csv preserves 102 DOI-level states and resource types. ORCID groups, summaries and source counts are in summary.json. zenodo-67-version-records.csv retains every version row; fixed-ten totals remain null unless all 60 rows have valid counters. surface-results.csv retains all 34 endpoints. request-delta-vs-2026-11-18.csv compares exact request keys.\n\n"
      "## Evidence limits\n\n"
      "Source ledger -> selected fields -> grouping tables -> summary -> this report. Prior evidence is not overwritten. Provider response bodies are not retained; only response digests, byte lengths, client timestamps and minimized public fields are retained. User-supplied statements are separately retained in maintainer-context.json.\n\n"
      "**Disposition:** DIAGNOSTIC_RECHECK / SOURCE-SPECIFIC_PARTIAL_OR_COMPLETE / NO_PROSPECTIVE_CELLS / FROZEN_CONTRACT_UNCHANGED.\n"
    )
    (args.output/"README.md").write_text(readme,encoding="utf-8")
    manifest=[]
    for path in sorted(args.input.iterdir()):
        if path.is_file(): manifest.append({"path":path.name,"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),"bytes":path.stat().st_size})
    (args.output/"input-file-manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print("RECONCILIATION_SUMMARY="+json.dumps(summary,sort_keys=True,ensure_ascii=False))

if __name__=="__main__":
    main()
