# Scholarly identity footprint: 2026-10-09 evening → 2026-10-10 bounded update

**Record kind:** `retrospective_cross_platform_reconciliation` / documentary research supplement; not a second registration, an eligible prospective observation, or an attempt to recreate a full historical 53-DOI API harvest.

**Prior source identity:** researcher-supplied *科研身份足迹全平台实测 · 2026-10-09 晚* (reported first live window 2026-10-09 22:34:20–22:39:58 Asia/Shanghai, gapfill 22:46:17–22:57:17). The researcher describes a separately retained `archive/raw/research-identity-metrics-2026-10-09/` directory with `status.txt` and `dois.txt`. **Those exact prior directory bytes/sha256 entries were not reopened in this review.** Its 50-DOI coverage and individual usage metrics are **historical source-reported results**, not current metrics.

**10/10 evidence sources and their distinct clocks:**
- Dated scholarly public-state [review](infrastructure-review-2026-10-10.md), [late closeout](closeout-review-2026-10-10.md), [ten software release identity review](fixed-ten-release-identity-review-2026-10-10.md) and the independently retrieved [OpenAlex 18-Work inventory](../monitoring/2026-10-10/03-openalex-work-aggregation/README.md) (actual **2026-10-10 23:32:12–23:34:52 Asia/Shanghai** outer extraction window).
- Researcher-reported **2026-10-10 23:54** Zenodo 11-family counters, later numerically matched by **2026-10-11 00:26–00:28** independent 33-version JSON reads; see the independently verified [full-version recheck](../monitoring/2026-10-11/01-zenodo-33-version-recheck/verification.md). No 23:54 source-byte HTTP response is retained **by this reviewer**.
- New v4 WorkflowHub DOI registrations and control software v3 release metadata verified **after midnight on 2026-10-11**, using immutable-looking provider **registration timestamps from 2026-10-10**. Registration timestamps are public metadata fields, **not** our contemporaneous retrieval timestamps. [Additive three-DOI field inventory](identity-footprint-new-dois-2026-10-10.csv).
- Local historical source dates and as-observed clocks are kept separate; `2026-10-10` in this filename is the **logical date being reconciled**, not a claim all evidence was freshly collected before midnight.

## 1. Identifier population and chronology

| Identity class | October 9 reported known DOIs | Added October 10 | Cumulative known identifiers by October 10 23:54 |
| --- | ---: | ---: | ---: |
| RS01–RS10 Zenodo **concept** DOIs | 10 | 0 | 10 |
| RS01–RS10 Zenodo **version** DOIs | 30 | 0 | 30 |
| Separately recorded audit-control Zenodo concept DOI | 1 | 0 | 1 |
| Audit-control Zenodo version DOIs | 2 | **1**: `10.5281/zenodo.23284570` | **3** |
| Frozen OSF study registration DOI | 1 | 0 | 1 |
| WorkflowHub **two** work-flow lineages' version DOIs | 6 | **2**: `10.48546/workflowhub.workflow.2332.4`, `10.48546/workflowhub.workflow.2334.4` | **8** |
| **Known DOI identities (NOT independent works)** | **50** | **3** | **53** |

Specific externally returned chronological facts, converted UTC→Asia/Shanghai:
- `2332.4` DataCite `registered=2026-10-10T05:44:41Z` → **2026-10-10 13:44:41 CST**, creator ORCID matches `0009-0001-3617-0832`.
- `2334.4` `registered=2026-10-10T05:44:45Z` → **13:44:45 CST**, same correctly identified creator ORCID.
- GitHub audit-control [new release](https://github.com/lostlight530/research-software-identity-audit/releases/tag/v2026.10-evidence-reconciliation) `published_at=2026-10-10T15:45:40Z` → **23:45:40 CST**.
- Control Zenodo [record `23284570`](https://zenodo.org/api/records/23284570) `created=2026-10-10T15:45:46.175611Z` → **23:45:46**, under unchanged `conceptrecid=23166490`.
- New version DOI [DataCite registry](https://api.datacite.org/dois/10.5281/zenodo.23284570) `registered=2026-10-10T15:45:48Z` → **23:45:48**, `IsVersionOf=10.5281/zenodo.23166490`.

The new audit-runtime **release** is an actual public software version, **not** a qualifying post-registration RS01–RS10 release; its publication does not begin prospective observations. No change to preregistered `10×6=60` object-layer units; `10×7=70` is still possible **platform checks**, not an analytical denominator. Workflow versions and DOI counts are not new RS research objects.

## 2. Cross-platform comparison — do not substitute October 9 statistics for October 10

| Surface | October 9 source-reported result (22:34–22:57) | October 10 observed evidence / later corroboration | State for an October 10 **complete remeasurement** |
| --- | --- | --- | --- |
| **WorkflowHub** | institution `457`, project `490`, person `1500`; workflows `2332/2334`, **v1–v3** each; public-page Activity **262 views / 17 downloads**; separate researcher-supplied dashboard **353 / 22** | Two **v4 version DOI registry** records independently confirmed by DataCite with 10/10 registration times. A direct structured **WorkflowHub v4/Activity-page** refresh is **not established** by this review | `DOI_EXPANSION_VERIFIED; WORKFLOWHUB_CURRENT_USAGE_NOT_REMEASURED` |
| **DataCite** | **50/50** known DOI direct GET 200/findable; **49** ORCID search hits, with beta `23166491` lacking ORCID; `citationCount=3`, `viewCount=0`, `downloadCount=0` across prior 50 | New **3** DOI metadata responses have been individually checked; public release DOI has same concept relation; existing OSF DOI `StudyRegistration` has canonical author ORCID plus an extra **noncanonical** creator identifier value reported in [October 10 public review](closeout-review-2026-10-10.md) | `NEW_3_VERIFIED; FULL_53_DOI_CENSUS_NOT_EXECUTED; COUNTER_TOTAL_NOT_REFRESHED` |
| **Zenodo** | Ten fixed families **873 views / 7 downloads**; audit control **49 / 0**; **30+2** version records (32 total) | Researcher-supplied **23:54** fixed ten **1,933 / 8**, separate audit control **74 / 3**, optional combined **2,007 / 11**; independent later public reads confirm all **11** concept families and **33** versions. See §3 | `LATER_NUMERIC_REPLICATION_CONFIRMED` (not timestamp-exact raw historical replay) |
| **OpenAlex** | Author `A5151904252` filtered Works **16**, author profile stale **43**, **48/50** known DOI appearances in `locations` by source method; v3 `2332.3/2334.3` absent in old DOI lookup | **18/18** filtered Works individually identifiable at **10/10 23:32–23:34**: 10 fixed concept Works + 1 control concept + OSF + 6 WorkflowHub **v1–v3 Work IDs**. At this later source state, both v3 Works present. `2332.4/2334.4` exact DOI query returned **0**. Full vs field-selected profile `works_count=30/16` conflicted; mechanism unknown | `AUTHOR_WORK_RELATION_CONFIRMED; PROFILE_COUNT_CONFLICT; V4_QUERY_NOT_OBSERVED`. Do **not** assert 18/53 from one simultaneous API instant: the third control DOI was registered **after** this Works extraction |
| **ORCID** | **14 groups / 60 work summaries** (DataCite 37; author-sourced 12; OpenAIRE 11), **48/50** source-reported DOI appearances; controlled omission of `2332.2/2334.1` from the ORCID Works collection | Public ORCID Works extraction later exposed strings for WorkflowHub **v4 DOI** values and other DOI relations, but **was flattened**, not safely parsed into groups/summaries. A newly exact ORCID count or comprehensive `/works` DOI coverage matrix is **not established** | `PARTIAL_PUBLIC_ASSOCIATION; GROUP_SUMMARY_RECOUNT_NOT_EXECUTED` |
| **OpenAIRE Graph** | Prior **33 DOI matches / 34 records** from 50 `pid` reads, with 17 source-reported not returned | October 10 separate public access attempt timed out; no comparable all-53-candidate enumeration | `UNRESOLVED_TIMEOUT`, **not zero and not unchanged** |
| **Software Heritage** | Earlier collector reported fixed-ten GitHub origins and Zenodo concept origins with visits, control GitHub origin 404; 21 origins visible | Later SWH public API attempt encountered protection challenge. The original origin-level outcomes must remain point-in-time observations, not rewritten as permanent preservation status | `ACCESS_CHALLENGED; NO_NEW_COMPLETE_VISIT_CENSUS` |
| **Research Software Directory** | **11** published software records, constellation project contains exactly **10** RS objects; audit-control separately cataloged | Public control software and ten-software constellation pages still retrievable in dated Oct10 review. RSD upstream issues [#1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870) and [#1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871) remain open in review | `PUBLIC_LISTINGS_VERIFIED; NO_INSTITUTIONAL_ENDORSEMENT` |
| **OSF** | Frozen public registration `5b329`; OSF project `wa5v8` private/not independently queried | Registration DOI visible as DataCite `StudyRegistration`, its Internet Archive `IsIdenticalTo` linkage readable; frozen contract remains unchanged | `REGISTRATION_PUBLIC; PROJECT_PRIVATE_STATUS_NOT_REMEASURED` |
| **Internet Archive** | Public OSF preregistration mirror `osf-registrations-5b329-v1`; old `downloads=0` | Mirror independently readable in Oct10 public review; download counter and full file inventory **not rerun** | `PUBLIC_MIRROR_VISIBLE; METRIC_NOT_REMEASURED` |
| **SciCrunch RRID** | `SCR_029105` resolver JSON read 200, source `validation.isValidated=false`, curator completion not established | Both public RRID search and official [Resource Report](https://scicrunch.org/resolver/SCR_029105) independently readable on Oct10, confirming identity and GitHub URL; old 10/07 pending state historically retained | `PUBLIC_INDEXED; CURATION_AND_ORCID_OWNERSHIP_UNVERIFIED` |
| **Crossref** | Source-reported **50/50** direct DOI Works GET 404 and **50/50** `agency=datacite`; ORCID filter 0 | No verified October 10 **53-DOI** repeat. DataCite agency vs Crossref works query have different contracts, and no-global-absence claim is allowed | `HISTORICAL_50_ONLY; ADDITIONAL_3_NOT_TESTED` |
| **Semantic Scholar** | Source-reported **50/50** direct DOI GET 404; batch POST failed/429; same-name author hits excluded | No matching Oct10 53-DOI repeat. Old 404s mean `DOI_QUERY_NOT_FOUND` at that past endpoint/time, not permanent non-indexing | `HISTORICAL_50_ONLY; ADDITIONAL_3_NOT_TESTED` |
| **GitHub** | Source-reported 11 repos' **14-day rolling traffic**, stars, clones; ten fixed repos latest releases all Oct04; account `public_repos=12` including external fork | Oct10 independent read-only release-list check **10/10 RS repositories** showed same three published Sep16/Sep30/Oct04 releases, **no eligible new fixed-corpus release in visible lists**. New **audit-control** GitHub release published 23:45:40; **Oct10 matching 14-day traffic census NOT RETAINED HERE** | `RELEASE_CHRONOLOGY_VERIFIED; TRAFFIC_UNRESOLVED` |
| **ROR** | Ten public `active` organization records, **not researcher affiliation** | No independently retained Oct10 ten-ROR recount; do not convert infrastructure operator identities into researcher employment or endorsement | `HISTORICAL_10_ONLY` |
| **Google Scholar / BASE / Dimensions** | Source-reported 403 / TLS or robot challenge / WAF or login 401; no bypass | No renewed access/evidence. Preserve `BLOCKED/UNRESOLVED`, never `0 indexed` | `ACCESS_GAP` |
| **rseng/RSE contributor integration** | Separate contributor-side metadata outreach (not one of seven operational scholarly platforms) | [rseng/software PR #498](https://github.com/rseng/software/pull/498) by `lostlight530` still **open**, `merged_at=null`, zero recorded reviews in Oct10 GitHub REST review; **no upstream acceptance** | `SUBMITTED_EXTERNAL_PR_NOT_MERGED` |

**Do not report** 2026-10-09 WorkflowHub Activity 262/17, DataCite 3 citations, ORCID 14/60, OpenAIRE 33/34, GitHub traffic 182/18611, Internet Archive downloads 0, or Semantic Scholar/Crossref `0/50` as **new October 10 readings**. They remain exactly the source-reported October 9 checkpoint until independently repeated with corresponding endpoint and denominator. A 403/404/429, bot challenge, timeout, API access denial, or empty search result remains a **query outcome**, not a blanket fact of non-existence.

## 3. Zenodo comparable family usage counters

| Population | Oct09 evening, original researcher-reported family values | Oct10 23:54 researcher-reported values | Delta within same family-count semantics |
| --- | ---: | ---: | ---: |
| RS01–RS10 family **views** | 873 | **1933** | **+1060** |
| RS01–RS10 Zenodo **file downloads** | 7 | **8** | **+1** |
| Separate audit-control concept family views | 49 | **74** | **+25** |
| Separate audit-control file downloads | 0 | **3** | **+3** |
| Optional descriptive 11-family **views** | 922 | **2007** | **+1085** |
| Optional descriptive file downloads | 7 | **11** | **+4** |

The 23:54 source values were **numerically repeated** in the Oct11 00:26–00:28 direct 33-version census, with all attached family aggregates consistent with their per-version sums. The earlier 22:11 RS07 anomaly is preserved: `23068494` attached family views `186`, three version views `45+33+7=85` (+101 mismatch); subsequently observed `150+34+12=196` for RS07 with all three reported family views also `196`. No causally established cache, counter, visitor, bot or ingestion mechanism. The fixed-ten later version sums are baseline **1535**, month-close **287**, October edition **111**, total **1933**. Family uniqueness is reported using attached `stats.unique_views`; never sum cross-version `version_unique_views` as deduplicated people, nor cross-repository uniqueness as a global audience.

The [Zenodo statistics definition](https://support.zenodo.org/help/en-gb/4-usage-statistics/15-what-is-a-view-download-data-volume) uses a **one-hour unique-view window** and counts record visits by humans **or machines**, excluding double-clicks and recognized robots; it does **not** imply a guaranteed count of distinct humans or establish traffic origin. More recent public counters may legitimately change. No causal explanation for the October 10 view surges is asserted.

## 4. Research design boundaries and follow-up

- **Cross-platform asymmetry is an observation**, not a defect to hide: DataCite registration, ORCID Works association, OpenAlex Work indexing and OpenAIRE PID matching are different public interfaces and separate observation contracts.
- The October 9 **controlled WorkflowHub** DOI cases `2332.2` and `2334.1` were deliberately omitted from the researcher's ORCID Works list, despite their DataCite creator ORCID. Preserve this distinction; do not automatically label an intentional ORCID non-entry as failed propagation.
- Versioned WorkflowHub DOI records are not scholarly works in one-to-one correspondence with the fixed RS software families; DataCite registered DOI count, OpenAlex Work count and ORCID grouped summaries have different units.
- The new audit-control release is **not RS11**, does not amend the OSF contract and does not instantiate the prospective longitudinal dataset; October 10 diagnostics stay in `monitoring/`.
- Unknown outcomes, earlier alternate failure routes and different-source/dated claims should remain historically inspectable. This report **does not** recapture the October 9 raw source archive or perform a full October 10 census of all platforms/53 DOIs. A future uniform DOI-coverage matrix must rerun every endpoint at a new correctly timestamped timepoint and report failures/missing coverage individually rather than manufacturing a complete October 10 matrix.

**Bounded result:** `OCTOBER_10_IDENTITY_FOOTPRINT_UPDATE_WITH_VERIFIED_DOI_EXPANSION_AND_PARTIAL_PLATFORM_REMEASUREMENT`. This is a **documentary and diagnostic** cross-platform reconciliation, with per-platform evidence scopes shown above, **not** a frozen retrospective reconstruction, complete 53-DOI coverage audit or eligibility-start claim.
