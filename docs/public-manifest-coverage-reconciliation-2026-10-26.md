# Public artifact integrity coverage reconciliation — 2026-10-26

**Classification:** implementation/assurance correction to the live GitHub research-control runtime. Not a new platform observation, new evidence capture, preregistration amendment, operational schedule, prospective timepoint, release or DOI.

## Reproducible problem and source

- Base GitHub `main` at review start: `41eb9db55ca28794798603ff48d613913581110a`, following merged PR #65
- `.github/workflows/validate.yml` ran `python -B tools/check_public_artifact_manifest.py` without an `--all` argument
- At that base revision, the tool's `DEFAULT` named only `evidence/2026-10-25/02-independent-institutional-recheck/artifact-manifest.json`
- PR #65 contributed two additional published manifests under `evidence/2026-10-26/` (18 morning and 17 evening rows); the reviewer separately inspected those public bytes, but the **configured future CI checksum step** did not automatically include them
- Therefore a green job at the base revision could not, solely by its public-artifact step, warrant a claim that the October 26 manifests were checksum-verified

This is initially a **verification coverage gap**, not by itself a finding of corrupt historical data. The expanded check subsequently surfaced one concrete historical locator conflict, reconciled below without altering original bytes.

## Smallest change

1. Add `discover_manifests(root)` to enumerate repository-local `evidence/**/artifact-manifest.json` paths, including future dated additions
2. Add `verify_all(root)` to aggregate the existing byte/SHA-256 verifier per discovered manifest, retaining per-manifest result/failure information and failing closed if none are found
3. Run `python -B tools/check_public_artifact_manifest.py --all` in the existing **advisory** CI step
4. Keep targeted `--manifest PATH` and historical no-argument behavior for backwards compatibility
5. Use synthetic temporary-tree tests to prove new manifests are automatically discovered, corrupted later additions fail aggregate verification, and files are never modified

No external API call is introduced. The same verifier continues to stream public file bytes and check normalized relative paths, duplicates and self-reference. This covers **published artifact integrity**, not semantic content correctness or original HTTP transport provenance.

## Newly surfaced historical locator mismatch: October 9

The first all-manifest PR run ([Actions #40354566511](https://github.com/lostlight530/research-software-identity-audit/actions/runs/40354566511)) discovered **13 manifests / 184 entries**; one October 9 manifest had **one file** with both a byte-length and SHA-256 mismatch. The verifier's two error messages describe the **same affected artifact**, not two distinct corrupted files. This run also caught an invalid synthetic test assumption about lexicographic manifest order, corrected in the same PR.

Source chain:

- The [original October 9 facility-recheck commit](https://github.com/lostlight530/research-software-identity-audit/commit/e36ccfbb16d9cbdfbccaa8a73167aee37488235b) recorded `monitoring/2026-10-09/01-facility-recheck/README.md` as **3,904 bytes**, SHA-256 `8834dc1ef68df9a31d0c83ee94738c6df58f167e9eca76f37abd842f7384d0d3`
- The [later October 9 reviewer commit](https://github.com/lostlight530/research-software-identity-audit/commit/9e62b7ccc3d5fd89d1a8320ff9646dce929e2e24) appended the separate review entrypoint to the mutable README. Its current checkout representation is **4,304 bytes**, so the unchanged original evidence manifest had a stale navigation locator
- The original 3,904-byte README is now retained under `evidence/2026-10-09/01-facility-recheck/prior-index-snapshots/monitoring-readme-20261009-original.txt`. Its Git blob SHA `c23091e68c90de9c5b57fccbe1afe442d4c26e9a` matches the original commit's blob exactly
- The original October 9 artifact manifest is independently copied **without edits** to `prior-index-snapshots/artifact-manifest-20261009-original.json` (original Git blob SHA `00f306a70032ed20592f73fa41445de1e400f6bf`)
- Only the active October 9 manifest's **README locator** is redirected to the byte-identical fixed snapshot, keeping its originally recorded byte count and SHA-256 unchanged. The current human-readable monitoring README remains unchanged
- `.gitattributes` prevents line-ending normalization of these fixed snapshots, including the original CRLF README, on non-Linux checkouts

This is a **dated source/locator reconciliation**, not a retrospective alteration to a scientific counter, platform request, capture clock, original review or the historical evidence itself. A later correctly updated README remains useful navigation, but cannot satisfy the checksum of the earlier version.

## Validation and research-contract boundaries

The PR and post-merge CI runs own executed test evidence. A future failed manifest should be investigated as a concrete missing, modified or incorrectly indexed public file; do not repair a historical source by silently changing its old capture bytes. If a historical locator correction is warranted, retain original manifest bytes, source context and a dated reconciliation, as in PR #65.

- OSF frozen contract, baseline cutoff, RS01–RS10 manifest, six layers, seven platforms and 60 object-layer units/timepoint: unchanged
- Dated monitoring and source evidence: unchanged
- Prospective dataset cells: **0 added**
- No new schedule, Release, tag, DOI, platform request or external service configuration
- Result labels must distinguish `PUBLIC_ARTIFACT_INTEGRITY_VERIFIED` from `RAW_HTTP_REPLAYED` and `SCIENTIFICALLY_VALIDATED`

**Acceptance principle:** all discovered published manifests must be visible to the checker. Aggregate CI remains advisory while the schema and baseline are under convergence; a green overall workflow is not proof of scientific data validity or even that every advisory step passed. Read individual step outcomes.
