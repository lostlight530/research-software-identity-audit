# VSHWK prospective observation-cycle ledger

**Study:** OSF VSHWK  
**Current case:** WorkflowHub Project 490  
**Embedded lineages:** 2332 v9 (A) and 2334 v9 (B)  
**Authority:** approved Schema Response `6afdcc7108de91a0f0cefdc6`

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
