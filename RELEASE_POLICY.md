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

## Later formal runtime archive — 2026-10-06

The initial beta listing above is a historical snapshot, not a claim that the beta is the only published version.

- GitHub tag: `v2026.10-initial-research-runtime`
- GitHub published: `2026-10-06T02:48:16Z`
- Zenodo version DOI: `10.5281/zenodo.23176748`
- Existing concept DOI: `10.5281/zenodo.23166490`
- DataCite registered: `2026-10-06T02:48:21Z`

This is an **already archived** release, not a release performed by this documentation update. The original beta DOI `10.5281/zenodo.23166491` remains valid for citing that exact beta. For both version identities, see [scholarly/CITATION.md](scholarly/CITATION.md) and [scholarly/identifiers.yaml](scholarly/identifiers.yaml).
