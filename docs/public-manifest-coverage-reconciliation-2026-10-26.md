# Public artifact integrity coverage reconciliation — 2026-10-26

**Classification:** implementation/assurance correction to the live GitHub research-control runtime. Not a new platform observation, new evidence capture, preregistration amendment, operational schedule, prospective timepoint, release or DOI.

## Reproducible problem and source

- Base GitHub `main` at review start: `41eb9db55ca28794798603ff48d613913581110a`, following merged PR #65
- `.github/workflows/validate.yml` ran `python -B tools/check_public_artifact_manifest.py` without an `--all` argument
- At that base revision, the tool's `DEFAULT` named only `evidence/2026-10-25/02-independent-institutional-recheck/artifact-manifest.json`
- PR #65 contributed two additional published manifests under `evidence/2026-10-26/` (18 morning and 17 evening rows); the reviewer separately inspected those public bytes, but the **configured future CI checksum step** did not automatically include them
- Therefore a green job at the base revision could not, solely by its public-artifact step, warrant a claim that the October 26 manifests were checksum-verified

This is a **verification coverage gap**, not a finding of corrupt historical data. No old manifest or byte artifact is rewritten as part of this logic correction.

## Smallest change

1. Add `discover_manifests(root)` to enumerate repository-local `evidence/**/artifact-manifest.json` paths, including future dated additions
2. Add `verify_all(root)` to aggregate the existing byte/SHA-256 verifier per discovered manifest, retaining per-manifest result/failure information and failing closed if none are found
3. Run `python -B tools/check_public_artifact_manifest.py --all` in the existing **advisory** CI step
4. Keep targeted `--manifest PATH` and historical no-argument behavior for backwards compatibility
5. Use synthetic temporary-tree tests to prove new manifests are automatically discovered, corrupted later additions fail aggregate verification, and files are never modified

No external API call is introduced. The same verifier continues to stream public file bytes and check normalized relative paths, duplicates and self-reference. This covers **published artifact integrity**, not semantic content correctness or original HTTP transport provenance.

## Validation and research-contract boundaries

The PR and post-merge CI runs own executed test evidence. A future failed manifest should be investigated as a concrete missing, modified or incorrectly indexed public file; do not repair a historical source by silently changing its old capture bytes. If a historical locator correction is warranted, retain original manifest bytes, source context and a dated reconciliation, as in PR #65.

- OSF frozen contract, baseline cutoff, RS01–RS10 manifest, six layers, seven platforms and 60 object-layer units/timepoint: unchanged
- Dated monitoring and source evidence: unchanged
- Prospective dataset cells: **0 added**
- No new schedule, Release, tag, DOI, platform request or external service configuration
- Result labels must distinguish `PUBLIC_ARTIFACT_INTEGRITY_VERIFIED` from `RAW_HTTP_REPLAYED` and `SCIENTIFICALLY_VALIDATED`

**Acceptance principle:** all discovered published manifests must be visible to the checker. Aggregate CI remains advisory while the schema and baseline are under convergence; a green overall workflow is not proof of scientific data validity or even that every advisory step passed. Read individual step outcomes.
