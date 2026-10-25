# Derived observations

Derived artifacts are computed from raw observations and must remain traceable to their inputs.

Permitted derivations include direct counts, proportions, directly measurable latency, propagation order, state-transition sequences, aggregation recurrence, and semantically valid cross-layer comparisons.

Do not impute missing evidence or collapse incompatible object types into equivalent states.

No derived prospective results are added by the bootstrap commit.

## Operational JSON lineage preflight (2026-10-25)

JSON artifacts here represent **derived results**, not new raw platform-observation requests. They must **not** be validated as if they had `object_id × infrastructure_layer × platform` fields or counted as additional study units.

The standard-library checker therefore applies a separate *minimal operational* envelope to `*.json` files in this directory:

- `derivation_id` — nonempty identifier for the calculation/output;
- `dataset_phase: prospective` — this directory must not be used to reclassify historical monitoring;
- `derived_at` — timezone-aware ISO-8601 execution/derivation time;
- `derivation_method_ref` — an attributable method/script/document reference;
- `input_observation_refs` — nonempty, non-duplicate repository-relative paths to existing JSON files under `observations/raw/`;
- `derived_at` cannot precede the recorded retrieval time of any referenced source observation.

A result may legitimately be `null` with a bounded `NO_CONCLUSION` interpretation. This envelope checks **lineage and chronology**, not calculation correctness, complete source coverage, reproducibility of off-repository processing, scientific validity, or first-release eligibility. Analyses outside JSON and dated historical exploratory work retain their designated owners and existing contracts.

This is repository-side preflight guidance, **not** an OSF amendment or declaration that prospective collection has begun. No derived data is introduced by this documentation update.
