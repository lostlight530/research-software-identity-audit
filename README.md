# research-software-identity-audit

[![DOI](https://zenodo.org/badge/1405944227.svg)](https://doi.org/10.5281/zenodo.23166490)

> Shared research-control, evidence, provenance, and reproducibility infrastructure for two independent OSF-registered prospective longitudinal observational studies.

This repository is the shared operational, evidence, provenance, and reproducibility workspace for two separately governed OSF studies. Their registrations, research objects, observation contracts, evidence streams, and denominators remain independent.

- **Study 1 — Research software identity propagation:** OSF registration [5b329](https://osf.io/5b329/), with the fixed corpus RS01–RS10 and its six-layer / 60 object-layer-unit contract
- **Study 2 — Open research workflow identity:** OSF public project [AUHJF](https://osf.io/auhjf/) and separate registration [VSHWK](https://osf.io/vshwk/), with the amended WorkflowHub Project 490 case and paired lineages 2332 v9 / 2334 v9

The studies share this CONTROL repository only as a governance and evidence-custody location. Shared repository ownership does not merge their scientific objects, sample frames, observation records, or denominators.

> **Important:** This repository is not RS11, not a third WorkflowHub lineage, and not an additional research sample in either study.

## Start here — documentation and repository navigation

This is the architecture entrypoint for the shared CONTROL repository. The [documentation map](docs/README.md) owns directory responsibilities, evidence classes, and docs-only maintenance rules; each approved OSF registration and revision remains the authority for its respective scientific protocol.

| Scope | Current operational entrypoints | Ownership boundary |
| --- | --- | --- |
| **Shared CONTROL infrastructure** | [Directory and ownership map](docs/README.md#2-directory-map-where-to-read-and-where-a-future-contribution-belongs) · [tools](tools/README.md) · [tests](tests/) | Shared governance, validation and evidence custody do not merge either study's scientific objects or denominators |
| **Study 1 · 5b329 / wa5v8** | [Study entry](studies/osf-wa5v8/README.md) · [Day 0](studies/osf-wa5v8/day0/README.md) · [Day 1](studies/osf-wa5v8/day1/README.md) · [Day 2](studies/osf-wa5v8/day2/README.md) | Its canonical contract, fixed corpus, schema and schedule remain at established root paths; historical baseline, monitoring and evidence are retained there |
| **Study 2 · VSHWK** | [Study entry](studies/osf-vshwk/README.md) · [Day 0](studies/osf-vshwk/day0/README.md) · [Day 1](studies/osf-vshwk/day1/README.md) · [Day 2](studies/osf-vshwk/day2/README.md) | Project 490 / paired lineages own a separate contract, cycle ledger and daily indexes under `studies/osf-vshwk/` |

**Physical ownership rule:** Study 1's frozen `baseline/` remains at its canonical root path. The former root-level diagnostic and evidence archives are consolidated under `history/diagnostics/` and `history/evidence/`; historical repository reviews and pinned inventories live under `history/documentation/` and `history/repository-inventory/`. Current operational work is indexed under `studies/`, while `tools/`, `tests/` and `.github/` remain shared CONTROL engineering. `history/` is not an active acquisition surface.

### Find the right file by task

| Task | Start with |
| --- | --- |
| Read what was registered | [OSF study registration](https://osf.io/5b329/overview) and [repository contract mapping](contract/preregistration.md) |
| Check fixed samples and counting rules | [RS01–RS10 manifest](corpus/object-manifest.csv) and [six-layer counting contract](schema/counting-rules.md) |
| Understand historical versus prospective status | [Initial baseline](baseline/README.md), [operational schedule](schedule/README.md), [prospective raw observation area](observations/raw/README.md) |
| Review the separate OSF workflow study | [Two-study index](studies/README.md), [Study 2 current contract and cycle ledger](studies/osf-vshwk/README.md) |
| Review wa5v8 daily operational materials | [wa5v8 runtime](studies/osf-wa5v8/README.md) |
| Review historical diagnostic measurements and retained evidence | [Dated monitoring index](history/diagnostics/README.md), [evidence inventory](history/evidence/README.md), [provenance discipline](provenance/README.md) |
| Reproduce or review a contribution | [Tools and advisory checks](tools/README.md), [contributing instructions](CONTRIBUTING.md), [open research method](OPEN_RESEARCH.md) |
| Cite the correct scholarly object | [Citation and identifier guide](scholarly/CITATION.md), [release policy](RELEASE_POLICY.md) |

**Historical operational-status note (as-of 2026-10-17):** At that dated review, the [local schedule record](schedule/README.md) had no declared numerical offsets. The October 14 fixed-ten public release cohort was recorded separately, and diagnostic monitoring packages were not eligible for retrospective promotion into the prospective dataset. This dated note is not a statement that Study 1 lacks a formal OSF prospective registration. The current approved 2026-11-18 OSF authority is documented in the following section. The registered event eligibility and follow-up rules remain in force; numerical offsets must not be invented or backdated.


---

## Current OSF authority — 2026-11-24

Both studies have formal OSF preregistrations and approved current schema-response revisions. “Prospective” describes their registered research designs; it does not mean every future observation cycle has already occurred or every external provider must respond successfully.

| Study | OSF registration | Current approved schema response | Current registered frame |
| --- | --- | --- | --- |
| **Study 1 — RSIA identity propagation** | [5b329](https://osf.io/5b329/) | [6afdcc3a7fb0a89b0e3dd7e4](https://api.osf.io/v2/schema_responses/6afdcc3a7fb0a89b0e3dd7e4/) · submitted 2026-11-18 · approved | RS01–RS10; six analytical layers; seven operational platforms; 60 object-layer units per scheduled timepoint; RSIA is supporting research-control/history/evidence/provenance infrastructure, not a sample object |
| **Study 2 — Open research workflow** | [VSHWK](https://osf.io/vshwk/) | [6afdcc7108de91a0f0cefd6c](https://api.osf.io/v2/schema_responses/6afdcc7108de91a0f0cefd6c/) · submitted 2026-11-18 · approved | One WorkflowHub Project 490 case; paired lineages 2332 v9 and 2334 v9; eight layers; event- or documented-review-initiated cycles without a fixed calendar interval, wave count, or end date |

### Current authority details

- **5b329:** the 2026-11-18 approved response updates registered fields 344-47 and 344-86. It explicitly leaves the five research questions, fixed corpus, six layers, seven-platform scope, 60-unit denominator, observation schedule, variables, analyses, missing-data handling, and non-causal interpretation unchanged. See the [current approved-revision crosswalk](studies/osf-wa5v8/day1/contract/osf-approved-revision-2026-11-18.md).
- **VSHWK:** the 2026-11-18 approved response makes Project 490 with lineages 2332 v9 / 2334 v9 the current case and replaces the former fixed three-wave design with repeated event- or documented-review-initiated cycles. WorkflowHub 2347 v2 remains historical context.
- **VSHWK registration-page metadata:** OSF API date_modified is 2026-11-24T12:00:17.626133Z (2026-11-24 20:00:17.626 Asia/Shanghai). Its Description names Project 490 and both current lineages but still contains the phrase “three prospective observation waves”; the approved Schema Response, not that descriptive metadata sentence, governs the protocol.
- **AUHJF:** this separate public OSF project is an entry point only and holds no data/files. Its project-level Description retains the 2347 v2 / three-wave wording and is not the VSHWK protocol authority.

**Status rule:** both formal prospective research contracts are in force. Diagnostic monitoring, pre-eligibility checks, and eligible prospective observation records remain distinct evidence classes. Study 1 must not be described as “diagnostic-only” merely because a particular record is classified as monitoring; monitoring records must also not be silently promoted into its prospective dataset.

**Dated inventories and diagnostics:** see the [historical repository inventory and review index](docs/README.md#historical-repository-inventory-and-review-index). Snapshot file/commit counts, provider outcomes, and retrospective reviews remain tied to their original source and observation windows; they are not current HEAD metrics or prospective study results.

## 数据层与阶段展示的证据关系 / Longitudinal research and stage-display evidence

**中文**：本研究的固定样本是 `RS01–RS10`，CONTROL 仓库不是 RS11；OSF 注册 DOI `10.17605/OSF.IO/5B329` 指向冻结的预注册研究合同，GitHub `main` 指向可演进的执行／治理软件，`baseline/` 是历史基线，`history/diagnostics/` 是诊断观测，`observations/` 才是适格的前瞻性观测归属面；不能把十个对象、六层计数、旧快照统计、页面聚合数或某次 API 读数混成统一分母，也不能将文档存在写成实际采集完成

**English**: The frozen corpus is RS01–RS10; CONTROL is not RS11. The OSF registration DOI identifies the frozen preregistration, live GitHub `main` owns evolving implementation/governance, `baseline/` retains historical baseline, `history/diagnostics/` holds diagnostics, and `observations/` is the eligible prospective observation surface. Never combine ten objects, six evidence layers, dated inventory counts, frontend aggregates, or single API observations into a shared denominator; a present file does not establish that eligible acquisition ran

**长期阶段显示 / Longitudinal stage display:** 展示条目应返回 corpus/object ID、infrastructure layer、observation eligibility、source URL、retrieval timestamp、exact Git revision、raw or derived provenance、verification state、missing/blocked reason，以及所引用归档 DOI 的 **concept/version/OSF registration** 类型；对长期趋势进行比较时，必须声明时间窗和统计口径；A display entry must preserve those identifiers and denominators rather than silently upgrading diagnostic evidence to prospective results

## Research registration

This section documents **Study 1 (OSF 5b329) only**. Study 2 has a separate registration and protocol namespace; see the [two-study index](studies/README.md) and [VSHWK current contract](studies/osf-vshwk/README.md).

**OSF Preregistration**

- Title: *Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures*
- Registration: https://osf.io/5b329/overview
- DOI: https://doi.org/10.17605/OSF.IO/5B329
- Associated OSF Project: https://osf.io/wa5v8
- Registered: October 5, 2026
- License of the OSF registration: CC BY 4.0

The OSF registration is the frozen research-plan object.

This GitHub repository is the live operational workspace used to implement, document, execute, and preserve the research process without silently rewriting the frozen registration.

The two objects therefore have different roles:

```text
OSF Registration
        │
        │ frozen research contract
        ▼
Operational specification
        │
        ▼
This repository
        │
        ├── corpus definitions
        ├── schemas
        ├── observation records
        ├── evidence
        ├── provenance
        ├── amendments
        └── reproducible analysis
```

---

# Research objective

Research software increasingly exists simultaneously across several infrastructures:

- source-code repositories
- archival repositories
- persistent-identifier registries
- author registries
- preservation archives
- scholarly discovery graphs

These systems do not necessarily represent the same object, operate on the same clock, expose the same metadata, or provide the same guarantees.

A software release may therefore exist in one infrastructure before it appears in another.

A record may be preserved but not yet discovered.

A DOI may resolve correctly while an author registry still contains incomplete or duplicated summaries.

A discovery graph may expose a record without guaranteeing its preservation or attribution.

A failed query may reflect rate limiting rather than absence.

This study observes those distinctions directly rather than collapsing them into a single global status.

---

# Research questions

The preregistered study asks five primary questions.

### RQ1 — Propagation

Across the prospective observation window, which scholarly-infrastructure layers register, propagate, preserve, aggregate, or discover each newly released research software object, and in what temporal order?

### RQ2 — Cross-layer consistency

Do identity and metadata states remain consistent across repository, identifier-registration, author-registry, archival, preservation, and discovery layers, or do measurable divergences emerge?

### RQ3 — Propagation latency

Where timestamps are directly observable and semantically comparable, how long does propagation from software release to downstream observation take across different infrastructure layers?

### RQ4 — Aggregation recurrence

Do previously observed aggregation behaviors recur, including family-level grouping and multiple source summaries associated with the same software family?

### RQ5 — Failure and correction

Which failures, partial states, rate limits, unresolved states, or correction events occur during the observation window, and at which infrastructure boundary does each observable state arise?

---

# Study design

The study uses a:

> **prospective longitudinal repeated-measures observational design**

No intervention is administered.

No research-software object, platform state, infrastructure behavior, release condition, or metadata state is experimentally manipulated.

No causal effect is estimated.

The study is descriptive and within-corpus rather than a population-level prevalence study.

---

# Fixed research corpus

The study corpus contains exactly:

> **10 predefined research software objects**

These objects were already included in the preceding historical audit.

The corpus is fixed for the preregistered prospective study.

This repository does not expand that corpus.

Specifically:

```text
10 research-software objects
        │
        │ observed by
        ▼
research-software-identity-audit
        │
        └── research infrastructure
            NOT an additional sample object
```

Mirrors, duplicate representations, supporting repositories, scholarly records, archival copies, and semantically non-equivalent objects are not automatically counted as additional research-software objects.

Any future expansion of the research corpus must be documented separately and must not be retrospectively represented as part of the original preregistered ten-object study.

---

# Scholarly-infrastructure layers

Each research software object is observed across six predefined infrastructure layers.

| Layer | Purpose in the study |
|---|---|
| Source repository | Source history, releases, repository identity, and release timestamps |
| Archival repository | Deposited scholarly software records and archival releases |
| Identifier registration | Persistent-identifier metadata and DOI relationships |
| Author registry | Attribution, author-level work records, grouping, and source summaries |
| Preservation archive | Long-term source preservation and archival identity |
| Discovery graph | Scholarly discovery, indexing, and downstream representation |

These layers are intentionally treated as different systems with different observable contracts.

They must not be interpreted as if they provided equivalent guarantees.

## Operational platforms

The six preregistered layers are analytical categories, not a requirement that exactly six concrete services be queried.

The current operational platform vocabulary is:

```text
GitHub
Zenodo
DataCite
ORCID
Software Heritage
OpenAIRE
OpenAlex
```

OpenAIRE and OpenAlex are intentionally recorded as separate platforms because they expose different records, clocks, processing states, and failure modes. Both map to the single preregistered `discovery_graph` layer.

Therefore:

```text
10 × 6 = 60 preregistered object-layer units
10 × 7 = 70 possible object-platform checks
```

The second quantity is evidence-collection granularity and does not replace the preregistered denominator.

---

# Unit of observation

The fundamental observation unit is:

```text
software object
    × infrastructure layer
    × observation time point
```

With:

```text
10 software objects
× 6 infrastructure layers
= 60 object-layer units
```

at each scheduled observation point.

Because the study uses repeated measurements, the total number of attempted observations depends on the number of operational observation time points.

---

# Observation schedule

The preregistered methodology requires observations to occur at predefined or scheduled time points following eligible software-release events.

The prospective dataset begins only after the OSF registration and after the first eligible new release event.

Concrete operational observation times, execution timestamps, and any subsequent schedule decisions are maintained in this repository with explicit provenance.

The operational schedule must not be silently rewritten after results become known.

Where a concrete operational specification is introduced after registration, it must retain its own timestamp and provenance and must not be retrospectively described as information contained in the frozen OSF registration.

---

# Observation states

Each attempted observation preserves its observed state.

The primary state vocabulary includes:

```text
observed
not found
rate limited
unresolved
partially verified
fully verified
```

Additional operational detail may be recorded where necessary, but the original observation must remain recoverable.

A failed or incomplete observation is not discarded merely because it is inconvenient.

Failure states are themselves research outcomes.

---

# Evidence rule

One of the central methodological rules of the project is:

> **Missing or unresolved evidence must not be converted into evidence of absence unless the observable contract of the relevant infrastructure explicitly supports that interpretation.**

Therefore:

```text
not found      ≠ global absence
rate limited   ≠ absence
unresolved     ≠ absence
partial        ≠ absence
unqueried      ≠ absence
```

A record may only be reported as absent when the evidence source and its documented contract justify that inference.

This distinction is fundamental to the study.

---

# Measured variables

Observation records may include:

- software-object identity
- infrastructure layer
- release-event timestamp
- retrieval timestamp
- observation time point
- observation state
- identifier type
- identifier value
- family/concept identifier
- version identifier
- creator identifier
- ORCID or equivalent creator identity
- archival identifier
- discovery-record identifier
- provenance fields
- source attribution
- verification mechanism
- version/family relationships
- DOI-to-record mappings
- aggregation state
- discovery state
- preservation state
- platform or HTTP response state
- pagination state
- rate-limit state
- correction event
- amendment event
- evidence location
- interpretation notes

Not every field is necessarily meaningful for every infrastructure layer.

Fields must only be compared when their semantics are compatible.

---

# Derived measures

The study intentionally avoids constructing a single global quality score.

Derived measures are limited to variables supported by directly observed evidence.

## Propagation latency

Where timestamps are both directly observed and temporally comparable:

```text
Latency(object, layer)
    =
first_observed_timestamp(object, layer)
    -
release_timestamp(object)
```

No latency value is imputed for missing, unresolved, rate-limited, or unqueried observations.

---

## Propagation order

Infrastructure layers may be ordered by their first directly observed qualifying post-release state.

Ties remain ties.

Missing observations are not assigned an inferred position.

---

## Cross-layer consistency

Semantically comparable identity fields may be classified as:

```text
consistent
divergent
unresolved
```

Only fields intended to express the same identity relation may be compared.

Differences between non-equivalent object types do not automatically constitute inconsistency.

---

## Aggregation recurrence

Previously observed structural patterns may be tested for recurrence, including:

- family-level grouping
- multiple source summaries
- duplicated or overlapping attribution surfaces
- equivalent recurring aggregation structures

A pattern is considered recurring only when the same predefined structural behavior is directly observed again.

---

## State-transition sequences

For each object-layer pair, categorical states may be ordered chronologically:

```text
state(t0)
→ state(t1)
→ state(t2)
→ ...
```

These transitions are reported descriptively.

They are not converted into a numerical quality score.

---

## Failure and partial-state frequency

Counts and proportions may be reported for:

- not found
- rate limited
- unresolved
- partial
- failed
- corrected
- otherwise incomplete observations

The denominator retains the full set of planned attempted observations where applicable.

Incomplete observations are not removed merely to make the result cleaner.

---

# Analysis policy

The preregistered study does not plan inferential statistical modeling.

The primary analyses use:

- direct counts
- proportions
- timestamp differences
- propagation order
- state-transition sequences
- cross-layer comparisons
- directly observed consistency or divergence

The study does **not** preregister:

- ANOVA
- regression
- structural equation modeling
- null-hypothesis significance testing
- p-value thresholds
- Bayesian model comparison
- causal modeling
- imputation-based reconstruction
- a composite infrastructure quality score

The research question concerns observable infrastructure behavior, not statistical generalization to an external population.

---

# Historical baseline and prospective evidence

The project distinguishes two evidence periods.

## Historical baseline

Earlier release waves and their previously collected observations form a fixed baseline.

Historical observations must not be retrospectively altered or reclassified merely to improve consistency with later evidence.

The first repository baseline package uses a cutoff of **2026-10-05 23:59:59 Asia/Shanghai** and preserves a Codex-generated reconciliation collected at approximately **2026-10-06 00:33:54 Asia/Shanghai**.

That package lives under `baseline/2026-10-05/`.

The collection clock is not backdated to the baseline cutoff. In particular, Zenodo counters observed on 2026-10-06 remain 2026-10-06 observations even when they describe releases published on 2026-10-04.

## Prospective observation window

The new dataset begins only after registration and the first eligible new release event.

The prospective dataset is recorded independently from the historical baseline.

This distinction must remain explicit in all derived analyses.

---

# Planned, operational, exploratory, and post hoc work

The repository distinguishes several classes of research activity.

### Preregistered

Directly specified by the frozen OSF registration.

### Operational specification

Details required to execute the preregistered design but recorded separately from the frozen registration.

Examples may include concrete execution schedules, machine-readable schemas, collection tooling, or repository-side implementation details.

### Amendment

A documented change to the study procedure made after registration.

Amendments must include their date, rationale, scope, and expected effect.

### Exploratory / post hoc

Analyses or checks introduced after registration that were not part of the original preregistered primary analysis.

Exploratory work is allowed.

It must simply remain identifiable as exploratory.

It must never be presented retrospectively as preregistered analysis.

---

# Provenance model

Every important research artifact should remain traceable to its origin.

The project distinguishes at least:

```text
source evidence
      ↓
raw observation
      ↓
normalized observation
      ↓
derived result
      ↓
interpretation
      ↓
reported conclusion
```

These layers must not be silently collapsed.

Where possible, observation records should preserve:

- source system
- source object
- retrieval timestamp
- query or endpoint identity
- platform response
- evidence artifact
- normalization rule
- derivation rule
- interpretation
- amendment or correction history

A current live endpoint is not assumed to reproduce a historical observation.

Historical evidence and present-day state must remain distinguishable.

---

# Corrections

Scholarly-infrastructure records may change after their first appearance.

Examples include:

- metadata correction
- creator-name correction
- identifier correction
- grouping changes
- source-attribution changes
- discovery-graph updates
- archival-resolution changes

Corrections should be recorded as state transitions rather than overwriting the previous observation.

Where possible:

```text
previous state
    ↓
correction event
    ↓
new state
```

The evidence trail should preserve both sides of the transition.

---

# Repository structure

Repository organization follows **responsibility and evidence role** rather than chronological marketing milestones. The canonical, maintained [directory and document map](docs/README.md#2-directory-map-where-to-read-and-where-a-future-contribution-belongs) lists the complete current ownership boundaries without repeating a static tree that becomes outdated after every monitoring package.

| Category | Directory owner |
| --- | --- |
| Frozen contract interpretation and fixed study identities | [`contract/`](contract/preregistration.md), [`corpus/`](corpus/object-manifest.csv), [`schema/`](schema/counting-rules.md) |
| Historic data boundary and operational schedule | [`baseline/`](baseline/README.md), [`schedule/`](schedule/README.md) |
| Historical diagnostic archive (not prospective) | [`history/diagnostics/`](history/diagnostics/README.md) |
| Schedule-governed prospective observations | [`observations/raw/`](observations/raw/README.md), [`observations/derived/`](observations/derived/README.md) |
| Retained historical evidence, provenance and descriptive analysis | [`history/evidence/`](history/evidence/README.md), [`provenance/`](provenance/README.md), [`analysis/`](analysis/README.md) |
| Citation and reproducible implementation | [`scholarly/`](scholarly/README.md), [`templates/`](templates/README.md), [`tools/`](tools/README.md), [`.github/`](.github/PULL_REQUEST_TEMPLATE.md) |
| Human-oriented repository documentation | [`docs/`](docs/README.md), [`OPEN_RESEARCH.md`](OPEN_RESEARCH.md), [`CONTRIBUTING.md`](CONTRIBUTING.md) |

Historical history/evidence/observation paths are intentionally **not moved for cosmetic cleanup**: earlier evidence manifests, digests and source locators must remain independently resolvable. The folder map is documentation, not an OSF amendment, release, scheduled wave, or new study-data record.

---

# Relationship to the ten research-software repositories

The study distinguishes the research corpus from the infrastructure used to study it.

```text
                ┌──────────────────────┐
                │  Research corpus     │
                │  10 software objects │
                └──────────┬───────────┘
                           │
                           │ repeated observations
                           ▼
             ┌─────────────────────────────┐
             │ Research Software Identity  │
             │ Audit                       │
             │                             │
             │ contract                    │
             │ schemas                     │
             │ evidence                    │
             │ provenance                  │
             │ analysis                    │
             └─────────────┬───────────────┘
                           │
                ┌──────────┴──────────┐
                ▼                     ▼
         OSF Registration       OSF Project
         frozen contract        live workspace
```

This repository is therefore part of the **research instrumentation and evidence infrastructure**, not part of the study sample.

---

# Observable-contract principle

Each scholarly infrastructure is interpreted according to what it actually exposes and guarantees.

The study does not assume that:

```text
existence
= identity
= attribution
= preservation
= discovery
= aggregation
= verification
```

These are separate properties.

Likewise:

```text
public
≠ indexed
≠ discovered
```

A platform may provide one property without providing another.

The project therefore treats repository, archival, identifier-registration, author-registry, preservation, and discovery systems as distinct observable contracts.

---

# Reproducibility

The repository is intended to make the research process inspectable and reproducible where the underlying infrastructures permit it.

Reproducibility may include:

- machine-readable object manifests
- documented infrastructure mappings
- explicit state taxonomies
- observation schemas
- evidence-retention rules
- timestamped observation records
- deterministic derived calculations
- validation tooling
- correction histories
- amendments
- analysis scripts
- provenance records

Reproducibility does not imply that every historical platform response can be reconstructed indefinitely.

External platforms evolve.

APIs change.

Discovery graphs update.

Records may be corrected.

Rate limits may differ.

For that reason, captured historical evidence and current live state are treated as different evidence objects.

---

# Public data and privacy

The study primarily uses public research-software and scholarly-metadata surfaces. Canonical public identifiers such as DOI, ORCID, public repository URLs, public release tags, and public scholarly record IDs are retained when necessary for reproducibility rather than pseudonymized.

Public accessibility does not mean everything visible should be collected. Credentials, API keys, cookies, session identifiers, private/expiring share tokens, IP addresses, unrelated visitor telemetry, private messages, and incidental personal information are excluded from committed evidence.

See `DATA_HANDLING.md` for the full policy.

---

# Research integrity

The project follows several operational principles.

1. Do not silently alter historical observations.

2. Do not treat failed retrieval as evidence of absence without infrastructure-specific justification.

3. Do not remove inconvenient missing, partial, or unresolved states from planned denominators.

4. Do not compare semantically non-equivalent identifiers as if they were identical.

5. Do not retroactively describe exploratory analysis as preregistered.

6. Do not collapse different infrastructures into a single global quality score.

7. Preserve timestamps and provenance whenever an observation or correction is recorded.

8. Distinguish raw evidence, normalized observation, derived result, and interpretation.

9. Record amendments and deviations explicitly.

10. Prefer auditable uncertainty over unsupported certainty.

---

# Scope and non-goals

This project is an infrastructure audit.

It is **not** intended to:

- rank scholarly infrastructures
- produce a universal infrastructure quality score
- infer causal effects
- estimate population-wide prevalence
- evaluate individual researchers
- treat discovery as equivalent to preservation
- treat identifier registration as equivalent to attribution
- infer absence from unresolved evidence
- generalize the ten-object corpus beyond what the observed evidence supports

The objective is narrower:

> observe what each infrastructure actually exposes, when it exposes it, how representations differ, and where the boundaries of each observable guarantee lie.

---

# Status

Current research stage:

**中文说明 / English reading:** 下述箭头为研究生命周期示意，不声明每个阶段已按计划执行；The sequence below is a research-lifecycle map, not an executed-run inventory

```text
Historical audit
      ↓
Engineering interpretation
      ↓
Trust-boundary analysis
      ↓
OSF preregistration
      ↓
Prospective longitudinal observation
      ↓
Evidence and reproducible analysis
```

The OSF preregistration is public and frozen.

This repository provides the live operational layer for the prospective research lifecycle.

Prospective observations are kept distinct from the historical baseline.

Pre-eligibility monitoring is also kept separate from the prospective dataset under `history/diagnostics/`.

---

# Citation

The frozen preregistered research plan can be cited as:

> Jiang, X. (2026, October 5). *Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures*. OSF. https://doi.org/10.17605/OSF.IO/5B329

The research software infrastructure is also archived and citable through Zenodo:

- **Concept DOI (all versions):** https://doi.org/10.5281/zenodo.23166490
- **Latest GitHub Release observed at the 2026-11-17 repository review / 2026-11-17 核对的最新 GitHub 发行版:** [`v2026.11-nov15-identity-reconciliation`](https://github.com/lostlight530/research-software-identity-audit/releases/tag/v2026.11-nov15-identity-reconciliation) (published 2026-11-15T15:55:57Z) — its new exact Zenodo version DOI is **NOT_VERIFIED** in this review / 本次未核实该发行版的新 Zenodo 版本 DOI
- **Most recent exact Zenodo version DOI independently documented here / 本仓现有证据最后确认的 Zenodo 版本 DOI:** [`v2026.10-control-lifecycle-reconciliation`](https://github.com/lostlight530/research-software-identity-audit/releases/tag/v2026.10-control-lifecycle-reconciliation) (published 2026-10-31) — https://doi.org/10.5281/zenodo.23839900
- **Identity rule / 身份规则:** A newer GitHub Release does not by itself establish a new Zenodo archive or DOI, and a current `main` citation field does not retrospectively change immutable archived tag bytes / 新 GitHub 发行版不自动证明已有新 Zenodo 归档或 DOI，当前 `main` 的引用字段不能倒改旧归档字节
- **Previous evidence-integrity release:** `v2026.10-evidence-integrity` (2026-10-18) — https://doi.org/10.5281/zenodo.23446162
- **Previous evidence-reconciliation release:** https://doi.org/10.5281/zenodo.23284570
- **Previous initial-runtime release:** https://doi.org/10.5281/zenodo.23176748
- **Historical `beta` release:** https://doi.org/10.5281/zenodo.23166491

The immutable October 10 release tag contains stale embedded citation/CodeMeta version fields. The live `main` metadata was corrected afterward; the tagged archive was **not** rewritten. See [citation and identifier guidance](scholarly/CITATION.md) and [release evidence note](RELEASE_POLICY.md#archived-evidence-reconciliation-release--2026-10-10).

Machine-readable citation metadata is maintained in `CITATION.cff`, `codemeta.json`, and `.zenodo.json`. See `scholarly/CITATION.md` for identifier-specific citation guidance.

---

# Licensing

Repository-owned software, schemas, templates, tooling, and documentation are released under the **MIT License** unless a file states otherwise.

Third-party evidence and externally sourced material retain their original attribution, rights, and source terms; inclusion in this repository does not relicense them.

The frozen OSF preregistration is a separate scholarly object released under **CC BY 4.0**.

See [LICENSING.md](./LICENSING.md) for scope details.

---

# Related resources

### OSF Preregistration

https://osf.io/5b329/overview

### Registration DOI

https://doi.org/10.17605/OSF.IO/5B329

### Associated OSF Project

https://osf.io/wa5v8

### Zenodo — all versions

https://doi.org/10.5281/zenodo.23166490

### Zenodo — historical October 18 evidence-integrity release

https://doi.org/10.5281/zenodo.23446162

### Zenodo — historical evidence-reconciliation release

https://doi.org/10.5281/zenodo.23284570

### Zenodo — historical beta release

https://doi.org/10.5281/zenodo.23166491

### ORCID

https://orcid.org/0009-0001-3617-0832

---

# Methodological summary

In compact form, this project follows the chain:

```text
question
    ↓
preregistered research contract
    ↓
fixed corpus
    ↓
explicit infrastructure boundaries
    ↓
scheduled observation
    ↓
timestamped evidence
    ↓
state classification
    ↓
provenance-preserving derivation
    ↓
descriptive analysis
    ↓
bounded conclusion
    ↓
retest
```

The central rule is simple:

> **Record what the infrastructure actually exposes, preserve what is unknown, and never turn missing evidence into stronger claims than the observable contract supports.**

---

## Repository boundary

For avoidance of doubt:

> **`research-software-identity-audit` is the research repository used to operate and document the study. It is not an additional research-software object in the fixed ten-object corpus defined by the OSF preregistration.**

That boundary is intentional and should remain explicit throughout the project lifecycle.

## October 10 research-state reconciliation (diagnostic, not prospective)

This repository's current supplementary records are deliberately separated by **evidence role**, and do not add a new fixed software object or new preregistered infrastructure layer:

- [Zenodo October 10 source diagnostic](history/diagnostics/2026-10-10/01-zenodo-surge-recheck/README.md) — original 11-concept source capture retained with source identity.
- [Zenodo independent 32-version recheck](history/diagnostics/2026-10-10/02-reconciliation/README.md) — separate reviewer, full version enumeration, version-summed **1,813 fixed-ten views / 7 downloads**, separately reported **51 control views**, and unresolved RS07 attached-family aggregate conflict (`186` vs version sum `85`).
- [October 10 institutional public-status ledger](scholarly/infrastructure-review-2026-10-10.md) — RSD, SciCrunch RRID, rseng, DataCite/Zenodo, OSF, ORCID, OpenAlex and bounded SWH/OpenAIRE outcomes. **RRID SCR_029105 is now publicly searchable**; earlier pending status remains historically recorded.
- [Supplementary Zenodo counting discipline](schema/counting-rules.md#supplementary-zenodo-version-family-reconciliation-2026-10-10) — no cross-version unique-person summation, no aggregate double-counting, no inferred version-level interval without comparable earlier version rows.

All October 10 records are **diagnostic/exploratory**, not eligible new-release timepoints. The OSF Registration remains frozen; the prospective window has **not** been evidenced as started. Public registry/DOI appearance does **not** prove institutional endorsement, scientific adoption, or a particular visitor/referrer/aggregation mechanism. Historical source and independent reviewer records have distinct authorship and provenance.

## October 10 final documentary and institutional closeout

The dated [October 10 final closeout](scholarly/closeout-review-2026-10-10.md) records a bounded repository contract/document audit, renewed institution-facing public status, external-source ownership, all ten **read-only** research template checks, and unresolved evidence limits. Supporting ledgers: [public scholarly-infrastructure review](scholarly/infrastructure-review-2026-10-10.md), [Zenodo 32-version reconciliation](history/diagnostics/2026-10-10/02-reconciliation/README.md), and [release identity policy](RELEASE_POLICY.md).

The external rseng PR #498 is **not** a merged upstream record; local GitHub documentation merges cannot substitute for that maintainer's decision. The research-control repository remains outside the fixed ten-object corpus. No new eligible release, operational schedule, prospective observation, scientific-impact claim or new registration is created by this documentation closeout.

## October 14 diagnostic records

[Midnight](history/diagnostics/2026-10-14/03-midnight-facility-recheck/README.md), [morning](history/diagnostics/2026-10-14/04-morning-facility-recheck/README.md), and [noon user pages](history/diagnostics/2026-10-14/05-noon-user-pages/README.md) retain separate source and time semantics. Forty fixed-family DOI routes resolve to ten OpenAlex Works in the morning capture. These records add no eligible prospective timepoint or fixed-corpus object

## October 14 evening new-release propagation

[Evening diagnostics and new-version evidence](history/diagnostics/2026-10-14/06-evening-facility-recheck/README.md) preserve ten new public releases, 72 findable DOIs, 15 ORCID groups / 85 sources and 43 enumerated versions; user pages and independent captures remain separate

## October 15 morning diagnostic recheck

[Full morning record](history/diagnostics/2026-10-15/01-morning-facility-recheck/README.md) retains 27 author-query Works, 84 ORCID source summaries, 72 DOI records and source-specific counter reconciliation; earlier captures remain dated

## Second independently preregistered workflow study (separate contract)

The same shared CONTROL repository also holds [OSF vshwk / WorkflowHub Project 490 study custody](studies/osf-vshwk/README.md) in the separate `studies/osf-vshwk/` namespace. Its approved amended case (2332/2334; eight project-level and sixteen nested lineage-level bundles per complete cycle) is **not part of the fixed RS01–RS10 / six-layer / 60-unit 5b329 design**. All other ten source repositories are read-only research subjects; see the [two-study boundary](studies/README.md).
