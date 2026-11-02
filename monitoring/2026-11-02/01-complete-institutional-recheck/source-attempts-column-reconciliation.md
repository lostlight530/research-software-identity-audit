# November 2 source-attempt ledger column-semantic reconciliation

**Scope:** documentation correction for the already committed diagnostic package only, not a new request, research observation, amended contract, or overwrite of original evidence.

## Identified field-label mismatch

The published [source-attempt ledger](source-attempts.csv) has this header:

`attempt_id,platform,scope,locator,retrieval_batch_start_utc,retrieval_batch_end_utc,http_status,response_sha256,response_bytes,error`

The column named `platform` contains **numeric surface-row IDs** (for example `datacite,18,...`), not platform strings like `datacite`. Surface 18 in the [34-row result](platform-results.csv) is **DataCite**; the first column of that result identifies the surface ID. Similarly, `attempt_id` contains request/attempt keys, not necessarily canonical platform names. A consumer must not group by `source-attempts.csv:platform` as though it held seven operational platform identifiers.

## Correct interpretation for this dated package

- Interpret `source-attempts.csv:platform` as `surface_id`, linked to the **`surface`** column in `platform-results.csv`; retain the original header unchanged for exact artifact-manifest digest validation
- Interpret `attempt_id` as an **attempt key**; the linked surface label is the `name` field of `platform-results.csv` (not automatically the OSF operational-platform vocabulary)
- Surface IDs 1–34 include supplementary directories, resolvers, standards and research services; they are **not** 34 institutions, 34 preregistered layers or 34 independent research objects
- The two retrieval columns are client-side attempt brackets, not provider event timestamps; retained failures and null HTTP statuses are not converted to absence
- The historical source CSV, its byte length/SHA-256, raw attempt values, earlier interpretation and original artifact manifest are **not edited** by this note

## Downstream machine-consumption rule

For a normalized **derived** table, use explicit columns `surface_id` and `surface_name` after a verified one-to-one join from the source ledger's numeric `platform` field to `platform-results.csv:surface`. Preserve the original raw column name separately (e.g. `source_column=platform`) and keep the join method and exact input references. Do not silently rename the source file or fabricate extra original response fields.

This is an append-only correction of a **schema-label interpretation**, not evidence of an external platform behavior change. The study stays at RS01–RS10, six layers, 60 planned units per eligible timepoint; this diagnostic package adds zero prospective cells.

**Source basis:** `monitoring/2026-11-02/01-complete-institutional-recheck/source-attempts.csv`, `platform-results.csv`, `record.json`, and `evidence/2026-11-02/01-complete-institutional-recheck/artifact-manifest.json` on main commit `3240ba90bcff79b89a6155c30dbc80a4f5eb5e62`.
