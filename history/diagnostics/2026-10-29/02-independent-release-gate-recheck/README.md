# Independent October 29 GitHub Release-gate recheck

**Logical date:** 2026-10-29, Asia/Shanghai  
**Classification:** diagnostic-only, read-only, additional independent connector pass; **not** prospective data, a scheduled timepoint, an OSF amendment, or a seven-platform census

## Scope and source provenance

- Frozen research contract: [OSF registration 5b329](https://osf.io/5b329/overview), DOI `10.17605/OSF.IO/5B329`; repository mapping: [contract/preregistration.md](../../../contract/preregistration.md)
- GitHub source-control base: [`7d2b8b9b762ec18c415ceb4d3c09ad63e9c6c22f`](https://github.com/lostlight530/research-software-identity-audit/commit/7d2b8b9b762ec18c415ceb4d3c09ad63e9c6c22f); **0 open PRs** at inspection
- Collection: connected GitHub `fetch` calls to the **11 exact Releases API list URLs** in [source-ledger.csv](source-ledger.csv), one list per frozen RS01–RS10 plus the separate CONTROL repository, `per_page=100`
- **Tool-orchestration client clock envelope:** `2026-10-29T15:58:34.748Z`–`2026-10-29T15:58:36.538Z` (23:58:34–23:58:36 Asia/Shanghai), measured by JavaScript `Date` immediately before and after the awaited connector call batch; not independently signed, not per-request start/end, not server-origin timestamps or exact first-appearance times
- The connector returned structured JSON lists, but unmodified HTTP response body bytes, headers, conditional requests, and external origin/cache proofs were **not archived here**. The CSV is a selected-field projection made from the connector result, not raw transport evidence

## Independently checked returned fields

| Scope | Result | Latest published Release |
| --- | --- | --- |
| Fixed **RS01–RS10** | **10/10 structured successful Release lists**, each with **4 public Release rows**; latest tag uniformly `v2026.10-fourteen-day-evidence-checkpoint` | 2026-10-14 UTC (object-specific timestamps in CSV) |
| **CONTROL**, not RS11 | **1/1 structured successful Release list**, with **4 public Release rows**; latest tag `v2026.10-evidence-integrity` | `2026-10-18T04:38:57Z` |

All returned list entries were non-draft and the latest entries were not prereleases. The observed fields agree with the previous [October 29 bounded diagnostic](../01-bounded-contract-recheck/README.md) and its [explicit clock correction](../01-bounded-contract-recheck/clock-provenance-correction.md). Agreement is limited to the listed GitHub Release fields and **does not retroactively validate the previous record's unverified 18-row time brackets**.

**Unit discipline:** 40 fixed-object published Release *rows* and 4 CONTROL Release *rows* are not 44 research objects or DOI records. The registered corpus remains **10 objects × 6 layers = 60 object-layer units per eligible scheduled timepoint**; the seven operational platforms could contribute **70 object-platform checks** when completely checked. OpenAIRE and OpenAlex share the one `discovery_graph` analytical layer.

## Contract, CI and access review

- [Schedule](../../../schedule/README.md): still has **no declared concrete offsets or complete scheduled follow-up list**; an October 14 fixed-corpus Release does **not** on its own establish eligible prospective execution
- [Raw observations](../../../observations/raw/README.md): no prospective records created by this recheck, no missing outcomes reclassified as absence
- At the inspected base SHA, [GitHub Actions run 40732181726](https://github.com/lostlight530/research-software-identity-audit/actions/runs/40732181726) concluded `success`; its job-step API separately reported `success` for the advisory checker, strict advisory check, observation tests, all-public-manifest verifier, retained-evidence checks, and record-path check. These are **implementation verification outcomes**, not new scientific or origin-source verification
- Separate public-page attempts in the same review session could not retrieve the OSF Overview (`403`) or resolve the DOI through the available web reader. Those **access limitations do not negate** the earlier recorded OSF registration or establish its original/updated version difference; these attempts are not included as successful requests in the 11 GitHub rows
- Zenodo, DataCite, ORCID, Software Heritage, OpenAIRE, and OpenAlex were **not independently recollected** in this pass. No claim of a contemporaneous full seven-platform recheck, external propagation change, latency, authorship aggregation, or missing object is justified

## Decision and residual uncertainty

**Result: `PASS` for the bounded 11-URL GitHub Releases field recheck; `PARTIAL / NO_CONCLUSION` for the cross-platform same-day research recheck.** The prior October 29 clock-provenance correction remains in force. No substantive new source-field delta was observed within the same 11 GitHub list projections, but no broad claim of no activity is made.

**Remaining gates:** exact frozen OSF revision history, source-retrieval provenance for external platforms, a separately declared operational schedule prior to any prospective interpretation, and fully attributable source captures. Future source failures, 403/404/429, anti-bot challenges or missing responses are recorded as limited/unknown, never as object-level absence.

**Change boundaries:** no edits to `contract/`, `corpus/`, `schema/`, `baseline/`, `schedule/`, `observations/`, historical monitoring, releases, tags or DOI records. No new dependencies, inference models or global scores.
