# VSHWK capture custody gaps

This directory records execution/custody failures that cannot be represented as a validated cycle package. It is operational evidence, not an additional analytical unit, endpoint retrieval state, study case, protocol amendment, or validated cycle.

## Procedure

1. Preserve the original precollection intent, error, already reachable source receipts and their exact blob/commit references. Distinguish verified attempted, verified not attempted, and unknown; a missing receipt alone proves neither an attempt nor its absence.
2. Record the actual failure/review clock, failing execution layer, missing artifacts, retained evidence count, and bounded disposition. Never interpret a collector failure as a provider HTTP response or global record absence.
3. Place the incomplete record under a uniquely dated attempt directory here. If moved from a staging cycle directory, preserve original blobs and locators; do not overwrite prior records. Retain an index entry and a pointer to the original commit where available.
4. Do not bypass the strict cycle validator, synthesize endpoint rows, or promote a partial package to a validated cycle. If exact originals are later recovered, retain their original provenance and append a reconciliation; if a new review is warranted, create a distinct intent before collection and preserve new clocks.
5. In future acquisition, use bounded batches and verify receipt persistence before starting the next batch, as described in the [cycle record template](../cycles/record-template.md).

## Index

| Record | Status | Attempt accounting |
| --- | --- | --- |
| [2026-11-26 Pacific attempt 01](2026-11-26-pst-01/README.md) | BLOCKED_CAPTURE_ORCHESTRATION_LIMIT | Unknown; zero reachable endpoint ledgers at review, not zero attempts |

The [November 24 legacy custody gap](../cycles/cycle-2026-11-24-pst-01/custody-gap.json) remains at its existing path, with its historical validation rules unchanged. The [independent November 26 cycle 02](../cycles/cycle-2026-11-26-pst-02/README.md) does not replace either gap. No existing history is relocated by this procedure.
