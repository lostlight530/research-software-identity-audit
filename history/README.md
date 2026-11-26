# Historical archive

**One historical landing zone.** This directory consolidates the former root-level diagnostic and evidence trees together with dated repository documentation and pinned repository inventories. Nothing under `history/` is a live monitor, an active acquisition queue, or a prospective dataset.

## Archive map

| Area | Former location | Contents | Boundary |
|---|---|---|---|
| [`diagnostics/`](diagnostics/README.md) | root `monitoring/` | 419 migrated source files (including the byte-preserved source index) plus one new navigation index across 85 event directories in 43 date folders, 2026-10-06–2026-11-22 | Historical diagnostic and pre-eligibility records; no new acquisitions |
| [`evidence/`](evidence/README.md) | root `evidence/` | 347 migrated source files (including the byte-preserved source index) plus one new navigation index across 36 event directories in 22 date folders, 2026-10-08–2026-11-22 | Historical source, projection, manifest and reconciliation packages; no new acquisitions |
| [`documentation/`](documentation/README.md) | `docs/history/` | 35 migrated documents, the byte-preserved source-era naming policy, and a new current index | Historical repository documentation, not current authority |
| [`repository-inventory/`](repository-inventory/README.md) | `docs/repository-inventory/` | 66 migrated inventory files plus one new current index (six pinned packages, 2026-11-06 through 2026-11-20) | Point-in-time Git tree inventories, not current HEAD metrics |
| [`migrations/`](migrations/README.md) | Prior migration ledgers and this consolidation | Append-only old-path → new-path records with Git blob identities | Path custody only; not source revalidation |
| [`catalogs/`](catalogs/README.md) | Historical role catalog | 768-row filename-based inventory of the former root `monitoring/` and `evidence/` files | Filename classification only; not a semantic audit |

## What remains outside this archive

- `baseline/` remains the canonical frozen Study 1 baseline at its established root path; it is not folded into the generic diagnostic/evidence archive
- `contract/`, `corpus/`, `schema/` and `schedule/` remain Study 1's established contract/runtime surfaces
- `provenance/` remains the active cross-cutting provenance policy and correction discipline
- Current daily Study 1 material belongs under `studies/osf-wa5v8/dayN/`; Study 2 material belongs under `studies/osf-vshwk/`
- Only protocol-eligible prospective observations may enter `observations/raw/`; archive paths never imply eligibility

## Migration guarantees

The 2026-11-26 consolidation relocates 871 original tracked paths. Every migrated destination reuses the exact source Git blob SHA recorded in the [file-by-file migration ledger](migrations/path-migration-2026-11-26.csv). The former `monitoring/README.md`, `evidence/README.md`, `docs/history/README.md`, and `monitoring/NAMING.md` are preserved byte-for-byte as explicitly named `*.source.md` files. New archive indexes and `docs/record-path-conventions.md` are additive navigation/governance documents; they do not replace or rewrite source-era content.

The older [October 8 evidence-path migration](migrations/monitoring-path-migration-2026-10-08.csv) and [November 25 documentation migration](migrations/path-migration-2026-11-25.csv) remain preserved as historical records. They describe their own source commits and migration scopes; this consolidation does not rewrite their earlier claims.

**Do not add new records to `history/` merely because they are non-prospective.** New operational diagnostics must remain in their owning study workspace, and prospective eligibility must be established independently under the frozen contract.
