# Study 2 contract — OSF VSHWK

## Authority precedence

1. **Scientific protocol authority:** OSF VSHWK approved amendment Schema Response [6afdcc7108de91a0f0cefdc6](https://api.osf.io/v2/schema_responses/6afdcc7108de91a0f0cefdc6/), submitted 2026-11-18T18:58:20.050020Z, `reviews_state=approved`
2. **Historical registration context:** the original VSHWK response `6af56f49221ba1b47e9f7490` preserves the initial WorkflowHub 2347 v2 framing and earlier three-wave wording; that original framing is historical, not the current case authority
3. **Current VSHWK registration-page metadata:** the owner-supplied OSF Metadata snapshot displays `Date Updated: Nov 24, 2026, 8:00 PM`. The public OSF API reports `date_modified=2026-11-24T12:00:17.626133Z`, equivalent to `2026-11-24 20:00:17.626 Asia/Shanghai`. The current Description names WorkflowHub Project 490, Lineage A (2332 v9), Lineage B (2334 v9), and 2347 v2 as historical context, but it still contains the sentence about "three prospective observation waves". This is descriptive registration-page metadata, not a schema response or amendment; the approved response above governs operational cycle initiation and timing
4. **Public project description:** AUHJF's separate owner-confirmed Description is preserved verbatim at [public-project-description.md](../public-project-description.md). It is project-level text, not a VSHWK schema response or amendment; its 2347 v2 / three-wave wording is not the current VSHWK protocol
5. **Operational implementation:** this directory, the endpoint manifest, cycle records, and validators implement the approved protocol; they do not amend OSF

The current approved case is WorkflowHub Project 490 with paired embedded lineages 2332 v9 (welcome-to-github) and 2334 v9 (zero-entropy-lab). WorkflowHub 2347 v2 remains historical context only.

## Research units and counting rules

- One bounded project-level case: Project 490
- Eight predefined scholarly-infrastructure layers
- Eight project-layer-cycle bundles per complete cycle
- Sixteen nested lineage-layer evidence bundles per complete cycle
- The sixteen nested bundles are repeated descriptive evidence within one case, not independent subjects or statistical samples
- The 22 endpoints in manifest v1 are nested collection checks, not 22 research objects or independent units
- Shared project-level and researcher-attribution evidence is retained once and linked into relevant nested analyses

## Cycle initiation and timing

The approved design uses repeated observation cycles, not a predetermined number of calendar-based waves. It sets no fixed interval, fixed maximum cycle count, or fixed calendar end date.

A cycle may be initiated by a relevant public infrastructure event or a documented full-scope review. The reason, reporting-day label, manifest version, and precollection intent must be recorded before acquisition begins.

Retain actual source acquisition timestamps in UTC and Asia/Shanghai. America/Los_Angeles is used only to label the reporting day. A reporting-day folder name never replaces the actual acquisition clock.

## Immutable endpoint contract

- [endpoints-v1.json](endpoints-v1.json) is the first declared operational endpoint set, created before Cycle 01 collection
- Published manifest versions are immutable. A future endpoint change requires a new versioned manifest and a documented scope / protocol-deviation rationale before the affected cycle begins
- Do not silently add fallback URLs, substitute providers, or retroactively expand a closed cycle
- See the [eight-layer and endpoint scope crosswalk](endpoint-scope-crosswalk.md) for included v1 endpoints and approved-but-not-selected conditional services

## Evidence and state separation

Keep these dimensions separate in every cycle:

1. **Endpoint retrieval state** — `RESPONSE_COMPLETE`, `RESPONSE_PARTIAL`, `NOT_FOUND_AT_QUERIED_ENDPOINT`, `RATE_LIMITED`, `ACCESS_BLOCKED`, `ENDPOINT_ERROR`, `NOT_QUERIED`, `NOT_APPLICABLE`
2. **Relationship verification state** — `VERIFIED_DIRECT_LINK`, `RECORD_FOUND_LINK_UNVERIFIED`, `UNRESOLVED`, `CONFLICT`, `NOT_ASSESSED`, `NOT_APPLICABLE`
3. **Record-condition flags** — `STALE_METADATA`, `DUPLICATE_REPRESENTATION`, `CONFLICTING_METADATA`; an unrecorded flag field is not a zero count
4. **Testing / monitoring / execution evidence** — distinguish registry testing metadata, monitor state, actual workflow run identity, run ID, triggering event, source revision, status, conclusion, and associated artifacts

A workflow file's presence does not prove execution. A GitHub Actions connector error does not prove that no run exists. A timeout, empty extractor result, blocked request, or failed search is not global absence. A DOI's `findable` state does not establish a related-identifier edge, adoption, or scientific validity.

## Provenance, fidelity, and analysis

- Original connector representations and provider-origin HTTP bytes are different evidence classes. If origin bytes, response headers, or HTTP status are unavailable, preserve `null` and label the capture as normalized connector/extractor output
- Never call an opaque connector result HTTP 200; never reconstruct missing provider bytes from a normalized excerpt
- Keep raw source ledgers immutable; normalized endpoint indexes, summaries, tables, and interpretations are derived products with explicit source references
- Preserve errors, partial results, unresolved relationships, and later corrections; corrections append and never rewrite the original attempt
- No imputation, causal inference, population-level generalization, adoption inference, institutional endorsement inference, or global quality score
- Report every count with its unit and denominator; do not treat endpoints, evidence bundles, lineages, or sample cases as interchangeable

## Physical separation

- Study 1 [5b329](https://osf.io/5b329/) owns root-level `contract/`, `history/diagnostics/`, `history/evidence/`, and conditional `observations/`
- Study 2 owns `studies/osf-vshwk/contract/` and `studies/osf-vshwk/cycles/`
- No Study 2 cycle writes RS01–RS10, modifies either source repository, changes OSF registrations/projects, or writes to WorkflowHub, Zenodo, DataCite, Software Heritage, ORCID, OpenAIRE or OpenAlex
