# October 31 noon user-page reconciliation

This diagnostic record retains the maintainer's 13:00-hour WorkflowHub Dashboard,
13:24 Zenodo family counters, DataCite Commons facets and OpenAIRE page counts.
It supplements the [earlier release/identity check](../01-bounded-research-identity-and-infrastructure-recheck/README.md).
It is a user-source import, not a fresh institutional census or scheduled prospective observation.

## Reported counters

| Surface | User-provided values | Counting unit |
|---|---|---|
| WorkflowHub | 7,117 views / 820 downloads | Four Dashboard assets |
| Zenodo fixed ten | 2,306 unique views / 16 unique downloads | Sum of ten family fields |
| Zenodo descriptive twelve | 2,457 unique views / 24 unique downloads | Fixed ten plus control and life-science software |
| DataCite Commons | 87 records: 66 Software + 19 Workflow + 1 Project + 1 Study Registration | ORCID-filtered DOI records |
| OpenAIRE My ORCID links | 15 | Displayed account link count |

The selected Dashboard Period and exact capture timestamp were not supplied.
The Zenodo table carries the maintainer's 13:24 label. Neither is replaced by an
invented second-resolution clock.

## Source comparison

The separately retained 12:00:27–12:02:44 public API/detail-page extraction has
WorkflowHub 6,979 / 822 and Zenodo twelve-family unique counters 2,455 / 24.
The Dashboard's 7,117 / 820 is a different source surface; the Life Science
Dashboard download count is 156 versus 167 in that earlier detail response.
These are numeric comparisons, without an assigned cache, rollback or growth mechanism.
The Zenodo user table differs in two unique-view fields: welcome 264 versus 263,
and Reflective Continuum 189 versus 188.

DataCite's 87 ORCID-query records and the separately attributed 88-DOI inventory
use different inclusion rules: the latter includes the maintainer's Beta record
without an ORCID creator identifier. Commons labels wa5v8 as Project; its API
resourceTypeGeneral=Text and resourceType=Project are preserved as separate fields.

OpenAIRE returns 13 entries for 5B329, eight for the control's current version,
ten for wa5v8 and three for Beta. These counts describe PID result entries,
not additional software families. The page displays August 10 as its last ORCID
synchronization date; the actual synchronization event was not independently checked.

## Artifacts and research boundary

- [Machine summary](record.json)
- [Zenodo user fields](zenodo-family-user-statistics.csv)
- [WorkflowHub user fields](workflowhub-dashboard-user-statistics.csv)
- [OpenAIRE PID counts](openaire-pid-result-counts.csv)
- [Cross-source numerical comparison](source-comparison.json)
- [Selected source fields and provenance](../../../evidence/2026-10-31/02-noon-user-page-reconciliation/README.md)

Join fixed IDs by repository name against corpus/object-manifest.csv. Do not
reuse display-order IDs from informal tables. CONTROL and the life-science
software remain supplementary; no RS11 is introduced.

The fixed ten objects, six analytical layers / 60 units, seven operational
platforms, frozen OSF contract, baseline, schedule and prospective dataset are
unchanged. The 14:41 all-version Zenodo capture is outside this noon record.
No historical source is overwritten and no release or DOI is created.
