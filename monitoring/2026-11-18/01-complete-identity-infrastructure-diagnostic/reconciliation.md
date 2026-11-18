# 2026-11-18 diagnostic reconciliation and explicit unknowns

**Source:** [GitHub Actions #44337384660](https://github.com/lostlight530/research-software-identity-audit/actions/runs/44337384660), executed **2026-11-18T15:35:32.034791+00:00 to 15:39:43.508949+00:00**. Same 458 exact (scope,key) identities as [2026-11-17 complete diagnostic](../../2026-11-17/02-full-selftest/README.md), not a new sampling denominator. The [request-level delta](request-delta.csv) retains every change, unresolved and degraded row

## What actually changed versus November 17

| Operational fact | November 17 | November 18 | Boundary |
| --- | --- | --- | --- |
| HTTP 200 and no recorded request failure | 451/458 | 402/458 | transport, not identity validation |
| Failed/partial external attempt | 7/458 | 56/458 | 46 Zenodo version, 10 supplementary surface |
| Zenodo version records, 67 possible checks | 67/67 retrieved | 21/67 retrieved | 45 timeouts, 1 HTTP 500, no object-absence claim |
| Zenodo fixed-ten (60-version) views/download sum | 4105 / 41 | **null / null** | not computable on incomplete records; not a decline to zero |
| DataCite known DOI requests | 102/102 transport | 102/102 transport | fixed inventory, not all possible DOIs |
| OpenAIRE positive DOI requests | 94/102 | 94/102 | not distinct software identities |
| OpenAlex exact canonical DOI | 33/102 | 34/102 | one changed result, DOI `10.48546/workflowhub.workflow.2332.9`; not RS11 |
| ORCID groups/work summaries | 18 / 119 | 18 / 119 | no observed change |
| SWH latest origin responses | 10/10 full | 10/10 full | latest origin status does not prove a fresh preservation visit |
| GitHub main / GitHub Releases | 11 changed main SHA | 11 unchanged release signatures | source commits do not imply new tagged release |

Supplementary surface failures in the actual November 18 source ledger: SciCrunch timeout, RRID Portal timeout, ScreenIT ASWG URLError, NIF timeout, dkNET HTTP 403, InterLex HTTP 403, Zenodo surface timeout, HAL HTTP 404, Identifiers.org HTTP 404 and N2T HTTP 403. Failed/partial statuses remain failures; 404/403 are not negative evidence of object existence

**Upstream institution/service interaction:** RSD-as-a-service #1871 remains closed, upstream PR #1897 previously merged (2026-11-16); this is **not** proof of production deployment, Chrome/Edge UI remediation or new user interaction. `rseng/software` PR #498 remains open and unmerged; no editorial acceptance. SciCrunch RRID `SCR_029105` ownership/curation progress is not verified by this capture

## Contract and corrections

- Fixed RS01–RS10 and CONTROL outside the corpus; six registered layers, 60 object-layer units per eligible scheduled point; seven operational platforms and 70 potential checks are separate denominators
- 34 supplementary service/standards URLs do not expand the population; **0 new prospective cells**
- No OSF edit, release DOI issue, Zenodo deposit, authentication write or historical source rewrite
- **NO_CHANGE_REQUIRED** for research runtime/contract: 11 pinned repository checks passed; this cycle only adds bounded new diagnostic evidence and source-aware classification, not a correction of any old raw record
- Correct the common interpretation error by preserving the Nov18 partial Zenodo aggregates as `null`; do not publish a fabricated negative usage trend or any synthetic count
- Date fields are client retrieval clocks, not initial propagation or first indexed timestamps; original external HTTP bodies are not stored, only their SHA-256/length and selected public projections

**Trace:** [source requests](../../../evidence/2026-11-18/01-complete-identity-infrastructure-diagnostic/source-attempts.jsonl) → [selected public fields](../../../evidence/2026-11-18/01-complete-identity-infrastructure-diagnostic/selected-fields.jsonl) → [458-key comparison](request-delta.csv) → [normalized record](record.json) → this reconciliation. [Previous full request ledger](../../../evidence/2026-11-17/02-full-selftest/source-attempts.jsonl) remains unchanged. Correction history is additive; no retrospective replacement
