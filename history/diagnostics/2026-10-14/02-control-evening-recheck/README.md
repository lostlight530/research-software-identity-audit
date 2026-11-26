# 2026-10-14 21:00-hour control-repository preflight review

**Research subject:** `lostlight530/research-software-identity-audit` — research governance, execution, evidence, provenance and analysis runtime, **not RS11**. All times below are actual 2026-10-14 retrieval windows, not a fabricated 21:00:00 snapshot. This is **diagnostic preflight**, not an OSF-preregistered prospective timepoint.

## Evidence and retrieval contract

- Fresh pre-review [main](https://github.com/lostlight530/research-software-identity-audit/commit/90040902edf4615b3f5ef8c4bec51d946d97b743) = `90040902edf4615b3f5ef8c4bec51d946d97b743`; open PRs = **0**, previous [main advisory CI succeeded](https://github.com/lostlight530/research-software-identity-audit/actions/runs/38527811475)
- [Machine summary](record.yaml); [62 source/attempt rows](platform-attempts.csv); [ten fixed-object GitHub/DOI identity joins](release-candidate-crosswalk.csv)
- Initial GitHub GET batch: **2026-10-14T13:09:14.232Z–13:09:15.349Z**; contract/citation file reads: **13:09:32.699Z–13:09:34.327Z**
- Fixed-ten GitHub Release/tag batch: **13:10:35.684Z–13:10:38.487Z**; detailed release reads: **13:13:39.275Z–13:13:40.543Z**
- Fixed-ten DataCite DOI checks: **13:14:55.259Z–13:14:56.911Z**; control DOI and selected OpenAlex fields: **13:09:56.925Z–13:10:05.238Z**; OpenAIRE/SWH/RSD/RRID/OSF and OpenAlex query: **13:11:36.002Z–13:11:46.550Z**; ORCID Works: **13:14:12.372Z–13:14:12.810Z**
- These are **outer client/tool windows**, not original HTTP completion timestamps or platform ingestion times. GitHub source via an authorized read-only connector; external public sources via content extractor. **No original raw HTTP bytes, per-response headers, verified cache bypass or SHA-256 transport digests retained**. Zenodo standalone retry's exact timing was not captured and is recorded as `NOT_CAPTURED`

## 1. New event that changes readiness: all ten fixed RS software releases

Each fixed RS01–RS10 repository currently has **four published public GitHub Releases** and **four current Git tag refs**. The newest tag is identical across all ten:

`v2026.10-fourteen-day-evidence-checkpoint`

Its public Release timestamps span **2026-10-14T11:14:44Z–11:16:33Z** (Beijing **19:14:44–19:16:33**), after the October 5 registration and **after the October 14 afternoon preflight capture**. Thus [the afternoon three-release observation](../01-preflight-integrity-recheck/README.md) remains correct **for its own retrieval window** and must not be overwritten.

The [ten-row crosswalk](release-candidate-crosswalk.csv) independently ties each GitHub Release/tag name to a **distinct public DataCite-registered Zenodo Version DOI** (`10.5281/zenodo.23365504`, `23365510`, `23365517`, `23365525`, `23365534`, `23365540`, `23365543`, `23365548`, `23365551`, `23365567`), its `IsVersionOf` Concept DOI, creator `0009-0001-3617-0832`, a per-object source URL and separately reported provider timestamps.

**Scientific boundary:** these published releases are **POST_REGISTRATION_RELEASE_ELIGIBILITY_CANDIDATES**. A new public release is now observed, but formal *eligible release* classification, prospective timepoint offsets, and schedule compliance **have not been adjudicated**. The [OSF contract bridge](../../../contract/preregistration.md) requires an eligible post-registration event; the [operational schedule](../../../schedule/README.md) still declares **no concrete offsets**. We cannot silently invent, retrospectively backdate or label this evening's diagnostic queries as 60 preregistered prospective cells. This is a real methodological readiness issue that must remain explicit.

GitHub release descriptions describe **bounded fourteen-day evidence checkpoints**, not new scientific phases, reproduced runtime behavior or a universally validated implementation. Current GitHub tag-ref presence and DataCite registry metadata do not prove bytewise Zenodo archive equality or exact platform-internal propagation timestamps.

## 2. Seven core operational platforms — research-control repository

| Platform | Observed result | Interpretive boundary |
| --- | --- | --- |
| GitHub | Three public control Releases; newest `v2026.10-evidence-reconciliation` published **2026-10-10T15:45:40Z**. Current main CFF/CodeMeta versions and DOI roles align | October 10 immutable tag's embedded older citation metadata remains an **archived drift fact**, corrected only on later main via [PR #34](https://github.com/lostlight530/research-software-identity-audit/pull/34). CI success tests configured advisory checks, not scientific truth |
| Zenodo | Direct reads of control version records `23166491`, `23176748`, `23284570` and `/versions` timed out | **CRAWL_TIMEOUT / current counters NOT_RECHECKED**, not record nonexistence, zero traffic or permission to borrow the afternoon **94 views / 90 unique_views / 3 downloads** as an evening sample |
| DataCite | Control Concept `10.5281/zenodo.23166490` now exposes **three `HasVersion` links**: `23166491`, `23176748`, `23284570`; latest version still has `IsVersionOf` Concept | The earlier two-link mismatch is **not present in this response**, but the cause or time of external convergence is **UNKNOWN**. Previous snapshots stay intact |
| ORCID | Public `/works` extractor yields flattened text with all four control Concept/version DOI strings and the ten new fixed-corpus version DOI strings | Native structured work-group and summary counts **NOT_RECONSTRUCTED**, no claim of complete grouping or exact ingest time |
| Software Heritage | Public origin-visits API extraction returns anti-bot challenge | **ACCESS_CHALLENGED / VISITS_NOT_VERIFIED**, not evidence of missing preserved source |
| OpenAIRE | Graph v1 exact PID for the three control Version DOIs each returns **`header.numFound=1`**; Concept DOI exact PID returns **0** | Exact-PID query asymmetry only, not a claim of global absence or the fixed-ten release propagation matrix |
| OpenAlex | Author-filtered Works query `meta.count=26`; selected author `works_count=26`; full author `works_count=26`, both with `updated_date=2026-10-13T12:33:52` | The three count surfaces **agree tonight**, in contrast to earlier 24/30 conflict. The complete author Work array was truncated by extraction and not fully verified. No inferred cause, transition time, independent software family count or impact interpretation |

The full OpenAlex author profile also returned `cited_by_count=1`; the citing object and provenance were not independently checked, so **do not claim external scholarly impact**.

## 3. Supplementary public surfaces and OSF authority

- **OSF:** [5b329](https://osf.io/5b329/overview) is the governing registration. Tonight the public extractor returned only a generic `OSF` representation: fresh native registration JSON and original-to-updated revision diff **NOT_VERIFIED**. The [afternoon Oct 14 preflight](../01-preflight-integrity-recheck/README.md) separately reported the public October 6 update statement and its declared support-material-only scope; do not rewrite the original registration on that basis
- **RSD:** public API returned one published control software entry; Concept DOI matches `10.5281/zenodo.23166490`. A listing is not institutional endorsement, a new research sample or new analytical layer
- **SciCrunch:** official [RRID resource report](https://scicrunch.org/resolver/SCR_029105) identifies the same control software; curator completion and ownership verification **NOT_VERIFIED**

## 4. Research contract preservation and disposition

The fixed sample is **RS01–RS10**, the frozen layers are **6**, the operational platforms are **7**. Thus **10 × 6 = 60** planned analytical units per *eligible scheduled timepoint* and **10 × 7 = 70** possible source checks. Neither is the count of observations performed this evening.

No baseline correction, OSF amendment, schema or checker edit, schedule declaration, formal prospective observation, control repository release/tag/DOI, or new statistical model was made. Historical provenance and incomplete states remain append-only, including the Oct 13–14 daytime failures, the Zenodo field conflicts, former DataCite relation mismatch, former OpenAlex profile divergence, and today's extraction failures.

**Review disposition:** `CONTROL_PREFLIGHT_RECHECK_COMPLETE`; `TEN_NEW_RELEASE_CANDIDATES_VERIFIED`; `PROSPECTIVE_ELIGIBILITY_UNADJUDICATED`; `DATACITE_CONTROL_HAS_VERSION_3`; `OPENALEX_THREE_SURFACES_AGREE_26`; `ZENODO_EVENING_NOT_VERIFIED`; `SWH_ACCESS_CHALLENGED`; `NO_PROSPECTIVE_DATASET_CREATED`.
