# Record path and ownership conventions

This document governs repository presentation paths. It does **not** amend either OSF registration or change the scientific contract.

## Current execution and evidence surfaces

| Surface | Current path | Ownership |
|---|---|---|
| Study 1 daily diagnostic work | `studies/osf-wa5v8/dayN/monitoring/YYYY-MM-DD/NN-event/` | Day-scoped operational diagnostics; each day has its own index |
| Study 1 daily retained evidence | `studies/osf-wa5v8/dayN/evidence/YYYY-MM-DD/NN-event/` | Evidence packages belonging to that Study 1 day |
| Study 2 cycles | `studies/osf-vshwk/cycles/cycle-YYYY-MM-DD-pst-NN/` | Independent event/review-initiated cycle contract and evidence |
| Eligible prospective raw observations | `observations/raw/` | Only records satisfying the frozen OSF eligibility and schedule contract |
| Derived observations | `observations/derived/` | Reproducible derivations linked to eligible raw observations |
| Cross-cutting provenance | `provenance/` | Active provenance, source attribution and correction policy |

Study 1 daily folders are navigation/operational workspaces, not automatically scheduled prospective timepoints. Study 2's cycle folders follow its separate approved event- or documented-review-initiated protocol. A date label or directory name never substitutes for an actual source retrieval timestamp or eligibility determination.

## Historical archive paths — no new acquisitions

| Historical path | Former path | Meaning |
|---|---|---|
| `history/diagnostics/YYYY-MM-DD/NN-event/` | root `monitoring/YYYY-MM-DD/NN-event/` | Retained pre-eligibility, diagnostic and retrospective records |
| `history/evidence/YYYY-MM-DD/NN-event/` | root `evidence/YYYY-MM-DD/NN-event/` | Retained source-response, projection, manifest and reconciliation packages |
| `history/documentation/` | `docs/history/` | Dated repository audits, governance and method reviews |
| `history/repository-inventory/` | `docs/repository-inventory/` | Pinned point-in-time repository inventories |

These locations are frozen archive surfaces. Do not create a new daily capture under `history/diagnostics/` or `history/evidence/`. Current Study 1 daily material belongs under its `studies/osf-wa5v8/dayN/` scope; Study 2 records belong under `studies/osf-vshwk/`. The root `baseline/` remains the canonical frozen historical baseline and is intentionally not merged into the generic archive.

## Event naming and file roles

- `YYYY-MM-DD` is the declared source observation/capture date, **not** ingestion, review, PR merge or CI time
- `NN` orders event packages within the owning day; it is **not** a prospective wave or analytical unit
- Use lowercase kebab-case for event slugs and research record filenames
- Do not use `latest`, `current` or `final` as canonical long-lived path-state markers
- Preserve an original source's self-label inside its source record; do not promote a label such as “Wave 3 final” into contract authority

| Canonical name | Role |
|---|---|
| `README.md` | Human-readable record entrypoint |
| `record.yaml` / `record.json` | Bounded machine summary; do not keep competing machine summaries in one event |
| `source.md`, `source-01-*.md` | Preserved source identity and claims |
| `verification.md` | Independent verifier's procedure and outcomes |
| `reconciliation.md` | Attributed correction/addendum; preserve the source record |
| `capture-summary.json` | Derived retained-capture counters and scope |
| `*-statistics.csv`, `*-delta.csv`, `*-routes.csv` | Domain-specific tabular products |
| `capture-manifest.json` | Endpoints, capture timestamps, status and raw-response digests |
| `artifact-manifest.json` | Published package paths and expected byte digests |
| `raw-responses.tar.gz` | Byte-preserved compressed raw-response evidence |
| `offline-verification.json` | Local verification report, not a GitHub runner result |

Historical `record.yaml` and `record.json` variants remain accepted. An explicitly offline replay-only directory may have a README without a machine record if it creates no new measurement. Do not convert or rename historical serialized artifacts for visual uniformity.

## Provenance and migration rules

1. Keep source observation date, actual retrieval timestamp, derived compilation timestamp, Git commit time and OSF study event date as independent provenance fields
2. Do not backdate a fresh API read into an older event directory
3. Preserve original source bytes, source identity, retrieval clocks, response conditions, digests and correction history
4. A historical path change requires an append-only old-path → new-path map and original Git blob identities
5. Historical path strings inside old records, inventories and artifact manifests remain source assertions. Resolve them through the migration map or an explicit compatibility resolver; do not silently rewrite original records
6. A Git blob proves source-byte custody at a Git revision, not independent platform authenticity or scientific validity

The [October 8 path migration](../history/migrations/monitoring-path-migration-2026-10-08.csv) and [November 26 archive consolidation](../history/migrations/path-migration-2026-11-26.csv) preserve their respective path/identity mappings. The earlier [November 25 documentation migration](../history/migrations/path-migration-2026-11-25.csv) remains a historical record.

## Research boundary

The path convention does not change RS01–RS10, the six analytical infrastructure layers, the seven operational platforms, the 60 preregistered object-layer units, the 70 possible platform checks, the frozen baseline cutoff, or either OSF registration. CONTROL is not RS11. A directory, checker pass, source response or GitHub path does not establish prospective eligibility.
