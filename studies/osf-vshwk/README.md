# Study 2 — Longitudinal Audit of an Open Research Workflow Across Scholarly Infrastructures

## Project and registration identity

- **Public project:** [OSF AUHJF](https://osf.io/auhjf/overview) · Project DOI [10.17605/OSF.IO/AUHJF](https://doi.org/10.17605/OSF.IO/AUHJF)
- **Registration:** [OSF VSHWK](https://osf.io/vshwk/overview) · Registration DOI [10.17605/OSF.IO/VSHWK](https://doi.org/10.17605/OSF.IO/VSHWK)
- AUHJF is an entry point only; the OSF overview states that it holds no data or files
- The owner-confirmed AUHJF Project Description is mirrored **verbatim** in [public-project-description.md](public-project-description.md)
- That public Description retains its stated historical focal case (WorkflowHub 2347 v2) and three-wave wording. It is project-level text, **not** the current VSHWK protocol authority
- **Current protocol authority:** VSHWK approved amendment [Schema Response 6afdcc7108de91a0f0cefd6c](https://api.osf.io/v2/schema_responses/6afdcc7108de91a0f0cefd6c/), submitted 2026-11-18T18:58:20.050020Z, `reviews_state=approved`
- **Latest registration-page metadata update:** OSF API `date_modified=2026-11-24T12:00:17.626133Z` (2026-11-24 20:00:17.626 Asia/Shanghai); this descriptive metadata update does not replace or amend the approved Schema Response
- Original VSHWK response `6af56f49221ba1b47e9f7490` and its 2347 v2 framing remain registration history; the approved amendment governs current prospective collection

## Current approved research case

The amended focal case is **one bounded WorkflowHub project**, [Project 490](https://workflowhub.org/projects/490), containing two paired embedded workflow lineages:

| Lineage | Source repository | WorkflowHub record | Registered version | DOI |
|---|---|---:|---:|---|
| A | [welcome-to-github](https://github.com/lostlight530/welcome-to-github) | [2332](https://workflowhub.org/workflows/2332?version=9) | v9 | [10.48546/workflowhub.workflow.2332.9](https://doi.org/10.48546/workflowhub.workflow.2332.9) |
| B | [zero-entropy-lab](https://github.com/lostlight530/zero-entropy-lab) | [2334](https://workflowhub.org/workflows/2334?version=9) | v9 | [10.48546/workflowhub.workflow.2334.9](https://doi.org/10.48546/workflowhub.workflow.2334.9) |

Registered source commits are historical identity anchors:
- A: `1c71b0d983021fd8fbcf6cc8cd2ccbbe7d0d6d2a`
- B: `5b360ed531812107cdd8fc1d26c808dcb393a4b8`

WorkflowHub 2347 v2 is historical context, not a current primary lineage. Historical record 2337 is not a third primary lineage and is contextual only where direct provenance supports it.

## Units and denominators

- Independent project-level case: **1**
- Predefined infrastructure layers: **8**
- Project-layer-cycle bundles: **1 × 8 = 8** per complete cycle
- Nested lineage-layer evidence bundles: **2 × 8 = 16** per complete cycle
- The 16 nested bundles are repeated descriptive evidence within one case, not 16 independent subjects
- Manifest v1 contains **22 endpoint locators**; this is collection granularity, not sample size

Shared Project 490 and ORCID candidate evidence are collected once and referenced at the appropriate analytical levels, not duplicated as independent records.

## Observation-cycle rules

The approved amendment specifies repeated observation cycles without a predetermined number of waves, fixed calendar interval, or fixed calendar end date. A cycle may be initiated by a relevant public-infrastructure event or a documented full-scope research review. Its reason must be recorded **before** collection begins.

A complete cycle accounts for every endpoint in its declared manifest by an actual attempt or an explicit, attributable reason for not querying it. A cycle may be complete by accounting while containing partial responses, errors, blocked endpoints, or unresolved relationships. Completion never means all providers succeeded.

For each cycle, preserve the actual precollection intent, manifest version, original source attempts, follow-up outcomes with their actual collection windows, normalized endpoint index, derived summary, project-level and nested lineage classifications, unresolved states, and bounded conclusion.

Actual source clocks are retained in UTC and Asia/Shanghai. America/Los_Angeles is a reporting-day label only; it never replaces the scientific acquisition timestamp.

## Repository custody and separation

This Study 2 namespace is inside the existing CONTROL repository. It is not a twelfth repository, RS11, or a third workflow lineage.

- Study 1 [5b329](https://osf.io/5b329/) retains its canonical root-level `contract/`, `corpus/`, `schema/`, and `schedule/`, plus established baseline, monitoring, evidence and conditional observation paths
- Study 2 VSHWK owns the separate `studies/osf-vshwk/` namespace: its `contract/`, `cycles/`, and Day 0–2 navigation indexes
- VSHWK day indexes point to canonical cycle/custody records; they do not copy evidence or turn a custody gap into a completed cycle
- RS01–RS10, both focal source repositories, WorkflowHub and all external scholarly services are read-only research targets
- Only the existing CONTROL repository receives study-control documentation and retained evidence

## Daily workspace index

- [Day 0 — 2026-11-23 Pacific](day0/README.md) → Cycle 01
- [Day 1 — 2026-11-24 Pacific](day1/README.md) → historical Cycle 02 custody gap; original acquisition records remain unavailable
- [Day 2 — 2026-11-25 Pacific](day2/README.md) → newly initiated, independent full-scope cycle

These Day pages are navigation indexes only. The canonical protocol remains in `contract/`; canonical acquisition, endpoint and evidence records remain under `cycles/`. The Day 1 index does not create a validated cycle, and Day 2 does not replace its missing historical records.

## Operational entrypoints

1. [Contract authority and state rules](contract/README.md)
2. [Eight-layer / 22-endpoint scope crosswalk](contract/endpoint-scope-crosswalk.md)
3. [Immutable endpoint manifest v1](contract/endpoints-v1.json)
4. [Prospective cycle ledger and SOP](cycles/README.md)
5. [Reusable cycle record template](cycles/record-template.md)
6. [Day 0 index and Cycle 01 report](day0/README.md)
7. [Day 1 index and historical custody-gap record](day1/README.md)
8. [Day 2 index and independent Cycle 2026-11-25 report](day2/README.md)
