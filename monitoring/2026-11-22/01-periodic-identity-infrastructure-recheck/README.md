# 2026-11-22 research software identity and infrastructure periodic recheck

**Classification:** `DIAGNOSTIC / REAL_RELEASE_AND_DOI_CHANGE / PARTIAL_DISCOVERY / NO_PROSPECTIVE_CELLS`

**Source windows:** current batch receipts are in [source files](../../../evidence/2026-11-22/01-periodic-identity-infrastructure-recheck/) and [machine summary](summary.json), assembled at `2026-11-22T15:05:30.872Z` (23:05:30 Asia/Shanghai). Timestamps attached to connector calls are actual collector batch windows, **not** provider publication, ingestion, indexing, or HTTP first-seen times. Historical comparison: [November 20 bounded diagnostic](../../2026-11-20/01-firstday-to-current-infrastructure-diagnostic/README.md) and [November 19 full 458-request cohort](../../2026-11-19/02-complete-institutional-recheck/README.md). These cohorts have different request denominators and transport/evidence fidelity.

## Contract and preserved identities

- Original OSF Registration [5b329](https://osf.io/5b329/overview), original October 5 Schema Response, and separately approved October 6 `344-83` wording revision remain distinct authority objects; refer to [version reconciliation](../../../contract/osf-registration-version-governance-2026-11-03.md)
- Fixed `corpus/object-manifest.csv` is **RS01–RS10** only; CONTROL `research-software-identity-audit` is **not RS11**, and supplementary LSEL is not an added fixed sample
- Six preregistered layers × ten objects = **60 object-layer analytical units per eligible scheduled point**. Seven operational platforms allow 70 potential object-platform checks. Neither is the count of Zenodo version rows
- [Operational schedule](../../../schedule/README.md) still declares no concrete offsets. A historical October 14 observed candidate release event is already documented, and November 20 is **not** unilaterally redesignated the first eligible event or a retrospective T0. No formal prospective rows, baseline rewrites, OSF writes, schema changes, release creation or DOI minting occurred in this diagnostic

## Same-source identity and change reconciliation

| Surface | Directly supported current evidence | Precise comparison / meaning |
| --- | --- | --- |
| GitHub main | **11/11** exact HEAD SHAs captured, all 11 differ from the pinned Nov 20 source snapshot | Git commit movement, not proof of research result change or code correctness |
| GitHub Releases | **10/10 RS01–RS10** latest published tags equal `v2026.11-twenty-day-evidence-checkpoint`, published 2026-11-20 04:55:19–04:55:50 UTC; CONTROL latest published tag remains `v2026.11-nov15-identity-reconciliation` | Nov 20 early diagnostic queried Releases ~00:29 UTC, **before** these ten published Releases. Its prior no-new-release result was valid for that earlier window |
| GitHub open PR | **0 across 11** on current query | `epistemic-pipeline#261` previously open was merged 2026-11-20 02:22:51 UTC, not a new open PR |
| Zenodo new versions | **10/10** latest published records with exact source repo and November 20 version tag; record IDs: `24387218, 24387215, 24387213, 24387214, 24387219, 24387210, 24387208, 24387209, 24387207, 24387220`, in RS01–RS10 order | Ten **new version identities**, **zero new research software samples** |
| DataCite | **10/10** exact new version DOI lookup identities, state `findable`, type `Software` | DOI registration verified within normalized connector representation; not downstream adoption |
| OpenAIRE | **10/10** exact DOI query strings return `total=1` and one result in each bounded extracted page | Positive DOI queries; aggregation semantics and independent software identity must not be inferred from query count |
| OpenAlex | New ten DOI exact-read attempts blocked by source extraction and backup external-reader rate limit | `UNKNOWN / BLOCKED`, **not ten negative discovery observations** |
| ORCID | Public Works content extracted, but the reader flattens the response; structured current group/summary count not independently recomputed | `PARTIAL`. Previous Nov 19 18 groups / 119 summaries remains an **older as-of value**, not a Nov 22 value |
| Software Heritage | 10 origin endpoints attempted; three rendered API documentation or embedded examples, seven returned connector `CRAWL_EMPTY_CONTENT` | No reliable live structured visit-count census; previous archival states cannot be replaced by these extraction failures |
| RSD | Eleven public software pages plus project and researcher pages yielded bounded text (13/13) | 10 fixed-object records + separately identified CONTROL; public listing is not institutional endorsement or proof of all metadata freshness |

### Usage metrics: exact comparable versions only

The **same 60 original Zenodo version record IDs** from November 20 were re-read, all 60 yielded exact record/DOI matches and typed `stats.version_views` and `stats.version_downloads`. Across those exact keys:

| Counter (summed version rows) | Nov 20 | Nov 22 batch | Delta |
| --- | ---: | ---: | ---: |
| `version_views` | 4,281 | 4,397 | **+116** |
| `version_downloads` | 45 | 51 | **+6** |

The **ten November 20 new version rows**, not present in the Nov 20 early 60-row cohort, separately had **12 version views / 11 version downloads** in the present retrieval. Thus the now inspected **70 Zenodo version identities** total **4,409 version views / 62 version downloads**. This is a **version-record sum**, **not** a total of unique people, attached-family views, ten new research objects, 70 operational platform checks, or 70 preregistered analytical units. No traffic source, human adoption, citation, or third-party reproduction is inferred.

### 34 supplementary institution/service/standard surfaces

All **34 fixed source locators** from the existing surface register received an attempted read with per-batch UTC bounds. The current Exa output provided **26 bounded content representations**, **8 connector errors** (ScreenIT ASWG, dkNET, InterLex, OSF Registries within this particular batch, Internet Archive, HAL, OpenAlex and Identifiers.org). Returned content includes homepages, standards pages and API documentation; `CONTENT_RETURNED` is **not** equivalent to verified software indexing or provider HTTP 200.

The separate earlier OSF registration read returned public/accepted metadata, while this subsequent 34-URL batch returned `CRAWL_HTTP_500` for OSF. These are **different connector outcomes**, not evidence that the accepted preregistration disappeared. EDAM ontology text and SWH documentation are not JSON-equivalent records. The previous Nov 20 source batch was **25 returned content / 9 not returned**, but the exact status categories and source freshness are not directly interchangeable.

**Additional RSD/RSE public interactions:** RSD [#1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870) closed October 16 and [#1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871) closed November 16; neither closure alone proves deployed code. RSE [#498](https://github.com/rseng/software/pull/498) remains open and unmerged. Fixed RS07 [PR #261](https://github.com/lostlight530/epistemic-pipeline/pull/261) is merged, and current open PR count is zero across the eleven tracked repositories.

**OSF service policy change, separate from the study contract:** COS [officially announced](https://help.osf.io/article/727-osf-projects-transition) that new OSF Projects are unavailable from November 16, 2026, and existing OSF Projects are scheduled to become read-only on February 19, 2027. The associated project `wa5v8` may need future workspace-planning attention if it holds mutable materials; **the frozen Registration `5b329` and registration workflow are unaffected**. No urgent project relocation or new registration is implied without inspecting actual material usage.

## Provenance and limitations

- Evidence is append-only, with separate [GitHub main](../../../evidence/2026-11-22/01-periodic-identity-infrastructure-recheck/github-main-11.jsonl), [Release](../../../evidence/2026-11-22/01-periodic-identity-infrastructure-recheck/github-latest-releases-11.jsonl), [PR](../../../evidence/2026-11-22/01-periodic-identity-infrastructure-recheck/github-open-prs-11.jsonl), [60 matched Zenodo version rows](../../../evidence/2026-11-22/01-periodic-identity-infrastructure-recheck/zenodo-60-same-version-attempts.jsonl), [ten new versions](../../../evidence/2026-11-22/01-periodic-identity-infrastructure-recheck/zenodo-latest-ten.jsonl), [DataCite](../../../evidence/2026-11-22/01-periodic-identity-infrastructure-recheck/datacite-ten-new-doi.jsonl), [OpenAIRE](../../../evidence/2026-11-22/01-periodic-identity-infrastructure-recheck/openaire-ten-new-doi.jsonl), [34 supplementary source attempts](../../../evidence/2026-11-22/01-periodic-identity-infrastructure-recheck/supplementary-source-attempts.jsonl), [RSD public pages](../../../evidence/2026-11-22/01-periodic-identity-infrastructure-recheck/rsd-11-software-project-person.jsonl), [SWH origin attempts](../../../evidence/2026-11-22/01-periodic-identity-infrastructure-recheck/swh-ten-origin-probes.jsonl) and [interaction states](../../../evidence/2026-11-22/01-periodic-identity-infrastructure-recheck/public-interactions.jsonl)
- The selected evidence files carry actual connector call batch windows, stable source URLs, Git blob identities in `summary.json`, explicit unknown/error outcomes, and bounded public fields. They are **not** original provider HTTP bytes or reliable per-request HTTP status receipts; first-index times and deeper internal propagation paths cannot be reconstructed
- This is **not** a repeat of the November 19 458-request/102-DOI cohort. It checks 60 old and ten newly discovered Zenodo versions, ten new DOI keys on DataCite/OpenAIRE, limited OpenAlex/ORCID/SWH and the registered 34 supplementary surfaces. Different source denominators must not be turned into recovery/failure percentages
- Read-only scientific diagnostic; no code defect independently verified, no frozen-contract correction, no historical raw evidence rewritten. Only append-only current diagnostic and machine receipts are proposed for the research-control repository
- `NOT_EXECUTED_LOCALLY`: local checkout/network execution of the repository checker was unavailable in this task environment; GitHub PR CI must be examined separately. CI passing, if it occurs, validates the configured workflow rather than scientific truth

**Disposition:** `RECORD_REAL_CHANGE / KEEP_PARTIAL_AND_UNKNOWN / NO_CODE_CORRECTION_REQUIRED / NO_PROSPECTIVE_DATASET_START`
