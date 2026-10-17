# Field-boundary correction note — 2026-10-17

This note is a later reconciliation of the flattened Zenodo listing text. It does not rewrite the 2026-10-16 observation or alter any source artifact.

## Correct parse

The user-supplied text placed adjacent values together without whitespace, e.g. `1875`. The correct field-boundary parse is **187 Views** and **5 Downloads**. Likewise, `1682` is **168 Views** and **2 Downloads**, and `1671` is **167 Views** and **1 Download**. These are two separately labelled fields, not one larger view count.

Zenodo's official page semantics state that landing pages primarily display unique views/downloads aggregated across all versions by default. Therefore, the current page display is recorded as page-visible unique counters. It is not silently rewritten as API `stats.views` total counters.

## Effect on prior record

The 2026-10-16 record's parsed API fields remain intact. Its example `1815` already represents two adjacent values, **181 unique views + 5 unique downloads**, not a numeric counter of 1,815. This note corrects the interpretation of the flattened current-page token and documents that page-visible fields must be parsed by label. It does not claim the earlier API observation was invalid, nor that the current UI/API difference identifies an event time.

No historic data, baseline, contract, or prospective dataset is changed by this correction.
