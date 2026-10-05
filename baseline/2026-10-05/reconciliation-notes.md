# Baseline reconciliation notes

## Source provenance

The source record in this package was produced by Codex during the 2026-10-06 reconciliation run and is preserved as:

`raw-reconciliation-record-2026-10-06.md`

The collection time was approximately `2026-10-06T00:33:54+08:00`.

The record reconciles events and states attributable to 2026-10-05 or earlier where support exists from public APIs, frozen evidence, or user-supplied public pages.

This note does not replace the raw record. It clarifies how the repository interprets it under the frozen OSF contract.

## Capture time versus release time

Two clocks must remain distinct:

- statistics capture: **2026-10-06 00:33 Asia/Shanghai**
- latest ten releases: **2026-10-04 21:00–21:01 Asia/Shanghai**

Therefore Zenodo counters observed during the reconciliation are 2026-10-06 observations. They must not be represented as counters that existed at release time on 2026-10-04.

At capture, the fixed ten Zenodo software families totaled:

- family views: 581
- family unique views: 556
- family downloads: 7
- family unique downloads: 6
- latest-version views: 15
- latest-version unique views: 13
- latest-version downloads: 0

## Six layers versus seven platforms

The raw reconciliation separates seven concrete platforms:

GitHub, Zenodo, DataCite, ORCID, Software Heritage, OpenAIRE, and OpenAlex.

This platform-level distinction is retained because OpenAIRE and OpenAlex expose different records, clocks, processing states, and failure behavior.

It does **not** amend the frozen six-layer preregistered design.

Operational mapping is defined in `schema/platforms.yaml`. Both OpenAIRE and OpenAlex map to the preregistered `discovery_graph` layer.

Accordingly:

- **70** = possible object × platform checks when all seven operational platforms are queried;
- **60** = preregistered object × infrastructure-layer units per scheduled timepoint.

The 70 platform checks are evidence-collection granularity, not a replacement research denominator.

## Historical reconstruction

A live endpoint queried after the baseline cutoff may support a historical claim when the endpoint exposes an immutable or semantically reliable historical timestamp.

It does not automatically prove that the complete live representation existed at that earlier time.

Where contemporaneous evidence is unavailable, the record must remain explicitly retrospective/reconstructed.

## Software Heritage boundary

The source record correctly preserves October content identity as `NOT_VERIFIED`.

No later summary may turn the partial/429/unqueried state into 10/10 complete verification without new evidence and an explicit correction record.
