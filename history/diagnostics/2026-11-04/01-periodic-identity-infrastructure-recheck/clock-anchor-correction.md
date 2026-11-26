# November 4 source comparison clock-anchor correction

**Class:** explicit non-destructive derived-record correction; not new source retrieval, reclassification of a scheduled prospective wave, OSF contract amendment, new Release/DOI or historical provider-data overwrite

## Original source and discovered error

PR [#88](https://github.com/lostlight530/research-software-identity-audit/pull/88), merged into `main` at `2425a79518f9dbbed5f12564e2122c573babc659`, published a November 4 selected-field diagnostic. Its relative GitHub comparison used the SHA table in [November 3 earlier read](../../2026-11-03/01-bounded-identity-infrastructure-recheck/github-main-deltas.csv), whose own README explicitly says **last 11-core main-read completed client UTC 2026-11-03T03:09:19.860Z** (Beijing 2026-11-03 11:09:19.860). This is a **client-side batch completion envelope**, not each origin request timestamp and not the end of November 3.

The PR #88 derived CSV labeled the source column `nov3_end_main_sha` and delta `ahead_since_nov3_end`, and `record.json` called the derived field `fixed_main_changed_repos_from_nov3_end`. The prose additionally described CONTROL `b00f4fa` as the November 3 **end-of-day** main. Neither end-of-day anchor was established by the retained evidence. CONTROL `b00f4fa` is directly associated with **2026-11-03T03:40:45Z** commit time; that is a commit clock, not a final day snapshot.

## Corrected interpretation

- `nov3_end_main_sha` → `nov3_source_read_main_sha`
- `ahead_since_nov3_end` → `ahead_since_nov3_source_read`
- JSON `fixed_main_changed_repos_from_nov3_end` → `fixed_main_changed_repos_since_nov3_source_read`, with explicit `source_comparison_baseline.main_read_completion_client_utc`
- CONTROL `b00f4fa` is the prior independently verified November 3 commit, **not** an attested Beijing day-end state
- Result is still **two sample repositories changed, three main-reachable commits** since that November 3 source-read envelope, namely RS01 two and RS02 one. RS01 changes have different commit dates: `855c659cec` at 2026-11-03T03:21:04Z and `19ebd2b219` at 2026-11-04T01:57:13Z; RS02 `b6e7b2a0a5` at 2026-11-04T01:45:55Z. They are not all new commits made on November 4

## Evidence and immutable history

- Historical comparator: [November 3 README](../../2026-11-03/01-bounded-identity-infrastructure-recheck/README.md) and [11-head delta CSV](../../2026-11-03/01-bounded-identity-infrastructure-recheck/github-main-deltas.csv)
- Original November 4 machine record at merge #88: Git blob `3634d802a0e0b8a3b72a9f90b800af04f5e14f5f`
- Original November 4 derived 11-head CSV at merge #88: Git blob `619550162e0933636f901a4c3e2416456350d6c9`
- Original merged commit `2425a79518f9dbbed5f12564e2122c573babc659` retains both original field names and exact values, so the prior assertion remains recoverable
- This change adjusts **only derived field labels, explanatory text, and a machine-readable correction history**. Eleven SHA values, three commit deltas, 34 source attempts, Zenodo counters, external institution states and historical source evidence are unchanged
- This correction does not declare a new prospective timepoint: RS01–RS10 remain fixed, six layers × ten objects = 60 possible object-layer cells per **eligible declared observation point**, concrete schedule offsets remain undeclared

**Outcome:** `DERIVED_CLOCK_ANCHOR_RELABELED` · `SOURCE_VALUES_UNCHANGED` · `ORIGINAL_BLOBS_RECOVERABLE` · `NO_PROSPECTIVE_CELLS` · `NO_CONTRACT_CHANGE`
