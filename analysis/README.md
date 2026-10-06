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
