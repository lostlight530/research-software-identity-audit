#!/usr/bin/env python3
"""One-time public repository validation harness for a temporary pull-request branch.
This driver does not write to origin, alter the preregistered contract, or create research observations.
"""
import argparse, json, os, pathlib, subprocess, sys, time, hashlib
from datetime import datetime, timezone
def now(): return datetime.now(timezone.utc).isoformat()
p=argparse.ArgumentParser()
p.add_argument("--repo",required=True)
p.add_argument("--source",required=True)
p.add_argument("--expected-sha",required=True)
p.add_argument("--output",required=True)
a=p.parse_args()
root=pathlib.Path(a.source).resolve();out=pathlib.Path(a.output).resolve();out.mkdir(parents=True,exist_ok=True)
checks=[];started=now()
def run(label,command,cwd=None,timeout=1200):
    place=str(root/(cwd or ""))
    t=time.monotonic()
    x={"label":label,"command":command,"cwd":cwd or ".","started_at_utc":now(),"exit_code":None}
    try:
        with (out/(f"{len(checks):02d}-"+label.replace(" ","_")+".log")).open("w",encoding="utf-8",errors="replace") as f:
            q=subprocess.run(command,cwd=place,stdout=f,stderr=subprocess.STDOUT,
                             env={**os.environ,"PYTHONUNBUFFERED":"1","PYTHONIOENCODING":"utf-8"},
                             timeout=timeout,check=False)
        x["exit_code"]=q.returncode
        x["status"]="PASS" if q.returncode==0 else "FAIL"
    except subprocess.TimeoutExpired:
        x["status"]="TIMEOUT"
    except Exception as e:
        x["status"]="EXECUTION_ERROR"; x["error_class"]=type(e).__name__
    x["ended_at_utc"]=now();x["duration_seconds"]=round(time.monotonic()-t,3)
    checks.append(x)
    print("SELFTEST_STEP",json.dumps({k:x[k] for k in ["label","status","exit_code"]},ensure_ascii=False),flush=True)
    return x["status"]=="PASS"
git=subprocess.check_output(["git","rev-parse","HEAD"],cwd=root,text=True).strip()
pin_ok=git==a.expected_sha
checks.append({"label":"pinned_head_matches","status":"PASS" if pin_ok else "FAIL","expected":a.expected_sha,"observed":git,"started_at_utc":now(),"ended_at_utc":now()})
identity={}
required=["README.md","OPEN_RESEARCH.md","RESEARCH_TEMPLATE.md"]
for x in required:
    identity[x]=(root/x).is_file()
checks.append({"label":"research_identity_documents","status":"PASS" if all(identity.values()) else "FAIL","fields":identity,"started_at_utc":now(),"ended_at_utc":now()})
for x in ["codemeta.json",".zenodo.json"]:
    f=root/x
    if f.is_file():
        try:
            doc=json.loads(f.read_text(encoding="utf-8"))
            checks.append({"label":"parse_"+x,"status":"PASS" if isinstance(doc,dict) else "FAIL","started_at_utc":now(),"ended_at_utc":now()})
        except Exception as e:
            checks.append({"label":"parse_"+x,"status":"FAIL","error_class":type(e).__name__,"started_at_utc":now(),"ended_at_utc":now()})
python=sys.executable
name=a.repo
if name=="welcome-to-github":
    run("python_unittests",[python,"-m","unittest","discover","-s","tests","-p","test*.py","-v"])
    run("npm_ci",["npm","ci"],timeout=900)
    run("pages_build",["npm","run","build","--","--base=/welcome-to-github/"],timeout=900)
    # Equivalent public Pages companion asset stage from the repository workflow
    d=root/"dist/docs/archaeology/legacy_traces";d.mkdir(parents=True,exist_ok=True)
    mem=root/"docs/archaeology/legacy_traces/MEMORIAL.md"
    if mem.is_file():
        (d/"MEMORIAL.md").write_bytes(mem.read_bytes())
        checks.append({"label":"pages_memorial_asset_copy","status":"PASS","started_at_utc":now(),"ended_at_utc":now()})
    else:
        checks.append({"label":"pages_memorial_asset_copy","status":"FAIL","started_at_utc":now(),"ended_at_utc":now()})
    run("verify_pages_routes",["node","tools/verify-welcome-public-surface.mjs"],timeout=120)
elif name=="zero-entropy-lab":
    run("foundation_full_test_runner",[python,"tests/run_tests.py"],timeout=1800)
elif name=="Axiom-0":
    run("python_unittests",[python,"-m","unittest","discover","-s","tests","-v"])
    run("frontend_npm_ci",["npm","ci"],cwd="FRONTEND",timeout=900)
    run("frontend_lint",["npm","run","lint"],cwd="FRONTEND")
    run("frontend_build",["npm","run","build"],cwd="FRONTEND")
    run("frontend_snapshot",["node","--test","tests/final-snapshot.test.mjs"],cwd="FRONTEND")
elif name=="reflective-continuum":
    run("python_unittests",[python,"-m","unittest","discover","-s","tests","-v"])
elif name=="agent-foundations":
    run("foundation_validate",[python,"FOUNDATION/validate.py"])
    run("foundation_contract",[python,"-m","unittest","FOUNDATION.test_contract","-v"])
elif name in ["auto-doc-engine","epistemic-pipeline","sci-render-kit"]:
    # Python 3.13 observed pin file is an environment description, not a scientific lock.
    run("install_repo_python_deps",[python,"-m","pip","install","-r","requirements-python313.txt"],timeout=900)
    run("repo_make_test",["make","test"],timeout=1800)
    if name=="sci-render-kit":
        run("install_js_deps_nonlocked",["npm","install","--ignore-scripts","--no-audit","--no-fund"],timeout=900)
        run("observable_offline",["node","tests/test_observable_offline.js"])
elif name in ["china-agentic-observatory","agentic-frontier-observatory"]:
    # These research-ledger repositories do not publish a uniform machine test command.
    # The result is strictly STRUCTURAL_ONLY and never presented as scientific validation.
    for x in ["METHODOLOGY.md","SCOPE.md","TAXONOMY.md","SOURCE_REGISTRY.md","watchlist/ACTIVE.md","reports/daily","reports/weekly","reports/monthly"]:
        exists=(root/x).exists()
        checks.append({"label":"structural_"+x,"status":"PASS" if exists else "FAIL","started_at_utc":now(),"ended_at_utc":now()})
elif name=="research-software-identity-audit":
    for label,cmd in [
        ("contract_advisory",[python,"tools/check.py","--mode","advisory"]),
        ("contract_strict",[python,"tools/check.py","--mode","strict"]),
        ("all_unittests",[python,"-m","unittest","discover","-s","tests","-v"]),
        ("manifest_integrity",[python,"tools/check_public_artifact_manifest.py","--all"]),
        ("retained_evidence",[python,"tools/check_retained_all.py"]),
        ("zenodo_family_arithmetic",[python,"tools/check_zenodo_family_rollup.py"]),
        ("record_paths",[python,"tools/check_record_paths.py"]),
        ("repository_text_integrity",[python,"tools/check_repository_text_integrity.py"]),
    ]:run(label,cmd,timeout=1800)
else:raise ValueError(name)
fail=[x for x in checks if x["status"] not in ["PASS"]]
classify="STRUCTURAL_ONLY" if name in ["china-agentic-observatory","agentic-frontier-observatory"] else "REPO_RUNTIME_TESTS"
report={"record_class":"isolated_temporary_pr_selftest_not_prospective","repo":name,"expected_sha":a.expected_sha,"observed_sha":git,"started_at_utc":started,"ended_at_utc":now(),"check_class":classify,"steps":checks,"failed_steps":len(fail),"result":"PASS" if not fail else "FAIL","external_institution_interaction":"NONE","study_cells_added":0,"notes":["No remote GitHub write from source checkout","Status class STRUCTURAL_ONLY does not imply a runnable repo-native test suite","CLI failure is retained, not converted to a success"]}
(out/"result.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("SELFTEST_RESULT="+json.dumps({k:report[k] for k in ["repo","expected_sha","check_class","failed_steps","result"]},ensure_ascii=False))
sys.exit(0 if not fail else 1)
