# Research-control repository review — 2026-10-12

**Scope:** `lostlight530/research-software-identity-audit` **only**. This repository is the research-control, governance, evidence/provenance, and analysis runtime for the frozen OSF-preregistered study, **not RS11**, not a replacement for any of RS01–RS10, and not an eligible fixed-corpus release event. No other repository was modified in this review.

**Review date:** 2026-10-12 **Asia/Shanghai**, public cross-platform field extraction with bounded outer execution windows **2026-10-12T11:30:08.810Z–11:33:17.968Z** (19:30:08–19:33:17 China Standard Time), plus narrower follow-up public checks. These windows are **not** evidence of per-response HTTP completion time, provider ingest time, or historical response bytes. The GitHub main-source checks took place during the same review period using an authorized read-only connector.

**Prior main at start:** `0a7e0dccd7f4823b02bcd2bdbf0df0cbc7411e05` — 2026-10-11 citation-metadata correction, merged as [PR #34](https://github.com/lostlight530/research-software-identity-audit/pull/34). There were **0 open PRs**. Configured [post-merge GitHub Actions run 38118916154](https://github.com/lostlight530/research-software-identity-audit/actions/runs/38118916154) completed **successfully**. This is the configured advisory workflow's result, not evidence of running every historical local offline verifier or proving scientific conclusions.

## 1. Repository and archival citation contract

| Check | Public or repository evidence | October 12 assessment |
| --- | --- | --- |
| Latest published audit-control GitHub Release | [`v2026.10-evidence-reconciliation`](https://github.com/lostlight530/research-software-identity-audit/releases/tag/v2026.10-evidence-reconciliation), published **2026-10-10T15:45:40Z** | **VERIFIED** latest of three published GitHub Releases retrieved; no new release created by this review |
| Latest Zenodo archived software version | [record `23284570`](https://zenodo.org/api/records/23284570) under concept `23166490`; release metadata `v2026.10-evidence-reconciliation` | **VERIFIED** direct record read |
| Zenodo family versions | [`/records/23284570/versions?allversions=true`](https://zenodo.org/api/records/23284570/versions?allversions=true): **3**, IDs `23284570, 23176748, 23166491` | **VERIFIED after retries**; earlier version-list and concept-search requests timed out and are **not erased** |
| Zenodo counter fields on latest version record | attached family `views=74`, `downloads=3`, `unique_views=71`; latest specific version `version_views=0`, `version_downloads=0` | **PUBLIC LIVE FIELDS** in this access window, **not** new 33-version recomputation and not frozen historical values |
| Version DOI registry | [DataCite `10.5281/zenodo.23284570`](https://api.datacite.org/dois/10.5281/zenodo.23284570), `registered=2026-10-10T15:45:48Z`, `IsVersionOf=10.5281/zenodo.23166490` | **REGISTERED/RELATION VERIFIED**, does not prove propagation time or usage |
| Concept DOI registry | [DataCite `10.5281/zenodo.23166490`](https://api.datacite.org/dois/10.5281/zenodo.23166490), `updated=2026-10-06T02:48:22Z`, only two `HasVersion` links (`23176748` and `23166491`) | **INCOMPLETE_RELATION_LIST_AT_QUERY_TIME** relative to three Zenodo versions; mechanism and eventual convergence **UNKNOWN** |
| Live `CITATION.cff` | `version=v2026.10-evidence-reconciliation`, first version DOI `10.5281/zenodo.23284570`, date released `2026-10-10`, author `lightlost`, ORCID, MIT | **LIVE MAIN ALIGNED** |
| Live `codemeta.json` | Same latest tag `version`, `datePublished=2026-10-10`, concept DOI `identifier`, author ORCID and MIT | **LIVE MAIN ALIGNED**; concept DOI here has a different intentionally version-independent referent |
| `.zenodo.json` | Stable software title, creator `lightlost` / ORCID `0009-0001-3617-0832`, MIT and `isSupplementTo` the OSF registration | **STABLE ARCHIVAL INPUT**, no phantom new release or forced version-specific DOI |
| Historical release tag payload | GitHub [tagged `CITATION.cff`](https://github.com/lostlight530/research-software-identity-audit/blob/v2026.10-evidence-reconciliation/CITATION.cff) and [tagged `codemeta.json`](https://github.com/lostlight530/research-software-identity-audit/blob/v2026.10-evidence-reconciliation/codemeta.json) still name initial-runtime/October 6 | **IMMUTABLE_ARCHIVED_METADATA_DRIFT** retained; correction to later main through PR #34 does not rewrite those bytes |
| `scholarly/identifiers.yaml` historical snapshot | top-level `recorded_date=2026-10-07` and `repository.current_release_tag=v2026.10-initial-research-runtime`; later appended DOI-expansion record identifies latest third release | **DATED_HISTORICAL_FIELD**, not an up-to-date current-release key; preserve 2026-10-07 semantics and disambiguate via 2026-10-12 review |

The **latest GitHub Release tag is an archived snapshot of prior main**. Changes made on main after the October 10 tag, including PR #34, must not be attributed to that immutable version. The [concept DOI](https://doi.org/10.5281/zenodo.23166490) remains the stable evolving-family citation; cite [version DOI `10.5281/zenodo.23284570`](https://doi.org/10.5281/zenodo.23284570) for the actual October 10 software snapshot. OSF [`10.17605/OSF.IO/5B329`](https://doi.org/10.17605/OSF.IO/5B329) identifies the separate frozen research contract.

## 2. Seven operational infrastructure platforms — control-only supplementary checks

The seven are source interfaces, **not seven preregistered study layers**. The audit-control repository is **outside** the fixed ten-object corpus and the following **control-only supplementary check table is not a set of eligible prospective observation cells**.

| Platform | Exactly bounded October 12 control-repository outcome |
| --- | --- |
| GitHub | Release list displays **three published releases**; latest `v2026.10-evidence-reconciliation`; main at initial check `0a7e0dcc...`, PR #34 merged, configured main CI successful |
| Zenodo | Latest software version record `23284570` **200/parsed** on retry; family `/versions` returned **3 matching IDs** on retry. Earlier `/versions` and direct-record reads **timed out**; concept-search query also **timed out**. Successful alternative path **does not erase** failed attempt states |
| DataCite | Version DOI and `IsVersionOf` parent verified; concept `HasVersion` still lists only **two** of Zenodo's three actual version records. **EXTERNAL_METADATA_RELATION_DIVERGENCE**, no proven cause or inferred ingested-at time |
| ORCID | Public `/works` extraction accessible as **flattened text** containing control software DOI relationships. Exact structured `group` count, work-summary count, ORCID association completeness **NOT_RECONSTRUCTED**, and ownership/curation not inferred |
| Software Heritage | Audit-control GitHub origin visits API returned **bot-protection challenge**, not a parseable visit-list JSON. DOI/deposit-origin attempt yielded an HTML/navigation representation, not verified visit-list JSON. Status **ACCESS_CHALLENGED / STRUCTURED_VISITS_NOT_VERIFIED**, not permanent absence |
| OpenAIRE | `/graph/v1/researchProducts?pid=10.5281%2Fzenodo.23284570` returned **`header.numFound=1`** and one software result titled *Research Software Identity Audit*, DOI PID `10.5281/zenodo.23284570`, internal ID `od______2659::1be8b1942a799c7e2f87c3050ab61d0a`. Exact concept DOI `23166490` returned **`header.numFound=0`**. These are **different exact PID queries**, not general absence or completeness claims; OpenAIRE does not report creator ORCID in this returned software row |
| OpenAlex | Concept DOI exact filter: **1 Work** `W7220365356`; latest **version DOI exact filter: 1 Work `W7221337741`** with creator `A5151904252`/ORCID. Author-filtered Works list returned **21 rows**, compared with previous Oct10 **18**, now additionally showing the two WorkflowHub v4 DOI Works. See below |

**OpenAlex new three exact DOI-to-Work mappings, independently checked through individual Work endpoints and separate DOI queries:**

| Registered DOI | October 12 Work ID | Work type / author relationship |
| --- | --- | --- |
| `10.5281/zenodo.23284570` (audit-control version) | [`W7221337741`](https://api.openalex.org/works/W7221337741) | `software`, author `A5151904252` with canonical ORCID |
| `10.48546/workflowhub.workflow.2332.4` | [`W7221337272`](https://api.openalex.org/works/W7221337272) | `other`, same author/ORCID; **supplementary related workflow**, not RS11 |
| `10.48546/workflowhub.workflow.2334.4` | [`W7221366684`](https://api.openalex.org/works/W7221366684) | `other`, same author/ORCID; **supplementary related workflow**, not RS11 |

OpenAlex author-list and profile response semantics still diverged in this check: author-filtered Works query **21**, `GET /authors/A5151904252?select=id,works_count,updated_date` **21** (`updated_date=2026-10-11T12:31:35`) but unselected `GET /authors/A5151904252` **30** (`updated_date=2026-10-01T12:39:15`). Profile response selection and timestamp differ; **mechanism UNKNOWN**. Work `updated_date=2026-10-11T09:32:39.932853` for the new three is a field returned by the platform, **not independently verified first-indexed time**.

**Prior dated reference:** the [October 10 independent OpenAlex review](../monitoring/2026-10-10/03-openalex-work-aggregation/README.md) obtained **18** author-filtered rows, without the three above. The newer **21** is a subsequent direct query result; it must not be relabeled as the Oct10 contemporaneous state. No model for exact propagation latency is warranted.

## 3. Supplementary public scholarly identity surfaces

- **Research Software Directory (RSD)**: exact [public software REST record](https://research-software-directory.org/api/v1/software?slug=eq.research-software-identity-audit&select=id,slug,is_published,concept_doi) returned exactly one `is_published=true` software listing, `concept_doi=10.5281/zenodo.23166490`. This is a **directory listing**, not upstream institutional endorsement or an eleventh fixed object.
- **SciCrunch / RRID**: [public Resource Report](https://scicrunch.org/resolver/SCR_029105) names *Research Software Identity Audit* and its actual GitHub URL, recommending `Research Software Identity Audit (RRID:SCR_029105)`. Text such as "claim ownership" is not independent proof of successful ownership verification or curator approval.
- **OSF**: preregistered contract and its DOI remain distinct. The public extractor displayed a **documentation/HTML representation** for `/v2/registrations/5b329/` rather than an independently parsed current registration JSON object. Thus this October 12 tool path is **not** claimed to validate a new OSF registration-state payload, and the frozen OSF contract was not edited.

## 4. Evidence, governance and operational readiness

- [Frozen OSF contract](../contract/preregistration.md), fixed [RS01–RS10 corpus](../corpus/object-manifest.csv), [schema counting rules](../schema/counting-rules.md), [operational schedule](../schedule/README.md), historical baseline, and observation-state vocabulary are **not modified** by this audit.
- **10×6=60** preregistered object-layer units per eligible timepoint; **10×7=70** possible operational platform checks; this review neither claims new RS releases nor a new prospective timepoint. All seven platforms above were queried only for control-repository identity diagnostics.
- GitHub release and Zenodo/DOI archived identity are verified, but tag-time citation drift, the DataCite parent relation gap, unresolved SWH visit API challenge, ORCID structural retrieval gap, and OpenAlex author-profile disagreement remain explicitly recorded.
- Only **public identifiers and public metadata** were used. No credentials, private emails, cookies, traffic secrets, API tokens, ownership claims, or access challenges were bypassed. The public extractor provided normalized JSON/text, **not unchanged original HTTP transport bytes, request headers, per-response server Date or SHA-256 provenance**. Do not claim a bytewise raw archive or successful local-offline checker execution.
- For this audit, `UNKNOWN`, `PARTIAL`, `BLOCKED` and query-level `NOT_OBSERVED` are legitimate results. A returned `header.numFound=0` is a **query result**, not proof of universal non-existence.

## Outcome

**`CONTROL_RUNTIME_CURRENT_CITATION_ALIGNED; ARCHIVE_TAG_DRIFT_PRESERVED; OPENAIRE_VERSION_VISIBLE; OPENALEX_NEW_VERSION_WORK_VISIBLE; REGISTRY_PARENT_RELATION_INCOMPLETE; SWH_AND_ORCID_PARTIAL`.**

**Next procedural check before any future archival release:** confirm tag-version agreement against `CITATION.cff` and `codemeta.json` **before publishing**, preserve version DOI only once minted, and leave previous tags untouched. A new release/DOI is **not created** by this October 12 review. The evidence limitations above require no artificial test data, schedule, RS11, extra operational platform or new external registry integration.
