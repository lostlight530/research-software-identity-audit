# CONTROL-only first-day-to-November-10 file governance and cleanup disposition

> **Audit class:** Pinned GitHub repository tree/history and deterministic path-role reconciliation, not research-data recapture, a new OSF preregistration revision, an eligible prospective observation, a software release, or a new DOI
>
> **Pinned source main:** [`fb3822101505ce761c6ea6be4df07952fd3aa86d`](https://github.com/lostlight530/research-software-identity-audit/commit/fb3822101505ce761c6ea6be4df07952fd3aa86d) — latest included commit 2026-11-10T13:11:33Z
>
> **Audit assembled at:** 2026-11-10T14:51:18.883Z (UTC); live API requests are not an atomic source-platform capture
>
> **Scope:** `lostlight530/research-software-identity-audit` only — **CONTROL**, never `RS11`

## Complete current-tree identity and continuity

| Check | Pinned result and limits |
| --- | --- |
| First commit | [`e5ba0a0e7dc548bd5bd3e79b4d7fc0cb95e528aa`](https://github.com/lostlight530/research-software-identity-audit/commit/e5ba0a0e7dc548bd5bd3e79b4d7fc0cb95e528aa) (2026-10-05T14:59:46Z), original README-only bootstrap |
| Reachable main commits | **135** GitHub API records, pages of 100 and 35, through this exact pinned head |
| Prior source-history continuity | All **110** earlier November 5 chronology SHAs and **20** November 8 additive chronology SHAs resolve in the 135 current reachable commits |
| Historical PRs | **106**: **105 merged**, **1 closed without merge** (#16), **0 open** at inventory retrieval |
| Current tracked blob paths | **724** in an untruncated recursive Git tree, see [complete path/SHA/size/role catalog](control-tracked-paths.csv) |
| Previous pinned snapshot | [November 8: 703 paths / 130 commits](../2026-11-08/README.md), pinned to [`b0ae26c88ff393740d9233b7a71be4f50e3d48f7`](https://github.com/lostlight530/research-software-identity-audit/commit/b0ae26c88ff393740d9233b7a71be4f50e3d48f7) |
| Exact 703-path continuity | **703/703** earlier catalog path/blob SHA/byte sizes verified against its own pinned Git tree, without rewriting that table |
| November 8 → current delta | **21 added / 2 modified / 0 removed** relative to the November 8 pinned *pre-audit* commit, see [per-path delta](control-delta-since-2026-11-08.csv); **5** additive commits, see [commit ledger](main-commits-since-2026-11-08.csv) |
| Exact same-blob candidates | **12 groups / 26 path occurrences**, unchanged from the older candidate set; see [review ledger](control-identical-blob-review.csv) |
| Conventional transient generated files | **0 filename matches** in the 724-path tree for caches, compiled Python bytecode, common build directories, editor swaps or temporary/backup suffixes |

This provides exhaustive **tracked-file path and Git-object identity coverage**, *not* a 724-file line-by-line source-content or scientific validity review, an audit of unreachable commits, private or untracked workstation files, or a replay of raw third-party HTTP bytes

## Role classification of all 724 pinned tracked files

- `DATED_DIAGNOSTIC_MONITORING`: **291**
- `GITHUB_AUTOMATION`: **7**
- `HISTORICAL_AUDIT_OR_CORRECTION`: **73**
- `HISTORICAL_BASELINE`: **7**
- `RESEARCH_CONTRACT_RUNTIME_OR_DOCUMENTATION`: **91**
- `RETAINED_SOURCE_EVIDENCE`: **235**
- `ROOT_GOVERNANCE_AND_SCHOLARLY_METADATA`: **17**
- `TESTS`: **3**

Classification reuses all 703 prior classifications after exact path/blob identity verification and classifies the 21 additions by established directory owner; these are **path-role decisions**, not semantic equivalence claims

## Rename, consolidation and disposal decision

- **Actual historical data/evidence renames: 0; historical deletes: 0; payload merges: 0**. They would modify stable locators or destroy independent dated event context without a proven disposable target
- **Verified same-blob duplicates: 12 / 26**, unchanged from November 8. The source event ID, capture clock, manifest link and source-vs-derived role are distinct even where file bytes match. Every occurrence remains `REVIEW_REQUIRED_NO_DELETE` until an evidence-backed, per-item disposition is recorded
- **Not garbage:** `baseline/`, `contract/`, `schedule/`, `schema/`, `monitoring/`, `evidence/`, `provenance/`, dated inventory snapshots, corrections, documented failed attempts, `raw-responses.tar.gz`, and `observations/` placeholders
- **Consolidation actually safe now:** one canonical navigation pointer in `docs/README.md` to this latest pinned inventory; retain older dated inventories as independently reproducible immutable *as-of* reports instead of rolling them into an untraceable living count
- **Future byproducts:** the accompanying narrowly scoped `.gitignore` excludes Python bytecode, common test/type-check caches, local virtualenv and OS finder artifacts, **not** research JSON/CSV/Markdown, captured archives or logs

No current tracked file was shown to be safely disposable by this source evidence. A future proposal to move or remove a candidate must provide original Git blob identity, inbound/outbound references, hash-manifest scope, owner contract, and a migration/correction record. Existing Git history remains immutable; a Git path deletion alone would not delete historical commits

## Research contract and limitations

- The OSF [registration 5b329](https://osf.io/5b329/overview) remains the separately frozen research authority; its prior versioning caveat is [already documented](../../../contract/osf-registration-version-governance-2026-11-03.md). A public web view being blocked does not authorize reconstructed claims about unseen OSF fields
- Exactly **RS01–RS10** and six preregistered layers remain the corpus and analytical contract: **60 object-layer cells per eligible declared point**. Seven operational platforms yield **70 possible platform checks**, *not* 70 preregistered cells
- `schedule/README.md` contains no frozen numeric time offsets. This housekeeping produces **zero prospective observations**, no new release, tag or DOI
- Hash equality is a byte identity condition; it is not source independence, redundant scientific meaning, or a deletion license
- The GitHub API current-path inventory does not establish historical source-origin HTTP payload authenticity, scholarly-platform indexing, scientific results, or current OSF API contents
- No attempt was made to inspect/download all 724 file bodies. Explicit review state: **`PATH_AND_OBJECT_IDENTITY_AUDITED / SEMANTIC_CONTENT_REVIEW_PARTIAL / NO_SAFE_TRACKED_DELETION_CONFIRMED`**

## Verification plan and outcome boundary

Pre-commit checks from connected GitHub API: exact trees `truncated=false`, historical catalog 703/703 join, main chronology 135 plus previous 130-SHA coverage, 106 PR states, 724-path role classification sum, 21/2/0 delta, duplicate candidate path continuity and zero matching common transient filenames

The source records and older dated snapshots are byte-identical to the pinned input tree on this maintenance branch. The actual PR validation, advisory test steps and post-merge `main` must be separately checked before stating that delivery succeeded. Advisory CI does not authenticate scientific claims or independently replay source-provider responses
