# RSIA dated record classification and naming consistency — 2026-10-24

## Scope and authority

This is a **repository-structure and naming review**, not an observational study result, OSF amendment, external platform verification, new release or scientific conclusion. Audited `main` baseline: `5c64e157c26d848854e44d2845b5576b28a8bf00` (after PR #60). The scan read a complete, non-truncated Git tree of **458 entries**. This document reports the original scan and the bounded non-destructive repairs proposed here; completion must be confirmed by the actual branch CI and merge state

Authority: [OSF frozen research contract](../contract/preregistration.md), [corpus manifest](../corpus/object-manifest.csv), [contribution / provenance policy](../CONTRIBUTING.md), and [path convention](../monitoring/NAMING.md). This review does **not** reinterpret source material

## Classified owning surfaces

| Owner | Record class / role | Handling |
| --- | --- | --- |
| `contract/` / `corpus/` / `schema/` / `schedule/` | Frozen-OSF interpretation, RS01–RS10 identity, six analytical layers, seven operational platforms, dated operational declarations | No contract or sample mutation |
| `baseline/` | Historical/initial baseline, not a prospective wave | No rewrite |
| `monitoring/YYYY-MM-DD/NN-<slug>/` | Dated diagnostics, attempts, reconciliations, retrospective handoffs, offline checks | 35 existing event identities; README navigation + bounded machine records |
| `evidence/YYYY-MM-DD/NN-<slug>/` | Byte/projection/manifest evidence of the **corresponding** monitoring event | 11 existing companion identities; not 11 extra observations |
| `observations/raw/` / `observations/derived/` | Actual preregistered prospective observation records / source-linked derivations | README-only placeholders; none added here |
| `provenance/` | Cross-cutting source/correction lineage | Preserve original locators and independent review |
| `analysis/` / `scholarly/` | Bounded analysis and citation/identifier research | No silent status promotion |
| `docs/` / `tools/` / `.github/` | Guidance, deterministic verifiers and GitHub Actions | This report, path checker and advisory integration |

The **same date/ordinal/slug** appearing once under `monitoring/` and once under `evidence/` denotes two storage planes of a **single event**; it is not an ordinal collision. The monitoring event ordinals on October 24 are consecutively `01` through `05`

## Findings at baseline and bounded repairs

1. **Directory envelopes:** all **35** monitoring event paths and **11** evidence companion paths match the documented `YYYY-MM-DD/NN-kebab-slug` pattern. All 35 monitoring events already appear in the monitoring master index
2. **Missing entrypoints:** exactly **four** earlier packages lacked `README.md`: monitoring October 6 `01-wave-01`, `02-openaire-link-attempt`, `03-reconciliation`, and evidence October 10 `01-zenodo-surge-recheck`. This patch adds **only navigation README files** linking each pre-existing machine/source/interpretation or archived-capture file. No original payload, timestamp or index number is changed
3. **Machine-record representation:** historical packages use `record.yaml` and later packages use `record.json`, both existing role-compatible machine formats. There is **no justification for rewriting original serialized fields or file identities** solely to make the suffix uniform. The naming contract now explicitly documents both variants
4. **Documented exception:** `2026-10-24/03-offline-family-stat-replay/` has only a README because it replays retained fields with no new capture. Treating it as a missing observation record would manufacture data. The checker allows this **single explicit exception**
5. **Historical filenames:** `2026-10-06/01-wave-01` is a retained pre-eligibility source label, not an eligible scheduled observation. Specialized historical filenames such as `independent-reconciliation.md` and `verification-outcome.md` remain traceable instead of being erased for cosmetic uniformity. `canonical-current-field-extracts.json` is a **time-bounded descriptive extract**, not a continuously updating moving snapshot
6. **Protection against recurrence:** a small, offline, read-only `tools/check_record_paths.py` checks dated envelopes, complete entrypoints, YAML/JSON variants, declared offline exception, event ordering, master index coverage, and matching evidence companions. The workflow step remains expressly **advisory** and must be checked at step level

## Boundary of this review

No evidence path is relocated; the October 8 33-path migration record and historical Git blob SHAs remain authoritative for those moved paths. No old source narrative, evidence archive, original request, copied byte, identifier, observation, baseline, retrieval timestamp or public statistics are silently modified

No new prospective cells are created. The fixed ten RS objects, six layers, seven concrete platforms, 60 object-layer units per **eligible** scheduled point, separate research control and independent Life Science pilot remain unchanged. The repository has **not** declared actual preregistered schedule offsets through this patch

**Naming consistency here means a stable convention with explicit historical compatibility**, not forced byte-for-byte identical filenames for semantically different and already published records

For actual execution outcomes inspect [GitHub Actions](../.github/workflows/validate.yml) and the linked pull request, including whether the new advisory path step really executed successfully
