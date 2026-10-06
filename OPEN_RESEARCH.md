# Open Research / 开放科研

Status: durable open-research production guide  
Scope: preregistered research execution, evidence, provenance, correction, release, and scholarly-metadata boundaries

## Language policy / 语言政策

English is the canonical/default language of this contract. Chinese text may be
used for accessibility and interpretation. Repository evidence and the frozen
OSF registration remain authoritative over prose summaries.

英文为本开放科研契约的默认规范语言；中文可用于辅助理解。仓库证据与冻结的 OSF
注册始终高于解释性文字。

## Authority

This repository does not replace the preregistration.

```text
OSF registration
= frozen research contract

GitHub main
= live operational research runtime

evidence + provenance
= support for observations

analysis
= bounded derivation from retained observations

Zenodo
= immutable archival/citation snapshots
```

If repository implementation conflicts with the frozen preregistration, the
conflict must be recorded as an amendment/deviation issue rather than silently
rewriting the contract.

## Research object boundary

The fixed research corpus is exactly `RS01`–`RS10`.

`research-software-identity-audit` is research-control infrastructure. It is
not `RS11`.

The preregistered analytical design remains:

```text
10 objects × 6 infrastructure layers
= 60 object-layer units per scheduled timepoint
```

Operational evidence collection may query seven concrete platforms. OpenAIRE
and OpenAlex remain distinct platforms under the single preregistered
`discovery_graph` layer.

```text
70 possible object-platform checks
!=
70 preregistered analytical units
```

## Research-production method

A substantive research unit should make recoverable, where applicable:

1. research question;
2. preregistered or explicitly exploratory status;
3. fixed object, version, platform, and time identity;
4. evidence/source basis;
5. procedure actually executed;
6. raw observation;
7. verification or counterexample check;
8. derived result where valid;
9. bounded interpretation;
10. uncertainty and retest condition.

Unknown, blocked, rate-limited, partial, degraded, failed, unresolved, and
no-conclusion states are legitimate outcomes.

Do not manufacture a complete state matrix merely for presentation quality.

## Baseline and prospective separation

The initial baseline cutoff is:

`2026-10-05T23:59:59+08:00` (`Asia/Shanghai`).

Retrospective baseline reconciliation may occur later, but the true retrieval
timestamp and reconstruction status must remain explicit.

```text
live endpoint != historical proof
baseline != prospective dataset
later success != earlier success
```

The prospective dataset begins only under the eligibility conditions defined by
the frozen research contract and the operational schedule.

## Evidence discipline

Prefer the smallest evidence artifact that verifies the claim.

For each material observation preserve, where applicable:

- object ID;
- platform;
- infrastructure layer;
- retrieval timestamp;
- source locator;
- attempt status;
- observation state;
- failure reason;
- evidence reference;
- correction/provenance link.

Do not interpret HTTP `404`, an empty search result, `429`, timeout, or access
failure as global non-existence unless the platform's observable contract
supports that inference.

## Public data and privacy

The study primarily uses public research-software and public scholarly metadata.

Canonical public identifiers needed for reproducibility may be retained.

Public accessibility does not justify indiscriminate collection. Follow
`DATA_HANDLING.md` and exclude credentials, cookies, session identifiers,
private or expiring share tokens, IP addresses, unrelated telemetry, private
messages, and incidental personal information.

## Analysis

The planned analysis is descriptive.

Appropriate operations include:

- direct counts and proportions;
- timestamp differences where comparable;
- propagation ordering;
- state transitions;
- cross-layer consistency/difference;
- failure, partial, unresolved, and rate-limit frequencies.

Do not silently add imputation, causal modeling, NHST, p-values, global
composite scores, or other inferential machinery outside the research plan.

## History and correction

Historical records are append-oriented.

A material correction should preserve:

```text
source evidence
→ raw observation
→ normalized/derived observation
→ analysis
→ interpretation
→ reported conclusion
```

When an error is found, record the prior value, corrected value, reason,
supporting evidence, timestamp, and affected outputs.

Do not rewrite point-in-time history merely to make later records look cleaner.

## Open-science file responsibilities

- `README.md` — public orientation and study entry points.
- `OPEN_RESEARCH.md` — durable research-production method.
- `RESEARCH_TEMPLATE.md` — human-facing bounded research template.
- `templates/` — machine-oriented operational templates.
- `AUTHORS` — repository authorship/maintenance attribution.
- `LICENSE` and `LICENSING.md` — reuse terms and licensing boundary.
- `CITATION.cff`, `codemeta.json`, `.zenodo.json` — software/citation metadata.
- `CONTRIBUTING.md` — contribution workflow.
- `CODE_OF_CONDUCT.md` and `SECURITY.md` — collaboration/security governance.
- `RELEASE_POLICY.md` — release and archive semantics.
- `.github/ISSUE_TEMPLATE/**` and pull-request template — reviewable intake.
- `AMENDMENTS.md` and `DEVIATIONS.md` — explicit governance history.

These surfaces improve openness and reproducibility; they do not establish
scientific validity by themselves.

## Release and scholarly metadata

Before a new archival release, verify agreement across:

- repository title and description;
- software author metadata;
- ORCID;
- license;
- concept DOI versus version DOI;
- OSF related identifier;
- release tag and release date.

A DOI or downstream index entry proves publication/representation, not runtime
execution, scientific validation, adoption, or reproduction.

## Permanent boundaries

```text
model != agent system
contract != observation
source exists != claim is true
raw observation != interpretation
checker present != checker executed
checker pass != scientific truth
publication != validation
indexing != repository truth
current state != historical state
```

## 中文摘要

本仓是冻结 OSF 研究合同的执行、证据、provenance 与分析运行层，不是第 11 个样本。
研究固定十个对象、六个分析层；七个平台只是采集粒度。历史 baseline 与 prospective
dataset 必须分离，失败、未知、429、部分验证与无结论均为合法研究结果。任何公开结论
都应尽可能追溯到原始证据与时间戳。
