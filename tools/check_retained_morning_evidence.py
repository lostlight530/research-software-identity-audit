"""Offline validation of imported identity evidence; no network calls."""
from pathlib import Path
import csv,json,hashlib,gzip,tarfile,io
from collections import Counter
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'evidence/2026-10-08/01-morning-recheck';M=ROOT/'monitoring/2026-10-08/01-morning-recheck'
checks=[]
def check(n,b):checks.append({'name':n,'passed':bool(b)})
s=json.loads((M/'capture-summary.json').read_text(encoding='utf-8'))
m=json.loads((P/'capture-manifest.json').read_text(encoding='utf-8'))
with tarfile.open(fileobj=io.BytesIO(gzip.decompress((P/'raw-responses.tar.gz').read_bytes())),mode='r') as t:
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
check('aggregate Zenodo file bytes',sum(f['size'] for r in rows for f in json.loads(raw[r['raw_archive_member']]).get('files',[]))==s['zenodo_totals']['file_bytes'])
check('aggregate current-version unique downloads',sum(json.loads(raw[r['raw_archive_member']])['stats']['version_unique_downloads'] for r in rows)==s['zenodo_totals']['version_unique_downloads'])
o=json.loads(raw['orcid.json']);groups=o['group'];summaries=[v for g in groups for v in g.get('work-summary',[])]
check('ORCID group structure',len(groups)==s['orcid']['group_count'])
check('ORCID source summary structure',len(summaries)==s['orcid']['summary_count'])
# Group membership follows DOI identifiers, not titles or historical RS ordering.
def group_dois(group):
 return {v['external-id-value'].strip().lower().removeprefix('https://doi.org/') for item in [group,*group.get('work-summary',[])] for v in (item.get('external-ids') or {}).get('external-id',[]) if v.get('external-id-type','').lower()=='doi'}
concept_dois={r['concept_doi'].lower() for r in rows}
fixed_groups=[g for g in groups if group_dois(g)&concept_dois]
check('ORCID fixed-corpus group count',len(fixed_groups)==s['orcid']['fixed_corpus_groups'])
check('ORCID fixed-corpus family coverage',set().union(*(group_dois(g)&concept_dois for g in fixed_groups))==concept_dois)
check('ORCID fixed-corpus summary count',sum(len(g.get('work-summary',[])) for g in fixed_groups)==s['orcid']['fixed_corpus_summaries'])
source_counts=Counter()
for v in summaries:
 source=v.get('source') or {};name=(source.get('source-name') or {}).get('value')
 if not name:
  check('ORCID unnamed source is record owner '+str(v.get('put-code')), (source.get('source-orcid') or {}).get('path')=='0009-0001-3617-0832')
  name='author/unnamed'
 source_counts[name]+=1
check('ORCID source distribution',dict(source_counts)==s['orcid']['sources'])
a=json.loads(raw['openalex_author.json']);check('OpenAlex list count',a['meta']['count']==len(a['results'])==s['openalex']['count'])
check('OpenAlex returned count',len(a['results'])==s['openalex']['returned'])
check('OpenAlex type distribution',dict(Counter(w['type'] for w in a['results']))==s['openalex']['types'])
# Eight distinct primary topics across the retained works list; the profile has a different surface.
check('OpenAlex primary-topic set',sorted({w['primary_topic']['display_name'] for w in a['results'] if w.get('primary_topic')})==sorted(s['openalex']['topics']))
r=json.loads(raw['rsd_software.json']);check('RSD public records',len(r)==s['rsd_public_records'] and all(x['is_published'] for x in r))
check('preserved monitoring status',s['record_class']=='pre_eligibility_monitoring' and s['prospective_dataset_member'] is False)
manifest=P/'artifact-manifest.json'
if manifest.exists():
 for e in json.loads(manifest.read_text(encoding='utf-8'))['files']:
  f=ROOT/e['path'];check('public artifact digest '+e['path'],hashlib.sha256(f.read_bytes()).hexdigest()==e['sha256'])
result={'checks':len(checks),'failed':sum(not x['passed'] for x in checks),'scope':'Offline verification of retained source bytes, canonical joins, exact counters, file-size totals, ORCID source/fixed-corpus groups and OpenAlex type/primary-topic reconstruction; no fresh platform observation','checks_detail':checks}
(P/'offline-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({k:result[k] for k in ('checks','failed')}))
if result['failed']:raise SystemExit(1)
