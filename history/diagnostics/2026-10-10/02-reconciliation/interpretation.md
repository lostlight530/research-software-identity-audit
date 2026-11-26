# 2026-10-10 reconciliation — version-level enumeration supersedes the "additional concept families" reading

## What changed

Full version enumeration (`GET /api/records?q=conceptrecid:<id>&all_versions=true&size=25`)
was run for all eleven concept families after the 01 record was pushed. Results:

- Every fixed object exposes exactly **three versions** in one concept family
  (2026-09-16 baseline / 2026-09-30 natural-month-close / 2026-10-04 v2026.10),
  plus the audit runtime with two versions (beta + v2026.10-initial-research-runtime).
- **Record 23068494 (RS07) and record 23068352 (RS10) are NOT independent concept
  families** — the concept-family search returns both as members of the canonical
  single family for each object. The 01 record's
  `additional_independent_concept_families` section is **withdrawn**.

## The actual mechanism (working model, pending convergence)

Per-version stats fields are **not always in lockstep**:

- 10 of 11 families show all versions with identical family-aggregated values
  (`UNIFORM`) — e.g. RS01 216/135 across all three versions.
- RS07 currently shows `SPLIT(2)`: baseline 85/82, natural-month-close **186/106**,
  v2026.10 85/82. RS10 showed the same SPLIT earlier in the day (23068352 at
  105/101 while siblings were 210/129) and has since **converged to UNIFORM 210/129**.

Working model: Zenodo aggregates view events into per-record counters and a
family-level aggregation pass periodically re-synchronises all member versions to
the same family value. A SPLIT is a **mid-aggregation state**, and the intraday
~100-view steps observed across repositories are aggregation passes completing
per family — not external behavioural events.

Consequences for interpretation:

- The canonical one-value-per-object reading (concept request → latest version
  stats) remains valid **after** a family's aggregation pass; for a family in
  SPLIT state the concept request returns the latest version's stale value
  (RS07 currently 85, understating its family total).
- RS07's true family total is not yet observable; it becomes fixed when the
  family converges (bounded below by 85, and by max(previous split values) on
  re-synchronisation).
- Unique-view semantics are unchanged: per-family deduplicated counters,
  cross-version/cross-family deduplication not performed.

## Verification data

Version-level enumeration retained in the collection scratch space and
summarised here. Per-family UNIFORM/SPLIT state at capture time:

| Object | versions | state | split values |
| --- | --- | --- | --- |
| RS01-RS06, RS08-RS10, AUDIT | 3 / 2 | UNIFORM | — |
| RS07 | 3 | SPLIT(2) | 85/82 vs 186/106 |

## Follow-ups

- Re-check RS07 family convergence before the next scheduled observation.
- 01 record is preserved as pushed (source preserved in Git history); this
  reconciliation file is the resolution contract per monitoring/NAMING.md.
- ZENODO-METHOD pairing-rule section updated out-of-repo to match this model.
