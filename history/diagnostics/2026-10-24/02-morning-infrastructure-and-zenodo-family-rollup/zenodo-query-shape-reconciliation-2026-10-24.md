# Zenodo family Views — explicit two-source reconciliation (2026-10-24)

**Finding:** Two full Zenodo version-list query shapes returned distinct, internally consistent **non-unique Views** for the same 12 families and 45 version DOIs.

| Separate population | Standard `/versions?size=25` | Diagnostic `/versions?size=25&audit_probe=20261024T0733` | Source-field difference |
| --- | ---: | ---: | ---: |
| RS01–RS10 fixed sample | 2,545 | **2,695** | +150 |
| Independent research control (NOT RS11) | 130 | **135** | +5 |
| Independent life-science pilot | 6 | 6 | 0 |
| **Twelve family Views combined** | **2,681** | **2,836** | **+155** |

**Source clocks:** the original normal-URL [selected-field record](record.json) captured its own batch at `2026-10-23T23:31:39.690Z–2026-10-23T23:31:47.474Z` UTC. A parallel normal-vs-diagnostic comparison was made at `2026-10-23T23:32:31.386Z–23:32:36.630Z` (normal 2,681; diagnostic 2,836). A repeat with two other diagnostic query shapes at `23:32:54.862Z–23:33:00.945Z` also returned **2,836**. Individual version DOI identities were unchanged across forms; both enumerated all 45 versions with no pagination and gave per-family `sum(version_views)=stats.views`.

**Interpretive status: unresolved.** The **2,836 is a genuine returned *field-value total*** and supports the researcher's correction that our not-unique Zenodo Views can exceed 2,700. However changing URL parameters does **not prove** the diagnostic response is the freshest uncached server snapshot. The +155 is **NOT** a confirmed increase in real views during an observed interval, and not an incremental human audience count. The original 2,681 response remains attributed evidence. Raw transport bytes / Date headers were not retained.

- [One row per Zenodo concept DOI family](zenodo-query-shape-family-comparison.csv) contrasts both totals, including the separate control and pilot.
- [All 45 version DOI comparison rows](zenodo-query-shape-version-comparison.csv) retain the `version_views` from both URL forms.
- [Machine-readable correction](zenodo-query-shape-reconciliation.json) retains source bounds, identifiers, and caveats.

Never sum family-wide `stats.views` attached to each individual version; each concept family is counted once. Never sum `version_unique_views` as globally de-duplicated people. This document amends **only the interpretation of supplementary Zenodo diagnostics**, not the frozen OSF registration, the baseline, the preregistered RS01–RS10 corpus, the six layers, or the operational schedule. **Zero prospective cells** are created.
