#!/usr/bin/env python3
"""Validate the retained October 9 package locally, without external calls."""
from pathlib import Path
import csv, datetime as dt, hashlib, json, tarfile

ROOT=Path(__file__).resolve().parents[1]
M=ROOT/'monitoring/2026-10-09/01-facility-recheck'
E=ROOT/'evidence/2026-10-09/01-facility-recheck'

def verify():
    checks=[]
    def check(label,value):
        checks.append({'check':label,'passed':bool(value)})
    summary=json.loads((M/'capture-summary.json').read_text(encoding='utf-8'))
    manifest=json.loads((E/'capture-manifest.json').read_text(encoding='utf-8'))['responses']
    raw={}; selected={}
    with tarfile.open(E/'raw-responses.tar.gz','r:gz') as tar:
        members={x.name:x for x in tar.getmembers()}
        expected={x['archive_member'] for x in manifest if x.get('archive_member')}
        check('archive exact member set',set(members)==expected)
        for x in manifest:
            check('request timestamp '+x.get('key',x.get('repository','')),dt.datetime.fromisoformat(x['started_at_utc'])<=dt.datetime.fromisoformat(x['finished_at_utc']))
            if not x.get('archive_member'):continue
            b=tar.extractfile(members[x['archive_member']]).read()
            check('raw digest '+x['archive_member'],hashlib.sha256(b).hexdigest()==x['sha256'])
            check('raw bytes '+x['archive_member'],len(b)==x['bytes'])
            if x.get('http_status')==200:
                try:obj=json.loads(b)
                except (ValueError,UnicodeError):continue
                raw[x['archive_member']]=obj
                if x['capture_group']=='facility':selected[x.get('retry_of',x['key'])]=obj
    corpus=list(csv.DictReader((ROOT/'corpus/object-manifest.csv').open(encoding='utf-8')))
    rows=list(csv.DictReader((M/'zenodo-statistics.csv').open(encoding='utf-8')))
    check('fixed ten canonical identities',[(x['object_id'],x['repository']) for x in rows[:10]]==[(x['object_id'],x['software_family']) for x in corpus])
    check('audit runtime remains supplementary',len(rows)==11 and rows[-1]['object_id']=='' and rows[-1]['corpus_role']=='audit_runtime_supplement')
    metrics=('views','unique_views','downloads','unique_downloads','version_views','version_unique_views','version_downloads','version_unique_downloads')
    for x in rows:
        obj=raw[x['raw_archive_member']]
        check('Zenodo DOI identity '+x['repository'],obj['doi']==x['version_doi'] and obj['conceptdoi']==x['concept_doi'] and str(obj['id'])==x['record_id'])
        for key in metrics:check('raw counter '+x['repository']+' '+key,int(x[key])==obj['stats'][key])
    for key in metrics:
        check('fixed total '+key,sum(int(x[key]) for x in rows[:10])==summary['zenodo_fixed_ten'][key])
        check('supplement-inclusive total '+key,sum(int(x[key]) for x in rows)==summary['zenodo_all_eleven_separate_context'][key])
    early=json.loads((E/'page-counter-source.json').read_text(encoding='utf-8'))
    for x in early['rows']:
        obj=raw['page-counter/'+x['repository']+'.json']
        check('earlier page unique pair '+x['repository'],x['page_views']==obj['stats']['unique_views'] and x['page_download_digit']==obj['stats']['unique_downloads'])
    dc=list(csv.DictReader((M/'datacite-identifiers.csv').open(encoding='utf-8')))
    check('forty DOI rows',len(dc)==40)
    for x in dc:
        obj=selected[x['object_id']+'_datacite_'+x['version']]['data']['attributes']
        check('DataCite '+x['expected_doi'],obj['doi'].lower()==x['expected_doi'].lower() and obj['state']==x['state'] and obj['types']['resourceTypeGeneral']==x['type'] and x['matched']==str(obj['state']=='findable' and obj['doi'].lower()==x['expected_doi'].lower()))
    groups=selected.get('orcid',{}).get('group',[])
    check('ORCID groups',len(groups)==summary['orcid']['group_count'])
    check('ORCID source summaries',sum(len(g.get('work-summary',[])) for g in groups)==summary['orcid']['summary_count'])
    oa=selected.get('openalex_author',{})
    check('OpenAlex query count',oa.get('meta',{}).get('count')==summary['openalex']['count'])
    check('OpenAlex returned count',len(oa.get('results',[]))==summary['openalex']['returned'])
    cells=list(csv.DictReader((M/'platform-states.csv').open(encoding='utf-8')))
    check('seventy unique operational cells',len(cells)==70 and len({(x['object_id'],x['platform']) for x in cells})==70)
    lookup={(x['object_id'],x['platform']):x['state'] for x in cells}
    for x in rows[:10]:
        key=x['object_id'];obj=selected.get(key+'_github',{})
        check('GitHub archived release '+key,obj.get('tag_name')=='v2026.10-open-research-production-framework' and lookup.get((key,'GitHub'))=='release_verified')
        ax=next((w for w in oa.get('results',[]) if w.get('doi','').lower()=='https://doi.org/'+x['version_doi'].lower()),{})
        check('OpenAlex exact version '+key,ax.get('type')=='software' and lookup.get((key,'OpenAlex'))=='software_version_observed')
        head=selected.get(key+'_swh_zenodo_snapshot_head_release',{})
        directory=selected.get(key+'_swh_zenodo_snapshot_head_release_directory')
        check('SWH directory chain '+key,head.get('target_type')=='directory' and isinstance(directory,list) and lookup.get((key,'SWH'))=='deposit_release_directory_verified')
        air=selected.get(key+'_openaire')
        check('OpenAIRE unresolved retains failed request '+key,air is not None or (lookup.get((key,'OpenAIRE'))=='query_unresolved' and any(y.get('key')==key+'_openaire' and y.get('http_status')!=200 for y in manifest)))
    check('classification remains diagnostic',summary['record_class']=='diagnostic_monitoring' and summary['prospective_dataset_member'] is False and summary['analytical_units']==60 and summary['possible_core_platform_checks']==70)
    artifacts=json.loads((E/'artifact-manifest.json').read_text(encoding='utf-8'))['artifacts']
    for x in artifacts:
        b=(ROOT/x['path']).read_bytes();check('artifact '+x['path'],hashlib.sha256(b).hexdigest()==x['sha256'] and len(b)==x['bytes'])
    return {'mode':'local_offline','network_calls':0,'checks':len(checks),'failed':sum(not x['passed'] for x in checks),'results':checks}

if __name__=='__main__':
    result=verify()
    (E/'offline-verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('mode','checks','failed','network_calls')}))
    raise SystemExit(bool(result['failed']))
