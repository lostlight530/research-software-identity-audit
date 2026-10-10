# 2026-10-10 Zenodo surge recheck

An independently collected diagnostic monitoring record taken during an observed
same-day surge in Zenodo family-view counters across all fixed objects.

## Independent correction notice (2026-10-10)

**[Read independent-reconciliation.md](independent-reconciliation.md) before using the identity and attribution interpretations below.** RS07 `23068494` and RS10 `23068352` are pre-existing **version DOIs**, not additional independent concept families. Zenodo's aggregated view/unique-view counters do **not** establish repeated **human** visits or a known actor. The original report is preserved below as point-in-time source interpretation; the correction supersedes those two claims without rewriting raw data.

## Results

Fixed ten: 1813 family views, 1080 summed family unique views, 7 downloads and 6 unique downloads

All eleven (fixed ten plus audit runtime in separate context): 1864 views, 1129 unique views

Delta versus the 2026-10-09 facility capture (02:30-02:34 UTC): fixed ten 840 -> 1813 views (+973) and 797 -> 1080 unique views (+283) in roughly 35 hours

## Intraday observation sequence (all captured by the local probe)

- 06:01 UTC: summed concept-family counters 1,545 (partial batch state)
- 07:34-07:45 UTC: 1,647 / unique 1,065 (full four-metric capture)
- 12:26 UTC: 1,860 / unique 1,125 (third pipeline batch: RS05 +104, RS08 +105)
- 13:12-13:23 UTC (this record): 1,864 / unique 1,129 on canonical concept recids

Four intraday batches each produced roughly 100-view step increases on one or two
repositories at a time. In every batch the unique-view increment stayed at
approximately one quarter of the total-view increment (about 25 distinct visitors
per 100 views), which is inconsistent with a single-crawler pattern under daily
per-visitor deduplication and is consistent with repeated human visits.

## Additional independent concept families

Two fixed objects carry additional independent Zenodo concept families beyond the
canonical concept recorded in the DOI map:

- RS07 epistemic-pipeline: concept 23068494 showed 186 views / 106 unique views
- RS10 agentic-frontier-observatory: concept 23068352 showed 105 views / 101 unique views

These are reported separately and are not merged into the fixed-ten sums above.
Cross-family unique deduplication was not performed; summed unique counters are
not a deduplicated audience.

## Counter reconciliation

The canonical concept-recid mapping used here follows tools/check.py
(check_canonical_object_mapping). An earlier intraday probe used a mixed
recid table (latest-version recids for some objects); totals agreed to within
single digits, and the canonical values in this record supersede those mixed
recid readings. A user-supplied independent cloud capture at 15:0x CST agreed
per-object on unique views for eight of ten fixed objects, with the remaining
two differences explained by the same pipeline-batch lag.

## Evidence and scope

[Capture summary](capture-summary.json) · [Zenodo counters](zenodo-statistics.csv) · [Delta since October 9](zenodo-delta.csv) · [Raw evidence](../../../evidence/2026-10-10/01-zenodo-surge-recheck/capture-manifest.json)

The 70 possible fixed-object/platform cells remain distinct from the 60
preregistered object/layer units. No prospective timepoint is claimed by this
unscheduled recheck. GitHub traffic telemetry is deliberately excluded from this
record: repository traffic analytics belong to the operator ledger, not to the
preregistered identity-chain observation set. Historical October 9 records
remain unchanged.

## Failed requests

- None. All 11 concept-family requests returned HTTP 200 on first attempt within this capture window.
