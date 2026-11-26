# November 3 derived correction of November 2 source-attempt surface IDs

**Class:** non-destructive, retrospective derived schema/column semantics correction; **not** recapture, new provider-origin request, scheduled prospective observation, amendment, change to historical source bytes, or new platform/analytic unit

## Verified defect and correct join

The original [November 2 attempt ledger](../../2026-11-02/01-complete-institutional-recheck/source-attempts.csv) has a header `attempt_id,platform,scope,...`. Its `platform` column holds **numeric 1–34 institutional/service/standard surface IDs**, **not** actual operational platform strings. This is already documented in the [November 2 correction](../../2026-11-02/01-complete-institutional-recheck/source-attempts-column-reconciliation.md). Original CSV is intentionally **unchanged** because it participates in historical source references and artifact digests.

This follow-up executes the documented one-to-one normalization using the same historical [34-row source dictionary](../../2026-11-02/01-complete-institutional-recheck/platform-results.csv) and produces [482 derived rows](source-attempts-derived-surface-join.csv), preserving original attempt keys and numeric source values with explicit new `derived_surface_id`, `derived_surface_name`, `operational_platform_if_core` and the non-equivalence of supplementary surfaces.

- Original attempt ledger Git blob: `536a64c8db0c3da31a363776103d769e591a297b`
- Original surface dictionary Git blob: `458141a5bf6f66eda15082497441d2033a0d6275`
- Source rows: **482**; dictionary entries: **34**; derived rows: **482**; missing surface-ID joins: **0**
- Derived at client UTC `2026-11-03T03:27:55.293Z`, not at the November 2 original HTTP retrieval clocks
- Core platform label joining is **surface mapping only**, not proof that the source query was a fresh complete check of that platform
- No lost/failed attempt is filtered; no HTTP status, URL, clock or source digest is imputed

Machine-readable [normalization record](record.json) contains mapping and provenance. This package is a correction to **downstream interpretation**, not evidence that provider responses have changed. It does not modify 10 × 6 = 60 object-layer units, the seven operational platforms, OSF versions, original baseline or the undeclared prospective schedule.
