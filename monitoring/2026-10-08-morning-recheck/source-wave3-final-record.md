# Conversation-supplied "Wave 3 Observation Record" — 2026-10-08

## Source identity

The current conversation supplied a finalized record titled:

> 学术软件身份链纵向审计：第三前瞻性观测波次全量规范记录
> (Wave 3 Observation Record 终版)

The source declares an observation cutoff of:

- 2026-10-08 08:35:00 Asia/Shanghai
- 2026-10-08 00:35:00 UTC

This cutoff is preserved as a source-declared as-of boundary. It does **not**
replace the earlier supplied retrieval window of 08:12–08:26 with a claim that
all platform states were retrieved at exactly 08:35.

The source identifies:

- OSF registration DOI: `10.17605/OSF.IO/5B329`
- Principal Investigator: Xuanyi Jiang
- ORCID: `0009-0001-3617-0832`
- OSF user: `6k425`
- GitHub: `lostlight530`
- research infrastructure repository:
  `lostlight530/research-software-identity-audit`

## Source-declared dataset phase

The source labels this record:

- dataset phase: `prospective`
- wave: `3`
- fixed denominator: `N=10`

The research repository **does not adopt the prospective classification** in
this reconciliation.

Reason: the frozen/operational contract requires the prospective dataset to
start only after registration and an eligible new fixed-corpus release event.
The independent public-endpoint pass for this update found all ten fixed
repositories still on the 2026-10-04
`v2026.10-open-research-production-framework` release, which predates the
2026-10-05 preregistration. No eligible post-registration fixed-corpus release
event is evidenced here.

Therefore:

```text
source label: prospective Wave 3
repository adjudication: pre_eligibility_monitoring
prospective_dataset_member: false
```

The source identity is retained; the classification is reconciled rather than
silently rewritten.

## Source-reported four-period metrics

| measure | T0 2026-10-05 | T1 2026-10-06 | T2 2026-10-07 | T3 2026-10-08 | T3 vs T2 |
|---|---:|---:|---:|---:|---:|
| ten-family Zenodo views | 575 | 616 | 695 | 775 | +80 |
| ten-family downloads | 7 | 7 | 7 | 7 | 0 |
| total reported package bytes | 29,261,316 | 29,282,855 | 29,282,855 | 29,282,855 | 0 |
| DataCite current-version DOI findable | 10 | 10 | 10 | 10 | 0 |
| source-defined SWH + tag + OpenAIRE closure | 0 | 0 | 10 | 10 | 0 |
| source-defined OpenAlex fixed-study scope | 40 | 40 | 41 | 41 | 0 |
| RSD public software records | 0 | 0 | 11 | 11 | 0 |
| audit-runtime Zenodo family views | 0 | 2 | 33 | 47 | +14 |
| Internet Archive mirror packages | 5 | 5 | 5 | 5 | 0 |

### Reconciliation notes

1. The source's OpenAlex `41` is normalized here as a **fixed-study-scope
   count**: 40 fixed-corpus Software works + 1 OSF registration. It is not the
   current main-author live Works-list total, which independently returned 43
   because two audit-runtime Software works are now also under the main author.
2. Aggregate package-byte equality from T2 to T3 supports only an aggregate-size
   no-change statement. It does not by itself prove bytewise identity. The
   repository retains the earlier unresolved T0/T1 size transition and does not
   infer a content mutation or a bytewise identity without row-level
   cross-wave checksum evidence.
3. The source calls the closure a "Four-Way Consensus Triad" but enumerates
   SWH + GitHub release tag + OpenAIRE. This repository stores the observed
   components rather than relying on the label.

## Source-supplied object rows and canonical mapping reconciliation

The source-supplied table uses the prior display-order mapping for RS06–RS10:

```text
source RS06 = china-agentic-observatory
source RS07 = agentic-frontier-observatory
source RS08 = sci-render-kit
source RS09 = auto-doc-engine
source RS10 = epistemic-pipeline
```

The authoritative `corpus/object-manifest.csv` mapping is:

```text
RS06 = auto-doc-engine
RS07 = epistemic-pipeline
RS08 = sci-render-kit
RS09 = china-agentic-observatory
RS10 = agentic-frontier-observatory
```

No raw source row is deleted. Derived rows in
`ten-repository-zenodo-delta.csv` use the canonical mapping.

The source-reported current values themselves are retained:

| canonical object | repository | concept DOI | current DOI | source-reported T3 views/downloads | T3-T2 views |
|---|---|---|---|---:|---:|
| RS01 | welcome-to-github | 10.5281/zenodo.22790907 | 10.5281/zenodo.23137203 | 98 / 4 | +8 |
| RS02 | zero-entropy-lab | 10.5281/zenodo.22791081 | 10.5281/zenodo.23137204 | 75 / 0 | +9 |
| RS03 | Axiom-0 | 10.5281/zenodo.22791103 | 10.5281/zenodo.23137205 | 93 / 0 | +8 |
| RS04 | reflective-continuum | 10.5281/zenodo.22791141 | 10.5281/zenodo.23137206 | 52 / 0 | +8 |
| RS05 | agent-foundations | 10.5281/zenodo.22791169 | 10.5281/zenodo.23137207 | 78 / 1 | +7 |
| RS06 | auto-doc-engine | 10.5281/zenodo.22791404 | 10.5281/zenodo.23137215 | 59 / 0 | +7 |
| RS07 | epistemic-pipeline | 10.5281/zenodo.22791463 | 10.5281/zenodo.23137216 | 74 / 0 | +10 |
| RS08 | sci-render-kit | 10.5281/zenodo.22791375 | 10.5281/zenodo.23137219 | 65 / 1 | +8 |
| RS09 | china-agentic-observatory | 10.5281/zenodo.22791309 | 10.5281/zenodo.23137211 | 88 / 0 | +7 |
| RS10 | agentic-frontier-observatory | 10.5281/zenodo.22791334 | 10.5281/zenodo.23137214 | 93 / 1 | +8 |

## Source-declared invariant suite

The source supplied six assertions. They are preserved below with repository
adjudication:

| source assertion | repository adjudication |
|---|---|
| N=10 | supported |
| OpenAlex Works Count=41 | supported only as fixed-study scope 40 Software + 1 OSF; not current author-list total |
| downloads=7 | source-reported and consistent with supplied T0–T3 series |
| total size=29,282,855 and "100% bitstream conserved" | aggregate size equality supported by source; bytewise identity not independently established |
| RSD 11/11 public | source-reported; audit-runtime and constellation pages independently readable, aggregate 11 not reconstructed in this updater |
| SWH + Tag + OpenAIRE 10/10 | independently supported for the declared component checks |

The source's terminal label
`ALL_INVARIANTS_CONSERVED_AND_VERIFIED` is therefore **not copied as the
repository's unqualified conclusion**. The repository conclusion is
`PARTIALLY_INDEPENDENTLY_VERIFIED_WITH_CONTRACT_RECONCILIATION`.
