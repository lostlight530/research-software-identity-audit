# Documentation map and maintenance guide

This file is an **orientation and contribution guide** for the live GitHub research-control repository. It is **not** a new research protocol, operational schedule, observation, correction event, or amendment of the [registered OSF study](https://osf.io/5b329/overview).

For the scientific background start with the [main README](../README.md); for the research-production discipline see [OPEN_RESEARCH.md](../OPEN_RESEARCH.md). The DOI of the separate frozen research plan is [10.17605/OSF.IO/5B329](https://doi.org/10.17605/OSF.IO/5B329).


**Latest dated maintenance handoff (2026-10-18):** [research session closeout and reproducibility handoff](research-session-closeout-2026-10-18.md). It crosswalks public evidence, the frozen OSF contract, four actually published control releases (including [October 18 postpublication reconciliation](../scholarly/release-identity-reconciliation-2026-10-18.md)), the user-confirmed Beta ORCID metadata refresh, and outstanding verification gates. It is a *historical review*, not a standing claim about all future `main` commits or live platform counters.

**Dated full-repository inventory (October 21, 2026):** [Control repository classification and evolution report](control-repository-inventory-2026-10-21.md), [complete tracked-file path catalog](control-repository-file-catalog-2026-10-21.csv), and [chronological main commit ledger](control-repository-main-commit-ledger-2026-10-21.csv). These inventory artifacts are documentation snapshots, not research observations or an RS11 designation.

**Historical source inventory through 2026-10-28:** [Lifecycle and OSF-contract audit](control-repository-lifecycle-audit-through-2026-10-28.md) · [full main-history ledger](control-repository-main-history-through-2026-10-28.csv) · [437 tracked paths with original Git blob SHAs](control-repository-tracked-files-through-2026-10-28.csv) · [machine-readable scoped snapshot](research-control-lifecycle-summary-through-2026-10-28.json). The [October 29 clock correction](../monitoring/2026-10-29/01-bounded-contract-recheck/clock-provenance-correction.md) is a separate later correction, not a retrospective change to the October 28 Git tree.

**Independent lifecycle closeout through October 31, 2026:** [First-day-to-current pinned Git history, source-freshness audit and corrections](research-control-lifecycle-closeout-through-2026-10-31.md) · [96-commit ledger](research-control-main-history-through-2026-10-31.csv) · [499-file pinned Git tree](research-control-tracked-files-through-2026-10-31.csv) · [77-PR ledger](research-control-pr-history-through-2026-10-31.csv) · [11 core main refs](research-core-main-heads-2026-10-31.csv) · [independent 34-surface access outcomes](research-independent-34-surface-access-2026-10-31.csv) · [bounded RS01 seven-platform outcomes](research-seven-platform-bounded-rs01-2026-10-31.csv) · [late machine-index correction history](research-historical-machine-record-reconciliation-2026-10-31.md). This is a later **retrospective diagnostic snapshot**, not a substitute for the October 28 pinned report or a prospective observation.

**2026-11-03 first-day-to-current governance reconciliation:** [Pinned 104-commit / 620-file source and classification audit](research-control-first-day-to-current-governance-audit-2026-11-03.md) · [620 Git-blob file catalog](research-control-file-ownership-snapshot-2026-11-03.csv) · [104 Git commits with actual clocks](research-control-main-commit-chronology-2026-11-03.csv) · [58 existing diagnostic event directories](research-control-dated-event-classification-2026-11-03.csv) · [OSF original versus approved revision authority](../contract/osf-registration-version-governance-2026-11-03.md). All totals are pinned to the **pre-audit** main commit `b6aa40231bcba62da98e089673652839952118cf`; subsequent correction files are **outside** that historical inventory. The full file catalog is path/identity-level classification, **not** per-file source-body validation.

**2026-11-05 complete first-day-to-current file maintenance and source-identity audit:** [Pinned 110-commit / 637-file / 91-PR review](research-control-first-day-to-2026-11-05-file-maintenance.md) · [637 Git path/blob/size ledger](research-control-tracked-files-through-2026-11-05.csv) · [110-commit chronology](research-control-main-history-through-2026-11-05.csv) · [91-PR status ledger](research-control-pr-history-through-2026-11-05.csv) · [61 monitoring event and 20 evidence companion path ledger](research-control-dated-events-through-2026-11-05.csv) · [17 added / 7 modified / 0 deleted file-identity reconciliation](research-control-file-delta-since-2026-11-03.csv). These exact counts are pinned to the **pre-maintenance** `main` `3356cea9609a4cc4744fa071fc6b42f05488b9c5`; current-branch repair files do not retroactively count as already present. Historic source records remain unchanged and no formal prospective cells are created.

**2026-11-08 CONTROL-only first-day-to-current file governance:** [Pinned 130-commit / 703-file path-and-blob classification closeout](repository-inventory/2026-11-08/README.md), [703-row catalog](repository-inventory/2026-11-08/control-tracked-paths.csv), [46 added / 6 changed / 0 removed delta](repository-inventory/2026-11-08/control-delta-since-2026-11-06.csv), [20 newer commits](repository-inventory/2026-11-08/main-commits-since-2026-11-05.csv), [12 retained same-blob groups](repository-inventory/2026-11-08/control-identical-blob-review.csv). Only the independent research-control repository is in scope; original contracts and historical files are unchanged. File identity classification is complete for the pinned tree; full body-level scientific review remains partial.

**2026-11-10 CONTROL-only pinned first-day-to-current cleanup and file governance:** [135-commit / 106-PR / 724-file current-tree audit and explicit no-deletion disposition](repository-inventory/2026-11-10/README.md) · [complete 724-path Git-object catalog](repository-inventory/2026-11-10/control-tracked-paths.csv) · [21 added / 2 modified / 0 removed comparison](repository-inventory/2026-11-10/control-delta-since-2026-11-08.csv) · [12 retained identical-blob review groups](repository-inventory/2026-11-10/control-identical-blob-review.csv). Older dated source inventories remain frozen; small `.gitignore` excludes only standard local execution byproducts, not scholarly evidence or failure records.

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

## Operational logic assurance (2026-10-25)

[Observation assurance and claim boundaries](observation-assurance-2026-10-25.md) documents what the existing checker can reject and what still requires researcher/source-evidence acceptance: seven platform-to-layer joins, clock comparability, prospective preflight, independent source attribution, projection versus raw bytes, incomplete retrievals, and non-equivalent counters. It is an **implementation review**, not a new OSF research contract, observation, amendment, scheduled timepoint, or data update. The synthetic unit-test entry is in [tools](../tools/README.md#observation-semantic-preflight-2026-10-25).


## Public manifest coverage reconciliation (2026-10-26)

[The dated integrity-check coverage review](public-manifest-coverage-reconciliation-2026-10-26.md) documents why the old hard-coded October 25 manifest entry did not automatically cover the October 26 morning/evening published artifacts, and the read-only, standard-library `--all` discovery fix. It changes **checker coverage**, not historical evidence, OSF contract, baseline, schedule, platform counters or prospective dataset. The CI check remains advisory; consult the step result before claiming that all published bytes passed verification.


## Seven-platform evidence semantics (2026-10-25)

[The seven-platform reviewer decision map](platform-evidence-semantics-2026-10-25.md) records each platform's concrete object grain, positive and negative claim boundaries, retrieval-clock interpretation, exact source links and invalid cross-platform implications. It is a **non-data implementation review** that does not amend OSF or create a new analytic layer. Apply this guide when reviewing assertions supported by GitHub, Zenodo, DataCite, ORCID, Software Heritage, OpenAIRE or OpenAlex.

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

## October 24 dated record classification and naming review

The [source-bounded path classification review](record-path-classification-review-2026-10-24.md) explains monitoring versus evidence ownership, documents four additive historical entrypoints, and preserves compatibility between historical `record.yaml` and later `record.json` summaries. Read the [normative path and migration rules](../monitoring/NAMING.md) and run the [offline path checker](../tools/check_record_paths.py) for structural integrity. The checker is advisory in CI; neither green workflow status nor path normalization creates a prospective observation or certifies original research evidence

## 2026-11-06 cross-repository file identity and OSF workspace inventory

[Complete 11-repository tracked-file inventory and documentation classification](repository-inventory/2026-11-06/README.md) pins the ten fixed RS01–RS10 repository trees plus the separate CONTROL tree: **8,802 Git-tracked blobs across 11 repositories**, each CSV retaining source main SHA, path, blob SHA, Git-reported byte size and deterministic path classification. The classification is path-level orientation, not semantic content review. Existing Daily/Weekly/Monthly records, historical audits, source archives, generated sidecars and recovered workflow backups are preserved; this pass performs no source rename or deletion.

The same report records the public OSF boundary: frozen Registration 5b329 remains separate; Associated Project wa5v8 is an entry-point surface with empty native OSF storage and a GitHub provider mirroring CONTROL, not a second source-of-truth file store. No authenticated OSF write connector was available, so no OSF mutation was attempted. It also records the process deviation that the ten RS catalogs were added directly to CONTROL main before the remaining report/catalog changes were moved onto a review branch.

**2026-11-06 cloud asset organization and OSF surface reconciliation:** [11-core-repository current-tree reconciliation, three ancillary repositories, document taxonomy/preservation decisions and OSF Registration/Project provider inventory](repository-inventory/2026-11-06/cloud-asset-organization-and-osf-surface-2026-11-06.md) · [ancillary repository register](repository-inventory/2026-11-06/ancillary-repositories.csv) · [OSF surface ledger](repository-inventory/2026-11-06/osf-surface-register.csv). This is a retrospective asset inventory, not a prospective observation or OSF amendment.

## 2026-11-07 follow-up: current path hygiene and advisory CI correction

[Exact 11-main Git-tree identity delta and bounded cleanup decision](repository-inventory/2026-11-07/README.md) pins **8,873 tracked path entries** across fixed RS01–RS10 plus separate CONTROL, without treating path counts as research units or file bodies as independently reviewed. It finds no high-confidence temporary-file pathname candidate and therefore performs **no speculative deletion**. The same review links the [November 7 machine-record / surface ledger / monitoring index reconciliation](../monitoring/2026-11-07/01-periodic-identity-infrastructure-recheck/reconciliation.md) and the original advisory checker exit-code failure hidden by overall workflow-level success. Historical source files, OSF contract and prospective status are preserved
