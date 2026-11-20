# First day through November 20 — research-control tracked-file and history classification

**Audit class:** pinned GitHub source/history and file-ownership reconciliation, not source-provider recapture, code execution across all past environments, historical source re-interpretation or a prospective study timepoint

## Exact source and scope

- Pinned CONTROL `main`: [`5bbdd7ecc0f0513e7f9857f87e4539abd58f9c58`](https://github.com/lostlight530/research-software-identity-audit/commit/5bbdd7ecc0f0513e7f9857f87e4539abd58f9c58) after [November 19 evidence custody reconciliation](source-branch-custody-reconciliation.md)
- Git tree: `7bcbe08a4a100b7d68b9f76df944885b23ab9f0e` with `truncated=false`
- Catalog compilation (UTC): `2026-11-20T00:24:19.494Z`
- First reachable `main` commit: [`e5ba0a0e7dc548bd5bd3e79b4d7fc0cb95e528aa`](https://github.com/lostlight530/research-software-identity-audit/commit/e5ba0a0e7dc548bd5bd3e79b4d7fc0cb95e528aa), `2026-10-05T14:59:46Z` UTC; first commit tree contained exactly `README.md`
- Current pinned **903 tracked Git blobs**, **211 tree directories**, **1114 tree entries**
- Main ancestry **158 commits**, oldest first in [chronology](main-reachable-commits.csv)
- **83 monitoring** dated event directories and **34 evidence companion** directories; event path taxonomy in [dated-event-classification.csv](dated-event-classification.csv)
- **17 owning groups** in the full [path, blob SHA and byte-size catalog](current-main-tracked-file-catalog.csv)
- This document and the accompanying catalog/ledger are created **after** the source pin and are excluded by design; subsequent commits may update main but do not retroactively change the source snapshot

## What was reviewed

1. Original OSF registration `2026-10-05`, subsequent approved October 6 response, and GitHub live contract/schema/schedule ownership remain distinct
2. Ten fixed sample objects RS01–RS10 from `corpus/object-manifest.csv`; the independent CONTROL source/Zenodo/Digital Object identity does not create RS11
3. The current tracked tree is enumerated **path by path**: 2026-10-05 first commit through the pinned November 20 main, with exact Git blob SHA-1 and byte sizes
4. All reachable **main** commits are enumerated with Git author/committer times. Branch-only commits are excluded, but the imported November 19 source Git commit is linked separately below
5. Every dated monitoring event has a path-based format/entrypoint/evidence-companion classification; the offline-only event is retained rather than supplied with a fictional observation
6. Historical reports from October 21 (300 files/71 commits), October 28 (437/87), November 3 (620/104), November 5 (637/110) and November 6 cross-repository 8,802-blob inventory are **preserved under their original source pins**, not edited to match today's total
7. The [November 19 source branch main-custody gap](source-branch-custody-reconciliation.md) was closed in PR #132 by importing 74 original Git blobs and two additive indexes, while preserving 01 source path-reuse correction and all original digest files

## File owners and research authority

| Owner | Tracked files at pinned source | Meaning |
| --- | ---: | --- |
| `.github` | 8 | repository-owned files |
| `analysis` | 3 | repository-owned files |
| `baseline` | 10 | repository-owned files |
| `contract` | 5 | repository mapping; frozen authority stays OSF |
| `corpus` | 1 | fixed ten sample manifest |
| `docs` | 66 | historical interpretations and navigation |
| `evidence` | 318 | origin/selected/derived evidence with independent provenance limits |
| `monitoring` | 411 | dated diagnostic only |
| `observations` | 2 | guides, not automatically scheduled prospective data |
| `provenance` | 2 | repository-owned files |
| `ROOT` | 19 | repository-owned files |
| `schedule` | 1 | repository-owned files |
| `schema` | 5 | machine taxonomy and counting |
| `scholarly` | 12 | repository-owned files |
| `templates` | 11 | repository-owned files |
| `tests` | 8 | repository-owned files |
| `tools` | 21 | repository-owned files |
| **TOTAL** | **903** | Tracked files, not observations |

## Naming and correction decisions

**NO_BULK_RENAME / NO_SOURCE_REWRITE.** Dated files with legacy `wave` labels or corrected source ID classifications retain their exact published paths, source timestamps, Git SHA and correction notes. Renaming all files would break existing evidence references and archived digests without increasing scientific verifiability

- Old `2026-10-06/01-wave-01` is *pre-eligibility diagnostic* despite its legacy name
- `2026-10-24/03-offline-family-stat-replay` is the intentional machine-record exception, not a missing prospective observation
- `2026-11-19/01` path reuse is retained with [explicit correction history](../../../monitoring/2026-11-19/03-web-assisted-surface-review/correction-history.md); the later `02` capture and `03`–`05` reconciliations stay distinct
- Source-branch import into `main` happened later than the original source runs; its Git merge clock does **not** redefine provider capture clocks

## Contract boundary

Original [OSF registration](https://osf.io/5b329), its [approved version reconciliation](../../../contract/osf-registration-version-governance-2026-11-03.md), [counting rules](../../../schema/counting-rules.md), and [schedule](../../../schedule/README.md) are authoritative in their respective scopes. **10 × 6 = 60** object-layer units per eligible timepoint; **10 × 7 = 70** possible platform checks are not substituted. The schedule has no declared concrete offsets. No new scheduled prospective observations are inferred from historical diagnostic source paths or current Git activity.

## Validation and limits

GitHub recursive tree and commit list were retrieved at pinned source; rows are machine-generated from exact Git returned paths, blob SHA, size, Git commit metadata, and path conventions. **This is not a line-by-line semantic audit of 903 files**, and the historical reachability ledger is not the complete universe of all previously created branches, deleted paths, unpublished source bytes or provider HTTP responses. A Git blob is source-byte custody, not independent platform authenticity. Existing checker/manifest CI must be independently inspected before merging these artifacts.

**Outcome:** `PATH_INVENTORY_903` / `REACHABLE_MAIN_COMMITS_158` / `EVENT_TAXONOMY_83` / `NO_BULK_REWRITE` / `NO_NEW_PROSPECTIVE_CELLS`

## Additive current diagnostic (not a new historical file pin)

The separate [November 20 source-bounded review](../../../monitoring/2026-11-20/01-firstday-to-current-infrastructure-diagnostic/README.md) appends current version-counter and seven-platform checks **after** the pinned `5bbdd7ecc0f0513e7f9857f87e4539abd58f9c58` tree. Its files therefore are **not** counted among the original 903 blobs / 158 commits / 83 dated events. The additional records have their own true retrieval windows; this audit intentionally does not recast their creation date as the historical source date.
