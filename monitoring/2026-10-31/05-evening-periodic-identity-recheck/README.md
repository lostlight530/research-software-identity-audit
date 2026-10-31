# October 31 evening periodic research-software identity and infrastructure recheck

**Classification:** append-only bounded diagnostic, not a scheduled or eligible prospective study observation, not a seven-platform 70-cell source-origin census, not an OSF amendment, and not a new Release/Tag/DOI

**Logical date:** 2026-10-31 Asia/Shanghai. **GitHub source read:** 2026-10-31T15:08:06Z–15:08:25Z; exact ten-repository compare pass 15:14:05Z–15:14:06Z. **Previous verified control checkpoint:** [`220ebe2513166e503f743f09e7f9f80de01e77cb`](https://github.com/lostlight530/research-software-identity-audit/commit/220ebe2513166e503f743f09e7f9f80de01e77cb), the merged PR #78. The current research-control HEAD was the same when creating this monitoring branch. Subsequent commits made *by this event* must not be used as its input snapshot.

## 1. Exact GitHub delta: substantial engineering maintenance, no new scholarly release

All eleven independently connected GitHub `main` branches, Open PR lists and published Release lists were read. Compared with the previous [pinned eleven-ref ledger](../../../docs/research-core-main-heads-2026-10-31.csv):

- **10/10 fixed sample source `main` SHAs changed**, each strictly ahead of its previous SHA with **0 behind**; the [individual compare ledger](github-main-deltas.csv) contains all original/current 40-character SHAs, ten compare URLs, timestamps, 109 accumulated additional *main-reachable Git commits* and 44 affected file paths counted per-repository two-tree diff. Those 44 path differences are **not** 44 new release artifacts, DOI records or independent objects
- Latest new `main` commits were **2026-10-31 14:51–14:52 UTC** (22:51–22:52 Asia/Shanghai). Checked diffs concern research daily/monthly manifests, historical audit/source-custody notes, relations, errata and maintenance documentation. The exact commits and paths are in GitHub compare results, not merely inferred from an Actions success signal
- **0 open PR** across all eleven at the pass; ten fixed repositories still have exactly **5** published Releases apiece with latest **`v2026.10-30-evidence-snapshot`** (October 30 15:44 UTC); CONTROL still has **4** published Releases, latest `v2026.10-evidence-integrity`; CONTROL `main` unchanged at the baseline SHA
- This is a **`MATERIAL_GITHUB_MAIN_DELTA`** in the software/maintenance plane, but **`NO_NEW_PUBLISHED_RESEARCH_RELEASE`** in the tested published-Release plane. No claim that the 109 intervening commits were all written by a particular agent or caused specific scholarly metadata changes

## 2. Core seven operational platforms, actual bounds

[Ten-object platform/DOI/visit crosswalk](core-platform-identity-recheck.csv), with exact URLs, original DOI relationships and response-age fields:

| Platform | Checked selection | Source-supported result |
| --- | --- | --- |
| GitHub | All RS01–RS10 and independent CONTROL current `main`, Open PR, published Releases; ten direct SHA comparisons | **10 changed HEADs**, CONTROL unchanged; Releases unchanged |
| Zenodo | Exact ten October 30 version record URLs | **10 extracted record identities**, same existing exact record IDs/concept families and version DOIs; extractor acquisition UTC-day **2026-10-31**, not per-origin fresh receipt |
| DataCite | Exact same ten version DOI API URLs | **10 extracted DOI identity matches**, acquired UTC-day **2026-10-31**; unchanged existing DOI identities, not ten newly minted DOIs |
| ORCID | Registered author Works representative endpoint and existing retained 12:00 corpus audit | Third-party extraction acquired **2026-10-27**; **NO fresh structured group recount**, so old **17 groups/104 summaries** cannot be reinterpreted as evening values |
| Software Heritage | Latest visit endpoints for all 10 GitHub origins | **10 extracted latest visit responses contain `status=full`** with non-null snapshot IDs; one extraction acquired October 27, other nine acquired October 31 (UTC day only). **Provider visit dates range September 16–October 30**, preceding today's new `main` commits; this does **not** prove today's HEADs archived |
| OpenAIRE | Exact DOI software-query representation for 10 new-version DOIs | **10 query representations acquired on October 31**, but some excerpts echo input DOI and therefore **do not establish a normalized ten-hit identity census**; original October 31 57 matched DOIs/87 record IDs belongs to its earlier 473-attempt collector |
| OpenAlex | Exact DOI-to-Work lookup for 10 new-version DOIs | **10 extraction representations acquired on October 31**, several return canonical **concept DOI** for a version DOI query. Do not count returned concept-family Works as ten distinct version DOI Works. Earlier author-profile **32 Works** remains a separate older read, **not freshly recounted** |

External extractor calls were executed on October 31 within **15:10:31–15:11:59 UTC**, while `acquired_at` is **day-truncated** and may represent cached source. Relevant extraction receipt IDs are in [machine summary](record.json). **Tool receipt ≠ origin-HTTP response hash or new provider ingestion timestamp**. The OpenAlex concept-versus-version discrepancy is an identity/normalization boundary, not a demonstrated scientific inconsistency or evidence that a version is absent.

**Usage counters remain noncomparable:** the separately preserved [13:41 Zenodo 55-version source package](../04-zenodo-all-version-statistics/README.md) reports for RS01–RS10 **3,200 views, 2,307 summed unique-view counters, 17 downloads, 16 unique-download counters**. The [12:00 institutional capture](../03-independent-institutional-statistics/README.md) reports **88 DOI, 17 ORCID work groups / 104 summaries, 32 OpenAlex author Works** and OpenAIRE **57 DOI matches / 87 record IDs** under their respective query semantics. This evening **did not recollect equivalent complete current usage/group counts**, so **no numeric engagement delta is computed**, and no unique-people/adoption claim is made.

## 3. Existing 34 surface inventory — access-status comparison only

An independent evening fetch of the [exact 34 existing representative URLs](surface-access-recheck.csv) occurred in a client tool envelope **2026-10-31T15:09:44.408Z–15:10:21.760Z**. It returned **2 connected current GitHub structured reads, 2 Oct 31 UTC-day extracted representations, 24 older cached/day-labeled representations and 6 access failures**. These are the **same access classes** as the immediately preceding [independent access ledger](../../../docs/research-independent-34-surface-access-2026-10-31.csv), not proof that underlying source content never changed.

The six failures remain explicitly retained: ScreenIT ASWG connection error, dkNET 404, InterLex 404, EDAM fetch/extraction error despite HTTP 200, Identifiers.org 404 and N2T 403. HAL returns an anti-bot page, not a HAL metadata confirmation. The **34 rows include identity registries, services, resolvers and standards**, not 34 independent scientific institutions or complete checks of every research object.

## 4. OSF original/revised contract, external interactions and guardrails

The [frozen registration](https://osf.io/5b329/overview) and [repository mapping](../../../contract/preregistration.md) are unchanged. The original-vs-later approved OSF Schema Response comparison previously found **29 compared keys; 28 unchanged, one exploratory `344-83` changed**. This pass separately saw a **2026-10-31 UTC-day acquired list** of OSF Schema Responses, while the two exact individual response representations remained extracted **2026-10-29**. This does not retrospectively revise the frozen OSF study or independently recapture byte-identical original versions.

Direct current upstream GitHub checks:
- [RSE Software Encyclopedia #498](https://github.com/rseng/software/pull/498): **OPEN**, **not merged**; no verified institutional decision change
- [RSD #1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870): **CLOSED**, fix described in published **v6.7.3**; [RSD #1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871): **OPEN**
- Additional published upstream releases **v6.7.4** (October 26: security, OpenAlex scraper, Java) and **v6.7.5** (October 27: security/RLS) now visible in the API; these releases **pre-date this evening's audit** and are not evidence of deployment, original reproduction-path retest, direct contributor acceptance, or a new result caused by the researcher

**Analytical denominator** stays **RS01–RS10 × six registered infrastructure layers = 60 object-layer units per eligible timepoint**, while **ten × seven operational platforms = 70 possible checks only**. OpenAIRE/OpenAlex both map to `discovery_graph`. CONTROL and supplementary life-science software are not new study objects. [The schedule](../../../schedule/README.md) still declares no concrete offsets, so **zero** eligible prospective cells were added; no baseline, historical raw record, original release, schema or OSF revision was modified.

## 5. Disposition

- **Observed change:** `MATERIAL_GITHUB_MAIN_DELTA` (10 fixed main SHA changes / 109 reachable commits / 44 per-repo two-tree changed paths)
- **No scholarly release change:** `NO_NEW_PUBLISHED_RESEARCH_RELEASE`; all sampled version DOI identities match previously recorded IDs in extracted day-granular public representations
- **Unchanged access/interaction classes:** `NO_MATERIAL_ACCESS_CLASS_CHANGE`, `NO_NEW_EXTERNAL_PR_MERGE_VERIFIED`
- **Limitations:** `PARTIAL / UNKNOWN` for fresh ORCID group counts, OpenAlex per-version identity/author profile, OpenAIRE complete hit normalization, current Zenodo usage deltas, source-origin byte custody, SWH replication of latest HEAD, platform indexing latency and upstream production deployment
- **Repair:** `NO_SOURCE_OR_CONTRACT_CORRECTION_REQUIRED`. This is an **additive** monitoring/identity/provenance record only, justified by the actual GitHub main change; no synthetic source success and no unnecessary Release/DOI

**Evidence chain:** exact GitHub source/ref and commit compare → selected external source URLs and extraction-acquisition age → source-scoped CSV → machine summary → this bounded interpretation. All earlier monitoring, evidence manifests and corrections remain untouched.
