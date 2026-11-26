# Independent reviewer reconciliation — 2026-10-09 evening (Asia/Shanghai)

**Scope:** bounded secondary review of the already merged [October 9 facility capture](README.md) (PR #23) and separately queried public endpoints. This is **not** a new prospective observation, not a rerun of the collector, and not a replacement for the original evidence or its local execution receipts.

| Field | Value |
| --- | --- |
| Reviewer | ChatGPT independent review via authorized GitHub connector, public web extraction, and read-only manifest arithmetic |
| Review date | 2026-10-09, evening, Asia/Shanghai |
| Review clock reference | approximately 2026-10-09T20:57+08:00; individual connector endpoint timestamps not exposed |
| Fixed source commit reviewed | `4151a13ed138df12a819f2909c82c3d1c21f022d` |
| Source capture window | 2026-10-09T02:30:44.088946Z to 2026-10-09T02:34:04.565360Z (from the original record, **not** this review's query window) |
| Input | original October 9 manifest, capture summary, 11-row Zenodo CSV, delta CSV, 70-row platform-state CSV, local offline report |
| Review state | `PARTIAL_INDEPENDENT_VERIFICATION_WITH_EXPLICIT_GAPS` |
| Dataset classification | `diagnostic_monitoring`; `prospective_dataset_member=false` |
| Changes to original records | none; this is an additive reviewer note |

## 1. Independently reconstructed **from retained GitHub text artifacts**

The reviewer parsed `evidence/2026-10-09/01-facility-recheck/capture-manifest.json` separately from the original collector and counted:

| Capture group | Request entries | HTTP 200 | Failed/non-200 |
| --- | ---: | ---: | ---: |
| `facility` | 175 | 159 | 16 |
| `page-counter` (earlier, separately timestamped) | 11 | 11 | 0 |
| **Total** | **186** | **170** | **16** |

- Of the 16 facility failures, **11 are OpenAIRE attempts** (ten object-level calls plus one extended RS01 retry), **one RRID HTTP 403**, and **four WorkflowHub DOI OpenAlex HTTP 404**.
- There are **175 response archive-member references** in the combined manifest. This enumeration does **not** itself verify compressed archive bytes or each response digest.
- `zenodo-statistics.csv` contains **10 fixed-corpus rows and one separate audit-runtime row**. The review independently summed the fixed ten columns: family views **840**, family unique views **797**, family downloads **7**, family unique downloads **6**, version views **86**, version unique views **76**, version downloads **0**, version unique downloads **0**.
- The October 8-to-9 row-level delta CSV sums to **+65 family views** and **+64 summed family unique views**. Counts describe platform counters, **not** deduplicated people, adoption, or software impact.
- The platform-state CSV contains **70 distinct object × platform entries**, with **10 OpenAIRE cells explicitly unresolved**. This remains **60 preregistered object × infrastructure-layer units** per scheduled point; the 70 here are operational platform cells in unscheduled monitoring, **not** 70 eligible prospective observations.
- The preserved local `offline-verification.json` contains **766 result rows**, each marked passed, and reports **766 checks / 0 failed / 0 network calls**. This is verification of the **internal consistency of the retained report object**; this reviewer did **not** rerun the 766-check program or establish its runtime environment.

## 2. Independent external endpoint checks during this review

### GitHub: release eligibility

Queried the following endpoints for each of **RS01–RS10**:

- `GET https://api.github.com/repos/lostlight530/<repository>/releases/latest`
- `GET https://api.github.com/repos/lostlight530/<repository>/releases?per_page=5`

All **20 endpoint reads succeeded** in the authorized GitHub connector. All ten `/latest` records had tag `v2026.10-open-research-production-framework` with `published_at` timestamps on **2026-10-04T13:00:12Z through 13:00:39Z**. Each repository's release-list endpoint returned **three releases** (October 4, September 30 and September 16), and **none of those lists showed a release published after the 2026-10-05 preregistration date**. List checking limits the `/latest` endpoint's usual pre-release exclusion bias.

**Bounded finding:** no new post-registration fixed-corpus GitHub Release event was observed in these queries. This is not proof no unpublished tags, drafts or other eligible events can ever exist. The existing operational schedule still has no declared concrete offsets. Do not promote any October 6–9 monitoring result to a prospective timepoint.

### DataCite: fixed-corpus latest-version DOI sample

Independently fetched the **ten October-version DOI metadata endpoints** using a separate public content extractor:

`https://api.datacite.org/dois/10.5281/zenodo.<record_id>`

With record IDs `23137203`, `23137204`, `23137205`, `23137206`, `23137207`, `23137215`, `23137216`, `23137219`, `23137211`, `23137214`, all **10/10 fetched excerpts** contained the expected DOI identity, `resourceTypeGeneral=Software`, and a `relationType=IsVersionOf` relation.

**Scope:** independently re-read **10 newest-version identifiers**, **not** all 40 historical fixed-corpus identifiers. The original morning retained collector supports its separate 40/40 claim; this review does not elevate that to a new 40/40 live rerun. Public-extractor snippets are **not** full raw-response bytes and no exact individual extractor retrieval timestamps were supplied.

### OpenAlex: main-author profile

The independently fetched `https://api.openalex.org/authors/A5151904252` excerpt exposed `works_count=43` and ORCID `0009-0001-3617-0832`, matching the morning capture for these fields. A profile count is **not** an independently rerun author Works listing or evidence about exact ingestion-transition chronology.

### ORCID, Zenodo, OpenAIRE, preservation and other surfaces

- The ORCID public Works endpoint could be extracted only in a flattened form; the review **did not independently reconstruct** the morning **14 groups / 56 summaries**.
- Attempts to retrieve the current Zenodo JSON API for selected fixed objects through two independent public retrieval paths were **inaccessible / timed out**. Morning Zenodo counters were **arithmetically verified from retained CSV**, not renewed as an evening live metric.
- The OpenAIRE API attempt through the external extractor also **timed out**, consistent with an access limitation but not independent proof of the precise morning failure cause or record absence.
- Software Heritage's ten release/directory chains, RSD's eleven published software records, the 40-DOI collector matrix, and other supplemental claims were **not fully rerun externally by this reviewer**. Their original collector and offline-verification provenance remain authoritative for the morning's execution, not a second independently reconstructed observation.
- RRID 403, HAL zero-query result, and the four WorkflowHub DOI OpenAlex 404 outcomes remain bounded endpoint results; none establishes absence/deletion of the corresponding scholarly object.

## 3. Actual execution limitations and independence

A direct clone attempt was executed in the reviewer's separate shell:

`git clone --depth 1 https://github.com/lostlight530/research-software-identity-audit.git ...`

It **failed before checkout** with `Could not resolve host: github.com` (exit status 128). Therefore:

- `python tools/check.py --mode strict`: **NOT_EXECUTED locally in this review**.
- `python tools/check_retained_facility_evidence.py`: **NOT_EXECUTED by this reviewer**.
- Archive-member byte-level SHA-256, `artifact-manifest.json` digest verification and the three negative mutation trials: **NOT_INDEPENDENTLY_RERUN** in this environment.
- No raw-response archive, existing source file, historical manifest or observation state was modified.
- The repository's existing advisory GitHub workflow is **not** a substitute for these local offline validations; the explicit user execution boundary against cloud-running the retained-evidence checker is preserved.

## 4. Assessment

**Observed and reproduced in reviewer tools:** request-group denominator reconciliation; 70 unique platform rows; fixed ten-vs-control separation; 840/797/7/6 counter sums and 65/64 deltas; 766 passed flags in the existing local report; current ten release-list/latest results; ten DataCite latest-version DOI excerpts; OpenAlex profile 43.

**Source-supported but not newly independently rerun:** bytewise response digests and 766 executable semantic checks; ORCID structured count 14/56; complete 40-DOI set; 10 SWH chains; 11 RSD records; the original collector's exact HTTP transactions; the reported negative mutation tests.

**Unresolved:** evening Zenodo counter state, OpenAIRE endpoint record state in reviewer access path, exact downstream ingestion times, lack of concrete prospective offsets, and any complete new eligible release event not evidenced by these queries.

**Conclusion:** `PARTIAL_INDEPENDENT_VERIFICATION_WITH_EXPLICIT_GAPS`. The October 9 source package is internally consistent for the independently recomputed arithmetic and manifest grouping, and independent available public DOI/release/profile checks do not contradict it. No eligible prospective release has been observed. No new preregistered observation or causal/scientific-impact claim is created by this review.

**Retest only if** source API accessibility changes, a new eligible release becomes evidenced, exact ORCID/group data is accessible to an independent reviewer, or local archive-byte execution access becomes available. No automatic observation window or release is triggered by this report.
