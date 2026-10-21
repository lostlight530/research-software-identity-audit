# Documentation map and maintenance guide

This file is an **orientation and contribution guide** for the live GitHub research-control repository. It is **not** a new research protocol, operational schedule, observation, correction event, or amendment of the [registered OSF study](https://osf.io/5b329/overview).

For the scientific background start with the [main README](../README.md); for the research-production discipline see [OPEN_RESEARCH.md](../OPEN_RESEARCH.md). The DOI of the separate frozen research plan is [10.17605/OSF.IO/5B329](https://doi.org/10.17605/OSF.IO/5B329).


**Latest dated maintenance handoff (2026-10-18):** [research session closeout and reproducibility handoff](research-session-closeout-2026-10-18.md). It crosswalks public evidence, the frozen OSF contract, four actually published control releases (including [October 18 postpublication reconciliation](../scholarly/release-identity-reconciliation-2026-10-18.md)), the user-confirmed Beta ORCID metadata refresh, and outstanding verification gates. It is a *historical review*, not a standing claim about all future `main` commits or live platform counters.

**Dated full-repository inventory (October 21, 2026):** [Control repository classification and evolution report](control-repository-inventory-2026-10-21.md), [complete tracked-file path catalog](control-repository-file-catalog-2026-10-21.csv), and [chronological main commit ledger](control-repository-main-commit-ledger-2026-10-21.csv). These inventory artifacts are documentation snapshots, not research observations or an RS11 designation.

## 1. Authority and object boundaries

| Surface | Authority and purpose | What it does **not** imply |
| --- | --- | --- |
| [OSF Registration](https://osf.io/5b329/overview) | Time-stamped research contract, with any transparent OSF update history distinguished | Later GitHub text is not retrospectively preregistered |
| [Associated OSF Project](https://osf.io/wa5v8) | Related project/materials surface, distinct from the registration | Project files or project status cannot amend the frozen registration |
| [GitHub `main`](../README.md) | Current executable/documentary research-control runtime | Current `main` is not an earlier release tag or historical observation |
| [Zenodo concept DOI](https://doi.org/10.5281/zenodo.23166490) | Citation identity for the control repository **family** | Not the DOI of an individual immutable archived release |
| [Zenodo version DOI](https://doi.org/10.5281/zenodo.23284570) | Dated, immutable archive of the **2026-10-10** control software release | Does not contain later commits made to GitHub `main` |
| [Corpus manifest](../corpus/object-manifest.csv) | The **ten** preregistered study software objects `RS01`–`RS10` | The separately reported audit/control repo is **not RS11** |

Six preregistered infrastructure **layers** yield `10 × 6 = 60` object-layer units **per eligible scheduled timepoint**. Seven operational **platforms** are GitHub, Zenodo, DataCite, ORCID, Software Heritage, OpenAIRE, and OpenAlex. The last two are independent checks mapped to the **same** `discovery_graph` layer: `10 × 7 = 70` possible platform checks is **not** the preregistered analysis denominator. See [the counting contract](../schema/counting-rules.md) and [platform mapping](../schema/platforms.yaml).

## 2. Directory map: where to read and where a future contribution belongs

| Owner | Contents and canonical entry | Change boundary |
| --- | --- | --- |
| `contract/` | [Frozen registration mapping](../contract/preregistration.md), [OSF Overview crosswalk](../contract/osf-overview-crosswalk-2026-10-08.md), [limitations](../contract/known-limitations.md) | Explain the registered contract; don't silently edit what was registered |
| `corpus/` | [Fixed-object manifest](../corpus/object-manifest.csv) | Exactly RS01–RS10; no new sample via documentation |
| `baseline/` | [Historical baseline](../baseline/README.md) and [2026-10-05 package](../baseline/2026-10-05/README.md) | Baseline cutoff **2026-10-05 23:59:59 Asia/Shanghai**; later retrieval is not historical capture |
| `schedule/` | [Operational schedule status and rules](../schedule/README.md) | No concrete offsets are declared in that record; a documentation update is not a schedule declaration |
| `schema/` | [Counting rules](../schema/counting-rules.md), [layers](../schema/infrastructure-layers.yaml), [platforms](../schema/platforms.yaml), [state vocabulary](../schema/state-taxonomy.yaml), [observation JSON schema](../schema/observation.schema.json) | Only contract-aware, separately reviewed schema changes |
| `monitoring/` | [Dated diagnostic and pre-eligibility records](../monitoring/README.md), [path conventions](../monitoring/NAMING.md) | Useful measurements, **not** auto-promoted to the prospective dataset |
| `observations/raw/` | [Prospective raw observation location](../observations/raw/README.md) | Only eligible, schedule-governed observation records belong here |
| `observations/derived/` | [Derived observation location](../observations/derived/README.md) | Derivations must cite actual raw observations; missing values not imputed |
| `evidence/` | [Original captured evidence / manifests](../evidence/README.md) | Preserve source identity, retrieval clock and digests; don't rewrite sealed bytes |
| `provenance/` | [Provenance policy](../provenance/README.md) | Traceable lineage through source → raw → derived → interpretation |
| `analysis/` | [Descriptive research analysis](../analysis/README.md) | Exploratory work clearly identified; no unregistered causal/inferential model |
| `scholarly/` | [Archive and identifier guide](../scholarly/README.md), [citation guide](../scholarly/CITATION.md) | Concept DOI, version DOI and OSF study DOI remain different identities |
| `templates/` | [Reusable research templates](../templates/README.md), [human-facing template](../RESEARCH_TEMPLATE.md) | Templates are **not** completed observations or data |
| `tools/` | [Offline and contract checker commands](../tools/README.md) | Advisory CI is a guardrail, not a claim of scientific verification |
| `.github/` | [PR template](../.github/PULL_REQUEST_TEMPLATE.md), [CI workflow](../.github/workflows/validate.yml), issue templates | PR/issue process is not a change to the research contract |
| `docs/` | This documentation map | Navigation and maintainership instructions, **not** observational evidence |
| `RELEASE_POLICY.md` and `scholarly/release-readiness-2026-10-18.md` | [Immutable release policy](../RELEASE_POLICY.md) and [dated package-preflight checklist](../scholarly/release-readiness-2026-10-18.md) | A preflight is not a new tag, Zenodo version DOI, or archived release |

**Do not move or rename historical `monitoring/`, `evidence/`, `baseline/`, or `provenance/` paths for cosmetic organization.** Existing evidence manifests, source locators, hashes, PR links and paper references may depend on those paths. The historical [October 8 path-migration ledger](../monitoring/path-migration-2026-10-08.csv) is a **dated** migration record, not permission for another silent rewrite.

## 3. Read a result without mixing evidence levels

Follow the narrowest source that actually supports the claim:

1. **Source evidence** — original platform response or explicitly attributed user-supplied text, with locator and actual retrieval interval.
2. **Raw observation** — response state and fields as seen, including 404, 429, timeout, blocked, degraded and partial.
3. **Normalized or derived observation** — explicit identity join, counter semantics, calculation rule and raw references.
4. **Interpretation** — bounded research judgment, alternative explanations and remaining unknowns.
5. **Reported conclusion** — claim tied back to a dated evidence chain and its amendments/corrections.

A later public endpoint does not replay a historical state. A DOI or successful CI run does not prove execution, adoption or scientific validity. Zenodo `views` and `unique_views` are distinct source fields; WorkflowHub Dashboard counts and per-version Activity need their own reporting window and entity-grain checks. A summed family-level unique counter is **not** a globally deduplicated number of people. Use the [existing counting rules](../schema/counting-rules.md); this guide adds **no new metric definitions**.

## 4. Docs-only maintenance workflow

**Documentation scope:** a documentation-only PR may fix navigation, link targets, terminology, accessibility, contributor guidance, or dated operational explanations. It must not insert new API results, tables of newly observed counts, prospective records, fake historical timestamps, new releases, or made-up verification outcomes.

1. Read fresh `main`, open PRs, the [OSF contract mapping](../contract/preregistration.md), relevant schema and the documents being changed. Prefer the smallest reviewable branch.
2. Decide whether the claim belongs to **durable documentation** (e.g. folder purpose) or a **dated source/monitoring record** (e.g. October API counters). Put it in the owner, without rewriting a past observation.
3. Preserve existing evidence/provenance files, stable paths, correction history and historical author/source attribution. To correct historical interpretation, create a separately attributed correction through the established research process, **not** a docs cleanup.
4. Review relative Markdown links against the branch tree. Keep file names, anchors and reference scopes unambiguous. Prefer links to canonical owners rather than duplicating mutable figures on the landing page.
5. Run the configured advisory contract check (if executable in the actual environment): `python tools/check.py --mode advisory`. If relevant, run `--mode strict` as an explicitly separate local check; do **not** present an unrun command as success.
6. In the PR state **which checks actually ran**, which were blocked/not executed, the exact changed files, scope constraints, and any unresolved evidence. Review the changed-file diff and CI, merge when appropriate, then verify `main` and its workflow run.

**Documentation-only acceptance boundary:** no changes to `contract/`, `corpus/`, `baseline/`, `schedule/`, `schema/`, `observations/`, `monitoring/`, `evidence/`, `provenance/`, or `analysis/` data/scripts; no changes to `.zenodo.json`, `CITATION.cff`, `codemeta.json`, Git tags or OSF records. An explanatory link to those files is fine. See [CONTRIBUTING.md](../CONTRIBUTING.md), [data handling](../DATA_HANDLING.md), and [licensing](../LICENSING.md).

## 5. External OSF service lifecycle (not a contract amendment)

The [OSF Projects transition guidance](https://help.osf.io/article/727-osf-projects-transition) states that OSF Projects stop accepting new projects/components **November 16, 2026** and existing projects are planned to become read-only **February 19, 2027**. [OSF's registration-specific guidance](https://help.osf.io/article/770-registrations) says **registrations/preregistrations are not affected** by that Projects transition. These are **externally published prospective service-policy dates**, not observed changes to this project's October 2026 state or to the frozen research contract.

Operationally keep the *associated OSF Project*, the *independent OSF Registration*, GitHub's mutable executable runtime, and Zenodo's immutable release archives separate. Check the official OSF documentation again before a future migration decision. Do not move or re-register evidence merely because a service-policy notice exists.

---

This page is an **index and maintenance explanation only**. When a summary disagrees with a frozen registration, source record, schema, or retained observation, consult the owning source and preserve the discrepancy instead of silently editing the historical record.

## October 18 research-only independent verification

The [dated research record](../monitoring/2026-10-18/03-independent-research-verification/README.md) owns the new measurements and archive inspection. The [minimized evidence package](../evidence/2026-10-18/03-independent-research-verification/README.md) declares public-field versus locally retained transport evidence. The standalone offline checker makes no network requests. **Historically**, it was not in CI when this October 18 note was written; the current [validation workflow](../.github/workflows/validate.yml) now runs the October 18 and October 20 package checkers as **advisory** steps. Neither their presence nor a green workflow retroactively establishes independent raw transport replay. Community correspondence, account operations, private monitoring identifiers and unrelated telemetry are outside this contribution.
