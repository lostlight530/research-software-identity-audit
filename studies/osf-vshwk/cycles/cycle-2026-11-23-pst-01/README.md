# OSF vshwk cycle 01 — actual Monday PST prospective observation attempts

**Study authority:** [OSF vshwk latest approved amendment](https://api.osf.io/v2/schema_responses/6afdcc7108de91a0f0cefd6c/) — 2026-11-18 submitted, `reviews_state=approved`, WorkflowHub Project 490, 2332 v9 (Welcome) and 2334 v9 (Zero). Original 2347 v2 is historical context, not the current primary sample.

**Reporting day:** 2026-11-23 America/Los_Angeles. Real extraction interval: **2026-11-24T07:07:37.297Z to 2026-11-24T07:09:58.002Z**, i.e. Nov 23 23:07–23:09 PST; China date 2026-11-24. Actual clocks are never backdated to the reporting-day folder.

**Contract before observation:** [endpoint manifest v1](../../contract/endpoints-v1.json) and [cycle initiation reason](intent.json) were merged in [CONTROL PR #141](https://github.com/lostlight530/research-software-identity-audit/pull/141) **before** collection began; initiation timestamp is `2026-11-24T07:05:22.196Z`. No observation was retrospectively promoted.

## Completion ≠ successful retrieval

| Attempt status from original connector | Count |
| --- | ---: |
| `RESPONSE_COMPLETE` | **4** |
| `RESPONSE_PARTIAL` | **9** |
| `ENDPOINT_ERROR` | **9** |
| **Predeclared endpoint attempts recorded** | **22/22** |

Every declared endpoint has an actual attempted source record. Errors are not discarded. Five additional, separately timed, per-URL checks preserve error details; original attempts and first-window outcomes remain immutable. Both lineages, all eight layers and the shared project endpoint were covered.

One project-level case × 8 layers yields **8 project-layer-cycle bundles**; paired two lineages × 8 layers yield **16 nested lineage-layer evidence bundles**. Neither the 22 URL attempts nor the 16 nested bundles are independent additional statistical subjects. Shared Project 490 and candidate ORCID evidence are referenced once, not multiplied.

## Verified and unresolved observations

- **GitHub current source at collection:** Welcome main `413ffe432073f5bb8b4dd57e8099b6d25bdb04ec`; Zero main `00b48696bd875c107c32f5b04f811b5354e6ac08`. Both actual `.github/workflows/nexus-life-cycle.yml` files were independently read at these exact commits.
- **Version provenance:** Git file blobs for both registered WorkflowHub v9 commits differ from the corresponding workflow file at these two observed main commits. This is **expected source version evolution**, not an anomaly: registered v9 hashes remain historical anchors while current main evolves. The hash difference does not imply failure, identity conflict, noncompliance, invalidity or which implementation is better.
- **WorkflowHub:** Project 490 and records 2332/2334 returned normalized page representations. Exact approved-v9 anchors come from OSF; current page extraction alone does not prove full cross-system relationship equivalence.
- **DataCite:** `10.48546/workflowhub.workflow.2332.9` and `10.48546/workflowhub.workflow.2334.9` returned exact DOI records, both `findable`, resource type `Workflow`. Each returned metadata record has **0 relatedIdentifier entries** in these bounded responses; that is not proof that no relation exists anywhere.
- **DOI resolver:** DOI-bearing landing-page text was returned, but origin-level redirect chain and HTTP status were not independently retained.
- **Zenodo:** Both exact candidate-search URLs produced `CRAWL_HTTP_500` at the extractor. One separately timed Welcome retry also failed. Archival association or absence is **UNKNOWN**, not `not present`.
- **Software Heritage:** Welcome returned API documentation/examples, **not** a verified live visit; Zero returned `CRAWL_EMPTY_CONTENT`. No live structured preservation receipt was confirmed.
- **GitHub Actions:** The two predefined workflow-specific run endpoints were rejected by connector URL policy. This is a **connector failure**, not proof of no NEXUS CORTEX executions.
- **ORCID:** Shared Works extract is flattened; no exact WorkflowHub DOI attribution link to either lineage was established.
- **OpenAIRE / OpenAlex:** First group-call transport failure is retained; separately timed exact URL attempts produced timeout (OpenAIRE) and `SOURCE_NOT_AVAILABLE` (OpenAlex). Both are **UNKNOWN** for actual discovery status.

## Source fidelity and end-state

See [original evidence and follow-ups](evidence/README.md), [normalized 22-endpoint index](endpoint-outcomes.jsonl) and [machine summary](summary.json). Original provider HTTP bytes, response headers and exhaustive pagination were not retained; status is **DEGRADED even though attempt coverage is COMPLETE**. Some extractor fragments contain adjacent batched content and are flagged without rewriting original source.

**Disposition:** `CYCLE_ATTEMPTS_CLOSED_WITH_UNRESOLVED_RESULTS`. No endpoint error is counted as global absence, no unverified identity promoted as verified, and no source repository, OSF, WorkflowHub, Zenodo or other external platform was modified. Separate OSF `5b329` historical monitoring and prospective schedule remain untouched.
