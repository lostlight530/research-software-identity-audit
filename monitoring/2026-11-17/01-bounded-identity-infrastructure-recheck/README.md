# November 17 bounded research-software identity and infrastructure recheck

**Record class:** `PARTIAL / DIAGNOSTIC / NOT_PROSPECTIVE` · Logical date **2026-11-17 Asia/Shanghai** · Compiled after the 2026-11-16 UTC connector checks. The exact per-request client retrieval timestamp was **not retained**; provider event clocks and extractor acquisition-day labels must not be presented as equivalent request clocks.

[Machine-readable selected-field source ledger](record.json) · [November 15 original 458-key comparator](../../2026-11-15/02-full-institutional-source-recheck/reconciliation.md) · [November 15 GitHub source SHA list](../../2026-11-15/01-periodic-identity-infrastructure-recheck/github-main-heads.csv)

## Contract and comparator authority

- **OSF 5b329**, original Schema Response `6ac3ae5e6da32e3d0576ed72`, and distinct approved October 6 revision `6ac4c12fed97b8b77ce88a9c` remain untouched. The original-versus-approved comparison changed only exploratory analysis field `344-83`; later examples are not original primary preregistration.
- Exactly **RS01–RS10**, six analytical layers and **60** object-layer units per eligible scheduled timepoint. Seven operational platforms / **70 possible checks** and **34 supplementary surfaces** do not add study cells. CONTROL is never RS11.
- No numeric schedule offsets declared, no valid planned prospective timepoint assigned here, **zero new prospective cells**. All work here is diagnostic. The prior November 15 458-request source cohort was captured `2026-11-15T14:13:01.443173Z–14:13:54.131351Z` and is **not repeated** here.
- Comparison uses the November 15 *repository-first* GitHub SHAs for RS01–RS10 and the later November 15 post-reconciliation main `1097d441...` for CONTROL. Those comparator clocks are not falsely represented as one simultaneous snapshot.

## Direct connected GitHub results

- Fresh `main` branch pointers, comparison endpoints, open-PR search and Release inventories were checked for **all 11** repositories. All **11** branches are ahead of their specified comparators and **none behind**. Across separate repository comparisons: **312** per-repository ahead commits for RS01–RS10 plus **2** for CONTROL = **314**, **not 314 commits made on November 17**.
- **0 open PRs** across the 11 core repositories at inspection. Each fixed RS repository has **6** published Releases; latest remains `v2026.11-ten-day-evidence-checkpoint` (published November 10 UTC). No new fixed-corpus GitHub Release since the November 15 comparator.
- CONTROL now has **6** published Releases; the newest, `v2026.11-nov15-identity-reconciliation`, was published **2026-11-15T15:55:57Z**, *after* the full source capture, and is distinct from a verified Zenodo DOI version. Do not infer new immutable archival minting or eligible prospective research observation from a GitHub Release or advancing `main`.
- Pre-record CONTROL main `2dbf8cfd5ef6705fc3a9e2cd146e4b58b4760b58` has [successful advisory validation run 43924524915](https://github.com/lostlight530/research-software-identity-audit/actions/runs/43924524915). Three other core repositories' queried Actions run collections were empty; an empty collection is **not** CI failure. GitHub CI does not replay third-party provider raw bytes.

## Verified external institution workflow change

- [RSD issue #1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871), **OPEN on November 15**, is now **CLOSED / completed**, with `closed_at=2026-11-16T14:13:33Z`.
- [RSD fix PR #1897](https://github.com/research-software-directory/RSD-as-a-service/pull/1897) **merged 2026-11-16T14:13:31Z** as commit `4557b7271cb113c62f95da515d674f20b0924ac5`. Its actual diff changes MUI `Select` / `MenuItem` long-option wrapping and selected-text visibility; the fixed-width chips still rely on hover text. This is **real upstream code acceptance**, not a verified deployment or Windows/Edge browser retest.
- [RSD #1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870) remains closed since October 16; [RSE #498](https://github.com/rseng/software/pull/498) remains open/unmerged with no submitted official review. SciCrunch `SCR_029105` curation completion and ownership are **UNKNOWN**.

## Seven core platforms and 34 preexisting supplementary surfaces

- A **public extractor** was invoked for all **34 exact existing URLs** in two batches, receipts `extract_69ba51a7c9b64ac7b6f68bec2a4c10de` and `extract_6521e60335e83ca6b21e00f0d340790e`. **29** returned extractable representations and **5** extractor errors (ScreenIT connection; dkNET 403; InterLex 404; Identifiers.org 404; N2T 403). The 29 include **HAL bot challenge**, **SWH API documentation**, and stale/cached resources; they are **not 29 independently verified target registrations**.
- `acquired_at` in the extractor is a **UTC day label**, often old (including November 4–14 and even February for a static standard). `allow_live_fetch` does **not** prove origin freshness. These attempts do not constitute a new 34-URL source-origin byte capture or an apples-to-apples comparison of November 15 provider responses.
- Connected GitHub is the only core platform freshly verified at the specified full repository scope. Current Zenodo 67-version / fixed RS 60-version statistics, DataCite/OpenAIRE/OpenAlex 102-DOI cohorts, ORCID structured groups, and Software Heritage 10 origins were **NOT_EXECUTED as fresh full cohorts** by this run. Prior November 15 values remain historical: DataCite **102/102** findable, OpenAIRE **94/102** positive queries, OpenAlex **33** exact canonical DOI matches, ORCID **18 groups / 117 summaries**, RS01–RS10 Zenodo **4,059 version-views / 39 version-downloads**, SWH **10 full origin latest-visit responses**. None is relabelled a November 17 measurement.
- Any 403/404, timeout, missing or stale HTML is **NOT** proof of object nonexistence, platform indexing failure, absent preservation, scholarly adoption or non-adoption. Distinct query populations, DOIs, page UI counters and work groups remain separate.

## Disposition and provenance gaps

**`PARTIAL_WITH_VERIFIED_GITHUB_AND_RSD_UPSTREAM_CHANGE / NO_CHANGE_REQUIRED_FOR_CODE / ZERO_PROSPECTIVE_CELLS`**

This monitoring addition records machine-selected fields and stable GitHub URLs; it does **not** preserve new raw HTTP response bytes, per-request header/timestamps or an independent 458-key recapture. Historical raw, frozen OSF, baseline, schema, schedule, published tags, release metadata and correction history are unchanged. No new DOI, study object or Release was created.

**Retest conditions:** verify #1897 deployed behavior through an actual RSD production browser check; run a fresh timestamped provider-origin collector only if the full 458-key cohort is needed, preserving failures and clocks; separately compare exact DOI identity before interpreting any future metric deltas. Current unknowns are retained, not filled.
