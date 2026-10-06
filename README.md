# research-software-identity-audit

[![DOI](https://zenodo.org/badge/1405944227.svg)](https://doi.org/10.5281/zenodo.23166490)

> Research infrastructure for a prospective longitudinal audit of research software identity propagation across open scholarly infrastructures.

This repository is the operational, evidence, provenance, and reproducibility workspace for the study:

**Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures**

The study is publicly preregistered on OSF and examines how a fixed corpus of research software objects is represented, propagated, preserved, aggregated, discovered, corrected, or left unresolved across multiple scholarly-infrastructure layers over time.

> **Important:** This repository supports the study. It is **not an eleventh research-software object** in the fixed ten-object study corpus.

---

## Research registration

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

The repository is expected to evolve around the following structure:

```text
.
├── README.md
├── DATA_HANDLING.md
├── CITATION.cff
├── codemeta.json
├── .zenodo.json
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── validate.yml
│
├── contract/
│   ├── preregistration.md
│   ├── contract-map.yaml
│   └── known-limitations.md
│
├── corpus/
│   └── object-manifest.csv
│
├── baseline/
│   ├── README.md
│   └── 2026-10-05/
│       ├── README.md
│       ├── manifest.yaml
│       ├── raw-reconciliation-record-2026-10-06.md
│       ├── reconciliation-notes.md
│       ├── source-ledger.yaml
│       ├── doi-map.csv
│       ├── platform-state.yaml
│       └── zenodo-statistics.yaml
│
├── schedule/
│   └── README.md
│
├── schema/
│   ├── observation.schema.json
│   ├── state-taxonomy.yaml
│   ├── infrastructure-layers.yaml
│   ├── platforms.yaml
│   └── counting-rules.md
│
├── observations/
│   ├── raw/
│   └── derived/
│
├── monitoring/
│   ├── README.md
│   └── 2026-10-06-wave-01/
│
├── evidence/
│   └── README.md
│
├── analysis/
│   └── README.md
│
├── provenance/
│   └── README.md
│
├── scholarly/
│   ├── README.md
│   ├── CITATION.md
│   └── identifiers.yaml
│
├── templates/
│   └── ...
│
├── tools/
│   ├── README.md
│   └── check.py
│
├── AMENDMENTS.md
└── DEVIATIONS.md
```

The exact structure may evolve as implementation proceeds.

Changes to repository organization do not themselves alter the frozen research design unless they modify the substantive research contract.

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

Pre-eligibility monitoring is also kept separate from the prospective dataset under `monitoring/`.

---

# Citation

The frozen preregistered research plan can be cited as:

> Jiang, X. (2026, October 5). *Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures*. OSF. https://doi.org/10.17605/OSF.IO/5B329

The research software infrastructure is also archived and citable through Zenodo:

- **Concept DOI (all versions):** https://doi.org/10.5281/zenodo.23166490
- **Archived `beta` release DOI:** https://doi.org/10.5281/zenodo.23166491

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

### Zenodo — beta release

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
