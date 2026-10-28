# Correction — October 29 diagnostic retrieval-clock provenance

**Affected original record:** [2026-10-29 bounded contract recheck](README.md), added in [PR #69](https://github.com/lostlight530/research-software-identity-audit/pull/69), merge commit `3ed22e5153a48452b89ab47c16f7cc4d097c8edb`

**Correction class:** explicit, post-publication `CLOCK_PROVENANCE_UNVERIFIED`; no change to OSF Registration, 2026-10-28 as-of Git snapshot, fixed corpus, original platform states, dataset phase or prospective cell count

## Exact defect

The original `record.json` states:

- `batch_start_utc = 2026-10-28T16:47:37Z`
- `batch_end_utc = 2026-10-28T16:48:56Z`
- `clock_provenance = conservative observer-side terminal clock bracket`

All 18 rows in `source-attempts.csv` repeat those same UTC bounds as `retrieval_batch_start_utc` / `retrieval_batch_end_utc`. **There are no retained timestamped terminal output or per-call connector records substantiating those exact bounds.** The values were entered during report construction without an actual source-supported time receipt, so the original precision and declared clock basis **must be retracted** as a scientific timing claim

The above old values remain **unverified author-entered placeholders**, not source-observed timestamps, network timing, response headers, actual retrieval clocks, or upper/lower bounds on platform propagation. No replacement timestamp is supplied or inferred

## Corrected reading of evidence

1. The connected GitHub provider returned structured public Release lists for **RS01–RS10 plus CONTROL**. Its item identities and Release timestamp fields remain source-returned fields, but the batch and individual retrieval clocks are **UNKNOWN**
2. The other seven ledger rows represent **submitted source-locator / extractor access attempts**, not proof of seven fresh direct origin HTTP responses. The external extractor reported only acquisition days, without raw origin HTTP transport bytes, response headers or a verified cache-bypass record
3. `acquired_at=2026-10-28T00:00:00Z` is **day-granularity** metadata: the acquisition could fall on either October 28 or October 29 in Beijing time. Do not assert it was definitely the *previous* or the *current* Beijing-local day
4. `acquired_at` for an OpenAIRE extraction was October 27 UTC, but neither this nor the other day-only acquisitions provides a precise individual request timestamp
5. `source_attempt_rows = 18` describes **CSV rows (11 GitHub locators + 7 other platform locators)**, not 18 independently completed origin HTTP requests
6. The original bounded GitHub Release-list comparison against October 27 covers **returned fields**, not a verified time-indexed full seven-platform census
7. The corrected status is **PARTIAL / NO_CONCLUSION** for any 2026-10-29 same-day full external recheck; the record still contains **zero** prospective observations

## Preservation and verification limits

The original machine/CSV bytes are retained in the previous Git commit [`3ed22e5153a4...`](https://github.com/lostlight530/research-software-identity-audit/commit/3ed22e5153a48452b89ab47c16f7cc4d097c8edb). We append this correction and an interpretive pointer, not silently overwrite that committed source history. Original `source-attempts.csv` rows are *not* rewritten with guessed times. The current machine record's `correction_notice` must be read whenever those clock fields are consumed

A successful source-ledger checker verifies that timestamps are parseable and ordered in the **provided table**. It cannot establish that the provided time values came from actual request clocks. Future precise timing claims require real independently attributable capture-time evidence or an explicit `UNKNOWN` state

**Source → original record → correction → permitted interpretation** remains traceable. No retroactive OSF schedule, baseline capture or new research unit is created
