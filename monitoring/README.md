# Monitoring

This directory stores useful measurements that occur outside the eligible
prospective dataset.

A monitoring record can be methodologically valuable without being promoted to a
scheduled prospective observation.

Use this area for:

- pre-eligibility propagation checks;
- infrastructure self-observation;
- post-baseline state checks before the first eligible fixed-corpus release;
- diagnostic captures whose timing does not satisfy the operational prospective schedule.

Monitoring records must preserve true retrieval time and must not be relabeled
later as preregistered prospective observations.


Post-release reconciliation records may also be stored here when they observe
the research-control repository or scholarly infrastructure before an eligible
fixed-corpus release begins the prospective dataset.

## Records by observation day

- [2026-10-06 / 01-wave-01](2026-10-06/01-wave-01/) — first pre-eligibility monitoring, not a preregistered wave
- [2026-10-06 / 02-openaire-link-attempt](2026-10-06/02-openaire-link-attempt/) — manual link attempt with bounded outcome
- [2026-10-06 / 03-reconciliation](2026-10-06/03-reconciliation/) — later reconciliation, original timestamps retained
- [2026-10-07 / 01-facility-audit](2026-10-07/01-facility-audit/) — supplied cross-platform audit and mapping reconciliation
- [2026-10-08 / 01-morning-recheck](2026-10-08/01-morning-recheck/) — morning monitoring plus separately imported retained evidence

For path rules and the complete old-to-new inventory, see [naming and migration](NAMING.md) and [path mapping](path-migration-2026-10-08.csv).

The date is the record's source-observation date, not necessarily its retrieval or evidence-import date. Ordinals order packages within a date and are **not** prospective-wave identifiers.

- [2026-10-09 / 01-facility-recheck](2026-10-09/01-facility-recheck/) — Independent facility and counter recheck

## October 10 diagnostic and interpretation records

- [2026-10-10 / 01-zenodo-surge-recheck](2026-10-10/01-zenodo-surge-recheck/) — source collector's original point-in-time Zenodo counters and the separately attributed corrective review; this is **not** an eligible prospective observation
- [2026-10-10 / 02-reconciliation](2026-10-10/02-reconciliation/independent-version-verification.md) — independently reviewed 11 concept families / 32 versions, the [32-row extract](2026-10-10/02-reconciliation/version-counters-independent.csv), and unresolved RS07 aggregate-field disagreement

The 01 original report and the 02 earlier `interpretation.md` have distinct author/provenance identity. The independent reviewer **does not adopt** the earlier suggestion of an identified Zenodo aggregation mechanism; it is a working hypothesis. Across October 9–10 the retained prior capture does not provide a matching 32-version enumeration, so per-version historical interval increments remain **NOT_DERIVABLE**. For the bounded version-counting procedure see [counting rules](../schema/counting-rules.md#supplementary-zenodo-version-family-reconciliation-2026-10-10).

- [2026-10-10 / 03-openalex-work-aggregation](2026-10-10/03-openalex-work-aggregation/README.md) — independent author-filtered OpenAlex Works listing (**18 distinct DOI/Work records**), including six version-specific WorkflowHub Works; DataCite v4 DOI visibility vs OpenAlex v4 query non-observation, ORCID structural-count gap, and author profile counts 16/30 kept distinct. This is a **diagnostic** aggregation record, not a new RS object or prospective observation.

## October 11 independent full-version counter recheck

- [2026-10-11 / 01-zenodo-33-version-recheck](2026-10-11/01-zenodo-33-version-recheck/README.md) — later independent verification of the user-reported **October 10 23:54** Zenodo counting guide: 11 concepts, 33 direct version records, 1,933 fixed-ten views / 8 downloads, 74 independent control views / 3 downloads, and an observed resolution of the earlier RS07 attached-family field conflict. The original source report and later API capture remain distinct; historical byte-level replay and internal traffic/aggregation causes remain **UNVERIFIED**.

## 2026-10-13 noon independent review — research-control repository only

- [2026-10-13 / 01-control-noon-recheck](2026-10-13/01-control-noon-recheck/README.md) — **actual retrieval 12:47:55.192–12:51:01.217 Asia/Shanghai**, not 12:00:00. Independent seven-operational-platform control-only review; [37 source/attempt ledger rows](2026-10-13/01-control-noon-recheck/platform-attempts.csv), [9 direct Zenodo version-stat field rows](2026-10-13/01-control-noon-recheck/zenodo-version-attempts.csv), and a bounded [machine summary](2026-10-13/01-control-noon-recheck/record.yaml). Zenodo first returns conflicting attached family counters **91/51/74** then independent repeated three-version reads and two enumerations all agree **91 views, 87 unique-view count, 3 downloads**. OpenAIRE exact latest version DOI visible, exact concept PID query zero; OpenAlex author list **24** while profile `works_count` read forms still conflict. SWH, ORCID group reconstruction, GitHub traffic and OSF structured read gaps retained. This adds **no RS11**, releases, retrospective rewrite or eligible prospective observation.

## 2026-10-13 evening fixed-corpus public release gate

- [2026-10-13 / 02-fixed-corpus-release-gate](2026-10-13/02-fixed-corpus-release-gate/README.md) — 19:44 Asia/Shanghai independent public GitHub Release-list queries for all fixed `RS01–RS10`: each latest returned published release dates to October 4, so no new post-registration **public GitHub Release** observed. Ten public Git tag-list calls were connector-blocked and remain `NOT_VERIFIED`; this does not establish an exhaustive eligible-event absence or start the prospective study. The [20-attempt source ledger](2026-10-13/02-fixed-corpus-release-gate/source-attempts.csv) retains the exact source URLs and bounded retrieval windows.

## October 14 preflight integrity and fixed-ten tag-ref check

- [2026-10-14 / 01-preflight-integrity-recheck](2026-10-14/01-preflight-integrity-recheck/README.md) — read-only preflight: all ten current GitHub Release **and Git tag-ref** lists parsed (previous day's unsupported tag path remains historically blocked), no new public release observed; separately retained Zenodo bare-field inconsistency versus later family/version match (94/90/3), DataCite reverse-link asymmetry, OpenAlex author query/profile differences (26/24/30), and OSF's publicly displayed Oct 6 update notice without claiming an original-to-updated field diff. External extractor rate-limit blocks preserved; **not prospective**.
