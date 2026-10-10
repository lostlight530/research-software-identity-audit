# User-supplied October 10 Zenodo counting guide — source-account summary

**Source identity:** user's 2026-10-11 Asia/Shanghai conversation message with declared data cutoff `2026-10-10 23:54 Asia/Shanghai`. This is a **faithful structured summary of user-reported values and method**, NOT a Zenodo original response, and is NOT the independent verifier's collection. Exact message transport timestamp and unmodified original message bytes were not exported in this repository update.

## User's objects and reported method

- Researcher `lightlost`, ORCID `0009-0001-3617-0832`; ten fixed research software objects, three versions each: September 16 baseline, September 30 month-close, October 4 production-framework.
- Separate control repository `research-software-identity-audit`, conceptrecid `23166490`, **three** version IDs: `23166491` (beta), `23176748` (initial runtime), `23284570` (new `v2026.10-evidence-reconciliation`).
- Search `/api/records?q=conceptrecid:<id>&allversions=true&size=20`, cross-check `/api/records/<version-id>/versions`, read each version's `version_views`, `version_unique_views`, `version_downloads`, `version_unique_downloads`, and reported family `views/unique_views/downloads/unique_downloads`; sum version views/downloads only; compare attached family fields; do not add unique counts across versions.
- User advised cache-busting query parameter and HTTP `Cache-Control: no-cache`, explicit Beijing retrieval timestamps, and retrying HTTP 504 or non-JSON responses. The separate verifier's extraction interface did **not** permit verifying a custom outbound Cache-Control request header.
- Distinguish Zenodo downloads from GitHub clones and concept DOIs from version DOIs.

## User-reported point-in-time totals

| Reported time (Asia/Shanghai) | Fixed ten views | Fixed ten downloads | Control views | Control downloads | Descriptive combined views | Provenance |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 2026-10-10 22:35 | 1924 | 7 | 51 | 0 | 1975 | User-supplied earlier version-by-version reading; reported cross-record agreement |
| 2026-10-10 23:54 | 1933 | 8 | 74 | 3 | 2007 | User-supplied later version-by-version reading; **subsequent** public API verification `2026-10-11 00:26–00:28` numerically matched |

**22:35 version-view subtotals (user report):** baseline 1532; month-close 287; October edition 105, total 1924.

**23:54 reported change from 22:35:** `welcome-to-github` family views 216 → 225 (+9), downloads 4 → 5 (+1); its baseline version views 174 → 177 (+3), October version views 13 → 19 (+6), month-close unchanged 29. Control family views 51 → 74 (+23), downloads 0 → 3 (+3), with beta 21 views, initial-runtime 53 views/3 downloads and the new edition 0 views/0 downloads. The user reports no changes in the other nine fixed families. Combined downloads as a derived display total = 8+3 = **11**.

**User-reported 23:54 family unique view / unique download fields:** fixed-ten `welcome 144/4, frontier 129/1, Axiom 123/0, China 119/0, epistemic 115/0, foundations 108/1, zero 104/0, sci 104/1, reflective 85/0, auto 91/0`; control `71/3`. These were separately re-read later as attached family fields, not deduplicated across software objects.

**Historical sequence supplied by user:** Sep 30 `120 views/2 downloads` (user-supplied, not first direct audit); Oct 4 `518/7` (reported first measured); Oct 5 `545`; Oct 6 `618`; Oct 7 `695`; Oct 8 `776`; Oct 9 `840`; Oct 10 at 10:38 `1088`, 14:49 `1393`, 17:39 `1497`, 19:52 `1706`, 22:11 `1813`, 22:35 `1924`, 23:54 `1933`. The user's description notes early dates **did not enumerate all versions**, so the sequence is not reclassified into a single fully version-audited historical dataset.

**User-reported exploratory event heuristic:** a software family receives `>= 50` additional views with `0` additional Zenodo downloads in a comparable interval; reported ten ~100-view jumps on October 10 with activity concentrated on baseline versions. Threshold is **post hoc, exploratory**; per-version event-by-event attribution, exact visitor identities and referrer channels are not independently established by this source summary.

**RS07 user correction:** at Oct 10 ~22:11, month-close record `23068494` attached `stats.views=186` while local version views summed to `85`; at 22:35, user says RS07 local version views `150+34+12=196` and attached family views had converged to 196. This resolves **observed counter agreement at the later time**, not internal-cause identification.

Do not alter this user-reported historical source summary to match later changing Zenodo API counters. For later direct verification, see [verification.md](verification.md).
