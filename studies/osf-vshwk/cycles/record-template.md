# VSHWK cycle record template

**OSF Project / Study Registration pair:** [AUHJF](https://osf.io/auhjf/) / [VSHWK](https://osf.io/vshwk/) · [2026-11-26 pair crosswalk](../../osf-object-pairing-crosswalk-2026-11-26.md)

> **Template only.** This file is not a cycle, observation, endpoint attempt, or research result. Copy the structure into a new cycle directory only after a real precollection decision.

## Stable path and identity

Recommended future directory pattern: `cycle-YYYY-MM-DD-pacific-NN/`. The date is the America/Los_Angeles reporting-day label only. Keep actual acquisition timestamps in UTC and Asia/Shanghai. Existing historical cycle IDs are not renamed.

## Required package

```text
cycle-YYYY-MM-DD-pacific-NN/
├── README.md
├── precollection-intent.json
├── endpoint-outcome-index.jsonl
├── cycle-summary.json
└── evidence/
    └── README.md
```

Additional original source ledgers may be added under `evidence/`; never overwrite or normalize them in place. A blocked capture that cannot satisfy the cycle package must be preserved separately under the [capture-gap procedure](../capture-gaps/README.md), not treated as a validated cycle.

## Before acquisition

1. Read the current OSF-approved VSHWK schema response and active immutable endpoint manifest
2. Read the latest remote state of both source repositories and relevant public services; do not inherit previous cycle state
3. Record the trigger / full-scope review reason, reporting-day label, UTC declaration time, Asia/Shanghai equivalent, manifest path and version, approved response ID, Project 490 and both lineages
4. Commit the precollection intent before the first source request
5. If scope or endpoints change, create and declare a new manifest version before collection; do not edit a published manifest

The protocol has no fixed calendar interval, predetermined wave count, or fixed end date.

## During acquisition

- Attempt every endpoint in the declared manifest, or retain an explicit `NOT_QUERIED` / `NOT_APPLICABLE` record with a reason
- Keep one endpoint row per manifest locator, including failures and unattempted endpoints
- Preserve exact source URL, collector, actual start/end UTC, Asia/Shanghai clock, reporting-day label, returned identity, retrieval state, relationship-verification state, record-condition flags, source evidence path and source blob SHA where available
- Preserve original connector/provider errors; do not convert opaque connector errors into provider HTTP status
- Use bounded batches with a verified durable checkpoint before the next batch: exact locator IDs, original minimized receipts, source clocks, ledger blob SHA and commit reference. Keep enough execution budget for the persistence steps. Batch sizes are implementation details, not new manifest versions or research units.
- Record collector invocation times, provider event timestamps, extractor acquisition dates and freshness separately. A cached or undated extract is not a contemporaneous provider observation. A record condition flag needs its own evidence; extraction age alone is not proof of provider metadata staleness.
- Keep only focal public identifiers and necessary verification fields; document excerpting/redaction and do not retain unrelated public-work entries or private/sensitive incidental material.
- At most one researcher-initiated retry for transient 5xx / timeout / rate-limit cases; respect visible `Retry-After`; if the intermediary hides the provider response, record opaque transport and do not claim retry compliance
- Capture shared Project 490 and ORCID evidence once; reference it in both lineage analyses without multiplying the underlying record
- Do not infer workflow execution from a file, registry card, or schedule declaration; require exact workflow identity, run ID, source revision, event, conclusion and associated evidence

## After acquisition

1. Immutable original source ledgers in `evidence/`
2. One normalized `endpoint-outcome-index.jsonl` row per manifest endpoint
3. `cycle-summary.json` with denominators, retrieval-state counts, relationship-state counts, per-layer and per-lineage classifications, source-fidelity limits, and disposition
4. `README.md` with the human-readable report and bounded conclusion
5. Update the cycle index only after the package is retained
6. Verify receipt-to-index coverage, exact manifest locators, unique IDs, clocks, ledger blob SHAs and summary counts. If acquisition/custody fails and the package cannot be closed faithfully, preserve the gap separately and keep unknown attempt counts unknown. Never use later acquisition to reconstruct missing originals.

## Required report sections

- Authority, case, lineages and manifest version
- Precollection trigger and declaration time
- Reporting-day label and actual UTC / Asia/Shanghai acquisition window
- Endpoint accounting and the meaning of completion
- 8-layer classification table
- Lineage A and B paired descriptions
- Verified direct fields and unverified candidate relationships
- Retrieval failures, partial responses, unattempted endpoints and follow-ups
- Record-condition flags (or explicit statement that the source representation does not serialize them)
- Testing / monitoring / execution evidence as a separate dimension
- Evidence fidelity, original-versus-derived boundary and source references
- Deviations, unresolved questions and next-cycle priorities
- A bounded disposition, never an all-green proxy

## Interpretation rules

- 1 project case × 8 layers = 8 project-layer bundles
- 2 lineages × 8 layers = 16 nested lineage-layer bundles, not independent samples
- Endpoint count is collection granularity, not sample size
- `RESPONSE_COMPLETE` does not by itself mean identity verified
- `RESPONSE_PARTIAL` or `ENDPOINT_ERROR` does not mean record absent
- `VERIFIED_DIRECT_LINK` is scoped to the exact fields and relationship tested; it is not global workflow equivalence
- A missing condition-flag field is not a zero flag count
- Historical records, current live reads, follow-ups and derived summaries keep separate provenance
