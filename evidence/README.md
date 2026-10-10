# Evidence

This directory holds or indexes timestamped evidence supporting observation records.

Evidence and interpretation are separate layers.

A live endpoint observed later is not automatically proof of an earlier historical state.

Each retained evidence object should be linkable to:

- source system;
- source object or query surface;
- retrieval timestamp;
- related observation ID;
- access or response condition;
- provenance/capture method.

Sensitive, private, credential-bearing, or redistribution-restricted material must not be committed merely for completeness.

## Retained packages

- [2026-10-08 / 01-morning-recheck](2026-10-08/01-morning-recheck/) — 17 original public API responses, timestamp and hash manifest, original local offline verification outcome

The original archive member names and source-response bytes are immutable through the path migration. See [monitoring naming rules](../monitoring/NAMING.md).

- [2026-10-09 / 01-facility-recheck](2026-10-09/01-facility-recheck/) — Timestamped original API responses and counter reconciliation

- [2026-10-10 / 01-zenodo-surge-recheck](2026-10-10/01-zenodo-surge-recheck/capture-manifest.json) — 11 archived original concept-recID responses from the source collector, **not** the later independent 32-version extraction

The independently extracted 32-version table is retained under [monitoring/2026-10-10/02-reconciliation](../monitoring/2026-10-10/02-reconciliation/version-counters-independent.csv) as **derived public fields** with bounded fetch windows, **not** original byte-level HTTP evidence. The October 10 institutional public-status investigation is separately recorded in [scholarly](../scholarly/infrastructure-review-2026-10-10.md).
