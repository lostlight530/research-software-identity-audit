# RSIA offline preflight handoff — 2026-11-20

Status: `LOCAL_VALIDATION_PASSED / FORMAL_COLLECTION_NOT_READY`.

This note transfers an offline readiness check, not a new audit, observation
batch, schedule declaration, or OSF amendment. November 23 is the planned start
of planning, not an approved observation timepoint or a substitute for the
registered first eligible release event.

## What ran

Base: [main d9e1a47301112201e8bee000069f717f157d52a6](https://github.com/lostlight530/research-software-identity-audit/tree/d9e1a47301112201e8bee000069f717f157d52a6).
On Python 3.12.14, 96 unit tests and the advisory and strict contract checks
passed. The all-manifest replay checked 28 manifests and 396 artifact rows with
zero failures. The bounded retained-evidence replay passed 3,231 checks. The
record-path and repository-text checks also passed. These results verify local
code and retained files, not past provider responses or scientific validity.

Reproduce from a checkout with Python 3.12 and no live collector:

```bash
python -B -m unittest discover -s tests -v
python -B tools/check.py --mode strict
python -B tools/check_public_artifact_manifest.py --all
python -B tools/check_retained_all.py
python -B tools/rehearse_prospective_preflight.py
```

The rehearsal creates and then removes a private temporary fixture tree. All
timestamps are fictional; no provider is contacted. It checks 70 simulated
platform attempts mapping to 60 unique object–layer cells, with separate
rate-limited, unresolved and partial results. It rejects five negative cases:
no schedule, missing platform attempt, duplicate attempt, late declaration,
and labeling a failed attempt fully verified. A derived record with no
conclusion remains legal. The duplicate/missing checks are rehearsal-level
assertions, not a new production ingestion gate. The temporary entries are
not retained as evidence or copied to the real `observations/` directory.

## Decisions required before formal collection

1. Confirm the release anchor against the [frozen contract](../contract/preregistration.md)
   and [OSF version authority mapping](../contract/osf-registration-version-governance-2026-11-03.md).
   The [October 13 gate](../monitoring/2026-10-13/02-fixed-corpus-release-gate/README.md)
   found no later published GitHub Release within its checked scope; tag-list
   access was not verified. The [October 14 reconstruction and diagnostic](../monitoring/2026-10-14/06-evening-facility-recheck/README.md)
   records the first observed eligible public release cohort in that retained
   scope. Do not relabel the later diagnostic as T0, or assume November 23
   supersedes the earlier trigger. Record missed or unresolved intervals as such.
2. Decide the forward operational interpretation, including declared timepoints,
   tolerances, and the final attempted follow-up and stop rule, before interpreting
   governed observations. The [schedule record](../schedule/README.md) currently
   has no concrete offsets. Do not backdate a declaration or silently replace the
   registered anchor. Keep any substantive change or deviation separate from the
   frozen record.
3. Retain per-attempt evidence and reconcile the final 60 object–layer cells
   separately from the 70 possible object–platform checks. Do not drop failures,
   impute missing results, or count raw and derived files twice.

No prospective cells, active schedule, CI workflow change, or external record
mutation is included in this handoff.
