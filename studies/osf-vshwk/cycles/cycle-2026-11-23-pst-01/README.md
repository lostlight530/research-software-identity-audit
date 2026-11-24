# VSHWK Cycle 01 — Project 490 paired-lineage endpoint census

**Disposition:** `CYCLE_ATTEMPTS_CLOSED_WITH_UNRESOLVED_RESULTS`  
**Protocol authority:** [approved VSHWK amendment](https://api.osf.io/v2/schema_responses/6afdcc7108de91a0f0cefdc6/)  
**Manifest:** [immutable endpoint manifest v1](../../contract/endpoints-v1.json)

## 1. Case, sample and denominators

The current case is one WorkflowHub [Project 490](https://workflowhub.org/projects/490) with two paired embedded workflow lineages:

- **A:** [welcome-to-github](https://github.com/lostlight530/welcome-to-github), WorkflowHub [2332 v9](https://workflowhub.org/workflows/2332?version=9)
- **B:** [zero-entropy-lab](https://github.com/lostlight530/zero-entropy-lab), WorkflowHub [2334 v9](https://workflowhub.org/workflows/2334?version=9)

Cycle 01 covers one project-level case, eight predefined infrastructure layers, eight project-layer-cycle bundles, and sixteen nested lineage-layer evidence bundles. The sixteen nested bundles are not independent statistical samples. The 22 endpoint locators are nested collection checks, not research objects.

WorkflowHub 2347 v2 is historical context only. The original registration response and older project-level description do not override the latest approved VSHWK amendment.

## 2. Precollection contract and clocks

- Reporting day: **2026-11-23 America/Los_Angeles**
- Precollection intent declared: `2026-11-24T07:05:22.196Z`
- Actual source acquisition: **2026-11-24T07:07:37.297Z–2026-11-24T07:09:58.002Z UTC**
- Same acquisition window in Asia/Shanghai: **2026-11-24 15:07:37.297–15:09:58.002 +08:00**
- Pacific reporting-day equivalent: **2026-11-23 23:07:37.297–23:09:58.002 -08:00**

The manifest and precollection intent were committed before acquisition in [PR #141](https://github.com/lostlight530/research-software-identity-audit/pull/141). The intent file is an immutable precollection snapshot; its `INITIATED_PENDING_COLLECTION` state and `collection_started=false` describe the moment it was declared and must not be rewritten after collection.

## 3. Endpoint accounting — completion is not success

All **22/22** manifest-v1 endpoints were attempted across both lineages and all eight layers.

| Retrieval state | Count | Meaning |
|---|---:|---|
| `RESPONSE_COMPLETE` | 4 | A bounded connector representation was returned |
| `RESPONSE_PARTIAL` | 9 | Some content was returned, but it did not satisfy the full evidence contract |
| `ENDPOINT_ERROR` | 9 | The bounded request did not return usable endpoint content |
| **Total** | **22** | **Complete attempt accounting, not 22 successful retrievals** |

Relationship-verification states are a separate dimension:

| Relationship state | Count | Bounded interpretation |
|---|---:|---|
| `VERIFIED_DIRECT_LINK` | 8 | Exact queried fields / source identity were directly matched; not a global equivalence claim |
| `RECORD_FOUND_LINK_UNVERIFIED` | 3 | A record/page representation was found, but the tested cross-system relationship was not fully verified |
| `NOT_ASSESSED` | 11 | Retrieval failure or returned content did not support relationship assessment |
| **Total** | **22** | One classification per endpoint row |

## 4. Eight-layer classification

| Layer | Endpoints | Complete | Partial | Errors | Relationship classification |
|---|---:|---:|---:|---:|---|
| L1 Source repository | 4 | 4 | 0 | 0 | 4 direct |
| L2 Workflow registry | 3 | 0 | 3 | 0 | 3 found / link unverified |
| L3 Archival repository | 2 | 0 | 0 | 2 | 2 not assessed |
| L4 Identifier registration / resolution | 4 | 0 | 4 | 0 | 4 direct DOI-field matches |
| L5 Source preservation | 2 | 0 | 1 | 1 | 2 not assessed |
| L6 Testing / monitoring / execution | 2 | 0 | 0 | 2 | 2 not assessed |
| L7 Researcher attribution | 1 | 0 | 1 | 0 | 1 not assessed |
| L8 Discovery / aggregation | 4 | 0 | 0 | 4 | 4 not assessed |
| **Total** | **22** | **4** | **9** | **9** | **8 direct / 3 unverified / 11 not assessed** |

## 5. Paired lineage classification

| Scope | Endpoints | Complete | Partial | Errors | Direct | Found / unverified | Not assessed |
|---|---:|---:|---:|---:|---:|---:|---:|
| Lineage A | 10 | 2 | 4 | 4 | 4 | 1 | 5 |
| Lineage B | 10 | 2 | 3 | 5 | 4 | 1 | 5 |
| Shared Project 490 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| Shared ORCID candidate | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| **Total** | **22** | **4** | **9** | **9** | **8** | **3** | **11** |

Shared Project 490 and ORCID endpoints are retained once, not duplicated as independent lineage records.

## 6. Evidence-backed findings

### Source repositories and version evolution

- Welcome main at collection: `413ffe432073f5bb8b4dd57e8099b6d25bdb04ec`
- Zero main at collection: `00b48696bd875c107c32f5b04f811b5354e6ac08`
- Both `.github/workflows/nexus-life-cycle.yml` files were read at those exact commits
- Both current workflow-file blobs differ from the respective registered v9 source blobs

This is **expected source-version evolution**, not an anomaly. Registered v9 commits remain historical identity anchors; later main revisions may evolve. The hash difference alone does not establish failure, identity conflict, protocol violation, or comparative implementation quality.

### Workflow registry

WorkflowHub Project 490 and records 2332 / 2334 returned bounded normalized page representations. The endpoint rows remain `RESPONSE_PARTIAL` and `RECORD_FOUND_LINK_UNVERIFIED`; page extraction is not a complete version/provenance graph or proof of every cross-system relationship.

### Identifier registration and resolution

- DataCite returned both exact lineage DOIs as `findable`, resource type `Workflow`
- Each bounded DataCite response contained zero `relatedIdentifier` entries; this describes the returned response, not proof that no relationship exists elsewhere
- DOI-bearing landing-page text was returned, but the origin-level redirect chain and provider HTTP status were not retained

The four `VERIFIED_DIRECT_LINK` labels apply only to the exact DOI/source fields queried. They do not establish adoption, execution, scientific validity, or a complete cross-platform provenance graph.

### Archival repository

Both exact Zenodo candidate-search endpoints failed with `CRAWL_HTTP_500`; the separate A-lineage follow-up confirmed the same error. No workflow-to-Zenodo archive relationship was verified. The result is **UNKNOWN**, not global absence.

### Source preservation

- The Welcome response contained Software Heritage API documentation/examples, not a verified live origin-visit receipt
- The Zero endpoint returned `CRAWL_EMPTY_CONTENT`
- No live structured Software Heritage visit was confirmed

Neither response establishes that the source is absent from Software Heritage.

### Testing, monitoring and execution

Both predeclared GitHub Actions workflow-run URLs were rejected by the connector's URL policy (`INVALID_ARGUMENT`). This is a connector access failure, not a provider response and not evidence that the workflows have no runs. No NEXUS CORTEX lifecycle execution was verified in this cycle.

The separate pinned workflow-file reads prove that workflow definitions were present at the observed commits; they do not prove that any run executed.

### Researcher attribution

The shared ORCID works response was flattened. No exact WorkflowHub DOI attribution relationship to either lineage was established in the returned representation. Attribution remains not assessed.

### Discovery and aggregation

The four exact DOI endpoints returned errors: OpenAIRE `CRAWL_LIVECRAWL_TIMEOUT`; OpenAlex `SOURCE_NOT_AVAILABLE`. The first grouped call and the later five-URL follow-up are retained separately. Neither error establishes a negative discovery result.

## 7. Error and follow-up classification

The five endpoint-specific follow-up rows were returned in **one bounded follow-up batch** over the same recorded time window; they are not five separately timed collection windows:

| Endpoint | Follow-up result |
|---|---|
| L3-A Zenodo | `CRAWL_HTTP_500` |
| L8-A OpenAIRE | `CRAWL_LIVECRAWL_TIMEOUT` |
| L8-A OpenAlex | `SOURCE_NOT_AVAILABLE` |
| L8-B OpenAIRE | `CRAWL_LIVECRAWL_TIMEOUT` |
| L8-B OpenAlex | `SOURCE_NOT_AVAILABLE` |

The original primary attempt rows remain unchanged. The primary A-Zenodo error fragment is truncated as `CRAWL_HTTP_`; the follow-up supplies the separately recorded full error code `CRAWL_HTTP_500`, without rewriting the original row.

The two GitHub Actions failures are connector policy rejections, not provider HTTP failures. The Software Heritage empty-content result is also distinct from the Zenodo and discovery-service errors.

## 8. Evidence fidelity and record-condition boundaries

- Original source ledgers are retained under [evidence/](evidence/README.md); they are not rewritten by the normalized index
- Provider-origin HTTP body bytes and response headers were not retained; provider-origin HTTP status is `null`
- Five bounded extractor fragments contain or may contain neighboring page/header/error material from batch concatenation; original fragments remain unchanged and are flagged
- The current v1 normalized endpoint rows do not serialize a `record_condition_flags` field. This cycle reports **NOT SERIALIZED / NOT COMPUTED**, not a zero count of stale, duplicate, or conflicting records
- Four supplementary source-file / registered-version crosschecks are not additional predeclared endpoint attempts
- No imputation, fallback endpoint substitution, or global-absence inference was applied

## 9. Scope, custody and non-actions

- All source repositories and external scholarly services were queried read-only
- Only the existing CONTROL repository received retained study-control records
- No OSF registration/project, WorkflowHub record, DOI metadata, Zenodo record, source repository, or other provider record was modified
- No new DOI or Release was created
- No RS01–RS10 prospective observation cells were written
- No workflow execution was inferred from a file definition or schedule

## 10. Conclusion and next-cycle priorities

**Conclusion:** `CYCLE_ATTEMPTS_CLOSED_WITH_UNRESOLVED_RESULTS`.

Cycle 01 is complete by its 22-endpoint attempt accounting. It is **not** a successful 22-endpoint retrieval cycle, a fully verified cross-infrastructure identity graph, or evidence that unresolved providers contain no records. Endpoint errors are **not global absence**.

The strongest direct observations are the two source-repository states, exact workflow-file reads, expected source-version evolution, and exact DataCite DOI records. The largest unresolved areas are archival linkage, live preservation receipts, lifecycle execution evidence, researcher attribution, and discovery aggregation. Connector-normalized evidence also limits source reproducibility.

Priorities for a later cycle:
1. Improve origin-level transport fidelity where provider access permits; retain original bytes, response headers and status rather than reconstructing them
2. Resolve the GitHub Actions endpoint access method without changing the declared v1 historical record; any future endpoint change must be versioned and predeclared
3. Establish exact query and identity contracts before selecting conditional WorkflowHub testing, LifeMonitor, OpenEBench, Research Software Directory, or nfdi.software surfaces
4. Preserve all unresolved and failed states; do not optimize for all-green reporting

## 11. Record reading order

1. [Precollection intent snapshot](precollection-intent.json)
2. [Immutable manifest v1](../../contract/endpoints-v1.json)
3. [Original source ledgers and provenance](evidence/README.md)
4. [Normalized endpoint outcome index](endpoint-outcome-index.jsonl)
5. [Derived machine summary](cycle-summary.json)
6. This bounded human-readable report

**Small and Stable · Contract before observation · Evidence before interpretation**
