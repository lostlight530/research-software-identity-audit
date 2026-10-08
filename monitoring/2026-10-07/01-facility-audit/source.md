# Supplied independent-audit summary — 2026-10-07

> Provenance note: this file preserves the substantive content supplied in the current conversation. Chat transport escaping and Markdown presentation are normalized. It is not a raw API-response archive and it is not a substitute for the referenced request log, response-byte manifest, or 70-row platform matrix.

Reported collection window:

`2026-10-07T14:45:45.460815+08:00` to `2026-10-07T14:56:19.143805+08:00`, Asia/Shanghai.

The supplied summary reported:

- GitHub: ten third releases using tag `v2026.10-open-research-production-framework`
- Zenodo: ten third-version records and corresponding concept DOI families; 695 family views, 664 family unique views, 7 downloads, 6 unique downloads
- current-version counters: 54 version views, 46 version unique views, 0 version downloads
- files: ten ZIP metadata entries totaling 29,282,855 bytes, with per-file checksums said to be retained in the absent evidence package
- DataCite fixed corpus: 40 DOI records findable, all typed Software
- ORCID: 12 groups / 54 source summaries total; fixed ten software families 10 groups / 50 summaries; audit runtime 1 group / 3 summaries; OSF 1 group / 1 summary
- Software Heritage: ten Zenodo DOI-origin routes with full visits, deposit release 3, and resolvable directory endpoints; GitHub-origin Axiom endpoint unresolved after two connection failures
- OpenAIRE: ten current-version DOI matches with software records reported `UNDER_CURATION`
- OpenAlex: author A5151904252 with 41 works (40 Software + 1 other), all OA, eight primary topics; all 40 fixed-corpus DOI records matched
- RSD: 11 software records reported `is_published=true` (ten fixed-corpus objects plus the separate audit runtime); `Agentic Research Constellation` reported public
- OSF / Internet Archive: registration 5b329 API and archive.org registration-copy metadata reported successful
- HAL: ORCID query returned zero public records; source explicitly did not treat this as evidence that no deposit was submitted
- RRID: one resolver connection failed and another official path returned 403; assigned `SCR_029105` retained from prior registry evidence

## Supplied per-repository table

The source used the following RS labels:

| source RS | repository | family views | family unique views | family downloads | OpenAlex current-version Work | ORCID summaries |
|---|---|---:|---:|---:|---|---:|
| RS01 | welcome-to-github | 90 | 87 | 4 | W7219674182 | 5 |
| RS02 | zero-entropy-lab | 66 | 59 | 0 | W7219850859 | 5 |
| RS03 | Axiom-0 | 85 | 81 | 0 | W7219917759 | 5 |
| RS04 | reflective-continuum | 44 | 43 | 0 | W7219566156 | 5 |
| RS05 | agent-foundations | 71 | 66 | 1 | W7219738811 | 5 |
| RS06 | china-agentic-observatory | 81 | 77 | 0 | W7219788805 | 5 |
| RS07 | agentic-frontier-observatory | 85 | 81 | 1 | W7219897209 | 5 |
| RS08 | sci-render-kit | 57 | 57 | 1 | W7219708281 | 5 |
| RS09 | auto-doc-engine | 52 | 50 | 0 | W7219899314 | 5 |
| RS10 | epistemic-pipeline | 64 | 63 | 0 | W7219690058 | 5 |

The source totals were 695 family views / 664 family unique views / 7 family downloads.

The source RS06–RS10 display-order labels conflict with the canonical manifest already established on repository main. Derived files in this package therefore normalize those IDs by repository identity; see `mapping-reconciliation.md`.

## Supplied Software Heritage route details

The source reported ten Zenodo-origin deposit release 3 routes and directory SWHIDs, plus separate GitHub-origin latest-readable visit timestamps. Those rows are normalized into `swh-routes.csv`.

The source explicitly stated that ZIP-unpack byte-for-byte comparison was not run.

## DataCite supplementary scope

In addition to the fixed 40 DOI sample, the source reported these four findable DOI records:

- OSF registration: `10.17605/OSF.IO/5B329` — StudyRegistration
- audit runtime concept: `10.5281/zenodo.23166490` — Software
- audit runtime beta: `10.5281/zenodo.23166491` — Software
- audit runtime later version: `10.5281/zenodo.23176748` — Software

The source therefore described an explicit 44-DOI check scope rather than using a prior aggregate “active DOI” count as a substitute.

## ORCID source split

The source reported:

- DataCite: 33
- OpenAIRE: 11
- author-added: 10
- total: 54

It also stated that a prior snapshot had the same total but a different source distribution and that source-level change requires put-code diffing.

## OpenAlex relation

The source reported OSF registration Work `W7220380722` as type `other`, associated with author `A5151904252` / ORCID `0009-0001-3617-0832`, and referencing audit-runtime beta Work `W7220470293`.

The source described this as an internal citation relation in the research activity. This package preserves the relation but does not infer a unique ingestion or propagation causal edge from it.

## Referenced but unavailable artifacts

The supplied summary referenced these artifacts as existing outside fresh repository main:

- `Evidence/IndependentFacilityAudit20261007/Results.json`
- `Evidence/IndependentFacilityAudit20261007/RequestLog.json`
- `Evidence/IndependentFacilityAudit20261007/CollectionContract.json`
- `Evidence/IndependentFacilityAudit20261007/EvidenceManifest.json`
- `Evidence/IndependentFacilityAudit20261007/PlatformMatrix.csv`
- `Methods/CollectIndependentFacilityAudit20261007.py`
- `Methods/DeriveIndependentFacilityAudit20261007.py`
- `TenRepositoryWave2Update20261007.md`
- `TenRepositoryAuditCurrentSummary20261007.md`

Fresh `main` returned 404 for those exact paths during this update. They are therefore not represented here as repository-resident evidence.
