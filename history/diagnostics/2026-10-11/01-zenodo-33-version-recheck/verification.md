# Independent verification of the October 10 Zenodo reproduction guide

**Reviewer state:** `LIVE_VERSION_ENUMERATION_AND_ARITHMETIC_VERIFIED_WITH_HISTORICAL_PROVENANCE_LIMIT`.

**Direct public extraction, Asia/Shanghai:** 2026-10-11 00:26:47–00:28:10; all timestamps below are actual outer tool-call request intervals, **not** per-request server `Date` timestamps or raw byte HTTP captures. `allow_live_fetch=true` and unique `_cb` nonce parameters were supplied; the extractor could **not** set or reveal an actual `Cache-Control: no-cache` transport header. Cache-busting parameters cannot by themselves prove bypass of every intermediary cache.

## Verification actually performed

| Independent check | UTC tool window | Observed outcome |
| --- | --- | --- |
| All-concept search `GET /api/records?q=conceptrecid:<id>&allversions=true&size=20&_cb=...` | 2026-10-10 `16:26:47.773Z–16:26:58.798Z` | **11/11** concept searches returned valid JSON and three version records each |
| `GET /api/records/<latest-version-id>/versions?allversions=true&_cb=...` | 2026-10-10 `16:27:14.768Z–16:27:20.533Z` | **11/11** version-list endpoints had `hits.total=3`, three matching version IDs and consistent `conceptrecid` |
| `GET /api/records/<version-id>?_cb=...` | batch A `16:27:51.602Z–16:28:01.015Z`; batch B `16:28:01.015Z–16:28:10.508Z` | **33/33** direct version JSON reads successful; source `id` and `conceptrecid` matches |
| Attached `stats.views` / `stats.downloads` compared against summed `stats.version_views` / `stats.version_downloads` | Derived from direct reads | **11/11 family sums match all three attached family counters**, across 33 records |
| Attached `stats.unique_views` and `stats.unique_downloads` agreement across sibling records | Derived from direct reads | **11/11 families** had uniform attached unique fields; **NOT** global uniqueness across versions/objects |

**Machine-readable derived data:** [zenodo-version-statistics.csv](zenodo-version-statistics.csv) contains 33 original version record IDs, all eight per-record stat fields, exact source locator, concept, operational object identity, version index/tag and **outer** batch source window.

## Exact reproducible computation at this later observation

| Role | Versions | Version-summed views | Version-summed downloads | Scope |
| --- | ---: | ---: | ---: | --- |
| RS01–RS10 | 30 | **1933** | **8** | Fixed research sample: 10 software objects |
| Independent audit runtime | 3 | **74** | **3** | A different concept family for a study-control software; **not RS11** |
| Optional combined **display** | 33 | **2007** | **11** | Not a new analytical unit/denominator |

The full eleven object comparison (views / Zenodo downloads):

| Object | `version_views` baseline / month-close / October | Family views | Family unique views | Family downloads | Family unique downloads |
| --- | --- | ---: | ---: | ---: | ---: |
| RS01 `welcome-to-github` | 177 / 29 / 19 | 225 | 144 | 5 | 4 |
| RS02 `zero-entropy-lab` | 151 / 24 / 12 | 187 | 104 | 0 | 0 |
| RS03 `Axiom-0` | 169 / 31 / 5 | 205 | 123 | 0 | 0 |
| RS04 `reflective-continuum` | 145 / 14 / 6 | 165 | 85 | 0 | 0 |
| RS05 `agent-foundations` | 145 / 44 / 3 | 192 | 108 | 1 | 1 |
| RS06 `auto-doc-engine` | 142 / 20 / 9 | 171 | 91 | 0 | 0 |
| RS07 `epistemic-pipeline` | 150 / 34 / 12 | 196 | 115 | 0 | 0 |
| RS08 `sci-render-kit` | 154 / 21 / 7 | 182 | 104 | 1 | 1 |
| RS09 `china-agentic-observatory` | 148 / 33 / 19 | 200 | 119 | 0 | 0 |
| RS10 `agentic-frontier-observatory` | 154 / 37 / 19 | 210 | 129 | 1 | 1 |
| AUDIT control (`beta` / `initial-runtime` / `evidence-reconciliation`) | 21 / 53 / 0 | 74 | 71 | 3 | 3 |

**AUDIT new third Zenodo version:** `23284570`, under concept `23166490`. The independent GitHub release listing also verified tag `v2026.10-evidence-reconciliation`, published `2026-10-10T15:45:40Z` (23:45:40 Asia/Shanghai). Zenodo record `23284570` had `version_views=0` and `version_downloads=0` at this later read; this is a point-in-time counter, not a statement that no user has ever accessed any associated release material.

## Comparison with the user's October 10 guide and the earlier reviewer record

- User-supplied 2026-10-10 23:54 fixed ten `1933/8`, control `74/3`, combined views `2007`: **numerically reproduced at 2026-10-11 00:26–00:28**. This does **not** provide the original raw response as it existed on October 10 at 23:54.
- User-supplied 2026-10-10 22:35 `1924/7` and control `51/0`: internal arithmetic of user-supplied rows agrees; this earlier timestamp's per-version bytes were **not independently fetched at that time by this reviewer**. Current web API cannot retroactively supply them.
- Earlier October 10 independent [32-row review](../../2026-10-10/02-reconciliation/independent-version-verification.md) recorded RS07 `version_views=45+33+7=85` and one attached month-close aggregate `stats.views=186`. Here all three local views are `150+34+12=196`, each attached family `views=196`, and attached family `unique_views=115`. The **field mismatch is not present in this later observation**; its historical occurrence and primary cause remain separately retained as `HISTORIC_AGGREGATE_CONFLICT` and `MECHANISM_UNKNOWN`.
- The directly comparable RS07 version-local changes from the earlier 32-row extract to this new 33-row extract are `+105 baseline, +1 month-close, +5 October`. Accordingly, the bounded verified statement is **baseline-dominant** counter increases, **not** strictly zero activity on other versions.
- The proposed exploratory `delta views >= 50; delta downloads = 0` surge threshold is **post hoc** and requires **matching consecutive version-local captures** for precise version attribution. A historical family-only series (such as October 5–9) cannot be automatically promoted into a complete per-version interval experiment.
- Per the [Zenodo statistics FAQ](https://support.zenodo.org/help/en-gb/4-usage-statistics/15-what-is-a-view-download-data-volume), a unique view/download is de-duplicated in a **one-hour** time window, and human-or-machine events are counted subject to the platform's filtering. Do **not** use a `unique_views` field as a certified human count. The documentation does **not** by itself verify an exhaustive transport-level rule that all REST API/OAI-PMH requests under every deployment condition are excluded.
- Zenodo view/download totals are **time-varying statistics**. Independent reproducibility means the procedure and arithmetic are independently executable; recovering the **exact historic numeric snapshot** requires retained contemporaneous response evidence. A nonce/cache-bypass request is not a historical query parameter.

## Failure handling and evidence minimization

The guide's recommendation not to fabricate half-complete family totals is correct, but **do not delete partial success or failed attempts**: retain every available per-version response and attempt status, preserve HTTP 429/504/parse failures as `PARTIAL/UNRESOLVED/FAILED`, and withhold only a falsely complete family aggregate. Do not equate a 404 with global absence. This run had no error among the 11 family-search, 11 version-list or 33 direct record retrievals **as exposed by the extraction layer**.

## Limitations and authority

1. The public extraction tool did **not** expose unchanged original JSON response bytes, HTTP transport headers or individual completion times. The CSV is **derived field data**, not byte-level raw provenance. A direct controlled HTTP capture from a reproducibility-capable environment is still the appropriate next evidentiary improvement if byte-identical verification is required.
2. No independent source verifies the exact October 10 22:35/23:54 *retrieval transaction*, underlying visitor location/referrer, human/bot attribution, internal statistics aggregation schedule, or causal reasons for step changes. The numeric values are corroborated by a later direct read.
3. Control repository release `23284570` does **not** constitute an eligible **new fixed-corpus RS01–RS10 release** for the OSF prospective longitudinal dataset. The record remains `diagnostic_monitoring` with `prospective_dataset_member=false`.
4. The immutable research contract remains RS01–RS10, six infrastructure layers / 60 object-layer units per scheduled timepoint and seven operational platforms / 70 potential checks. The eleven concept families / 33 version records are this **supplementary** counter-audit granularity only.
5. No new release, tag, DOI, schedule, amendment, external account or prospective observation was created by this review.

**Verdict:** `LIVE_33_VERSION_RECHECK_MATCHES_USER_NUMERIC_REFERENCE; HISTORICAL_EXACT_REPLAY_NOT_ESTABLISHED; ACTOR_CAUSALITY_UNKNOWN`.
