# Research Template / 科研记录模板

Status: prospective human-facing research template  
Scope: new bounded research, reconciliation, special analysis, or exploratory records

Operational observation batches should use the machine-oriented templates under
`templates/`. This file is for human-readable research records and does not
retrofit historical records.

## Record identity / 记录身份

- Research record ID:
- Record type: scheduled observation / reconciliation / analysis / special / exploratory
- Research status: preregistered / amendment-governed / exploratory / post hoc
- Logical date or period:
- Actual execution date:
- Retrieval/execution window:
- Base Git revision:
- Related schedule ID:
- Related amendment/deviation IDs:
- Prior related record:

Use `UNKNOWN`, `NOT_APPLICABLE`, `NOT_EXECUTED`, or `NOT_OBSERVED`
instead of inferring a value from neighboring fields.

## Research question / 研究问题

State one bounded question that can be contradicted by evidence.

## Contract basis / 合同基础

- Frozen preregistration clause or repository contract:
- Fixed corpus scope:
- Infrastructure layer(s):
- Operational platform(s):
- Prospective or baseline:
- Known limitations:

## Falsifiable hypothesis or bounded judgment / 可证伪假设

- Proposed explanation:
- Support condition:
- Falsifier:

If the record is purely descriptive and no hypothesis is appropriate, say so.

## Evidence/source basis / 证据基础

For each material source record:

- source locator:
- publisher/platform:
- retrieval timestamp:
- source identity/version:
- supported proposition:
- limitation:
- evidence reference:

Do not count multiple URLs from the same evidence identity as independent
sources.

## Identity boundary / 身份边界

List identities that must remain separate in this record, for example:

- software family versus version;
- repository versus archive record;
- concept DOI versus version DOI;
- infrastructure layer versus concrete platform;
- release timestamp versus retrieval timestamp;
- historical event time versus current endpoint state.

## Procedure actually executed / 实际过程

Describe exactly what was queried, inspected, parsed, or calculated.

Do not describe an intended procedure as executed.

## Raw observations / 原始观测

Record direct platform responses and retained evidence before interpretation.

```text
404 != global absence
429 != absence
empty result != non-existence
live endpoint != historical proof
partial != complete
```

## Verification and counterexample / 复核与反例

- Independent verification attempted:
- Counterexample/disconfirming check:
- Result:
- Unresolved verification gap:

If verification could not be performed, record why.

## Derived result / 派生结果

Only include calculations supported by comparable observed fields.

Appropriate examples:

- direct count;
- proportion;
- timestamp difference;
- propagation order;
- state transition;
- cross-layer difference;
- failure/partial/unresolved frequency.

No imputation or causal claim is implied.

## Interpretation / 解释

Separate:

- verified fact;
- raw observation;
- platform-returned state;
- evidence-based inference;
- hypothesis;
- unknown.

## Provisional conclusion / 暂时结论

Allowed outcomes include:

- OBSERVATION
- FINDING
- NO_CONCLUSION
- UNKNOWN
- PARTIAL
- DEGRADED
- REFUTED
- INVALIDATED

Do not manufacture a positive conclusion for cadence completeness.

## Correction and historical impact / 修正与历史影响

- Does this change a prior interpretation?
- Prior record/reference:
- Correction mechanism:
- Historical record preserved: yes/no
- Downstream analyses affected:

## Research increment / 研究增量

Record only what this unit actually added:

- new evidence;
- new state transition;
- new counterexample;
- narrower observable boundary;
- corrected interpretation;
- new uncertainty;
- NONE.

## Retest condition / 复验条件

State what future event, evidence, or platform state would justify retesting.

## Release/publication boundary

A repository merge, release, DOI, ORCID/OpenAIRE/OpenAlex appearance, or checker
pass is not itself evidence of the scientific conclusion.

When this record supports a public claim, include the traceable evidence path.
