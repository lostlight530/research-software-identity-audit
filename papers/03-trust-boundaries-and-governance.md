# Who Guarantees What? Trust Boundaries and Failure Modes in Open Scholarly Infrastructure

**Subtitle:** Evidence Semantics, Provenance, and Correction Governance for Research Software Identity

**Author:** Xuan yi Jiang · Independent Researcher  
**ORCID:** 0009-0001-3617-0832  
**Manuscript status:** Working revision, 19 November 2026  
**Article type:** Governance / methodological note

## Abstract

Open scholarly infrastructure is often described through its success path: an identifier resolves, a work appears in an author registry, a source repository is archived, and a discovery graph exposes a searchable record. Governance must also account for what those events do not guarantee. A successful request may return a semantically different object; a source summary may be one assertion among several grouped records; an archive-origin response may not establish a new preservation visit; a missing result may be caused by a blocked or incomplete query; and a digest of a selected-field projection is not the original provider response.

This paper develops a trust-boundary and failure-mode framework from an auditable research-software identity case. The historical October case involved ten software objects, forty DOI identifiers, and fifty-two ORCID source summaries. A later 18 November diagnostic attempted 458 fixed public-source requests, of which 402 returned HTTP 200 without recorded failure and 56 were failed or partial. The diagnostic returned 34 exact canonical OpenAlex DOI matches, 94 positive OpenAIRE DOI queries, and 18 ORCID groups containing 119 source summaries. Zenodo's fixed-ten, sixty-version views/download totals remained unknown because only 21 of 67 version requests succeeded. These figures are reported as different evidence units, not as one aggregate success metric.

The framework distinguishes four guarantee classes—registration, attribution, preservation, and discovery—and adds explicit evidence, transport, clock, object-grain, and correction boundaries. It organizes governance into observed behaviors, risks configured against, and unresolved coverage limits. It also defines an append-oriented correction record that preserves the prior state and makes every amendment independently inspectable. The result is a portable audit method for research software and other scholarly objects, without claiming that the case exhausts all possible failure modes.

**Keywords:** provenance; trust boundaries; evidence semantics; research software governance; DOI; ORCID; preservation; discovery; audit

---

## 1. Introduction

Persistent identifiers and open scholarly registries make research outputs easier to identify, cite, preserve, and discover. Yet the same output can be represented by multiple identifiers, records, source assertions, archive objects, and graph entities. These systems expose different guarantees and operate on different clocks.

A DOI resolver, a registration agency, an author registry, a preservation archive, and a discovery graph do not answer the same question. Treating them as one generic “verified” state creates two kinds of error: overclaiming, when evidence from one layer is used to assert a guarantee owned by another; and false alarms, when an unqueried or delayed layer is described as failed.

This paper asks: **who guarantees what, at which boundary, and what evidence is sufficient for each claim?** The answer is deliberately operational. A governance rule is useful only when it tells a researcher what object to query, what field to retain, what clock to report, what inference is permitted, and how a later correction must preserve history.

## 2. Four guarantee classes

The framework begins with four classes.

### 2.1 Registration and existence

A registration agency can establish that a particular identifier has a registered metadata record and that the record exposes specified fields and relationships at a given time. This does not establish scientific truth, content equality, correct authorship in a normative sense, preservation, or discovery.

DataCite's metadata schema defines typed relations, including `HasVersion`, `IsVersionOf`, `IsNewVersionOf`, and `IsPreviousVersionOf`. These relations are directed descriptions of relationships between registered resources. Schema 4.7, released on 3 March 2026, also added SWHID as a related-identifier type [1, 2]. A relation must be reported with its direction and source record; an absent reverse relation should not automatically be converted into a claim that the identifier itself is invalid.

### 2.2 Attribution

An author registry can expose work assertions, their source attribution, external identifiers, and grouping relationships. A source-attributed entry indicates the system or person that added an assertion to the registry. ORCID separately distinguishes the assertion origin that connected the researcher to the work; source and assertion origin can differ. Neither field automatically constitutes independent scientific review, institutional endorsement, employment, or validation of the software [3].

ORCID groups works according to identifiers and identifier relationships. It distinguishes identifiers referring to the work itself, identifiers for a whole of which the work is part, and identifiers for alternate versions [3]. A work group, an individual summary, and an independent scholarly work are therefore different units.

### 2.3 Preservation

A preservation archive can establish that a specific origin, visit, snapshot, revision, directory, or content object is represented and resolvable under its observable API. A successful origin lookup is not equivalent to proof that a new visit occurred during the current audit. A resolvable snapshot does not, by itself, prove bit-level equality between two independent deposit paths.

Software Heritage's content-addressed identifiers allow specific archived objects to be referenced and traversed through the archive graph [4]. The exact object type matters: origin, snapshot, revision, directory, and content identifiers should not be collapsed into one generic “archive verified” label.

### 2.4 Discovery

A discovery graph can establish that a particular record or location is represented under a specific query and retrieval time. It does not guarantee registration, attribution, preservation, scientific review, or adoption.

OpenAlex models Works and their locations, using persistent identifiers and declared relations as well as matching mechanisms for records without shared identifiers [5]. OpenAIRE separately performs research-product deduplication and grouping [6]. Their representations and matching behavior are not interchangeable. A positive result in one graph is not evidence that the other graph contains the same representation.

## 3. Trust-boundary matrix

| Claim class | Observable evidence | What the evidence can support | What it does not establish |
|---|---|---|---|
| Registration | Exact DOI record and metadata response | Identifier record exists at the named agency and retrieval time | Scientific truth, content equality, downstream indexing |
| Attribution | ORCID work group, source summary, external identifier and relationship | A registry assertion is present with the observed source attribution | Independent review, endorsement, legal identity proof |
| Preservation | Origin visit, snapshot, revision, directory or content SWHID | The named archived object is represented or resolvable | New visit at the current audit, cross-origin bit equality |
| Discovery | Exact DOI-to-Work or research-product match under a named query | A discovery representation is present for the observed query | Registration authority, author approval, preservation, adoption |
| Correction | Dated original value, corrected value, reason, and readback | A correction event is documented and traceable | A proven platform defect or causal repair unless separately established |

The matrix is intentionally non-transitive. Evidence that satisfies one row cannot be used to silently fill another.

## 4. Failure-mode taxonomy

The following taxonomy combines the five categories identified in the original October note with failure boundaries exposed by the expanded repository audit. Each category is labeled by evidence status: **observed**, **risk configured against**, or **coverage/interpretation limit**. These labels prevent a guarded risk from being misreported as an incident.

### F1. Metadata pollution through mistyped fields

**Status:** Risk configured against; not observed in the original case.

Deposit forms can invite category errors, such as placing a software family DOI in a field intended for a previously published article DOI. A registration schema may validate field type while failing to detect that the identifier is conceptually inappropriate.

**Rule:** classify an identifier by the object it identifies, not by a superficially similar form label. Software-family identity belongs in a suitable related-object or reference field, not in an unrelated publication-history field.

### F2. Duplicate deposition and metric fragmentation

**Status:** Risk configured against.

Depositing the same software object independently in multiple services can split records and usage metrics. Publishing versions without a family-level identity can multiply representations.

**Rule:** use one canonical archival deposit path where possible; use links and typed relations elsewhere rather than creating unnecessary copies. A family DOI and a version DOI must be retained as separate object types [7].

### F3. Undocumented aggregation and source-summary duplication

**Status:** Observed.

In the October historical fixed-corpus subset, ORCID exposed fifty-two source summaries in ten groups: thirty-two DataCite, ten OpenAIRE, and ten author-added summaries. The third-party-to-author source-summary ratio was 42:10. A separate 6 October baseline reconciliation recorded fifty-four summaries in twelve groups across the full visible ORCID record, while the fixed-corpus subset remained fifty-two summaries in ten groups. In the 18 November diagnostic, the public ORCID response contained eighteen groups and 119 work summaries. These are three dated/scope-specific snapshots, not one cumulative total. They count ORCID source labels, not necessarily the actors that originally initiated the researcher-work association; ORCID's source and assertion-origin fields represent distinct roles [3].

These counts do not represent independent software objects. The same work group can contain multiple source assertions and alternate representations. The platform's grouping and display behavior must be inspected rather than inferred from a single total.

**Rule:** retain group identity, source identity, external identifier type/value/relationship, and display index where available. Count groups and summaries separately.

### F4. Latency hierarchy misread as malfunction

**Status:** Coverage limit, not a measured latency result.

The 3–4 October historical capture did not include October-version OpenAlex queries. A separate 6 October baseline reconciliation later recorded ten latest-version records found in OpenAlex, but did not establish their first-index timestamps. The November diagnostic likewise did not establish first-index timestamps for the full cohort. Client retrieval time is not the platform's internal ingestion time.

**Rule:** calculate latency only where release-event and first qualifying downstream timestamps are directly observed and comparable. Otherwise report unqueried, first observed, interval-bounded, or unknown. Do not invent a latency value from a later successful query.

### F5. Version-label drift

**Status:** A correction forced during the original study.

Human-readable ordinal labels can drift from platform identifiers and from the release chronology as a corpus grows. If separate documents use different ordinal conventions, the manuscript can contradict the machine record.

**Rule:** use stable prose labels such as baseline, second release, and October release; use exact platform identifiers and tag strings in machine contexts; retain one explicit mapping table. A correction changes future prose and records an amendment event; it does not rewrite earlier deposits.

### F6. Transport success confused with semantic identity

**Status:** Observed as a necessary distinction in the expanded diagnostics.

On 18 November, all 102 known DataCite DOI requests and all 102 OpenAIRE DOI requests returned HTTP 200. OpenAIRE produced 94 positive DOI queries. OpenAlex returned 34 exact canonical DOI matches and 34 distinct Work IDs. These are not equivalent measures: HTTP completion is a transport result, a positive query is a source result, and an exact canonical DOI match is an identity result. OpenAlex can attach multiple DOI-bearing locations to one Work; a strict canonical DOI match count is therefore narrower than a full reconciliation of every queried DOI against every Work location [5, 6].

The 458-request diagnostic as a whole contained 402 HTTP-200 attempts without recorded failure and 56 failed or partial attempts. A complete request ledger can therefore coexist with incomplete semantic coverage.

**Rule:** record transport state and semantic identity state as separate fields. Do not count HTTP 200 as an identity match.

### F7. Selected-field projections confused with original provider evidence

**Status:** Observed evidence limitation.

The November diagnostic retained request locators, client clocks, response digests, byte lengths, error/status information, and selected public fields. Original provider response bodies were not published. A digest of a response that is not available to the reader cannot independently reproduce that response.

**Rule:** label the evidence representation precisely: original response bytes, retained local-only bytes, published selected-field projection, page transcription, or later interpretation. Never describe a projection hash as a public raw-response archive.

### F8. Version-level and family-level statistics mixed

**Status:** Observed incompleteness and a documented historical mismatch.

Zenodo exposes version-specific and family-attached statistics. They can differ in entity grain and aggregation semantics. The 18 November diagnostic retrieved only 21 of 67 version requests successfully, so the fixed-ten sixty-version views/download totals were retained as `null`. This does not mean zero usage or a decrease from the prior complete series.

A separate 10 October RS07 case showed a version record with attached `stats.views=186`, while the sum of the three version-local view fields was 85. This is an observed field discrepancy, not proof of the platform's internal synchronization cause.

**Rule:** compare only like-for-like fields, entities, query modes, and windows. Keep attached aggregate fields and version-local fields separate. Do not sum version-level unique values as globally deduplicated people.

### F9. Research sample and control infrastructure conflated

**Status:** Explicitly guarded by the frozen contract.

The fixed corpus is RS01–RS10. The research-control repository is not RS11. Six analytical layers produce sixty preregistered object-layer units per eligible timepoint; seven operational platforms produce up to seventy possible platform checks. Thirty-four supplementary surfaces are outside the seven-platform vocabulary.

**Rule:** never add the control repository, supplementary services, DOI records, retries, source summaries, or HTTP requests to the preregistered sample denominator.

### F10. CI completion confused with scientific acceptance

**Status:** Explicitly guarded by the repository assurance model.

The repository checker validates selected structural and semantic constraints. GitHub Actions runs some tests in advisory mode. Synthetic fixtures test code behavior, not live provider state. A green workflow does not prove that every test passed as a blocking gate, that all external sources were checked, or that a scientific claim is true.

**Rule:** report the exact workflow, job, step, exit outcome, and scope. Distinguish test success, repository integrity, external observation, independent verification, and scientific acceptance.

### F11. Discovery graph aggregation confused with one-to-one identity

**Status:** Platform behavior and case-specific identity boundary.

OpenAlex may map multiple locations to a Work, while OpenAIRE identifies and groups duplicate research products. An index record may therefore represent a cluster of source records rather than a direct one-to-one copy of a DOI deposit.

**Rule:** retain the requested DOI, returned canonical identifier, graph Work or product ID, location/source, and query time. An exact canonical match is a narrower claim than a returned candidate or a successful transport.

## 5. Evidence semantics and provenance roles

The repository's evidence model distinguishes the source publisher, researcher, collector, reconciler, and verifier. These roles describe activities and responsibility boundaries; they do not automatically create independent sources.

A practical evidence ladder is:

1. **Original provider response bytes:** strongest retained source representation where legally and operationally publishable.
2. **Locally retained source bytes with digest:** inspectable within the declared custody/access boundary.
3. **Published selected-field projection:** a bounded derivative of a source response, not the full response.
4. **Manual page transcription:** a human reading with explicit attribution and known or unknown capture time.
5. **Derived analysis:** calculations linked to named inputs and an attributable method.
6. **Interpretation:** a bounded explanation that cites the evidence and states uncertainty.

W3C PROV-O provides a vocabulary for entities, activities, and agents [8]. The repository uses the conceptual distinction without claiming that all records are serialized as a PROV-O graph. A source request is an activity; the response or retained projection is an entity; the researcher or software collector is an agent. A digest does not independently authenticate the agent or the provider.

## 6. Correction-surface governance

Correction must not erase the state that made the correction necessary. Historical evidence is append-oriented. A material correction should preserve:

| Field | Required meaning |
|---|---|
| Correction ID | Stable identifier for the correction event |
| Original record | Exact historical path, object ID, and prior value |
| Corrected interpretation/value | New value or explicitly unresolved state |
| Reason | What was wrong, incomplete, or mis-scoped |
| Supporting evidence | Source locator, response, comparison, or review record |
| Correction clock | Actual timestamp and timezone |
| Responsible actor | Researcher, collector, reviewer, or automation role |
| Affected outputs | Manuscript sections, tables, derived metrics, or links requiring revision |
| Disposition | Corrected, superseded, unresolved, or no-change-required |

A correction record should not claim a proven provider defect merely because two representations differ. It should state whether the cause is known, suspected, or unresolved. New evidence can change the present interpretation without changing what an earlier observer actually saw.

## 7. Governance decision rules

For each proposed statement, reviewers should ask:

1. What is the exact object: repository, tag, family DOI, version DOI, ORCID group, source summary, origin, snapshot, Work, or product record?
2. Which platform and endpoint produced the evidence?
3. What query shape, pagination, authentication state, and retrieval time apply?
4. Is the claim about transport, object existence, identity matching, attribution, preservation, discovery, or correction?
5. Is the timestamp an event time, provider-updated time, client request time, or later review time?
6. Are the compared metrics at the same entity grain and with compatible semantics?
7. Is the retained evidence original bytes, a projection, a transcription, or an interpretation?
8. What is not established, and what observation would change the conclusion?

The allowed outcomes include `OBSERVED`, `NOT_FOUND_AT_THIS_ENDPOINT`, `RATE_LIMITED`, `PARTIAL`, `UNRESOLVED`, `NOT_RUN`, and `NO_CONCLUSION`. They are not interchangeable with a binary success/failure flag.

## 8. Limitations

The taxonomy derives from one researcher's deployment and a finite set of public-source diagnostics. It is not an exhaustive catalogue of scholarly-infrastructure failure modes. The historical case covers ten fixed software objects; the later 458-request cohort is diagnostic and includes source checks at finer granularity than the preregistered sixty object-layer units. The November diagnostic did not publish all original provider response bodies, and the prospective observation schedule has no concrete offsets. Consequently, this paper does not estimate general provider reliability, causal effects, or population-level failure rates.

The observed differences do not prove a provider defect unless the relevant source contract and independent evidence support that conclusion. A mismatch may be a field-semantic difference, a query-shape difference, a clock difference, an incomplete retrieval, or a real inconsistency; the classification must remain open until the evidence distinguishes these explanations.

## 9. Conclusion

Trust in open scholarly infrastructure is layered, object-specific, and time-bounded. Registration, attribution, preservation, and discovery are separate guarantees. Transport success, semantic identity, source attribution, archival representation, and scientific acceptance are separate claims.

The practical governance contribution is a trust-boundary matrix, a typed failure taxonomy, and an append-oriented correction contract. Together they allow a researcher to report what a platform actually established without promoting an endpoint response into a broader institutional guarantee. The governing principle is simple: every claim should name its object, source, clock, evidence representation, and inference boundary.

## AI-use disclosure

AI-assisted tools supported literature discovery, drafting organization, language editing, and reference cross-checking for this working revision. No external provider observation, original research datum, or scientific result is asserted to have been generated by an AI model. The author must review and verify the final manuscript, all references, and every numerical statement before submission and retains responsibility for the published version.

## References

1. DataCite Metadata Working Group. (2026). *DataCite Metadata Schema Documentation*, Version 4.7. https://doi.org/10.14454/qdd3-ps68
2. DataCite. Versioning and related identifiers. https://support.datacite.org/docs/versioning
3. ORCID. How are items grouped together in an ORCID record? https://info.orcid.org/ufaqs/how-are-items-grouped-together-in-an-orcid-record/
4. ORCID. Integration and API FAQ: source and assertion origin. https://info.orcid.org/documentation/integration-and-api-faq/
5. Software Heritage. SWHIDs and persistent identifiers. https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html
6. OpenAlex. Matching and merging Works. https://help.openalex.org/data/works/matching/
7. OpenAlex. DOIs and locations in Works. https://help.openalex.org/data/works/dois/
8. OpenAIRE. Research-product deduplication. https://graph.openaire.eu/docs/11.3.0/graph-production-workflow/deduplication/research-products/
9. Zenodo. DOI versioning. https://support.zenodo.org/help/en-gb/1-upload-deposit/97-what-is-doi-versioning
10. W3C. (2013). PROV-O: The PROV Ontology. https://www.w3.org/TR/prov-o/
11. Jiang, X. Y. (2026). Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures. OSF Registration. https://doi.org/10.17605/OSF.IO/5B329
12. Barker, M., et al. (2022). Introducing the FAIR Principles for research software. *Scientific Data, 9*, 622. https://doi.org/10.1038/s41597-022-01710-x
13. Jiang, X. Y. (2026). Baseline package — cutoff 2026-10-05; reconciliation collected approximately 2026-10-06 00:33:54 Asia/Shanghai. https://github.com/lostlight530/research-software-identity-audit/tree/main/baseline/2026-10-05
14. Jiang, X. Y. (2026). 2026-11-18 complete identity-infrastructure diagnostic. https://github.com/lostlight530/research-software-identity-audit/tree/main/monitoring/2026-11-18/01-complete-identity-infrastructure-diagnostic
15. Jiang, X. Y. (2026). Observation assurance and claim boundaries. https://github.com/lostlight530/research-software-identity-audit/blob/main/docs/observation-assurance-2026-10-25.md
