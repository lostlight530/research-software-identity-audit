# Scholarly release checklist

Use this checklist before creating a GitHub/Zenodo release.

## Identity

- [ ] Release tag and title are final.
- [ ] The tag points to the intended commit.
- [ ] `CITATION.cff` reflects the release version and release DOI when known.
- [ ] `codemeta.json` reflects the intended software identity.
- [ ] `.zenodo.json` creator metadata includes the correct ORCID.
- [ ] OSF registration DOI and Zenodo DOI are not conflated.
- [ ] The repository remains explicitly outside the fixed ten-object study corpus.

## Contract

- [ ] No README, schema, or tooling change silently rewrites the frozen OSF preregistration.
- [ ] Operational specifications are labeled as operational specifications.
- [ ] Substantive post-registration changes are recorded in `AMENDMENTS.md`.
- [ ] Execution departures are recorded in `DEVIATIONS.md`.
- [ ] Exploratory/post hoc work is labeled.

## Data and evidence

- [ ] Prospective observations are post-registration and follow an eligible release trigger.
- [ ] Every planned object-layer unit is accounted for.
- [ ] Missing/rate-limited/unresolved/partial/failed states remain in the record.
- [ ] Evidence references resolve to retained or externally persistent evidence.
- [ ] Historical evidence is not replaced by current live state.
- [ ] No secrets, credentials, private material, or redistribution-restricted evidence is included.

## Analysis

- [ ] Derived outputs trace back to raw observations and evidence.
- [ ] No missing values are silently imputed.
- [ ] No unsupported absence claim is introduced.
- [ ] Preregistered and exploratory analyses remain distinguishable.
- [ ] Conclusions remain bounded to the observed corpus and infrastructure contracts.

## Archival release

- [ ] GitHub release notes state what is and is not included.
- [ ] Zenodo ingest has completed.
- [ ] Version-specific DOI is recorded after minting.
- [ ] Concept DOI remains the stable all-versions citation surface.
- [ ] `scholarly/identifiers.yaml` is updated when DOI state changes.
- [ ] OSF project resources are updated when a new archival object should be linked.
