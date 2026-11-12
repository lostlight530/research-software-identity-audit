# 2026-11-13 bounded institutional/source recheck

**Class:** diagnostic public-source monitoring; not a scheduled OSF prospective observation, not an account interaction and not a claim of complete institutional acceptance

**Actual corrected cloud capture:** 2026-11-12T17:06:46.320272Z–17:07:52.118572Z (2026-11-13 Asia/Shanghai) on GitHub Actions [run 43265914410](https://github.com/lostlight530/research-software-identity-audit/actions/runs/43265914410)

[Machine record](record.json) | [Source attempt ledger](../../../evidence/2026-11-13/01-full-institutional-recheck/source-attempts.jsonl) | [Selected public fields](../../../evidence/2026-11-13/01-full-institutional-recheck/selected-fields.jsonl) | [Hash manifest](../../../evidence/2026-11-13/01-full-institutional-recheck/artifact-manifest.json)

## Bound scope and denominators

- **11** fresh GitHub main SHA and release inventories: **10** fixed research software objects RS01–RS10 plus independent CONTROL, not RS11
- **34** established external institution/service/standard surfaces, *not* 34 separate partner institutions
- **102** known DOI inventory: 92 from the November 8 diagnostic inventory plus ten November 10 fixed-object checkpoint version DOIs; not a claim that there are only 102 public DOIs in every possible system
- **458** actual public HTTP attempts in this runner: 34 surface + 306 exact DOI lookups (DataCite/OpenAIRE/OpenAlex) + 67 Zenodo individual versions + 33 GitHub heads/releases and RSD software pages + 10 Software Heritage origins + two RSD issues + RSD person/project + four WorkflowHub metadata endpoints
- OSF original response `6ac3ae5e6da32e3d0576ed72` and approved revision `6ac4c12fed97b8b77ce88a9c` remain distinct; no OSF write. No operational prospective timepoint offsets are declared, **zero** prospective cells added
- **60 preregistered object × layer units per eligible scheduled timepoint** remain the contract. 7 platforms and 34 external surfaces do not redefine that denominator

## Current directly captured results

| Surface | Current public endpoint evidence | Semantic limit |
| --- | --- | --- |
| DataCite | 102/102 known DOI calls HTTP 200, all `findable` | DOI identity, not independent citation/adoption |
| OpenAIRE | 102/102 DOI calls HTTP 200, 94 returned positive software query totals | Query-positive DOI count, not 94 distinct software objects; 8 zero-result queries are not universal absence |
| OpenAlex | 102 DOI lookups HTTP 200, 33 distinct returned Work IDs; 33 returned canonical DOI exact matches, 69 canonical mismatches | Multiple DOI queries may resolve to an aggregated Work; no inference of 102 independent Works |
| ORCID | 18 groups / 117 work summaries, 92 DataCite source-name, 12 OpenAIRE source-name, 13 unavailable source-name | Missing source-name is **UNKNOWN**, not proof of 13 self/manual updates |
| Zenodo | All 67 version records HTTP 200; fixed ten sum to **3,849 family views / 37 downloads** from 60 version records | Version views summed by exactly ten families; no unique-human or adoption inference |
| Software Heritage | All 10 fixed GitHub origin latest-visit queries HTTP 200 and report `full` | Stored visit dates precede query; not evidence that a fresh preservation visit happened this run |
| 34 established surfaces | 25 HTTP 200, 3 HTTP 403, 2 HTTP 404, 4 no HTTP response; one of the 25 HTTP 200 responses truncated at 2 MB | A successful HTTP response does not prove that the target software is indexed or that a review is complete |
| WorkflowHub | Four workflow JSON metadata pages return HTTP 200, versions 9 / 9 / 1 / 2 for 2332 / 2334 / 2337 / 2347 | No current Activity views/downloads derived from this JSON capture |

## Comparable changes and interactions

- November 12 same fixed-ten Zenodo version cohort: **3,836 → 3,849 views (+13)**, **37 → 37 downloads (0)**; uses the version-level statistic rather than re-adding each record's attached family aggregate
- November 12 ORCID: **17 → 18 groups**, **115 → 117 summaries**; DataCite source-name 90 → 92. Account-origin of the 13 source-name-null entries remains unverified in this capture
- November 8 exact same 92-DOI OpenAIRE query cohort: **59 → 84 query-positive DOI requests (+25)**; ten November 10 new version DOIs are separately 10/10 positive, giving 94/102. These are endpoint observation changes, not first-index or ingestion-latency timestamps
- [RSD issue #1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870) is **CLOSED** since 2026-10-16T12:11:19Z; [#1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871) remains **OPEN**. Closure does not prove deployment of the exact reported fix
- [RSE metadata PR #498](https://github.com/rseng/software/pull/498) remains **OPEN / not merged**; no maintainer acceptance or production index coverage is asserted
- RSD's eleven software public URL responses are HTTP 200, but eleven public software representations remain **ten fixed software objects + separately named CONTROL**, not an eleventh study sample

## Evidence and failure discipline

- The **first** cloud-run [43265103686](https://github.com/lostlight530/research-software-identity-audit/actions/runs/43265103686) and corrected [43265914410](https://github.com/lostlight530/research-software-identity-audit/actions/runs/43265914410) are separately preserved as run receipts; the second fixes nullable ORCID source-field interpretation and canonical DOI comparison, not silent overwriting of earlier source results
- The corrected source ledger has 458 per-request UTC windows, URL locators, HTTP/error outcomes, response SHA-256 and minimized field extracts. The source ledger SHA-256 is `d52b84134f0e88f30c71cee87d1718ae34d34b0863726c35cc4c271c06e8084e`
- **No unmodified origin HTTP body bytes** were committed, so byte-exact historical replay is not available from the public package. Credential, private-email, cookie/session and IP pattern scans returned no matches in the minimized payload
- Current failures remain visible: SciCrunch and allied resolvers timeouts, ScreenIT network error, dkNET / InterLex / N2T 403, HAL / Identifiers.org 404, EDAM payload truncated; none proves missing research identity
- No authenticated ORCID/OpenAIRE/RSD account claim changes or private institution correspondence were performed, and no external software adoption or scientific endorsement was inferred

**Disposition:** `PARTIAL_WITH_VERIFIED_PUBLIC_IDENTITY_DELTAS_AND_PRESERVED_UNKNOWN`. This closes the bounded public cloud recheck without changing archived raw history, sample size, preregistration or introducing new Release/DOI.
