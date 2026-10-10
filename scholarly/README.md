# Scholarly identity and archival surfaces

This repository participates in a wider scholarly-object graph, but each surface has a distinct role.

## Canonical identifiers

- **GitHub repository:** https://github.com/lostlight530/research-software-identity-audit
- **Zenodo concept DOI (all versions):** https://doi.org/10.5281/zenodo.23166490
- **Zenodo beta release DOI:** https://doi.org/10.5281/zenodo.23166491
- **OSF Registration:** https://osf.io/5b329/overview
- **OSF Registration DOI:** https://doi.org/10.17605/OSF.IO/5B329
- **Associated OSF Project:** https://osf.io/wa5v8
- **Author ORCID:** https://orcid.org/0009-0001-3617-0832

Machine-readable identifier roles are recorded in `identifiers.yaml`. Human citation guidance is in `CITATION.md`.

## Zenodo role

The Zenodo concept DOI identifies the evolving repository across versions.

The version DOI identifies the exact archived `beta` release.

The repository badge therefore links to the concept DOI:

`10.5281/zenodo.23166490`

while the archived beta snapshot is identified by:

`10.5281/zenodo.23166491`

Future releases must preserve this concept/version distinction.

## OSF role

The OSF registration DOI identifies the frozen preregistered research contract.

The associated OSF project remains a live project surface for ongoing study materials and links.

Neither OSF identifier is interchangeable with a Zenodo software DOI.

## Scholarly-object boundary

GitHub repository identity, Zenodo concept record, Zenodo version record, OSF registration, OSF project, ORCID attribution, and downstream discovery records are related but non-equivalent scholarly objects.

## October 10 supplementary verification and correction

The [dated scholarly-infrastructure reconciliation](infrastructure-review-2026-10-10.md) records independently accessible RSD software/person/ten-software project links, the publicly searchable control-repository RRID `SCR_029105`, open upstream RSD Issues #1870/#1871, still-open rseng PR #498, DataCite concept/version DOI relations, and explicit OpenAIRE/SWH/OpenAlex access or interface uncertainties. It does **not** imply institutional accreditation, formal collaboration, platform account login verification, or scientific review.

**Control repository has two archived version DOIs**, not only the historical beta: `10.5281/zenodo.23166491` (beta) and `10.5281/zenodo.23176748` (October runtime), both under concept DOI `10.5281/zenodo.23166490`. This extends the earlier beta-only explanatory example without changing the prior historical release record.

The older `identifiers.yaml` `recorded_date=2026-10-07` and `rrid.public_indexing_state=pending` describe that **dated** state. The [October 10 reconciliation](infrastructure-review-2026-10-10.md) separately verifies **public RRID search visibility**, while the exact indexing-event time, full curator-workflow status and ORCID ownership association are still unknown.
