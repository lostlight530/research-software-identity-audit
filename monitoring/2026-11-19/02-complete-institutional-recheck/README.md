# 2026-11-19 complete public identity-infrastructure recheck

**Class:** future-only public diagnostic, not prospective research observation. The 458 request keys match the 2026-11-18 cohort. Per-request clocks are in the source ledger; capture summary is in summary.json.

## Scope

- 34 supplementary institution/service/standard surfaces
- 102 exact DOI keys queried independently against DataCite, OpenAIRE and OpenAlex (306 requests)
- 67 individually versioned Zenodo records: 60 across RS01-RS10, 5 CONTROL, 2 supplementary LSEL
- 11 GitHub main, 11 GitHub Releases, 11 RSD software, 10 Software Heritage origins, 2 RSD issues, 1 RSD person, 1 RSD project and 4 WorkflowHub records

Fixed corpus RS01-RS10; CONTROL is not RS11; six layers and 60 units per eligible scheduled timepoint remain frozen. Seven operational platforms/70 possible checks are a separate denominator. New prospective cells: 0.

## OpenAIRE aggregation and split

openaire-doi-query-results.csv preserves each DOI query, API total, returned count, page completeness and result IDs. openaire-result-id-groups.csv maps each result ID to queried DOI values. openaire-12-repository-grouping.csv provides the twelve Zenodo-family grouping view.

Aggregation means one result ID is returned for multiple DOI queries within a repository family. Split means one DOI query returns multiple distinct result IDs. A completed zero-result query differs from an unsuccessful request. Only complete result pages enter group summaries.

## OpenAlex and remaining platforms

openalex-work-id-groups.csv maps Work IDs to queried DOI values; openalex-12-repository-version-grouping.csv maps version DOI queries per family. One exact DOI endpoint returns one Work projection; multiple DOI versions resolving to one Work are shared Work mappings, not a multi-Work split. Author-profile works_count remains distinct from DOI exact matches and distinct Work IDs.

datacite-doi-state.csv preserves 102 DOI-level states and resource types. ORCID groups, summaries and source counts are in summary.json. zenodo-67-version-records.csv retains every version row; fixed-ten totals remain null unless all 60 rows have valid counters. surface-results.csv retains all 34 endpoints. request-delta-vs-2026-11-18.csv compares exact request keys.

## Evidence limits

Source ledger -> selected fields -> grouping tables -> summary -> this report. Prior evidence is not overwritten. Provider response bodies are not retained; only response digests, byte lengths, client timestamps and minimized public fields are retained. User-supplied statements are separately retained in maintainer-context.json.

**Disposition:** DIAGNOSTIC_RECHECK / SOURCE-SPECIFIC_PARTIAL_OR_COMPLETE / NO_PROSPECTIVE_CELLS / FROZEN_CONTRACT_UNCHANGED.
