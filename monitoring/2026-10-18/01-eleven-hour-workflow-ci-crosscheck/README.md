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

**Publicly listed/published and Work-in-progress are different fields**, not necessarily inconsistent. The fourth workflow was already identified on October 17: it is **not** an observed new creation on October 18. The Team Dashboard's **11-hour display counts were supplied later as flattened researcher-provided text**, retained separately below; the underlying selected Period and asset-type filter were **not verified** and the totals were not independently fetched from the Dashboard API.

## 3. bio.tools and OpenEBench

The [public bio.tools API](https://bio.tools/api/t/life-science-protein-file-audit) still exposes `biotoolsID=life-science-protein-file-audit`, corresponding to `life-science-ecosystem-lab/bio_tool`, with raw `validated=0` and `homepage_status=0` fields. No interpretation of these raw flags as absence, invalidity, certification, or non-functionality is justified.

The user-supplied bio.tools page includes an [OpenEBench link](https://openebench.bsc.es/tool/life-science-protein-file-audit). A public extract showed only the portal shell without tool-specific benchmark data. **OpenEBench benchmarking, ranking, monitoring scores, and quality badge states remain unverified**.

The source repository's `bio_tool/README.md` still describes the registry submission as a future candidate; its documentation drift relative to the publicly visible bio.tools ID is an **unresolved docs task**, not a new registration event today. No source-repository changes are made by this control-repository observation.

## 4. Evidence/provenance limits and classification

The [source attempt ledger](source-attempts.csv) contains **31 bounded source entries** with origin and outcome classification. It is a compact attribution ledger, **not** 31 contemporaneous sealed HTTP raw responses. A public repo cannot become an archive of restricted private LifeMonitor account data. Current failure/access states remain legal scientific results.

- **Authoritative independent evidence:** public GitHub merge commit, validation run, five job status results, source code and RO-Crate declarations, public WorkflowHub listing, public bio.tools fields.
- **Maintainer-provided observation:** private LifeMonitor dashboard `all_passing` / 1 Passed; user-provided WIP description and OpenEBench link.
- **Unknown/unsupported:** direct private LifeMonitor verification; automatic registry synchronization; independent benchmark score; selected Dashboard Period/type filter and live API counters; interpretation of bio.tools flags; current public raw HTTP byte archives.
- **Study phase:** no OSF frozen contract modifications, no schema, no schedule offsets, no new eligible timepoint, no prospective dataset cells, no new sample or layer.

[Machine-readable summary](record.json) · [Source/attempt ledger](source-attempts.csv) · [Previous October 17 diagnostic](../../2026-10-17/01-field-boundary-cross-platform-recheck/README.md).


## 5. Researcher-supplied 11-hour Zenodo public listing: preserve concatenated field boundaries

The user's 2026-10-18 11-hour flattened Zenodo listing repeats the October 14 software release titles and places two adjacent **labelled fields** in one token. For example `1895` means **189 page Views + 5 page Downloads**, **not** 1,895 views. Each fixed RS ID was joined by the exact Zenodo record URL to the previous [October 17 user-page extract](../../2026-10-17/01-field-boundary-cross-platform-recheck/zenodo-page-field-extract.csv).

| Fixed ten | 2026-10-17 page | 2026-10-18 researcher page | Display difference |
| --- | ---: | ---: | ---: |
| All-version unique Views (summed by ten distinct families) | 1,511 | **1,533** | **+22** |
| All-version unique Downloads | 16 | **16** | **0** |

The per-family [machine-readable page table](zenodo-user-page-counters.csv) includes the **original concatenated token**, the separated fields, the DOI family identity, the prior source, and the exact ambiguity boundary. Neither page provided a reliable exact capture minute, and the October 18 values are **researcher-supplied**, not independently retained HTTP responses. The control repository's usage counters were **not provided**; it is not silently added to these fixed-ten figures.

Zenodo's default public record page displays hourly-window-deduplicated, all-version aggregate counts; the sum across ten distinct DOI families is **not a globally deduplicated count of individual people**.

## 6. WorkflowHub Team Dashboard: four asset display values, unknown filter

Four public workflow identities in project 490 are enumerated above, but **asset activity counters in this section come from the researcher's 11-hour Team Dashboard transcription**, not from independent API metrics:

| Asset | Dashboard most-viewed display | Dashboard most-downloaded display |
| --- | ---: | ---: |
| [2334](https://workflowhub.eu/workflows/2334) — NEXUS zero-entropy-lab | 1,365 | 106 |
| [2332](https://workflowhub.eu/workflows/2332) — NEXUS welcome-to-github | 1,247 | 138 |
| [2337](https://workflowhub.eu/workflows/2337) — Brain Evolution | 414 | 17 |
| [2347](https://workflowhub.eu/workflows/2347) — Life Science Knowledge Workflow | 71 | 15 |
| **Four-asset arithmetic sum** | **3,097** | **276** |

The older three assets sum to **3,026 shown views / 261 shown downloads**, corresponding to display differences of **+515 / +57** relative to the separate October 16 user-supplied dashboard record (**2,511 / 204**). These are *display-value differences*, **not a confirmed same-window growth series**, because the selected Dashboard Period and asset Type were not preserved in either supplied extract. The `Most active submitters` figure **5** is also user-supplied; it is a separate submission count, not part of the view/download totals. Complete source attribution and absent filter state are in [workflowhub-dashboard-user-counters.csv](workflowhub-dashboard-user-counters.csv).

## 7. DataCite Commons 72 DOI Works versus OpenAlex 29 author Works

**Correction to the attribution of “72 Works”:** the user's additional evidence unambiguously identifies this label as **DataCite Commons** ORCID-related **DOI Works search**, **not** OpenAlex author Works. This distinction was independently checked with the **DataCite public REST API**, using the exact ORCID query with both common identifier formats:

`creators_and_contributors.nameIdentifiers.nameIdentifier:(0009-0001-3617-0832 OR "https://orcid.org/0009-0001-3617-0832")`

API `meta.total=72`; four `page[size]=0` requests verify **Software 53 + Workflow 18 + StudyRegistration 1 = 72** using `types.resourceTypeGeneral` filters. The user's Commons facet also shows repository distribution **Zenodo 53 + WorkflowHub 18 + Open Science Framework 1**, all listed publication year **2026**. These repository facets are **attributed to the user-supplied Commons page**, not separately verified via the same REST filter syntax.

A more restrictive, **different** DataCite API query using only the short bare ORCID format returns `meta.total=53`. This **does not mean 19 DOI Works disappeared**: the identifiers or matching query changed. The precise reason for each difference is **not resolved by the aggregate responses alone**. Exact query strings, source URLs, and count fields are retained in [datacite-orcid-works-query-results.csv](datacite-orcid-works-query-results.csv). The review did **not enumerate all 72 individual DOI records**.

[OpenAlex author A5151904252](https://openalex.org/authors/A5151904252) and its separately queried author-filtered Works API currently expose **29 Works and 1 citation**. The researcher's supplied list contains [29 distinct OpenAlex Work IDs](openalex-user-visible-work-identities.csv): **17** WorkflowHub version-associated Works, **10** fixed-sample Zenodo Works, **1** control-software Zenodo Work and **1** OSF registration Work. These are **not** the same counted unit as the 72 DataCite DOI search results. A record can be a separate DOI/version while representing the same evolving software or workflow family. Neither count expands the ten preregistered objects or establishes 72 independent scientific publications.

The former “72 is unverified OpenAlex count” provisional interpretation is superseded by the **DataCite query reproduction in this same unmerged branch**. No already-published historical observation was modified.
