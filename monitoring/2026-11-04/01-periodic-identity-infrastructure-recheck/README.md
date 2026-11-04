# November 4 bounded identity and infrastructure patrol

**Classification:** append-only, source-bounded diagnostic monitoring, **not** a scheduled prospective observation, full contemporary DOI census, OSF amendment, source-origin byte archive, or new software publication

**Date:** 2026-11-04 Asia/Shanghai. Acquisition is not atomic: independently queried connected-GitHub API state, public-content extractor results, and older reference packages have different clocks. Tool-provided `acquired_at` for public extraction is truncated to the **start of a UTC day**, not an origin HTTP request time. Original HTTP response bodies/headers and cryptographic origin digests are **not retained**. Tool receipt IDs, source locators, state and errors are preserved in this package

## Contract and comparison

- [Original OSF registration](https://osf.io/5b329/overview) is frozen; the [dated original/revised Schema Response reconciliation](../../../contract/osf-registration-version-governance-2026-11-03.md) found 29 compared fields with one changed later-approved exploratory field `344-83`, not a new primary analysis
- [Fixed manifest](../../../corpus/object-manifest.csv): RS01–RS10 = ten samples, CONTROL excluded; six layers and **60** object-layer units per eligible scheduled timepoint, seven operational platforms and **70 possible checks**, not 70 research units
- [Schedule](../../../schedule/README.md) still has no declared concrete offsets. The October 14 fixed-ten release cohort does not retroactively make monitoring records scheduled prospective cells. This patrol adds **0 prospective cells**
- Source comparators: [November 3 bounded patrol](../../2026-11-03/01-bounded-identity-infrastructure-recheck/README.md), [November 2 full institutional diagnostic](../../2026-11-02/01-complete-institutional-recheck/README.md), and [November 2 all-version Zenodo measurement](../../2026-11-02/02-all-version-recheck/README.md). Distinguish source date, extract acquisition day and this new review's compilation clock

## Connected GitHub observations

- [11-head ledger](github-main-heads.csv) retains exact main SHAs relative to the **November 3 source-read completion envelope at 2026-11-03T03:09:19.860Z (11:09:19 Beijing), not a verified November 3 day-end state**, and the [November 3 prior ledger](../../2026-11-03/01-bounded-identity-infrastructure-recheck/github-main-deltas.csv) comparison: RS01 advanced two commits, RS02 advanced one; RS03–RS10 stayed at the previous recorded SHAs. Relative to November 3's earlier **pre-patrol** CONTROL `c12c56bf`, main has three completed review/correction commits; relative to the **last separately verified November 3 control commit** `b00f4fa` (committed 2026-11-03T03:40:45Z; **not** a proven end-of-day capture), CONTROL is unchanged
- At the bounded read, there are **two open core PRs**, RS01 #901 (Parallax Daily) and RS02 #792 (Ballast Daily); CONTROL and the other eight samples have zero open PRs. Do not merge or modify the separate daily producer PRs from this research patrol
- The 10 sample release lists still show five published releases each and the latest tag `v2026.10-30-evidence-snapshot`; CONTROL shows five releases with latest `v2026.10-control-lifecycle-reconciliation`. Main commits are not release/DOI events
- Prior CONTROL main `b00f4fa` advisory [validation run 41573633210](https://github.com/lostlight530/research-software-identity-audit/actions/runs/41573633210) is completed/success; no claim that all 11 repositories' CI or independent scientific replay was executed

## Seven platforms and 34 previously established surfaces

- [Exact 34 representative URL accesses](surface-access-recheck.csv) retain extraction, error, acquisition-day and source locator for each **surface ID**; these are 34 *service/standard rows*, not 34 separate institutional collaborators, 34 complete object censuses or 34 new operational platforms
- Selected current access succeeds for some URLs but many responses are cached from October. Seven-platform **live synchronous full coverage is PARTIAL/UNKNOWN**. Historical **90 attributable DOI identities**, **ORCID 17 groups / 106 work summaries**, **OpenAlex 32 author-filtered Works**, **OpenAIRE 88/90 attempted responses**, **57 Zenodo versions (50 fixed)**, **3,308 fixed-ten views and 17 downloads** remain *November 2* observations, **not** today's counters
- The same Zenodo RS01 latest-version record `23811380` returned the attached family fields **386 views / 7 downloads** with a 2026-11-04 UTC-day acquisition stamp; comparable November 2 baseline was **369 / 6**, thus **+17 / +1** as a *selected-field diagnostic interval*. A separate supplementary PILOT (outside the corpus) returned 22 / 6 versus 14 / 5, but neither is a prospective observation. Other family representations were predominantly older cached data: **do not compute a full 10-family aggregate change or negative deltas**
- The six URL errors are retained separately: ScreenIT/ASWG connect error, dkNET 404, InterLex 404, EDAM extraction error despite reported HTTP 200, Identifiers.org 404, N2T 403. Endpoint errors ≠ global absence; prior object-specific JSON paths on the same ecosystems may have been usable

## Independent upstream interactions

- RSE [PR #498](https://github.com/rseng/software/pull/498): **OPEN, unmerged, 0 reviews**, no new institutional intake established
- RSD [Issue #1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870): **CLOSED/completed** since October 16, without a new production-UI retest; [#1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871): **OPEN**. Latest published upstream release observed is `v6.7.5` (October 27). No change in this bounded status comparison
- RRID `SCR_029105` remains identifiable on older SciCrunch/RRID/NIF public extracts, but updated curator validation, ownership, actual adoption, formal affiliation and current 12-record RSD census remain **UNKNOWN**; the supplementary CONTROL software entry is not RS11

## Disposition and limitations

**`SELECTED_ZENODO_METRIC_DELTA` + `SOURCE_MAIN_DELTA_2` + `NO_NEW_FIXED_RELEASE` + `EXTERNAL_PARTIAL_UNKNOWN` + `NO_SCIENTIFIC_SOURCE_REPAIR_REQUIRED`**

No defect justifies editing the frozen contract, old baseline, historical HTTP attempts, already archived tags or DOI identifiers. This monitoring note is a bounded new observation receipt, **not** manufactured scientific progress or an additional study wave. Associated [machine summary](record.json) and [per-source ledger](surface-access-recheck.csv) make the access limits inspectable. No new Release or DOI is requested

## November 4 explicit clock-anchor correction

The original PR #88 derived ledger used `nov3_end_main_sha`, `ahead_since_nov3_end` and `fixed_main_changed_repos_from_nov3_end` for a **November 3 03:09:19.860Z source-read envelope**. Those historical labels incorrectly implied a day-end state; the 11/3 raw field values and 11/4 collected SHA/commit comparisons were not themselves wrong. The two CSV headers, one JSON key and the prose label are now corrected with explicit provenance, without modifying the underlying SHAs, commit counts, source records or earlier commits. Read the [dated clock-anchor correction note](clock-anchor-correction.md) before interpreting the source intervals. This is not a new capture, study wave or OSF amendment.
