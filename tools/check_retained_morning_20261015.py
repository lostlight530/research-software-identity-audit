"""Offline source-aware verification for the October 15 morning package; no network."""
import collections,csv,datetime as dt,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];M=ROOT/'monitoring/2026-10-15/01-morning-facility-recheck';E=ROOT/'evidence/2026-10-15/01-morning-facility-recheck'
def verify():
 c=[]
 def check(n,v):c.append({'check':n,'passed':bool(v)})
 def rows(name):return list(csv.DictReader((M/name).open(encoding='utf-8-sig')))
 a=json.loads((E/'artifact-manifest.json').read_text(encoding='utf-8'))['artifacts']
 check('exact artifact inventory',{x['path'] for x in a}=={p.relative_to(ROOT).as_posix() for base in (M,E) for p in base.rglob('*') if p.is_file() and p.name not in ('artifact-manifest.json','offline-verification.json')})
 for x in a:
  b=(ROOT/x['path']).read_bytes();check('hash '+x['path'],len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256'])
 ledger=json.loads((E/'capture-manifest.json').read_text(encoding='utf-8'))['requests'];fields=json.loads((E/'field-extracts.json').read_text(encoding='utf-8'));s=json.loads((M/'capture-summary.json').read_text(encoding='utf-8'));by={x['key']:x for x in ledger}
 for x in ledger:
  check('timestamp '+x['key'],dt.datetime.fromisoformat(x['started_at_utc'])<=dt.datetime.fromisoformat(x['finished_at_utc']))
  if x.get('retry_of') and x.get('http_status')==200:by[x['retry_of']]=x
 def obj(k):
  if '#record_id=' in k:
   key,rec=k.split('#record_id=');return next(z for z in obj(key)['hits']['hits'] if str(z['id'])==rec)
  x=by.get(k,{});return fields.get(x.get('key'),{}) if x.get('http_status')==200 else {}
 check('299 retained attempts',len(ledger)==s['requests']==299)
 z=rows('zenodo-family-statistics.csv');fixed=list(csv.DictReader((ROOT/'corpus/object-manifest.csv').open(encoding='utf-8')))
 check('canonical fixed ten and supplement',[(x['object_id'],x['software_family']) for x in z[:10]]==[(x['object_id'],x['software_family']) for x in fixed] and z[-1]['object_id']=='COMPANION')
 metrics=('views','downloads','unique_views','unique_downloads','version_views','version_downloads','version_unique_views','version_unique_downloads')
 for x in z:
  v=obj(x['source_request_key']);check('version identity '+x['object_id'],v['doi']==x['doi'] and v['conceptdoi']==x['concept_doi'])
  for k in metrics:check('family counter '+x['object_id']+' '+k,int(x[k])==v['stats'][k])
 for k in metrics:check('fixed sum '+k,sum(int(x[k]) for x in z[:10])==s['zenodo_fixed_ten'][k])
 check('1400 family unique sum 2231 total',s['zenodo_fixed_ten']['unique_views']==1400 and s['zenodo_fixed_ten']['views']==2231)
 versions=rows('zenodo-version-statistics.csv');enum=rows('version-enumerations.csv');ids=set()
 for x in enum:
  check('complete enumeration '+x['object_id'],x['total']==x['returned'] and x['has_next']=='False');ids.update(x['record_ids'].split(' | '))
 check('43 unique version records',len(versions)==43 and len(ids)==43 and {x['record_id'] for x in versions}==ids)
 for x in versions:
  v=obj(x['source_request_key']);check('version source '+x['record_id'],str(v['id'])==x['record_id'] and v['doi']==x['doi'])
  for k in metrics:check('version field '+x['record_id']+' '+k,int(x[k])==v['stats'][k])
 dc=rows('datacite-identifiers.csv');check('72 findable',len(dc)==72 and all(x['state']=='findable' for x in dc))
 for x in dc:check('DOI '+x['doi'],obj(x['request_key'])['data']['attributes']['doi'].lower()==x['doi'])
 groups=obj('orcid')['group'];ss=[w for g in groups for w in g['work-summary']];check('ORCID 15 groups 84 sources',len(groups)==15 and len(ss)==84)
 codes={w['put-code'] for w in ss};check('duplicate removed other survives',229954516 not in codes and 229954515 in codes)
 check('ORCID source counts',dict(collections.Counter((w['source'].get('source-name') or {}).get('value','author/unnamed') for w in ss))=={'DataCite':61,'OpenAIRE':11,'author/unnamed':12})
 works=obj('openalex_primary_all_corpora');check('27 queried Works and profile 26',works['meta']['count']==27 and len(works['results'])==27 and obj('openalex_primary_profile')['works_count']==26 and obj('openalex_primary_selected_profile')['works_count']==26)
 check('two newly returned v7 works',{x['doi'].rsplit('/',1)[-1] for x in s['openalex']['added_works']}=={'workflowhub.workflow.2334.7','workflowhub.workflow.2332.7'})
 check('audit DOI routes converge',obj('openalex_companion_latest_doi')['id']==obj('openalex_companion_concept_doi')['id']=='https://openalex.org/W7220365356' and by['openalex_prior_control_work']['http_status']==404)
 cells=rows('platform-states.csv');check('70 distinct current checkpoint cells',len(cells)==70 and len({(x['object_id'],x['platform']) for x in cells})==70)
 for platform,state in [('GitHub','checkpoint_release_verified'),('Zenodo','checkpoint_version_family_verified'),('DataCite','checkpoint_version_findable'),('ORCID','checkpoint_version_assertion_observed'),('OpenAIRE','checkpoint_exact_record_observed'),('OpenAlex','checkpoint_doi_not_found')]:check('current platform '+platform,sum(x['platform']==platform and x['state']==state for x in cells)==10)
 sh=rows('swh-identity-checks.csv');check('only Axiom checkpoint commit verified',[x['object_id'] for x in sh if x['commit_directory_verified']=='True']==['RS03'])
 row=next(x for x in sh if x['object_id']=='RS03');rev=obj('RS03_swh_tag_revision');directory=obj('RS03_swh_tag_directory');check('exact commit archive directory',rev['id']==row['github_tag_commit']==row['revision_id'] and 'directory_entry_count' in directory and rev.get('directory'))
 for w in s['workflowhub']:
  v=obj('workflowhub_'+w['id']);page=obj('workflowhub_'+w['id']+'_latest_html');check('workflow latest and activity '+w['id'],v['data']['attributes']['latest_version']==w['latest_version'] and page['activity']=={'views':w['views'],'downloads':w['downloads']})
 check('no new page, no schedule promotion',s['user_page_provided_this_round'] is False and s['prospective_dataset_member'] is False and s['new_governance_schedule_declared'] is False)
 return {'mode':'local_offline','network_calls':0,'checks':len(c),'failed':sum(not x['passed'] for x in c),'results':c}
if __name__=='__main__':
 r=verify();(E/'offline-verification.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in r.items() if k!='results'}));[print('FAIL',x['check']) for x in r['results'] if not x['passed']];sys.exit(bool(r['failed']))
