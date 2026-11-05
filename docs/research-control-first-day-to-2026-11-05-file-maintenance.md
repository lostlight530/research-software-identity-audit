# Research-control repository: complete first-day-to-November-5 file identity and maintenance review

> **Source class:** pinned, retrospective GitHub `main` history and entire tracked-tree inventory with a bounded current checker-assurance repair. **Not** an OSF registration revision, historical research-source recapture, new eligible prospective observation, source-platform census, new DOI, or archived software Release.
>
> **Pinned pre-maintenance source `main`:** [`3356cea9609a4cc4744fa071fc6b42f05488b9c5`](https://github.com/lostlight530/research-software-identity-audit/commit/3356cea9609a4cc4744fa071fc6b42f05488b9c5), committed **2026-11-05T05:37:11Z**. **Audit compilation client UTC:** 2026-11-05T10:21:53.900Z. The audit files and checker changes on this PR are intentionally **outside** that pinned pre-maintenance tree. GitHub API queries were sequentially/batch read, not an atomic snapshot or origin HTTP-byte capture.

## 1. Whole-repository scope, verified against GitHub object identities

| Snapshot target | Pinned count / resolution | Source |
| --- | --- | --- |
| Repository created | **2026-10-05T14:59:45Z** | GitHub repository metadata |
| First main commit | **`e5ba0a0e7dc548bd5bd3e79b4d7fc0cb95e528aa`**, **2026-10-05T14:59:46Z** | [GitHub original commit](https://github.com/lostlight530/research-software-identity-audit/commit/e5ba0a0e7dc548bd5bd3e79b4d7fc0cb95e528aa) |
| First-day-to-pinned-main reachable commits | **110**; commit pagination returned 100 + 10 | [Complete 110-commit chronology](research-control-main-history-through-2026-11-05.csv) |
| All tracked files at pinned main | **637**; Git recursive tree reports `truncated=false` | [All 637 Git path/blob/size identities](research-control-tracked-files-through-2026-11-05.csv) |
| PR lifecycle as-of this pinned review | **91** historic PRs: 90 merged, 1 closed-unmerged [#16](https://github.com/lostlight530/research-software-identity-audit/pull/16), 0 open | [91-PR source-state ledger](research-control-pr-history-through-2026-11-05.csv) |
| Monitoring event folders | **61**; **19 `record.yaml`**, **41 `record.json`**, **1 explicitly documented offline-only event** | [Dated event path/record-format ledger](research-control-dated-events-through-2026-11-05.csv) |
| Evidence event companions | **20**, all matched to dated monitoring event paths | [Dated event path ledger](research-control-dated-events-through-2026-11-05.csv) |

**Reproducibility boundary:** Git tree entries provide the Git-reported **path, blob SHA and byte size**. This is full *path-and-object identity* coverage, **not** 637 individual source-body scientific reviews, a provider-origin checksum verification, or recovery of local-only original HTTP response archives. Event directory dates are reported *source/event labels*, not freshly measured per-request retrieval clocks. The source query is reproducible from the pinned exact commit; no moving `latest` alias is used as historical proof.

## 2. Chained reconciliation with the earlier exact historical baseline

The [November 3 original, dated first-day audit](research-control-first-day-to-current-governance-audit-2026-11-03.md) pinned `b6aa40231bcba62da98e089673652839952118cf` with **104 reachable commits and 620 files**, and preserved all 620 original file SHA/byte sizes. During this review, **all 620 rows** were independently joined against that exact pinned Git tree with **zero path/SHA/size mismatches**; the **104 chronology SHAs** matched the Git API source commit set without mismatch. Earlier October 21/28/31 historical snapshots remain unchanged and should not be silently adjusted to November 5 totals.

From that exact November 3 baseline to the exact November 5 pre-maintenance main:

- **+6 main-reachable commits** (104 → 110), corresponding to the November 3 research-control history correction plus November 4–5 monitoring and semantic correction work. See the full pinned chronology for the exact ordering, timestamps and commit subjects
- **+17 tracked paths, 7 existing blob identities modified, 0 deleted**, yielding 637 current paths. [Each exact old/new Git blob identity, reported byte size, and forward disposition](research-control-file-delta-since-2026-11-03.csv)
- **+3 dated monitoring event folders** (58 → 61) and **0 new evidence companion folders** (20 → 20) relative to the November 3 pre-audit pinned event inventory
- The 17 newly present paths include dated Nov 3 retrospective crosswalks, the Nov 3 482-attempt derived surface-ID correction package, and the Nov 4–5 bounded monitoring packages. **No earlier source package was deleted**; the current code/tests and navigation edits are separate changes, not retroactive replacements of OSF Schema Response text or raw historical observations

This is an additive **source-history chain**, not a claim that the November 3 report had already observed or predicted later commits.

## 3. File responsibility, naming and preservation decisions

- **Frozen research authority:** the [OSF registration](https://osf.io/5b329/overview), October 5 original Schema Response and October 6 approved revision remain distinct. Their previously verified `344-83` exploratory wording difference is [documented](../contract/osf-registration-version-governance-2026-11-03.md), not silently promoted to a primary preregistered procedure
- **Study identity:** [manifest](../corpus/object-manifest.csv) remains exactly **RS01–RS10**; the control repository is **CONTROL, never RS11**. Six preregistered layers imply **60** object-layer units per eligible scheduled point; seven concrete platforms imply **70 possible object-platform checks, not 70 research units**
- **Current operational schedule:** [schedule](../schedule/README.md) still lacks declared numeric offsets; diagnostic records and release-published changes **cannot be relabeled** as formal prospective cells. This audit adds **0** cells and does not alter the baseline cutoff `2026-10-05T23:59:59+08:00`
- **Current path envelopes:** all 61 dated monitoring directories use valid `YYYY-MM-DD/NN-kebab-case` identities, each has `README.md`; 60 have one machine record, one is the already documented [offline-only replay exception](../monitoring/2026-10-24/03-offline-family-stat-replay/README.md). The 20 evidence companions have matching monitoring event IDs, with **no orphan by current path identity**
- **Legacy naming:** `2026-10-06/01-wave-01`, old source-attempt fields, historical `record.yaml` variants, retained `canonical-current-field-extracts.json`, old Git blob SHAs and already published artifact manifests stay untouched. Prefer documented aliases or explicit correction history rather than breaking source identity with cosmetic renames
- **Authority boundary:** `monitoring/` is diagnostic; `evidence/` preserves source/evidence artifacts at their own evidentiary level; `observations/` currently has only instructional scaffolding; `docs/` contains as-of navigation and dated reviews. No external platform status or researcher-account claim is inferred from a Git path or file existence

## 4. Actual assurance gap and bounded repair in this maintenance PR

**Detected:** [the existing path checker](../tools/check_record_paths.py) already validates dated envelopes, source projection count and the special November 3 surface-ID reconciliation. It did **not** enter the November 4–5 `bounded_diagnostic_source_access_not_prospective` `surface-access-recheck.csv` format via those guarded record-class predicates. Thus an incorrect 34-row count, error status, receipt identity or client-batch clock in that new record class could previously pass the relevant **path-only** verification.

**Repair:** add a read-only, standard-library `check_bounded_surface_ledger` guard to the existing checker and synthetic-only tests to its existing advisory test suite. It checks the two accepted record summary layouts, CSV schema, row/count/identity/receipt/error consistency, day-granular acquisition labels and available batch-clock/receipt joins. Preserves **HTTP errors as errors**; does not assert access means indexing, or extractor retrieval means original-provider HTTP freshness. Existing historical CSV/JSON files remain byte-identical; no new database, dependency, API or strict merge gate is added.

**Why this scope:** a real validator coverage omission is worth correcting; renaming all 637 paths, regenerating legacy snapshots to look current, changing original OSF wording, inventing new per-request timestamps, or creating another Release/DOI would not improve evidence integrity.

## 5. Verification, CI, known limits and handoff

**Source checks already performed:** GitHub recursive trees at both exact commits, paginated 110-history set, independent exact 104-SHA and 620-path baseline join, 91 historical PR states, 61 monitoring and 20 evidence event identity classification, and current contract/manifest/schema/schedule provenance read. These are connected-GitHub **static/API** checks and not a new scholarly-platform observation.

**New branch tests:** synthetic tests for status/count/identity/receipt/day granularity/client clock and no-prospective-promotion. The actual GitHub PR workflow and post-merge `main` workflow must be inspected for their specific step outcomes before reporting completion. CI uses **advisory** validation; a green overall workflow is not an independent scientific replay. Independent local-only HTTP archive replay is **NOT_EXECUTED** in this repository-cloud-only maintenance task.

**Remaining boundaries:** individual historical source origins, retained local-only raw response bytes, third-party cache age versus actual HTTP provider times, qualitative correctness of all 637 file bodies, live DOI/ORCID/Zenodo/OpenAlex/OpenAIRE/SWH census, and actual institution adoption are not newly verified. A source failure or unqueried object is **UNKNOWN / PARTIAL**, never automatically evidence of absence.

**Disposition:** `WHOLE_TREE_IDENTITY_AUDITED` + `OLD_BASELINE_OBJECT_JOIN_PASS` + `DATED_EVENT_STRUCTURE_PASS` + `BOUNDED_SURFACE_LEDGER_ASSURANCE_GAP_REPAIRED` + `NO_FROZEN_CONTRACT_CHANGE` + `NO_NEW_PROSPECTIVE_CELLS`. Deployment and CI outcomes belong to the actual PR/merge evidence, not this pre-merge historical source note.
