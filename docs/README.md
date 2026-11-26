# Documentation map and maintenance guide

## Current OSF authority — 2026-11-24

This repository supports **two independent formal OSF prospective observational studies**. Their current approved schema responses, not a shared GitHub document or a project-level Description, govern each study's protocol.

- **Study 1 — OSF 5b329:** current approved response [6afdcc3a7fb0a89b0e3dd7e4](https://api.osf.io/v2/schema_responses/6afdcc3a7fb0a89b0e3dd7e4/), submitted 2026-11-18 and approved. It confirms RS01–RS10, six analytical layers, seven operational platforms, 60 object-layer units per scheduled point, and RSIA's supporting infrastructure role. It does not change the observation schedule. Read the [current revision crosswalk](../studies/osf-wa5v8/day1/contract/osf-approved-revision-2026-11-18.md).
- **Study 2 — OSF VSHWK:** current approved response [6afdcc7108de91a0f0cefd6c](https://api.osf.io/v2/schema_responses/6afdcc7108de91a0f0cefd6c/), submitted 2026-11-18 and approved. It defines Project 490 with lineages 2332 v9 and 2334 v9, and repeated event- or documented-review-initiated cycles without fixed calendar intervals, wave count, or end date. The VSHWK registration Description was subsequently updated on 2026-11-24; that metadata update is not a new schema amendment.
- **AUHJF** is the separate public project entry point, not a substitute for the VSHWK registration. Its project Description retains the original 2347 v2 / three-wave wording as historical project-level text.

Formal preregistration status, operational execution details, monitoring diagnostics, and successful external-provider retrieval are separate dimensions. A provider failure does not invalidate an OSF registration; a diagnostic record does not become a prospective observation merely because it was collected later.

## 2026-11-17 bilingual scholarly-control navigation / 双语科研控制合同导航

**文档责任 / Ownership:** 这是只读导航和解释层，非注册合同、统计 schema、科研观察或研究原始记录的修订 / This is an explanatory pointer only, not a study amendment, new observation or executable schema change

| Canonical owner / 原始拥有者 | 中文解释 / Chinese reading key | English evidence boundary |
| --- | --- | --- |
| [Frozen preregistration](../contract/preregistration.md) | 十个固定研究软件对象与六类基础设施层，每次合格观测的分析单位为六十 | The frozen OSF registration remains the sole owner of preregistered scope |
| [Known limitations](../contract/known-limitations.md) | 不可用的来源、未知索引时钟和缺少原始响应字节不能自动补齐 | Missing, failed or inaccessible provider records remain typed unknowns |
| [OSF Overview crosswalk](../contract/osf-overview-crosswalk-2026-10-08.md) | 早期条款解释保留原观察截点与当时未知 | A dated crosswalk does not silently absorb later OSF version evidence |
| [OSF registration versions](../contract/osf-registration-version-governance-2026-11-03.md) | 原始注册与后续获批修订是两个来源身份，不回填为同一历史版本 | Approved revisions do not retroactively modify the original registration text |
| [Current 2026-11-18 approved 5b329 revision](../studies/osf-wa5v8/day1/contract/osf-approved-revision-2026-11-18.md) | 当前 5b329 获批版本与 RSIA 支撑基础设施边界 | Current approved authority is distinct from the original and 2026-10-06 revisions |
| [Counting rules](../schema/counting-rules.md) | 预注册的六十个对象层单位不同于七个平台潜在的七十个检查 | `10 × 6 = 60` planned analytic cells and `10 × 7 = 70` platform checks are distinct |
| [Analysis guidance](../analysis/README.md) | 描述性主分析、探索性计算和正式前瞻观测须分开 | Exploratory analysis is not newly preregistered primary inference |
| [Historical baseline](../baseline/README.md) | 基线身份不会由后续重新采集更改 | Later reconciliations cannot rewrite historical observation time |
| [Provenance index](../provenance/README.md) | 原始响应、外部服务字段、衍生表和文档解释各自有来源 | Raw, derived, presentation and later interpretation are separate evidence grades |
| [Amendment ledger](../AMENDMENTS.md) | 仅真实、单独审批的正式研究修订才能形成 amendment 条目 | An explanatory translation is not a new formal amendment |
| [Deviation ledger](../DEVIATIONS.md) | 保留 2026-11-06 的真实仓库维护偏差与修正链 | The recorded direct-main process deviation remains historically visible |

**当前发行身份 / Release identity:** The November 15 GitHub Release is distinct from the October 31 exact-version Zenodo DOI, whose last independently documented value is `10.5281/zenodo.23839900`, and the November 15 new version DOI is not verified by this document / 新的 GitHub Release 不能继承旧 Zenodo 版本 DOI

**门禁 / Review gate:** Under the existing [documentation-only acceptance boundary](#4-docs-only-maintenance-workflow), this page may clarify contract owners but may not edit their files or silently create research findings / 本文仅承担中英导航，受保护合同的任何内容变更需独立合同审查


This file is an **orientation and contribution guide** for the live GitHub research-control repository. It is **not** a new research protocol, operational schedule, observation, correction event, or amendment of either registered OSF study: [5b329](https://osf.io/5b329/overview) or [VSHWK](https://osf.io/vshwk/overview).

For the scientific background start with the [main README](../README.md); for the research-production discipline see [OPEN_RESEARCH.md](../OPEN_RESEARCH.md). The DOI of the separate frozen research plan is [10.17605/OSF.IO/5B329](https://doi.org/10.17605/OSF.IO/5B329).


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

Read the repository by **ownership and evidence role**, not by assuming every top-level directory has the same temporal status. The physical layout intentionally has three cooperating areas:

1. **Current study workspaces — `studies/`:** the two OSF studies have separate namespaces and daily indexes. Day folders organize work; they do not create OSF waves, scheduled timepoints, or new analytical units.
2. **Study 1's established root surfaces and retained history:** its canonical `contract/`, `corpus/`, `schema/`, and `schedule/` remain at the root. The frozen `baseline/` remains at its canonical root path; former root-level diagnostics and evidence are consolidated under `history/diagnostics/` and `history/evidence/`. `observations/raw/` remains a reserved eligibility-governed prospective surface, not a general historical archive.
3. **Shared CONTROL engineering and documentation:** `tools/`, `tests/`, `.github/`, reusable templates, provenance guidance, and repository navigation support both studies without merging their scientific records.

| Owner | Contents and canonical entry | Change boundary |
| --- | --- | --- |
| `studies/` | [Two-study index and Day 0–2 matrix](../studies/README.md); [Study 1 wa5v8 workspace](../studies/osf-wa5v8/README.md); [Study 2 VSHWK workspace](../studies/osf-vshwk/README.md) | Separate OSF ownership. Day indexes point to canonical records; they do not copy evidence or imply a fixed wave count |
| `contract/` | Study 1 [frozen registration mapping](../contract/preregistration.md), [OSF Overview crosswalk](../contract/osf-overview-crosswalk-2026-10-08.md), and [known limitations](../contract/known-limitations.md) | Study 1 root-level contract mapping only; OSF registration and approved responses remain authoritative |
| `corpus/` | [Fixed-object manifest](../corpus/object-manifest.csv) | Exactly RS01–RS10; no new sample via documentation |
| `schema/` | [Counting rules](../schema/counting-rules.md), [layers](../schema/infrastructure-layers.yaml), [platforms](../schema/platforms.yaml), [state vocabulary](../schema/state-taxonomy.yaml), [observation JSON schema](../schema/observation.schema.json) | Study 1 contract-aware schema; changes require separate review |
| `schedule/` | [Registered timing rules and operational schedule record](../schedule/README.md) | Study 1 schedule authority; do not invent numerical offsets absent from the approved OSF response |
| `baseline/` | [Historical baseline](../baseline/README.md) and [2026-10-05 package](../baseline/2026-10-05/README.md) | Frozen historical cutoff **2026-10-05 23:59:59 Asia/Shanghai**; later retrieval is not historical capture |
| `history/diagnostics/` | [Historical diagnostic archive](../history/diagnostics/README.md) | Frozen root-level diagnostics; no new acquisitions belong here |
| `history/evidence/` | [Historical evidence archive](../history/evidence/README.md) | Frozen root-level packages; original payload bytes, source clocks and manifests remain intact |
| `observations/raw/` | [Prospective raw observation location](../observations/raw/README.md) | Reserved for eligible, schedule-governed Study 1 records; not a destination for historical monitoring |
| `observations/derived/` | [Derived observation location](../observations/derived/README.md) | Derivations must cite actual raw observations; missing values are not imputed |
| `provenance/` | [Provenance policy](../provenance/README.md) | Preserve source → raw → derived → interpretation lineage and correction history |
| `analysis/` | [Descriptive research analysis](../analysis/README.md) | Keep exploratory work identified; no unregistered causal or inferential model |
| `scholarly/` | [Scholarly and archive index](../scholarly/README.md), [citation guide](../scholarly/CITATION.md) | Keep control-repository citation identity, OSF registration identity and external research-object identifiers distinct; dated reviews remain historical |
| `history/documentation/` | [Historical repository documentation](../history/documentation/README.md) | Dated audits, method reviews and closeouts; not current contract authority |
| `history/repository-inventory/` | [Pinned repository inventory packages](../history/repository-inventory/README.md) | Point-in-time snapshots; not current HEAD counts or research observations |
| `templates/` | [Reusable research templates](../templates/README.md), [human-facing template](../RESEARCH_TEMPLATE.md) | Templates are structure aids, not completed observations or evidence |
| `tools/` | [Offline and contract checker commands](../tools/README.md) | Validation establishes only the properties each checker actually tests |
| `tests/` | Synthetic and regression tests for repository contracts and tooling | Tests exercise implementation behavior; they do not establish external platform truth |
| `.github/` | [PR template](../.github/PULL_REQUEST_TEMPLATE.md), [CI workflow](../.github/workflows/validate.yml), issue templates | PR/issue automation is shared engineering support, not a change to either research contract |
| `docs/` | This current documentation map plus the separately classified historical subdirectories above | Navigation and maintenance instructions, not observational evidence |
| `RELEASE_POLICY.md` and root governance files | [Immutable release policy](../RELEASE_POLICY.md), amendments, deviations, data handling and open-research guidance | Repository governance and release history; not a substitute for either OSF registration |

**Existing root paths are deliberately retained.** Do not move or rename root-level `monitoring/`, `evidence/`, `baseline/`, or `provenance/` paths for cosmetic organization. Their manifests, source locators, hashes, PR links and paper references may depend on those paths. Historical documentation is classified under `docs/history/`; dated repository inventories remain under `docs/repository-inventory/`. The Study 2 day indexes under `studies/osf-vshwk/day*/` are navigation-only pointers to the canonical cycle and custody records.
## 3. Read a result without mixing evidence levels

Follow the narrowest source that actually supports the claim:

1. **Source evidence** — original platform response or explicitly attributed user-supplied text, with locator and actual retrieval interval.
2. **Raw observation** — response state and fields as seen, including 404, 429, timeout, blocked, degraded and partial.
3. **Normalized or derived observation** — explicit identity join, counter semantics, calculation rule and raw references.
4. **Interpretation** — bounded research judgment, alternative explanations and remaining unknowns.
5. **Reported conclusion** — claim tied back to a dated evidence chain and its amendments/corrections.

A later public endpoint does not replay a historical state. A DOI or successful CI run does not prove execution, adoption or scientific validity. Zenodo `views` and `unique_views` are distinct source fields; WorkflowHub Dashboard counts and per-version Activity need their own reporting window and entity-grain checks. A summed family-level unique counter is **not** a globally deduplicated number of people. Use the [existing counting rules](../schema/counting-rules.md); this guide adds **no new metric definitions**.

## Operational logic assurance (2026-10-25)

[Observation assurance and claim boundaries](../history/documentation/method-and-integrity-reviews/observation-assurance-2026-10-25.md) documents what the existing checker can reject and what still requires researcher/source-evidence acceptance: seven platform-to-layer joins, clock comparability, prospective preflight, independent source attribution, projection versus raw bytes, incomplete retrievals, and non-equivalent counters. It is an **implementation review**, not a new OSF research contract, observation, amendment, scheduled timepoint, or data update. The synthetic unit-test entry is in [tools](../tools/README.md#observation-semantic-preflight-2026-10-25).


## Public manifest coverage reconciliation (2026-10-26)

[The dated integrity-check coverage review](../history/documentation/method-and-integrity-reviews/public-manifest-coverage-reconciliation-2026-10-26.md) documents why the old hard-coded October 25 manifest entry did not automatically cover the October 26 morning/evening published artifacts, and the read-only, standard-library `--all` discovery fix. It changes **checker coverage**, not historical evidence, OSF contract, baseline, schedule, platform counters or prospective dataset. The CI check remains advisory; consult the step result before claiming that all published bytes passed verification.


## Seven-platform evidence semantics (2026-10-25)

[The seven-platform reviewer decision map](../history/documentation/method-and-integrity-reviews/platform-evidence-semantics-2026-10-25.md) records each platform's concrete object grain, positive and negative claim boundaries, retrieval-clock interpretation, exact source links and invalid cross-platform implications. It is a **non-data implementation review** that does not amend OSF or create a new analytic layer. Apply this guide when reviewing assertions supported by GitHub, Zenodo, DataCite, ORCID, Software Heritage, OpenAIRE or OpenAlex.

## 4. Docs-only maintenance workflow

**Documentation scope:** a documentation-only PR may fix navigation, link targets, terminology, accessibility, contributor guidance, or dated operational explanations. It must not insert new API results, tables of newly observed counts, prospective records, fake historical timestamps, new releases, or made-up verification outcomes.

1. Read fresh `main`, open PRs, the [OSF contract mapping](../contract/preregistration.md), relevant schema and the documents being changed. Prefer the smallest reviewable branch.
2. Decide whether the claim belongs to **durable documentation** (e.g. folder purpose) or a **dated source/monitoring record** (e.g. October API counters). Put it in the owner, without rewriting a past observation.
3. Preserve existing evidence/provenance files, stable paths, correction history and historical author/source attribution. To correct historical interpretation, create a separately attributed correction through the established research process, **not** a docs cleanup.
4. Review relative Markdown links against the branch tree. Keep file names, anchors and reference scopes unambiguous. Prefer links to canonical owners rather than duplicating mutable figures on the landing page.
5. Run the configured advisory contract check (if executable in the actual environment): `python tools/check.py --mode advisory`. If relevant, run `--mode strict` as an explicitly separate local check; do **not** present an unrun command as success.
6. In the PR state **which checks actually ran**, which were blocked/not executed, the exact changed files, scope constraints, and any unresolved evidence. Review the changed-file diff and CI, merge when appropriate, then verify `main` and its workflow run.

**Documentation-only acceptance boundary:** no changes to `contract/`, `corpus/`, `baseline/`, `schedule/`, `schema/`, `observations/`, `history/` archive payloads, `provenance/`, or `analysis/` data/scripts; no changes to `.zenodo.json`, `CITATION.cff`, `codemeta.json`, Git tags or OSF records. An explanatory link to those files is fine. See [CONTRIBUTING.md](../CONTRIBUTING.md), [data handling](../DATA_HANDLING.md), and [licensing](../LICENSING.md).

## 5. External OSF service lifecycle (not a contract amendment)

The [OSF Projects transition guidance](https://help.osf.io/article/727-osf-projects-transition) states that OSF Projects stop accepting new projects/components **November 16, 2026** and existing projects are planned to become read-only **February 19, 2027**. [OSF's registration-specific guidance](https://help.osf.io/article/770-registrations) says **registrations/preregistrations are not affected** by that Projects transition. These are **externally published prospective service-policy dates**, not observed changes to this project's October 2026 state or to the frozen research contract.

Operationally keep the *associated OSF Project*, the *independent OSF Registration*, GitHub's mutable executable runtime, and Zenodo's immutable release archives separate. Check the official OSF documentation again before a future migration decision. Do not move or re-register evidence merely because a service-policy notice exists.

---

This page is an **index and maintenance explanation only**. When a summary disagrees with a frozen registration, source record, schema, or retained observation, consult the owning source and preserve the discrepancy instead of silently editing the historical record.

## Historical repository inventory and review index

The former dated reports and catalogs previously mixed into the `docs/` root are now **physically classified** under [historical documentation](../history/documentation/README.md), with a [path-to-original-Git-blob migration ledger](../history/migrations/path-migration-2026-11-25.csv). The existing dated `repository-inventory/` packages retain their own folder identities.

The dated catalogs, snapshots, closeouts, and review notes below are point-in-time material, not present-tense contract authority or newly eligible prospective observations. The original source links, claims, qualifiers, and retrieval boundaries are retained. Consult the current directory/ownership map and docs-only maintenance guidance above before using these historical records.

## 2026-11-20 all eleven repositories — complete current tracked paths

[All 11 pinned source Git trees: 9,675 file paths and 11 exact Nov 6→Nov 20 per-repo delta ledgers](../history/repository-inventory/2026-11-20/cross-repositories/README.md), with original and current path membership, exact Git blobs, byte sizes and strictly separated CONTROL role. This is a non-atomic multi-repo path-level survey and does **not** claim full body/semantic verification

## Latest: 2026-11-20 complete first-day-to-current CONTROL source tree

[Exact pinned 903-file Git blob catalog, 158 reachable-main commit chronology and 83 dated monitoring event classification](../history/repository-inventory/2026-11-20/README.md) · [November 19 source branch custody correction](../history/repository-inventory/2026-11-20/source-branch-custody-reconciliation.md) · [November 20 bounded platform diagnostic](../history/diagnostics/2026-11-20/01-firstday-to-current-infrastructure-diagnostic/README.md)

All are retrospective documentation / current diagnostic records, **not** changes to the OSF frozen study, historical source bodies or prospective observation schedule


**Historical research-session handoff (2026-10-18):** [research session closeout and reproducibility handoff](../history/documentation/diagnostic-and-closeout-reviews/research-session-closeout-2026-10-18.md). It crosswalks public evidence, the frozen OSF contract, four actually published control releases (including [October 18 postpublication reconciliation](../scholarly/release-identity-reconciliation-2026-10-18.md)), the user-confirmed Beta ORCID metadata refresh, and outstanding verification gates. It is a *historical review*, not a standing claim about all future `main` commits or live platform counters.

**Dated full-repository inventory (October 21, 2026):** [Control repository classification and evolution report](../history/documentation/inventory-ledgers/control-repository-inventory-2026-10-21.md), [complete tracked-file path catalog](../history/documentation/inventory-ledgers/control-repository-file-catalog-2026-10-21.csv), and [chronological main commit ledger](../history/documentation/inventory-ledgers/control-repository-main-commit-ledger-2026-10-21.csv). These inventory artifacts are documentation snapshots, not research observations or an RS11 designation.

**Historical source inventory through 2026-10-28:** [Lifecycle and OSF-contract audit](../history/documentation/inventory-ledgers/control-repository-lifecycle-audit-through-2026-10-28.md) · [full main-history ledger](../history/documentation/inventory-ledgers/control-repository-main-history-through-2026-10-28.csv) · [437 tracked paths with original Git blob SHAs](../history/documentation/inventory-ledgers/control-repository-tracked-files-through-2026-10-28.csv) · [machine-readable scoped snapshot](../history/documentation/inventory-ledgers/research-control-lifecycle-summary-through-2026-10-28.json). The [October 29 clock correction](../history/diagnostics/2026-10-29/01-bounded-contract-recheck/clock-provenance-correction.md) is a separate later correction, not a retrospective change to the October 28 Git tree.

**Independent lifecycle closeout through October 31, 2026:** [First-day-to-current pinned Git history, source-freshness audit and corrections](../history/documentation/inventory-ledgers/research-control-lifecycle-closeout-through-2026-10-31.md) · [96-commit ledger](../history/documentation/inventory-ledgers/research-control-main-history-through-2026-10-31.csv) · [499-file pinned Git tree](../history/documentation/inventory-ledgers/research-control-tracked-files-through-2026-10-31.csv) · [77-PR ledger](../history/documentation/inventory-ledgers/research-control-pr-history-through-2026-10-31.csv) · [11 core main refs](../history/documentation/inventory-ledgers/research-core-main-heads-2026-10-31.csv) · [independent 34-surface access outcomes](../history/documentation/diagnostic-and-closeout-reviews/research-independent-34-surface-access-2026-10-31.csv) · [bounded RS01 seven-platform outcomes](../history/documentation/diagnostic-and-closeout-reviews/research-seven-platform-bounded-rs01-2026-10-31.csv) · [late machine-index correction history](../history/documentation/diagnostic-and-closeout-reviews/research-historical-machine-record-reconciliation-2026-10-31.md). This is a later **retrospective diagnostic snapshot**, not a substitute for the October 28 pinned report or a prospective observation.

**2026-11-03 first-day-to-current governance reconciliation:** [Pinned 104-commit / 620-file source and classification audit](../history/documentation/inventory-ledgers/research-control-first-day-to-current-governance-audit-2026-11-03.md) · [620 Git-blob file catalog](../history/documentation/inventory-ledgers/research-control-file-ownership-snapshot-2026-11-03.csv) · [104 Git commits with actual clocks](../history/documentation/inventory-ledgers/research-control-main-commit-chronology-2026-11-03.csv) · [58 existing diagnostic event directories](../history/documentation/inventory-ledgers/research-control-dated-event-classification-2026-11-03.csv) · [OSF original versus approved revision authority](../contract/osf-registration-version-governance-2026-11-03.md). All totals are pinned to the **pre-audit** main commit `b6aa40231bcba62da98e089673652839952118cf`; subsequent correction files are **outside** that historical inventory. The full file catalog is path/identity-level classification, **not** per-file source-body validation.

**2026-11-05 complete first-day-to-current file maintenance and source-identity audit:** [Pinned 110-commit / 637-file / 91-PR review](../history/documentation/inventory-ledgers/research-control-first-day-to-2026-11-05-file-maintenance.md) · [637 Git path/blob/size ledger](../history/documentation/inventory-ledgers/research-control-tracked-files-through-2026-11-05.csv) · [110-commit chronology](../history/documentation/inventory-ledgers/research-control-main-history-through-2026-11-05.csv) · [91-PR status ledger](../history/documentation/inventory-ledgers/research-control-pr-history-through-2026-11-05.csv) · [61 monitoring event and 20 evidence companion path ledger](../history/documentation/inventory-ledgers/research-control-dated-events-through-2026-11-05.csv) · [17 added / 7 modified / 0 deleted file-identity reconciliation](../history/documentation/inventory-ledgers/research-control-file-delta-since-2026-11-03.csv). These exact counts are pinned to the **pre-maintenance** `main` `3356cea9609a4cc4744fa071fc6b42f05488b9c5`; current-branch repair files do not retroactively count as already present. Historic source records remain unchanged and no formal prospective cells are created.

**2026-11-08 CONTROL-only first-day-to-current file governance:** [Pinned 130-commit / 703-file path-and-blob classification closeout](../history/repository-inventory/2026-11-08/README.md), [703-row catalog](../history/repository-inventory/2026-11-08/control-tracked-paths.csv), [46 added / 6 changed / 0 removed delta](../history/repository-inventory/2026-11-08/control-delta-since-2026-11-06.csv), [20 newer commits](../history/repository-inventory/2026-11-08/main-commits-since-2026-11-05.csv), [12 retained same-blob groups](../history/repository-inventory/2026-11-08/control-identical-blob-review.csv). Only the independent research-control repository is in scope; original contracts and historical files are unchanged. File identity classification is complete for the pinned tree; full body-level scientific review remains partial.

**2026-11-10 CONTROL-only pinned first-day-to-current cleanup and file governance:** [135-commit / 106-PR / 724-file current-tree audit and explicit no-deletion disposition](../history/repository-inventory/2026-11-10/README.md) · [complete 724-path Git-object catalog](../history/repository-inventory/2026-11-10/control-tracked-paths.csv) · [21 added / 2 modified / 0 removed comparison](../history/repository-inventory/2026-11-10/control-delta-since-2026-11-08.csv) · [12 retained identical-blob review groups](../history/repository-inventory/2026-11-10/control-identical-blob-review.csv). Older dated source inventories remain frozen; small `.gitignore` excludes only standard local execution byproducts, not scholarly evidence or failure records.

## October 18 research-only independent verification

The [dated research record](../history/diagnostics/2026-10-18/03-independent-research-verification/README.md) owns the new measurements and archive inspection. The [minimized evidence package](../history/evidence/2026-10-18/03-independent-research-verification/README.md) declares public-field versus locally retained transport evidence. The standalone offline checker makes no network requests. **Historically**, it was not in CI when this October 18 note was written; the current [validation workflow](../.github/workflows/validate.yml) now runs the October 18 and October 20 package checkers as **advisory** steps. Neither their presence nor a green workflow retroactively establishes independent raw transport replay. Community correspondence, account operations, private monitoring identifiers and unrelated telemetry are outside this contribution.

## October 24 dated record classification and naming review

The [source-bounded path classification review](../history/documentation/method-and-integrity-reviews/record-path-classification-review-2026-10-24.md) explains monitoring versus evidence ownership, documents four additive historical entrypoints, and preserves compatibility between historical `record.yaml` and later `record.json` summaries. Read the [normative path and migration rules](../history/diagnostics/NAMING.md) and run the [offline path checker](../tools/check_record_paths.py) for structural integrity. The checker is advisory in CI; neither green workflow status nor path normalization creates a prospective observation or certifies original research evidence

## 2026-11-06 cross-repository file identity and OSF workspace inventory

[Complete 11-repository tracked-file inventory and documentation classification](../history/repository-inventory/2026-11-06/README.md) pins the ten fixed RS01–RS10 repository trees plus the separate CONTROL tree: **8,802 Git-tracked blobs across 11 repositories**, each CSV retaining source main SHA, path, blob SHA, Git-reported byte size and deterministic path classification. The classification is path-level orientation, not semantic content review. Existing Daily/Weekly/Monthly records, historical audits, source archives, generated sidecars and recovered workflow backups are preserved; this pass performs no source rename or deletion.

The same report records the public OSF boundary: frozen Registration 5b329 remains separate; Associated Project wa5v8 is an entry-point surface with empty native OSF storage and a GitHub provider mirroring CONTROL, not a second source-of-truth file store. No authenticated OSF write connector was available, so no OSF mutation was attempted. It also records the process deviation that the ten RS catalogs were added directly to CONTROL main before the remaining report/catalog changes were moved onto a review branch.

**2026-11-06 cloud asset organization and OSF surface reconciliation:** [11-core-repository current-tree reconciliation, three ancillary repositories, document taxonomy/preservation decisions and OSF Registration/Project provider inventory](../history/repository-inventory/2026-11-06/cloud-asset-organization-and-osf-surface-2026-11-06.md) · [ancillary repository register](../history/repository-inventory/2026-11-06/ancillary-repositories.csv) · [OSF surface ledger](../history/repository-inventory/2026-11-06/osf-surface-register.csv). This is a retrospective asset inventory, not a prospective observation or OSF amendment.

## 2026-11-07 follow-up: current path hygiene and advisory CI correction

[Exact 11-main Git-tree identity delta and bounded cleanup decision](../history/repository-inventory/2026-11-07/README.md) pins **8,873 tracked path entries** across fixed RS01–RS10 plus separate CONTROL, without treating path counts as research units or file bodies as independently reviewed. It finds no high-confidence temporary-file pathname candidate and therefore performs **no speculative deletion**. The same review links the [November 7 machine-record / surface ledger / monitoring index reconciliation](../history/diagnostics/2026-11-07/01-periodic-identity-infrastructure-recheck/reconciliation.md) and the original advisory checker exit-code failure hidden by overall workflow-level success. Historical source files, OSF contract and prospective status are preserved
