# Identity Propagation of Research Software Across Open Scholarly Infrastructures

**Subtitle:** An Auditable Case Study and Preregistered Longitudinal Research Framework

**Author:** Xuan yi Jiang · Independent Researcher  
**ORCID:** 0009-0001-3617-0832  
**Manuscript status:** Working revision, 19 November 2026  
**Article type:** Empirical case study / research infrastructure study

## Abstract

Research software can acquire multiple scholarly identities as it moves from a source repository into archival repositories, identifier registries, author registries, preservation archives, and discovery graphs. These infrastructures represent different object types and apply different matching, aggregation, and update rules. A DOI, an author-registry summary, a preservation snapshot, and a discovery-graph Work are therefore not interchangeable observations of one uniform record.

This paper reports an auditable historical case involving ten research-software repositories observed across three release waves from 16 September to 4 October 2026. At the retained 3–4 October snapshot, forty DataCite-registered DOIs represented ten software families and thirty version records. The fixed-corpus subset of the author's ORCID record contained fifty-two work summaries grouped into ten groups: thirty-two DataCite-origin summaries, ten OpenAIRE-origin summaries, and ten author-added summaries. Third-party source summaries therefore outnumbered author-added summaries 42 to 10, a ratio of 4.2:1. Software Heritage recorded ten archived origins; all ten had full snapshots at the 3 October audit, while the 4 October recheck fully verified two chains and partially verified one. All ten September-version DOIs matched in OpenAlex within the 3–4 October capture. October-version queries were not part of that capture; a separate 6 October baseline reconciliation later recorded ten latest-version records found in OpenAlex.

The paper distinguishes this historical case from later read-only diagnostics. On 18 November 2026, a fixed 458-key public-source diagnostic produced 402 HTTP-200 attempts without recorded failure and 56 failed or partial attempts. It reported 102/102 successful DataCite requests, 94/102 positive OpenAIRE DOI queries, 34 exact canonical OpenAlex DOI matches, and 18 ORCID groups containing 119 work summaries. Zenodo's sixty-version aggregate remained unknown because the diagnostic retrieved only 21 of 67 version requests successfully. These later figures are diagnostic source checks, not prospective repeated-measures observations and not replacements for the historical snapshot.

The study's frozen OSF contract defines ten fixed objects, six analytical layers, and sixty object-layer units per eligible scheduled timepoint. The research-control repository is not an eleventh sample object. As of 19 November, no concrete operational observation offsets are declared and no prospective cells have been added. The paper's contribution is therefore a bounded empirical account, a transparent cross-platform object model, and an explicit longitudinal design whose future claims remain conditional on eligible releases, a declared schedule, and source-level evidence.

**Keywords:** research software; scholarly infrastructure; identity propagation; DOI; ORCID; DataCite; OpenAIRE; OpenAlex; Software Heritage; longitudinal audit

---

## 1. Introduction

Research software is increasingly treated as a citable scholarly output, but its identity is distributed across systems that were not designed around one shared object model. A source repository exposes branches, tags, commits, and releases. An archival repository exposes version records and family-level identities. An identifier registration agency exposes metadata and directed relationships. An author registry exposes work groups and source-attributed assertions. A preservation archive exposes origins, visits, snapshots, and content-addressed identifiers. Discovery graphs ingest, match, merge, and expose records according to their own pipelines.

The central research problem is not simply whether a software DOI can be found. It is whether a specific object can be followed across infrastructures without confusing identifiers, source assertions, grouped summaries, archive snapshots, or discovery representations. This paper examines that problem through a historical case and documents the boundary between the case and a separately preregistered prospective study.

The analysis follows the FAIR principles for research software and the FORCE11 software citation principles, particularly persistent identification, attribution, accessibility, and version specificity [1, 2]. It does not treat discoverability as a proxy for scientific validity or adoption.

## 2. Research questions and design

The frozen OSF registration, titled *Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures*, was registered on 5 October 2026 [3]. Its five primary questions concern:

- **RQ1 — Propagation:** which infrastructure layers register, propagate, preserve, aggregate, or discover each newly released object, and in what directly observed temporal order?
- **RQ2 — Cross-layer consistency:** whether semantically comparable identity and metadata fields remain consistent across layers or diverge;
- **RQ3 — Propagation latency:** elapsed time between release and downstream observation, only where timestamps are directly observed and comparable;
- **RQ4 — Aggregation recurrence:** recurrence of family-level grouping and multiple source summaries;
- **RQ5 — Failure and correction:** failures, partial states, rate limits, unresolved states, and corrections at observable infrastructure boundaries.

The preregistered design is prospective, longitudinal, repeated-measures, observational, and descriptive. It specifies no causal model, inferential statistical model, imputation, or global infrastructure-quality score.

### 2.1 Fixed sample and denominator

The fixed corpus contains ten research-software objects, RS01–RS10. The six analytical infrastructure layers are source repository, archival repository, identifier registration, author registry, preservation archive, and discovery graph. The observation unit is:

`software object × infrastructure layer × observation timepoint`

Thus, each eligible scheduled timepoint contains sixty planned object-layer units. Seven concrete platforms are used operationally: GitHub, Zenodo, DataCite, ORCID, Software Heritage, OpenAIRE, and OpenAlex. OpenAIRE and OpenAlex are separate operational platforms under the same discovery-graph layer. Seventy possible object-platform checks do not replace the sixty preregistered analytical units.

The control repository, `research-software-identity-audit`, is not RS11. It stores the operational implementation, evidence, provenance, schemas, tests, and governance records. Adding it to the sample would be a design change and is not done here.

### 2.2 Historical case versus prospective study

The historical case described in Sections 3–5 predates the 5 October registration. It is a retained baseline case, not a prospective observation wave. The later November diagnostics are also explicitly classified as diagnostics. The repository's schedule currently contains no concrete operational offsets, and the prospective raw-observation directory has no eligible data. No later diagnostic is retroactively promoted into the preregistered prospective dataset.

## 3. Historical case: three release waves across ten repositories

The historical release window began with the baseline tag on 16 September 2026 and ended with the October framework release on 4 October, eighteen calendar days between the first and last release dates. Three release tags were used across all ten repositories:

1. `v2026.09-open-research-baseline`
2. `v2026.09-natural-month-close`
3. `v2026.10-open-research-production-framework`

The retained field-level captures were taken on 3 and 4 October. Earlier events are supported by release timestamps, notification emails, and archived audit notes rather than a continuous daily sampling series.

## 4. Results

### 4.1 Identifier registration and versioning

At the retained DataCite snapshot, ten software families had ten family DOIs and thirty version DOIs, for forty findable identifiers. The family DOI represents the evolving software concept; each version DOI identifies a frozen deposit. Zenodo documents this distinction and recommends citing a specific version when the exact artifact used must be recoverable [4].

The counts refer to different object types. Forty identifiers are not forty software objects, and thirty version records are not thirty additional families.

### 4.2 Author-registry aggregation

The fixed-corpus ORCID subset contained fifty-two work summaries in ten groups:

| Source attribution | Summaries |
|---|---:|
| DataCite | 32 |
| OpenAIRE | 10 |
| Author-added | 10 |
| **Total** | **52** |

Third-party sources contributed forty-two summaries compared with ten author-added summaries, a 4.2:1 ratio within the fixed-corpus subset. The later 6 October baseline reconciliation recorded twelve groups and fifty-four summaries across the full visible ORCID record, while the fixed-corpus subset remained ten groups and fifty-two summaries. This is a scope distinction, not a change to the ten-object sample. The ratio is a source-record ratio, not an independent-work ratio. ORCID groups work records according to external identifiers and their relationships to the work; source summaries within a group remain distinct assertions [5]. The preferred display entry can also depend on the registry's display-index behavior, so a newly ingested DOI does not necessarily become the preferred representation.

### 4.3 Preservation

At the 3 October audit, ten origins had full snapshots. The record retained sixteen visits across the ten origins. On 4 October, two chains were re-verified end to end: the Git-origin and concept-DOI deposit paths for `welcome-to-github` and `Axiom-0`. One chain, `epistemic-pipeline`, was partially re-verified. Two repositories returned rate limits, and five were not re-reached before the record closed.

These states must remain separate. A previous full snapshot does not mean a later recheck was performed; a rate-limited attempt is not evidence of absence. Software Heritage exposes origin visits and links visits to snapshots, from which the snapshot, revision, directory, and content graph can be traversed [6].

### 4.4 Discovery

All ten September-version DOIs matched in OpenAlex in the retained 3–4 October historical check. October-version queries were not included in that capture. The subsequent baseline reconciliation, collected at approximately 2026-10-06 00:33:54 Asia/Shanghai, recorded forty fixed-corpus OpenAlex Work records and ten latest-version records found. The later query closes part of the historical discovery-coverage gap, but it does not reveal the first time at which those records entered OpenAlex and therefore does not supply a propagation-latency measurement.

OpenAlex models scholarly Works and their locations. It can use persistent identifiers and declared relations, and it also applies matching to records without shared persistent identifiers [7]. OpenAIRE separately aggregates research-product records and applies duplicate-identification and grouping procedures [8]. A positive result in one graph cannot be substituted for a result in the other.

### 4.5 Historical observation matrix

| Evidence surface | Historical result | Boundary |
|---|---|---|
| GitHub October release/tag | Observed for all ten objects | A release record is not the full tag universe |
| DataCite family and version DOIs | 40 identifiers findable | Registration is not discovery or scientific review |
| ORCID October DOI in group | Observed for all ten objects | Group and source-summary counts differ |
| Zenodo and OpenAlex September-version records | Observed for all ten objects in the 3–4 October capture | The separate 6 October baseline reconciliation later found all ten latest-version records in OpenAlex |
| Software Heritage recheck | Two full, one partial; two rate-limited; five not re-reached | Does not establish all October content identity |

The matrix describes retained observations only. It does not imply complete October discovery, complete content-equivalence checks, or bit-level equality between independent archive paths.

## 5. Later diagnostic evidence: 18 November 2026

A later read-only public-source diagnostic executed from 15:35:32.034791 to 15:39:43.508949 UTC on 18 November. It attempted the same 458 exact source keys as the 17 November diagnostic. This is a fixed diagnostic request cohort, not a new sample or a prospective timepoint.

| Diagnostic surface | 18 November result | Interpretation boundary |
|---|---|---|
| All source attempts | 458 attempted; 402 HTTP 200 without recorded failure; 56 failed/partial | Transport coverage, not identity verification |
| DataCite | 102/102 HTTP 200 | Known DOI inventory only |
| OpenAIRE | 102/102 HTTP 200; 94 positive DOI queries | Positive queries are not distinct software identities |
| OpenAlex | 34 exact canonical DOI matches and 34 distinct Work IDs | Exact match is narrower than HTTP success |
| ORCID | 18 groups / 119 summaries | Summary count is not a count of independent works |
| Zenodo | 21/67 version requests HTTP 200; 45 timeouts; one HTTP 500 | Sixty-version views/download totals are `null`, not zero |
| Software Heritage | 10/10 latest-origin responses | Origin response does not prove a fresh preservation visit |
| GitHub Releases | 11 release signatures unchanged in the comparison | Source commits do not imply a new tagged release |

The 102 DOI requests belong to the known diagnostic DOI inventory and must not be read as 102 fixed research objects. The 34 supplementary service/standards surfaces are likewise not additional analytical layers. The 11 pinned repositories include the ten sample repositories and the control repository; the control remains outside RS01–RS10.

The diagnostic retained 458 source-attempt projections with client UTC clocks, locators, response digests, status/error classifications, and selected public fields. Original provider response bodies were not published. Therefore, the SHA-256 values support comparison of the retained representation but do not make the original response bytes independently replayable.

### 5.1 A concrete non-comparability example

The 18 November Zenodo request cohort did not retrieve enough version records to calculate the fixed-ten sixty-version views/download totals. The correct value is `null`. Treating it as zero would convert an incomplete retrieval into a false usage collapse. Comparing it directly with the 17 November complete 60-version series would also be invalid because the entity coverage differs.

## 6. Interpretation

The case demonstrates that identity propagation is not a single success/failure state. The same software family may be registered in DataCite, represented by multiple source summaries in ORCID, preserved in Software Heritage, and discovered in OpenAlex or OpenAIRE at different times and through different matching rules.

The strongest methodological result is the need to separate:

1. **Object identity:** family, version, repository, release, DOI, Work, group, origin, snapshot;
2. **Platform identity:** which provider emitted the representation;
3. **Evidence identity:** which request, source projection, archive, or manual reading supports the claim;
4. **Clock identity:** release event, registration, source update, client retrieval, or later review;
5. **Analytical identity:** the preregistered object-layer unit versus a platform request, retry, source summary, or derived metric.

A successful HTTP response establishes a transport fact. It does not by itself establish that the returned object is the requested object. A source summary establishes an assertion in a registry, not an independent endorsement. A current live response cannot reconstruct an earlier historical response without retained evidence.

## 7. Limitations and prospective status

This paper has three evidence regimes that must not be conflated:

- the 16 September–4 October historical release-wave case;
- later read-only diagnostic retrievals, including the 18 November 458-key cohort;
- the prospective repeated-measures design frozen in the OSF registration.

The historical case is a single-author, ten-object deployment with discontinuous retained captures. The November diagnostic is a bounded public-source recheck, not an eligible prospective wave. The operational schedule has no concrete offsets, and no prospective cells have been added. Accordingly, the five preregistered questions have not yet been answered by a completed prospective repeated-measures dataset.

The findings are descriptive and case-bounded. They do not establish causal propagation, general provider latency, population prevalence, software adoption, scientific quality, or institutional endorsement. Missing, blocked, rate-limited, partial, and unqueried states remain explicit.

## 8. Conclusion

Research software acquires identity through a network of infrastructures whose objects, clocks, and guarantees differ. In the historical case, ten repositories produced forty DOI identifiers, fifty-two ORCID source summaries, ten preserved origins, and ten September-version OpenAlex matches. Those counts describe different kinds of records and cannot be added or substituted for one another.

The later diagnostic demonstrates why the distinction remains necessary: a complete request cohort can still contain failed and partial attempts; an HTTP-200 response can still fail exact identity matching; and incomplete version retrieval can make an aggregate unknowable. A rigorous longitudinal study must preserve those limits rather than smoothing them into a global success rate.

## AI-use disclosure

AI-assisted tools supported literature discovery, drafting organization, language editing, and reference cross-checking for this working revision. No external provider observation, original research datum, or scientific result is asserted to have been generated by an AI model. The author must review and verify the final manuscript, all references, and every numerical statement before submission and retains responsibility for the published version.

## References

1. Barker, M., et al. (2022). Introducing the FAIR Principles for research software. *Scientific Data, 9*, 622. https://doi.org/10.1038/s41597-022-01710-x
2. Smith, A. M., Katz, D. S., Niemeyer, K. E., & FORCE11 Software Citation Working Group. (2016). Software citation principles. *PeerJ Computer Science, 2*, e86. https://doi.org/10.7717/peerj-cs.86
3. Jiang, X. Y. (2026). Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures. OSF Registration. https://doi.org/10.17605/OSF.IO/5B329
4. Zenodo. DOI versioning. https://support.zenodo.org/help/en-gb/1-upload-deposit/97-what-is-doi-versioning
5. ORCID. How are items grouped together in an ORCID record? https://info.orcid.org/ufaqs/how-are-items-grouped-together-in-an-orcid-record/
6. Software Heritage. SWHIDs and origin visits. https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html
7. OpenAlex. Works overview and repositories. https://help.openalex.org/data/works/
8. OpenAIRE. Graph API and research-product deduplication. https://graph.openaire.eu/docs/11.2.0/apis/graph-api/
9. OpenAlex. Getting indexed. https://help.openalex.org/how-to/getting-indexed/
10. DataCite. Versioning. https://support.datacite.org/docs/versioning
11. Jiang, X. Y. (2026). Baseline package — cutoff 2026-10-05; reconciliation collected approximately 2026-10-06 00:33:54 Asia/Shanghai. https://github.com/lostlight530/research-software-identity-audit/tree/main/baseline/2026-10-05
12. Jiang, X. Y. (2026). 2026-11-18 complete identity-infrastructure diagnostic. https://github.com/lostlight530/research-software-identity-audit/tree/main/monitoring/2026-11-18/01-complete-identity-infrastructure-diagnostic
