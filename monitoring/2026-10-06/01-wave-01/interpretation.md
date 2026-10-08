# Wave 1 interpretation

## Status

This record is retained as **pre-eligibility monitoring**, not as a prospective
study timepoint.

The frozen contract states that the prospective dataset begins only after the
first eligible post-registration release event in the fixed ten-object corpus.
No such event is recorded before the 2026-10-06 09:15 Asia/Shanghai capture.

## Supported findings

- Zenodo family views increased from 575 at the cutoff ledger to 616 at T1:
  +41, or approximately 7.13%.
- Downloads remained 7. This supports only "no observed download-count change";
  it does not support a claim about malicious or non-malicious traffic.
- Package bytes remained 29,261,316.
- The largest view increases were agentic-frontier-observatory (+13) and
  china-agentic-observatory (+11).
- Fixed-corpus OpenAlex Work count remained 40.
- The research-control repository remains strictly outside the fixed sample.
- The supplied timestamps support an 18m36s release-to-ORCID-via-OpenAIRE interval
  for the research-control repository.

## Non-comparable DataCite count

The raw 41 -> 43 DataCite figure is preserved but not interpreted as a temporal
registration delta.

The research-control repository's two DOI records were registered before the T0
cutoff, so a T0 count of 41 and T1 count of 43 reflect a scope/discovery
difference unless a narrower counting query is specified.

## Software Heritage state transition

The stable count of ten directory hashes is not "no change" in verification
state.

The baseline machine record was explicitly `NOT_VERIFIED`. The Wave 1 source
reports all ten as fully verified. This is therefore represented as a
verification-state transition while retaining the earlier baseline state.

## Propagation order

The research-control repository sample supports:

```text
GitHub <= Zenodo <= DataCite <= OpenAIRE-sourced ORCID
```

This record does not extend that chain to OpenAlex without a T1 OpenAlex
appearance record for the beta DOI.
