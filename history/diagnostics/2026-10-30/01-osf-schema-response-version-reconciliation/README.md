# October 30 OSF Schema Response version reconciliation

**2026-10-30 (Asia/Shanghai)** · diagnostic evidence reconciliation · **not** a change to the registered OSF contract, an amendment, a scheduled observation, a prospective timepoint or a publication event

## Exact version identities and method

The public [OSF Registration `5b329`](https://osf.io/5b329/overview) has explicit API relationships `original_response`, `latest_response` and [`schema_responses` collection](https://api.osf.io/v2/registrations/5b329/schema_responses/). The following **two public Schema Response objects** were returned by that list and read using exact API URLs:

| Version | Exact API object | Version fields returned |
| --- | --- | --- |
| **Original** | [`6ac3ae5e6da32e3d0576ed72`](https://api.osf.io/v2/schema_responses/6ac3ae5e6da32e3d0576ed72/) | `is_original_response=true`, `reviews_state=approved`, `date_created=2026-10-05T14:04:14.757212Z`, `date_modified=2026-10-05T14:06:00.148012Z` |
| **Later approved revision** | [`6ac4c12fed97b8b77ce88a9c`](https://api.osf.io/v2/schema_responses/6ac4c12fed97b8b77ce88a9c/) | `is_original_response=false`, `reviews_state=approved`, `date_created=2026-10-06T09:36:47.653316Z`, `date_submitted=2026-10-06T09:58:52.719704Z`, `date_modified=2026-10-06T09:59:27.955055Z` |

**Evidence scope:** public JSON-formatted responses rendered by a **third-party public-content extractor** against the above official OSF API locators. We parsed the returned JSON and compared the complete `revision_responses` key/value mappings by structured equality, including empty strings/arrays. A second, differently named public-content extractor returned matching excerpts of the two version IDs, dates and revised field, but the two readers must **not** be represented as independent publisher sources or proof of bypassing caches.

**Client invocation envelope:** `2026-10-29T16:09:26.476Z`–`2026-10-29T16:09:29.810Z` (2026-10-30 00:09:26–00:09:29 Asia/Shanghai). It brackets one three-URL tool call, **not** three per-origin retrieval times, server publication timestamps, or individual source capture clocks. The report does not retain byte-identical origin HTTP response bodies, headers, signed fetch receipts or third-party cache freshness evidence. The [machine-readable selected-field comparison](field-diff.json) records each source locator, both version IDs, comparison scope, clock provenance and literal changed values; it is a **derived projection**, not raw response evidence.

## Difference actually established

- **2** Schema Response resources were returned by the list
- **29** original versus latest `revision_responses` field keys compared
- **28 identical values**, including the original RQ text, fixed sample/layer unit rules, primary measured and derived variables, analysis constraints, inclusion/exclusion and missing-data language
- **1 changed field:** `344-83`, labeled **Other planned analysis** in the previously supplied Overview

The original `344-83` allowed unexpected state transitions, new aggregation patterns, platform anomalies and similar secondary work, explicitly requiring **exploratory / post hoc** labeling. The later version made specific additional examples explicit: software concept-family contextual benchmarks, bounded sensitivity checks on platform engagement metrics, tie-aware rank/percentile summaries and other anomalies. Its own second paragraph continues requiring analyses introduced after original registration to remain **exploratory/post hoc**. The two exact public text values are in [`field-diff.json`](field-diff.json).

**Revision justification is a separate source statement:** the later Schema Response states: "Added links to supporting research materials and clarified their descriptions. No changes were made to the preregistered study design, hypotheses, sampling, or analysis plan." The actually compared `revision_responses` data changed **one exploratory analysis field**. Preserve both the author's statement and the structured field diff; do **not** treat the justification as proof of zero textual change. The version comparison does not independently audit added OSF resources or attachments.

## Contract resolution and non-resolution

This explicitly **resolves the previously unverified original-versus-updated wording for these 29 registration-response fields**, which the [October 8 Overview crosswalk](../../../contract/osf-overview-crosswalk-2026-10-08.md) had correctly left `UNVERIFIED` *as of that earlier review*. The crosswalk is not retroactively rewritten; the original text of `344-83` is now identifiable, and the later wording is not backdated into the original preregistration.

- The original preregistration remains the source of the primary **RS01–RS10 / six layers / 60 analytical units** contract. The seven operational platforms and 70 possible platform checks remain separate implementation concepts.
- Neither version establishes concrete T0/+24h/+72h/+7d offsets in the repo's [operational schedule](../../../schedule/README.md). Do not automatically treat an October 14 fixed-corpus release or this reconciliation as authorization for a scheduled prospective timepoint.
- A revision's `date_created`, `date_submitted`, `date_modified` and `reviews_state` are distinct fields. They are **not** exact evidence of when a specific paragraph first became visible to an observer. The enclosing registration's own modification clock is also a separate object clock.
- The observed difference concerns the **other/exploratory analysis response**. Benchmarking, percentile/rank or platform-engagement summaries must **not** be promoted into originally preregistered primary analyses on the basis of the later revision.
- No new platform records, research samples, denominator, derived scientific results, archived release, DOI, raw or prospective observation cells are created in this review.
- Original server-response byte integrity and the chronology of OSF resource links remain outside this comparison's evidence scope.

**Outcome:** `PARTIAL_VERIFIED_VERSION_DIFF` for the *specific OSF public Schema Response text fields*; `NO_CONCLUSION` for uncaptured origin HTTP bytes, resource-link revision history, full external seven-platform current states, or prospective-study eligibility. An OSF version update is a source event, **not** an amendment silently performed by this GitHub report.

This report and its machine-readable projection are new, append-only documentation. Earlier claims that the exact original-version wording was unknown remain valid **at their earlier retrieval date**, and their original records are preserved without overwrite.
