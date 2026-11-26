# VSHWK cycle 2026-11-26 PST 02 — independently declared checkpointed review

**Disposition:** `CYCLE_ATTEMPTS_CLOSED_WITH_UNRESOLVED_RESULTS`.

This is a separately initiated review, not a repair of [attempt 01](../../capture-gaps/2026-11-26-pst-01/README.md). The original attempt count remains unknown. See [precollection intent](precollection-intent.json), [startup gate review](../../../startup-gate-review-2026-11-26.json), and the immutable manifest v1. The last documented approved VSHWK response is `6afdcc7108de91a0f0cefdc6`; a fresh exhaustive revision-list check is unavailable. No operational task-day number is assigned.

## Acquisition and counting

- Precollection declaration: 2026-11-26T08:09:38.402Z; committed at [f09b335](https://github.com/lostlight530/research-software-identity-audit/commit/f09b335bf1d0307e2b26d5be8af0fed41dde89ea).
- Connector invocation window: 2026-11-26T08:10:03.138Z–2026-11-26T08:10:59.971Z UTC (Pacific 2026-11-26T00:10:03.138-08:00–2026-11-26T00:10:59.971-08:00; Asia/Shanghai 2026-11-26T16:10:03.138+08:00–2026-11-26T16:10:59.971+08:00).
- 22/22 declared locators have newly recorded attempt receipts in three committed batches, with no retries; 4 complete expected identity-field responses, 14 partial extractor representations, 4 errors.
- Complete retrieval here refers to expected fields, not retained provider-origin HTTP bytes, atomic cross-provider state, or scientific completeness.
- One project case × eight layers = eight analytical bundles; two embedded lineages × eight layers = sixteen nested evidence bundles, not independent subjects. Shared Project 490 and ORCID receipts are counted once.

| Layer | Endpoints | Complete | Partial | Error |
| --- | ---: | ---: | ---: | ---: |
| L1_source_repository | 4 | 4 | 0 | 0 |
| L2_workflow_registry | 3 | 0 | 3 | 0 |
| L3_archival_repository | 2 | 0 | 0 | 2 |
| L4_identifier_registration_resolution | 4 | 0 | 4 | 0 |
| L5_source_preservation | 2 | 0 | 2 | 0 |
| L6_testing_monitoring_execution | 2 | 0 | 0 | 2 |
| L7_researcher_attribution | 1 | 0 | 1 | 0 |
| L8_discovery_aggregation | 4 | 0 | 4 | 0 |

## Bounded findings

GitHub main identities for A and B are `d58327faf9811cc1931ebf4922999d65fc120485` and `6a816f8843bf6c654cc439cf4875cfb47be2a4db`. Workflow file blobs are `85017c64e2f1197a588ce7cc1fbbb3f484f8b08c` and `9f7c430fa244e3e772b802a963d7e2e434820195`. Head and workflow refs were read independently, not atomically. Both Actions locators were rejected by the connector; no workflow-run result is established.

Dated WorkflowHub and DataCite excerpts acquired on 2026-11-22 contain the exact 2332.9 and 2334.9 version DOIs and the registry project excerpt links both focal records. The two DOI landing excerpts have extractor acquired day 2026-11-26; actual redirect chains are not retained. Zenodo search errors were reported by the extractor as HTTP 500; provider-origin status remains unknown. Software Heritage returned documentation-style older excerpt bodies with candidate visit/snapshot identifiers, not verified fresh structured origin visits. ORCID's 2026-11-12 excerpt does not establish exact focal version links. Both OpenAIRE software-query excerpts acquired on 2026-11-25 show scoped zero hits; OpenAlex excerpts of that date identify W7234696653 and W7225559577 with matching canonical DOIs. Scoped zero is not global absence. No execution, adoption, equivalence of archived bytes, or complete fresh propagation is inferred.

The relation classifications (13 directly linked returned representations, 2 candidate records with link unverified, 7 unresolved) refer to the fields in the captured representation, not its freshness. The extractor acquisition day and our attempt timestamps are deliberately separate. No Study 1 prospective cell, new schedule, provider mutation, or study amendment is created.

- [Endpoint index](endpoint-outcome-index.jsonl)
- [Machine summary](cycle-summary.json)
- [Evidence custody](evidence/README.md)
