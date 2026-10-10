# Analysis

Primary preregistered analysis is descriptive.

Allowed primary operations include:

- direct counts;
- proportions;
- timestamp differences where directly measurable;
- propagation order;
- state-transition sequences;
- cross-layer consistency/divergence where fields are semantically comparable;
- recurrence of predefined aggregation patterns;
- failure/partial-state frequencies.

Not preregistered:

- causal modeling;
- ANOVA;
- regression;
- SEM;
- null-hypothesis significance testing;
- p-value thresholds;
- Bayesian model comparison;
- imputation;
- a single global infrastructure-quality score.

Exploratory work is allowed but must remain explicitly labeled.

## Exploratory Zenodo benchmark

The Zenodo same-publication-date benchmark is an exploratory/post hoc contextual analysis, not a preregistered primary analysis and not a prospective dataset observation.

Its default ranking metric remains `stats.views`. Manual workflow runs may select `views`, `unique_views`, `downloads`, or `unique_downloads` as bounded sensitivity checks over the same cohort construction. Changing the exploratory metric does not change the fixed RS01–RS10 corpus, the six preregistered infrastructure layers, the 60 object-layer units per scheduled time point, or any prospective observation rule.

The primary cohort matches Zenodo software concept families at `publication_date` calendar-date resolution. It must not be described as exact sub-day age matching, and platform engagement counters must not be interpreted as software quality, scientific impact, adoption, or citation impact.

## RQ and observation-time interpretation (OSF Overview crosswalk, 2026-10-08)

The supplied OSF Overview maps to descriptive RQ1 propagation/state chronology, RQ2 semantically comparable identity consistency, RQ3 bounded release-to-first-observed latency, RQ4 recurrence of predefined author-registry aggregation structures, and RQ5 incomplete/failure/correction-state frequency. See [clause-level mapping](../contract/osf-overview-crosswalk-2026-10-08.md).

`first_observed_timestamp` denotes first **directly observed qualifying evidence**; do not silently infer the actual platform's earlier internal ingestion or transition time from a sampled API retrieval. Order ties remain ties. Unsupported comparisons remain unresolved; all planned attempted-cell denominators retain missing/failed/partial outcomes where applicable.

The supplied `Other planned analysis — Updated` wording does not establish initial-registration revision history. Benchmark, sensitivity and tie-aware rank analyses stay **exploratory/post hoc**, with no upgrade to preregistered primary findings.

## October 10 diagnostic version counts (exploratory)

The [Zenodo version-level reconciliation](../monitoring/2026-10-10/02-reconciliation/independent-version-verification.md) verifies 11 concept families and 32 enumerated version records, with RS01–RS10 (30 versions) kept separate from the control repository (2 versions). In its own bounded retrieval window, the independent version-sum method yielded **1,813** views / **7** downloads for the fixed ten and **51** views / **0** downloads for the separately reported control.

A single RS07 version record exposes a conflicting attached family aggregate (`186`) against the derived version-view sum (`85`). This is an unresolved observable field disagreement, **not** a new software object or proven synchronization mechanism. Historical version-localized delta inference is blocked without matched earlier version-level snapshots. See the [supplementary counting rules](../schema/counting-rules.md#supplementary-zenodo-version-family-reconciliation-2026-10-10).

These counter comparisons remain **diagnostic/exploratory**; they do not belong to the preregistered prospective 60-cell observation frame and do not identify visitors, causal propagation, adoption, or code usage.
