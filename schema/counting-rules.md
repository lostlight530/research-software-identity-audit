# Counting rules

## Preregistered denominator

At each declared observation point:

- 10 fixed software objects
- × 6 fixed infrastructure layers
- = **60 planned object-layer units**

All planned attempted object-layer cells remain in the denominator where applicable.

## Operational platform granularity

Evidence may be collected from seven currently defined concrete platforms:

- GitHub
- Zenodo
- DataCite
- ORCID
- Software Heritage
- OpenAIRE
- OpenAlex

These are operational platforms, not seven newly preregistered infrastructure layers.

OpenAIRE and OpenAlex both map to the preregistered `discovery_graph` layer because they expose distinct discovery/aggregation representations inside the same analytical layer.

Therefore:

- `10 × 7 = 70` may describe a complete set of object × platform checks;
- `10 × 6 = 60` remains the preregistered object × infrastructure-layer denominator.

A platform-check count must never be relabeled as a preregistered object-layer count.

## Retained outcomes

Do not remove an observation because it is not found, rate limited, unresolved, partially verified, failed, or otherwise incomplete.

## No imputation

Do not synthesize latency, propagation order, presence, identity consistency, or completeness when required evidence is missing or semantically incomparable.

## Identity counting

Count only records that map to a predefined software family or directly related scholarly identifier.

Do not count mirrors, duplicate representations, unrelated records, semantically non-equivalent objects, the OSF registration, or this research-control repository as additional sample objects.

## Baseline versus prospective

Historical/initial baseline records are not prospective observations.

A reconciliation performed after a baseline cutoff may verify historical timestamps or reconstruct states when evidence supports doing so, but the retrieval time and reconstruction status must remain explicit.

## Latency

Compute propagation latency only when both release timestamp and first qualifying downstream observation timestamp are directly observed and temporally comparable.

## Absence

A not-found, unresolved, rate-limited, partial, failed, or unqueried observation is not evidence of global absence unless the relevant observable contract explicitly supports that inference.
