# OpenAlex exact version-DOI query: returned Work primary-DOI scope

**Record class:** append-only diagnostic normalization of **third-party extracted representations**, not an original OpenAlex HTTP archive, not a new platform event, not a preregistered observation, and not a change to the original or revised OSF contract

**Relationship to prior work:** [2026-11-01 / 02 follow-up](../02-followup-identity-infrastructure/README.md) retained concept-vs-version identity as unresolved. This record sharpens the *bounded fields that were actually returned*, without claiming any new source-side transition or a full original-source census

## Query/response normalization

[Ten-row source-scoped mapping](openalex-version-query-response.csv) contains one selected **2026-10-30 version DOI** per fixed software object RS01–RS10. Every extracted lookup **returned a Work**; in **10/10 extracted excerpts** the returned Work's top-level `doi` is the corresponding **Zenodo concept DOI**, **not** the version DOI used in the lookup URL. Ten Work IDs are distinct across the ten object families. This establishes a bounded `version DOI query → concept-primary Work` mapping **in these extracts**, not ten separately identified version-primary Works

- **Extraction receipt:** `extract_38119fce74251caa83349a6c8f9c1a47`, a ten-URL OpenAlex request with live-fetch allowed but response acquisition **UTC-day truncated**: RS01 `2026-11-01T00:00:00Z`, RS02–RS10 `2026-10-31T00:00:00Z`. These are extractor acquisition day labels, **not** source-origin HTTP request timestamps, and older cached content is possible
- **Source locators:** the exact OpenAlex DOI lookup URL is retained per row. Top-level returned `id` and `doi` values are literal extracted fields. Prior [seven-platform ledger](../01-periodic-identity-infrastructure-recheck/core-seven-platform-recheck.csv) supplies the selected version/concept DOI pairs, with provenance limitations retained
- **Not established:** whether OpenAlex separately indexes all version DOI identifiers under other fields or other Work IDs, whether DOI alias resolution or consolidation caused this response, current source-origin content, provider ingestion lag, new citation counts, or a substantive propagation change
- **No false absence inference:** a returned concept-primary Work does **not** mean the version DOI is unregistered, unavailable at DataCite, or globally undiscoverable. Zenodo and DataCite selected version DOI representations were separately retrieved in the previous follow-up and this verification
- **Research denominator:** fixed RS01–RS10, 6 preregistered layers, 60 object-layer units per eligible scheduled point; OpenAIRE and OpenAlex remain separate operational checks inside `discovery_graph`. The ten query/response rows are diagnostic representations, **not** new analytical units, scheduled observations or releases

**Disposition:** `EVIDENCE_SCOPE_CLARIFIED__NO_NEW_PROVIDER_STATE_PROVEN__VERSION_LEVEL_WORK_UNRESOLVED__NO_CHANGE_REQUIRED`. No mutation of historical evidence, preregistered contract, corpus, scholarly citation metadata, DOI, tag, Release, or prospective dataset
