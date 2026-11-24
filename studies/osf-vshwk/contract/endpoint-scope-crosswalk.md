# OSF VSHWK scope-to-endpoint crosswalk

**Protocol authority:** approved Schema Response `6afdcc7108de91a0f0cefdc6`  
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

## Approved scope named conditionally but not selected as v1 endpoints

The approved schema response also describes possible evidence surfaces subject to an exact, directly supportable relationship with the focal project or lineage:

- WorkflowHub-displayed testing metadata
- LifeMonitor
- OpenEBench
- Research Software Directory
- nfdi.software

These surfaces are **not endpoint locators in manifest v1**. Their absence from v1 means `NOT_SELECTED_IN_MANIFEST_V1`, not `NOT_FOUND`, provider absence, or a negative study result. The v1 contract avoids inventing fallback URLs or broad searches without a verified query and identity contract.

If a surface is judged necessary for a later cycle, first document its exact locator, query semantics, identity rule, evidence-retention method, and scope rationale in a new manifest version. Declare that version before collection. Do not add it retroactively to Cycle 01 or rewrite manifest v1.

## Shared and nested evidence

- Project 490 is one shared project endpoint, collected once
- ORCID works is one shared candidate endpoint, collected once
- Each lineage retains its own source repository identity, WorkflowHub record, DOI, version history and provenance stream
- Project-level records may inform both lineage analyses but remain one underlying record
- Endpoint attempts, returned records, evidence bundles and cross-checks are nested evidence, not additional independent samples

## Interpretation boundary

A cycle can account for all 22 declared endpoints while retaining partial responses and errors. Report retrieval state, relationship-verification state, record-condition flags, and execution evidence separately. Do not infer global absence from an endpoint error, or execution from a workflow definition.
