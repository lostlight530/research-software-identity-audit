# First-day-to-current research-control repository naming, classification and OSF governance reconciliation — 2026-11-03

> **Audit class:** pinned retrospective GitHub source-history and path-governance review with explicitly appended later corrections. **Not** a historical raw-platform recapture, a new formal prospective timepoint, a study-contract amendment, a new GitHub Release, a new DOI, or an OSF-account edit.
>
> **Pinned pre-audit main:** [`b6aa40231bcba62da98e089673652839952118cf`](https://github.com/lostlight530/research-software-identity-audit/commit/b6aa40231bcba62da98e089673652839952118cf), committed **2026-11-03T03:14:42Z**; the inventory created on this branch is **outside the pinned inventory by definition**. All dates and CSV rows must be read at their source granularity.

## 1. Complete inspectable current-tree and reachable-main snapshots

- **Repository creation:** `2026-10-05T14:59:45Z`, after separate OSF registration (`2026-10-05T14:04:13Z`)
- **First reachable main commit:** [`e5ba0a0e7dc548bd5bd3e79b4d7fc0cb95e528aa`](https://github.com/lostlight530/research-software-identity-audit/commit/e5ba0a0e7dc548bd5bd3e79b4d7fc0cb95e528aa), `2026-10-05T14:59:46Z`; original first tree contains only `README.md`
- GitHub connected recursive tree at the pinned main commit: `truncated=false`, **620 tracked blobs** and **142 tree directories** (762 returned tree elements)
- Reachable `main` commit pages 1–2 (`100+4`) at pinned commit: **104 commits**. [All 104 SHAs, author/committer clocks, parent count, subject and source locator](research-control-main-commit-chronology-2026-11-03.csv); this counts the full reachable set returned by the GitHub commit-list endpoint, not only first-parent merges, unrelated branches or original platform observations
- [All 620 pinned file paths, original Git blob SHA, reported byte size, owner, path-derived semantic/temporal category and rename disposition](research-control-file-ownership-snapshot-2026-11-03.csv). A path-level class is **not** proof that all 620 file bodies were manually inspected or every externally sourced value independently replayed
- [All 58 pinned dated monitoring event directories and 20 evidence companions](research-control-dated-event-classification-2026-11-03.csv), with recorded machine-file variant, stable slug and semantic limits. This new audit's subsequent November 3 **02** event is outside the pinned 58-event snapshot

### Owner distribution at pinned source

| Owner | File count | Correct authority class |
| --- | ---: | --- |
| Root | 17 | Governance, license and software citation |
| `.github/` | 7 | Repository CI and collaboration infrastructure |
| `contract/` | 4 | OSF research contract **mapping**, not independently frozen OSF bytes |
| `corpus/` | 1 | Canonical fixed RS01–RS10 manifest |
| `baseline/` | 10 | Historical baseline, no prospective conversion |
| `schema/` | 5 | Six-layer/seven-platform machine contract |
| `schedule/` | 1 | Operational scheduling; **no declared concrete offsets** |
| `monitoring/` | 287 | Dated diagnostics, retrospectively reconciled records, check/coverage indices |
| `evidence/` | 221 | Source/evidence custody and selected-field projections with mixed authenticity granularity |
| `observations/` | 2 | Prospective **directory guides only**; no scheduled observation records |
| `provenance/` | 2 | Provenance and correction discipline |
| `analysis/` | 3 | Descriptive method and explicitly exploratory analysis code |
| `scholarly/` | 11 | Citation, DOI and archive identity controls |
| `templates/` | 11 | Blank templates, never completed studies |
| `tools/` | 14 | Validators / offline verification tools |
| `tests/` | 3 | Synthetic checker tests, not real platform experiments |
| `docs/` | 21 | Dated navigation and retrospective history reports |
| **Total** | **620** | **Fixed ten software objects, not 620 research units** |

### Dated-event naming diagnostics

At the pinned source, all **58** `monitoring/YYYY-MM-DD/NN-lowercase-kebab/` event paths satisfy the date/event pattern, are consecutively numbered within each source-date folder, and contain `README.md`. All **20** dated `evidence/` event directories have a matching `monitoring/` parent record and their own entrypoint. **57** monitoring events include exactly one normal `record.yaml` or `record.json`; one explicit **offline replay only** event has no machine observation record. No new fictional observation should be produced to eliminate this deliberate exception.

This is **structure validation**, not independent proof of 58 source-origin retrievals or correct historical timestamps.

## 2. Historical names and categories requiring explicit correction / retention

| Existing path or name | Proper classification and forward-facing label | Decision |
| --- | --- | --- |
| `monitoring/2026-10-06/01-wave-01/` | **Pre-eligibility diagnostic / legacy source wave label**; `wave` is not a preregistered prospective wave | **Preserve path/contents/Git blobs**, add alias in complete catalog, do not silently rename sealed evidence |
| `monitoring/2026-10-24/03-offline-family-stat-replay/` | Existing offline validator/replay, **not** a newly sampled measurement | Keep README-only documented exception; do not invent `record.json` |
| `record.yaml` vs `record.json` | Both established, accepted **machine-summary format variants** | Keep pre-existing serialization; one event = one machine summary, no cosmetic conversion |
| `monitoring/2026-11-02/01-complete-institutional-recheck/source-attempts.csv` column `platform` | Actually **numeric surface IDs 1–34**, not seven operational platform names | Preserve original file and digest; add derived 482-row **surface ID / surface name** join separately in [dated November 3 reconciliation](../monitoring/2026-11-03/02-source-attempt-surface-id-reconciliation/README.md) |
| Legacy RS06–RS10 label/display-order confusion | Canonical IDs come solely from [current fixed corpus manifest](../corpus/object-manifest.csv), **RS06 auto-doc-engine, RS07 epistemic-pipeline, RS08 sci-render-kit, RS09 china-agentic-observatory, RS10 agentic-frontier-observatory** | Retain [October 6 source correction](../baseline/2026-10-05/correction-object-id-mapping-2026-10-06.md) and original Codex record; normalize derived interpretation, never rewrite raw attribution |
| Historical path `canonical-current-field-extracts.json` | Name records *collector's bounded historical viewpoint*, not live always-current truth | Preserve dated path, do not auto-rename just because a filename contains `current` |
| Earlier dated inventories (Oct 21 / 28 / 31) | Valid independent **point-in-time snapshots** with 300/437/499 pinned tracked files at their respective bases; today's base has 620 | Preserve source cutoff and do **not** edit earlier files so every report falsely reports today's totals |
| `OSF 5b329` original + approved `344-83` revision | Two independently versioned OSF Schema Responses, one changed exploratory field among 29 compared | Use [canonical version-governance crosswalk](../contract/osf-registration-version-governance-2026-11-03.md), not an overwritten original registration or false primary preregistration |

**Disposition:** no demonstrated need to physically rename or relocate all 620 already-compliant current files. A bulk move would break published path references, artifact-manifest hashes, Git source identity, public links and historical evidence custody while providing no new scientific validity. The complete table now explicitly records **each file's naming/preservation decision** so future genuine defects can be repaired selectively and append-only.

## 3. OSF registration authority, including approved revision

The authoritative [original and approved OSF Schema Response crosswalk](../contract/osf-registration-version-governance-2026-11-03.md) distinguishes registration `5b329`, original response `6ac3ae5e6da32e3d0576ed72`, approved revision `6ac4c12fed97b8b77ce88a9c`, mutable associated project `wa5v8`, and separately created GitHub control runtime.

The [retained field diff](../monitoring/2026-10-30/01-osf-schema-response-version-reconciliation/field-diff.json) reports **29 compared fields, 28 unchanged, one changed `344-83` (Other planned analysis)**. Later family-benchmark/engagement/rank examples are **exploratory/post hoc, not initial preregistered primary analyses**. No OSF account mutation or additional revision is performed or claimed in this GitHub task.

**Study design remains:** fixed RS01–RS10; six preregistered layers; 60 object-layer units **per eligible scheduled timepoint**; seven operational platforms, 70 potential object-platform checks (not 70 analytic units); historical baseline separate from prospective; no imputation, causal inference or composite score. The schedule still has **no concretely declared offsets**, so all existing diagnostics and this audit add **0** prospective cells.

## 4. Real correction made during this full-history governance pass

The [November 3 normalized surface-ID repair](../monitoring/2026-11-03/02-source-attempt-surface-id-reconciliation/README.md) implements the November 2 source-ledger correction without mutating the original attempt file. Two pinned Git blobs provide the 482 original attempts and 34 surface labels. The derived output retains **482 / 482** rows with **zero unmatched IDs**; it explicitly separates `source_attempt_key`, numeric `surface_id`, `surface_name`, and any mapped core operational platform from 34 supplementary/standards surfaces. Derived execution time is **November 3**, while the original retrieval clocks remain November 2; they must not be conflated.

No other historical defect has been asserted corrected merely because the file inventory is complete. Where only path names were inspected, the catalog says so. No CI status is predeclared; use the actual PR / post-merge workflow receipts.

## 5. Rule for all further renaming, migration, normalization and correction

1. **First identify authority, object and phase:** OSF original / later approved response, GitHub tracked source, historical baseline, selected diagnostic/extractor, original byte evidence, derived field, exploration, template or actual prospective observation
2. **Use canonical IDs and maintain source identity:** RS01–RS10 are fixed. CONTROL and supplementary projects are outside the sample. A DOI or Release cannot silently create a new object
3. **Check path rules before moving:** only proven misowned/misnamed mutable files should be moved. For already cited historical paths, prefer a current index alias or a dated correction instead of rewriting old source bytes
4. **If moving a file is really required:** record original path, original Git blob SHA, new path, exact byte-preservation/correction policy, references, change timestamp and migration map; update **only** affected mutable links/manifests under their own contract and document every unavoidable hash change
5. **Never convert evidence type by appearance:** a `record.json` summary is not an original HTTP body, a successful source query is not independent adoption, an unresolved 404 is not global absence, a current endpoint is not a historical source timestamp
6. **Keep statistical units separate:** 60 per eligible timepoint vs 70 potential platform checks vs 34 supplementary URLs vs 620 source files vs 104 Git commits
7. **Use PR/CI verification with bounded claims:** self-review exact diff, run actual checker, respect advisory guards, squash merge only when mergeable and controls are acceptable, then verify new main and post-merge CI

## 6. Evidence, scope and work remaining

- Original first-day repo tree and current pinned GitHub recursive tree were read via authenticated GitHub connector; historical commit list paginated `100+4`, every current tracked path with Git blob identity was cataloged
- The **complete original Git object tree at the pinned main** was inventoried, not every unreachable branch, closed PR discussion, untracked local file, historical deleted path or third-party platform response body
- The 620-row inventory is **path-based classification**, not a certification that each file's scientific claims have been independently verified. Source/role mismatches discovered later need an explicit correction record, not a retroactive all-green assertion
- Current OSF original/revision public extractor representations carried older UTC-day acquisition clocks; the retained October 30 field diff remains the specific evidence. No fresh OSF admin read/write or OSF-approved revision is claimed here
- No new Release, tag, DOI, OSF revision, formal observation, platform or sample was created by the audit

**Outcome:** `HISTORICAL_TREE_CLASSIFIED_620` + `MAIN_REACHABLE_CHRONOLOGY_104` + `DATED_EVENT_TAXONOMY_58` + `OSF_ORIGINAL_REVISION_MAPPED` + `DERIVED_LEDGER_FIELD_CORRECTED_482` + `BULK_RENAME_NOT_JUSTIFIED` + `NO_PROSPECTIVE_CELLS`.
