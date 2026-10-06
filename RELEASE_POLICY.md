# Release and Archival Policy

This repository treats `main` as the current operational research state and
release tags as immutable point-in-time snapshots.

## Policy

- Create a release only from a reviewed and merged `main` revision.
- Do not move or rewrite an existing release tag to include later work.
- A release records repository state at publication time; it does not rewrite prior baseline, evidence, or preregistration history.
- Confirm citation, author, license, DOI-role, and related-identifier metadata before archival publication.
- Keep Zenodo concept DOI and version DOI semantically distinct.
- Add a version-specific DOI to release metadata only after that DOI actually exists.
- Preserve failed, partial, unresolved, and rate-limited research states in archived records.
- A release is not evidence that a scheduled observation executed or that a scientific conclusion is valid.

## Existing archive

The initial research-runtime release is:

- GitHub tag: `beta`
- title: `Beta— Research Runtime Bootstrap`
- release date: 2026-10-05
- Zenodo concept DOI: `10.5281/zenodo.23166490`
- archived beta DOI: `10.5281/zenodo.23166491`

The archived beta remains a historical snapshot.

Later changes to `main` must be represented by a later release if they are to
be included in a new archival snapshot.

## Metadata sources

For future GitHub-to-Zenodo releases:

- `.zenodo.json` is the Zenodo-specific archival metadata surface;
- `CITATION.cff` is the repository citation surface;
- `codemeta.json` is the general software metadata surface;
- `scholarly/identifiers.yaml` records identifier roles and provenance.

These files should agree on core repository metadata before a release is
published.
