# Conversation-supplied morning audit — 2026-10-08

## Provenance

The values below were supplied in the current conversation as the result of a
local/AI audit. The source reports collection during **08:12–08:26
Asia/Shanghai**, before an 08:30 summary cutoff. This package does not rewrite
those heterogeneous retrieval times into one simultaneous 08:30 observation.

The source named two local report files:

- `TenRepositoryMorningRecheck20261008.md`
- `AgentCohortRefresh20261008.md`

The updater did not read those files because the authorized desktop device was
offline. Device-specific local paths are not copied into this public repository.

## Aggregate source-reported state

| metric | 2026-10-07 preserved snapshot | 2026-10-08 source | change |
|---|---:|---:|---:|
| ten-family cumulative views | 695 | 775 | +80 |
| sum of ten family unique_views | 664 | 733 | +69 |
| ten-family downloads | 7 | 7 | 0 |
| ten current-version views | 54 | 70 | +16 |
| ten current-version downloads | 0 | 0 | 0 |
| OpenAlex main-author Works list | 41 | 43 | +2 |
| ORCID public work groups | 12 | 14 | +2 |
| ORCID source summaries | 54 | 56 | +2 |
| RSD public software records | 11 | 11 | 0 |

The source explicitly states that 733 is a sum of ten per-family
`unique_views` counters, not a cross-family deduplicated number of people.

## Fixed ten-object rows

| repository | prior family views | current family views | delta | current family downloads |
|---|---:|---:|---:|---:|
| welcome-to-github | 90 | 98 | +8 | 4 |
| zero-entropy-lab | 66 | 75 | +9 | 0 |
| Axiom-0 | 85 | 93 | +8 | 0 |
| reflective-continuum | 44 | 52 | +8 | 0 |
| agent-foundations | 71 | 78 | +7 | 1 |
| china-agentic-observatory | 81 | 88 | +7 | 0 |
| agentic-frontier-observatory | 85 | 93 | +8 | 1 |
| sci-render-kit | 57 | 65 | +8 | 1 |
| auto-doc-engine | 52 | 59 | +7 | 0 |
| epistemic-pipeline | 64 | 74 | +10 | 0 |

Source interpretation:

- largest absolute view increase: epistemic-pipeline, +10
- highest current family views: welcome-to-github, 98
- Axiom-0 and agentic-frontier-observatory: 93 each

Derived CSV rows use the repository's canonical RS mapping rather than this
display order.

## Identity-chain source report

- GitHub: 10/10 latest release remains the 2026-10-04 release
- Zenodo: 10/10 current-version DOI and family DOI relationships align
- DataCite: fixed-corpus 40/40 DOI records findable
- ORCID: fixed corpus remains 10 groups / 50 source summaries
- Software Heritage: 10/10 deposit snapshot -> release -> directory routes resolve
- OpenAIRE: 10/10 current-version exact DOI searches return records
- OpenAlex: all 40 fixed-corpus DOI records occur in the main-author Works list
- RSD: 11 public software records, the fixed ten plus the separate audit runtime

The source reports audit-runtime Zenodo family statistics separately as 47
views / 45 unique_views / 0 downloads. These are not added to the fixed-corpus
ten-family totals.

## OpenAlex source report

Main author: `lightlost / A5151904252`.

The source describes the current live list as:

```text
40 fixed-corpus Software works
+ 2 audit-runtime Software works (concept + current version)
+ 1 OSF registration work (other)
= 43 Works
```

The beta remains on secondary author `lostlight530 / A5157531946`.

The source reports:

- main author profile summary still displays 41 while live Works query returns 43
- secondary author profile summary displays 2 while its list returns 1
- the known citation remains the OSF-registration -> beta internal research-lineage relation
- no new external citation was observed in the checked audit-runtime lineage

## Agent cohort source report

The source reports a fixed cohort of **432 confirmed Agent software families**,
all 432 rechecked, with **868 checks** passing.

| repository | prior cohort-snapshot views | current views | delta | prior rank | current rank |
|---|---:|---:|---:|---:|---:|
| agentic-frontier-observatory | 88 | 93 | +5 | 8 | 8 |
| china-agentic-observatory | 83 | 88 | +5 | 9 | 9 |
| agent-foundations | 73 | 78 | +5 | 10 | 10 |
| epistemic-pipeline | 66 | 74 | +8 | 11 | 11 |

The source explicitly states that these prior view values differ from the
identity-chain table because the two historical snapshots were collected at
different times. They remain separate comparison baselines.

## Remaining source-reported states

- RSE PR #498: not merged
- HAL: no public record returned by the source query; no non-submission inference
- RRID: public resolver still blocked by HTTP 403
- identity-chain checks: 192 passed
- Agent-cohort checks: 868 passed
