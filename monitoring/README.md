# Monitoring

This directory stores useful measurements that occur outside the eligible
prospective dataset.

A monitoring record can be methodologically valuable without being promoted to a
scheduled prospective observation.

Use this area for:

- pre-eligibility propagation checks;
- infrastructure self-observation;
- post-baseline state checks before the first eligible fixed-corpus release;
- diagnostic captures whose timing does not satisfy the operational prospective schedule.

Monitoring records must preserve true retrieval time and must not be relabeled
later as preregistered prospective observations.


Post-release reconciliation records may also be stored here when they observe
the research-control repository or scholarly infrastructure before an eligible
fixed-corpus release begins the prospective dataset.

## Records by observation day

- [2026-10-06 / 01-wave-01](2026-10-06/01-wave-01/) — first pre-eligibility monitoring, not a preregistered wave
- [2026-10-06 / 02-openaire-link-attempt](2026-10-06/02-openaire-link-attempt/) — manual link attempt with bounded outcome
- [2026-10-06 / 03-reconciliation](2026-10-06/03-reconciliation/) — later reconciliation, original timestamps retained
- [2026-10-07 / 01-facility-audit](2026-10-07/01-facility-audit/) — supplied cross-platform audit and mapping reconciliation
- [2026-10-08 / 01-morning-recheck](2026-10-08/01-morning-recheck/) — morning monitoring plus separately imported retained evidence

For path rules and the complete old-to-new inventory, see [naming and migration](NAMING.md) and [path mapping](path-migration-2026-10-08.csv).

The date is the record's source-observation date, not necessarily its retrieval or evidence-import date. Ordinals order packages within a date and are **not** prospective-wave identifiers.

- [2026-10-09 / 01-facility-recheck](2026-10-09/01-facility-recheck/) — Independent facility and counter recheck

## October 10 diagnostic and interpretation records

- [2026-10-10 / 01-zenodo-surge-recheck](2026-10-10/01-zenodo-surge-recheck/) — source collector's original point-in-time Zenodo counters and the separately attributed corrective review; this is **not** an eligible prospective observation
- [2026-10-10 / 02-reconciliation](2026-10-10/02-reconciliation/independent-version-verification.md) — independently reviewed 11 concept families / 32 versions, the [32-row extract](2026-10-10/02-reconciliation/version-counters-independent.csv), and unresolved RS07 aggregate-field disagreement

The 01 original report and the 02 earlier `interpretation.md` have distinct author/provenance identity. The independent reviewer **does not adopt** the earlier suggestion of an identified Zenodo aggregation mechanism; it is a working hypothesis. Across October 9–10 the retained prior capture does not provide a matching 32-version enumeration, so per-version historical interval increments remain **NOT_DERIVABLE**. For the bounded version-counting procedure see [counting rules](../schema/counting-rules.md#supplementary-zenodo-version-family-reconciliation-2026-10-10).

- [2026-10-10 / 03-openalex-work-aggregation](2026-10-10/03-openalex-work-aggregation/README.md) — independent author-filtered OpenAlex Works listing (**18 distinct DOI/Work records**), including six version-specific WorkflowHub Works; DataCite v4 DOI visibility vs OpenAlex v4 query non-observation, ORCID structural-count gap, and author profile counts 16/30 kept distinct. This is a **diagnostic** aggregation record, not a new RS object or prospective observation.

## October 11 independent full-version counter recheck

- [2026-10-11 / 01-zenodo-33-version-recheck](2026-10-11/01-zenodo-33-version-recheck/README.md) — later independent verification of the user-reported **October 10 23:54** Zenodo counting guide: 11 concepts, 33 direct version records, 1,933 fixed-ten views / 8 downloads, 74 independent control views / 3 downloads, and an observed resolution of the earlier RS07 attached-family field conflict. The original source report and later API capture remain distinct; historical byte-level replay and internal traffic/aggregation causes remain **UNVERIFIED**.

## 2026-10-13 noon independent review — research-control repository only

- [2026-10-13 / 01-control-noon-recheck](2026-10-13/01-control-noon-recheck/README.md) — **actual retrieval 12:47:55.192–12:51:01.217 Asia/Shanghai**, not 12:00:00. Independent seven-operational-platform control-only review; [37 source/attempt ledger rows](2026-10-13/01-control-noon-recheck/platform-attempts.csv), [9 direct Zenodo version-stat field rows](2026-10-13/01-control-noon-recheck/zenodo-version-attempts.csv), and a bounded [machine summary](2026-10-13/01-control-noon-recheck/record.yaml). Zenodo first returns conflicting attached family counters **91/51/74** then independent repeated three-version reads and two enumerations all agree **91 views, 87 unique-view count, 3 downloads**. OpenAIRE exact latest version DOI visible, exact concept PID query zero; OpenAlex author list **24** while profile `works_count` read forms still conflict. SWH, ORCID group reconstruction, GitHub traffic and OSF structured read gaps retained. This adds **no RS11**, releases, retrospective rewrite or eligible prospective observation.

## 2026-10-13 evening fixed-corpus public release gate

- [2026-10-13 / 02-fixed-corpus-release-gate](2026-10-13/02-fixed-corpus-release-gate/README.md) — 19:44 Asia/Shanghai independent public GitHub Release-list queries for all fixed `RS01–RS10`: each latest returned published release dates to October 4, so no new post-registration **public GitHub Release** observed. Ten public Git tag-list calls were connector-blocked and remain `NOT_VERIFIED`; this does not establish an exhaustive eligible-event absence or start the prospective study. The [20-attempt source ledger](2026-10-13/02-fixed-corpus-release-gate/source-attempts.csv) retains the exact source URLs and bounded retrieval windows.

## October 14 preflight integrity and fixed-ten tag-ref check

- [2026-10-14 / 01-preflight-integrity-recheck](2026-10-14/01-preflight-integrity-recheck/README.md) — read-only preflight: all ten current GitHub Release **and Git tag-ref** lists parsed (previous day's unsupported tag path remains historically blocked), no new public release observed; separately retained Zenodo bare-field inconsistency versus later family/version match (94/90/3), DataCite reverse-link asymmetry, OpenAlex author query/profile differences (26/24/30), and OSF's publicly displayed Oct 6 update notice without claiming an original-to-updated field diff. External extractor rate-limit blocks preserved; **not prospective**.

## October 14, 21:00-hour full control preflight and ten new release eligibility candidates

- [2026-10-14 / 02-control-evening-recheck](2026-10-14/02-control-evening-recheck/README.md) — seven-platform control-repository diagnostic; [62 source/attempt entries](2026-10-14/02-control-evening-recheck/platform-attempts.csv), [10 fixed-corpus GitHub Release / DataCite DOI joins](2026-10-14/02-control-evening-recheck/release-candidate-crosswalk.csv), [machine summary](2026-10-14/02-control-evening-recheck/record.yaml). All ten fixed RS objects have a new October 14 published fourteen-day checkpoint: **post-registration release eligibility candidate**, not authorization to backdate a prospective timepoint. Control DataCite Concept DOI now returns 3 HasVersion links, OpenAlex author list/selected/full count each 26; Zenodo current counters timed out, ORCID structured groups unavailable, SWH bot challenged. Frozen OSF registration, baseline, schedule, schema and prospective dataset unchanged.

## October 14 retained diagnostics and user pages

- [2026-10-14 / 03-midnight-facility-recheck](2026-10-14/03-midnight-facility-recheck/README.md) — 00:04–00:16 independent API capture, incomplete Zenodo counters retained as null
- [2026-10-14 / 04-morning-facility-recheck](2026-10-14/04-morning-facility-recheck/README.md) — 08:03–08:07 independent API capture; 33 version records and 40 DOI routes
- [2026-10-14 / 05-noon-user-pages](2026-10-14/05-noon-user-pages/README.md) — user-labelled noon Zenodo unique counters and WorkflowHub Dashboard; exact time/Period unknown

## October 14 evening new-release propagation

[Evening diagnostics and new-version evidence](../monitoring/2026-10-14/06-evening-facility-recheck/README.md) preserve ten new public releases, 72 findable DOIs, 15 ORCID groups / 85 sources and 43 enumerated versions; user pages and independent captures remain separate

## October 15 morning diagnostic recheck

[Full morning record](../monitoring/2026-10-15/01-morning-facility-recheck/README.md) retains 27 author-query Works, 84 ORCID source summaries, 72 DOI records and source-specific counter reconciliation; earlier captures remain dated

## October 16 noon: 11 family Zenodo total vs unique counters and cross-platform verification
- [2026-10-16 / 01-noon-counter-contract-recheck](2026-10-16/01-noon-counter-contract-recheck/README.md) — independently extracted [eleven Zenodo family counters](2026-10-16/01-noon-counter-contract-recheck/zenodo-family-api-stats.csv): **fixed ten 2,283 total / 1,449 unique views**, separately **control 103 / 96**, descriptive all-eleven sum **2,386 / 1,545**; downloads **20 total / 19 unique**. Control latest standalone API reply **74 / 71** conflicted with full 3-version family response **103 / 96** and remains recorded. [User-attributed WorkflowHub Dashboard](2026-10-16/01-noon-counter-contract-recheck/workflowhub-dashboard-user-extract.csv) lists three assets totaling 2,511 shown views / 204 shown downloads, with selected period unknown. [59 source/read paths](2026-10-16/01-noon-counter-contract-recheck/source-attempts.csv) and [machine summary](2026-10-16/01-noon-counter-contract-recheck/record.json) retain OpenAlex Works **29 vs author profile 26**, blocked SWH and incomplete ORCID structured read. **Only diagnostic preflight**: 11 software families are not 11 OSF analytical samples; no historic baseline rewrite, schedule declaration or prospective timepoint.

## October 17 field-boundary and cross-platform catalogue recheck
- [2026-10-17 / 01-field-boundary-cross-platform-recheck](2026-10-17/01-field-boundary-cross-platform-recheck/README.md) — re-parsed ten Zenodo public record pages as separate labelled unique-view / unique-download fields (**1,511 / 16** summed over RS01–RS10), compared with the October 16 API unique fields (**1,449 / 16**) without claiming event-time precision; retains the separately reported control page as partial because its counter fields were not extracted. Confirms four WorkflowHub identities under project 490, including the new 2347 workflow; records an unresolved 2334 date-field difference without choosing a source. Captures public bio.tools ID `life-science-protein-file-audit` and notes source-repository README drift. [Machine summary](2026-10-17/01-field-boundary-cross-platform-recheck/record.json), [Zenodo field extract](2026-10-17/01-field-boundary-cross-platform-recheck/zenodo-page-field-extract.csv), [WorkflowHub identity extract](2026-10-17/01-field-boundary-cross-platform-recheck/workflowhub-asset-identities.csv), [20-entry source ledger](2026-10-17/01-field-boundary-cross-platform-recheck/source-attempts.csv). **Diagnostic only**: no OSF contract changes, schedule offsets, or prospective cells.

## October 18 11-hour monitoring, field-boundary and registry-catalogue checks
- [2026-10-18 / 01-eleven-hour-workflow-ci-crosscheck](2026-10-18/01-eleven-hour-workflow-ci-crosscheck/README.md) — public GitHub `life-science-ecosystem-lab` [PR #26](https://github.com/lostlight530/life-science-ecosystem-lab/pull/26) merge and [validate run #39092740134](https://github.com/lostlight530/life-science-ecosystem-lab/actions/runs/39092740134) have 5/5 jobs SUCCESS; separately attributed private LifeMonitor page shows 1 Passed with external dashboard verification blocked. User-supplied **ten RS Zenodo 1,533 unique views / 16 unique downloads**, and four WorkflowHub Team Dashboard assets **3,097 views / 276 downloads** (Dashboard Period/type not verified). **DataCite Commons 72 DOI Works** exactly reproduced by REST API (53 Software + 18 Workflow + 1 StudyRegistration); **OpenAlex author Works 29** is a distinct index. [Zenodo source table](2026-10-18/01-eleven-hour-workflow-ci-crosscheck/zenodo-user-page-counters.csv), [WorkflowHub source table](2026-10-18/01-eleven-hour-workflow-ci-crosscheck/workflowhub-dashboard-user-counters.csv), [DataCite verified queries](2026-10-18/01-eleven-hour-workflow-ci-crosscheck/datacite-orcid-works-query-results.csv), [OpenAlex IDs](2026-10-18/01-eleven-hour-workflow-ci-crosscheck/openalex-user-visible-work-identities.csv), [machine summary](2026-10-18/01-eleven-hour-workflow-ci-crosscheck/record.json), [source ledger](2026-10-18/01-eleven-hour-workflow-ci-crosscheck/source-attempts.csv). All are **diagnostic, not prospective**; private identifiers excluded.
