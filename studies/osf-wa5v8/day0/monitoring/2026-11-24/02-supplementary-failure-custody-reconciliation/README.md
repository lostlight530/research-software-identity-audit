# 2026-11-24 supplementary surface failure-custody reconciliation

**Classification:** `DIAGNOSTIC FOLLOW-UP / SEPARATELY TIMED SOURCE RETRIEVAL / NOT PROSPECTIVE`

This is a small **append-only follow-up** to the already merged [November 24 periodic diagnostic](../01-periodic-identity-infrastructure-recheck/README.md). It addresses a specific evidence-completeness gap: the [original 34-surface ledger](../../../evidence/2026-11-24/01-periodic-identity-infrastructure-recheck/supplementary-34-source-attempts.jsonl) recorded `CONNECTOR_ERROR` for seven entries without their per-item connector reason codes (row 23 OpenAIRE already included a reason). **The original ledger is deliberately unchanged.**

The seven exact source locators were re-attempted at **2026-11-23 16:39:19.236–16:39:21.308 UTC** (2026-11-24 00:39 Asia/Shanghai). All seven follow-up calls returned connector errors with individually retained reason codes in the [follow-up evidence ledger](../../../evidence/2026-11-24/02-supplementary-failure-custody-reconciliation/source-attempts.jsonl).

| Surface row | Source | New independently observed connector reason |
| --- | --- | --- |
| 11 | ScreenIT ASWG | `CRAWL_UNKNOWN_ERROR` |
| 13 | dkNET | `CRAWL_NOT_FOUND` |
| 14 | InterLex | `CRAWL_NOT_FOUND` |
| 20 | Internet Archive | `CONTENT_NOT_CACHED` |
| 21 | HAL | `SOURCE_NOT_AVAILABLE` |
| 22 | OpenAlex | `SOURCE_NOT_AVAILABLE` |
| 24 | Identifiers.org | `CRAWL_NOT_FOUND` |

## Interpretation, not a retroactive repair

- The reason codes describe the **separately timed follow-up attempts only**. They are **not asserted as the error causes of the original 16:18–16:19 UTC collection**; its missing reason fields remain missing in that original record.
- `CRAWL_NOT_FOUND` and `CONTENT_NOT_CACHED` describe extractor behavior and do not prove that a scholarly record, provider endpoint, software registration, or historical object does not exist.
- No provider HTTP status or original provider response bytes were captured. The timestamps above bound the connector calls, not server-side first-index times or separate HTTP transaction completion times.
- The seven rows overlap the 34 registered source locators; they are not seven new surfaces, new objects, or seven additional preregistered analytical units.
- Original [OSF Registration 5b329](https://osf.io/5b329/overview) and approved `344-83` revision remain unchanged. Fixed **RS01–RS10 × 6 = 60** planned object-layer units per eligible timepoint; CONTROL is not RS11. The [operational schedule](../../../../../../schedule/README.md) has no concrete offsets, so this is **not a formal prospective observation cycle**.
- This package changes no original observations, source blobs, source-counter values, historical baseline, endpoint manifest, Release, DOI or OSF state.

**Disposition:** `SOURCE_FAILURE_REASON_FOLLOWUP_RETAINED / ORIGINAL_UNKNOWN_REMAINS_UNKNOWN / NO_DATASET_OR_CONTRACT_CHANGE`.
