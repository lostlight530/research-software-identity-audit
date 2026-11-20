"""Offline synthetic fixture replay; not a collector or a schedule declaration."""
import csv
import json
import sys
import tempfile
from pathlib import Path
from collections import Counter
if not __debug__:
    raise SystemExit("Do not run this rehearsal with -O; assertions are required.")
repo = Path(__file__).resolve().parents[1]
import check as audit
with (repo/'corpus/object-manifest.csv').open() as stream:
    obj={r['object_id'] for r in csv.DictReader(stream)}
layers=set(audit.EXPECTED_PLATFORM_LAYERS.values())
pairs=audit.EXPECTED_PLATFORM_LAYERS
assert len(obj)==10 and len(layers)==6 and len(pairs)==7
with tempfile.TemporaryDirectory(prefix='rsia-fixture-no-network-') as scratch:
    root=Path(scratch); audit.ROOT=root
    raw=root/'observations/raw'; raw.mkdir(parents=True)
    schedule=root/'schedule'; schedule.mkdir()
    evidence=root/'evidence/mock-receipts'; evidence.mkdir(parents=True)
    rows=[]
    for o in sorted(obj):
        for p,l in sorted(pairs.items()):
            k=f'SYNTHETIC-{o}-{p}'
            ref=f'evidence/mock-receipts/{k}.txt'
            (root/ref).write_text('OFFLINE SYNTHETIC FIXTURE, NO EXTERNAL REQUEST\n')
            a=dict(observation_id=k,object_id=o,platform=p,infrastructure_layer=l,observation_timepoint='SYNTHETIC-POINT',dataset_phase='prospective',retrospective_reconstruction=False,release_event_timestamp='2099-01-02T00:00:00Z',retrieval_timestamp='2099-01-03T00:00:00Z',attempt_status='completed',observation_state='observed',evidence_refs=[ref])
            if (o,p)==('RS01','github'): a.update(attempt_status='failed',observation_state='rate_limited',failure_reason='synthetic 429')
            elif (o,p)==('RS02','openaire'): a.update(attempt_status='failed',observation_state='unresolved',failure_reason='synthetic timeout')
            elif (o,p)==('RS03','zenodo'): a.update(observation_state='partially_verified')
            (raw/(k+'.json')).write_text(json.dumps(a))
            rows.append(a)
    def tally(records):
        expected={(o,l) for o in obj for l in layers}
        keys=Counter((a['object_id'],a['platform']) for a in records)
        assert keys==Counter({(o,p):1 for o in obj for p in pairs}), 'missing or duplicate platform attempt'
        found={(a['object_id'],a['infrastructure_layer']) for a in records}
        assert found==expected and len(found)==60
        return len(found),len(records)
    def must_fail(f, phrase):
        try: f()
        except AssertionError as e: assert phrase in str(e),(phrase,str(e))
        else: raise AssertionError('expected refusal: '+phrase)
    must_fail(audit.check_observations,'active schedule declaration')
    decl=schedule/'synthetic.yaml'
    decl.write_text('status: active\nschedule_id: SYNTHETIC-ONLY\ndeclared_at: 2099-01-01T12:00:00Z\ntimepoints:\n  - id: SYNTHETIC-POINT\n    offset_or_rule: PT24H\n')
    audit.check_observations()
    assert tally(rows)==(60,70)
    must_fail(lambda:tally(rows[:-1]),'missing or duplicate')
    must_fail(lambda:tally(rows+[rows[0]]),'missing or duplicate')
    before=decl.read_text()
    decl.write_text(before.replace('2099-01-01','2099-01-04'))
    must_fail(audit.check_observations,'predates retrieval')
    decl.write_text(before)
    f=next(raw.glob('SYNTHETIC-RS01-github.json')); record=json.loads(f.read_text())
    record['observation_state']='fully_verified'; f.write_text(json.dumps(record))
    must_fail(audit.check_observations,'cannot itself be fully_verified')
    record['observation_state']='rate_limited'; f.write_text(json.dumps(record))
    (root/'observations/derived').mkdir()
    derived=dict(derivation_id='SYNTHETIC-NO-CONCLUSION',dataset_phase='prospective',derived_at='2099-01-03T01:00:00Z',derivation_method_ref='SYNTHETIC-ONLY',input_observation_refs=[str(f.relative_to(root))],result=None)
    (root/'observations/derived/no-conclusion.json').write_text(json.dumps(derived))
    audit.check_observations()
    summary=dict(semantic_preflight='PASS',analytical_cells=60,platform_attempts=70,state_counts=dict(Counter(r['observation_state'] for r in rows)),negative_cases=5,network_calls=0,prospective_cells_written=0,synthetic_material_retained_in_repo=False)
    print(json.dumps(summary,indent=2))
