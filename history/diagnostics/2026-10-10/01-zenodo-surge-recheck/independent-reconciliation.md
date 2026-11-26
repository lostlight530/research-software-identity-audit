# Independent reconciliation — 2026-10-10 Zenodo surge identity and inference boundaries

**Type:** append-only reviewer correction to the original [October 10 diagnostic monitoring report](README.md), not a recapture, baseline edit, preregistration amendment, prospective observation, or deletion of earlier interpretations.

- Source commit inspected: `281bed0e2a98ff2163c536c486748bfb787989ee`
- Observation window in original collector: `2026-10-10T13:12:08Z` to `2026-10-10T13:23:06Z`
- Reviewer: independent GitHub/text arithmetic + public DataCite DOI version relationships + official Zenodo statistics documentation
- Reviewer execution date: 2026-10-10 Asia/Shanghai; exact external extractor request timestamps were not exposed
- Verification state: `PARTIAL_INDEPENDENT_VERIFICATION_WITH_CONFIRMED_INTERPRETIVE_CORRECTION`
- Dataset membership: `diagnostic_monitoring`; `prospective_dataset_member=false`

## CORRECTION 1 — Two alleged independent concept families are existing version records

The prior README calls `23068494` (RS07) and `23068352` (RS10) **"additional independent Zenodo concept families."** This object-type classification is **incorrect**.

The preserved [canonical baseline DOI map](../../../baseline/2026-10-05/doi-map.csv) explicitly identifies:

| Fixed object | Actual existing concept DOI | Record cited as "additional concept" | Correct role |
| --- | --- | --- | --- |
| RS07 `epistemic-pipeline` | `10.5281/zenodo.22791463` | `10.5281/zenodo.23068494` | September 30 **version DOI** of the same concept |
| RS10 `agentic-frontier-observatory` | `10.5281/zenodo.22791334` | `10.5281/zenodo.23068352` | September 30 **version DOI** of the same concept |

Independent public DataCite records for [RS07 v2](https://api.datacite.org/dois/10.5281/zenodo.23068494) and [RS10 v2](https://api.datacite.org/dois/10.5281/zenodo.23068352) explicitly give `relationType=IsVersionOf` to the corresponding canonical concept DOI. These are **not newly discovered software objects or independent version families**.

The two old reported counter pairs (`186/106` and `105/101`) remain preserved as **source-reported endpoint values whose exact statistics scope and capture provenance are not independently reconstructed in the retained eleven-response archive**. Do not add them to the canonical ten family totals, call them additional independent concept families, or use them to claim cross-family visitors.

## CORRECTION 2 — No human/bot or per-person attribution from views / unique views

The original README interprets approximately one-quarter unique-to-total increments as `inconsistent with a single-crawler pattern` and `consistent with repeated human visits`. This is an **unsupported attribution inference** and is not a demonstrated result.

Zenodo's [statistics specification](https://zenodo.org/help/statistics) and [current support explanation](https://support.zenodo.org/help/en-gb/4-usage-statistics/15-what-is-a-view-download-data-volume) define a unique view by a **one-hour visitor window** per record. Zenodo filters recognised robots but explicitly allows **human or machine** views; its observed aggregate API counters do not expose visitor identities, human/machine labels, per-request timing, or the referrer composition used to prove a specific behavioral cause. Across time periods, the anonymized visitor identifier can also rotate, and summing `unique_views` across different repositories is not global audience deduplication.

Therefore:

- `+973` total family views and `+283` summed family unique views across the ten fixed objects are **observed counter changes**, not `973` or `283` human visitors.
- Their aggregate ratio is `283/973 ≈ 29.1%`; this ratio does **not** distinguish repeated human activity from all automated, scripted, cache/pipeline, aggregation, or mixed explanations.
- An intraday stair-step pattern, even if shown by separate collector screenshots/logs, cannot by itself certify event times, independent visitor counts, bot exclusion effectiveness, provenance of each request, or causality.
- The original report's four intraday batch descriptions and user-supplied cloud cross-check remain **source claims** unless their own time-stamped response bytes are retained and separately validated. This eleven-response package only materializes the final capture window.

**Correct interpretation:** `COUNTER_SURGE_OBSERVED; ACTOR_ATTRIBUTION=UNKNOWN; REASON=UNRESOLVED`.

## Independently recomputed parts that remain valid

Re-read `zenodo-statistics.csv`, `zenodo-delta.csv`, `capture-summary.json`, and `capture-manifest.json` from the fixed source commit:

| Check | Independent recomputation |
| --- | --- |
| Fixed objects and control separation | 10 fixed rows + 1 separate audit-runtime row |
| Fixed family views | `1813` |
| Fixed summed family unique views | `1080` (not globally deduplicated) |
| Fixed downloads / summed unique downloads | `7 / 6` |
| Fixed version_views / version_unique_views from the source table | `100 / 90` (scope of endpoint version counters not independently established) |
| Previous October 9 fixed views / unique views | `840 / 797` |
| Sum of ten row-level changes | `+973 / +283` |
| Capture-manifest request entries | `11`, all labeled HTTP 200, each with an archive-member name and SHA-256 |

**Additional locator ambiguity, not silently corrected:** all eleven manifest URLs request the **concept record IDs** (e.g., `22791463`), whereas the derived CSV `record_id` column shows **October version IDs** (e.g., `23137216`) and `concept_doi` is blank. This may be an intentional distinction between endpoint locator and returned latest version but **that semantic mapping has not been independently established from raw response content in this review**. Treat it as `IDENTIFIER_ROLE_UNRESOLVED` until the retained archive's `id`, `conceptrecid`, `conceptdoi`, `doi`, and `stats.*` values are independently inspected. The source CSV and raw archive remain unchanged.

## Execution/evidence boundary

- Available reviewer execution: GitHub API latest-`main`, open PR and commit diff inspection; parsing/summing retained text CSV and JSON; independent public DataCite relationship excerpts; official Zenodo metrics contract.
- **NOT_EXECUTED** by this reviewer: local tarball decompression and archive SHA-256 verification; rerun of all eleven Zenodo API calls; source collector's four intraday probes; full control repository strict checker locally.
- Direct `git ls-remote` from the reviewer's shell failed with `Could not resolve host: github.com`; GitHub API via authorized connector was available. This is a *local shell network restriction*, not evidence the repositories are absent.
- The `main` advisory CI success validates its configured contract checks, **not** today's original Zenodo response bytes or human-attribution hypothesis.

## Disposition

**The reported counter changes and fixed-ten denominator are arithmetically supported; the two "additional concept families" and human-repeat inference are superseded by these corrections.** Neither original source content nor original identifiers are erased. No release eligibility, operational observation schedule, 60 preregistered units, 70 platform-check granularity, or prospective dataset status is changed.

Retest trigger: when original archived JSON can be independently checked for `id/conceptrecid/doi/stats` relationships; if the collector's earlier four timepoint raw responses become available; or if the platform exposes directly attribution-relevant metrics. Do not infer the missing data in the meantime.
