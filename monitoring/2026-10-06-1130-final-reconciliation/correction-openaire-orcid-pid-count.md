# Correction: OpenAIRE ORCID-link count semantics

Date: 2026-10-06

## Trigger

The earlier OpenAIRE page showed `11 ORCID links` across three pages. That
display was initially normalized as an ORCID-linked software-result count.

A later exact PID search for ORCID `0009-0001-3617-0832` supplied a stronger
semantic observation:

- Research products: 1
- Projects: 0
- Data sources: 0
- Organizations: 0

The sole research product is:

- `lostlight530/research-software-identity-audit: Beta— Research Runtime Bootstrap`
- DOI: `10.5281/zenodo.23166491`
- type: Research software
- source: Zenodo

## Correction

The earlier value `11` is retained as observed UI evidence but is reclassified
as a Link-service/UI count with unresolved exact entity semantics.

It must not be used as the count of research products returned by exact ORCID
PID search.

The supported exact-PID research-product count is `1`.

## Research impact

No preregistered unit changes.

The fixed corpus remains RS01-RS10.

The correction affects only OpenAIRE counting semantics in the post-release
reconciliation record.
