# 2026-10-08 morning recheck

## Classification

- record class: `pre_eligibility_monitoring`
- prospective dataset member: **false**
- source collection window: **2026-10-08 08:12–08:26 Asia/Shanghai**, minute resolution
- source as-of label: **before 08:30 Asia/Shanghai**
- all platforms treated as one simultaneous 08:30 state: **no**
- fixed corpus changed: **no**
- preregistered layer denominator changed: **no**

No eligible post-registration fixed-corpus release event is recorded before this
recheck. The ten GitHub release pages independently verified here still point to
the 2026-10-04 `v2026.10-open-research-production-framework` release. This
package is therefore monitoring/reconciliation evidence, not a prospective
scheduled timepoint.

## Source and independent-verification planes

The conversation supplied a completed local morning audit and two local report
filenames. The updater could not read the local files because the authorized
desktop device was offline. The values in `source-summary.md` are therefore
preserved as conversation-supplied source evidence.

A separate independent public-endpoint pass was then executed. Results are
recorded in `independent-verification.md` and `normalized-summary.yaml`.

The two planes are intentionally not collapsed:

```text
conversation-supplied local audit
            !=
independent public-endpoint verification
```

Unsupported or blocked independent checks remain source-reported, partial, or
blocked rather than being promoted to verified success.

## Fixed-corpus metric delta reported by source

| metric | 2026-10-07 preserved snapshot | 2026-10-08 morning source | delta |
|---|---:|---:|---:|
| Zenodo family views | 695 | 775 | +80 |
| sum of family unique_views | 664 | 733 | +69 |
| family downloads | 7 | 7 | 0 |
| current-version views | 54 | 70 | +16 |
| current-version downloads | 0 | 0 | 0 |
| OpenAlex live author Works query | 41 | 43 | +2 |
| ORCID public work groups | 12 | 14 | +2 |
| ORCID source summaries | 54 | 56 | +2 |
| RSD public software records | 11 | 11 | 0 |

The source explicitly defines 733 as the sum of ten software-family
`unique_views` counters. It is not a cross-repository deduplicated audience
count.

## Independent verification result

Independently verified in this updater pass:

- GitHub: 10/10 exact 2026-10-04 release pages readable
- DataCite: 40/40 fixed-corpus DOI endpoints readable and typed Software
- Software Heritage: 10/10 previously preserved October directory SWHIDs readable
- OpenAIRE: 10/10 current-version exact DOI searches return one Software record,
  status `UNDER_CURATION`
- OpenAlex: 40/40 fixed-corpus DOI records resolve as Software under
  `A5151904252`; live Works query count is 43
- OpenAlex audit-runtime lineage: concept and current version are under the main
  author; beta remains under `A5157531946`; OSF registration remains an
  `other` work and references the beta work

Partially verified:

- ORCID public Works endpoint was readable and exposed current audit-runtime
  DOI/source content. The flattened extractor exposed 35 DataCite and 11
  OpenAIRE source-label occurrences, consistent with two additional DataCite
  appearances relative to the prior 33/11 source distribution. The extractor
  did not retain ORCID's XML grouping structure, so the updater does **not**
  claim an independent reconstruction of 14 groups / 56 summaries.

Blocked or not independently rerun:

- Zenodo human record pages for the ten current versions were readable, but the
  independent REST fetch path returned an unexpected-content-type failure and
  the human-page extraction did not expose the view counters. The 775 / 733 /
  70 statistics remain source-reported in this package.
- the full 432-family Agent cohort was not rerun because the local report and
  cohort inputs were inaccessible to the updater; the four owned rows and
  ranks are preserved as source-reported exploratory evidence.
- RSD's audit-runtime software page and constellation project page were
  independently readable, but the updater did not reconstruct the source's
  aggregate count of 11 records from a complete RSD listing.
- RSE PR #498 lacks a repository/URL in available updater evidence; its pending
  state remains source-reported.
- HAL zero-result and RRID resolver 403 remain bounded request/search outcomes,
  not absence claims.

## Files

- `source-summary.md` — source-reported morning audit
- `normalized-summary.yaml` — machine-readable source/verification separation
- `ten-repository-zenodo-delta.csv` — canonical RS01–RS10 source-reported view delta
- `agent-cohort-owned-rows.csv` — four source-reported owned rows in the 432-family exploratory cohort
- `independent-verification.md` — independent endpoint procedure and bounded outcomes
