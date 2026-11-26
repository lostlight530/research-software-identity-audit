# Object-ID mapping reconciliation

## Status

- recorded: 2026-10-07
- fixed corpus changed: no
- source report changed: no
- derived join keys corrected: yes

## Conflict observed

The supplied 2026-10-07 independent-audit table used this mapping for its final five rows:

```text
RS06 china-agentic-observatory
RS07 agentic-frontier-observatory
RS08 sci-render-kit
RS09 auto-doc-engine
RS10 epistemic-pipeline
```

Fresh repository state already records that ordering as the prior incorrect display-order join.

The canonical manifest is:

```text
RS01 welcome-to-github
RS02 zero-entropy-lab
RS03 Axiom-0
RS04 reflective-continuum
RS05 agent-foundations
RS06 auto-doc-engine
RS07 epistemic-pipeline
RS08 sci-render-kit
RS09 china-agentic-observatory
RS10 agentic-frontier-observatory
```

## Handling

The supplied source statement is preserved as source history.

All machine-readable derived files in this package join by repository identity to `corpus/object-manifest.csv`, not by source display order.

No metric value, DOI, OpenAlex Work ID, SWHID, timestamp, repository name, or aggregate total is changed by this reconciliation. Only the RS identifier join key is normalized.

## Why this matters

Object IDs are analytical keys. A display-order mismatch can silently move correct measurements to the wrong software object while leaving portfolio totals unchanged.

For this repository:

```text
aggregate total agreement
!=
object-level identity correctness
```

Future imports must join on canonical repository identity or another explicit immutable key and then resolve the RS ID from the manifest.
