"""Offline acceptance for the October 14 evening new-release package; no network."""
import collections,csv,datetime as dt,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];M=ROOT/'monitoring/2026-10-14/06-evening-facility-recheck';E=ROOT/'evidence/2026-10-14/06-evening-facility-recheck'
def verify():
 checks=[]
 def check(n,v):checks.append({'check':n,'passed':bool(v)})
 def rows(n):return list(csv.DictReader((M/n).open(encoding='utf-8-sig')))
 manifest=json.loads((E/'artifact-manifest.json').read_text(encoding='utf-8'))['artifacts']
 for x in manifest:
  b=(ROOT/x['path']).read_bytes();check('artifact '+x['path'],len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256'])
 check('exact artifact membership',{x['path'] for x in manifest}=={p.relative_to(ROOT).as_posix() for base in (M,E) for p in base.rglob('*') if p.is_file() and p.name not in ('artifact-manifest.json','offline-verification.json')})
 s=json.loads((M/'capture-summary.json').read_text(encoding='utf-8'));f=json.loads((E/'field-extracts.json').read_text(encoding='utf-8'));ledger=json.loads((E/'capture-manifest.json').read_text(encoding='utf-8'))['requests'];by={x['key']:x for x in ledger}
 for x in ledger:
  check('timestamp '+x['key'],dt.datetime.fromisoformat(x['started_at_utc'])<=dt.datetime.fromisoformat(x['finished_at_utc']))
  if x.get('retry_of') and x.get('http_status')==200:by[x['retry_of']]=x
 def obj(k):
  if '#record_id=' in k:
   key,rec=k.split('#record_id=');return next(x for x in obj(key)['hits']['hits'] if str(x['id'])==rec)
  x=by.get(k,{});return f.get(x.get('key'),{}) if x.get('http_status')==200 else {}
 fixed=list(csv.DictReader((ROOT/'corpus/object-manifest.csv').open(encoding='utf-8')));new=rows('new-release-statistics.csv')
 check('canonical ten new releases',{x['object_id']:x['software_family'] for x in new}=={x['object_id']:x['software_family'] for x in fixed})
 for x in new:
  key=x['object_id']+'_new_'+x['new_record_id'];z=obj(x['zenodo_source_request']);g=obj(x['object_id']+'_github_latest');a=obj(key+'_datacite')['data']['attributes']
  check('new release '+x['object_id'],g['tag_name']=='v2026.10-fourteen-day-evidence-checkpoint' and g['published_at']==x['github_published_at_utc'] and x['github_new_tag_observed']=='True')
  check('new DOI '+x['object_id'],z['doi']==x['new_version_doi'] and a['doi']==z['doi'] and a['state']=='findable')
  for field in ('views','downloads','unique_views','unique_downloads','version_views','version_downloads','version_unique_views','version_unique_downloads'):check('new counter '+x['object_id']+' '+field,int(x[field])==z['stats'][field])
  check('new version views and downloads zero '+x['object_id'],int(x['version_views'])==0 and int(x['version_downloads'])==0)
 check('new family totals',sum(int(x['views']) for x in new)==2215 and sum(int(x['unique_views']) for x in new)==1386)
 cells=rows('new-release-platform-states.csv');check('seventy new-version cells',len(cells)==70 and len({(x['object_id'],x['platform']) for x in cells})==70)
 for platform,state in [('GitHub','new_public_release_verified'),('Zenodo','new_version_family_verified'),('DataCite','new_version_findable'),('ORCID','new_version_source_assertion_observed'),('OpenAIRE','new_version_record_observed'),('OpenAlex','new_version_doi_query_not_found')]:check('new platform '+platform,sum(x['platform']==platform and x['state']==state for x in cells)==10)
 versions=rows('all-observed-version-statistics.csv');enum=rows('version-enumeration-verification.csv');ids=set()
 for x in enum:
  check('complete enumeration '+x['object_id'],x['http_status']=='200' and x['total']==x['returned'] and x['has_next_page']=='False');ids.update(x['record_ids'].split(' | '))
 check('43 distinct version IDs',len(versions)==43 and len(ids)==43 and {x['record_id'] for x in versions}==ids)
 for x in versions:
  z=obj(x['source_request_key']);check('version source '+x['record_id'],str(z['id'])==x['record_id'] and z['doi']==x['doi'])
  for field in ('version_views','version_downloads','version_unique_views','version_unique_downloads'):check('version stat '+x['record_id']+' '+field,int(x[field])==z['stats'][field])
 dc={}
 for k,x in by.items():
  if x['platform']=='DataCite':
   d=obj(k).get('data',{})
   if isinstance(d,dict) and d.get('attributes',{}).get('doi'):dc[d['attributes']['doi'].lower()]=d['attributes']['state']
 check('72 individual findable DOIs',len(dc)==72 and all(v=='findable' for v in dc.values()))
 groups=obj('orcid')['group'];summaries=[w for g in groups for w in g['work-summary']]
 check('15 groups 85 source summaries',len(groups)==15 and len(summaries)==85)
 sources=collections.Counter((w['source'].get('source-name') or {}).get('value','author/unnamed') for w in summaries);check('ORCID source split',dict(sources)=={'DataCite':62,'OpenAIRE':11,'author/unnamed':12})
 codes={w['put-code'] for w in summaries};dup=s['new_release']['orcid_duplicate_datacite_assertions'];check('duplicate source assertions retained',len(dup)==1 and set(dup[0]['put_codes']).issubset(codes) and dup[0]['summary_count']==2)
 check('three OpenAlex count surfaces 26',obj('openalex_primary_all_corpora')['meta']['count']==26 and obj('openalex_primary_profile')['works_count']==26 and obj('openalex_primary_selected_profile')['works_count']==26)
 correction=json.loads((E/'user-openalex-correction.json').read_text(encoding='utf-8'));check('copy omission user-corrected',correction['user_corrected_works_count']==26 and correction['interpretation'].startswith('copy omission'))
 page=rows('user-page-api-reconciliation.csv');check('11 user page pairs match API unique',len(page)==11 and all(x['page_matches_api_unique_pair']=='True' and x['page_unique_views']==x['api_unique_views'] and x['page_unique_downloads']==x['api_unique_downloads'] for x in page))
 check('diagnostic with observed releases, no invented T0',s['record_class']=='diagnostic_monitoring' and s['prospective_dataset_member'] is False and s['new_release']['release_event_observed'] is True and s['new_release']['prospective_schedule_declared'] is False)
 return {'mode':'local_offline','network_calls':0,'checks':len(checks),'failed':sum(not x['passed'] for x in checks),'results':checks}
if __name__=='__main__':
 r=verify();(E/'offline-verification.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in r.items() if k!='results'}));[print('FAIL',x['check']) for x in r['results'] if not x['passed']];sys.exit(bool(r['failed']))
