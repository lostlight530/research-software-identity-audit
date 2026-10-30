# October 30 independent tag-ref and source-shape recheck

**Class:** append-only, **diagnostic only**, not an OSF amendment, prospective wave, new release, DOI, or full cross-platform census

## Why this was needed

The earlier [October 30 source-access review](../02-bounded-periodic-infrastructure-recheck/README.md) and [post-merge GitHub delta](../03-post-audit-github-delta/README.md) confirmed 11 published-Release lists, but those lists alone cannot rule out **plain Git tags**. This bounded follow-up separately queried Git tag references and reconciled source-exact fields without rewriting the earlier records.

## GitHub: 11 tag-ref checks, 44 returned refs

- The [tag-ref ledger](tag-ref-objects.csv) records **44** current `refs/tags/*` rows and target Git **commit SHA** values: **4 each** for the ten preregistered RS01–RS10 repositories and the standalone CONTROL
- All 44 returned current tag names match those in the separately queried 11 `GET /releases?per_page=100` published-Release lists, acquired within the same working session
- Fixed ten latest: `v2026.10-fourteen-day-evidence-checkpoint` (**2026-10-14 UTC published Release**); CONTROL latest: `v2026.10-evidence-integrity` (**2026-10-18 UTC**)
- The result eliminates the narrower **current tag-list gap** in the previous October 30 release-only view; it does **not** prove no deleted/historical tags, draft objects, other release mechanisms, or that a repository current commit has been archived. GitHub release `created_at`, `published_at`, Git tag target commit and `main` HEAD remain different clocks/objects
- Client tag-query batch envelope: `2026-10-30T14:52:34.203Z`–`2026-10-30T14:52:36.263Z` (UTC), **not** 11 independently captured origin HTTP timestamps. Structured GitHub connector results were parsed, but original provider HTTP response bytes/headers were not separately archived

## One strictly comparable Zenodo field delta

The existing [October 27 RS01 exact API-path representation](../../2026-10-27/01-bounded-seven-platform-recheck/README.md) for `/api/records/23365504/versions/latest` was **328 views / 239 unique_views / 6 downloads / 13 version_views**. A third-party extractor representation **acquired on October 30 UTC** under that **same URL** returned **346 / 256 / 6 / 18**, respectively.

The four **returned-field differences** are `+18 / +17 / 0 / +5`. This is not event-level access log data, global unique humans, independently verified scholarly adoption or a server-authenticated fresh snapshot. The extractor only provided **day-truncated UTC acquisition time**; the full-extract client envelope was `2026-10-30T14:50:42.157Z–14:50:43.429Z`. No original response-body bytes, headers or cache-bypass proof were obtained.

The [machine record](record.json) separates the original exact comparison path, source/acquisition clocks, source field names and calculated deltas. Other sampled platforms did **not** yield equivalent October 30 full dataset evidence: DataCite had a same-day **single OSF DOI** extract; ORCID, SWH and OpenAIRE returned **October 27** extracts; OpenAlex **October 6**; OSF **October 12**. They must not be presented as fresh October 30 cross-platform measurements. The previous **34-surface** ledger is retained unchanged, and this is not 34 new source acquisitions.

## Institutional engineering progress — source-level, not deployment-level

- [RSD #1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870) closed on October 16 UTC
- Independent upstream [RSD v6.7.3 release notes](https://github.com/research-software-directory/RSD-as-a-service/releases/tag/v6.7.3) dated **October 22 UTC** explicitly report the `custom markdown url validation and saving` fix, commit [`e04f179`](https://github.com/research-software-directory/RSD-as-a-service/commit/e04f179d70d93eefa1275eac7edaf4662410a1a4). The latest observed upstream release is v6.7.5 dated October 27 UTC
- The researcher's actual RSD production deployment/version, original reproduction-path retest, and user-facing resolution are **NOT_VERIFIED**; upstream published source `!=` demonstrated production fix
- [RSD #1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871) remains open; [RSE #498](https://github.com/rseng/software/pull/498) remains open/unmerged

## Contract and decision

**No scientific sample or method expansion:** RS01–RS10 = **10**, CONTROL `!= RS11`; six analytic layers = **60 per eligible scheduled point**, seven distinct operational platforms = **70 possible checks**, a different quantity. Operational schedule still declares **no concrete offsets**. October 14 GitHub releases and their currently visible tags are **not** authorization to backdate scheduled prospective observations. Zero prospective cells created

The RS01 citation metadata's September baseline concept DOI is documented as intentionally distinct from its October 14 version DOI in its own `RELEASE_POLICY.md`, so this audit does **not** label that difference a metadata defect or rewrite archived tags. No source code, frozen OSF text, prior evidence, baseline, schema, schedule, external account, Release, Tag or DOI changed

**Outcome:** `PASS` for the bounded 44-ref current GitHub tag-name/commit-target inventory and matched Release names; `SELECTED_FIELD_DELTA` for the RS01 Zenodo API representation; `PARTIAL / UNKNOWN` for full current seven-platform or 34-surface object census; `NO_CHANGE_REQUIRED` for code and citation metadata. CI validates repository structure and retained artifacts, not external scientific accuracy
