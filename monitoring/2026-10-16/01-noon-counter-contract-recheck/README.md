# 2026-10-16 noon: 11 software-family counters and cross-platform preflight

**Phase:** diagnostic monitoring / **NOT** an eligible prospective OSF observation. **Fixed RS01–RS10 = ten study objects**; `research-software-identity-audit` = separately reported control infrastructure, **not RS11**. The researcher's requested noon checkpoint is a daypart, **not** evidence of an exact 12:00:00 capture. This verification started after noon in Asia/Shanghai; outer retrieval windows are in the [attempt ledger](source-attempts.csv) and [machine summary](record.json).

This is an **append-only new observation**. The existing [October 15 morning raw-derived record](../../2026-10-15/01-morning-facility-recheck/README.md), frozen OSF registration, baseline, schema, schedule and checkers are unchanged.

## 1. Critical Zenodo distinction: total vs hourly unique

Zenodo's official [statistics definitions](https://support.zenodo.org/help/en-gb/4-usage-statistics/15-what-is-a-view-download-data-volume) distinguish:
- `views` / `downloads`: total record visits or file download events (robots and double-clicks filtered; **not hourly deduplicated**).
- `unique_views` / `unique_downloads`: repeated visits/downloads by an anonymized visitor **to that record within one hour** counted once. This is **not** a count of distinct humans across all families or days.
- The [post-2023 public record page](https://support.zenodo.org/help/en-gb/4-usage-statistics/2-why-is-the-views-downloads-count-lower-than-before-the-migration-oct-2023) primarily displays the **unique** values, normally aggregated across **all versions** of one Concept DOI. Total counts remain in the API.

**Our computation uses exactly ONE family-attached `stats.views`, `stats.unique_views`, `stats.downloads`, `stats.unique_downloads` set per Concept DOI, not 43 versions' repeated family counters.** All 11 raw field extracts, exact source URLs and outer windows are in [`zenodo-family-api-stats.csv`](zenodo-family-api-stats.csv).

| Object family | API total views | API unique views | Total downloads | Unique downloads |
| --- | ---: | ---: | ---: | ---: |
| RS01 welcome-to-github | 265 | 181 | 6 | 5 |
| RS02 zero-entropy-lab | 223 | 138 | 1 | 1 |
| RS03 Axiom-0 | 246 | 161 | 1 | 1 |
| RS04 reflective-continuum | 197 | 115 | 1 | 1 |
| RS05 agent-foundations | 224 | 139 | 2 | 2 |
| RS06 auto-doc-engine | 217 | 132 | 0 | 0 |
| RS07 epistemic-pipeline | 225 | 142 | 1 | 1 |
| RS08 sci-render-kit | 208 | 130 | 2 | 2 |
| RS09 china-agentic-observatory | 234 | 150 | 1 | 1 |
| RS10 agentic-frontier-observatory | 244 | 161 | 2 | 2 |
| **Ten fixed samples** | **2,283** | **1,449** | **17** | **16** |
| **Control repo (separate)** | **103** | **96** | **3** | **3** |
| **11 software-family descriptive sum** | **2,386** | **1,545** | **20** | **19** |

The user's October 16 noon *transcribed* 11-result Zenodo front-end list (e.g. `1815` meaning **181 unique views, 5 unique downloads** for RS01) agrees **numerically** with all eleven independently extracted family unique counters. The search text itself has no independently verified per-page HTTP capture timestamp; the current API cross-check is **2026-10-16T04:55:31.248Z–04:55:57.369Z**, including a separate control-family enumeration. No user or robot identity is inferred.

**Preserved control conflict:** a standalone read of `GET /api/records/23284570` returned attached **74 total views / 71 unique views / 3 downloads**, a previously seen older field set. Independently, `GET /api/records/23284570/versions` enumerated all **3** control versions and each attached family stats reported **103 total views / 96 unique views / 3 downloads**. Version-specific `version_views` were **25 + 55 + 23 = 103**. We use the internally consistent complete-family enumeration for the **stated derived total**, but retain the earlier direct-record reply verbatim at the **field-extract** level as `CONFLICTING_OLDER_EXTRACT`, **not** a proven cache mechanism or exact update time. No bytewise original HTTP transport archives have been collected in this pass.

Historical comparison, at the *same named family field granularity*: the archived **2026-10-15 09:34–09:36 Asia/Shanghai** data shows fixed-ten `views=2231, unique_views=1400, downloads=8, unique_downloads=7` and control `95, 91, 3, 3`. October 16 extracted counters differ by **+52 / +49** for the fixed-ten views / unique views, and **+8 / +5** for the control. Across all eleven, totals differ by **+60 `views`**, **+54 `unique_views`**, **+9 total downloads**, **+9 unique downloads**. These are **two retrieval snapshots**, not proof of when events occurred or how backends counted them.

The existing complete [Zenodo version inventory](../../2026-10-15/01-morning-facility-recheck/version-enumerations.csv) counted **40 fixed-ten versions + 3 control versions = 43** at its October 15 capture. We did **not** repeat all 43 individual record reads today; the **11 latest version records** and control's **3-version list** were checked. Thus the historical enumerated count is not silently relabeled as a new 43-record exhaustive capture.

## 2. WorkflowHub: independent user-supplied Team Dashboard surface

The researcher-provided **October 16 noon Team Dashboard text** names these three assets; the [three-row attributed table](workflowhub-dashboard-user-extract.csv) preserves *dashboard* numbers distinct from per-version detail `Activity`:

| Public asset | Most viewed count | Most downloaded count |
| --- | ---: | ---: |
| [zero-entropy-lab NEXUS CORTEX](https://workflowhub.eu/workflows/2334) | 1,162 | 80 |
| [welcome-to-github NEXUS CORTEX](https://workflowhub.eu/workflows/2332) | 1,029 | 111 |
| [welcome-to-github Brain Evolution](https://workflowhub.eu/workflows/2337) | 320 | 13 |
| **Arithmetic sum of these three dashboard asset counts** | **2,511** | **204** |

The same supplied panel lists **Xuanyi Jiang: 4** under Most active submitters. **No selected Dashboard period or asset-type filter state is discernible from the text alone.** SEEK's official [Dashboard guide](https://docs.seek4science.org/help/user-guide/project-dashboard.html) defines these panels as asset rankings **within the selected period**; therefore do **not** compute a delta against [Oct 15 version-detail `Activity`](../../2026-10-15/01-morning-facility-recheck/workflowhub-detail-statistics.csv), call 2,511 distinct viewers, or claim 204 independent people. The public WorkflowHub asset identities were checked but the three numeric dashboard counts **were not independently retrieved from the Team Dashboard**; attempts to extract public `.json` views failed and are recorded, not invented as successful API validation.

## 3. Other platforms and identity / availability checks

- **GitHub:** all ten fixed repositories still expose four published Releases each, latest `v2026.10-fourteen-day-evidence-checkpoint` on **October 14**. Control has three, latest `v2026.10-evidence-reconciliation` on **October 10**. Current RS01/RS02 `main` commits have advanced on October 16; later `main` is **not** contained in the earlier immutable archived Release. All 11 current `main` SHAs and 11 release-list source locators are in the [attempt ledger](source-attempts.csv)
- **DataCite:** all **ten** October 14 release-version DOIs plus the control version DOI are currently **findable** and return matching `IsVersionOf` Concept DOI relationships; DOI identity is not itself bytewise ZIP equivalence or a first-indexing timestamp
- **OpenAIRE:** each of the ten new fixed-corpus version DOI **exact-PID** Graph v1 queries returned `header.numFound=1`. Control latest version PID also returned 1, while control Concept DOI exact-PID query returned 0. The latter is **not** proof of global absence
- **OpenAlex:** live author-filtered Works list `meta.count=29`, **29 returned: 11 software + 18 other**; selected and full author profile `works_count=26`, `cited_by_count=1`, `updated_date=2026-10-13T12:33:52`. The **29-versus-26 discrepancy is retained**, not forced to equal; 11 `software` Works does not mean an eleventh preregistered RS sample nor 11 independent Zenodo families
- **ORCID:** public works content available as flattened text, but **current native work-group and summary totals were NOT re-counted**. Historical October 15 15 groups / 84 summaries remain dated historical evidence, not a fabricated October 16 structured extraction
- **Software Heritage:** control-origin visit endpoint served an anti-bot challenge. **NOT VERIFIED**, not repository absence. No new 10-object commit/directory/ZIP equivalence census was performed
- **OSF:** registration [5b329](https://osf.io/5b329/overview) still controls the research contract; the public October 6 update banner is visible, but **original-to-updated native fieldwise diff remains UNVERIFIED**
- **Supplementary:** public RSD control entry reports `is_published=true` and the matching Concept DOI; RRID `SCR_029105` has a public resolver page. Neither turns the control into RS11 or a new infrastructure layer

Source and status granularity are retained in [`source-attempts.csv`](source-attempts.csv) (**59** categorized attempts/read paths; some are batch windows, not guaranteed 59 independent raw HTTP 200 replies). The extraction services supply machine-readable fields/excerpts; **original transport bytes, headers and per-request server timestamps are not retained**.

## 4. Contract and conclusion

- **OSF frozen sample = 10; layers = 6; unit denominator = 60 per eligible scheduled timepoint**. Seven operational platforms imply **70 possible finer-grained object × platform checks**, **NOT** a new denominator or an executed 70-cell wave
- The October 14 post-registration release cohort exists and is verified, but the repository still has **no concrete declared operational offsets**. Prospective eligibility and follow-up timepoints remain **UNADJUDICATED**, and this retrospective-looking dashboard review is diagnostic only
- No baseline, frozen contract, schema, schedule, historical capture, repository Release, tag, DOI, synthetic latency, imputation, claimed independent audience size, or new official observation timepoint is created by this PR
- **Bounded outcome:** `ZENODO_11_FAMILY_TOTAL_UNIQUE_RECONCILED`; `CONTROL_STALE_RECORD_STATS_RETAINED`; `WORKFLOWHUB_DASHBOARD_USER_SOURCE_PERIOD_UNKNOWN`; `OPENALEX_AUTHOR_QUERY_PROFILE_DISAGREE_29_VS_26`; `SWH_VISITS_CHALLENGED`; `NOT_PROSPECTIVE`
