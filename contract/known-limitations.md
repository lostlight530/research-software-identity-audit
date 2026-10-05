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
