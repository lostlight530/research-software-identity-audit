# Correction reconciliation 01 — fixed-corpus identity mapping

**Recorded:** 2026-10-20  
**Scope:** Derived records in PR #50 only  
**Original submitted branch head:** `bfc42199ff3d23014c88d7c1def451e834c535ed`  
**Frozen manifest used:** `corpus/object-manifest.csv` at base `2b112639a346bb6a3f73c5afa03d939a75c2cf28`

## Finding

The original derived extract and family-statistics CSV retained internally coherent repository-specific DOI, version, and counter fields, but four `object_id` labels did not match the frozen manifest. This was a derived join/labeling defect, not a change in the fixed corpus or in platform responses.

| Canonical object ID | Canonical repository | Original submitted label |
|---|---|---|
| RS06 | `auto-doc-engine` | RS09 |
| RS07 | `epistemic-pipeline` | RS10 |
| RS09 | `china-agentic-observatory` | RS06 |
| RS10 | `agentic-frontier-observatory` | RS07 |

The original submitted versions remain available in Git history at [the pre-correction field extract](https://github.com/lostlight530/research-software-identity-audit/blob/bfc42199ff3d23014c88d7c1def451e834c535ed/evidence/2026-10-20/01-independent-research-recheck/field-extracts.json) and [the pre-correction statistics CSV](https://github.com/lostlight530/research-software-identity-audit/blob/bfc42199ff3d23014c88d7c1def451e834c535ed/monitoring/2026-10-20/01-independent-research-recheck/zenodo-family-statistics.csv).

## Reconciliation applied

1. Joined each derived record's repository slug to `corpus/object-manifest.csv` (`software_family`), then assigned the canonical object ID.
2. Restored `RS01–RS10` order in `field-extracts.json` and `zenodo-family-statistics.csv`.
3. Added offline checker assertions for the canonical `object_id → repository` mapping in both files, plus a deliberate RS06/RS09 label-transposition negative case.
4. Added the October 20 checker as an advisory step in the existing `validate` workflow. No new workflow job, dependency, external service, or schema was introduced.
5. Updated artifact byte counts and SHA-256 values for the changed derived files and this reconciliation note.

## Preserved unchanged

- `capture-manifest.json`, all 147 source-attempt entries, source URLs, status codes, retrieval intervals, response byte counts and SHA-256 values
- All record IDs, version DOIs, concept DOIs, repository-specific response fields and numeric counters
- `record.json` retrieval window, historical `git_head`, aggregate sums and research classification
- Frozen manifest, OSF contract, baseline, schedule, schema and prospective dataset

No external endpoint was queried during this correction. This is a derived-record reconciliation against the frozen manifest, not a new observation. Aggregate totals remain unchanged; the correction fixes the attribution of four object-level rows.

## Verification boundary

The original `offline-verification.json` in the submitted commit reported 268 checks / 0 failures **before** the identity invariant existed. It must not be read as validation of the corrected package. That prior file is marked superseded in the corrected tree; the corrected checker is now part of the existing advisory GitHub Actions workflow. Its result must be read from the run attached to the corrected commit. No claim is made that a local Python execution occurred in this session.
