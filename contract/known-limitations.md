# Known limitations and contract ambiguities

## 中文专业对应与范围 / Chinese subject counterpart and scope

**实质研究对象 / Exact subject:** 已知局限需要保持类型化未知，缺少历史来源字节或第一个索引时间时不可推导传播延迟

**English owning title:** Known limitations and contract ambiguities

**单位与版本 / Unit and version:** 读者需要同时确认 RS01–RS10、六层与七具体平台的不同口径，以及原始研究、版本化软件发行、实时外部平台数据的独立身份，任何未知保持未核实 / Keep distinct denominators, exact release identity, observation clocks, unknown source responses and the frozen preregistered boundary

| English original section / 原文章节 | 中文定位 / Chinese mapping |
| --- | --- |
| KL-001 — Concrete observation offsets are not enumerated in the frozen text export | 对应的受限研究过程与原始记录 |
| KL-002 — Live endpoints are not historical proof | 对应的受限研究过程与原始记录 |
| KL-003 — Infrastructure clocks and object semantics differ | 对应的受限研究过程与原始记录 |
| KL-004 — External access conditions affect observation | 对应的受限研究过程与原始记录 |
| KL-005 — Analytical layers and operational platforms differ | 对应的受限研究过程与原始记录 |
| KL-006 — Supplementary institution-facing surfaces are outside the frozen platform vocabulary | 对应的受限研究过程与原始记录 |
| KL-007 — Summary-level imports do not substitute for raw request evidence | 对应的受限研究过程与原始记录 |
| KL-008 — Zenodo version-level and attached-family counters may disagree | 对应的受限研究过程与原始记录 |
| KL-009 — Public institutional listing and RRID index have distinct authority | 对应的受限研究过程与原始记录 |
| KL-010 — OpenAlex author profile response conflict | 对应的受限研究过程与原始记录 |

**历史不回写 / Non-retroactivity:** 此语言补充不改变原始 OSF、历史样本、注册版本、计数或先前失败记录 / This explanatory layer does not modify any historical observation or external registration


This ledger records known representational or operational limitations without rewriting the frozen study contract.

## KL-001 — Numerical observation offsets are not enumerated in the accessible registered response

OSF 5b329 is a formal, approved prospective longitudinal observational registration. Its current approved Schema Response (`6afdcc3a7fb0a89b0e3dd7e4`, approved 2026-11-18) specifies the event-anchored prospective window: begin after the first eligible post-registration release event, use predefined follow-up points, and stop after the final preregistered point has been attempted across RS01–RS10 and all six layers. The approved revision explicitly states that the observation schedule was not changed.

The accessible structured registration response does not enumerate numerical offsets or a numbered timepoint list. This is a limit on the precision of the schedule representation available in that response; it is **not** evidence that the formal prospective research contract is absent or merely diagnostic. Do not downgrade the registration status on this basis, and do not invent offsets.

**Handling:** preserve the registered event eligibility, predefined-follow-up, and stopping rules. Any separately declared operational timepoint detail must have its own prior declaration timestamp and provenance and must not be described as literal OSF preregistration text unless the OSF source supports that claim.

## KL-002 — Live endpoints are not historical proof

A later public API or web response does not necessarily reconstruct an earlier response.

**Handling:** keep captured historical evidence distinct from present live state.

## KL-003 — Infrastructure clocks and object semantics differ

Repository releases, DOI registration, author-registry ingestion, preservation, and discovery can use different clocks and object types.

**Handling:** calculate latency only when timestamps are directly observed and temporally comparable; compare identity fields only when semantically equivalent.

## KL-004 — External access conditions affect observation

Rate limits, pagination, platform errors, and endpoint availability can prevent complete retrieval.

**Handling:** preserve the attempt and reason; do not drop the cell or infer absence.

## KL-005 — Analytical layers and operational platforms differ

The frozen research contract defines six scholarly-infrastructure layers. Operational evidence collection may use multiple concrete platforms within one layer. In the current mapping, OpenAIRE and OpenAlex are separate platforms under the single preregistered `discovery_graph` layer. Platform-level checks improve observability but do not change the six-layer contract or the 60 object-layer units per scheduled timepoint.

## KL-006 — Supplementary institution-facing surfaces are outside the frozen platform vocabulary

Research Software Directory, SciCrunch/RRID Registry, OSF/Internet Archive relationship surfaces, HAL, and similar institutional or registry surfaces may provide useful identity, curation, preservation, or relationship evidence without belonging to the seven operational platforms currently mapped to the frozen six-layer research contract.

**Handling:** record them as supplementary surfaces unless a future explicit amendment changes the operational study contract. Their presence must not silently change the 10 × 6 = 60 preregistered object-layer denominator or relabel the 10 × 7 = 70 possible platform checks.

## KL-007 — Summary-level imports do not substitute for raw request evidence

A conversation-level or narrative audit summary may reference request logs, response bytes, checksums, scripts, or row-level matrices that are not themselves available to the repository updater.

**Handling:** preserve the summary with explicit provenance, materialize only derivations supported by supplied fields, mark unavailable raw artifacts as evidence gaps, and do not fabricate missing request/response evidence.

## KL-008 — Zenodo version-level and attached-family counters may disagree

In the October 10 independent 32-version public-field extraction, the same RS07 concept family had version-local `version_views=45+33+7=85`, while one month-close version record attached `stats.views=186` and `stats.unique_views=106` versus sibling attached aggregate fields `85/82`. Count **versions by their local fields** under the explicitly declared exploratory method; keep the conflicting family-aggregate fields as observed discrepancies. **Do not** add 101 as extra family traffic, backfill any historical period, or claim a proven internal synchronization mechanism.

The extractor supplied bounded execution windows rather than original HTTP bytes or per-request server times, so this secondary validation is **not** byte-identical evidence. See [2026-10-10 reviewer record](../monitoring/2026-10-10/02-reconciliation/independent-version-verification.md).

## KL-009 — Public institutional listing and RRID index have distinct authority

The public RRID search newly verified `SCR_029105` indexed for the audit-control repository. A dated earlier record still says `pending`; neither date supplies a direct timestamp for the actual indexing transition. RSD public person/project/software records, rseng open PR #498, OSF registration, DataCite DOI relations, RRID indexing and authenticated platform-account access are non-equivalent claims. No institution's scientific endorsement or employment/partnership follows without independent evidence. Details: [institutional ledger](../scholarly/infrastructure-review-2026-10-10.md).

## KL-010 — OpenAlex author profile response conflict

A full-profile query returned `works_count=30` with `updated_date=2026-10-01T12:39:15` while a field-selected query returned `works_count=16` with `updated_date=2026-10-09T12:31:04`. Previous profile and author-Works counts were time-specific and are not rewritten to match one of these incompatible live surfaces. Save exact query shape, source snapshot and retrieval window on any further comparison. Cause is **UNRESOLVED**, not automatically indexing loss or newly generated works.
