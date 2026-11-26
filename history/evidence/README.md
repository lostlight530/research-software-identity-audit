# Historical evidence archive

<badge>ARCHIVED · NO NEW ACQUISITIONS</badge>

This is the former root-level `evidence/` archive. It retains source-response packages, capture manifests, structured projections, event ledgers, reconciliation artifacts and package documentation from **2026-10-08 through 2026-11-22** (36 event directories across 22 date folders).

It is not the destination for new daily research material. Current evidence belongs to the corresponding Study 1 day workspace under `studies/osf-wa5v8/dayN/evidence/`, or to the independently governed Study 2 cycle under `studies/osf-vshwk/cycles/`. Eligible prospective evidence must be linked through the registered `observations/raw/` contract, not inferred from archive membership.

Evidence and interpretation remain separate. Preserve original source identity, retrieval clocks, source locators, response conditions, digests and correction history. The directory consolidation does not re-capture, re-hash or rewrite the archived payloads. See the [path migration ledger](../migrations/path-migration-2026-11-26.csv) and [current path conventions](../../docs/record-path-conventions.md).

## Directory naming

All retained event directories use the same path envelope:

`YYYY-MM-DD/NN-lowercase-kebab-case/`

- `YYYY-MM-DD` is the declared source observation/capture date, not the later archive migration, review, PR merge or CI date
- `NN` and the event slug preserve the event identity shared with the corresponding `history/diagnostics/` package
- The evidence archive is a subset of the diagnostic event set. Gaps in the ordinal sequence, or a first retained package numbered `03` or later, are intentional; **do not renumber evidence packages independently**
- Deeper directories such as `prior-index-snapshots/`, `selected-history/` and `user-supplied/` are artifact groupings inside an event package, not additional dated events
- This `README.md` is the current archive index. `README.source.md` is the former root-level evidence index preserved byte-for-byte; it is not the current navigation entrypoint

## Complete retained event index

The following index lists all **36** retained evidence event directories. Links open each event's own `README.md`; names and ordinals are shown exactly as stored.

| Source date | Retained event package |
|---|---|
| 2026-10-08 | [`01-morning-recheck`](2026-10-08/01-morning-recheck/README.md) |
| 2026-10-09 | [`01-facility-recheck`](2026-10-09/01-facility-recheck/README.md) |
| 2026-10-10 | [`01-zenodo-surge-recheck`](2026-10-10/01-zenodo-surge-recheck/README.md) |
| 2026-10-14 | [`03-midnight-facility-recheck`](2026-10-14/03-midnight-facility-recheck/README.md); [`04-morning-facility-recheck`](2026-10-14/04-morning-facility-recheck/README.md); [`05-noon-user-pages`](2026-10-14/05-noon-user-pages/README.md); [`06-evening-facility-recheck`](2026-10-14/06-evening-facility-recheck/README.md) |
| 2026-10-15 | [`01-morning-facility-recheck`](2026-10-15/01-morning-facility-recheck/README.md) |
| 2026-10-18 | [`03-independent-research-verification`](2026-10-18/03-independent-research-verification/README.md) |
| 2026-10-20 | [`01-independent-research-recheck`](2026-10-20/01-independent-research-recheck/README.md) |
| 2026-10-24 | [`04-local-history-evidence-handoff`](2026-10-24/04-local-history-evidence-handoff/README.md) |
| 2026-10-25 | [`02-independent-institutional-recheck`](2026-10-25/02-independent-institutional-recheck/README.md) |
| 2026-10-26 | [`01-morning-institutional-recheck`](2026-10-26/01-morning-institutional-recheck/README.md); [`02-evening-institutional-recheck`](2026-10-26/02-evening-institutional-recheck/README.md) |
| 2026-10-31 | [`02-noon-user-page-reconciliation`](2026-10-31/02-noon-user-page-reconciliation/README.md); [`03-independent-institutional-statistics`](2026-10-31/03-independent-institutional-statistics/README.md); [`04-zenodo-all-version-statistics`](2026-10-31/04-zenodo-all-version-statistics/README.md) |
| 2026-11-02 | [`01-complete-institutional-recheck`](2026-11-02/01-complete-institutional-recheck/README.md); [`02-all-version-recheck`](2026-11-02/02-all-version-recheck/README.md); [`03-retained-local-evidence-completion`](2026-11-02/03-retained-local-evidence-completion/README.md) |
| 2026-11-08 | [`01-end-of-day-user-pages`](2026-11-08/01-end-of-day-user-pages/README.md); [`02-complete-institutional-recheck`](2026-11-08/02-complete-institutional-recheck/README.md); [`03-all-version-recheck`](2026-11-08/03-all-version-recheck/README.md) |
| 2026-11-10 | [`03-openaire-orcid-openalex-reconciliation`](2026-11-10/03-openaire-orcid-openalex-reconciliation/README.md) |
| 2026-11-12 | [`01-identity-claim-reconciliation`](2026-11-12/01-identity-claim-reconciliation/README.md) |
| 2026-11-13 | [`01-full-institutional-recheck`](2026-11-13/01-full-institutional-recheck/README.md) |
| 2026-11-15 | [`02-full-institutional-source-recheck`](2026-11-15/02-full-institutional-source-recheck/README.md) |
| 2026-11-17 | [`02-full-selftest`](2026-11-17/02-full-selftest/README.md) |
| 2026-11-18 | [`01-complete-identity-infrastructure-diagnostic`](2026-11-18/01-complete-identity-infrastructure-diagnostic/README.md) |
| 2026-11-19 | [`01-complete-institutional-recheck`](2026-11-19/01-complete-institutional-recheck/README.md); [`02-complete-institutional-recheck`](2026-11-19/02-complete-institutional-recheck/README.md); [`03-web-assisted-surface-review`](2026-11-19/03-web-assisted-surface-review/README.md); [`04-zenodo-supplementary-inventory-reconciliation`](2026-11-19/04-zenodo-supplementary-inventory-reconciliation/README.md); [`05-targeted-surface-semantic-reconciliation`](2026-11-19/05-targeted-surface-semantic-reconciliation/README.md) |
| 2026-11-20 | [`01-firstday-to-current-infrastructure-diagnostic`](2026-11-20/01-firstday-to-current-infrastructure-diagnostic/README.md) |
| 2026-11-22 | [`01-periodic-identity-infrastructure-recheck`](2026-11-22/01-periodic-identity-infrastructure-recheck/README.md) |

## Selected package notes

- [2026-10-08 / 01-morning-recheck](2026-10-08/01-morning-recheck/) — 17 original public API responses, timestamp and hash manifest, original local offline verification outcome

The original archive member names and source-response bytes are immutable through the path migration. See [monitoring naming rules](../../docs/record-path-conventions.md).

- [2026-10-09 / 01-facility-recheck](2026-10-09/01-facility-recheck/) — Timestamped original API responses and counter reconciliation

- [2026-10-10 / 01-zenodo-surge-recheck](2026-10-10/01-zenodo-surge-recheck/capture-manifest.json) — 11 archived original concept-recID responses from the source collector, **not** the later independent 32-version extraction

The independently extracted 32-version table is retained under [monitoring/2026-10-10/02-reconciliation](../diagnostics/2026-10-10/02-reconciliation/version-counters-independent.csv) as **derived public fields** with bounded fetch windows, **not** original byte-level HTTP evidence. The October 10 institutional public-status investigation is separately recorded in [scholarly](../../scholarly/infrastructure-review-2026-10-10.md).

## October 14 retained diagnostics and user pages

- [2026-10-14 / 03-midnight-facility-recheck](2026-10-14/03-midnight-facility-recheck/README.md) — 00:04–00:16 independent API capture, incomplete Zenodo counters retained as null
- [2026-10-14 / 04-morning-facility-recheck](2026-10-14/04-morning-facility-recheck/README.md) — 08:03–08:07 independent API capture; 33 version records and 40 DOI routes
- [2026-10-14 / 05-noon-user-pages](2026-10-14/05-noon-user-pages/README.md) — user-labelled noon Zenodo unique counters and WorkflowHub Dashboard; exact time/Period unknown

## October 14 evening new-release propagation

[Evening diagnostics and new-version evidence](../diagnostics/2026-10-14/06-evening-facility-recheck/README.md) preserve ten new public releases, 72 findable DOIs, 15 ORCID groups / 85 sources and 43 enumerated versions; user pages and independent captures remain separate

## October 15 morning diagnostic recheck

[Full morning record](../diagnostics/2026-10-15/01-morning-facility-recheck/README.md) retains 27 author-query Works, 84 ORCID source summaries, 72 DOI records and source-specific counter reconciliation; earlier captures remain dated

- [October 18 independent research field extracts](2026-10-18/03-independent-research-verification/README.md) — minimized public representation with explicit local-only raw bytes and source archive digest verification

- [October 20 research evidence](2026-10-20/01-independent-research-recheck/README.md): minimized public fields, per-attempt digests and retained failure/retry states

## October 25 later independent institutional recheck

- [2026-10-25 / 02-independent-institutional-recheck](2026-10-25/02-independent-institutional-recheck/README.md) — 162 timestamped attempts; twelve page/API unique pairs match, 76 DOI records, structured ORCID 17/89, SWH four current release chains, source-separated WorkflowHub counts; diagnostic only, zero prospective cells

## October 26 institutional checklist rechecks

- [2026-10-26 / 01-morning-institutional-recheck](2026-10-26/01-morning-institutional-recheck/README.md) — 405 timestamped attempts; 34 supplemental surfaces, 77 identified DOI records, 12-family fields; diagnostic only, zero prospective cells
- [2026-10-26 / 02-evening-institutional-recheck](2026-10-26/02-evening-institutional-recheck/README.md) — 384 timestamped attempts; 34 supplemental surfaces, 77 identified DOI records, 12-family fields; diagnostic only, zero prospective cells

## November 19 supplementary Zenodo version identity reconciliation

- [2026-11-19 / 04-zenodo-supplementary-inventory-reconciliation](2026-11-19/04-zenodo-supplementary-inventory-reconciliation/README.md) — selected Zenodo, DataCite and GitHub release metadata for two previously unkeyed supplementary versions; connector-normalized projections only, with explicit retrieval window and artifact digests

## November 19 targeted surface semantics and path-entrypoint reconciliation

- [2026-11-19 / 05-targeted-surface-semantic-reconciliation](2026-11-19/05-targeted-surface-semantic-reconciliation/README.md) — minimal public identity projections, original EDAM runner digest and source locators; unresolved InterLex/HAL preserved

## November 20 first-day-to-current infrastructure evidence

- [2026-11-20 / 01-firstday-to-current-infrastructure-diagnostic](2026-11-20/01-firstday-to-current-infrastructure-diagnostic/README.md) — scoped 160 source attempt records with batch retrieval windows and selected public fields; provider HTTP original bodies not retained; 60 fixed-sample Zenodo versions independently identified in current records

## November 22 periodic diagnostic evidence and entrypoint reconciliation

- [2026-11-22 / 01-periodic-identity-infrastructure-recheck](2026-11-22/01-periodic-identity-infrastructure-recheck/README.md) — 11 retained public-source JSONL ledgers with original connector batch UTC bounds, selected provider fields, explicit unknowns, and Git blob source identities; the documentation entrypoint was added after [PR #136](https://github.com/lostlight530/research-software-identity-audit/pull/136) because the prior advisory path checker reported a missing evidence README; historical source JSONL files were not changed

## November 24 material relocated to wa5v8

The original two evidence packages are now under [Day 0 evidence](../../studies/osf-wa5v8/day0/evidence/README.md); see the [path and blob mapping](../../studies/osf-wa5v8/path-migration-2026-11-25.json). The source ledgers remain byte-identical.


## Preserved source-era index

The former root [`evidence/README.md`](README.source.md) is retained byte-for-byte as `README.source.md`. Its original relative links and source-era path statements are intentionally unchanged; use this README as the current archive entrypoint. The original naming policy is preserved at [`record-path-conventions.source.md`](../documentation/record-path-conventions.source.md); current path ownership is defined in [`docs/record-path-conventions.md`](../../docs/record-path-conventions.md).
