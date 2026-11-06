# November 6 bounded research-software identity and infrastructure patrol

**Class:** dated, append-only **diagnostic monitoring** and selected-field reconciliation against the [November 5 source-read record](../../2026-11-05/01-bounded-identity-infrastructure-recheck/README.md). **Not** a frozen-OSF amendment, newly scheduled prospective timepoint, historical baseline backfill, original HTTP transport archive, full DOI census, new GitHub Release or Zenodo deposit.

**Declared source-observation date:** 2026-11-06 Asia/Shanghai. The separate [machine summary](record.json) retains actual client-read batches; this report's GitHub queries were not atomic, and the extractor-provided `acquired_at` timestamps are **UTC-day granularity only**, not origin response times. Where acquisition is older than today, the value is a **reused source representation**, never a November 6 live provider verification.

## OSF contract, sample and analytical boundary

The [original OSF Registration](https://osf.io/5b329/overview) and [October 6 approved Schema Response revision](../../../contract/osf-registration-version-governance-2026-11-03.md) retain separate authorities. A previous exact 29-field comparison identified only `344-83`, exploratory planned-analysis wording, as changed. The current extractor reused November 1 representations of both schema responses; **no new live OSF revision claim** is justified. No registration write was attempted.

The [fixed corpus](../../../corpus/object-manifest.csv) remains **RS01–RS10** (ten research software objects), with the separate research-control repository **CONTROL, never RS11**. Six preregistered layers imply **60 object-layer cells per eligible scheduled timepoint**; seven operational platforms imply **70 possible object-platform checks**, not a new study denominator. The [schedule](../../../schedule/README.md) still declares no concrete operational offsets. This package is diagnostic, creates **0** formal prospective observation cells and does not modify baseline, original source records or the frozen contract.

## GitHub: 11 current mains, all PRs and published Releases

The [11-row GitHub comparison](github-main-heads.csv) pins the exact **Nov 5 prior source SHA** and newly connected **Nov 6 main SHA** for each object. GitHub read envelopes: branches **10:04:32.888–10:04:35.201 UTC**, PRs **10:04:44.638–10:04:46.739 UTC**, Release lists **10:04:55.044–10:04:56.376 UTC**, and SHA comparisons **10:05:10.326–10:05:13.286 UTC** on **2026-11-06**. These are client **batch** clocks, not individual HTTP origin timestamps.

- **All 10 fixed sample mains advanced**, with zero behind: RS01 **+35**, RS02 **+46**, RS03 **+33**, RS04 **+39**, RS05 **+29**, RS06 **+34**, RS07 **+39**, RS08 **+49**, RS09 **+26**, RS10 **+29** = **359 main-reachable commits summed across ten repositories** since the *recorded Nov 5 source SHAs*. The counted commits were not all authored on Nov 6. The unchanged CONTROL main is `756558f770099bc1676c6ca7dee14cf9419dd898`
- A sample diff shows dated source-custody and A1/A2 research audits across the repos; selected software and tool maintenance also changed in RS02, RS05–RS08, including documentation, CodeMeta, smoke workflow configuration and adapter implementation. **359 commits are not 359 unique releases, people, or scholarly propagation events**
- **Five Open PRs, all Draft:** [RS01 #916](https://github.com/lostlight530/welcome-to-github/pull/916), [RS01 #915](https://github.com/lostlight530/welcome-to-github/pull/915), [RS02 #807](https://github.com/lostlight530/zero-entropy-lab/pull/807), [RS05 #378](https://github.com/lostlight530/agent-foundations/pull/378), [RS10 #249](https://github.com/lostlight530/agentic-frontier-observatory/pull/249). CONTROL has no Open PR. Draft internal WorkflowHub proposals **do not prove WorkflowHub platform acceptance or an institutional relationship**
- Ten fixed repositories still list exactly **five published GitHub Releases each**, latest `v2026.10-30-evidence-snapshot`, **50** in total; CONTROL still lists five, latest `v2026.10-control-lifecycle-reconciliation`. There are **zero newly published Releases** against Nov 5. A fresh Git tag-ref re-enumeration or ten-family Zenodo version census was **not performed**, so this is specifically a GitHub published-Release-list result

## Seven operational platforms and 34 pre-existing supplementary service/standard surfaces

The exact [34-row source locator, access status, receipt and clock ledger](surface-access-recheck.csv) repeats all previously documented URLs rather than substituting new routes. The two extractor attempt envelopes were **10:05:49.161–10:06:31.650 UTC**, receipt `extract_509b7dd0af360c17235f328147171f33`, and **10:06:46.800–10:06:51.453 UTC**, receipt `extract_6762bce0d87a227689efd3e26f0735a4`.

- **34 attempts → 28 extractor representations / 6 errors**, the same access-class result as Nov 5. The six preserved errors are IDs **11** ASWG `connect_error`, **13** dkNET `404`, **14** InterLex `404`, **15** EDAM `fetch_error` despite HTTP 200 reported, **24** Identifiers.org `404`, **25** N2T `403`. These statuses do **not** prove a record, identifier or institution does not exist
- Of the 28 returned representations, **only surface 17 (Zenodo) has a Nov 6 UTC-day acquisition label**, **0** have Nov 5 and **27** have Nov 4 or earlier. A 28/34 extractor success ratio is **not** 28 currently verified institutional accessions
- In particular, HAL surface **21** returned a bot challenge, **not** a HAL work record; Software Heritage surface **29** returned API documentation, **not** structured SWH origin/visit JSON. Their `EXTRACTED` state is a transport/extractor label, not a positive scientific observation of inclusion or preservation
- Core platform selected-field boundary: GitHub **fresh via connected source**; Zenodo **Nov 6 selected RS01 record**; DataCite **Nov 4 OSF registration DOI extract / Oct 31 RS01 version DOI extract**, ORCID **Oct 27 author works extract**, OpenAIRE **Nov 4 selected DOI extract**, OpenAlex **Nov 4 author profile extract**, SWH **Nov 4 documentation-only extract**. The seven platforms were attempted as separate evidence sources; this **does not** constitute a full contemporary ten-object × seven-platform census

## Comparable Zenodo record and usage counter

Selected RS01 [Zenodo version record 23811380](https://zenodo.org/api/records/23811380) and the `versions/latest` route for `23365504` resolved to the **same record** in extractor response receipt `extract_529c4df76fa201067c14a102f7cd3cc8` (client read **10:07:19.149–10:07:20.965 UTC**, extractor `acquired_at=2026-11-06T00:00:00Z`).

- Exact DOI roles: concept `10.5281/zenodo.22790907`, version `10.5281/zenodo.23811380`, publication date **2026-10-30**
- Same record, attached **family `stats.views`: 391 (Nov 5 retained source) → 408 (Nov 6 extractor), +17**. Attached **`stats.downloads`: 7 → 7, +0**
- Nov 6 independently exposed fields within this record: attached family `unique_views=317`, version-local `version_views=19`, `version_downloads=1`. These use **different grains** and are neither added together nor called 17 distinct human visitors

**Evidence limitation:** the source full-content extractor initially returned parseable selected record JSON, but the subsequent independent attempt to retain an entire raw response in GitHub was `RATE_LIMITED`. Original HTTP response bytes, origin headers, and a source transport digest were **not retained**. The [machine record](record.json) keeps the validated selected fields, URL, acquisition day, request envelope, error classification and external receipt **without falsely describing this as byte-level replay**. There is no fabricated second capture.

The earlier **Nov 2** 90-DOI/17-ORCID-group/32-OpenAlex-Work/88-OpenAIRE-result/57-Zenodo-version counts remain **historical reference only**, not a new Nov 6 recount.

## Institution-facing interaction and governance

Independent GitHub upstream reads at client session ~**2026-11-06T10:07 UTC**:

- [RSE Encyclopedia #498](https://github.com/rseng/software/pull/498): **open, unmerged, zero reviews**, last updated **2026-10-07T13:02:55Z**
- [RSD #1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870): **closed/completed Oct 16**, no verified production UI re-test
- [RSD #1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871): **open**, no new verified interaction since prior check. Latest upstream RSD published Release **v6.7.5**
- RRID `SCR_029105` earlier resolver/index observations remain separate from curator validation, institutional endorsement and user adoption; recent cached resolver results cannot establish a new curator event
- Official OSF Projects read-only notice remains an external-policy issue, **not** a change to the preregistration. The previous record's official-page internal **2026 versus 2027 API-date conflict** remains **UNRESOLVED**, not silently repaired

No new verifiable direct institutional correspondence, accepted contribution, curation approval or partnership is established by this patrol.

## Verification, repair and unresolved states

This task's only identified implementation defect is a **forward-compatibility check gap** in the Nov 5 advisory `check_bounded_surface_ledger` implementation: historical `nov5/nov4` acquisition-day key names should not be reused to validate records dated Nov 6 onward. This PR adds a **date-neutral, opt-in bucket comparison**, plus synthetic positive/negative tests, without altering the previously retained Nov 4–5 data or adding a new dependency. GitHub Actions advisory checker and the actual PR/post-merge status must be checked separately.

No frozen OSF contract, fixed manifest, existing baseline, raw source package, historical observation, schema/platform vocabulary, Release, DOI, citation identity or active concrete schedule is changed. No unplanned statistical inference, imputation, global composite score or research claim upgrade is introduced.

**Remaining unknown:** up-to-the-minute full 10×7 observations, all 90 historical DOI identities today, current ORCID/OpenAlex/OpenAIRE indexing or counts, SWH source preservation visits, live institution curator/account outcomes, actual external HTTP bytes/headers, and full ten-family Zenodo usage increments. **`PARTIAL` and `UNKNOWN` are valid conclusions**, not missing successes to invent.

**Disposition:** `PARTIAL` · `ALL_FIXED_MAIN_AHEAD_359` · `NO_NEW_RELEASE` · `RS01_ZENODO_FAMILY_VIEWS_PLUS_17` · `UPSTREAM_STATUS_NO_CHANGE` · `EXTRACTOR_RAW_CAPTURE_RATE_LIMITED` · `DATE_NEUTRAL_CHECKER_REPAIR` · `PROSPECTIVE_CELLS_0`
