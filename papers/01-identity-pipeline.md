# From Git Tag to Scholarly Record: Engineering an Auditable Identity Pipeline for Research Software

**Subtitle:** A field-level engineering account of persistent identity, attribution, preservation, and discovery

**Author:** Xuan yi Jiang · Independent Researcher  
**ORCID:** 0009-0001-3617-0832  
**Manuscript status:** Working revision, 19 November 2026  
**Article type:** Technical note / research infrastructure

## Abstract

Research software moves through several infrastructures after a source-code release. A Git tag identifies a source-control event; an archival repository can mint a version DOI and a family DOI; a registration agency exposes DOI metadata; an author registry may ingest and group work assertions; a preservation archive may retain a content-addressed snapshot; and discovery services may later represent the software as a searchable scholarly object. These transitions are related, but they do not share one object model, one clock, or one guarantee.

This technical note describes an auditable identity pipeline built by an independent researcher across ten public research-software repositories. The historical case used three release waves between 16 September and 4 October 2026. At the retained 3–4 October snapshot, forty DataCite-registered DOIs represented ten software families and thirty version records. The fixed-corpus subset of the author's ORCID record contained fifty-two work summaries in ten groups, with thirty-two DataCite-source summaries, ten OpenAIRE-source summaries, and ten author-source summaries. Software Heritage showed ten origins archived; the retained 3 October audit recorded full snapshots for all ten origins, while the 4 October recheck fully re-verified two chains and partially re-verified one. October-version discovery queries were not part of that 3–4 October capture. A separate 6 October baseline reconciliation later recorded ten latest-version records found in OpenAlex; that later retrieval is not backdated into the earlier snapshot.

The note then describes the repository-side control architecture that preserves the distinction between a frozen research contract, a mutable operational implementation, historical baseline evidence, diagnostic monitoring, and eligible prospective observations. By 18 November, a later read-only diagnostic had attempted 458 fixed public-source requests, but it remained diagnostic rather than a prospective study wave. The central engineering contribution is not a claim of universal automation: it is a field-level contract for stating exactly what was configured, what was observed, what was derived, and what remains unknown.

**Keywords:** research software; identity pipeline; DOI; ORCID; Zenodo; DataCite; Software Heritage; OpenAlex; provenance; reproducibility

---

## 1. Introduction

Research software is simultaneously a source repository, a sequence of versioned releases, a citable research output, an author-attributed work, a preservable source artifact, and a potential node in a scholarly discovery graph. These representations are not interchangeable. A repository URL does not by itself identify an immutable release. A DOI does not by itself prove preservation. An author-registry entry does not establish independent scientific endorsement. A discovery record does not prove that the exact requested DOI was matched.

The practical question addressed here is narrower than whether scholarly infrastructure is generally effective: can an independent researcher configure and inspect a traceable identity chain using publicly available services, without institutional credentials? The historical deployment shows that this is operationally possible for the observed objects. It also shows why the result must be described field by field rather than as a single “published” or “verified” state.

The work follows the principles that research software is a legitimate citable research output and that citations should identify a specific version where reproducibility requires it [1, 2]. It treats persistent identifiers and content-addressed preservation as complementary rather than competing mechanisms.

## 2. Scope and case boundary

The historical case contains ten public repositories covering agent-systems research, research infrastructure, reference software, scientific rendering and documentation, and two source-grounded AI observatories. The case window begins with a baseline release tag on 16 September 2026 and ends with the October framework release on 4 October 2026, an eighteen-calendar-day interval between the first and last release dates.

Three release tags were applied across the ten repositories:

1. `v2026.09-open-research-baseline`
2. `v2026.09-natural-month-close`
3. `v2026.10-open-research-production-framework`

The present GitHub repository, `research-software-identity-audit`, is the research-control and evidence workspace. It is not an eleventh research-software object. The fixed analytical corpus remains RS01–RS10 under the frozen OSF registration [3]. This distinction matters: the control repository contains schemas, tools, evidence indexes, monitoring records, and governance documentation used to operate the study. It cannot be added to its own sample without changing the research design.

## 3. Pipeline architecture

### 3.1 Identity path

The operational path can be represented as six scholarly-infrastructure layers instantiated by seven concrete platforms:

| Analytical layer | Operational platform | Primary object or representation |
|---|---|---|
| Source repository | GitHub | Repository, tag, commit, Release |
| Archival repository | Zenodo | Version record and concept/family record |
| Identifier registration | DataCite | DOI registration metadata and relations |
| Author registry | ORCID | Work groups and source-attributed summaries |
| Preservation archive | Software Heritage | Origin visits, snapshots, revisions, directories, SWHIDs |
| Discovery graph | OpenAIRE | Research-product records and aggregation |
| Discovery graph | OpenAlex | Work records, locations, author entities |

The six-layer model is analytical. The seven-platform vocabulary is operational. OpenAIRE and OpenAlex remain distinct platforms within the single preregistered discovery-graph layer. Ten objects multiplied by six layers yields sixty planned object-layer units per eligible timepoint; ten objects multiplied by seven platforms yields seventy possible object-platform checks. The latter is not a replacement denominator.

### 3.2 Five-stage release-triggered path

The historical identity pipeline has five connected stages:

1. **Release.** A Git tag and corresponding release event establish a versioned source-control event.
2. **Archival minting.** Repository-to-Zenodo integration is enabled per repository. Subsequent eligible release events produce a version record and a concept/family identity.
3. **Identifier registration.** DataCite exposes the registered DOI metadata, including creator metadata and the author's ORCID iD.
4. **Author-registry propagation.** With the required account authorization and metadata conditions, DataCite Auto-Update can add registered works to the author's ORCID record.
5. **Preservation and discovery.** Software Heritage can expose origin visits and snapshots; discovery graphs ingest scholarly records according to their own source and matching processes.

Zenodo's concept DOI represents all versions of a record, while a version DOI identifies a specific deposited version. Zenodo recommends citing the specific version when exact reproducibility is required [4]. DataCite represents version relationships through directed relation types such as `HasVersion` and `IsVersionOf`; the direction of the relation must be retained rather than silently treated as symmetric [5].

### 3.3 Configuration surface

The original deployment required a small number of explicit configuration actions:

- enable the archival integration once per repository;
- place the author's ORCID iD in the appropriate creator metadata;
- authorize the account-level DataCite Auto-Update permission;
- request archival harvesting for pre-existing repository history.

The public read endpoints could be inspected without institutional affiliation, but the configuration writes and account permissions required authenticated user accounts. Free access must not be confused with unauthenticated access.

## 4. Historical worked case

At the retained 3–4 October 2026 snapshot:

| Unit | Count | Meaning |
|---|---:|---|
| Software families | 10 | Fixed historical case objects |
| Family DOIs | 10 | Concept/family identifiers |
| Version DOIs | 30 | Three version identifiers per family |
| Findable DOIs | 40 | Ten family plus thirty version identifiers |
| ORCID work groups | 10 | Grouped work representations |
| ORCID work summaries | 52 | Source records, not distinct software objects |
| DataCite summaries | 32 | Source-attributed summaries |
| OpenAIRE summaries | 10 | Source-attributed summaries |
| Author summaries | 10 | Author-added assertions |

The third-party-source to author-source summary ratio within the fixed-corpus subset was 42:10, or 4.2:1. The later 6 October baseline reconciliation separately recorded 54 summaries in 12 groups across the full visible ORCID record; the fixed-corpus subset remained 52 summaries in 10 groups. The difference reflects scope, not an extra two research objects. These counts describe ORCID source labels (the entity that added an assertion), not necessarily the assertion origin (the person or system that established the researcher–work connection); those roles can differ [12]. They count source summaries, not independent works, software objects, or endorsements. ORCID groups works according to identifiers and identifier relationships; the group and individual source assertions are different units [6].

For preservation, sixteen visits across ten origins were retained, with all ten origins showing full snapshots at the 3 October audit. On 4 October, two chains were re-verified end to end and one partially. Two repositories returned rate limits, and five were not re-reached before the historical record closed. These are different coverage states and must not be collapsed into “ten re-verified on 4 October.”

For discovery, all ten September-version DOIs matched in OpenAlex in the retained 3–4 October historical check. October-version DOIs were not queried within that capture window. The subsequent baseline reconciliation, collected at approximately 2026-10-06 00:33:54 Asia/Shanghai, recorded ten latest-version records found in OpenAlex and forty fixed-corpus Work records. This later result is a separate observation with its own retrieval clock; it does not alter what was or was not queried on 3–4 October.

## 5. From a one-off pipeline to an auditable research runtime

The current control repository extends the original field walkthrough into a versioned research runtime. Its authority model is explicit:

- the OSF registration is the frozen research contract;
- GitHub `main` is the evolving operational implementation;
- `baseline/` preserves historical baseline material;
- `monitoring/` holds dated diagnostics;
- `evidence/` holds retained source projections and evidence packages;
- `observations/raw/` is reserved for eligible prospective raw observations;
- `observations/derived/` holds derivations linked to raw observations;
- `provenance/`, schemas, tools, and tests support traceability and validation.

The repository's current schedule declares no concrete operational offsets. Accordingly, it does not claim that the preregistered prospective observation window has started. The absence of prospective records is a boundary condition, not a failed observation and not permission to invent a schedule.

### 5.1 Later diagnostic, separate from the historical case

A read-only diagnostic executed on 18 November 2026 attempted 458 exact public-source request keys. The client retrieval window was 15:35:32.034791–15:39:43.508949 UTC. The record reported 402 HTTP-200 requests without recorded failure and 56 failed or partial attempts. Within that diagnostic:

- DataCite: 102/102 requests returned HTTP 200;
- OpenAIRE: 102/102 requests returned HTTP 200, with 94 positive DOI queries;
- OpenAlex: 34 exact canonical DOI matches and 34 distinct returned Work IDs; a strict canonical match is narrower than matching every DOI-bearing Work location;
- ORCID: 18 public work groups and 119 work summaries;
- Software Heritage: 10/10 latest-origin responses;
- Zenodo: 21/67 version requests returned HTTP 200; 45 timed out and one returned HTTP 500.

The fixed-ten, sixty-version Zenodo views/download totals were retained as `null`, not zero, because the version retrieval was incomplete. The 458 attempts are a diagnostic request cohort, not 458 research units. The 102 DOI requests are not 102 software objects. The November diagnostic does not rewrite the October historical snapshot and does not create prospective observations.

### 5.2 Semantic extraction as a separate layer

The 19 November main-branch revision added conservative, source-specific semantic projections for six supplementary public-source keys: bio.tools, OpenEBench tool metadata, Handle URL mapping, Crossref registration-agency lookup, CiteAs metadata, and EDAM ontology metadata. The projections are deliberately bounded: a registry entry does not prove adoption; a monitoring tool card does not prove benchmark execution; a DOI-agency lookup does not mean Crossref registered the work; and a citation-metadata record does not prove that a citation event occurred.

The associated tests use synthetic fixtures and are network-free. They test parser and classification behavior, not the truth of the external provider's current state. Historical ledgers are not rewritten by the new extractor. This distinction is essential when a software implementation evolves after the evidence it interprets was collected.

## 6. Field contract and evidence discipline

Every material claim should be traceable through:

`source locator → request/reading event → raw or retained source representation → normalized observation → derivation → interpretation`

At minimum, the observation record should preserve the object identity, platform, analytical layer, exact target, query shape, retrieval clock, transport outcome, source fields, evidence reference, verification status, and failure reason where applicable.

The following states must remain distinct:

- transport completed versus transport failed;
- exact target matched versus target unresolved;
- record present versus record absent under a bounded endpoint contract;
- version record versus family record;
- ORCID group versus source summary;
- origin visit versus snapshot or content identifier;
- current live state versus historical captured state;
- raw provider bytes versus a selected-field projection or transcription.

A response digest is useful for integrity comparison when the corresponding bytes are available. A digest alone does not publish or independently reproduce the original provider response. Similarly, a successful CI run proves only the checks that actually ran, under the scope and outcome recorded by that run.

## 7. Reproduction checklist

A researcher attempting to reproduce the configuration should:

1. register an ORCID iD and identify the public account permissions required by each service;
2. enable the repository integration for each source repository;
3. include the ORCID iD in the appropriate creator metadata;
4. publish a tagged release and record the exact tag, commit, and event clocks;
5. distinguish concept/family DOI from version DOI;
6. request preservation harvesting where the archive requires it;
7. query each downstream platform with a recorded endpoint, query shape, and retrieval timestamp;
8. preserve source-attributed work summaries and identifier relationships;
9. record partial, blocked, rate-limited, failed, and unqueried states without imputing success or absence;
10. report the final state separately for registration, attribution, preservation, and discovery.

The checklist is not a guarantee that all providers will return identical records or process events within a fixed latency. It is a method for making the observed state inspectable.

## 8. Limitations

The original worked case is a single-author, ten-object deployment over eighteen calendar days. Historical captures are discontinuous rather than a complete daily sampling series. Some October discovery and preservation checks were not run. The later November diagnostic is a separate read-only retrieval and has incomplete Zenodo version coverage. Original external response bytes are not all published; some retained evidence consists of response hashes, selected public fields, and source-attempt projections. The repository's current prospective schedule has no concrete offsets, and the prospective raw-observation area remains distinct from diagnostics.

The case therefore demonstrates an attainable configuration and an auditable reporting discipline. It does not establish universal provider behavior, population-level performance, causal propagation, scientific quality, software adoption, or a complete prospective longitudinal result.

## 9. Conclusion

A research-software identity pipeline is not one DOI and not one “verified” badge. It is a chain of typed objects and institution-specific transitions: repository releases, archived versions, registered identifiers, author assertions, preservation snapshots, and discovery records. The engineering task is to preserve the distinctions between them.

The practical contribution is a reproducible field contract and a control architecture that keeps the frozen research design, mutable software, historical baseline, diagnostic monitoring, and future prospective observations separate. For independent researchers, the limiting factor is not necessarily institutional access. It is the discipline to state exactly what each layer guarantees, what was actually queried, and what the retained evidence cannot establish.

## AI-use disclosure

AI-assisted tools supported literature discovery, drafting organization, language editing, and reference cross-checking for this working revision. No external provider observation, original research datum, or scientific result is asserted to have been generated by an AI model. The author must review and verify the final manuscript, all references, and every numerical statement before submission and retains responsibility for the published version.

## References

1. Smith, A. M., Katz, D. S., Niemeyer, K. E., & FORCE11 Software Citation Working Group. (2016). Software citation principles. *PeerJ Computer Science, 2*, e86. https://doi.org/10.7717/peerj-cs.86
2. Barker, M., et al. (2022). Introducing the FAIR Principles for research software. *Scientific Data, 9*, 622. https://doi.org/10.1038/s41597-022-01710-x
3. Jiang, X. Y. (2026). Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures. OSF Registration. https://doi.org/10.17605/OSF.IO/5B329
4. Zenodo. DOI versioning. https://support.zenodo.org/help/en-gb/1-upload-deposit/97-what-is-doi-versioning
5. DataCite. Versioning and related identifiers. https://support.datacite.org/docs/versioning
6. ORCID. How are items grouped together in an ORCID record? https://info.orcid.org/ufaqs/how-are-items-grouped-together-in-an-orcid-record/
7. DataCite. How to connect your ORCID to DataCite. https://support.datacite.org/docs/datacite-and-orcid
8. Software Heritage. SWHIDs and origin visits. https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html
9. OpenAlex. Works overview and repository indexing. https://help.openalex.org/data/works/
10. OpenAIRE. Graph API documentation. https://graph.openaire.eu/docs/11.2.0/apis/graph-api/
11. W3C. PROV-O: The PROV Ontology. https://www.w3.org/TR/prov-o/
12. ORCID. Integration and API FAQ: source and assertion origin. https://info.orcid.org/documentation/integration-and-api-faq/

### Repository evidence

13. Jiang, X. Y. (2026). Baseline package — cutoff 2026-10-05; reconciliation collected approximately 2026-10-06 00:33:54 Asia/Shanghai. https://github.com/lostlight530/research-software-identity-audit/tree/main/baseline/2026-10-05
14. Jiang, X. Y. (2026). 2026-11-18 complete identity-infrastructure diagnostic. https://github.com/lostlight530/research-software-identity-audit/tree/main/monitoring/2026-11-18/01-complete-identity-infrastructure-diagnostic
