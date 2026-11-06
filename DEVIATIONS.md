# Deviations

Append-only ledger for departures from a declared procedure that do not silently redefine the research contract.

No deviations are recorded by the bootstrap commit.

## Entry template

### DEV-YYYYMMDD-NN — Short title

- **Observed:** ISO-8601 timestamp
- **Expected procedure:** what was planned
- **Actual event:** what happened
- **Cause:** known cause or unresolved
- **Affected observations:** IDs/timepoints/layers
- **Handling:** retained, retried, marked failed, partial, etc.
- **Interpretive impact:** none / bounded / material / unresolved
- **Related evidence/PR/commit:** references

A deviation is evidence about execution and should not be hidden merely because it is inconvenient.

## Recorded process deviations

### DEV-20261106-01 — GitHub Contents API catalog writes bypassed branch → PR

- **Observed:** 2026-11-06T15:38:45Z–2026-11-06T15:40:20Z, based on the first and last directly written Git commit timestamps. These are **commit clocks**, not a reconstructed exact HTTP request window
- **Expected procedure:** begin from fresh CONTROL `main`, create an isolated branch, review the diff, run advisory checks through a PR, and squash merge after verifying the review and CI results
- **Actual event:** ten **new** RS01–RS10 tracked-path catalog CSV files under `docs/repository-inventory/2026-11-06/` were created through GitHub Contents API calls without an explicit `branch`; the destination defaulted to CONTROL `main`. This is a **repository-maintenance execution-process deviation**, not an OSF preregistered study procedure, scheduled observation, or newly released study object
- **Cause:** the branch argument was omitted for those ten create-file operations, as recorded in the inventory report; no unrelated execution mechanism is inferred
- **Affected observations:** **none**. Zero RS01–RS10 research objects added or removed; zero of the six preregistered layers or 60 possible object-layer units for an eligible scheduled point changed. No research raw source/evidence, frozen contract, historical baseline, formally eligible prospective cell, DOI or Release was altered
- **Handling:** **RETAIN / DOCUMENT / NO HISTORY REWRITE**. Preserve the ten Git commits and their catalog blob identities as reproducible provenance, rather than deleting/recreating valid files or force-pushing. The separate branch-based [inventory PR #94](https://github.com/lostlight530/research-software-identity-audit/pull/94) completed the report, remaining catalogs and navigation, while [PR #95](https://github.com/lostlight530/research-software-identity-audit/pull/95) documented the subsequent OSF GitHub-provider projection. Both were merged; post-merge CONTROL workflow [42247576102](https://github.com/lostlight530/research-software-identity-audit/actions/runs/42247576102) concluded `success`. For future modifications, explicitly use a dedicated branch and PR
- **Interpretive impact:** **none to the fixed scientific sampling/denominator and historical observation content; bounded repository governance/auditability issue**. This entry does not retroactively make the direct commits PR-reviewed. GitHub CI success is not independent validation of the 8,802 catalogued file bodies
- **Related evidence/PR/commit:** [pinned 11-repository inventory and original process disclosure](docs/repository-inventory/2026-11-06/README.md) · [all ten commit SHAs, times and classifications](docs/repository-inventory/2026-11-06/control-main-commit-delta-since-2026-11-05.csv) · first direct-main [`e5908d2c133bc80c79384c0e9af38ca172d8c195`](https://github.com/lostlight530/research-software-identity-audit/commit/e5908d2c133bc80c79384c0e9af38ca172d8c195) · last direct-main [`44b3defa6a67cf0eb45b6519fc8245827731c7a6`](https://github.com/lostlight530/research-software-identity-audit/commit/44b3defa6a67cf0eb45b6519fc8245827731c7a6)

**Status:** `CORRECTLY_DISCLOSED_AND_RETAINED`; no original files removed; no formal amendment, new schedule, or prospective observation added
