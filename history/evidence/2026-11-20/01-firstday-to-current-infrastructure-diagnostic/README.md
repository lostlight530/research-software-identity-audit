# 2026-11-20 bounded source-attempt and selected-field custody

This event is diagnostic, not scheduled prospective research. Its actual connector retrieval *batch* clocks, scoped source locators, selected public fields, and failed/unresolved outcomes are preserved in JSONL files. Original provider HTTP bytes and exact per-request HTTP status codes were **not** retained; GitHub source commit/tree/blob identities are separate authentic Git objects.

## Source families

- `zenodo-source-attempts.jsonl` — **69** known version IDs (60 RS fixed, six CONTROL, three LSEL) with exact record/DOI counters or explicit failures
- `zenodo-selected-fields.jsonl` — minimized provider fields, not complete origin response bytes
- `github-main-attempts.jsonl`, `github-latest-releases.jsonl`, `github-open-prs.jsonl` — **11** repositories × 3 GitHub read scopes
- `surface-source-attempts.jsonl`, `surface-selected-fields.jsonl` — **34** supplementary existing surfaces, unresolved and unprojected cases retained
- `public-interactions.jsonl` — RSD 1870/1871, RSE 498 and epistemic 261 point-in-time GitHub issue/PR state
- `core-platform-targeted-attempts.jsonl` — **20** selective DataCite/OpenAIRE/OpenAlex/ORCID/SWH queries
- Three bounded summaries — `zenodo-bounded-summary.json`, `surface-bounded-summary.json`, `core-platform-targeted-summary.json`

The source scopes add to 160 attempt rows, not 160 distinct DOI identities, not 160 raw HTTP bodies and not a replacement for the November 19 458-key full diagnostic.

See [provenance](provenance.json), [monitoring summary](../../../diagnostics/2026-11-20/01-firstday-to-current-infrastructure-diagnostic/summary.json) and [full history taxonomy](../../../repository-inventory/2026-11-20/README.md). Earlier source event files are not rewritten.
