# Cross-repository tracked-file inventory and documentation classification — 2026-11-06

**Purpose:** establish a pinned, machine-readable path/blob/size inventory for the ten fixed research-software repositories plus the separate research-control repository, and provide a single navigation and preservation policy.

**Snapshot clock:** GitHub connected-source reads during 2026-11-06. The source queries were sequential/batched, not an atomic 11-repository transaction. Each CSV pins the exact source main commit used for its recursive tree. All 11 GitHub recursive trees returned truncated=false.

## 1. Object boundary and pinned source trees

| Object | Repository | Pinned source main | Tracked blobs |
|---|---|---|---:|
| RS01 | [welcome-to-github](https://github.com/lostlight530/welcome-to-github) | 46107dc7a3857008868ec5341d451d2355ae0b5f | 1,549 |
| RS02 | [zero-entropy-lab](https://github.com/lostlight530/zero-entropy-lab) | d7c605f83bcd423601bea1e79cca496ddf646b56 | 2,344 |
| RS03 | [Axiom-0](https://github.com/lostlight530/Axiom-0) | aa1c692c10a371e7815034bcc81f05b644bf6444 | 509 |
| RS04 | [reflective-continuum](https://github.com/lostlight530/reflective-continuum) | 2cbbd11710cb45efadb2b7980861740784b0ef6b | 617 |
| RS05 | [agent-foundations](https://github.com/lostlight530/agent-foundations) | 79474f8efa89dc549b5893558decb0170eaab605 | 160 |
| RS06 | [auto-doc-engine](https://github.com/lostlight530/auto-doc-engine) | 7eb7bd903d9b0a118df89533f857f4f1c2088c98 | 336 |
| RS07 | [epistemic-pipeline](https://github.com/lostlight530/epistemic-pipeline) | 5817bd41ec9922fc29ca78c9291fbb06786f3649 | 337 |
| RS08 | [sci-render-kit](https://github.com/lostlight530/sci-render-kit) | 003e8c9691c00cad7ab4c6336bb00a475f6815ef | 347 |
| RS09 | [china-agentic-observatory](https://github.com/lostlight530/china-agentic-observatory) | 43035f9af841a7e7d8fb83bf3c1d3d191faac9ab | 1,013 |
| RS10 | [agentic-frontier-observatory](https://github.com/lostlight530/agentic-frontier-observatory) | 9afbc25a74e1cf825b7598de4c83d6a82f004140 | 933 |
| CONTROL | [research-software-identity-audit](https://github.com/lostlight530/research-software-identity-audit) | 44b3defa6a67cf0eb45b6519fc8245827731c7a6 | 657 |

**Total: 8,802 Git-tracked file blobs across 11 repositories.** This is a tree-entry count, not 8,802 individually content-reviewed documents. CONTROL is the research contract/runtime/evidence repository and is not RS11.

The CONTROL repository's first-day-to-current Git history is continued from the November 5 pinned 110-commit report by the [12-commit delta ledger](control-main-commit-delta-since-2026-11-05.csv). GitHub compare from the first commit on 2026-10-05 to the current source main reports 121 commits ahead of the first commit (122 reachable commits including the initial commit). The delta includes the merged November 5 full-tree audit, the merged November 6 diagnostic patrol and ten direct-main catalog additions; the latter are explicitly recorded as a process deviation below.

## 2. Machine-readable catalogs

Each CSV records repository and object ID, exact pinned source main commit, tracked path, Git blob SHA, Git-reported byte size, deterministic path classification, and extension.

| Object | Catalog |
|---|---|
| RS01 | [rs01-welcome-to-github-tracked-paths.csv](rs01-welcome-to-github-tracked-paths.csv) |
| RS02 | [rs02-zero-entropy-lab-tracked-paths.csv](rs02-zero-entropy-lab-tracked-paths.csv) |
| RS03 | [rs03-axiom-0-tracked-paths.csv](rs03-axiom-0-tracked-paths.csv) |
| RS04 | [rs04-reflective-continuum-tracked-paths.csv](rs04-reflective-continuum-tracked-paths.csv) |
| RS05 | [rs05-agent-foundations-tracked-paths.csv](rs05-agent-foundations-tracked-paths.csv) |
| RS06 | [rs06-auto-doc-engine-tracked-paths.csv](rs06-auto-doc-engine-tracked-paths.csv) |
| RS07 | [rs07-epistemic-pipeline-tracked-paths.csv](rs07-epistemic-pipeline-tracked-paths.csv) |
| RS08 | [rs08-sci-render-kit-tracked-paths.csv](rs08-sci-render-kit-tracked-paths.csv) |
| RS09 | [rs09-china-agentic-observatory-tracked-paths.csv](rs09-china-agentic-observatory-tracked-paths.csv) |
| RS10 | [rs10-agentic-frontier-observatory-tracked-paths.csv](rs10-agentic-frontier-observatory-tracked-paths.csv) |
| CONTROL | [control-research-software-identity-audit-tracked-paths.csv](control-research-software-identity-audit-tracked-paths.csv) |

These are path/blob/size identity catalogs, not independently computed content-body hashes, source-body scientific reviews, or proof that every path is a human-facing document.

### Exact same-blob path groups (RS01–RS10)

[Duplicate blob identity ledger](rs01-rs10-duplicate-blob-groups.csv) contains **159 groups / 611 path entries** where two or more distinct paths share an identical Git blob SHA within the same repository. Distribution: RS01 77 groups / 273 paths; RS02 60 / 228; RS03 0; RS04 9 / 84; RS05 9 / 18; RS06 0; RS07 0; RS08 0; RS09 4 / 8; RS10 0.

These are exact byte-identical content groups, not confirmed redundant documents. Many are date-labelled Daily/Weekly/Monthly or telemetry records. A repeated body may represent a legitimate no-change state, a template/sidecar, or a copied stale record; the blob hash alone cannot decide. The ledger therefore marks every group REVIEW_REQUIRED_NO_DELETE. No file was removed, renamed or collapsed. Selected examples were content-read: RS01 early quantitative-dashboard/radar files carry no embedded observation date; RS02 telemetry files are date-labelled but byte-identical; RS04 repeated cortex self-check bodies are date-labelled; RS05 daily/weekly architecture documents are identical across different owner paths; RS09 C3/C4/C5/C6 no-material-change entries are identical across two days. Their historical semantics remain unresolved pending each repo's own SOP and source evidence.

## 3. Classification vocabulary and interpretation

The catalogs use deterministic path-based buckets with fixed precedence:

- ROOT_GOVERNANCE_AND_SCHOLARLY_METADATA — repository entrypoints, contribution/security/license/citation and software metadata
- GITHUB_AUTOMATION — workflows, issue/PR templates and repository automation
- DOCUMENTATION_AND_GUIDES — contributor, user, architecture and operational guides
- DOMAIN_OR_RESEARCH_RECORDS — repo-native domain, research and governance collections
- DATED_RESEARCH_RECORD — daily/weekly/monthly or date-partitioned research material
- RETAINED_SOURCE_OR_INPUT_ARCHIVE / DATA_AND_CAPTURE — imported source snapshots, capture and retained input material
- HISTORICAL_AUDIT_OR_CORRECTION — audits, errata, reconciliations and correction records
- RUNTIME_SOURCE_OR_TOOLS / CONTRACT_OR_AUTOMATION_IMPLEMENTATION — executable implementation, scripts and automation contracts
- TESTS / SCHEMAS — validation and machine-readable contracts
- PUBLICATION_OR_FRONTEND — website, rendered/public-facing entrypoints
- CONTROL-specific: DATED_DIAGNOSTIC_MONITORING, RETAINED_SOURCE_EVIDENCE, HISTORICAL_BASELINE, RESEARCH_CONTRACT_RUNTIME_OR_DOCUMENTATION
- OTHER_OR_REVIEW_REQUIRED — intentionally unresolved by path-only rules

**Classification limitation:** a path bucket is an orientation hint, not proof of a file's semantics, freshness, authority, duplication or deletion eligibility. A hash-suffixed filename inside an archive is not automatically a duplicate. A README, sidecar, note, machine summary, workflow backup, generated report or historical correction can have a different role even when its extension matches another file.

## 4. Repository-level organization model

The existing repository-native structures remain the primary owners; this index does not flatten them into one universal directory scheme:

| Repository family | Canonical organization already present |
|---|---|
| RS01 welcome-to-github | docs/, docs/brain/inputs/archive/, horizon-cortex/, parallax/, AGI/, historical-audits/ |
| RS02 zero-entropy-lab | data/inputs/archive/, ballast/, aegis-cortex/, src/, tests/, AGI/, historical-audits/ |
| RS03–RS04 | RESEARCH/, METHODOLOGY/, ADR/, REFERENCES/, CODE/, AGI/, historical-audits/ |
| RS05 | FOUNDATION/, docs/, AGI/, historical-audits/ |
| RS06–RS08 | docs/01-source-and-explanation/, docs/02-examples-and-contracts/, docs/03-maintenance-and-audit/, maintenance/, runtime modules, schemas and tests |
| RS09–RS10 | reports/daily/YYYY/MM/YYYY-MM-DD/, history/, governance/, workstreams/, watchlist/, ledger/, maps/, plus SOP/source registry/taxonomy |
| CONTROL | contract/, corpus/, baseline/, schedule/, schema/, monitoring/, observations/, evidence/, provenance/, analysis/, scholarly/, templates/, tools/, docs/ |

## 5. Preservation and cleanup decisions

**No source file was renamed, moved or deleted in this inventory task.** The current path structures encode distinct research roles and provenance:

1. Keep dated Daily/Weekly/Monthly records in repo-native time partitions. They are not generic documentation clutter.
2. Keep historical-audits/, corrections, errata and reconciliations append-only. New interpretation belongs in a new reconciliation record.
3. Keep source snapshots and imported upstream documents in archive namespaces. Hash-suffixed filenames may preserve collision identity and source lineage.
4. Keep .note.md or other sidecars only under the repo's own note contract; do not merge them into the source file or infer that they are disposable.
5. Keep recovered workflow backups under explicit recovered/original timestamp paths. They are historical implementation artifacts, not necessarily active workflows.
6. Keep generated public frontend files separate from source documents and machine records.
7. Only rename or delete after proving the path is not a source identity, generated contract input, workflow dependency, manifest reference, cross-repository link, citation target or historical record.

The next cleanup pass, if needed, should be content- and reference-aware: duplicate-body candidates → reference graph → owner contract → explicit disposition (KEEP, SUPERSEDED_BUT_RETAIN, ALIAS, MOVE_WITH_MIGRATION, DELETE_CONFIRMED). This path catalog alone does not authorize deletion.

## 6. OSF authority and workspace mapping

The public OSF API representation acquired on 2026-11-06 supports this distinction:

- **Registration 5b329:** public, accepted, approved, unembargoed; registration storage provider exists but its OSF-storage folder returns zero files. The latest registration-detail representation available to this task was acquired on **2026-11-04**, not Nov 6. Its content and revision history are not edited here.
- **Associated Project wa5v8:** public, created 2026-10-05; public node detail reports current_user_permissions=[] and current_user_is_contributor=false in this unauthenticated read context. Its native OSF-storage folder is empty. Its GitHub provider exposes **33 top-level files/folders** (page size 10, four pages) from the connected CONTROL repository, not a second independently uploaded copy of the full Git tree.
- **Project Home Wiki:** one page, Home, version 4, last modified 2026-10-31T02:08:31.671891Z. Its text says the Project is an entry point only and holds no data or files; it points to the frozen preregistration DOI, Zenodo archive family and GitHub source repository.

The current session has **no authenticated OSF write connector**. Public API Allow: PUT/PATCH metadata is not a permission grant. No OSF mutation was attempted. The correct arrangement is to retain the Project as a small entry point and keep source/evidence files in GitHub and immutable Zenodo releases according to their existing contracts. Do not upload duplicate GitHub files to OSF storage merely to make the file browser look populated.

## 7. Process deviation recorded

During the first catalog-write pass, ten per-repository CSV files (RS01–RS10) were created using the GitHub Contents API without an explicit branch argument, so those **new index files were committed directly to CONTROL main**. This deviated from the repository's normal branch → PR → CI workflow.

Scope of the deviation:
- only ten new path/blob/size catalog files were added;
- no pre-existing file, source evidence, contract, baseline, historical record, schedule, observation, DOI or Release was modified or deleted;
- current main and those commits are preserved; no force-push or history rewrite is attempted;
- the CONTROL catalog, this report and navigation updates are being made on a dedicated branch for PR review;
- future inventory updates must use a branch and PR.

This is an execution-process deviation, not a research-contract amendment or a new research observation.

## 8. Scope and verification limits

- **Verified:** all 11 recursive GitHub trees were complete (truncated=false), exact main SHAs are pinned above, each CSV records Git path/blob SHA/size, and the fixed corpus remains ten objects plus one separate control repository.
- **Not performed:** content-body review of all 8,802 blobs, semantic duplicate detection, reference-aware rename/delete eligibility, complete historical commit replay of all ten software repositories since their individual first commits, or authenticated OSF file/wiki changes.
- **Not implied:** no new prospective observations, no OSF amendment, no new Release/DOI, no evidence that a file is current merely because it exists on main.

**Disposition:** WHOLE_11_REPO_PATH_INVENTORY_CREATED · 8802_TRACKED_BLOBS · NO_SOURCE_RENAMES_OR_DELETIONS · OSF_PROJECT_ENTRYPOINT_ONLY · OSF_WRITE_BLOCKED_NO_AUTH_CONNECTOR · DIRECT_MAIN_INDEX_WRITE_DEVIATION_RECORDED

## 9. Post-merge verification (2026-11-06)

The inventory package was merged through [PR #94](https://github.com/lostlight530/research-software-identity-audit/pull/94) at **2026-11-06T15:51:52Z**. Final CONTROL main is **67ea02a27996b0836d4544a71371742abbf19ece**. Its complete recursive tree contains **661 tracked blobs**; the 11 source-tree catalogs above remain pinned to their stated source SHAs. The CONTROL tree therefore grew from the pinned 657-file source snapshot by four inventory artifacts (CONTROL path catalog, duplicate-blob ledger, commit-delta ledger and inventory README). The current aggregate across the ten unchanged sample trees plus current CONTROL main is **8,806 tracked blobs**; the reproducible pre-self-reference catalog total remains **8,802**.

- PR #94 validation workflow: [42246818596](https://github.com/lostlight530/research-software-identity-audit/actions/runs/42246818596), completed success
- Post-merge CONTROL main workflow: [42246997767](https://github.com/lostlight530/research-software-identity-audit/actions/runs/42246997767), completed success
- PR #94 is merged; CONTROL Open PR count returned to zero
- OSF Associated Project GitHub provider re-read after merge returned the new folder path `/docs/repository-inventory/2026-11-06/` with **14 entries across two pages**, including all 11 path catalogs, the duplicate ledger, commit-delta ledger and README. Its parent docs collection reports 32 entries.
- OSF Project native osfstorage still returns **0 files**; frozen Registration 5b329 osfstorage still returns **0 files**. No duplicate upload was created.
- The Home Wiki remains the existing version 4 entry-point statement; it was not modified.

OSF provider acquisition labels are UTC-day granularity from the public extractor, while per-entry `last_touched` values are returned by the OSF representation. This verifies the GitHub-provider projection after merge, not an authenticated OSF write, not an independent OSF file upload, and not a change to the frozen registration.
