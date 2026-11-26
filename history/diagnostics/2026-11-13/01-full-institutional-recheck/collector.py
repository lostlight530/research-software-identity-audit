#!/usr/bin/env python3
"""Read-only cloud diagnostics. Not preregistered prospective observations."""
import csv,hashlib,json,os,pathlib,threading,urllib.error,urllib.parse,urllib.request
from collections import Counter,defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
ROOT=pathlib.Path(__file__).resolve().parents[3]
OUT=pathlib.Path(os.environ.get("AUDIT_OUTPUT","cloud-institutional-retest"))
OUT.mkdir(exist_ok=True,parents=True)
utc=lambda:datetime.now(timezone.utc).isoformat()
start=utc()
ua="lostlight530-research-identity-audit/2026-11-13 public read-only"
SURFACES="""WorkflowHub|https://workflowhub.eu/workflows/2332
LifeMonitor|https://api.lifemonitor.eu/openapi.json
Helmholtz RSD|https://helmholtz.software/
RSD|https://research-software-directory.org/software/research-software-identity-audit
nfdi.software|https://nfdi.software/
bio.tools|https://bio.tools/api/tool/life-science-protein-file-audit/?format=json
OpenEBench|https://openebench.bsc.es/monitor/tool/life-science-protein-file-audit
RSE Encyclopedia|https://api.github.com/repos/rseng/software/pulls/498
SciCrunch|https://scicrunch.org/resolver/RRID:SCR_029105.json
RRID Portal|https://rrid.site/resolver/RRID:SCR_029105.json
ScreenIT ASWG|https://aswg.scicrunch.org/resolver/RRID:SCR_029105.json
NIF|https://neuinfo.org/resolver/RRID:SCR_029105.json
dkNET|https://dknet.org/data/source/SCR_029105
InterLex|https://scicrunch.org/interlex/ilx_0381348
EDAM|https://edamontology.org/EDAM.owl
ORCID|https://pub.orcid.org/v3.0/0009-0001-3617-0832/works
Zenodo|https://zenodo.org/api/records/24112453
DataCite|https://api.datacite.org/dois/10.17605/osf.io/5b329
OSF Registration|https://api.osf.io/v2/registrations/5b329/
Internet Archive|https://archive.org/metadata/osf-registrations-5b329-v1
HAL|https://hal.science/hal-05780132v1
OpenAlex|https://api.openalex.org/authors/A5151904252
OpenAIRE|https://api.openaire.eu/search/software?doi=10.5281%2Fzenodo.23365504&format=json
Identifiers.org|https://identifiers.org/rrid:SCR_029105
N2T|https://n2t.net/rrid:SCR_029105
Bioregistry|https://bioregistry.io/api/registry/rrid
Handle DOI|https://hdl.handle.net/api/handles/10.17605/osf.io/5b329
Crossref agency|https://api.crossref.org/works/10.17605/osf.io/5b329/agency
Software Heritage|https://archive.softwareheritage.org/api/1/origin/https://github.com/lostlight530/welcome-to-github/visit/latest/
GitHub|https://api.github.com/repos/lostlight530/welcome-to-github/releases?per_page=100
CiteAs|https://api.citeas.org/product/https%3A%2F%2Fgithub.com%2Flostlight530%2Fwelcome-to-github
CWL Viewer|https://view.commonwl.org/
RO-Crate|https://w3id.org/ro/crate/1.1
CFF|https://citation-file-format.github.io/"""
fixed=["welcome-to-github","zero-entropy-lab","Axiom-0","reflective-continuum","agent-foundations","auto-doc-engine","epistemic-pipeline","sci-render-kit","china-agentic-observatory","agentic-frontier-observatory"]
surfaces=[x.split("|",1) for x in SURFACES.splitlines()]
assert len(surfaces)==34
with (ROOT/"evidence/2026-11-08/02-complete-institutional-recheck/doi-identifiers.csv").open(encoding="utf-8-sig",newline="") as f:
    dois={x["doi"].lower() for x in csv.DictReader(f)}
with (ROOT/"evidence/2026-11-12/01-identity-claim-reconciliation/zenodo-all-version-statistics.csv").open(encoding="utf-8-sig",newline="") as f:
    versions=list(csv.DictReader(f))
for x in versions:
    if x["repository"] in fixed and x["version_index"]=="5":
        dois.add(x["doi"].lower())
assert len(dois)==102,(len(dois),sorted(dois)[-5:])
assert len(versions)==67
tasks=[("surface",f"{i:02d}:{name}",url) for i,(name,url) in enumerate(surfaces,1)]
for d in sorted(dois):
    tasks.extend([("datacite_doi",d,"https://api.datacite.org/dois/"+d),
      ("openaire_doi",d,"https://api.openaire.eu/search/software?"+urllib.parse.urlencode({"doi":d,"format":"json"})),
      ("openalex_doi",d,"https://api.openalex.org/works/https://doi.org/"+d)])
for row in versions:
    tasks.append(("zenodo_version",row["repository"]+":"+row["record_id"],"https://zenodo.org/api/records/"+row["record_id"]))
for n in fixed+["research-software-identity-audit"]:
    tasks.extend([("github_main",n,f"https://api.github.com/repos/lostlight530/{n}/branches/main"),("github_releases",n,f"https://api.github.com/repos/lostlight530/{n}/releases?per_page=100"),("rsd_software",n,"https://research-software-directory.org/software/"+n.lower())])
for n in fixed:
    tasks.append(("swh_origin",n,"https://archive.softwareheritage.org/api/1/origin/https://github.com/lostlight530/"+n+"/visit/latest/"))
for i in [1870,1871]:
    tasks.append(("rsd_issue",str(i),f"https://api.github.com/repos/research-software-directory/RSD-as-a-service/issues/{i}"))
tasks.extend([("rsd_person","person","https://research-software-directory.org/persons/19b238a1-a7c4-4cdb-894e-38686c617cbe/software"),
("rsd_project","project","https://research-software-directory.org/projects/agentic-research-constellation")])
for i in [2332,2334,2337,2347]:
    tasks.append(("workflowhub","workflow-"+str(i),f"https://workflowhub.eu/workflows/{i}.json"))
assert len(tasks)==34+306+67+33+10+2+2+4
locks=defaultdict(lambda:threading.BoundedSemaphore(2))
def fetch(item):
    scope,key,url=item
    hostname=urllib.parse.urlsplit(url).hostname
    with locks[hostname]:
        a=utc();status=None;err=None;raw=b"";fields={};size_header=None
        h={"User-Agent":ua,"Accept":"application/json, text/html;q=0.8, */*;q=0.2"}
        if hostname=="api.github.com" and os.getenv("GITHUB_TOKEN"):
            h["Authorization"]="Bearer "+os.environ["GITHUB_TOKEN"]
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers=h),timeout=7) as r:
                status=r.status; raw=r.read(2000001);size_header=r.headers.get("Content-Length")
                if len(raw)>2000000:err="TRUNCATED_RESPONSE_2MB"
        except urllib.error.HTTPError as e:
            status=e.code;err="HTTP_"+str(status)
            try:raw=e.read(300000)
            except Exception:pass
        except Exception as e:
            err=type(e).__name__  # exclude private network diagnostics
        b=utc()
        if status==200 and not err:
            try:
                obj=json.loads(raw)
                if scope=="datacite_doi":
                    q=obj.get("data",{}).get("attributes",{});fields={"doi":q.get("doi"),"state":q.get("state"),"registered":q.get("registered"),"resource_type":q.get("types",{}).get("resourceTypeGeneral")}
                elif scope=="openaire_doi":
                    t=obj.get("response",{}).get("header",{}).get("total");fields={"result_total":t.get("$") if isinstance(t,dict) else t}
                elif scope=="openalex_doi":fields={"work_id":obj.get("id"),"doi":obj.get("doi"),"type":obj.get("type"),"canonical_doi_exact_match":(obj.get("doi") or "").lower().rstrip("/")==("https://doi.org/"+key).lower()}
                elif scope=="zenodo_version":
                    z=obj.get("stats",{});fields={"id":obj.get("id"),"doi":obj.get("doi"),"conceptdoi":obj.get("conceptdoi"),"version_views":z.get("version_views"),"version_downloads":z.get("version_downloads"),"family_views_attached":z.get("views"),"family_downloads_attached":z.get("downloads")}
                elif scope=="github_main":fields={"sha":obj.get("commit",{}).get("sha")}
                elif scope=="github_releases":fields={"releases":len(obj),"latest_tag":obj[0].get("tag_name") if obj else None,"latest_published_at":obj[0].get("published_at") if obj else None}
                elif scope=="swh_origin":fields={"visit":obj.get("visit"),"status":obj.get("status"),"date":obj.get("date"),"snapshot":obj.get("snapshot")}
                elif scope=="rsd_issue":fields={"state":obj.get("state"),"updated_at":obj.get("updated_at"),"closed_at":obj.get("closed_at")}
                elif scope=="workflowhub":
                    data=obj.get("data") or {}; attrs=data.get("attributes") or {}; fields={"id":obj.get("id") or data.get("id"),"title":obj.get("title") or attrs.get("title"),"version":obj.get("version") or attrs.get("version"),"json_top_level_keys":sorted(obj.keys())[:12]}
                elif scope=="surface" and key.startswith("16:"):
                    groups=obj.get("group",[])
                    src=Counter((((s.get("source") or {}).get("source-name") or {}).get("value") or "UNKNOWN") for g in groups for s in (g.get("work-summary") or []))
                    fields={"groups":len(groups),"summaries":sum(len(g.get("work-summary") or []) for g in groups),"source_counts":dict(src)}
                elif scope=="surface" and key.startswith("22:"):
                    fields={"works_count":obj.get("works_count"),"cited_by_count":obj.get("cited_by_count"),"id":obj.get("id")}
            except Exception as e:
                fields={"representation":"PUBLIC_HTTP_200_NON_JSON_OR_UNSUPPORTED","semantic_identity_status":"NOT_VERIFIED","parse_kind":type(e).__name__}
        return {"scope":scope,"key":key,"locator":url,"started_at_utc":a,"finished_at_utc":b,"http_status":status,"failure":err,"raw_sha256":hashlib.sha256(raw).hexdigest() if raw else None,"response_bytes_read":len(raw),"content_length":size_header,"selected_public_fields":fields}
with ThreadPoolExecutor(max_workers=10) as pool:
    rows=list(pool.map(fetch,tasks))
with (OUT/"source-attempts.jsonl").open("w",encoding="utf8") as f:
    for row in rows:f.write(json.dumps(row,sort_keys=True,ensure_ascii=False)+"\n")
with (OUT/"selected-fields.jsonl").open("w",encoding="utf8") as f:
    for row in rows:
        if row["selected_public_fields"]:f.write(json.dumps({k:row[k] for k in ["scope","key","started_at_utc","finished_at_utc","selected_public_fields"]},ensure_ascii=False)+"\n")
summary={"record_class":"bounded_public_cloud_retest_not_prospective","start_utc":start,"end_utc":utc(),"source":"GitHub Actions runner / unauthenticated public scholarly endpoints, GitHub token for public GitHub only","fixed_corpus":"RS01-RS10","control_is_rs11":False,"osf_write_attempted":False,"layers":6,"preregistered_units_per_eligible_timepoint":60,"new_prospective_cells":0,"surface_count":len(surfaces),"known_doi_inventory":len(dois),"scope_counts":{},"limits":["all results are diagnostic attempts, not a complete confirmed indexing census","HTTP 200 does not imply object identity verified","HTTP 404/403/429 and timeout do not imply nonexistence","response SHA-256 only; original response bytes are not published","no authenticated OSF/ORCID/RSD account access or UI claim action","timestamp is client receipt, not first indexed or published","OpenAlex 200 does not mean canonical requested DOI equals returned Work DOI","public HTML document response is not independent identity verification"]}
for scope in sorted({row["scope"] for row in rows}):
    x=[row for row in rows if row["scope"]==scope]
    summary["scope_counts"][scope]={"attempted":len(x),"http_statuses":dict(Counter(str(q["http_status"]) for q in x)),"failed_or_partial":sum(q["failure"] is not None for q in x)}
ax=[r for r in rows if r["scope"]=="openalex_doi"]
oa=[r for r in rows if r["scope"]=="openaire_doi"]
zv=[r for r in rows if r["scope"]=="zenodo_version"]
oc=[r for r in rows if r["scope"]=="surface" and r["key"].startswith("16:")]
summary["derived_diagnostic_not_study_units"]={
 "openalex_exact_canonical_doi_matches":sum(r["selected_public_fields"].get("canonical_doi_exact_match",False) for r in ax),
 "openalex_distinct_returned_work_ids":len({r["selected_public_fields"].get("work_id") for r in ax if r["selected_public_fields"].get("work_id")}),
 "openaire_positive_exact_doi_queries":sum(str(r["selected_public_fields"].get("result_total","0")).isdigit() and int(r["selected_public_fields"].get("result_total","0"))>0 for r in oa),
 "zenodo_total_version_views_fixed_ten":sum(int(r["selected_public_fields"].get("version_views") or 0) for r in zv if r["key"].split(":")[0] in fixed),
 "zenodo_total_version_downloads_fixed_ten":sum(int(r["selected_public_fields"].get("version_downloads") or 0) for r in zv if r["key"].split(":")[0] in fixed),
 "orcid_public_work_groups":oc[0]["selected_public_fields"].get("groups") if oc else None,
 "orcid_public_work_summaries":oc[0]["selected_public_fields"].get("summaries") if oc else None,
}
with (OUT/"summary.json").open("w",encoding="utf8") as f:json.dump(summary,f,indent=2,ensure_ascii=False)
with (OUT/"sha256-manifest.txt").open("w",encoding="utf8") as f:
    for path in sorted(OUT.glob("*")):
        if path.name!="sha256-manifest.txt":f.write(hashlib.sha256(path.read_bytes()).hexdigest()+"  "+path.name+"\n")
print("AUDIT_CLOUD_SUMMARY_JSON="+json.dumps(summary,sort_keys=True,ensure_ascii=False))
print("AUDIT_SOURCE_LEDGER_SHA256="+hashlib.sha256((OUT/"source-attempts.jsonl").read_bytes()).hexdigest())
