# Frozen research contract

Canonical research object:

- **Title:** Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures
- **OSF Registration:** https://osf.io/5b329/overview
- **DOI:** https://doi.org/10.17605/OSF.IO/5B329
- **Associated OSF Project:** https://osf.io/wa5v8
- **Registered:** 2026-10-05
- **Registration license:** CC BY 4.0

This file maps the repository runtime to the frozen OSF registration. It does not replace or silently amend the registered object.

## Frozen boundaries

- fixed corpus: 10 research software objects
- fixed scope: 6 scholarly-infrastructure layers
- observation unit: software object × infrastructure layer × observation time point
- 60 object-layer units per scheduled observation point
- prospective, longitudinal, repeated-measures, observational, descriptive design
- no causal interpretation
- no inferential statistical model
- no imputation
- no global composite infrastructure score
- historical observations remain a fixed baseline
- prospective observations begin only after registration and the first eligible new release event
- exploratory/post hoc work remains explicitly labeled
- amendments and deviations are logged rather than folded back into the original contract

## Evidence rule

Missing, unresolved, rate-limited, partial, failed, or unsuccessful retrieval must not be promoted into evidence of absence unless the relevant infrastructure's observable contract explicitly supports that interpretation.

## Schedule representation

The preregistration commits the study to predefined/scheduled observation points. The OSF interface used at submission did not provide a dedicated field for enumerating concrete operational offsets.

Concrete execution times therefore belong in `schedule/` with their own timestamp and provenance. Repository-side operational schedules must not be retrospectively represented as literal preregistered offsets unless independently supported by the frozen registration.

## Authority order

1. Frozen OSF registration controls claims about what was preregistered.
2. Dated amendments control explicit post-registration changes.
3. Dated operational specifications control implementation details that do not rewrite the substantive contract.
4. Exploratory work remains labeled exploratory/post hoc.

## Clause-level Overview crosswalk (2026-10-08)

The researcher's supplied OSF Overview was compared against the live repository without rewriting the frozen registration or historical captures. The [clause-level crosswalk](osf-overview-crosswalk-2026-10-08.md) maps RQ1–RQ5, the 12 measured-variable categories, six descriptive derived analyses, prior foreknowledge, no imputation/exclusions, prospective eligibility, stopping and the experimental/exploratory boundary.

In that supplied Overview, `Other planned analysis` is marked **Updated**. Without an independently preserved OSF version history or edit timestamp, the wording must **not** be asserted to have belonged to the originally frozen registration. Existing benchmarks remain exploratory/post hoc regardless of that unresolved revision history.

This addition is explanatory, **not** an amendment or declaration that a prospective observation window has started.

## Dated OSF Schema Response version reconciliation (2026-10-30)

**Subsequent evidence update, not a new or amended frozen contract:** the original October 8 Overview crosswalk correctly stated that it lacked direct OSF revision evidence *at that time*. The [October 30 version-by-version public API reconciliation](../monitoring/2026-10-30/01-osf-schema-response-version-reconciliation/README.md) now identifies the [original Schema Response](https://api.osf.io/v2/schema_responses/6ac3ae5e6da32e3d0576ed72/) and a [later approved revision](https://api.osf.io/v2/schema_responses/6ac4c12fed97b8b77ce88a9c/). Across **29** `revision_responses` keys, the extracted representations have **one changed value, `344-83` (Other planned analysis)**. Primary questions, fixed corpus/layers, counting, measured/derived variables and primary analysis wording did **not** differ in that field-level comparison.

The original `344-83` generically permitted clearly labeled exploratory/post hoc analyses; the October 6 revision made family benchmarking, engagement-metric sensitivity and tie-aware rank/percentile examples explicit. These added examples were **not present in the original version** and must not be represented as initially preregistered primary analyses. The later revision's justification is retained separately from the observed text diff. Exact revision timestamps, source URLs, field values and third-party extractor limits are in the linked record.

The original October 8 crosswalk and all historical monitoring files remain as-of records rather than silently rewritten. The schedule still has no declared concrete offsets, and neither this new provenance finding nor the OSF revision initiates a prospective observation wave.
