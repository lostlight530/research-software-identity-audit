# 2026-11-19 evidence-path correction history

## Issue

The initial 2026-11-19 evidence run `44352245857` was first committed to:

- evidence/2026-11-19/01-complete-institutional-recheck/
- monitoring/2026-11-19/01-complete-institutional-recheck/

A subsequent run `44355868835` reused the same `01` path instead of creating a new attempt path. This changed the current tree contents of `01`; the earlier source files were not deleted from Git history, but the path reuse violated the intended append-only evidence-path discipline.

## Preserved identities

- Earlier capture: run `44352245857`, source ledger SHA-256 recorded in its original provenance at commit `50a9649138d34ce32bc1c6692f17694f45b99cae`.
- Reused-path capture: run `44355868835`, source ledger SHA-256 `631a5812c44976afff78b5e0f40db05850a259c6b6d3176677fbfa1f537505f6`, committed at `517c33fe349e9194d05b6fbf095c8988f99b1d9a`.
- New append-only capture: run `44356891292`, source ledger SHA-256 `3533de5328d954d1650e01dccfedf084b84a6e9bcdc559973f1ed9e97794877d`, stored under `02-complete-institutional-recheck/`.

The first capture remains recoverable from commit `50a9649138d34ce32bc1c6692f17694f45b99cae`; no Git history rewrite was performed.

## Corrective action

The temporary workflow now:

1. writes to a distinct `02` path,
2. refuses to overwrite an existing evidence path,
3. uploads the source/derived artifact before the repository push,
4. rebases against the current evidence branch before pushing,
5. no longer appends to the shared monitoring index during concurrent runs.

The final `02` run completed successfully and contains 458 source attempts. The duplicate run `44355884574` failed only while rebasing the shared monitoring index; its source summary is in its immutable Actions log, but it did not write a second evidence package.

## Classification

`CORRECTION_HISTORY_RECORDED` / `NO_HISTORICAL_GIT_REWRITE` / `APPEND_ONLY_PATH_GUARD_ADDED`.
