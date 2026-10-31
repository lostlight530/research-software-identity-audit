# Control-repository lifecycle and independent source recheck — October 5–31, 2026

> **Kind:** pinned retrospective GitHub engineering audit and bounded independent public-surface diagnostic, compiled after the historical events. **Not** a scheduled prospective observation, OSF amendment, new Release/Tag/DOI, origin-HTTP recapture, or eleven-object scientific sample
>
> **Snapshot base:** [`c4df38945c91c49dc0486550251269d75c80722e`](https://github.com/lostlight530/research-software-identity-audit/commit/c4df38945c91c49dc0486550251269d75c80722e), last committer timestamp **2026-10-31T06:28:47Z**. The work in this closeout PR is **outside** that pinned inventory by design

## Verified lifecycle inventory

- Control repository `created_at=2026-10-05T14:59:45Z`; first reachable `main` commit [`e5ba0a0e7dc548bd5bd3e79b4d7fc0cb95e528aa`](https://github.com/lostlight530/research-software-identity-audit/commit/e5ba0a0e7dc548bd5bd3e79b4d7fc0cb95e528aa) at **2026-10-05T14:59:46Z** — the repo was created after the separate OSF registration on October 5 at 14:04:13Z
- Independent GitHub REST read: **96 reachable `main` commits**, [complete ordered ledger](research-control-main-history-through-2026-10-31.csv), fetched with `sha=<snapshot>&per_page=100`, oldest entry independently checked. Does **not** include unreachable branches, PR-only commits, untracked local files or every external research event
- Current recursive tree: **625 entries**, **`truncated=false`**, **499 tracked blobs**. [All 499 original Git blob SHAs, owning prefixes and as-of difference](research-control-tracked-files-through-2026-10-31.csv)
- Older Oct 28 frozen tree [`4cacb9b6...`](https://github.com/lostlight530/research-software-identity-audit/commit/4cacb9b617d2e0383ffca8c757e66c5a44a5a793): **87 reachable `main` commits, 437 tracked blobs**. Two pinned tree endpoints compare as **62 added paths, 4 changed preexisting blobs, 0 removed paths**. This is an endpoint-to-endpoint Git comparison, not proof of zero intermediate changes
- [Full pull-request history](research-control-pr-history-through-2026-10-31.csv): **77 PRs**, **76 merged**, **1 closed without merging** (#16), **0 open** at the checked snapshot. PR lifecycle records and merged Git commits are different counting units
- [Eleven independently fetched core `main` refs](research-core-main-heads-2026-10-31.csv): RS01–RS10 all have **5** published Releases, most recent `v2026.10-30-evidence-snapshot`, and the separate CONTROL has **4**, latest `v2026.10-evidence-integrity`; all eleven have zero Open PR at initial read. These are Release-list results, not unique DOI or independent scholarly-adoption counts

## Day-one to current research-engineering history

| Beijing-local date | Grounded engineering/research event | Contract/provenance limit |
| --- | --- | --- |
| **Oct 5** | Frozen OSF Registration `5b329`; subsequent independent control repo creation and first `main` commit; historical baseline cutoff at 23:59:59 Asia/Shanghai | Later baseline reconciliation retrieval does not become a contemporaneous Oct 5 raw observation |
| **Oct 6–13** | Baseline reconciliation, RS identity correction, original source/provenance retention, schema and OSF Overview crosswalk, exploratory platform measurements and release-gate work | The OSF later `344-83` revision is not retrospectively original preregistration |
| **Oct 14–18** | Ten fixed sample checkpoint Releases, subsequent identity/discovery diagnostics; CONTROL separate evidence-integrity release and archival/citation review | A fixed-corpus Release does not itself declare a scheduled prospective timepoint |
| **Oct 19–24** | Source checks, local evidence handoff, file and path inventories, creation/release calendar reconstructions and corrections | Git objects, local captures and external API timestamps are distinct |
| **Oct 25–28** | Platform semantics/assurance checks, 34-row external-surface investigation, public manifest checks and the historical [Oct 28 cutoff](control-repository-lifecycle-audit-through-2026-10-28.md) | The Oct 28 audit pins 87 commits/437 tracked files and is not silently overwritten |
| **Oct 29–30** | Independent GitHub release gate, OSF original/revised 29-field comparison and bounded 34-surface snapshots; ten new fixed-corpus GitHub Releases on Oct 30 | Two historical diagnostics originally lacked machine indexes; later indexes explicitly attributed in [reconciliation](research-historical-machine-record-reconciliation-2026-10-31.md) |
| **Oct 31** | New ten-version Zenodo/DataCite identity diagnostics, user dashboard vs API field reconciliation, 473-attempt/34-surface record, 55-version capture, time-zone correction and PR #77 merged with advisory CI | All retained today as **diagnostic**; UTC+8 corrected time is 13:41–13:42, not 14:41–14:42 |

These phases are navigational summaries of dated files; the [complete commit list](research-control-main-history-through-2026-10-31.csv) provides independently inspectable Git timing, and the [monitoring index](../monitoring/README.md) owns the actual source-specific study record.

## Independent bounded cloud recheck and freshness

This separate closeout re-read does **not** relabel PR #77's **473 requests** as newly re-executed. A fresh batch of source-access calls to [all 34 existing representative surface URLs](research-independent-34-surface-access-2026-10-31.csv) ran within the tool-client interval **2026-10-31T06:50:43.114Z–06:51:10.327Z**:

| Independent access result | Count | Permitted interpretation |
| --- | ---: | --- |
| Connected GitHub structured reads | **2** | Exact current RSE PR #498 and RS01 Releases list, not original HTTP byte custody |
| Third-party extractor acquired on October 31 UTC | **2** | Extraction has **day-granularity** acquisition; not proven origin-uncached or per-request fresh |
| Third-party extractor acquired on older UTC dates | **24** | Previously acquired/cache representation, not newly measured platform state |
| Fetch error / access blocked | **6** | Retain failures (connect; 404; 403; extraction error even though status 200), not evidence of global object absence |
| **Existing surface inventory total** | **34** | 34 services, standards and resolvers — **not 34 independent research institutions** |

Cloud selected-source `extract_id` provenance: `extract_3e7a142e75dc62aa2a8a0c803879db46`, `extract_b25bc8c65239868aa131469cc5f092c8`. They are **tool receipts, not cryptographic origin capture signatures**. No HTTP origin body bytes/headers were captured in this closeout. The earlier independently retained 473-request package remains separately attributed to its own 12:00–12:02 Beijing collector window.

A further [seven-operational-platform RS01 sample](research-seven-platform-bounded-rs01-2026-10-31.csv), attempted within **2026-10-31T06:52:04.436Z–06:52:54.720Z**, found GitHub connected-current; selected Zenodo and DataCite representations acquired on Oct 31 UTC; ORCID and Software Heritage older Oct 27 extracts; OpenAIRE timeout and OpenAlex exact DOI 404. This is **one selected object/sample route**, not 70 completed object-platform checks. It provides **no new global non-indexing claim**. The exact source URLs and separate discovery failures are retained in the CSV.

## Current earlier-captured platform metrics, not independently recreated in this closeout

The [October 31 existing institutional diagnostic](../monitoring/2026-10-31/03-independent-institutional-statistics/README.md) reports 88 attributable DOI records, ORCID 17 groups / 104 summaries, and OpenAlex 32; OpenAIRE's 88 queried DOI seeds produced 57 matching DOI and 87 record IDs. Its claims belong **only to its original collector and source window**, not to this second 34-representative-URL access audit. The [Zenodo all-version record](../monitoring/2026-10-31/04-zenodo-all-version-statistics/README.md) has 50 fixed-corpus + 4 CONTROL + 1 supplementary versions, fixed-corpus 3,200 views / 2,307 summed unique-view counters / 17 downloads / 16 unique-download counters. No unique-person, causal-referral, citation/adoption or independent-scientific-validation conclusion follows from those values.

Institutional progress from direct GitHub source: [RSD #1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870) **closed** at 2026-10-16T12:11:19Z; [RSD #1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871) **open**; [RSE #498](https://github.com/rseng/software/pull/498) **open/unmerged**. Upstream RSD v6.7.3 describes improved external-Markdown URL validation, but the original production reproduction path and user-side deployment have not been independently replayed. None is an employment or scientific endorsement.

## Correction boundary, formal analytical status and acceptance gate

The two previously missing machine record **indexes** are now added as retrospective derived pointers, not as invented original source bytes: see [correction note](research-historical-machine-record-reconciliation-2026-10-31.md). The Oct 31 correction of the incorrect `14:41` local label stays in [its original source's correction history](../monitoring/2026-10-31/04-zenodo-all-version-statistics/clock-conversion-correction.md). Earlier evidence, initial baseline, frozen registration and later OSF revision text remain as recorded.

**OSF scientific scope:** `RS01–RS10` fixed 10 objects; **6 analytical layers**, **60 object-layer units per declared eligible timepoint**; **7 operational platforms**, **70 possible platform checks** (not analytical units). OpenAIRE/OpenAlex both map to `discovery_graph`. `CONTROL`, life-science supplementary and new workflow/DOI records are not additional study objects. The [schedule](../schedule/README.md) still has **no concrete offsets**, so **0 new prospective cells**. No registration/revision, schedule, baseline, tag, release, DOI or current source identity was modified by this closeout.

**Known still-unknown items:** original source HTTP bodies/cache bypass for third-party extracts; fresh structured ORCID, OpenAlex, OpenAIRE and SWH 10-object census; exact propagation/ingestion latency; platform-internal indexing and cache reconciliation; scientific usage or independent verification; complete CI history of every past branch/PR. GitHub CI verifies repository contract and selected retained artifacts, not those scientific claims.

**Implementation checks required before merge:** new Git history/tree/PR CSV row counts (96/499/77), source-row 34 and platform-row 7, dated monitoring path checker, machine index provenance, strict contract guard, manifest integrity and existing retained tests. Any runner success must be checked by step, not equated to all commands passing.
