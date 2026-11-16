# Frozen research contract

## 中文专业对应与范围 / Chinese subject counterpart and scope

**实质研究对象 / Exact subject:** OSF 冻结研究方案覆盖 RS01–RS10、六层、每计划时点 60 个对象层单位，绝不把七平台 70 项检查替代原始设计

**English owning title:** Frozen research contract

**冻结保护 / Freeze guard:** 本段只是原有条款的非规范性语言指引，不构成对 OSF Registration 的写入、增补、修订或新计划时点 / This is a non-normative translation aid, not an amendment to the registered contract

**单位与版本 / Unit and version:** 读者需要同时确认 RS01–RS10、六层与七具体平台的不同口径，以及原始研究、版本化软件发行、实时外部平台数据的独立身份，任何未知保持未核实 / Keep distinct denominators, exact release identity, observation clocks, unknown source responses and the frozen preregistered boundary

| English original section / 原文章节 | 中文定位 / Chinese mapping |
| --- | --- |
| Frozen boundaries | 冻结的研究边界 |
| Evidence rule | 证据认定规则 |
| Schedule representation | 时间计划与真实执行 |
| Authority order | 权威先后关系 |
| Clause-level Overview crosswalk (2026-10-08) | 对应的受限研究过程与原始记录 |
| Dated OSF Schema Response version reconciliation (2026-10-30) | 对应的受限研究过程与原始记录 |

**历史不回写 / Non-retroactivity:** 此语言补充不改变原始 OSF、历史样本、注册版本、计数或先前失败记录 / This explanatory layer does not modify any historical observation or external registration


Canonical research object:

- **Title:** Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures
- **OSF Registration:** https://osf.io/5b329/overview
- **DOI:** https://doi.org/10.17605/OSF.IO/5B329
- **Associated OSF Project:** https://osf.io/wa5v8
- **Registered:** 2026-10-05
- **Registration license:** CC BY 4.0

This file maps the repository runtime to the frozen OSF registration. It does not replace or silently amend the registered object.

**2026-11-03 original-versus-approved-version authority:** [OSF Registration and Schema Response governance reconciliation](osf-registration-version-governance-2026-11-03.md) explicitly distinguishes the October 5 original response, October 6 approved `344-83` exploratory wording revision, current GitHub operational mapping and the unmodified 60-unit contract. This is an additive interpretation/authority index, **not** an OSF write, amendment, or claim of fresh full-byte origin-capture.

## Frozen boundaries

- fixed corpus: 10 research software objects
- fixed scope: 6 scholarly-infrastructure layers
- observation unit: software object × infrastructure layer × observation time point
- 60 object-layer units per scheduled observation point
- prospective, longitudinal, repeated-measures, observational, descriptive design
- no causal interpretation
- no inferential statistical model
- no imputation
- no global composite infrastructure score
- historical observations remain a fixed baseline
- prospective observations begin only after registration and the first eligible new release event
- exploratory/post hoc work remains explicitly labeled
- amendments and deviations are logged rather than folded back into the original contract

## Evidence rule

Missing, unresolved, rate-limited, partial, failed, or unsuccessful retrieval must not be promoted into evidence of absence unless the relevant infrastructure's observable contract explicitly supports that interpretation.

## Schedule representation

The preregistration commits the study to predefined/scheduled observation points. The OSF interface used at submission did not provide a dedicated field for enumerating concrete operational offsets.

Concrete execution times therefore belong in `schedule/` with their own timestamp and provenance. Repository-side operational schedules must not be retrospectively represented as literal preregistered offsets unless independently supported by the frozen registration.

## Authority order

1. Frozen OSF registration controls claims about what was preregistered.
2. Dated amendments control explicit post-registration changes.
3. Dated operational specifications control implementation details that do not rewrite the substantive contract.
4. Exploratory work remains labeled exploratory/post hoc.

## Clause-level Overview crosswalk (2026-10-08)

The researcher's supplied OSF Overview was compared against the live repository without rewriting the frozen registration or historical captures. The [clause-level crosswalk](osf-overview-crosswalk-2026-10-08.md) maps RQ1–RQ5, the 12 measured-variable categories, six descriptive derived analyses, prior foreknowledge, no imputation/exclusions, prospective eligibility, stopping and the experimental/exploratory boundary.

In that supplied Overview, `Other planned analysis` is marked **Updated**. Without an independently preserved OSF version history or edit timestamp, the wording must **not** be asserted to have belonged to the originally frozen registration. Existing benchmarks remain exploratory/post hoc regardless of that unresolved revision history.

This addition is explanatory, **not** an amendment or declaration that a prospective observation window has started.

## Dated OSF Schema Response version reconciliation (2026-10-30)

**Subsequent evidence update, not a new or amended frozen contract:** the original October 8 Overview crosswalk correctly stated that it lacked direct OSF revision evidence *at that time*. The [October 30 version-by-version public API reconciliation](../monitoring/2026-10-30/01-osf-schema-response-version-reconciliation/README.md) now identifies the [original Schema Response](https://api.osf.io/v2/schema_responses/6ac3ae5e6da32e3d0576ed72/) and a [later approved revision](https://api.osf.io/v2/schema_responses/6ac4c12fed97b8b77ce88a9c/). Across **29** `revision_responses` keys, the extracted representations have **one changed value, `344-83` (Other planned analysis)**. Primary questions, fixed corpus/layers, counting, measured/derived variables and primary analysis wording did **not** differ in that field-level comparison.

The original `344-83` generically permitted clearly labeled exploratory/post hoc analyses; the October 6 revision made family benchmarking, engagement-metric sensitivity and tie-aware rank/percentile examples explicit. These added examples were **not present in the original version** and must not be represented as initially preregistered primary analyses. The later revision's justification is retained separately from the observed text diff. Exact revision timestamps, source URLs, field values and third-party extractor limits are in the linked record.

The original October 8 crosswalk and all historical monitoring files remain as-of records rather than silently rewritten. The schedule still has no declared concrete offsets, and neither this new provenance finding nor the OSF revision initiates a prospective observation wave.
