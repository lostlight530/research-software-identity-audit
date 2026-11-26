# Historical documentation — classified physical archive

This directory contains **relocated historical repository-control reports**, not ongoing Study 1 or Study 2 research execution. The two approved OSF studies remain separately governed under [`studies/`](../../studies/README.md). Dated reporting, audit counts, and historical source views retain their original as-of provenance.

## Categories

- [`inventory-ledgers/`](inventory-ledgers/) — Git path/blob inventories, commit and PR ledgers, governance and lifecycle snapshots
- [`method-and-integrity-reviews/`](method-and-integrity-reviews/) — dated semantic/path/integrity assurance notes and local preflights
- [`diagnostic-and-closeout-reviews/`](diagnostic-and-closeout-reviews/) — bounded platform snapshots, correction notes, and research-session closeouts

## Existing dated monitoring and evidence records

**Source commit:** `264c051aae27fdfbf5b344b502a7bcaedfccae3e` (before this path-classification PR). Git blob SHA values in the file-role index are explicitly pinned to that source tree; the link-rebased `monitoring/README.md` has a new blob on this PR branch, while all 767 other listed legacy files retain the original blobs.

The [retained-file role index](../catalogs/legacy-monitoring-evidence-file-roles-2026-11-25.csv) classifies **all 768 then-tracked paths** across legacy `monitoring/` (421) and `evidence/` (347), preserving original paths and Git blob SHAs. This is a **file-role inventory inferred from filenames**, not a review of scientific content, proof of successful provider acquisition, formal observation eligibility, or a new sample. Values classified `other_*` are intentionally not assigned invented meanings.

These already date/event-scoped source packages remain in their original locations because validators, sealed manifests, historical references, and external deep links depend on their paths. The docs move below is a separate, explicitly enumerated relocation.

## Preserved history and migration

- [Exact file-by-file migration map](../migrations/path-migration-2026-11-25.csv) records each former flat path, its new classified path, and the **original Git blob SHA**
- CSV and JSON source snapshots moved **byte-identically**, reusing their original Git blobs
- Markdown reports were only adjusted where necessary to rebase Markdown **relative hyperlinks** after relocation; their original Git blobs remain available through the recorded SHA and source Git history. No scientific conclusions, event clocks, denominators, or data values were reinterpreted
- References from current navigation must point to the new paths; historical source-path mentions in dated inventories continue to describe the historical tree they actually audited
- `docs/repository-inventory/YYYY-MM-DD/` is already dated and grouped, so this migration does not reshuffle its separately pinned inventory packages
- `monitoring/`, `evidence/`, `baseline/`, `contract/`, `schedule/`, `schema/` and `studies/` are intentionally **not migrated by this documentation-only change**: their existing source paths, validators, and evidence or protocol ownership require independent checking

This index does not assert a new acquisition, protocol amendment, or prospective observation.
