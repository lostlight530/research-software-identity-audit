# Independent live Zenodo full-version verification — 2026-10-10

**Reviewer state:** `VERSION_ENUMERATION_AND_COUNTER_ARITHMETIC_VERIFIED_WITH_BYTE_PROVENANCE_LIMIT`

**Comparison authority:** original 10-10 `01-zenodo-surge-recheck` is retained; existing `02-reconciliation/interpretation.md` remains an earlier, independently authored interpretation. This record adds a **separate live cross-check**, not a recapture of prior timestamps, not a rewrite of the source record, and not an OSF preregistered/prospective observation.

## 1. Procedure executed independently

On **2026-10-10 Asia/Shanghai** a public-content extraction tool was instructed to fetch Zenodo's JSON endpoints with live fetching enabled; all direct URL requests included a distinct cache-busting `_cb` query argument. The extractor's HTTP response headers, server `Date`, unmodified raw transport bytes and per-request completion timestamps were **not** exposed. Recorded times are the outer **request-batch start/end windows**, not individual transaction timestamps.

| Procedure | UTC tool-request window | Outcome |
| --- | --- | --- |
| Eleven concept search queries: `/api/records?q=conceptrecid:<id>&all_versions=true&size=25&_cb=...` | `2026-10-10T14:20:30.804Z`–`14:20:56.659Z` | 11/11 successful JSON extractions, ten 3-version families plus one 2-version control |
| Independent family version list: `/api/records/<latest-version-id>/versions?_cb=...` | `2026-10-10T14:21:19.701Z`–`14:21:34.191Z` | 11/11 successful, all count, version IDs and `conceptrecid` identities agree |
| Each individual version record: `/api/records/<version-id>?_cb=...` | batch A `14:22:01.614Z`–`14:22:19.036Z`; batch B `14:22:19.036Z`–`14:22:47.161Z` | **32/32 successfully parsed**, correct `id` and `conceptrecid` |
| Exact supplied parameter alias `allversions=true` versus documented `all_versions=true` (RS07) | `2026-10-10T14:22:57.915Z`–`14:23:07.612Z` | Both returned all three RS07 records and matching identifiers; official docs prefer `all_versions` |

The authoritative machine-readable **derived field extract** is [version-counters-independent.csv](version-counters-independent.csv), 32 rows. It includes version index, individual record ID, version counts, reported family counts, source URL and the relevant outer extraction window. **It is not a verbatim HTTP raw archive, has no source-byte SHA-256, and must not be represented as a byte-reproducible original response.**

## 2. Counting contract actually tested

- Identity: exactly **ten** predefined RS objects, each with one canonical Zenodo concept and 3 existing versions; separately **one** audit runtime/control concept with 2 versions. The audit runtime is **not RS11** and does not change the OSF fixed corpus.
- `family_views(o) = sum(version_views(o,v))` over the **enumerated versions**.
- `family_downloads(o) = sum(version_downloads(o,v))` over the same versions.
- Retain `version_unique_views` on **each individual record**. Do **not** add cross-version unique counts as a deduplicated family-wide population or cross-repository unique audience.
- Compare every version record's attached `stats.views` against the computed family view sum. If divergent, preserve the value and classify it as an aggregate-field inconsistency; do **not** add the outlier to version sums.
- These are **observed current API counters** during the retrieval window, not 22:11 historical raw bytes or inferred event-level traffic, people, referrers, or ingestion times.

## 3. Independently recomputed totals

| Object | Version record IDs v1 / v2 / v3 (or v1 / v2) | Version views | Sum | Version downloads | Sum |
| --- | --- | --- | ---: | --- | ---: |
| RS01 welcome-to-github | 22790908 / 23068145 / 23137203 | 174 + 29 + 13 | **216** | 2 + 2 + 0 | 4 |
| RS02 zero-entropy-lab | 22791082 / 23068144 / 23137204 | 151 + 24 + 12 | **187** | 0 + 0 + 0 | 0 |
| RS03 Axiom-0 | 22791104 / 23068261 / 23137205 | 169 + 31 + 5 | **205** | 0 + 0 + 0 | 0 |
| RS04 reflective-continuum | 22791142 / 23068260 / 23137206 | 145 + 14 + 6 | **165** | 0 + 0 + 0 | 0 |
| RS05 agent-foundations | 22791170 / 23068262 / 23137207 | 145 + 44 + 3 | **192** | 0 + 1 + 0 | 1 |
| RS06 auto-doc-engine | 22791405 / 23068471 / 23137215 | 142 + 20 + 9 | **171** | 0 + 0 + 0 | 0 |
| RS07 epistemic-pipeline | 22791464 / 23068494 / 23137216 | 45 + 33 + 7 | **85** | 0 + 0 + 0 | 0 |
| RS08 sci-render-kit | 22791376 / 23068472 / 23137219 | 154 + 21 + 7 | **182** | 0 + 1 + 0 | 1 |
| RS09 china-agentic-observatory | 22791310 / 23068347 / 23137211 | 148 + 33 + 19 | **200** | 0 + 0 + 0 | 0 |
| RS10 agentic-frontier-observatory | 22791335 / 23068352 / 23137214 | 154 + 37 + 19 | **210** | 0 + 1 + 0 | 1 |
| **Fixed ten total** | **30 versions** | — | **1,813** | — | **7** |
| **AUDIT control, separate** | 23166491 / 23176748 | 19 + 32 | **51** | 0 + 0 | **0** |
| **Eleven displayed together** | **32 versions** | — | **1,864** | — | **7** |

The originally reported `22:11 Asia/Shanghai` **1,813 / 51 / 1,864** is **numerically reproduced**, but the independently checked snapshot is **22:20–22:23**, not proof of raw API values at 22:11.

## 4. One anomalous family-record, two aggregate fields

RS07 concept `22791463` had **three matching versions**, independently confirmed by the concept search, `/versions`, and all three direct version record URLs:

| RS07 version | `version_views` | `version_unique_views` | Attached `stats.views` | Attached `stats.unique_views` |
| --- | ---: | ---: | ---: | ---: |
| baseline `22791464` | 45 | 43 | 85 | 82 |
| month-close `23068494` | 33 | 32 | **186** | **106** |
| October `23137216` | 7 | 7 | 85 | 82 |

- The three **version view** counters sum to **85**, not 186: **+101 extra** in month-close's attached aggregate `views` field.
- Its attached aggregate `unique_views=106` differs by **+24** from the attached aggregate `unique_views=82` in each sibling record. This is a direct **within-family aggregate-field disagreement**, not a claim that unique visitors can be globally deduplicated across versions.
- Its **own** `version_views=33`, not 186.
- Classification: `FAMILY_AGGREGATE_MISMATCH`; `OBJECT_FAMILY_COUNT=1`; `ANOMALOUS_VERSION_RECORDS=1`; `ANOMALOUS_AGGREGATE_FIELDS=2`.
- Keep `186 / 106` as *observed exceptional raw fields* (in the extracted data); do not invent an extra family or add the +101 to the computed 1,813.

## 5. Explicit disagreement with a prior mechanism inference

The earlier `02-reconciliation/interpretation.md` suggests the mismatch represents a **mid-aggregation synchronization pass**, that the latest-version family value **understates the true total**, and that the platform's later convergence determines the true family count. The observed JSON **cannot independently establish** any of those platform-internal explanations. Repeated success of the direct endpoints verifies that the discrepancy is **observable and reproducible within this query interval**, not why it arose.

Under the **user-defined version-sum counting rule**, RS07 is **85** at this snapshot. `186` is an **unresolved conflicting attached aggregate**, not an independently established larger ground truth. Even if fields later converge, that cannot retroactively prove the earlier discrepancy's cause. Mechanisms such as delayed aggregation, inconsistent materialized counters, cache/index lag or other platform processing remain hypotheses.

## 6. Time-interval/delta evidence boundary

Today's ten-family fixed **version sums** independently reproduce the figures reported by the October 10 `01` snapshot. The October 9 `01-facility-recheck` provided **family views** of 840 (and control 48), so the **family-level snapshot delta** is **+973** for fixed ten and **+3** for control, conditional on matching the same counting semantics.

However, the retained October 9 morning package does **not** include a **full 32-version per-version view snapshot** under this five-step enumeration procedure. It is therefore **not valid** to reconstruct October 9-to-10 changes for v1 versus v2 versus v3 solely by subtracting a past family total. A full version-level interval table remains `NOT_DERIVABLE_FROM_RETAINED_PRIOR_VERSION_ROWS` until a comparable earlier version-wise snapshot is available.

Moreover, two distinct version reads in a bounded window do not expose the precise time of underlying user views, and a sudden visible step does **not** demonstrate a particular source actor, crawler, search engine, DOI link pathway, or synchronization mechanism.

## 7. Verification and preservation status

**Verified during this run:** 11 concept families; 32 version records; 11 version-list endpoint agreements; per-version counters; 1,813 / 7, control 51 / 0, combined 1,864 / 7; RS07's single anomalous version-record with two conflicting aggregate fields.

**Not performed:** direct Zenodo HTTP raw-byte retention and SHA-256; manual Zenodo HTML browser counters; new human/referrer attribution; complete historical version-wise interval reconstruction; execution of the existing repository local-only retained archive checker. External extraction success is not a formal raw-byte integrity result, nor a retrospective historical timestamp.

**Research contract:** `diagnostic_monitoring`, `prospective_dataset_member=false`. No new release trigger is inferred, no changes to fixed ten objects, six layers, 60 scheduled object-layer units, seven platforms or 70 possible operational checks. No new cloud CI is added.

**Evidence chain:** Zenodo public live JSON endpoints → independently extracted 32 record fields + 11 listings and version-list counts → [derived CSV](version-counters-independent.csv) → arithmetic / disagreement checks → this interpretation. Exact original transport bytes remain a provenance gap rather than silently labeled verified.

**Retest condition:** re-read the same 32 record IDs and compare all version views/downloads and attached family fields, preserving actual per-request timestamps and original HTTP response bytes if a direct source client becomes available. Preserve the existing original and `02` interpretation files unchanged.
