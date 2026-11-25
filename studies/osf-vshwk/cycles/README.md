# VSHWK prospective observation-cycle ledger

**Study:** OSF VSHWK  
**Current case:** WorkflowHub Project 490  
**Embedded lineages:** 2332 v9 (A) and 2334 v9 (B)  
**Authority:** approved Schema Response `6afdcc7108de91a0f0cefd6c`

## Cycle initiation policy

The approved protocol does **not** prescribe a fixed daily schedule, calendar interval, predetermined wave count, or fixed end date. Each cycle is initiated by a relevant public-infrastructure event or a documented full-scope research review. Its reason and manifest version must be recorded before acquisition begins.

A reporting-day label is not an acquisition timestamp. Retain actual source clocks in UTC and Asia/Shanghai; use America/Los_Angeles only as a reporting-day label. Never backdate a cycle or inherit a previous run's source state.

## Cycle accounting

Every cycle applies its declared versioned manifest to both lineages and all eight analytical layers. Every endpoint must have either an actual attempt record or an explicit `NOT_QUERIED` / `NOT_APPLICABLE` disposition with a reason. Attempt accounting can be complete while provider retrieval remains partial or failed.

The primary analytical unit is one project × one layer × one cycle: **8 project-layer bundles** per complete cycle. The two lineages add **16 nested lineage-layer evidence bundles**, not 16 independent samples. Shared Project 490 and ORCID evidence are retained once.

## Cycle index

| Cycle | Reporting day | Manifest | Endpoint accounting | Disposition |
|---|---|---|---:|---|
| [Cycle 01](cycle-2026-11-23-pst-01/README.md) | 2026-11-23 America/Los_Angeles | [v1](../contract/endpoints-v1.json) | 22/22 attempted | `CYCLE_ATTEMPTS_CLOSED_WITH_UNRESOLVED_RESULTS` |

Cycle 01's actual acquisition window was 2026-11-24T07:07:37.297Z–2026-11-24T07:09:58.002Z. The reporting-day label is 2026-11-23 Pacific; the actual China acquisition date is 2026-11-24.

## Reusable entrypoint

Use the [cycle record template](record-template.md) for future cycles. It is a structure guide only, not a research record and not an observation. Do not copy Cycle 01 results into a later cycle.

## Historical custody gap — November 24 Pacific reporting day

The separate [Cycle 02 custody index](cycle-2026-11-24-pst-01/evidence/README.md) entered main in commit [4b91ff61](https://github.com/lostlight530/research-software-identity-audit/commit/4b91ff61a7d74d38bd43671779ad1db3d36b3369), whose title calls it Day 1 evidence custody. The index itself calls the folder Cycle 02. These labels do not establish a completed observation. The pinned tree contains the index alone, not its listed source ledgers, original precollection intent, outcome index or summary. The November 25 review found no recovery branch or PR; historical acquisition clocks and attempt count remain unknown.

See the [machine-readable custody-gap record](cycle-2026-11-24-pst-01/custody-gap.json). Disposition: `BLOCKED_ORIGINAL_RECORDS_NOT_AVAILABLE`. This is **not a validated cycle**, not a new observation, and not an endpoint failure count. The original index is retained unchanged. Restore the exact original records with provenance if they become available; no later read may be substituted or backdated. A separately initiated future review uses its own actual clocks and manifest.

## Task-day label correction — 2026-11-25

The owner clarified that the Cycle 02 custody review and [PR #148](https://github.com/lostlight530/research-software-identity-audit/pull/148) merge at 2026-11-25 01:35–01:36 America/Los_Angeles were still part of operational **Day 1**. The current task day is now **Day 2**. The earlier assistant incorrectly inferred Day 2 from the Pacific calendar date alone. Operational task-day labels are owner-supplied workflow labels; they are distinct from cycle IDs, reporting-day dates, and acquisition timestamps, and one task day may span calendar dates. See the append-only [machine-readable task-day correction](cycle-2026-11-24-pst-01/task-day-label-correction-2026-11-25.json).

The `BLOCKED_ORIGINAL_RECORDS_NOT_AVAILABLE` disposition remains for the Day 1 recovery attempt. The owner confirms the local remote-device access path was offline during that attempt. This is an access-path limitation, not evidence that the original records never existed or are globally unavailable. The exact device-status timestamp and raw status output were not retained; no more precise historical claim is made. The existing custody-gap record, original index blob, Pacific reporting-day field, and all acquisition-time unknowns remain unchanged. No Day 2 observation was created by this correction.
