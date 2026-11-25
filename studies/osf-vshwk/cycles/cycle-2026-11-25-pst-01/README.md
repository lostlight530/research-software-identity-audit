# Day 2 — OSF VSHWK — independently initiated Project 490 full-scope cycle

**Cycle ID:** `cycle-2026-11-25-pst-01`  
**Approved authority:** OSF VSHWK schema response `6afdcc7108de91a0f0cefd6c`  
**Task / reporting day:** Day 2, 2026-11-25 America/Los_Angeles (PST)  
**Precollection declaration:** 2026-11-25T13:34:22.306Z UTC in [immutable intent](precollection-intent.json), committed before queries  
**Initial endpoint query windows:** 2026-11-25T13:35:07.326Z–2026-11-25T13:36:22.146Z UTC (tool-call envelopes)  
**Supplementary verification:** up to 2026-11-25T13:40:11.886Z UTC

## Scope and Day 2 independence

One WorkflowHub Project 490 case, paired lineage A: workflow 2332 v9, lineage B: workflow 2334 v9. The [immutable manifest v1](../../contract/endpoints-v1.json) prescribes **22 endpoint locators in eight layers**. A new, documented full-scope reviewer request initiated Day 2 before any source fetch; Day 1 records were used for **format only**, not copied as fresh evidence or extrapolated as current status. The historical Cycle 02 custody gap is left untouched; this is a newly initiated cycle, not a replacement for missing original attempts.

## Endpoint accounting and findings

**Primary attempted endpoints: 22/22**; initial retrieval states: {"RESPONSE_COMPLETE":2,"RESPONSE_PARTIAL":16,"ENDPOINT_ERROR":4}. Two GitHub Actions exact URLs were rejected by the GitHub connector but then returned **partial extracted first-page run records** through a separate tool at those same URLs. Both workflow-source files were independently pinned to exact Git blobs; those follow-ups do not overwrite the original failed or partial attempts. Both Zenodo searches returned extractor errors.

| Layer | Exact locator attempts | Bounded interpretation |
|---|---:|---|
| L1 source repository | 4 | Both new main SHAs and two exact workflow definition Git blobs were independently verified; YAML presence does not prove execution |
| L2 workflow registry | 3 | Version-9 WorkflowHub records returned exact target DOI text; Project 490 excerpt does **not** independently demonstrate both lineage memberships in its bounded snippet |
| L3 archival repository | 2 | Both Zenodo query extraction calls errored; archive relationship remains unresolved |
| L4 identifiers / resolution | 4 | DataCite exact A/B DOIs appeared; both retained excerpts show empty `relatedIdentifiers` arrays; DOI resolver output is a partial rendered landing page, not proof of software provenance |
| L5 source preservation | 2 | Software Heritage fragments resemble API documentation / example request-response text, **zero verified live structured visit receipts** |
| L6 testing and execution | 2 | Same-URL supplementary extractor found GitHub Actions run IDs `45549148507` (A) and `45548254443` (B), each showing `schedule`, `completed`, `success`. These are actual run-record excerpts, but not evidence that registered historical v9 was executed by those current-main runs |
| L7 researcher attribution | 1 | One shared ORCID works excerpt, not two or sixteen independent attribution records; exact relations to both focal lineages remain unverified from the retained bounded snippet |
| L8 discovery / aggregation | 4 | Two OpenAIRE DOI-filtered API excerpts reported `total=0`; both OpenAlex DOI-keyed Work records appeared with matching DOI; provider categories and search scopes differ |

**OpenAlex identities:** A `https://openalex.org/W7234696653`; B `https://openalex.org/W7225559577`. This is discovery of those DOI-linked Work objects, **not** proof of source-code equivalence, user adoption, or a verified end-to-end workflow propagation chain.

## Units, evidence fidelity, unresolved states

The case remains **one independent project** with **eight project-layer bundles** and **16 nested lineage-layer evidence bundles**, the latter not independent study samples. The manifest contains 22 collection locators, not 22 independent cases. The [endpoint outcome index](endpoint-outcome-index.jsonl) tracks each locator's original attempt separately from any follow-up, while the [machine summary](cycle-summary.json) provides exact state and layer counts.

The saved GitHub connector projections and web-extractor excerpts are **not provider-origin HTTP** body/status receipts. Query failure, a scoped OpenAIRE zero, absent extraction fields, and a rendered Software Heritage documentation example are **not global absence**. Condition flags not captured are recorded as unassessed rather than zero. No fallback endpoint was silently substituted into the 22-locator manifest.

**Disposition:** `CYCLE_ATTEMPTS_CLOSED_WITH_UNRESOLVED_RESULTS`. The primary attempt ledger is complete, but source retrieval/relationship verification is partial and does not imply all eight layers are scientifically fully verified. No OSF update, external repository mutation, DOI issuance, preregistration amendment, or historical backfill occurred.

- [Independent precollection intent](precollection-intent.json)
- [Primary-source and follow-up evidence index](evidence/README.md)
- [Machine cycle summary](cycle-summary.json)
- [Exactly 22 endpoint outcome rows](endpoint-outcome-index.jsonl)
