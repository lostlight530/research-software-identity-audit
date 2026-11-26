# OSF VSHWK scope-to-endpoint crosswalk

**OSF Project / Study Registration pair:** [AUHJF](https://osf.io/auhjf/) / [VSHWK](https://osf.io/vshwk/) · [2026-11-26 pair crosswalk](../../osf-object-pairing-crosswalk-2026-11-26.md)

**Protocol authority:** approved Schema Response `6afdcc7108de91a0f0cefd6c`  
**Operational endpoint set:** [manifest v1](endpoints-v1.json), declared 2026-11-24T07:05:22.196Z before Cycle 01 acquisition  
**Current case:** one WorkflowHub Project 490 case; paired embedded lineages 2332 v9 and 2334 v9

This crosswalk distinguishes the eight OSF-approved analytical layers from the bounded endpoint locators selected for manifest v1. A layer is an analytical dimension; an endpoint is one specific collection locator; neither is a separate research subject.

## Manifest v1 coverage

| Layer | OSF-approved analytical scope | Manifest v1 locators | Count |
|---|---|---|---:|
| L1 Source repository | Source repositories, workflow definitions, commits and provenance | `L1-A-head`, `L1-A-workflow`, `L1-B-head`, `L1-B-workflow` | 4 |
| L2 Workflow registry | WorkflowHub Project 490 and records 2332 / 2334 at v9 | `L2-A-version9`, `L2-B-version9`, `L2-shared-project490` | 3 |
| L3 Archival repository | Zenodo candidate records linked by exact lineage DOI | `L3-A-zenodo-search`, `L3-B-zenodo-search` | 2 |
| L4 Identifier registration and resolution | DataCite metadata and DOI resolution for both version DOIs | `L4-A-datacite`, `L4-A-doi-resolve`, `L4-B-datacite`, `L4-B-doi-resolve` | 4 |
| L5 Source preservation | Software Heritage origin visit for each source repository | `L5-A-swh-visit`, `L5-B-swh-visit` | 2 |
| L6 Testing, monitoring and execution | Exact NEXUS CORTEX GitHub Actions lifecycle workflow-run endpoints | `L6-A-actions`, `L6-B-actions` | 2 |
| L7 Researcher attribution | One shared ORCID works endpoint; retain once, do not duplicate by lineage | `L7-shared-orcid-works` | 1 |
| L8 Discovery and aggregation | Exact DOI lookups in OpenAIRE and OpenAlex for both lineages | `L8-A-openaire`, `L8-A-openalex`, `L8-B-openaire`, `L8-B-openalex` | 4 |
| **Total** | **Eight analytical layers** | **22 predeclared endpoint locators** | **22** |

The denominator is 22 endpoint locators per manifest-v1 cycle. It is not 22 independent research objects, and it does not change the one-case / eight-project-layer / sixteen-nested-lineage-layer structure.

## Approved scope surfaces not separately endpointized or assessed in v1

The approved schema response names the following surfaces in its layer descriptions. Manifest v1 does not provide a dedicated endpoint for each one, so their states must be reported as coverage limits rather than provider absence:

- **L6 — WorkflowHub-displayed testing metadata:** explicitly named in the approved L6 scope, but no dedicated L6 endpoint was declared in v1. The partial L2 WorkflowHub page captures are not separately normalized or promoted to L6 testing evidence
- **L6 — LifeMonitor and OpenEBench:** conditional surfaces, to be included only where an explicit relationship to the focal workflow can be established; neither has a v1 endpoint
- **L7 — WorkflowHub creator information:** named in the approved L7 scope, but v1 has only the shared ORCID works endpoint. Creator information incidentally present in an L2 page is not silently promoted to a separately verified L7 attribution record
- **L8 — Research Software Directory and nfdi.software:** named discovery / aggregation surfaces, but neither has a v1 endpoint

These limits mean `NOT_SEPARATELY_ASSESSED_IN_MANIFEST_V1`, not `NOT_FOUND`, provider absence, or a negative study result. They do not change the 22-endpoint v1 denominator or invalidate its attempt accounting; they bound claims about the breadth of platform coverage within the approved layers.

If a surface is judged necessary for a later cycle, first document its exact locator, query semantics, identity rule, evidence-retention method, and scope rationale in a new manifest version. Declare that version before collection. Do not add it retroactively to Cycle 01 or rewrite manifest v1.

## Shared and nested evidence

- Project 490 is one shared project endpoint, collected once
- ORCID works is one shared candidate endpoint, collected once
- Each lineage retains its own source repository identity, WorkflowHub record, DOI, version history and provenance stream
- Project-level records may inform both lineage analyses but remain one underlying record
- Endpoint attempts, returned records, evidence bundles and cross-checks are nested evidence, not additional independent samples

## Interpretation boundary

A cycle can account for all 22 declared endpoints while retaining partial responses and errors. Report retrieval state, relationship-verification state, record-condition flags, and execution evidence separately. Do not infer global absence from an endpoint error, or execution from a workflow definition.
