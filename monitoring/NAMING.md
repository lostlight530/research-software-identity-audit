# Naming and path migration (2026-10-08)

This document is a **repository presentation-path convention**, not an OSF preregistration amendment.

## Record paths

- Monitoring: `monitoring/YYYY-MM-DD/NN-<event-slug>/`
- Retained evidence: `evidence/YYYY-MM-DD/NN-<event-slug>/`
- `YYYY-MM-DD` = declared observation/capture date, **not** ingestion time.
- `NN` = ordering within the day, **not** a prospective wave index.
- Lowercase kebab-case for project directories and research record filenames.
- Preserve standard ecosystem filenames, Python `snake_case.py`, and established fixed corpus identifiers.
- Do not use `latest`, `current`, or `final` as canonical long-lived **path-state markers**.
- A source's original self-label (such as "Wave 3 final") is still retained **inside the historical record**, not promoted to contract authority.

## Record file roles

| Canonical name | Role |
| --- | --- |
| `README.md` | Human-readable entrypoint to the record |
| `record.yaml` | Normalized, bounded machine summary |
| `source.md`, `source-01-*.md` | Preserved source identity and claims |
| `verification.md` | Independent verifier's procedure and outcomes |
| `reconciliation.md` | Correction/addendum interpretation, source preserved in Git history |
| `capture-summary.json` | Derived retained-capture counters and scope |
| `*-statistics.csv`, `*-delta.csv`, `*-routes.csv` | Domain-specific tabular products |
| `capture-manifest.json` | Endpoints, capture timestamps, status, and raw-response digests |
| `artifact-manifest.json` | Public package paths and their expected byte digests |
| `raw-responses.tar.gz` | Byte-preserved compressed raw response evidence |
| `offline-verification.json` | Retained local verification report, **not** a GitHub runner result |

## Preservation and traceability

This migration relocates 33 tracked paths; every old path and its **original Git blob SHA** appears in [path-migration-2026-10-08.csv](path-migration-2026-10-08.csv).

- Source records that are only renamed reuse their exact Git blobs.
- Captured response archive bytes, archive member filenames, source response manifests, and canonical DOI/RS identity values remain unchanged.
- A small number of README/derived documentation and machine locator strings change **only** for internal links and paths. The migration ledger marks them.
- `artifact-manifest.json` is updated to bind the same retained artifact identities to their new paths; changed presentation files receive new SHA-256 digests. This is not a recapture.
- `offline-verification.json` preserves the previously run local checker report. It does not assert that the migration itself reran the checker.
- Historical prose in source records may mention old filenames; the mapping is the resolution contract. Do not silently change original source narratives.
- The original local names inside `raw-responses.tar.gz` include obsolete RS display mappings and are intentionally left intact. Derived CSV uses `corpus/object-manifest.csv`.

**Research semantics unchanged:** 10 fixed objects; 6 layers/60 object-layer units; 7 concrete platforms/70 possible checks; baseline cutoff; pre-eligibility classification; no RS11; no prospective promotion.

The existing `tools/check.py` remains the advisory GitHub CI check. `tools/check_retained_morning_evidence.py` remains an explicitly **local/offline** verifier and is not added to cloud CI.

## October 24 compatibility clarification — forward naming contract

An audit of the *current checked-out tree* found 35 dated monitoring event directories and 11 dated evidence event directories. They use the same `YYYY-MM-DD/NN-lowercase-kebab-slug` envelope. The independently retained evidence companion of an event may deliberately reuse the **same** `NN-slug` under `evidence/`: this is **one event with two owning surfaces**, not duplicate observations and not a second event ordinal.

### File role names and historical preservation

- `README.md` is the human-facing navigation entrypoint for each dated monitoring or evidence event directory. Legacy packages that once lacked it may receive **additive entrypoints only** without recapturing or changing their original metadata.
- `record.yaml` is the established normalized summary name for earlier historical monitoring events. Later retained monitoring packages may use **`record.json`** for a structured machine summary instead. They are accepted format variants with the same role, **not two simultaneous observation records**. Prefer the established variant within an event package; do not convert historical serialized artifacts solely for visual uniformity.
- An explicitly **offline replay-only** directory (currently `2026-10-24/03-offline-family-stat-replay`) may contain `README.md` without either record file: it validates existing retained source fields and is **not** a fresh measurement.
- `source.md`, `verification.md` and `reconciliation.md` remain preferred generic role names. More specific historical filenames (for example `independent-reconciliation.md`, `verification-outcome.md`, and `zenodo-query-shape-reconciliation-2026-10-24.md`) are retained with their existing links and attribution; they do **not** redefine a new competing canonical state.
- A term such as `current` within a frozen descriptive file title (for example `canonical-current-field-extracts.json`) can denote the *original author's time-bounded field selection*. It does **not** mean the file is a continuously refreshed authoritative `latest` snapshot. No long-lived directory may be named by a moving `latest/current/final` state marker.
- `2026-10-06/01-wave-01` is a **historical label preserved by the original migration**. Its `pre_eligibility_monitoring` classification takes precedence over the word `wave`; it is not an eligible prospective wave. Do not silently rename it and break its migrated Git-blob provenance.

### Scope / identity / chronology rules

1. The date folder represents the event's **declared source observation/capture date**, not the later ingest, review, PR merge or CI date. Record actual retrieval and source clocks separately; do not backdate a fresh API read into an older event folder
2. `NN` is unique and consecutive **within the `monitoring` day** in the present repository; `evidence/` can use a subset of matching `NN-slug` companions. Neither number implies a scheduled prospective time point
3. Route scientific diagnostic and retrospective state to `monitoring/`, source byte/projection packages to `evidence/`, actual preregistered observation cells **only** to `observations/` after verified eligibility, independent cross-cutting provenance to `provenance/`, generic methodology and navigation to `docs/` or the designated contract/tool surface
4. The OSF preregistration, RS01–RS10, six analytical layers, seven operational platforms, frozen baseline and undeclared concrete schedule are not affected by this path convention. CONTROL and PILOT are not new sample IDs
5. Historical path changes require a **separate old-path → new-path map and original Git blob identities**. Do not rename published evidence or mutate capture manifests for cosmetic consistency. Reclassification is explicit and append-only
6. The local checker `python -B tools/check_record_paths.py` validates dated event envelopes, entrypoints, normal machine-record variants, documented offline-only exception, monitoring index coverage and evidence/monitoring companions. It checks **structure, not source validity or scientific truth**

## November 3 first-day-to-current classification and derived-column correction (forward rule)

The [dated full-history classification](../docs/research-control-first-day-to-current-governance-audit-2026-11-03.md) pins **104 reachable main commits / 620 pre-audit tracked files / 58 dated monitoring event directories / 20 dated evidence companions** to main `b6aa40231bcba62da98e089673652839952118cf`. These are snapshots, **not** continuously refreshed counts or a study denominator. The complete [file owner/name/temporal-policy index](../docs/research-control-file-ownership-snapshot-2026-11-03.csv) is path-level evidence and must not be cited as a manual body/content audit of every file.

**Forward naming and semantic normalization:**

- A valid historical path must **not** be moved simply to make an old record's slug match today's preferred terminology. For `2026-10-06/01-wave-01`, the current display/semantic alias is **pre-eligibility diagnostic**, retaining the old Git path/bytes rather than pretending it was a preregistered prospective timepoint
- Every new `monitoring/YYYY-MM-DD/NN-kebab-case/` event must carry an entrypoint and a machine summary **unless** separately declared as a true offline replay-only exception with no new measurement; record.yaml/record.json are accepted historical variants, not competing observation units
- The capture date path, original source retrieval timestamp, derived compilation timestamp, Git commit time and OSF study event date are independent provenance fields. A later correction always gives its **real** later clock
- The November 2 source ledger uses `platform` for numeric **34-surface IDs**. The [November 3 482-row derived normalization](2026-11-03/02-source-attempt-surface-id-reconciliation/README.md) joins it to surface labels without rewriting historical CSV or promoting 34 surfaces into 34 new preregistered platforms. New *derived* ledgers must instead use explicit `surface_id`, `surface_name` and optional separate `operational_platform`
- Research sample RS01–RS10, the independent CONTROL runtime, supplementary software and OSF registration are separate identities; platform counts, repository commits, software versions and file counts must never be renamed as the **60** object-layer denominator
- Current citation/contract documentation may add an alias/index to an older source; actual historical-source relocation requires original path/blob mapping, linked references, audit of manifest/hash impact, and an explicit later correction. No silent delete/rename of original evidence, version tags, DOI objects or OSF revisions

This rule is forward-looking repository governance, **not** a post hoc amendment to the originally registered study or evidence of new prospective observation cells.
