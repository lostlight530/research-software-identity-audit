# 2026-11-20 main-line custody reconciliation of November 19 research evidence

**Record class:** Git-only source-history/record-custody reconciliation, not a new
external platform retrieval, retrospective raw reconstruction or prospective study observation

- Reconciliation documentation created at: `2026-11-20T00:18:03.398Z` UTC
- Pre-import CONTROL main: [`5951dba891bc021246e48f75379ef158e5b327b4`](https://github.com/lostlight530/research-software-identity-audit/commit/5951dba891bc021246e48f75379ef158e5b327b4)
- Archived source evidence tree: [`9b8c1cbbbd4f2c09961b171bfd8f5c2c4caefb63`](https://github.com/lostlight530/research-software-identity-audit/commit/9b8c1cbbbd4f2c09961b171bfd8f5c2c4caefb63)
- Pre-import source evidence tree SHA: `81e63e6d32d062bccb3618f227e36aada11589e4`
- Source provenance: [PR #128](https://github.com/lostlight530/research-software-identity-audit/pull/128) and
  [PR #130](https://github.com/lostlight530/research-software-identity-audit/pull/130) were merged into the
  **research/2026-11-19-institutional-recheck-evidence** branch,
  **not** into `main`
- The `main` PRs #127 and #129 did not incorporate those source event paths
- Therefore 2026-11-19 events `01`–`05` and their companions were absent from
  `main` before this reconciliation even though source blobs existed in Git history

## Exact corrective action

- Import the **74 previously absent Git blobs** under
  `monitoring/2026-11-19/` (42) and `evidence/2026-11-19/` (32)
  **by their original Git blob object SHAs**, without downloading and rewriting them
- Restore the two dated navigation indices `monitoring/README.md` and
  `evidence/README.md` from the source branch: each contains its existing
  `main` content as an unmodified prefix followed by additive November 19
  event links
- Preserve the source history `01` path-reuse correction record and the actual
  `02` 458-request ledger and evidence; do **not** collapse repeated attempts
  into a synthetic single capture
- Preserve the latest source-specific 04/05 semantic reconciliations, including
  unknown, failed or partial outcomes and their actual capture provenance

These paths are source-event **identity** restoration, not first publication at
the original capture time. The current PR/merge time is a later custody event.
Importing by Git SHA guarantees exact bytes for the imported Git blobs, but
**does not prove** that the original external HTTP response bytes were retained
or that the source-platform findings were scientifically correct

## Contract and remaining limits

- Frozen [OSF 5b329](https://osf.io/5b329) and its later approved revision
  remain distinct historical authority objects
- Fixed study sample: RS01–RS10. CONTROL remains outside the sample
- Six preregistered layers, 60 object-layer analytical units per eligible
  scheduled timepoint; seven operational platforms / 70 possible checks
  are a separate denominator
- No new prospective observation, eligible release, release tag, DOI, OSF
  change, schedule, causal interpretation or imputed observation is made
- Original source ledgers remain unedited, and identified historical inconsistencies
  stay in their append-only correction notes

**Interpretation:** `EVIDENCE_MAIN_CUSTODY_GAP_RECONCILED` /
`HISTORIC_BYTES_PRESERVED` / `NO_CONTRACT_DRIFT` /
`NO_NEW_PROSPECTIVE_CELLS`
