# 2026-10-18 11:00-hour LifeMonitor, WorkflowHub and bio.tools cross-check

**Diagnostic monitoring only.** This record responds to the researcher's **October 18 Beijing 11 o'clock** supplied page extracts. The exact original page capture minute is **unknown**; a review-session local clock read was **2026-10-18T11:25:12+08:00**. Native GitHub action timestamps are event timestamps, **not** the screenshot/retrieval timestamps. No per-request HTTP response bytes, headers or server Date timestamps were collected.

The authoritative study remains [OSF Registration 5b329](https://osf.io/5b329/overview): exactly RS01–RS10, six preregistered layers and **60** object-layer units per eligible scheduled timepoint. The seven operational platforms remain GitHub, Zenodo, DataCite, ORCID, Software Heritage, OpenAIRE and OpenAlex. WorkflowHub, LifeMonitor, OpenEBench and bio.tools are **supplementary**, not additional preregistered units. The audit control repository is not RS11.

## 1. LifeMonitor: supplied private dashboard vs independent GitHub evidence

The maintainer's 11-hour page extract describes a **Private**, **CWL** workflow (version 1), origin **local file uploaded**, state **all_passing** and test instances **1 Passed, 0 Failed, 0 Error, 0 Waiting, 0 Running, 0 Aborted**. This is a **user-supplied private-surface observation**. It was **not independently read through an authenticated LifeMonitor API**: public extraction of the workflow page returned only a loading shell. The private workflow path and private workflow/test-instance IDs are **deliberately not republished** in this public repository; the underlying source repository's already-public status claims are separately referenced.

A *distinct, externally reproducible* GitHub result exists:
- [Life-science repository PR #26](https://github.com/lostlight530/life-science-ecosystem-lab/pull/26) merged **2026-10-18 03:11:25 UTC (11:11:25 Beijing)**, repairing the Workflow Testing RO-Crate `TestInstance` name, supported `GithubService` vocabulary and service fields. Its stated local `142 tests passed` remains a **PR author claim**, not independently rerun for this control-repo record.
- [GitHub Actions validate.yml run #39092740134](https://github.com/lostlight530/life-science-ecosystem-lab/actions/runs/39092740134), for exact source `main` commit [`d2a6ec6e943f0b8888e007053ddb0d3d9be47367`](https://github.com/lostlight530/life-science-ecosystem-lab/commit/d2a6ec6e943f0b8888e007053ddb0d3d9be47367), completed **2026-10-18 03:12:06 UTC (11:12:06 Beijing)** with `success`. A separate [jobs API](https://api.github.com/repos/lostlight530/life-science-ecosystem-lab/actions/runs/39092740134/jobs) reports **five successful jobs**: Repository contracts, Knowledge Workflow, Evidence Tool, Portable package and aggregate `validate`.
- [Public repository RO-Crate metadata](https://github.com/lostlight530/life-science-ecosystem-lab/blob/d2a6ec6e943f0b8888e007053ddb0d3d9be47367/ro-crate-metadata.json) names the GitHub test instance and supported service contract; the public [standards-status summary](https://github.com/lostlight530/life-science-ecosystem-lab/blob/d2a6ec6e943f0b8888e007053ddb0d3d9be47367/metadata/standards-status.json) separately attributes the private LifeMonitor state to a maintainer-observed local upload.

**Interpretation boundary:** the passing external monitor display and five successful GitHub jobs are *different evidence streams*. The private view cannot be externally replayed from its page shell. Neither proves automatic WorkflowHub–LifeMonitor synchronization, continuous monitoring, successful scheduled production runs, biological inference or scientific validity. A source file named `evidence/field-tests/2026-10-17/lifemonitor-inspection.json` is a **static software inspection** (PASS 1/WARN 3/FAIL 0), **not** the LifeMonitor Test Instance result and must never be compared as if it were the same test.

## 2. WorkflowHub: four public workflow identities

The [project 490 public workflow index](https://workflowhub.eu/projects/490/workflows) still lists **four** workflow entries:

| ID | Public identity | Latest version DOI |
|---|---|---|
| [2347](https://workflowhub.eu/workflows/2347) | Life Science Knowledge Workflow; UI version 0.4.0; user-supplied status Work-in-progress | [10.48546/workflowhub.workflow.2347.1](https://doi.org/10.48546/workflowhub.workflow.2347.1) |
| [2332](https://workflowhub.eu/workflows/2332) | NEXUS CORTEX Life Cycle — welcome-to-github | [10.48546/workflowhub.workflow.2332.8](https://doi.org/10.48546/workflowhub.workflow.2332.8) |
| [2334](https://workflowhub.eu/workflows/2334) | NEXUS CORTEX Life Cycle — zero-entropy-lab | [10.48546/workflowhub.workflow.2334.8](https://doi.org/10.48546/workflowhub.workflow.2334.8) |
| [2337](https://workflowhub.eu/workflows/2337) | Brain Evolution — welcome-to-github (distinct historical precursor) | [10.48546/workflowhub.workflow.2337.1](https://doi.org/10.48546/workflowhub.workflow.2337.1) |

**Publicly listed/published and Work-in-progress are different fields**, not necessarily inconsistent. The fourth workflow was already identified on October 17: it is **not** an observed new creation on October 18. The Team Dashboard's current view/download counts were **not** captured here; never backfill them from the previous October 16 extract.

## 3. bio.tools and OpenEBench

The [public bio.tools API](https://bio.tools/api/t/life-science-protein-file-audit) still exposes `biotoolsID=life-science-protein-file-audit`, corresponding to `life-science-ecosystem-lab/bio_tool`, with raw `validated=0` and `homepage_status=0` fields. No interpretation of these raw flags as absence, invalidity, certification, or non-functionality is justified.

The user-supplied bio.tools page includes an [OpenEBench link](https://openebench.bsc.es/tool/life-science-protein-file-audit). A public extract showed only the portal shell without tool-specific benchmark data. **OpenEBench benchmarking, ranking, monitoring scores, and quality badge states remain unverified**.

The source repository's `bio_tool/README.md` still describes the registry submission as a future candidate; its documentation drift relative to the publicly visible bio.tools ID is an **unresolved docs task**, not a new registration event today. No source-repository changes are made by this control-repository observation.

## 4. Evidence/provenance limits and classification

The [source attempt ledger](source-attempts.csv) contains **11 bounded source entries** with origin and outcome classification. It is a compact attribution ledger, **not** 11 contemporaneous sealed HTTP raw responses. A public repo cannot become an archive of restricted private LifeMonitor account data. Current failure/access states remain legal scientific results.

- **Authoritative independent evidence:** public GitHub merge commit, validation run, five job status results, source code and RO-Crate declarations, public WorkflowHub listing, public bio.tools fields.
- **Maintainer-provided observation:** private LifeMonitor dashboard `all_passing` / 1 Passed; user-provided WIP description and OpenEBench link.
- **Unknown/unsupported:** direct private LifeMonitor verification; automatic registry synchronization; independent benchmark score; updated Dashboard counters; interpretation of bio.tools flags; current public raw HTTP byte archives.
- **Study phase:** no OSF frozen contract modifications, no schema, no schedule offsets, no new eligible timepoint, no prospective dataset cells, no new sample or layer.

[Machine-readable summary](record.json) · [Source/attempt ledger](source-attempts.csv) · [Previous October 17 diagnostic](../2026-10-17/01-field-boundary-cross-platform-recheck/README.md).
