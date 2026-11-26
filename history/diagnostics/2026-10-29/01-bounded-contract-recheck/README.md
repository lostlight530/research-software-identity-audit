# October 29 bounded research-contract and public-source recheck

> **Explicit correction:** `batch_start_utc` and `batch_end_utc` in the original machine/CSV report are **unverified author-entered placeholders**, not captured request clocks. All 18 CSV clock bounds must not be used as timing evidence. See the [clock-provenance reconciliation](clock-provenance-correction.md); the original source is retained in PR #69 history.

**2026-10-29 (Asia/Shanghai)** · **diagnostic monitoring only** · not an OSF amendment, scheduled prospective observation, release, new DOI, or fresh seven-platform longitudinal census

## Authority and provenance

- Frozen research registration: [OSF 5b329](https://osf.io/5b329/overview), DOI `10.17605/OSF.IO/5B329`
- Exact repository base before this record: [`4cacb9b617d2e0383ffca8c757e66c5a44a5a793`](https://github.com/lostlight530/research-software-identity-audit/commit/4cacb9b617d2e0383ffca8c757e66c5a44a5a793); open PRs: **0**
- Dated source comparison: [October 27 bounded record](../../2026-10-27/01-bounded-seven-platform-recheck/README.md)
- Source attempt scope: **11** connected GitHub published-Release lists and **7** other operational platform access/extraction attempts, captured in [18-row source ledger](source-attempts.csv) and [machine summary](record.json)
- Observer clock envelope: `2026-10-28T16:47:37Z` to `2026-10-28T16:48:56Z` UTC, bracketed by local terminal clocks in this session. This is a **conservative client-side bracket**, not each HTTP request's timestamp or source's update/registration time. The calendar date is Beijing-local; UTC is still October 28.
- Neither response headers nor original third-party HTTP response bytes were retained. External extractor output was often **already acquired on October 27 or 28 UTC** and cannot certify a new October 29 source state. An optional query parameter `rsia_audit=20261029` changes the request URL but does **not** prove cache bypass.

## What the fresh GitHub connector directly returned

| Object scope | API finding | Claim boundary |
| --- | --- | --- |
| Fixed RS01–RS10 | All ten queried repository Release lists contained exactly **4 published Releases**; latest tag `v2026.10-fourteen-day-evidence-checkpoint` and respective published timestamps on **2026-10-14 UTC** | 40 returned published Releases are **not** 40 samples/DOIs and the query is not a full tags/drafts census |
| CONTROL | **4 published Releases**; latest `v2026.10-evidence-integrity` published `2026-10-18T04:38:57Z` | CONTROL is the research runtime, **not RS11** |
| Comparison to October 27 | Same bounded list counts, latest tags and published timestamps as the October 27 retained report | No observed difference **in these same API fields**; not a claim of no other repository or platform activity |

## Seven external research-platform access attempts

| Platform | Observed access/extraction condition | Scientific interpretation permitted |
| --- | --- | --- |
| Zenodo | Selected RS01 record text for `10.5281/zenodo.23365504`; extractor acquisition day **2026-10-28 UTC** | Earlier acquired representation, **not** today's new views/download counters |
| DataCite | OSF DOI typed `StudyRegistration`, `findable` in extracted text; acquisition day **2026-10-28 UTC** | DOI state from this representation, not frozen registration revision proof or today's newly certified query |
| ORCID | Researcher Works text flattened; acquisition day **2026-10-28 UTC** | No fresh reliable group/work-summary count |
| Software Heritage | CONTROL latest-visit attempt yielded an **Anubis anti-bot page**; acquisition day **2026-10-28 UTC** | **BLOCKED**, never interpreted as missing origin or absent preservation |
| OpenAIRE | An RS01 exact DOI query text was accessible, but extraction acquisition day was **2026-10-27 UTC** | Not an October 29 result; no full ten-object census |
| OpenAlex | Selected author profile text contained `works_count=32`, source `updated_date=2026-10-19`; acquisition day **2026-10-28 UTC** | Still `UNRESOLVED_QUERY_SHAPE_CONFLICT` against separately retained 21/30 profile shapes; **not** a newly measured transition |
| OSF | Registration API text includes `public=true` and `reviews_state=accepted`; acquisition day **2026-10-28 UTC** | Original-versus-updated registration wording remains **NOT_VERIFIED**; no change to frozen contract |

Other direct web-reader attempts made during the review failed with 403, cache-miss or inaccessible-URL conditions; these failures are disclosed here rather than interpreted as negative observations or silently converted into successful requests. They occurred outside the focused ledger's explicitly bracketed window and lack independently usable individual-request clocks.

## Study contract and gate decisions

The study retains **ten** fixed objects RS01–RS10 across **six** analytical layers, giving **60 object-layer units per eligible scheduled timepoint**. The seven operational platforms provide at most **70 possible object-platform checks**, a different count. OpenAIRE and OpenAlex both belong to `discovery_graph` but have separate observable contracts. No additional source, DOI, monitoring request, or CONTROL Release changes this denominator.

The [operational schedule](../../../schedule/README.md) declares **no concrete offsets**. The fixed-corpus October 14 releases have historical evidence, but cannot alone establish that the scheduled prospective collection gate was met. This record adds **zero** rows to `observations/raw/` or `observations/derived/`.

**Status:** `PARTIAL / NO_CONCLUSION` for a same-day seven-platform observation; GitHub Release-list recheck is complete for its expressly stated API scope. No new claims of propagation timing, cross-layer absence, independent scholarly adoption or backend processing are warranted.

**Retest trigger:** a retrieval path that returns attributable contemporaneous source representation, including exact source/query shape, real capture clocks and retained original response evidence, plus a separately declared qualifying schedule before any interpretation as prospective data. Review the OSF frozen-version history independently before claiming its original wording.

**Scope protection:** no edits to `contract/`, `corpus/`, `schema/`, `baseline/`, `schedule/`, `observations/`, or previous records; no external write, new release/tag/DOI, synthetic result, statistical model or amendment.
