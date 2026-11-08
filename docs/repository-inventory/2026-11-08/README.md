# CONTROL-only first-day-to-November-8 file governance closeout

**Scope:** `lostlight530/research-software-identity-audit` only — **CONTROL, never RS11**. No RS01–RS10 repository was modified, indexed or audited in this maintenance change.

**Classification:** retrospective Git object/path inventory and documentary governance reconciliation, **not** research-source recapture, a prospective observation, an OSF amendment, a release, or a DOI.

**Pinned pre-maintenance main:** [`b0ae26c88ff393740d9233b7a71be4f50e3d48f7`](https://github.com/lostlight530/research-software-identity-audit/commit/b0ae26c88ff393740d9233b7a71be4f50e3d48f7); the current-tree contents and all comparisons below refer to this immutable point-in-time snapshot, **not to the branch after this new inventory is committed**. This inventory was compiled from authenticated GitHub REST reads. The GitHub endpoints were retrieved sequentially/in parallel, not as an atomic repository-wide transaction.

## Verified continuity and exact counts

| Check | Pinned result | Interpretation |
| --- | ---: | --- |
| Initial main commit | [`e5ba0a0e7dc548bd5bd3e79b4d7fc0cb95e528aa`](https://github.com/lostlight530/research-software-identity-audit/commit/e5ba0a0e7dc548bd5bd3e79b4d7fc0cb95e528aa) | 2026-10-05 14:59:46 UTC |
| Initial commit tracked files | **1** | `README.md`; it still exists, though its content has evolved |
| Main-reachable commits through pinned source | **130** | 110 in the [Nov 5 historical ledger](../../research-control-main-history-through-2026-11-05.csv) and **20 verified additions** in [this additive delta](main-commits-since-2026-11-05.csv); 110/110 old SHAs were found in the current reachable set |
| Historical PRs | **101** | 100 merged, 1 closed-unmerged, zero open at this check; PR status is a *separate* lifecycle object from Git commits |
| Current tracked file path/blob identities | **703** | Full recursive Git Tree `truncated=false`; [complete 703-row catalog](control-tracked-paths.csv) |
| [Nov 6 pinned CONTROL tree](../2026-11-06/control-research-software-identity-audit-tracked-paths.csv) | **657** | Older source commit `44b3defa6a67cf0eb45b6519fc8245827731c7a6`; do not retrospectively overwrite it |
| Nov 6 → pinned Nov 8 tree delta | **46 added / 6 changed / 0 removed paths** | [Exact paths and old/new Git blob IDs](control-delta-since-2026-11-06.csv); changes are source-tree identity changes, not the number of newly created research units |
| Exact identical Git blob groups in current tree | **12 groups / 26 paths** | [Separate candidate ledger](control-identical-blob-review.csv); all `REVIEW_REQUIRED_NO_DELETE` |

This is exhaustive *current tracked path-and-Git-object identity coverage*. It is **not** complete per-blob scientific body reading, a semantic deduplication decision, a full commit-by-commit content replay of every historical revision, an inventory of unreachable branches/untracked files, or an origin HTTP-response replay. For that reason `CONTENT_REVIEW_PARTIAL` remains correct.

## Classification and naming disposition

All **703** pinned current paths received a documented classification; **0** remain in `UNCLASSIFIED_REVIEW_REQUIRED` in this snapshot.

The original Nov 6 deterministic path catalog used the intentionally unresolved `OTHER_OR_REVIEW_REQUIRED` for three root files. Based on their canonical role, **only the new derived inventory classification** resolves these:

- `.gitattributes` — repository-wide file/line-ending governance
- `.zenodo.json` — scholarly archival metadata
- `RESEARCH_TEMPLATE.md` — human-facing canonical research template

All three are now classified `ROOT_GOVERNANCE_AND_SCHOLARLY_METADATA`, but **their path, blob SHA and bytes are left intact**. This is a derived file-role correction, not a rewrite of the historical Nov 6 table.

The 46 newly present paths follow established repository-native owners: 9 dated/docs inventory or governance files, 23 retained `evidence/` files, and 14 dated `monitoring/` files. No new top-level authority bucket or alternative naming scheme is introduced.

Existing historical labels such as `01-wave-01`, `record.yaml` / `record.json`, source-hash names, original raw artifacts, sidecars and corrections are preserved. `monitoring/NAMING.md` and the existing path/ownership checker remain the governing naming and projection controls. **No bulk rename, delete, move, forced reclassification of old observations, or format conversion** is justified.

### Classification totals at the pinned 703-file main

- `DATED_DIAGNOSTIC_MONITORING`: 277
- `GITHUB_AUTOMATION`: 7
- `HISTORICAL_AUDIT_OR_CORRECTION`: 68
- `HISTORICAL_BASELINE`: 7
- `RESEARCH_CONTRACT_RUNTIME_OR_DOCUMENTATION`: 91
- `RETAINED_SOURCE_EVIDENCE`: 233
- `ROOT_GOVERNANCE_AND_SCHOLARLY_METADATA`: 17
- `TESTS`: 3

The summed category counts equal **703**. This classification is reproducible from exact path strings and the Git-tree blob IDs. It must not be represented as 703 qualitative content reviews.

## Identical blobs, retained provenance and candidate dispositions

The **12 identical-Git-blob groups / 26 path entries** contain separate dated captures, comparisons, offline verification, and/or machine-summary roles. Identical bytes may be a legitimate `NO_CHANGE` result or a copied artifact; the Git hash alone cannot distinguish these.

All 26 candidate path occurrences are marked `REVIEW_REQUIRED_NO_DELETE`. Nothing was renamed or deleted. A future individual candidate requires content review, owning-contract review, inbound/outbound reference and manifest checks, and a logged `KEEP | SUPERSEDED_BUT_RETAIN | ALIAS | MOVE_WITH_MIGRATION | DELETE_CONFIRMED` decision before any destructive write.

## Contract, assurance and preservation boundaries

- Original OSF Registration [5b329](https://osf.io/5b329/overview), its separately approved Oct 6 exploratory wording revision, original baseline, existing amendment/deviation history and research evidence are unchanged.
- Fixed RS01–RS10 stay at six preregistered layers / **60 object-layer units** per eligible scheduled point. CONTROL remains an independent execution and provenance repository, **not RS11**. Seven operational platforms imply 70 possible platform checks, **not** 70 research units.
- `schedule/README.md` still lacks concrete offsets; this file-governance change creates **0 prospective cells**.
- Previous historical snapshots, raw source packages and their byte hashes are not silently changed. A current Git API response is not evidence of a past OSF or platform state.
- Published Zenodo versions, Tags, all DOI identities and external OSF storage/wiki remain untouched.
- The [Nov 7 correction](../../../monitoring/2026-11-07/01-periodic-identity-infrastructure-recheck/reconciliation.md) retains the initial checker failure and subsequent repair. Green CI is not a scientific content audit.

**Maintenance disposition:** `CONTROL_ONLY_FULL_CURRENT_TREE_IDENTITY_AUDITED`; `HISTORY_CONTINUITY_130_COMMITS`; `CLASSIFICATION_703_PATHS_0_UNCLASSIFIED`; `EXACT_BLOB_DUPLICATE_REVIEW_12_GROUPS_KEEP`; `CONTENT_REVIEW_PARTIAL`; `NO_BULK_RENAME_OR_DELETE`; `NO_FROZEN_CONTRACT_CHANGE`; `NO_NEW_PROSPECTIVE_CELLS`.

This snapshot is a source-of-record for *its pinned source commit*. Later changes should use a new dated delta rather than editing this historical record in place. PR, CI and post-merge main evidence must be checked against their actual GitHub states; their outcomes are not preclaimed here.
