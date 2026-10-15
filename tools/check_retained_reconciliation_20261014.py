"""Offline checks for October 14 diagnostics and user-source reconciliation. No network."""
import collections,csv,datetime as dt,hashlib,json,re,sys,urllib.parse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def verify():
 checks=[]
 def check(name,value):checks.append({'check':name,'passed':bool(value)})
 def rows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig')))
 fixed=rows(ROOT/'corpus/object-manifest.csv');expected={x['object_id']:x['software_family'] for x in fixed}
 for slug in ('03-midnight-facility-recheck','04-morning-facility-recheck','05-noon-user-pages'):
  e=ROOT/'evidence/2026-10-14'/slug;m=ROOT/'monitoring/2026-10-14'/slug;s=json.loads((m/'capture-summary.json').read_text(encoding='utf-8'))
  check(slug+' diagnostic only',s['record_class']=='diagnostic_monitoring' and s['prospective_dataset_member'] is False)
  manifest=json.loads((e/'artifact-manifest.json').read_text(encoding='utf-8'))['artifacts']
  check(slug+' exact artifact membership',{x['path'] for x in manifest}=={p.relative_to(ROOT).as_posix() for base in (e,m) for p in base.rglob('*') if p.is_file() and p.name not in ('artifact-manifest.json','offline-verification.json')})
  for a in manifest:
   p=ROOT/a['path'];b=p.read_bytes();check('hash '+a['path'],len(b)==a['bytes'] and hashlib.sha256(b).hexdigest()==a['sha256'])
  if slug=='05-noon-user-pages':
   source=json.loads((e/'user-page-transcription.json').read_text(encoding='utf-8'));z=rows(m/'zenodo-page-statistics.csv');w=rows(m/'workflowhub-dashboard-statistics.csv')
   check('user source timestamp remains unknown',source['source_kind']=='user_supplied_page_text' and source['exact_capture_timestamp'] is None and source['workflowhub_dashboard_selected_period'] is None)
   check('page canonical ten and supplement',[(x['object_id'],x['software_family']) for x in z[:10]]==list(expected.items()) and z[-1]['object_id']=='' and z[-1]['scope']=='audit_runtime_supplement')
   for a,b in zip(z,source['zenodo_rows']):
    for k in ('page_unique_views','page_unique_downloads','morning_api_unique_views','morning_api_unique_downloads'):check('user row '+a['software_family']+' '+k,int(a[k])==b[k])
   check('fixed page sum',sum(int(x['page_unique_views']) for x in z[:10])==1361 and sum(int(x['page_unique_downloads']) for x in z[:10])==7)
   check('eleven page sum',sum(int(x['page_unique_views']) for x in z)==1451 and sum(int(x['page_unique_downloads']) for x in z)==10)
   check('page vs API unique difference',sum(int(x['unique_view_difference']) for x in z[:10])==5 and sum(int(x['unique_download_difference']) for x in z[:10])==0)
   check('Dashboard totals and comparable user difference',sum(int(x['views']) for x in w)==1800 and sum(int(x['downloads']) for x in w)==132 and sum(int(x['view_difference']) for x in w)==294 and sum(int(x['download_difference']) for x in w)==6)
   check('two NEXUS totals',sum(int(x['views']) for x in w if x['workflow_id']!='2337')==1595 and sum(int(x['downloads']) for x in w if x['workflow_id']!='2337')==127)
   continue
  ledger=json.loads((e/'capture-manifest.json').read_text(encoding='utf-8'))
  check('public fields not raw '+slug,ledger['public_raw_http_bytes_preserved'] is False)
  logs=ledger['requests'];extracts=json.loads((e/'field-extracts.json').read_text(encoding='utf-8'));by={x['key']:x for x in logs}
  for x in logs:
   check('attempt timestamp '+x['key'],dt.datetime.fromisoformat(x['started_at_utc'])<=dt.datetime.fromisoformat(x['finished_at_utc']))
   if x.get('source_raw_sha256'):check('local source digest syntax '+x['key'],bool(re.fullmatch('[0-9a-f]{64}',x['source_raw_sha256'])))
   if x.get('retry_of') and x.get('http_status')==200:by[x['retry_of']]=x
  def obj(k):
   x=by.get(k,{});return extracts.get(x.get('key'),{}) if x.get('http_status')==200 else {}
  check('complete attempt count '+slug,len(logs)==s['requests'])
  orc=obj('orcid');check('ORCID counts '+slug,len(orc['group'])==s['orcid']['group_count'] and sum(len(g['work-summary']) for g in orc['group'])==s['orcid']['summary_count'])
  oa=obj('openalex_primary_all_corpora');check('OpenAlex Works count '+slug,oa['meta']['count']==s['openalex']['count'] and len(oa['results'])==s['openalex']['returned'])
  check('OpenAlex profile distinct '+slug,obj('openalex_primary_profile')['works_count']==s['openalex']['profile_works_count'])
  drows=rows(m/'datacite-identifiers.csv');expected_dc={}
  for k,x in by.items():
   if x['platform']!='DataCite':continue
   value=obj(k).get('data');items=value if isinstance(value,list) else [value] if isinstance(value,dict) else []
   for a in items:expected_dc[a['attributes']['doi'].lower()]=a['attributes']['state']
  check('DataCite public inventory '+slug,{x['doi']:x['state'] for x in drows}==expected_dc and len(drows)==60)
  ors=rows(m/'orcid-source-summaries.csv');actual_put={str(w['put-code']) for g in orc['group'] for w in g['work-summary']}
  check('ORCID public source ledger '+slug,{x['put_code'] for x in ors}==actual_put and len(ors)==s['orcid']['summary_count'])
  wf=rows(m/'workflowhub-detail-statistics.csv')
  for row,w in zip(wf,s['workflowhub']):
   check('Workflow detail ledger '+slug+' '+w['id'],row['workflow_id']==w['id'] and int(row['latest_version'])==w['latest_version'] and int(row['views'])==w['detail_activity']['views'] and int(row['downloads'])==w['detail_activity']['downloads'])
  cells=rows(m/'platform-states.csv');check('canonical seventy cells '+slug,len(cells)==70 and len({(x['object_id'],x['platform']) for x in cells})==70 and {x['object_id'] for x in cells}==set(expected))
  for oid in expected:
   check('GitHub release '+oid+' '+slug,obj(oid+'_github').get('tag_name')=='v2026.10-open-research-production-framework')
   for ver in ('concept','v1','v2','v3'):check('DataCite '+oid+' '+ver+' '+slug,obj(oid+'_datacite_'+ver)['data']['attributes']['state']=='findable')
   check('OpenAIRE version '+oid+' '+slug,any(('oai:zenodo.org:'+str(obj(oid+'_zenodo').get('id',''))) == (a.get('originalId',{}).get('$') if isinstance(a.get('originalId'),dict) else a.get('originalId')) for a in obj(oid+'_openaire').get('records',[])) if 'morning' in slug else bool(obj(oid+'_openaire').get('records')))
   directory=obj(oid+'_swh_zenodo_snapshot_head_release_directory');check('SWH directory endpoint '+oid+' '+slug,'directory_entry_count' in directory)
  z=rows(m/'zenodo-family-statistics.csv');check('canonical family identities '+slug,{x['object_id']:x['software_family'] for x in z if x['object_id']!='COMPANION'}==expected)
  if 'midnight' in slug:
   check('missing Zenodo not zero',s['zenodo_fixed_ten'] is None and s['zenodo_delta'] is None)
  else:
   fields=('views','downloads','unique_views','unique_downloads','version_views','version_downloads','version_unique_views','version_unique_downloads')
   for x in z:
    k=x['object_id']+'_zenodo' if x['object_id']!='COMPANION' else 'companion_zenodo';v=obj(k)
    for f in fields:check('Zenodo '+x['object_id']+' '+f,int(x[f])==v['stats'][f])
   for f in fields:check('Zenodo fixed sum '+f,sum(int(x[f]) for x in z if x['object_id']!='COMPANION')==s['zenodo_fixed_ten'][f])
   versions=rows(m/'zenodo-version-statistics.csv');check('33 version records',len(versions)==33 and all(x['doi'] and x['http_status']=='200' for x in versions))
   d=rows(m/'openalex-doi-resolution.csv');check('forty DOI routes ten Works',len(d)==40 and len({x['work_id'] for x in d})==10 and sum(x['doi_exact_match']=='True' for x in d)==10)
   for x in d:
    w=obj(x['object_id']+'_openalex_doi_'+x['version']);check('OpenAlex route '+x['requested_doi'],w.get('id')==x['work_id'] and (w.get('doi') or '').removeprefix('https://doi.org/').lower()==x['returned_doi'])
   for oid in expected:check('family convergence '+oid,len({x['work_id'] for x in d if x['object_id']==oid})==1)
   check('no synthetic midnight delta',s['zenodo_delta'] is None and s['zenodo_last_complete_reference']['delta_to_current']['views']==47)
 for base in (ROOT/'monitoring/2026-10-14',ROOT/'evidence/2026-10-14'):
  for p in base.rglob('*.md'):
   for link in re.findall(r'\]\(([^)\n]+)\)',p.read_text(encoding='utf-8')):
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',link) or link.startswith('#'):continue
    check('relative link '+str(p.relative_to(ROOT))+' '+link,(p.parent/urllib.parse.unquote(link.split('#')[0])).exists())
 return {'mode':'local_offline','network_calls':0,'checks':len(checks),'failed':sum(not x['passed'] for x in checks),'results':checks}
if __name__=='__main__':
 result=verify()
 for slug in ('03-midnight-facility-recheck','04-morning-facility-recheck','05-noon-user-pages'):
  (ROOT/'evidence/2026-10-14'/slug/'offline-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='results'}))
 for c in result['results']:
  if not c['passed']:print('FAIL',c['check'])
 sys.exit(bool(result['failed']))
