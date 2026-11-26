# October 31 bounded research identity and infrastructure recheck

**Class:** append-only diagnostic monitoring, **NOT** a scheduled prospective observation, OSF amendment, new release initiated by this audit, or complete 60-unit census  
**Logical day:** 2026-10-31 Asia/Shanghai  
**Compiled:** 2026-10-31T00:18:02.002Z (UTC, report-construction clock only)  
**Base CONTROL main:** [385f0bce3af8c465c74408df76789a6cc8dec1f1](https://github.com/lostlight530/research-software-identity-audit/commit/385f0bce3af8c465c74408df76789a6cc8dec1f1)  
**Corpus authority:** [object-manifest.csv](../../../corpus/object-manifest.csv), **RS01–RS10** only; CONTROL is not RS11

## Proven current GitHub release delta

The direct GitHub connector read all 11 `main` refs, 11 complete published-Release lists (`per_page=100`), 11 Git tag-ref lists, and open PRs. Compared with the [October 30 44-tag evidence record](../../2026-10-30/04-tag-ref-and-source-shape-recheck/README.md), each fixed repository has **one additional published Release and one matching current Git tag**: `v2026.10-30-evidence-snapshot`, published October 30 **15:44:08–15:44:57 UTC**, after the prior audit commit. Fixed-sample published Release rows **40 → 50**, fixed tag refs **40 → 50**, CONTROL remains **4 releases and 4 tags**. Total now 54 across 11 engineering repos, **not 54 study objects or 54 DOI identities**. Original previous dated evidence is not changed.

At read, four unrelated producer PRs were open: [welcome #871](https://github.com/lostlight530/welcome-to-github/pull/871), [zero #761](https://github.com/lostlight530/zero-entropy-lab/pull/761), [China #218](https://github.com/lostlight530/china-agentic-observatory/pull/218), [global #222](https://github.com/lostlight530/agentic-frontier-observatory/pull/222); CONTROL had zero open PRs. These are not merged or modified by this review. Exact new release, Zenodo identity and source URLs are in [the 10-row cohort ledger](new-release-cohort.csv).

## Cross-platform version-identity confirmation

Ten exact Zenodo `/api/records/<old-version-id>/versions/latest` URLs returned selected representations acquired on **2026-10-31 UTC** with **10 new Zenodo record IDs and version DOIs**, each identified as the October 30 tag within its original 10 concept families. Ten corresponding DataCite DOI API URLs returned selected records acquired on the same UTC day, with matching DOI identities and creator ORCID. These are **ten new version identifiers of ten existing objects**, not ten new sample objects. GitHub published timestamps and Zenodo record created timestamps are distinct provider event fields, not independent measured ingestion latency. DataCite registration event timestamps were not independently extracted.

Two selected new DOI OpenAlex exact endpoints returned HTTP 404, while two OpenAIRE selected new DOI queries timed out. They are **bounded access/query outcomes**; the other eight new DOI identities have **not** been independently checked at these two discovery providers. No new ORCID structured group recount, Software Heritage ten-origin census, total Zenodo engagement rollup, global citation count, or independent scholarly adoption claim is made.

## Existing 34-surface checklist reconciliation

[The 34-row source ledger](surface-attempts.csv) repeats the existing inventory's exact representative URLs, **not 34 full per-object checks**. Public extractor results: **3** acquired on October 31 UTC (RSE GitHub PR endpoint, RS01 Zenodo selected latest, RS01 GitHub Releases endpoint), **25** older cached/day-granular extracts, and **6** fetch failures (ASWG connect, dkNET 404, InterLex 404, EDAM extraction error despite HTTP 200, Identifiers.org 404, N2T 403). HAL returned an October 30 **Anubis bot challenge** rather than HAL research metadata. Independent connected GitHub calls additionally check PR #498 and all 11 release/tag lists. The October 30 34-surface source ledger remains unchanged; these counts describe the *October 31 retrieval attempt representation*, not 34 fresh origin responses. No API headers, byte-identical external raw responses, per-request precise retrieval timestamps or cache-bypass proofs were saved.

Other retained results are appropriately **STALE/UNKNOWN**: ORCID Works acquired Oct 27, SWH Oct 27, OpenAIRE older DOI Oct 27, OpenAlex author Oct 6, OSF registration Oct 12, DataCite registration DOI Oct 30. The two known public OSF Schema Response versions were accessible only as **Oct 29** acquired extracts in this review; the existing [original vs approved revision comparison](../../2026-10-30/01-osf-schema-response-version-reconciliation/README.md) is not overwritten or called fresh.

## Institutional interaction and engineering decision

Direct GitHub source: [RSD #1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870) remains **closed** since 2026-10-16T12:11:19Z (upstream v6.7.3 documented a fix), but researcher production deployment and original reproduction-path retest remain **UNVERIFIED**; [RSD #1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871) remains **open**; [RSE #498](https://github.com/rseng/software/pull/498) remains **open and unmerged**, without submitted review evidence. No new institutional affiliation, formal endorsement, or independently verified interaction progress was inferred.

**Contract gate:** ten objects × six fixed layers = **60 object-layer analytical units per eligible scheduled point**, while ten × seven operational platforms = **70 potential platform checks**, not 70 analytical units. The [schedule](../../../schedule/README.md) still has **no concrete offsets**. This October 30 ten-release cohort requires a bounded eligibility assessment, but is **not by itself proof of a declared scheduled prospective run**. **Zero prospective observation cells** were written. Original OSF registration, later approved revision, baseline, source evidence, schema, manifest and earlier records remain unchanged.

**Decision:** `MATERIAL_VERSION_IDENTITY_DELTA` for directly checked new GitHub release/tag, Zenodo version and DataCite DOI identities; `PARTIAL / UNKNOWN` for full seven-platform and 34-surface same-day census; `NO_CHANGE_REQUIRED` for source/code or metadata correction. No new Release, Tag, DOI, externally edited account, schedule or inference model created by this audit.

**Provenance limitation:** provider-returned `published_at` / `created` fields are event clocks; extractor `acquired_at` is **UTC-day truncated** and not origin-freshness proof; `compiled_at_utc` is only report-construction time. The [machine summary](record.json) and exact source URLs in both ledgers support independent rechecks. This note does not claim to retain complete original source HTTP bytes, full response headers or exact per-request retrieval timestamps.
