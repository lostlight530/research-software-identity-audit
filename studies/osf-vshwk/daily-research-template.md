# Study 2 daily research template — Project AUHJF / Registration VSHWK

> **Template only.** This file is not a cycle, observation, endpoint attempt, or research result. A Pacific reporting-day label is a navigation label, not a cycle trigger or acquisition timestamp.

## 1. Study identity and authority

- **OSF Project:** [AUHJF](https://osf.io/auhjf/) · Project DOI [10.17605/OSF.IO/AUHJF](https://doi.org/10.17605/OSF.IO/AUHJF)
- **OSF Study Registration:** [VSHWK](https://osf.io/vshwk/) · Registration DOI [10.17605/OSF.IO/VSHWK](https://doi.org/10.17605/OSF.IO/VSHWK)
- **Current approved authority:** Schema Response [6afdcc7108de91a0f0cefd6c](https://api.osf.io/v2/schema_responses/6afdcc7108de91a0f0cefd6c/)
- **Project / Registration pair:** [2026-11-26 OSF object crosswalk](../osf-object-pairing-crosswalk-2026-11-26.md)
- **Study contract:** [contract/README.md](contract/README.md)
- **Immutable endpoint manifest:** [contract/endpoints-v1.json](contract/endpoints-v1.json)
- **Cycle record template:** [cycles/record-template.md](cycles/record-template.md)

## 2. Daily gate — a day is not a cycle

The approved VSHWK protocol allows a cycle to be initiated by either:

- a relevant public-infrastructure event; or
- a documented full-scope research review.

It does **not** prescribe a fixed daily interval, fixed maximum cycle count, predetermined wave count, or fixed calendar end date. Do not create a new cycle merely because the calendar advanced or a Day folder is expected.

1. Read fresh main, open PRs, the latest approved VSHWK Schema Response, the active immutable endpoint manifest, the current cycle ledger, and relevant source state.
2. Review only the trigger signals needed to decide whether a relevant public-infrastructure event has occurred. If a trigger check is made, preserve its exact source, locator, retrieval clock, and evidence separately. This minimal trigger surveillance is not a full cycle and is never retroactively counted as one of the 22 manifest endpoint attempts. If the same locator is queried again after a cycle's precollection intent is committed, preserve that later request as a distinct cycle attempt.
3. Record the reason a cycle is being considered. If neither a relevant event nor a documented full-scope review exists, record the daily gate as NO_CYCLE_INITIATED and do not execute the full 22-endpoint manifest.
4. Before the first full-cycle source request, create and commit an immutable precollection intent containing the trigger/review reason, reporting-day label, actual declaration time, manifest version, authority ID, Project 490, and both lineage identities.
5. If a scope or endpoint change is needed, declare a new versioned manifest and rationale **before** collection. Never edit manifest v1 or silently add fallback endpoints.
6. A reporting-day label uses America/Los_Angeles only. Preserve actual acquisition timestamps in UTC and Asia/Shanghai.

The daily gate disposition is workflow bookkeeping, not a new research-state taxonomy.

## 3. Fixed case, nested evidence, and endpoint denominator

- **One independent project-level case:** WorkflowHub Project 490
- **Lineage A:** welcome-to-github, WorkflowHub record 2332 v9, DOI 10.48546/workflowhub.workflow.2332.9
- **Lineage B:** zero-entropy-lab, WorkflowHub record 2334 v9, DOI 10.48546/workflowhub.workflow.2334.9
- **Analytical scope:** 8 predefined infrastructure layers
- **Per complete cycle:** 8 project-layer bundles and 16 nested lineage-layer evidence bundles
- The 16 nested bundles are repeated descriptive evidence within one case, **not 16 independent samples**
- **Manifest v1:** 22 endpoint locators across the eight layers; endpoint checks are collection granularity, not research sample size

| Layer | Manifest v1 endpoints |
|---|---:|
| L1 Source repository | 4 |
| L2 Workflow registry | 3 |
| L3 Archival repository | 2 |
| L4 Identifier registration / resolution | 4 |
| L5 Source preservation | 2 |
| L6 Testing, monitoring and execution | 2 |
| L7 Researcher attribution | 1 |
| L8 Discovery and aggregation | 4 |
| **Total** | **22** |

Capture shared Project 490 and shared ORCID evidence once. Reference it in both lineage analyses without duplicating the underlying source record.

## 4. Daily entry — copy only after the gate

### Daily review identity

- Operational task day:
- Reporting date:
- Reporting timezone (America/Los_Angeles):
- Reviewer:
- Daily review timestamp:
- Relevant public-infrastructure event or documented full-scope review:
- Evidence supporting the initiation reason:
- Cycle initiated: YES / NO
- If no cycle, reason:

### Precollection declaration — required before acquisition

- Cycle ID:
- Approved Schema Response ID:
- Manifest path and version:
- Precollection intent path:
- Precollection intent commit:
- Intent committed before first source request: YES / NO
- Declaration timestamp (UTC):
- Declaration timestamp (Asia/Shanghai):
- Reporting-day label (Pacific):
- No prior-day source state reused: YES / NO

### Acquisition window and endpoint accounting

- Actual first source acquisition (UTC):
- Actual last source acquisition (UTC):
- Asia/Shanghai equivalent:
- Expected endpoints: 22
- Primary endpoint attempts:
- Explicit NOT_QUERIED rows and reasons:
- Explicit NOT_APPLICABLE rows and reasons:
- Follow-up attempts (kept separate from primary attempts):
- Original source-ledger paths and blob SHAs:
- Normalized endpoint outcome index:
- Cycle machine summary:
- Human-readable cycle report:

### Keep the evidence dimensions separate

1. **Endpoint retrieval:** RESPONSE_COMPLETE, RESPONSE_PARTIAL, NOT_FOUND_AT_QUERIED_ENDPOINT, RATE_LIMITED, ACCESS_BLOCKED, ENDPOINT_ERROR, NOT_QUERIED, NOT_APPLICABLE
2. **Relationship verification:** VERIFIED_DIRECT_LINK, RECORD_FOUND_LINK_UNVERIFIED, UNRESOLVED, CONFLICT, NOT_ASSESSED, NOT_APPLICABLE
3. **Record-condition flags:** STALE_METADATA, DUPLICATE_REPRESENTATION, CONFLICTING_METADATA; if the source does not serialize flags, record NOT_SERIALIZED / NOT_ASSESSED, not zero
4. **Testing / monitoring / execution:** retain exact workflow identity, run ID, triggering event, source revision, status, conclusion, and artifacts separately. A workflow definition or schedule declaration does not prove execution.

### Bounded disposition and next work

- Cycle disposition:
- Per-layer unresolved results:
- Lineage A unresolved results:
- Lineage B unresolved results:
- Source-fidelity limits:
- Deviations / corrections:
- Next-cycle priorities:

## 5. Collection and interpretation rules

- Account for every manifest locator with a primary attempt or explicit NOT_QUERIED / NOT_APPLICABLE reason.
- Preserve original errors and partial results. A complete attempt ledger is not a successful retrieval cycle.
- At most one researcher-initiated retry for transient 5xx / timeout / rate-limit cases; respect visible Retry-After. If the intermediary hides the provider response, record opaque transport and do not claim retry compliance.
- Do not infer global absence from HTTP 404, empty extraction, 429, timeout, connector rejection, or access failure.
- Do not infer execution from a workflow file, registry record, or schedule.
- Do not silently substitute providers, fallback URLs, or endpoints outside the declared manifest.
- Keep primary attempts, supplementary follow-ups, raw source ledgers, normalized indexes, summaries, and interpretations separately traceable.
- Do not mutate OSF, WorkflowHub, Zenodo, DataCite, GitHub source repositories, Software Heritage, ORCID, OpenAIRE, or OpenAlex as part of a read-only cycle.
- A cycle may close with unresolved results; never optimize the report for an all-green disposition.

**Small and Stable · Contract before observation · Evidence before interpretation**
