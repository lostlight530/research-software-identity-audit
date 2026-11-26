# November 10 periodic research-software identity and infrastructure patrol

**Record class:** bounded diagnostic monitoring, **not** an OSF-scheduled prospective timepoint. **Logical date:** 2026-11-10 Asia/Shanghai. Machine compilation clock is in [record.json](record.json); source GitHub calls are non-atomic, and external extractor `acquired_at` timestamps are **UTC day labels**, not individual HTTP response clocks.

## Contract / provenance gate

- Original frozen [OSF 5b329](https://osf.io/5b329/overview) is distinct from its October 6 approved Schema Response revision. Previously retained 29-field comparison changed only `344-83` (exploratory examples); no new OSF source-byte diff or OSF write in this session
- Exactly [RS01–RS10](../../../corpus/object-manifest.csv) remain sample members; **CONTROL is not RS11**; the supplementary Life Science family is not added
- Six preregistered analytical layers × ten objects = **60 eligible object-layer units per scheduled timepoint**. Seven operational platforms would mean 70 checks, **not** 70 analytical units; OpenAIRE and OpenAlex both map to `discovery_graph`
- [schedule/README.md](../../../schedule/README.md) still declares no concrete operational offsets; no **new fixed-corpus Published Release** was verified. **Zero prospective cells** created
- No original baseline, prior raw attempt ledger, OSF amendments/deviations, historical file, release artifact, DOI or source citation identity is modified

## Direct current GitHub evidence

[11-row pinned comparison](github-main-heads.csv) takes each **November 9 recorded main SHA** as base and reads November 10 connected `main`/Open PR/Published Release collections

- **All ten fixed-sample mains ahead, 0 behind; 183 summed per-repository ahead commits** relative to November 9 recorded SHAs (not a November 10-only daily commit rate)
- **CONTROL main unchanged** at `200cc6611e11ee5c557ceaae442b5e30b7db51de`, with **0 open PRs before patrol**
- Existing single open Draft PR: [RS05 / agent-foundations #378](https://github.com/lostlight530/agent-foundations/pull/378); no independently verified new external scholarly acceptance
- Fixed ten still each have **5 Published Releases**, latest `v2026.10-30-evidence-snapshot` (total 50). CONTROL remains 5, latest `v2026.10-control-lifecycle-reconciliation`. **Zero new Published Releases** since previous catalog; new main commits are not new release events

## Seven platforms / 34 established services and standards

[34 source URLs and access states](surface-access-recheck.csv) preserve IDs 1–34, two extractor receipts, six failures and exact acquisition-day labels:

- **34 attempts → 28 extracted representations / 6 access or extraction errors** at IDs **11, 13, 14, 15, 24, 25**
- Among 28 successful extracts: **1** with November 10 UTC-day label, **10** November 9, **17** older. These are not 28 current origin-provider verifications. ID 13 dkNET yields HTTP 403, ID 11 connection error, ID 14 HTTP 404, ID 15 extraction failure with HTTP 200, ID 24 HTTP 404, ID 25 HTTP 403; source access errors **never** imply object absence
- **Zenodo RS01:** [record 23811380](https://zenodo.org/api/records/23811380), version DOI `10.5281/zenodo.23811380`, concept DOI `10.5281/zenodo.22790907`, still version `v2026.10-30-evidence-snapshot`. Attached family views **422 (Nov 9 day) → 424 (Nov 10 day), +2**; attached unique views **330 → 332, +2**; family downloads **7 → 7**, version-local views **22 → 22**. Both `/records/23811380` and `/records/23365504/versions/latest` returned the same selected record. No source HTTP bytes/headers were retained, and these are **not unique human readers or day-specific rates**
- **Zenodo twelve-family selected record URL attempt:** 12 URL representations returned, but **only RS01 has a November 10 acquisition label**; 11 others are cached from October 31–November 4, so a new fixed-ten aggregate and 57-version contemporaneous reconciliation are **NOT_DERIVABLE**. Exact URL/day pairs are retained in [record.json](record.json)
- **WorkflowHub #2332:** independent detail extraction labelled **Nov 9** reported **3259 views / 485 downloads**, versus **3177 / 473** in Nov 8 provider-capture (between-capture **+82/+12**). It is **not a Nov 10 live metric**. #2334/#2337/#2347 returned Oct 16–17 cached pages, so no current four-workflow total is claimed; November 8 Detail 9443/1240 and Dashboard 9603/1241 stay separately attributed
- **DataCite / ORCID / OpenAlex / OpenAIRE:** November 8's [492-attempt capture](../../2026-11-08/02-complete-institutional-recheck/README.md) remains the latest **full retained recheck**: 92 attributable DOI identities (including two WorkflowHub version DOIs added vs Nov 2), 19 ORCID groups / 108 summaries, 32 OpenAlex Works, 92 OpenAIRE DOI queries with 59 matched DOI queries mapping to 17 different software result IDs. **No November 10 full DOI, author or discovery census**; today's selected extracts for these are cached October 27–November 4
- **Software Heritage:** Nov 8 latest visits reported `full` for all 12 origins (10 fixed, CONTROL, supplementary). Today's selected extraction returns documentation, **not a fresh origin visit JSON**; individual release-revision preservation remains independently unverified. **HAL** still offers only a cached bot-challenge page here, not an accession or moderation receipt

## Institution-facing interactions, directly checked via GitHub

- [RSE Encyclopedia PR #498](https://github.com/rseng/software/pull/498): **open / unmerged**, last updated `2026-10-07T13:02:55Z`
- [RSD #1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870): **closed** on `2026-10-16T12:11:19Z`, but production UI retest remains **UNKNOWN**
- [RSD #1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871): **open**, last updated `2026-10-16T08:05:49Z`; last published upstream RSD Release `v6.7.5`
- RRID `SCR_029105` has older resource resolver representations, but latest curator confirmation, any new endorsement or institutional affiliation remain **UNKNOWN / NOT_VERIFIED**

## Evidence, correction, review disposition

Connected GitHub branch, PR and Release metadata were directly read, with comparison source SHAs in [github-main-heads.csv](github-main-heads.csv). Selected third-party excerpts and their exact source locators/UTC-day acquisition labels, receipts, errors and special Zenodo/WorkflowHub reconciliations are in [surface-access-recheck.csv](surface-access-recheck.csv) and [record.json](record.json). External extractor output does **not** preserve the original current HTTP transport, server timestamp or per-response SHA-256, and may return older cached content; do not promote it to real-time proof.

**No verified code/schema, scientific contract, DOI identity or historical evidence defect**. The only justified write is **append-only diagnostic monitoring + navigation**. No new release, DOI, OSF revision, retrospective baseline rewrite, inferential statistical claim or prospective observation was created. Advisory checker command logs and PR/post-merge CI must be inspected separately.

**Disposition:** `PARTIAL` / `NO_NEW_RELEASE` / `GITHUB_FIXED_MAIN_PLUS_183` / `RS01_FAMILY_VIEWS_PLUS_2` / `34_SURFACES_28_EXTRACTED_6_ERRORS` / `INSTITUTION_NO_MATERIAL_CHANGE` / `NO_CHANGE_REQUIRED` / `PROSPECTIVE_CELLS_0`
