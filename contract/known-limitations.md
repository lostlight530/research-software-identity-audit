# Known limitations and contract ambiguities

This ledger records known representational or operational limitations without rewriting the frozen study contract.

## KL-001 — Concrete observation offsets are not enumerated in the frozen text export

The preregistration states that observations occur at predefined/scheduled observation points, but the available frozen text export does not enumerate concrete offsets. The OSF interface used at submission did not provide a dedicated field for entering those offsets.

**Handling:** concrete timepoints may be declared separately in `schedule/`, with declaration timestamp and provenance. They must not be represented as literal frozen-registration text unless independently verified.

## KL-002 — Live endpoints are not historical proof

A later public API or web response does not necessarily reconstruct an earlier response.

**Handling:** keep captured historical evidence distinct from present live state.

## KL-003 — Infrastructure clocks and object semantics differ

Repository releases, DOI registration, author-registry ingestion, preservation, and discovery can use different clocks and object types.

**Handling:** calculate latency only when timestamps are directly observed and temporally comparable; compare identity fields only when semantically equivalent.

## KL-004 — External access conditions affect observation

Rate limits, pagination, platform errors, and endpoint availability can prevent complete retrieval.

**Handling:** preserve the attempt and reason; do not drop the cell or infer absence.

## KL-005 — Analytical layers and operational platforms differ

The frozen research contract defines six scholarly-infrastructure layers. Operational evidence collection may use multiple concrete platforms within one layer. In the current mapping, OpenAIRE and OpenAlex are separate platforms under the single preregistered `discovery_graph` layer. Platform-level checks improve observability but do not change the six-layer contract or the 60 object-layer units per scheduled timepoint.

## KL-006 — Supplementary institution-facing surfaces are outside the frozen platform vocabulary

Research Software Directory, SciCrunch/RRID Registry, OSF/Internet Archive relationship surfaces, HAL, and similar institutional or registry surfaces may provide useful identity, curation, preservation, or relationship evidence without belonging to the seven operational platforms currently mapped to the frozen six-layer research contract.

**Handling:** record them as supplementary surfaces unless a future explicit amendment changes the operational study contract. Their presence must not silently change the 10 × 6 = 60 preregistered object-layer denominator or relabel the 10 × 7 = 70 possible platform checks.

## KL-007 — Summary-level imports do not substitute for raw request evidence

A conversation-level or narrative audit summary may reference request logs, response bytes, checksums, scripts, or row-level matrices that are not themselves available to the repository updater.

**Handling:** preserve the summary with explicit provenance, materialize only derivations supported by supplied fields, mark unavailable raw artifacts as evidence gaps, and do not fabricate missing request/response evidence.

## KL-008 — Zenodo version-level and attached-family counters may disagree

In the October 10 independent 32-version public-field extraction, the same RS07 concept family had version-local `version_views=45+33+7=85`, while one month-close version record attached `stats.views=186` and `stats.unique_views=106` versus sibling attached aggregate fields `85/82`. Count **versions by their local fields** under the explicitly declared exploratory method; keep the conflicting family-aggregate fields as observed discrepancies. **Do not** add 101 as extra family traffic, backfill any historical period, or claim a proven internal synchronization mechanism.

The extractor supplied bounded execution windows rather than original HTTP bytes or per-request server times, so this secondary validation is **not** byte-identical evidence. See [2026-10-10 reviewer record](../monitoring/2026-10-10/02-reconciliation/independent-version-verification.md).

## KL-009 — Public institutional listing and RRID index have distinct authority

The public RRID search newly verified `SCR_029105` indexed for the audit-control repository. A dated earlier record still says `pending`; neither date supplies a direct timestamp for the actual indexing transition. RSD public person/project/software records, rseng open PR #498, OSF registration, DataCite DOI relations, RRID indexing and authenticated platform-account access are non-equivalent claims. No institution's scientific endorsement or employment/partnership follows without independent evidence. Details: [institutional ledger](../scholarly/infrastructure-review-2026-10-10.md).

## KL-010 — OpenAlex author profile response conflict

A full-profile query returned `works_count=30` with `updated_date=2026-10-01T12:39:15` while a field-selected query returned `works_count=16` with `updated_date=2026-10-09T12:31:04`. Previous profile and author-Works counts were time-specific and are not rewritten to match one of these incompatible live surfaces. Save exact query shape, source snapshot and retrieval window on any further comparison. Cause is **UNRESOLVED**, not automatically indexing loss or newly generated works.
