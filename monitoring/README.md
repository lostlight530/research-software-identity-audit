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


## October 18 later ORCID–OpenAIRE work update (user-attributed)

- [2026-10-18 / 02-orcid-openaire-work-refresh](2026-10-18/02-orcid-openaire-work-refresh/README.md) — researcher reports refreshing **11 ORCID links**, with **one explicit authenticated success receipt** for audit-control Beta DOI `10.5281/zenodo.23166491`. The user's ORCID Work detail displays **DataCite Software** (last modified 2026-10-09) vs **OpenAIRE Dataset** (last modified **2026-10-18**) for the **same DOI**. Public ORCID shows the DOI and source channels, but the post-click item timestamp and all other ten results were **not independently replayed**. No green-icon synchronization, new DOI, new sample, or prospective observation is inferred. [Machine summary](2026-10-18/02-orcid-openaire-work-refresh/record.json).

## October 18 11-hour monitoring, field-boundary and registry-catalogue checks
- [2026-10-18 / 01-eleven-hour-workflow-ci-crosscheck](2026-10-18/01-eleven-hour-workflow-ci-crosscheck/README.md) — public GitHub `life-science-ecosystem-lab` [PR #26](https://github.com/lostlight530/life-science-ecosystem-lab/pull/26) merge and [validate run #39092740134](https://github.com/lostlight530/life-science-ecosystem-lab/actions/runs/39092740134) have 5/5 jobs SUCCESS; separately attributed private LifeMonitor page shows 1 Passed with external dashboard verification blocked. User-supplied **ten RS Zenodo 1,533 unique views / 16 unique downloads**, and four WorkflowHub Team Dashboard assets **3,097 views / 276 downloads** (Dashboard Period/type not verified). **DataCite Commons 72 DOI Works** exactly reproduced by REST API (53 Software + 18 Workflow + 1 StudyRegistration); **OpenAlex author Works 29** is a distinct index. [Zenodo source table](2026-10-18/01-eleven-hour-workflow-ci-crosscheck/zenodo-user-page-counters.csv), [WorkflowHub source table](2026-10-18/01-eleven-hour-workflow-ci-crosscheck/workflowhub-dashboard-user-counters.csv), [DataCite verified queries](2026-10-18/01-eleven-hour-workflow-ci-crosscheck/datacite-orcid-works-query-results.csv), [OpenAlex IDs](2026-10-18/01-eleven-hour-workflow-ci-crosscheck/openalex-user-visible-work-identities.csv), [machine summary](2026-10-18/01-eleven-hour-workflow-ci-crosscheck/record.json), [source ledger](2026-10-18/01-eleven-hour-workflow-ci-crosscheck/source-attempts.csv). All are **diagnostic, not prospective**; private identifiers excluded.

## October 18 independent research verification

- [22:41–22:42 research-only diagnostic](2026-10-18/03-independent-research-verification/README.md) — 76 DOI enumeration, separate OpenAlex profile/query counts, fixed-ten checkpoint joins, archived Citation/CodeMeta byte inspection and supplementary software CI evidence

## October 19 bounded independent evening check

- [2026-10-19 / 01-evening-bounded-public-check](2026-10-19/01-evening-bounded-public-check/README.md) — fixed-ten GitHub Release/tag ref gate, DataCite count, OpenAlex profile/query discrepancy with two additional Work IDs, and paired Zenodo URL-variant counter conflict. Diagnostic only, no prospective cells.

## October 20 independent research recheck

- [Fixed-ten recheck and user-page reconciliation](2026-10-20/01-independent-research-recheck/README.md): 12/12 page/API unique pairs agree; 40 versions enumerated; OpenAlex 32/32; SWH checkpoint chains 2/10, full-origin visits 10/10 Post-review identity correction: [reconciliation note](../evidence/2026-10-20/01-independent-research-recheck/correction-reconciliation-01.md).

## October 21 bounded midday recheck

- [2026-10-21 / 01-midday-bounded-recheck](2026-10-21/01-midday-bounded-recheck/README.md) — public fixed-ten GitHub release/tag gate, DataCite count, OpenAlex profile/Works difference, Zenodo URL-variant statistics and SWH blocked revision retrieval; diagnostic only, zero prospective cells.

## October 21 evening all-version recheck

- [2026-10-21 / 02-evening-all-version-recheck](2026-10-21/02-evening-all-version-recheck/README.md) — fixed RS01–RS10 four-version audit (40 Zenodo records), 76 ORCID-linked DataCite DOI/type records and 32 OpenAlex Works/type records; diagnostic only, no prospective cells.

## October 22–23 bounded rechecks (separate source dates)

- [October 22 00:19 prior-chat 12-family Zenodo source transcription](2026-10-22/01-early-chat-snapshot-reconciliation/README.md) — retrospective selected-field transcript written October 23, not a historical raw HTTP capture and **not** the full October 22 day.
- [October 23 00:08–00:16 early public platform diagnostic](2026-10-23/01-early-public-infrastructure-recheck/README.md) — 12 Zenodo families / 45 version records; DataCite, OpenAlex, OpenAIRE, GitHub; ORCID and SWH degraded; zero prospective cells. No claim the rest of October 23 has happened.

## October 24 early review and source-bounded daily/weekly coverage

- [2026-10-24 early 12-repository recheck](2026-10-24/01-early-twelve-repository-public-recheck/README.md) — GitHub Releases/source-head split, Zenodo 45 versions, DataCite 76 DOI records, OpenAlex 32 Works, 10 OpenAIRE software queries, ORCID degraded and SWH not reattempted; zero prospective cells.
- [Twelve-repository daily and weekly source index](coverage/README.md) — release publication dates (Beijing) and actual source-covered family-view dates; no historical missing-day imputation.

## October 24 morning all-platform check and Zenodo family rollup

- [2026-10-24 / 02-morning-infrastructure-and-zenodo-family-rollup](2026-10-24/02-morning-infrastructure-and-zenodo-family-rollup/README.md) — same-day second bounded audit of seven contracted platforms plus supplementary institutional surfaces, with **12 one-row-per-family combined Zenodo counters** and 45 individual version DOI evidence rows; source-bound OpenAlex/ORCID/SWH and institutional failure states retained; zero prospective cells.

## October 24 offline family-statistics check

- [2026-10-24 / 03-offline-family-stat-replay](2026-10-24/03-offline-family-stat-replay/README.md) — read-only validator for the existing 12-family and 45-version selected-field snapshots and their 2,681/2,836 URL-shape discrepancy; no fresh observation or prospective cells.

- [2026-10-24 / 04-local-history-evidence-handoff](2026-10-24/04-local-history-evidence-handoff/README.md) — attributed local evidence from the Oct01 user-reported node and Oct03 facility audit through the Oct24 midnight capture; original clocks, failures, public-field projections and canonical RS reconciliation retained; cloud review pending, zero prospective cells.

- [2026-10-24 / 05-post-handoff-integrity-recheck](2026-10-24/05-post-handoff-integrity-recheck/README.md) — independently rechecked 12 public GitHub Release lists after PR #59, added bounded offline handoff transfer integrity checks, retained six unrefreshed platform states under earlier dated reports; zero new prospective cells.

## October 25 bounded seven-platform diagnostic

- [2026-10-25 / 01-bounded-seven-platform-recheck](2026-10-25/01-bounded-seven-platform-recheck/README.md) — 12 GitHub Release lists, 12 Zenodo families / 45 versions, DataCite 76 DOI records, OpenAIRE 10 exact software DOI matches, OpenAlex 21/30/32 profile query-shape conflict, ORCID flattened and SWH blocked; source-scoped, zero prospective cells.

## October 25 later independent institutional recheck

- [2026-10-25 / 02-independent-institutional-recheck](2026-10-25/02-independent-institutional-recheck/README.md) — 162 timestamped attempts; twelve page/API unique pairs match, 76 DOI records, structured ORCID 17/89, SWH four current release chains, source-separated WorkflowHub counts; diagnostic only, zero prospective cells

## October 26 institutional checklist rechecks

- [2026-10-26 / 01-morning-institutional-recheck](2026-10-26/01-morning-institutional-recheck/README.md) — 405 timestamped attempts; 34 supplemental surfaces, 77 identified DOI records, 12-family fields; diagnostic only, zero prospective cells
- [2026-10-26 / 02-evening-institutional-recheck](2026-10-26/02-evening-institutional-recheck/README.md) — 384 timestamped attempts; 34 supplemental surfaces, 77 identified DOI records, 12-family fields; diagnostic only, zero prospective cells

- [2026-10-27 / 01-bounded-seven-platform-recheck](2026-10-27/01-bounded-seven-platform-recheck/) — GitHub Release-list census and bounded official-platform field extraction; selected Zenodo/OSF/DataCite/ORCID/SWH/OpenAIRE/OpenAlex diagnostics; unresolved OpenAlex query-shape conflict, blocked SWH control read; zero prospective cells

## October 29 bounded contract and source-access recheck

- [2026-10-29 / 01-bounded-contract-recheck](2026-10-29/01-bounded-contract-recheck/README.md) — 11 fresh GitHub Release-list checks plus seven external-source access attempts with acquisition-date limits; GitHub counts unchanged within Release-list scope, external freshness not certified, zero prospective cells

- [2026-10-29 / 02-independent-release-gate-recheck](2026-10-29/02-independent-release-gate-recheck/README.md) — independent connected-GitHub API pass over all 11 published Release lists with a directly measured client-side tool envelope and 11-row selected-field ledger; identical bounded Release-list fields to the earlier diagnostic. The earlier [01 clock-provenance correction](2026-10-29/01-bounded-contract-recheck/clock-provenance-correction.md) remains authoritative for its unsupported timing claims. External-platform and OSF revision checks remain unresolved; zero prospective cells.


## October 30 OSF original-versus-revised contract-text reconciliation

- [2026-10-30 / 01-osf-schema-response-version-reconciliation](2026-10-30/01-osf-schema-response-version-reconciliation/README.md) — public OSF API comparison of **two approved Schema Response versions**, with a 29-key comparison and **only `344-83` (Other planned analysis) changed**. Original and revised wording, version identity/time fields, the revision author's justification and collector/clock limitations are retained separately. This resolves a **previously unknown original-version field difference**, without rewriting the 2026-10-08 crosswalk, amending the OSF contract, backdating exploratory analyses or producing prospective cells.

## October 30 bounded periodic 34-surface source-access check

- [2026-10-30 / 02-bounded-periodic-infrastructure-recheck](2026-10-30/02-bounded-periodic-infrastructure-recheck/README.md) — current GitHub 11-core Release/PR check plus 34 existing institutional/service/standard surface-row representative attempts; extractor acquisition age and six access failures retained, without inventing a contemporaneous full seven-platform census. Includes a dated Oct 5–30 control-runtime timeline; zero prospective cells.

## Existing October 30–31 diagnostic entries (index reconciliation)

- [2026-10-30 / 03-post-audit-github-delta](2026-10-30/03-post-audit-github-delta/README.md) — pre-existing dated GitHub delta record, linked without reconstructing its original retrieval clock
- [2026-10-30 / 04-tag-ref-and-source-shape-recheck](2026-10-30/04-tag-ref-and-source-shape-recheck/README.md) — pre-existing tag-reference and query-shape diagnostic, not a new prospective event
- [2026-10-31 / 01-bounded-research-identity-and-infrastructure-recheck](2026-10-31/01-bounded-research-identity-and-infrastructure-recheck/README.md) — earlier October 31 release/identity and 34-surface bounded check, retained at its original timestamp

## October 31 noon user-page reconciliation

- [2026-10-31 / 02-noon-user-page-reconciliation](2026-10-31/02-noon-user-page-reconciliation/README.md) — source-separated 13:00 Dashboard, 13:24 Zenodo, DataCite Commons and OpenAIRE counts; prior API fields labelled by their actual capture time; zero prospective cells

## October 31 independently retained statistics

- [2026-10-31/03-independent-institutional-statistics](2026-10-31/03-independent-institutional-statistics/README.md) — actual 12:00 capture, 473 read attempts, source-scoped 34 surfaces, 88 DOI inventory and OpenAIRE DOI grouping
- [2026-10-31/04-zenodo-all-version-statistics](2026-10-31/04-zenodo-all-version-statistics/README.md) — actual 13:41 all-version capture, 55 versions, 48 family-field reconciliations and same-record deltas

## October 31 evening periodic identity/infrastructure recheck

- [2026-10-31 / 05-evening-periodic-identity-recheck](2026-10-31/05-evening-periodic-identity-recheck/README.md) — independent GitHub all-eleven main/PR/Release pass and ten exact SHA compares (**109 added main-reachable Git commits in total, 44 two-tree affected paths**, unchanged fixed-corpus Release counts), ten-object Zenodo/DataCite version DOI extraction and SWH visit-date check, bounded OpenAIRE/OpenAlex semantics, 34-surface cache-age/failure ledger, upstream status and OSF revision boundary. **Diagnostic only; no new source-origin raw HTTP bytes, no prospective cells, no frozen-contract edit or new Release/DOI**.

## November 1 bounded identity and infrastructure patrol

- [2026-11-01 / 01-periodic-identity-infrastructure-recheck](2026-11-01/01-periodic-identity-infrastructure-recheck/README.md) — eleven fresh GitHub main and open PR/Release checks, ten fixed-corpus source SHA changes with exact comparison ledger, 34 external surface access attempts with cached/error boundaries, existing seven-platform DOI evidence, and the **already-published** fifth CONTROL version DOI plus dated citation drift reconciliation. Diagnostic only; not an eligible prospective observation, additional sample, or new DOI created by this check.

- [2026-11-01 / 02-followup-identity-infrastructure](2026-11-01/02-followup-identity-infrastructure/README.md) — independent same-day post-PR-#80 source-snapshot follow-up, **one RS03 main change** (two commits, one path, original A2 blocked), 11 tag/Release/PR crosschecks, seven-platform identity representations and 34 exact source-access attempts; **source-clock race documented, no new fixed Release/DOI, no scientific source correction, no prospective cells**.
- [2026-11-01 / 03-openalex-version-query-scope](2026-11-01/03-openalex-version-query-scope/) — 10 exact version-DOI OpenAlex lookup excerpts returned concept-primary Work DOI; version-level Work identity remains unproven, diagnostic only

## November 2 independent recheck and retained local completion

- [2026-11-02/01-complete-institutional-recheck](2026-11-02/01-complete-institutional-recheck/README.md) — 34 service rows, 90 DOI attempts and partial OpenAIRE results; diagnostic/retrospective only, zero prospective cells
- [2026-11-02/02-all-version-recheck](2026-11-02/02-all-version-recheck/README.md) — 57 Zenodo versions and 48 family joins; diagnostic/retrospective only, zero prospective cells
- [2026-11-02/03-retained-local-evidence-completion](2026-11-02/03-retained-local-evidence-completion/README.md) — source-dated local coverage inventory and missing selected fields; diagnostic/retrospective only, zero prospective cells

- [2026-11-02 / attempt-ledger column-semantic reconciliation](2026-11-02/01-complete-institutional-recheck/source-attempts-column-reconciliation.md) — append-only clarification that the published `source-attempts.csv` column labeled `platform` actually contains 1–34 surface IDs; the original source bytes, manifest, attempt outcomes and scientific denominator remain unchanged

## November 3 bounded identity and infrastructure recheck

- [2026-11-03 / 01-bounded-identity-infrastructure-recheck](2026-11-03/01-bounded-identity-infrastructure-recheck/README.md) — 11 current core main/PR/Release/tag reads and source-pinned SHA comparisons against the previous explicitly retained main-head ledger, 34 exact supplementary URL attempts with cached/failure states, seven-platform evidence-freshness boundaries, current RSE/RSD interaction states, and CI status limits. Append-only diagnostic; **no new preregistered cells, DOI, Release or frozen-contract change**.

## November 3 full-history semantic correction

- [2026-11-03 / 02-source-attempt-surface-id-reconciliation](2026-11-03/02-source-attempt-surface-id-reconciliation/README.md) — derived 482/482 attempt-key to numeric surface-ID / 34-surface-name correction of the **November 2** original source-attempt ledger, original two Git blobs and retrieval clocks preserved, 0 unmatched dictionary keys. This does not create new HTTP attempts, a scheduled prospective study cell, an analytical layer or an OSF amendment
- [First-day-to-current file and Git history classification](../docs/research-control-first-day-to-current-governance-audit-2026-11-03.md) — pinned retrospective 104-commit / 620-file / 58-event inventory and original-versus-revised OSF authority mapping; the later derived event is not backfilled into the pinned source snapshot

## November 4 bounded periodic identity and institution recheck

- [2026-11-04 / 01-periodic-identity-infrastructure-recheck](2026-11-04/01-periodic-identity-infrastructure-recheck/README.md) — 11 current core GitHub main/PR/release selected fields, exact 34 pre-existing service/standard URL extraction attempts with acquisition-day and six retained errors, selected comparable Zenodo RS01 counter delta, RSE/RSD independent upstream statuses and strict non-prospective contract boundary; no new DOI, release or scientific-source repair. The machine record and ledgers are source-bounded, not a current 90-DOI or seven-platform full census

## November 5 bounded identity and infrastructure recheck

- [2026-11-05 / 01-bounded-identity-infrastructure-recheck](2026-11-05/01-bounded-identity-infrastructure-recheck/README.md) — eleven current main/PR/Release comparisons against explicitly dated Nov 4 source SHAs, 34 exact supplementary URL extraction attempts with source acquisition-day limits and six retained errors, selected RS01 Zenodo attached-family +5 views / 0 downloads, unchanged RSE/RSD PR/Issue states, and official OSF Project read-only policy notice. Dated diagnostic only; **zero prospective observations, no new DOI or Release, no frozen-contract change**.

## November 6 bounded identity and infrastructure recheck

- [2026-11-06 / 01-periodic-identity-infrastructure-recheck](2026-11-06/01-periodic-identity-infrastructure-recheck/README.md) — eleven connected GitHub mains, five Draft PRs, ten fixed sample mains advanced 359 commits in total against Nov 5 source SHA ledger with zero new published Release, 34 exact surface URL attempts retaining six errors and 27 cached older representations, selected RS01 Zenodo attached family views +17 / downloads +0, unchanged independent RSE/RSD interaction states, a raw-response retention rate-limit gap, and a date-neutral advisory checker fix. **Diagnostic only, zero prospective cells and no OSF/DOI/Release rewrite**.

## November 7 bounded identity and infrastructure recheck

- [2026-11-07 / 01-periodic-identity-infrastructure-recheck](2026-11-07/01-periodic-identity-infrastructure-recheck/README.md) — 11 pinned GitHub main/PR/Release comparisons, exact 34-surface source-access ledger with date-bounded extractor representations and six retained errors, selected RS01 Zenodo family views +4, institution-facing status checks and explicit 0 prospective units. The [dated November 7 compatibility reconciliation](2026-11-07/01-periodic-identity-infrastructure-recheck/reconciliation.md) corrects the diagnostic CSV/machine-summary schema without pretending new provider evidence or rewriting the original October historical sources

## November 8 end-of-day pages and independent institutional recheck

- [2026-11-08/01-end-of-day-user-pages](2026-11-08/01-end-of-day-user-pages/README.md) — user Zenodo cards, WorkflowHub Dashboard and 15 OpenAIRE ORCID links; diagnostic only, zero prospective cells
- [2026-11-08/02-complete-institutional-recheck](2026-11-08/02-complete-institutional-recheck/README.md) — 34 surfaces, 92 DOI queries, 17 distinct OpenAIRE IDs and source attempt clocks; diagnostic only, zero prospective cells
- [2026-11-08/03-all-version-recheck](2026-11-08/03-all-version-recheck/README.md) — 57 Zenodo versions, 48 field joins and separate family/version counters; diagnostic only, zero prospective cells

## November 9 bounded identity and infrastructure recheck

- [2026-11-09 / 01-periodic-identity-infrastructure-recheck](2026-11-09/01-periodic-identity-infrastructure-recheck/README.md) — eleven exact main/PR/release checks against November 7 pinned SHAs, 34 pre-existing services and standards with 28 dated excerpts and six retained errors, one November 9 RS01 Zenodo comparable family counter (+3 views), independent RSE/RSD status checks and explicit zero prospective observations. No source repair, DOI or Release; prior November 8 full cross-platform capture remains a separate historical observation

## November 10 bounded identity and infrastructure recheck

- [2026-11-10 / 01-periodic-identity-infrastructure-recheck](2026-11-10/01-periodic-identity-infrastructure-recheck/README.md) — current eleven GitHub main/PR/Release SHA comparison (+183 fixed-corpus main-reachable commits since Nov 9, no Published Release), 34 established service/standard URL access outcomes with six retained errors and dated caches, selected Nov 10 RS01 Zenodo family views +2, institution-facing unchanged RSE/RSD states and explicit zero prospective cells. No OSF, release, DOI, baseline or schema change

## November 10 OSF preregistration usage metric

- [2026-11-10 / 02-osf-registration-usage](2026-11-10/02-osf-registration-usage/README.md) — OSF-reported DataCite usage event for preregistration DOI 10.17605/osf.io/5b329: 30 `unique-dataset-investigations-regular` during October 2026. Supplementary diagnostic signal only; not an RS01–RS10 object-layer observation or prospective cell


## November 10 user-supplied OpenAIRE, OpenAlex and ORCID-link reconciliation

- [2026-11-10/03-openaire-orcid-openalex-reconciliation](2026-11-10/03-openaire-orcid-openalex-reconciliation/README.md) — maintainer-supplied OpenAIRE PID UI counts (13 / 8 / 10 / 4), OpenAlex author profile Works 33 and Work `W7220380722`, plus the OpenAIRE “My ORCID links” 15-link page showing RS01–RS10 DOI families. Includes the RS01 four-DOI / one-OpenAIRE-result-ID aggregation case. Source capture time unknown; UI/API surfaces are not treated as directly comparable; diagnostic only, zero prospective cells.

- [2026-11-12 / 01-identity-claim-reconciliation](2026-11-12/01-identity-claim-reconciliation/) — independent public-source recheck and separately attributed OpenAIRE claim reconciliation
