# 2026-11-20 eleven-repository tracked path and Git-blob classification

**Class:** non-atomic pinned GitHub tree snapshots and strict two-endpoint path/blob comparison, NOT an audit of every file's scientific contents and NOT a prospective research observation

This complements the [CONTROL first-day 2026-10-05→Nov20 history](../README.md), which has **903 source-pinned tracked blobs / 158 reachable main commits / 83 dated monitoring events** at its *earlier* CONTROL pin `5bbdd7ec...`. The CONTROL row below is pinned **later**, after PR #133, at `8ecefe06...`, therefore correctly contains **932** blobs and must not replace the earlier pinned 903-file inventory

## Exact coverage

- **11/11** core repositories: RS01–RS10 (fixed study corpus) plus **one separate CONTROL** repository, not RS11
- **All 11** recursive source Git trees returned `truncated=false`, each at an exact pinned main commit in [the source pin register](source-pin-register.csv) and [machine summary](summary.json)
- **11** full tracked file catalogs covering every returned *current* Git blob path: repository, role, pinned source SHA, path, blob SHA-1, Git byte size, path-derived class, extension
- **11** comparison files joining every path to the historical source-pinned [2026-11-06 inventory](../../2026-11-06/README.md), preserving new-only, old-only, and same-path-but-new-Git-blob states
- One [repository comparison CSV](repository-reconciliation.csv) and an immutable-source-view [machine summary](summary.json)

## Totals and exact two-snapshot comparison

| Role | Repository | Nov 6 paths | Nov 20 paths | Now only | Prior only | Same-path changed SHA | Evidence |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| RS01 | [welcome-to-github](https://github.com/lostlight530/welcome-to-github) | 1,549 | 1,566 | 162 | 145 | 31 | [Paths](rs01-welcome-to-github.csv) · [Delta](delta-rs01-welcome-to-github.csv) |
| RS02 | [zero-entropy-lab](https://github.com/lostlight530/zero-entropy-lab) | 2,344 | 2,448 | 290 | 186 | 36 | [Paths](rs02-zero-entropy-lab.csv) · [Delta](delta-rs02-zero-entropy-lab.csv) |
| RS03 | [Axiom-0](https://github.com/lostlight530/Axiom-0) | 509 | 522 | 62 | 49 | 56 | [Paths](rs03-Axiom-0.csv) · [Delta](delta-rs03-Axiom-0.csv) |
| RS04 | [reflective-continuum](https://github.com/lostlight530/reflective-continuum) | 617 | 608 | 79 | 88 | 40 | [Paths](rs04-reflective-continuum.csv) · [Delta](delta-rs04-reflective-continuum.csv) |
| RS05 | [agent-foundations](https://github.com/lostlight530/agent-foundations) | 160 | 159 | 45 | 46 | 33 | [Paths](rs05-agent-foundations.csv) · [Delta](delta-rs05-agent-foundations.csv) |
| RS06 | [auto-doc-engine](https://github.com/lostlight530/auto-doc-engine) | 336 | 373 | 37 | 0 | 27 | [Paths](rs06-auto-doc-engine.csv) · [Delta](delta-rs06-auto-doc-engine.csv) |
| RS07 | [epistemic-pipeline](https://github.com/lostlight530/epistemic-pipeline) | 337 | 375 | 38 | 0 | 36 | [Paths](rs07-epistemic-pipeline.csv) · [Delta](delta-rs07-epistemic-pipeline.csv) |
| RS08 | [sci-render-kit](https://github.com/lostlight530/sci-render-kit) | 347 | 384 | 37 | 0 | 28 | [Paths](rs08-sci-render-kit.csv) · [Delta](delta-rs08-sci-render-kit.csv) |
| RS09 | [china-agentic-observatory](https://github.com/lostlight530/china-agentic-observatory) | 1,013 | 1,196 | 185 | 2 | 37 | [Paths](rs09-china-agentic-observatory.csv) · [Delta](delta-rs09-china-agentic-observatory.csv) |
| RS10 | [agentic-frontier-observatory](https://github.com/lostlight530/agentic-frontier-observatory) | 933 | 1,112 | 181 | 2 | 36 | [Paths](rs10-agentic-frontier-observatory.csv) · [Delta](delta-rs10-agentic-frontier-observatory.csv) |
| CONTROL | [research-software-identity-audit](https://github.com/lostlight530/research-software-identity-audit) | 657 | 932 | 275 | 0 | 30 | [Paths](control-research-software-identity-audit.csv) · [Delta](delta-control-research-software-identity-audit.csv) |
| **TOTAL** | **11 repositories** | **8,802** | **9,675** | **1,391** | **518** | **390** | Separate pinned sources |

**Net delta = 1,391 now-only paths − 518 prior-only paths = +873 tracked paths**. Same-path changed blob counts are **not extra paths**, and current path growth is **not** evidence of additional research objects, new research papers, independent software uses or citations

The row `prior-only` means *not present in the pinned current tree*; it does not prove an object has disappeared from Git history. The row `same-path changed SHA` proves Git content-identity change but not scientifically meaningful change. No automatic bulk rename, deletion or deduplication was performed

## Source time, provenance and ownership boundaries

- 2026-11-06 counts and pinned SHAs are from the historical [11-repo catalog](../../2026-11-06/README.md); its preserved original rows were used for path/SHA joins
- 2026-11-20 live GitHub tree queries (UTC, **non-atomic across repos**): RS01–RS05 `00:44:51.608–00:44:53.572`, RS06–RS08 `00:45:42.365–00:45:43.665`, RS09–RS10 and CONTROL `00:47:15.935–00:47:17.750`
- These source snapshots are fixed by per-repo main SHA, so a subsequent GitHub change does not silently rewrite the observation
- This catalog is a **path and Git object identity classification** — not a line-by-line content/semantics review of 9,675 files, not an 11-repo reachable history ledger, not a new current HTTP census, and not proof that current code was executed
- Earlier CONTROL dated [monitoring/evidence](../../../..) files and the newly restored Nov 19 evidence remain in their owning paths
- GitHub Commit/Tree/Blob objects and API capture clocks are different from Zenodo DOI clocks, original platform HTTP responses and frozen OSF registration

## Governance and disposition

- The frozen [OSF preregistration](https://osf.io/5b329) and approved revision history remain distinct source-authority versions
- The fixed RS01–RS10 study corpus and **six preregistered layers × ten = 60 object-layer units** remain unchanged
- Seven operational platforms/70 possible checks and 34 supplementary surfaces remain separate
- No new release, DOI, OSF write, formal prospective observation, research-sample expansion or intervention was created

**Disposition:** `ALL_11_CURRENT_PATH_IDENTITIES_CAPTURED` / `TWO_ENDPOINT_PATH_DELTA_RECONCILED` / `NO_DESTRUCTIVE_CLEANUP` / `NO_CONTRACT_DRIFT` / `PROSPECTIVE_CELLS_ADDED_0`
