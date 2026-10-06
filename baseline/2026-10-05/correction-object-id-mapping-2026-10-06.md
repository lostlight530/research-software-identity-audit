# Correction — baseline object-ID mapping

- **Recorded:** 2026-10-06
- **Scope:** machine-derived baseline DOI and Zenodo-statistics mappings
- **Raw source preserved:** yes
- **Fixed corpus changed:** no
- **Aggregate totals changed:** no

## Problem

The Codex-generated raw reconciliation source record used a repository ordering in
which the last five software families did not match the canonical fixed
`corpus/object-manifest.csv` object IDs.

The incorrect derived mapping was propagated into the first machine summaries.

## Canonical mapping

The fixed corpus manifest is authoritative:

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

## Prior incorrect mapping

The raw reconciliation source and first derived tables represented:

```text
RS06 china-agentic-observatory
RS07 agentic-frontier-observatory
RS08 sci-render-kit
RS09 auto-doc-engine
RS10 epistemic-pipeline
```

## Correction

`doi-map.csv` and `zenodo-statistics.yaml` are corrected to the canonical
manifest IDs.

The raw Codex record remains unchanged as the historical source record.

The correction does not alter repository names, DOI values, Zenodo counters,
file digests, timestamps, or aggregate totals. It only repairs the object-ID
join key in derived machine-readable artifacts.

Future records must join on `corpus/object-manifest.csv` rather than infer RS
IDs from display order.
