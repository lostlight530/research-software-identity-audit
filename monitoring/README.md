# Monitoring

This directory stores useful measurements that occur outside the eligible
prospective dataset.

A monitoring record can be methodologically valuable without being promoted to a
scheduled prospective observation.

Use this area for:

- pre-eligibility propagation checks;
- infrastructure self-observation;
- post-baseline state checks before the first eligible fixed-corpus release;
- diagnostic captures whose timing does not satisfy the operational prospective schedule.

Monitoring records must preserve true retrieval time and must not be relabeled
later as preregistered prospective observations.


Post-release reconciliation records may also be stored here when they observe
the research-control repository or scholarly infrastructure before an eligible
fixed-corpus release begins the prospective dataset.

## Records by observation day

- [2026-10-06 / 01-wave-01](2026-10-06/01-wave-01/) — first pre-eligibility monitoring, not a preregistered wave
- [2026-10-06 / 02-openaire-link-attempt](2026-10-06/02-openaire-link-attempt/) — manual link attempt with bounded outcome
- [2026-10-06 / 03-reconciliation](2026-10-06/03-reconciliation/) — later reconciliation, original timestamps retained
- [2026-10-07 / 01-facility-audit](2026-10-07/01-facility-audit/) — supplied cross-platform audit and mapping reconciliation
- [2026-10-08 / 01-morning-recheck](2026-10-08/01-morning-recheck/) — morning monitoring plus separately imported retained evidence

For path rules and the complete old-to-new inventory, see [naming and migration](NAMING.md) and [path mapping](path-migration-2026-10-08.csv).

The date is the record's source-observation date, not necessarily its retrieval or evidence-import date. Ordinals order packages within a date and are **not** prospective-wave identifiers.

- [2026-10-09 / 01-facility-recheck](2026-10-09/01-facility-recheck/) — Independent facility and counter recheck

## October 10 diagnostic and interpretation records

- [2026-10-10 / 01-zenodo-surge-recheck](2026-10-10/01-zenodo-surge-recheck/) — source collector's original point-in-time Zenodo counters and the separately attributed corrective review; this is **not** an eligible prospective observation
- [2026-10-10 / 02-reconciliation](2026-10-10/02-reconciliation/independent-version-verification.md) — independently reviewed 11 concept families / 32 versions, the [32-row extract](2026-10-10/02-reconciliation/version-counters-independent.csv), and unresolved RS07 aggregate-field disagreement

The 01 original report and the 02 earlier `interpretation.md` have distinct author/provenance identity. The independent reviewer **does not adopt** the earlier suggestion of an identified Zenodo aggregation mechanism; it is a working hypothesis. Across October 9–10 the retained prior capture does not provide a matching 32-version enumeration, so per-version historical interval increments remain **NOT_DERIVABLE**. For the bounded version-counting procedure see [counting rules](../schema/counting-rules.md#supplementary-zenodo-version-family-reconciliation-2026-10-10).
