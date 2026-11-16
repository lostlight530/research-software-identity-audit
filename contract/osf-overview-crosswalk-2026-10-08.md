# OSF Overview → repository contract crosswalk (2026-10-08)

## Scope and authority

- **Study:** Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures
- **Registration:** [OSF 5b329](https://osf.io/5b329/overview) · DOI [10.17605/OSF.IO/5B329](https://doi.org/10.17605/OSF.IO/5B329)
- **Comparison source:** the researcher-supplied OSF Overview text in the 2026-10-08 collaboration, covering Research questions, foreknowledge, design, sampling, variables, indices, analysis, missing data, and other information.
- **Source boundary:** this is a clause-by-clause comparison to the supplied Overview, **not** an independently retrieved OSF version export or proof of the initial OSF revision's exact wording. The supplied `Other planned analysis` field displays **Updated**, but no OSF edit timestamp, change diff, or frozen-version history was supplied. Do not infer when or whether those words belonged to the initial registration.
- **Authority:** frozen OSF registration > dated substantive amendments > timestamped operational specification > explicitly exploratory/post hoc work. This crosswalk **does not modify** the registration, create an amendment, or authorize a new observation.

All legacy historical source files, baseline manifests, correction history, dated monitoring records, and local/retained response archives remain unchanged. Apparent differences below are recorded, not silently reconciled into historical success.

## Preregistered design and sample

| Supplied Overview clause | Repository representation | Assessment / operational boundary |
| --- | --- | --- |
| RQ1–RQ5; repeated object × layer × time observations | `contract/preregistration.md`; `analysis/README.md`; `templates/analysis-manifest.template.yaml` | Aligned in purpose. See question map below; do not present pre-eligibility snapshots as RQ findings from the new window. |
| Prospective, longitudinal, non-randomized and descriptive; no interventions or causal inference; no blinding | `contract/contract-map.yaml`; `contract/preregistration.md`; `analysis/README.md` | Aligned. Previous analyst exposure is explicitly disclosed by the supplied Overview; no claim of blinding or independent fresh-corpus analysis. |
| Fixed purposive **10** objects and six layers, **60** object-layer units per scheduled point | `corpus/object-manifest.csv`; `schema/infrastructure-layers.yaml`; `schema/counting-rules.md`; `tools/check.py` | Aligned. `research-software-identity-audit` is control/runtime, not RS11. |
| Public records and APIs, predeclared field mappings and source attribution | `schema/platforms.yaml`; `schema/observation.schema.json`; `templates/observation-record.template.json` | Operational seven-platform mapping is more granular than six registered layers; **70 possible object-platform checks are not 70 preregistered units**. |
| No new objects, layers, extra follow-up points, or dropped failed cells to improve results | `schema/counting-rules.md`; `schedule/README.md`; `AMENDMENTS.md`; `DEVIATIONS.md` | Aligned as stated policy. Additional institutional surfaces and benchmarks remain supplementary/exploratory. |

## RQ-to-analysis map

| RQ | Preregistered question | Planned evidence / output | Relevant repository surface |
| --- | --- | --- | --- |
| RQ1 | Which layers register, propagate, preserve, aggregate, or discover a **newly released** fixed software object, and in what observed order? | Layer-specific identifier/state traces, first qualifying post-release observations; tied or unobserved layers preserved | `schema/observation.schema.json`; `schema/infrastructure-layers.yaml`; `templates/analysis-manifest.template.yaml` |
| RQ2 | Does semantically comparable identity/metadata agree or diverge across layers? | `consistent` / `divergent` / `unresolved` comparisons with relation type, DOI/version, author/creator, archival origin and evidence | `schema/counting-rules.md`; `OPEN_RESEARCH.md` |
| RQ3 | How does **measurable** release-to-observation latency differ by layer? | `first qualifying directly observed downstream timestamp - release timestamp`; no imputation | `schema/counting-rules.md`; `schedule/README.md` |
| RQ4 | Do predefined family grouping or multiple source-summary patterns recur in the eligible prospective window? | Structural pattern comparison with historical baseline, source identity and counts; no treatment of multiple summaries as multiple research objects | `baseline/`; `schema/infrastructure-layers.yaml`; `analysis/README.md` |
| RQ5 | Which failed, not-found, limited, unresolved, partial or corrected states occur, and where is the **observable** boundary? | All attempted-cell outcomes, query status, failure reason, evidence and corrections; no automatic inference of underlying platform cause | `schema/state-taxonomy.yaml`; `schema/observation.schema.json`; `DEVIATIONS.md` |

**Clock interpretation for RQ1/RQ3:** an API's first **observed** representation time is not automatically the platform's internal ingestion, registration, publication, or state-transition timestamp. Unless a directly evidenced platform event timestamp exists and is comparable, report the **first detection at a sampled observation point**, not a precise backend propagation duration or causal mechanism. Respect retrieval windows, ties, unknown earlier appearances, clock/source type and timestamp precision.

## Measured-variable coverage (12 source categories)

| Supplied Overview variable | Existing fields or contract surface | Limitation that remains visible |
| --- | --- | --- |
| 1. Software object identity | `object_id` / `corpus/object-manifest.csv` | Fixed RS01–RS10 only |
| 2. Infrastructure layer | `infrastructure_layer`; `schema/infrastructure-layers.yaml` | Not interchangeable with seven platforms |
| 3. Release event timestamp | `release_event_timestamp`; batch `trigger_event` | Must cite eligible post-registration release evidence |
| 4. Retrieval timestamp | `retrieval_timestamp`; provenance/evidence manifests | Do not replace actual retrieval with logical cutoff |
| 5. Observation state | `observation_state`; `schema/state-taxonomy.yaml` | Preserve observed/not_found/rate_limited/unresolved/partially_verified/fully_verified; failed attempts are separately `attempt_status` |
| 6. Identifier type and values | `identifier_type`, `identifier_value`, `family_identifier`, `version_identifier` | A family/concept DOI is not a release-version DOI |
| 7. Identity/provenance | `creator_identifier`, `source_attribution`, `verification_mechanism`, `evidence_refs` | A single normalized field does not prove full attribution/record identity equivalence |
| 8. Aggregation and source composition | `aggregation_state` and retained ORCID response/summaries | The generic observation schema does **not** structurally enforce numeric group/source splits; preserve typed derived tables plus raw evidence when those analyses are made |
| 9. Discovery | `discovery_state`; OpenAIRE/OpenAlex distinct operational checks | Endpoint `not_found` ≠ global absence |
| 10. Preservation | `preservation_state`; SWH origin/release/directory evidence | Resolvability is not content/bytewise identity without supporting verification |
| 11. Platform response and pagination | `platform_response`, `pagination_complete`, `attempt_status`, `failure_reason` | Record HTTP 404/429/timeout/403 and limits literally; no silent promotion |
| 12. Correction/amendment events | `correction_event`, `amendment_ref`, `AMENDMENTS.md`, `DEVIATIONS.md` | Boolean marker alone does not replace a timestamped append-only correction history |

The existing JSON schema encodes a **single operational observation record**, not an entire study execution, source-summary table, or historical archive. Monitoring before eligibility remains in `monitoring/` with `pre_eligibility_monitoring` classification, **not** a synthetic prospective record. Do not add monitoring as a seventh layer or as extra registered observations merely to satisfy a schema.

## Six derived analyses and explicit exclusions

| OSF-derived index | Admissible result | Invalid shortcut |
| --- | --- | --- |
| Propagation latency | Comparable, directly observed release and first qualifying downstream observation timestamps | Imputing unqueried cells or equating first API read to an unevidenced ingestion timestamp |
| Propagation order | Observed chronology, ties preserved; missing layers left unordered | Inferring an intermediate layer's unseen ordering |
| Cross-layer consistency | Same identity relation only: consistent/divergent/unresolved | Declaring different semantic object types inconsistent |
| Aggregation recurrence | Same predefined group/source-summary pattern independently observed in the new eligible window | Treating historical or pre-eligibility repetition as prospective recurrence |
| State-transition sequence | Chronological categorical states with evidence and corrections | Converting states to a global quality score; overwriting earlier failures |
| Failure/partial frequency | Direct counts and proportions, retaining the full planned attempted-cell denominator where applicable | Dropping failures/unqueried/partial cases or silently changing denominator |

The study has **no** causal interpretation, inferential model, p-value/NHST/Bayes-factor criterion, ANOVA/regression/SEM, numerical normalization/centering, missing-value imputation, global score or outlier exclusion. These are guardrails, not an instruction to add statistical code.

## Eligibility, stopping and schedule: current unresolved operational prerequisite

The supplied Overview states:

1. Historical earlier release waves remain the fixed baseline.
2. **The first eligible post-registration new release event** triggers the prospective window; merely querying after registration is not sufficient.
3. Observation points/follow-up are predefined; after the final planned point is attempted for all ten objects and six layers, collection stops. Failed/unresolved attempts do not by themselves extend the window.
4. Extensions, procedural changes, or additional exploratory checks must be distinguished and governed as appropriate.

`schedule/README.md` currently says **no concrete operational offsets are declared**. The supplied Overview does not enumerate such offsets, and no timepoint list can be invented from this excerpt. This is an **unresolved pre-execution operational specification**, not proof that an unobserved schedule existed or that current monitoring was eligible. Any real schedule declaration requires its own prior timestamp and provenance; do not retroactively claim that specific offsets were frozen in OSF.

All 2026-10-06, 2026-10-07, and 2026-10-08 packages presently under `monitoring/` remain **pre-eligibility monitoring**, even where sources called them Wave 1/2/3 or prospective. A later valid eligible event cannot silently turn them into new-window results.

## Prior knowledge, missing states and exploratory analysis

- **Foreknowledge:** the supplied OSF form says the author previously observed relevant data and **cannot certify** any higher degree of independence from prior access. This is a documented study characteristic, not a defect to hide. Prior observations informed the contract; the prospective analysis itself was not yet carried out at registration.
- **No formal blinding/randomization**; failure of an endpoint, empty result, or HTTP 404/429 remains a bounded request outcome, not general non-existence. Missing/partial/unresolved results are retained without imputation.
- **Other planned analysis — Updated:** the supplied current Overview permits secondary exploratory/post hoc conceptual-family benchmarking, bounded platform-metric sensitivities, and tie-aware rank/percentile reports. The word `Updated` alone does **not** provide original-version text, revision date, or evidence that the added wording was frozen at first registration. Continue labeling the existing Zenodo benchmark and Agent cohort work **exploratory/post hoc**, not preregistered RQ findings.
- **UI placeholders:** `No files selected` and `No data` in the supplied OSF form are interface states in that text, not a basis to fabricate an attachment or observation.

## Alignment disposition

- **Aligned substantive contract:** N=10; six analytical layers and 60 planned units; repeat observations; no causal/inferential analysis or imputation; retain unresolved states and corrections; prospective starts only at a qualifying new release; research runtime outside sample.
- **Covered but not fully machine-typed:** detailed ORCID source-summary composition and richer provenance/correction chronology require raw evidence and auxiliary summaries, not inference from one schema string or boolean.
- **Unresolved / not invented:** exact operational offsets and initial-versus-updated OSF field revision provenance.
- **Change class of this document:** append-only explanation and traceability enhancement. No historical observation, frozen preregistration, schema vocabulary, schedule, or numerical analysis is modified.

Related authority: [frozen contract bridge](preregistration.md), [existing limitation record](known-limitations.md), [operational schedule](../schedule/README.md), [descriptive analysis](../analysis/README.md), [monitoring records](../monitoring/README.md).
