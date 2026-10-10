# 2026-10-10 / 02 — Zenodo version-family reconciliation

**Record class:** `diagnostic_monitoring` / `exploratory`, **not** an OSF scheduled prospective observation. This folder contains work from **different source/reviewer executions**; preserving that distinction is part of the evidence contract.

## Reading order and source ownership

1. [record.yaml](record.yaml) — original second-pass operational summary, with its **actual 14:07–14:14 UTC collector window**.
2. [interpretation.md](interpretation.md) — **original second-pass author/agent interpretation**, preserved as dated source. Its "mid-aggregation synchronization" explanation and "true family total must be higher" suggestion are **hypotheses, not verified mechanisms**.
3. [zenodo-statistics.csv](zenodo-statistics.csv) — original derived canonical-record table, **not a 32-row version enumeration**.
4. [independent-version-verification.md](independent-version-verification.md) — later, separately attributed independent public-API extraction and method/interpretive correction; this is the controlling interpretation **for this independent review**, not a replacement for the original collector.
5. [version-counters-independent.csv](version-counters-independent.csv) — 32 derived fields from **ten concept families × three versions, plus one independently reported control family × two versions**; not raw response bytes.

## Results under the later independent method

- **Fixed RS01–RS10:** 1,813 version-summed views, 7 version-summed downloads (30 individual versions).
- **Control repository:** 51 views, 0 downloads (two versions), **not RS11**.
- **Descriptive combined:** 1,864 views, 7 downloads over 11 displayed repositories; **sample denominator stays ten**.
- **Within-family conflict:** RS07 month-close `23068494` attached `stats.views=186` while its family members' `version_views` sum to `45+33+7=85` (+101); attached `stats.unique_views=106` versus other family records `82`. The anomaly is **one version record with two attached-field differences**, not an 11th or 12th study family.
- **Unverified:** why the conflicting attached field arose, visitor origin, bot/human composition, exact underlying event times, historical version-level interval growth and a byte-identical replay of the independent extractor. An observed disagreement does not establish a platform internals synchronization cycle.

The 2026-10-10 evening independent retrieval reproduced the older reported numerical totals but **did not** prove an earlier 22:11 source response was identical or preserve the raw HTTP bytes for the 32 separate reads. `version-counters-independent.csv` is derived public metadata, with outer batch windows and no transport-byte hash.

[Method boundary](../../../schema/counting-rules.md#supplementary-zenodo-version-family-reconciliation-2026-10-10) · [Original October 10 collector](../01-zenodo-surge-recheck/README.md) · [External institutional review](../../../scholarly/infrastructure-review-2026-10-10.md).

**Source lineage:** original source collector -> its preserved evidence and 02 interpretation -> separate later independent version comparison -> reviewer correction and unresolved states. Do not relabel the original author's collection as this reviewer's raw observation.
