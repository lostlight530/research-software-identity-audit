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

- [2026-10-08 / 01-morning-recheck](2026-10-08/01-morning-recheck/) �� 17 original public API responses, timestamp and hash manifest, original local offline verification outcome

The original archive member names and source-response bytes are immutable through the path migration. See [monitoring naming rules](../monitoring/NAMING.md).

- [2026-10-09 / 01-facility-recheck](2026-10-09/01-facility-recheck/) �� Timestamped original API responses and counter reconciliation

- [2026-10-10 / 01-zenodo-surge-recheck](2026-10-10/01-zenodo-surge-recheck/capture-manifest.json) �� 11 archived original concept-recID responses from the source collector, **not** the later independent 32-version extraction

The independently extracted 32-version table is retained under [monitoring/2026-10-10/02-reconciliation](../monitoring/2026-10-10/02-reconciliation/version-counters-independent.csv) as **derived public fields** with bounded fetch windows, **not** original byte-level HTTP evidence. The October 10 institutional public-status investigation is separately recorded in [scholarly](../scholarly/infrastructure-review-2026-10-10.md).

## October 14 retained diagnostics and user pages

- [2026-10-14 / 03-midnight-facility-recheck](2026-10-14/03-midnight-facility-recheck/README.md) �� 00:04�C00:16 independent API capture, incomplete Zenodo counters retained as null
- [2026-10-14 / 04-morning-facility-recheck](2026-10-14/04-morning-facility-recheck/README.md) �� 08:03�C08:07 independent API capture; 33 version records and 40 DOI routes
- [2026-10-14 / 05-noon-user-pages](2026-10-14/05-noon-user-pages/README.md) �� user-labelled noon Zenodo unique counters and WorkflowHub Dashboard; exact time/Period unknown

## October 14 evening new-release propagation

[Evening diagnostics and new-version evidence](../monitoring/2026-10-14/06-evening-facility-recheck/README.md) preserve ten new public releases, 72 findable DOIs, 15 ORCID groups / 85 sources and 43 enumerated versions; user pages and independent captures remain separate

## October 15 morning diagnostic recheck

[Full morning record](../monitoring/2026-10-15/01-morning-facility-recheck/README.md) retains 27 author-query Works, 84 ORCID source summaries, 72 DOI records and source-specific counter reconciliation; earlier captures remain dated

- [October 18 independent research field extracts](2026-10-18/03-independent-research-verification/README.md) �� minimized public representation with explicit local-only raw bytes and source archive digest verification

- [October 20 research evidence](2026-10-20/01-independent-research-recheck/README.md): minimized public fields, per-attempt digests and retained failure/retry states

## October 25 later independent institutional recheck

- [2026-10-25 / 02-independent-institutional-recheck](2026-10-25/02-independent-institutional-recheck/README.md) �� 162 timestamped attempts; twelve page/API unique pairs match, 76 DOI records, structured ORCID 17/89, SWH four current release chains, source-separated WorkflowHub counts; diagnostic only, zero prospective cells
