"""Offline validation of imported identity evidence; no network calls."""
from pathlib import Path
import csv,json,hashlib,gzip,tarfile,io
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'evidence/2026-10-08-morning-recheck';M=ROOT/'monitoring/2026-10-08-morning-recheck'
checks=[]
def check(n,b):checks.append({'name':n,'passed':bool(b)})
s=json.loads((M/'retained-capture-summary.json').read_text(encoding='utf-8'))
m=json.loads((P/'response-manifest.json').read_text(encoding='utf-8'))
with tarfile.open(fileobj=io.BytesIO(gzip.decompress((P/'platform-responses.tar.gz').read_bytes())),mode='r') as t:
 raw={x.name:t.extractfile(x).read() for x in t if x.isfile()}
for x in m['responses']:
 check('capture-byte SHA256 '+x['archive_member'],hashlib.sha256(raw[x['archive_member']]).hexdigest()==x['sha256'])
 check('capture-byte size '+x['archive_member'],len(raw[x['archive_member']])==x['bytes'])
 check('timestamp order '+x['archive_member'],x['started_at_utc']<=x['finished_at_utc'])
rows=list(csv.DictReader((M/'zenodo-statistics.csv').open(encoding='utf-8')))
canonical={r['software_family']:r['object_id'] for r in csv.DictReader((ROOT/'corpus/object-manifest.csv').open(encoding='utf-8'))}
check('fixed ten distinct families',len(rows)==len({x['repository'] for x in rows})==10)
for r in rows:
 z=json.loads(raw[r['raw_archive_member']]);check('canonical repository join '+r['repository'],canonical[r['repository']]==r['object_id'])
 check('record and DOI identity '+r['repository'],str(z['id'])==r['record_id'] and z['doi']==r['version_doi'] and z['conceptdoi']==r['concept_doi'])
 for k in ('views','unique_views','downloads','unique_downloads','version_views','version_unique_views','version_downloads'):
  check('captured counter '+r['repository']+'/'+k,int(r[k])==z['stats'][k])
for k in ('views','unique_views','downloads','unique_downloads','version_views','version_unique_views','version_downloads'):
 check('aggregate counter '+k,sum(int(r[k]) for r in rows)==s['zenodo_totals'][k])
o=json.loads(raw['orcid.json']);groups=o['group'];summaries=[v for g in groups for v in g.get('work-summary',[])]
check('ORCID group structure',len(groups)==s['orcid']['group_count'])
check('ORCID source summary structure',len(summaries)==s['orcid']['summary_count'])
a=json.loads(raw['openalex_author.json']);check('OpenAlex list count',a['meta']['count']==len(a['results'])==s['openalex']['count'])
r=json.loads(raw['rsd_software.json']);check('RSD public records',len(r)==s['rsd_public_records'] and all(x['is_published'] for x in r))
check('preserved monitoring status',s['record_class']=='pre_eligibility_monitoring' and s['prospective_dataset_member'] is False)
manifest=P/'artifact-manifest.json'
if manifest.exists():
 for e in json.loads(manifest.read_text(encoding='utf-8'))['files']:
  f=ROOT/e['path'];check('public artifact digest '+e['path'],hashlib.sha256(f.read_bytes()).hexdigest()==e['sha256'])
result={'checks':len(checks),'failed':sum(not x['passed'] for x in checks),'scope':'Offline verification of retained source bytes, canonical joins, exact counters and public group/list reconstruction; no fresh platform observation','checks_detail':checks}
(P/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({k:result[k] for k in ('checks','failed')}))
if result['failed']:raise SystemExit(1)
