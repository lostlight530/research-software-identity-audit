# Independent research recheck — 2026-10-20

**Diagnostic monitoring**, retrieved **19:08:48–19:10:19 Asia/Shanghai**. Fixed research sample RS01–RS10; six analytical layers, seven operational platforms and 60 planned analytical units are unchanged. No schedule-governed prospective cells are created.

## User pages and independent API counters

All **12 supplied Zenodo page pairs** match the independently captured family `unique_views` / `unique_downloads` exactly. The researcher explicitly confirmed the final-digit split, including the pilot's `13` = **1 unique view / 3 unique downloads**.

### Views

| Scope | User page unique views | API unique views | API total views |
| --- | ---: | ---: | ---: |
| Fixed ten software families | 1,637 | 1,637 | 2,478 |
| Control repository | 118 | 118 | 126 |
| Independent life-science pilot | 1 | 1 | 2 |

### Downloads

| Scope | User page unique downloads | API unique downloads | API total downloads |
| --- | ---: | ---: | ---: |
| Fixed ten software families | 16 | 16 | 17 |
| Control repository | 5 | 5 | 5 |
| Independent life-science pilot | 3 | 3 | 5 |

Family-level unique sums are not globally deduplicated people. Fixed-ten version-only fields are separately retained: **51 views / 48 unique views**, **9 downloads / 9 unique downloads**. The 12-row [page/API crosscheck](user-page-api-reconciliation.csv) retains each original joined number and both independent unique fields.

## Identity and version coverage

- All ten current latest GitHub releases remain `v2026.10-fourteen-day-evidence-checkpoint`.
- Each Zenodo family enumerates four versions with no next page: **40 version DOI records**, all independently joined to findable DataCite records. Ten concept DOIs are separately joined.
- DataCite ORCID enumeration remains **76 distinct findable records**, **56 Software / 19 Workflow / 1 StudyRegistration**.
- ORCID exposes **17 groups / 89 work summaries**.
- OpenAlex now exposes **profile 32 / query 32**, types **12 software / 20 other**, cited-by count **1**. The earlier supplied profile **30** and list/type count **32** remain separate user-source fields, not overwritten by the later API.
- Ten checkpoint version-DOI routes resolve to the **ten concept-level OpenAlex Works**. A successful route is not an exact version-DOI Work: exact-version matches are **0/10**.
- OpenAIRE searches for the ten checkpoint DOIs each return one result. RSD returns eleven specified software records. HAL query returns zero; SciCrunch is 403. OSF registration and Internet Archive metadata are accessible.

## Preservation is inspected at two levels

All ten SWH latest origin visits are `full` with snapshots. The checkpoint tag is visible in two latest snapshots: **Axiom-0** and **Reflective Continuum**. For those two, the snapshot tag target equals the GitHub checkpoint commit, its SWH revision resolves and its directory resolves: **2/10 checkpoint tag→commit→directory chains**.

The remaining eight checkpoint revision requests return 404, and their latest inspected snapshots do not expose the checkpoint tag. This is the observed state of those endpoints, not proof of global/permanent absence or a claim that all ten checkpoint packages are preserved. It does not negate their earlier full-origin visits.

## WorkflowHub sources remain separate

### Views

| Workflow | User Team Dashboard | Independently captured version-detail Activity |
| --- | ---: | ---: |
| 2334 zero | 1,660 | 1,545 |
| 2332 welcome | 1,501 | 1,404 |
| 2337 Brain Evolution | 533 | 502 |
| 2347 Life Science Knowledge Workflow | 256 | 233 |

### Downloads

| Workflow | User Team Dashboard | Independently captured version-detail Activity |
| --- | ---: | ---: |
| 2334 zero | 120 | 115 |
| 2332 welcome | 163 | 156 |
| 2337 Brain Evolution | 26 | 23 |
| 2347 Life Science Knowledge Workflow | 112 | 106 |

User Dashboard totals are **3,950 views**, **421 downloads**. Period selection and exact user-capture timestamp were not supplied. The independently retrieved Activity fields belong to a different surface; they are not substituted into the Dashboard or used to infer negative growth.

## Supplementary software and archive verification

Previously retained October 18 archive bytes were **rehashed**, not redownloaded, and compared with today's Zenodo file metadata: control ZIP **1,392,684 bytes**, MD5 `dbc5b4bdbd5e5fbb3b6fb6eb5ec44fa3`; pilot ZIP **290,240 bytes**, MD5 `d5e515de06f37f03c7118fcee617ccd3`. Both match. Archived control Citation/CodeMeta still carry the October 10 version; pinned current-main metadata carries `v2026.10-evidence-integrity`.

bio.tools remains version 0.4.0 / MIT / Emerging; OpenEBench's named record still has `validated: 0`. Two specified historical GitHub CI runs were reread, not rerun. No private LifeMonitor surface was queried, and no archived source code was executed.

## Attempts, reproduction and publication

**147 requests:** 128 HTTP 200, ten HTTP 400, eight HTTP 404, one HTTP 403. The ten first version-enumeration requests used size=100 and received an explicit unauthenticated size-limit error; corrected size=25 requests all succeeded. Both attempts are retained. No permission expansion was needed.

[Machine record](record.json) · [Version/family fields](zenodo-family-statistics.csv) · [DOI list](datacite-identifiers.csv) · [Evidence representation](../../../evidence/2026-10-20/01-independent-research-recheck/README.md)

Run `python -B tools/check_research_recheck_20261020.py` for offline hashes, count/identity joins, failure-state preservation and page/API reconciliation. Public evidence is explicitly minimized field extracts and original response digests. Full response bytes remain local; the public verifier does not authenticate unpublished transport bytes. Existing October 18 and earlier dated records remain intact.

## Correction / reconciliation after review

The submitted package contained a derived identity-labeling defect: four `object_id` labels were transposed relative to the frozen `corpus/object-manifest.csv`. The repository/DOI-specific values and counters were internally consistent, but four per-object records were attributed to the wrong preregistered units. The exact correction and pre-correction commit are documented in the [correction reconciliation](../../../evidence/2026-10-20/01-independent-research-recheck/correction-reconciliation-01.md).

The corrected `field-extracts.json` and `zenodo-family-statistics.csv` now join by repository slug to the frozen manifest and are ordered RS01–RS10. Only derived object-ID labels and row/array order changed; numeric counters, DOI values, version records, source locators and the 147-attempt capture manifest are unchanged. The original submission remains in Git history.

The earlier `offline-verification.json` was generated before this invariant existed (268 checks / 0 failures); it is explicitly superseded and is not evidence for the corrected package. The offline checker now verifies canonical ID-to-repository mappings in both derived files and rejects a deliberate transposition. It is run as an advisory step in the existing `validate` workflow; this adds no new job or dependency. This correction does not create a prospective observation or alter the frozen contract.
