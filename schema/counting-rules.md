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

## Supplementary Zenodo version-family reconciliation (2026-10-10)

**Scope:** exploratory/diagnostic engagement-counter analysis of the existing fixed ten research-software objects; the **control repository is separately reported**. This clarification is **not an amendment to the frozen prospective analysis** and does not transform 11 displayed repositories into 11 preregistered sample objects.

1. Enumerate all versions inside each canonical Zenodo concept using a bounded `GET /api/records?q=conceptrecid:<id>&all_versions=true` query and cross-check the record IDs using `GET /api/records/<version-record-id>/versions`. Record actual query windows and API success/failure. An `allversions` alias was observed to work for RS07 but `all_versions` is the preferred explicit query spelling for the procedure.
2. For every enumerated **version record**, retain `id`, `conceptrecid`, `stats.version_views`, `stats.version_unique_views`, `stats.version_downloads`, plus its **attached** `stats.views` / `stats.unique_views`. Distinguish the original source collector, independent public-field extraction, bytewise original archive, and later reconciliation; a cache-busting query string does not itself prove fresh uncached transport.
3. Within a fully enumerated family, calculate `derived_family_views = sum(version_views)` and `derived_family_downloads = sum(version_downloads)`. Retain version-level `version_unique_views` separately; **do not sum version-level unique views as unique persons or a deduplicated family audience**.
4. Compare **each** version record's attached `stats.views` to that family's calculated version-view sum. Record discrepancies as `FAMILY_AGGREGATE_MISMATCH` with version ID, observed values, fetch-window provenance and delta; **never add** those attached aggregate fields again into family totals. Aggregate `stats.unique_views` disagreements across same-concept records may be reported as raw field conflicts but must not be replaced with sums of `version_unique_views`.
5. Sum derived family totals over **exactly RS01–RS10**, and report the research-control family's totals and optional combined descriptive total separately. Form interval differences only between independently **comparable** endpoints at matched family or version granularity. Missing earlier per-version snapshots are `NOT_DERIVABLE`, not backfilled using later family totals.

**Observed October 10 case:** one version record, RS07 month-close `23068494`, returned attached `stats.views=186`, while three version views were `45+33+7=85`, yielding an **attached-family field difference of +101**. Its `stats.unique_views=106` also disagreed with the other family records' `82`. No extra concept was found and the reason for this split is **UNRESOLVED**. It is not proof of source referrers, human browsing, platform ingestion time, or a specific aggregation/synchronization process. Reference: [independent 32-version review](../monitoring/2026-10-10/02-reconciliation/independent-version-verification.md).

**Reproducibility limit:** the independent 32-version table is a derived public JSON-field extract with outer tool batch windows. It does not by itself preserve unmodified raw HTTP response bytes, SHA-256 or per-request server timestamps; the separate source collector's 11 original responses cannot substitute for those 32 raw responses.
