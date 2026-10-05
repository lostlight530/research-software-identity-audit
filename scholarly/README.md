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

## ORCID role

ORCID `0009-0001-3617-0832` anchors the scholarly author identity used in `CITATION.cff`, `.zenodo.json`, and `codemeta.json`.

## Identity rule

GitHub repository identity, Zenodo concept record, Zenodo version record, OSF registration, OSF project, ORCID attribution, and downstream discovery records are related but non-equivalent scholarly objects.
