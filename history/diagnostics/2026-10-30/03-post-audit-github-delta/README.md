# October 30 post-audit GitHub state delta

**Diagnostic monitoring / append-only addendum, NOT prospective observation** · compiled 2026-10-30T14:42:31.209Z UTC · study logical date 2026-10-30 (Asia/Shanghai)

## Why this additional record exists

The earlier [October 30 34-surface inspection](../02-bounded-periodic-infrastructure-recheck/README.md) was committed as [#73](https://github.com/lostlight530/research-software-identity-audit/pull/73) using a previous GitHub state. Subsequent **real GitHub merges** changed that state. This is a **bounded increment about repository and upstream PR state**, not a second 34-surface capture or an amendment.

The linked [machine record](record.json) contains **11 complete HEAD SHAs**, exact source URLs, previous snapshot prefixes, six PR numbers and merge clocks. All direct GitHub API checks occurred in a **client-observation envelope** spanning `2026-10-30T14:36:03.103Z` through `2026-10-30T14:42:31.209Z`. This is an execution envelope only: **neither per-origin HTTP request timestamps nor release/publication times**. The connector returned structured selected fields, not archived origin HTTP bodies or response headers.

## Directly rechecked GitHub state

- 11/11 canonical `main` refs read; all 11 HEAD SHAs differ from the corresponding earlier October 30 note (CONTROL now `aaaf7d6d`, previously `6546c9de`; fixed-software values in `record.json`)
- 11/11 repository Open PR lists returned **zero** at this later inspection, compared with **six** recorded in the earlier same-day snapshot
- All six earlier PRs were checked individually and returned **merged=true**, not simply closed: [welcome #864](https://github.com/lostlight530/welcome-to-github/pull/864), [zero #754](https://github.com/lostlight530/zero-entropy-lab/pull/754), [auto-doc #194](https://github.com/lostlight530/auto-doc-engine/pull/194), [epistemic #190](https://github.com/lostlight530/epistemic-pipeline/pull/190), [China #215](https://github.com/lostlight530/china-agentic-observatory/pull/215), [global #219](https://github.com/lostlight530/agentic-frontier-observatory/pull/219). Their exact GitHub merge times are kept in `record.json`
- 11/11 direct `GET /releases?per_page=100` checks are **unchanged in the comparable fields**: every RS01–RS10 repository returns four published Releases, latest `v2026.10-fourteen-day-evidence-checkpoint` (October 14 UTC); CONTROL independently returns four, latest `v2026.10-evidence-integrity` (October 18 UTC). This API **does not constitute an exhaustive Git tag or draft inventory**
- Latest-matching `main` Actions results returned `success` for seven sample/control engineering repositories plus CONTROL; three repos returned no `main` runs in that API query. The latest CONTROL [#73 main run](https://github.com/lostlight530/research-software-identity-audit/actions/runs/40982063480) and each configured advisory step reported success. No inference of absent CI bugs or scientific validity follows

The main changes are **engineering/documentation merges**, not new registered research-software versions, 60 planned observations, academic citation events or independently measured platform adoption.

## Institutions, platforms, and the 34-surface boundary

Fresh connected GitHub metadata: RSD [#1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870) is closed (2026-10-16 UTC) but no production fix redeployment or manual reproduction was established; [#1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871) remains open. RSE [#498](https://github.com/rseng/software/pull/498) remains open/unmerged. RSD upstream latest Release `v6.7.5` was published October 27 and concerns security changes; a vendor Release does not certify which version is running in the researcher's production editing session.

The prior same-day **34 representative URL attempts** remain at their original evidence level: **11 same-day-acquired extracts**, **15 older extracts**, **2 connected GitHub source reads**, **6 failed URLs**. These are neither 34 independent institutions nor 34 full object censuses. This addendum **did not reacquire these 34 sources**, nor complete contemporaneous Zenodo, DataCite, ORCID, SWH, OpenAIRE or OpenAlex object-level re-enumeration. Therefore: **NO NEW VERIFIED SCIENTIFIC PROPAGATION STATE** from this GitHub delta. The [October 26 full checklist result](../../2026-10-26/02-evening-institutional-recheck/README.md) retains its historical metrics and genuine retrieval date.

## Frozen contract and action decision

- [OSF original/revised field reconciliation](../01-osf-schema-response-version-reconciliation/README.md) is already recorded: 29 compared response fields, only `Other planned analysis` revised; later benchmarking is not retroactive preregistration
- RS01–RS10 fixed; CONTROL is **not RS11**; **six layers × ten objects = 60 units**, versus seven operational platforms/70 *possible checks*
- [Schedule](../../../schedule/README.md) still has **no concrete offsets**; October 14 Releases do not by themselves authorize an eligible scheduled prospective wave; zero prospective cells added
- No change to OSF, corpus, baseline, schema, schedule, prior raw evidence, prior diagnostic records, tags, Releases, DOIs or external accounts. This record merely captures a proven **GitHub state transition** with precise source attribution
- No new software defect or frozen-contract drift was established requiring a code repair: `NO_CHANGE_REQUIRED`; **external full-census status `PARTIAL / UNKNOWN`**

**Verification boundary:** machine summary is valid JSON, the direct GitHub joins and six PR timestamps come from the connected GitHub responses; CI and external research transport must be interpreted separately. No offline clone or complete source checker run is claimed merely because this report was prepared.
