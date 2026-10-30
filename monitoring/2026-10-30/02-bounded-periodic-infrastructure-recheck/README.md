# October 30 bounded periodic research-infrastructure recheck

**Logical date:** 2026-10-30, Asia/Shanghai  
**Class:** read-only diagnostic monitoring and retrospective timeline summary, **NOT** a scheduled prospective observation, OSF amendment, new release or new DOI  
**Base main:** [`6546c9debb050966ff93ff87d92eb6021b6349b3`](https://github.com/lostlight530/research-software-identity-audit/commit/6546c9debb050966ff93ff87d92eb6021b6349b3), 0 open control PRs when checked

## Coverage and measurement limits

The [34-row source-attempt projection](surface-attempts.csv) maps one representative URL to each of the 34 existing platform/service/standard surface rows in the [October 26 institution checklist](../../../evidence/2026-10-26/02-evening-institutional-recheck/surface-attempt-crosswalk.json). This is **surface-level sampled coverage**, not a full multi-object census, nor 34 independent research institutions. The [machine record](record.json) retains the bounds and count.

| Evidence condition | Surface rows | Permitted claim |
| --- | ---: | --- |
| Third-party content extract with `acquired_at` on 2026-10-30 UTC | 11 | An accessible source representation with day-granularity acquisition, **not** verified uncached origin response or a certified new field transition |
| Third-party extract acquired on earlier UTC dates | 15 | Historical/cache representation only, **not** newly observed October 30 platform state |
| Structured connected GitHub read | 2 | Exact GitHub API scope, including the RSE PR and 11 published-Release list queries |
| Failed public URL extraction | 6 | Bounded failures: ASWG connection error; dkNET, InterLex, HAL and Identifiers.org selected paths returned 404; N2T returned 403. **None** proves global absence |
| **Total** | **34** | One attempted representative source per existing checklist row |

Public reader batch client clocks: `2026-10-30T00:42:58.097Z–00:43:35.407Z` and `00:43:51.210Z–00:44:01.189Z`. Structured connected GitHub Releases batch: `00:44:11.871Z–00:44:13.679Z`. These bracket **tool execution**, not individual origin requests, source content changes or first-appearance timestamps. Extractor acquisition clocks are **UTC-day truncated**. No original external HTTP bytes, headers, signed fetch proofs, or unmodified local raw-response artifacts were archived by this diagnostic. The CSV is an attributed selected-field/access ledger, **not raw HTTP evidence**.

Zenodo's chosen RS01 version response, SciCrunch/RRID, NIF, bio.tools, LifeMonitor, EDAM, Bioregistry, Handle, Crossref Agency and CiteAs had same-day-acquired extracts. These do **not** support full family/version sums, complete DOI enumeration, new ORCID group counts or independent scholarly uptake. ORCID, DataCite, OSF, OpenAlex, OpenAIRE and Software Heritage extracts were older. Preserve prior [October 26 independently recorded platform counts](../../2026-10-26/02-evening-institutional-recheck/README.md) at **their original date** rather than relabeling them as October 30 figures.

## GitHub exact source results

Connected GitHub checked all 11 core `main` branches and all 11 `GET /releases?per_page=100` lists. All 10 fixed repositories returned **four published Release rows each**, with latest `v2026.10-fourteen-day-evidence-checkpoint` published on October 14 UTC. CONTROL independently returned **four**, latest `v2026.10-evidence-integrity` published October 18 UTC. These fields agree with the [Oct 29 independent list check](../../2026-10-29/02-independent-release-gate-recheck/README.md). The response does **not** enumerate plain Git tags, drafts, or every possible release-history route.

| Fixed corpus | Current `main` prefix | Fixed corpus | Current `main` prefix |
| --- | --- | --- | --- |
| RS01 welcome-to-github | `209c84c1` | RS06 auto-doc-engine | `907d0dfd` |
| RS02 zero-entropy-lab | `6c8f448d` | RS07 epistemic-pipeline | `2d19cf23` |
| RS03 Axiom-0 | `d0fd7034` | RS08 sci-render-kit | `5696b29a` |
| RS04 reflective-continuum | `b2a099f9` | RS09 china-agentic-observatory | `2c399dea` |
| RS05 agent-foundations | `682b7383` | RS10 agentic-frontier-observatory | `c08ada02` |

CONTROL current `main`: `6546c9de`, **not RS11**. Six unrelated core-repository open PRs were present at inspection: [welcome #864](https://github.com/lostlight530/welcome-to-github/pull/864), [zero #754](https://github.com/lostlight530/zero-entropy-lab/pull/754), [auto-doc #194](https://github.com/lostlight530/auto-doc-engine/pull/194), [epistemic #190](https://github.com/lostlight530/epistemic-pipeline/pull/190), [China #215](https://github.com/lostlight530/china-agentic-observatory/pull/215), [global #219](https://github.com/lostlight530/agentic-frontier-observatory/pull/219). Their producer/review gates were **not** modified.

Public upstream interaction status: [RSD #1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870) **closed 2026-10-16T12:11:19Z** by the project workflow; closure is **not** independently confirmed production fix deployment. [RSD #1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871) remains **open**; [rseng/software #498](https://github.com/rseng/software/pull/498) remains **open, unmerged, without submitted review evidence**. These outcomes must not be converted into institutional affiliation or endorsement.

## First day → last checked day: bounded longitudinal engineering history

Retrospective reading of the [complete current `main` commit list](https://api.github.com/repos/lostlight530/research-software-identity-audit/commits?sha=main&per_page=100) yielded **91 main-reachable commits**, from `e5ba0a0e` on **2026-10-05T14:59:46Z** through `6546c9de` on **2026-10-29T16:11:49Z** (October 30 Beijing). These are **Git committer timestamps**, not captured historical API responses, unique experiments, PR counts or evidence objects. This extends the [as-of Oct 28 pinned 87-commit historical audit](../../../docs/control-repository-lifecycle-audit-through-2026-10-28.md) without altering its cutoff.

| Beijing-local period | Source-grounded sequence |
| --- | --- |
| Oct 5 | OSF Registration `5b329` frozen as the registered plan; CONTROL repository subsequently initialized; the initial baseline cutoff remains **23:59:59 Asia/Shanghai** |
| Oct 6–9 | Baseline reconciliation and early diagnostic monitoring; original OSF Overview crosswalk; platform identity and source/field comparisons. Historical reconciliation retrieval clocks are not reset to Oct 5 |
| Oct 10–13 | DOI/version identity reconciliation and control citation metadata correction; seven-platform control checks and fixed-corpus release-gate diagnostics, with corrections retained |
| Oct 14–18 | Ten fixed-software checkpoint Releases, later discovery/preservation checks, CONTROL evidence-integrity release and archive reconciliation. All pre-schedule diagnostics remain separate from prospective data |
| Oct 19–24 | Independently bounded rechecks, local evidence handoff, source coverage/reconciliation, historical file/path and commit inventories |
| Oct 25–27 | Semantic assurance and platform observable-contract review; 34-surface / 384-request Oct 26 institutional recheck; public manifest verification repair and Oct 27 limited seven-platform diagnostic |
| Oct 28–29 | Pinned retrospective lifecycle review and later 29th bounded recheck; October 29 record's unverified request-clock placeholders corrected. No history is silently repaired |
| Oct 30 | [Independent GitHub Release gate](../../2026-10-29/02-independent-release-gate-recheck/README.md) and [OSF original-versus-revised response comparison](../01-osf-schema-response-version-reconciliation/README.md) already on main; this additional 34-row diagnostic is a bounded new **source-access comparison**, not a new OSF registration or prospective wave |

For the OSF version matter: the separately documented **29 compared `revision_responses` fields had 28 equal and one changed, `344-83` Other planned analysis**. Later exploratory examples must not be backdated into original preregistered primary analyses. This record does not re-run original OSF JSON byte capture or add a second independent publisher source.

## Contract, verification and decision

- Frozen objects: **RS01–RS10 = 10**; CONTROL and PILOT are independent supplementary software families
- Frozen layers: **6**, **60 object-layer units per eligible scheduled timepoint**; seven operational platforms, **70 possible platform checks**, different units
- [Operational schedule](../../../schedule/README.md) still declares **no concrete offsets**. An October 14 fixed-software Release is not sufficient to establish an eligible scheduled prospective collection
- `observations/raw/` and `observations/derived/`: **zero new prospective cells**
- No contract, baseline, schedule, schema, historical package, Release, tag, DOI or external account edit
- Previous CONTROL [main CI run 40909170317](https://github.com/lostlight530/research-software-identity-audit/actions/runs/40909170317) finished `success`; individual advisory steps were also reported `success`. This is implementation validation, **not** source-freshness or scientific correctness evidence
- No same-day **complete** 10-object/seven-platform census, complete 34-surface object matrix, new 12-family Zenodo totals, complete ORCID group recount, OpenAlex conflict resolution, or full Software Heritage visit refresh was performed

**Outcome: `PARTIAL / NO_CONCLUSION` for a full same-day cross-platform census; `PASS` for 11 bounded GitHub published-Release lists and 34 surface-row attempts.** No material change in the compared GitHub Release-list fields. Real external state transitions remain **UNKNOWN** without comparable current origin evidence.

**Retest conditions:** actual source-provenance-consistent acquisitions for stale/failed platforms, complete version/family or author-work query shape when a metric is claimed, deploy-level confirmation if RSD #1870 is interpreted as fixed, and a separately declared operational schedule before any future prospective classification. 
