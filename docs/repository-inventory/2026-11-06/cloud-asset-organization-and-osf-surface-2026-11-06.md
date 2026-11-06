# Cloud asset organization, document classification and OSF surface reconciliation — 2026-11-06

**Classification:** retrospective cloud asset and document-organization review, pinned to current GitHub main trees and public OSF API representations acquired on 2026-11-06. This is not a new research observation, OSF registration amendment, new DOI, new Release, or permission to rewrite historical source artifacts.

## 1. Scope and exact repository boundary

The authenticated GitHub connection lists **14 public repositories** owned by `lostlight530`. The research project’s defined core remains **11 repositories**: RS01–RS10 plus the separate CONTROL repository. The other three are ancillary and are explicitly not study objects.

| ID | Repository | Main | Tracked blobs | Classification |
|---|---|---|---:|---|
| RS01 | [welcome-to-github](https://github.com/lostlight530/welcome-to-github) | `46107dc7a3857008868ec5341d451d2355ae0b5f` | 1,549 | Research software |
| RS02 | [zero-entropy-lab](https://github.com/lostlight530/zero-entropy-lab) | `d7c605f83bcd423601bea1e79cca496ddf646b56` | 2,344 | Research software |
| RS03 | [Axiom-0](https://github.com/lostlight530/Axiom-0) | `aa1c692c10a371e7815034bcc81f05b644bf6444` | 509 | Research software |
| RS04 | [reflective-continuum](https://github.com/lostlight530/reflective-continuum) | `2cbbd11710cb45efadb2b7980861740784b0ef6b` | 617 | Research software |
| RS05 | [agent-foundations](https://github.com/lostlight530/agent-foundations) | `79474f8efa89dc549b5893558decb0170eaab605` | 160 | Research software |
| RS06 | [auto-doc-engine](https://github.com/lostlight530/auto-doc-engine) | `7eb7bd903d9b0a118df89533f857f4f1c2088c98` | 336 | Research software |
| RS07 | [epistemic-pipeline](https://github.com/lostlight530/epistemic-pipeline) | `5817bd41ec9922fc29ca78c9291fbb06786f3649` | 337 | Research software |
| RS08 | [sci-render-kit](https://github.com/lostlight530/sci-render-kit) | `003e8c9691c00cad7ab4c6336bb00a475f6815ef` | 347 | Research software |
| RS09 | [china-agentic-observatory](https://github.com/lostlight530/china-agentic-observatory) | `43035f9af841a7e7d8fb83bf3c1d3d191faac9ab` | 1,013 | Research software |
| RS10 | [agentic-frontier-observatory](https://github.com/lostlight530/agentic-frontier-observatory) | `9afbc25a74e1cf825b7598de4c83d6a82f004140` | 933 | Research software |
| CONTROL | [research-software-identity-audit](https://github.com/lostlight530/research-software-identity-audit) | `8494b254ebe9b9811524ed8e73a1c36099efb83d` | 661 | Contract, runtime, evidence and provenance control |

The ten sample trees total **8,145** blobs; current CONTROL contributes **661**; total **8,806 tracked blobs** across the 11 core repositories. All 11 recursive trees were returned with `truncated=false`. Ten research repository tree contents exactly match the 10 existing pinned path/blob/size catalogs. CONTROL’s earlier 657-path catalog has **4 additive paths**, with **2 existing navigation documents modified** since that catalog. No path was deleted in that comparison.

The previous [November 6 whole-tree inventory](README.md) remains the path/blob/size source of record. Its 8,802 total was the ten fixed trees plus the then-pinned 657-path CONTROL tree; 8,806 is the current 10 + 661 total. The path catalogs are not 8,806 body-level scientific reviews.

## 2. Three ancillary repositories — separate from the research corpus

The current GitHub account list exposes three additional public repositories:

- `lostlight530/software` is a **fork of `rseng/software`**, default branch `master`. Its recursive tree response was truncated after 24,324 returned blob entries, so that number is **not** a complete file count. It is an upstream contribution surface, not a new sample object.
- `lostlight530/life-science-ecosystem-lab` has 305 tracked blobs on a complete recursive tree, two published Releases and no Open PR at this read. It is an adjacent research/evidence tooling project, not RS11.
- `lostlight530/ling-cookbook` has 163 tracked blobs on a complete recursive tree, no published Release and no Open PR at this read. It is a separate cookbook/skill asset, not RS12.

Pinned branch heads, tree-completeness flags and release/PR counts are in [ancillary-repositories.csv](ancillary-repositories.csv). These repositories are intentionally not folded into the RS01–RS10 corpus or the 11-repository research-control count.

## 3. Existing document organization and classification — preserve repo-native ownership

The current structures are already differentiated by artifact role. A single universal folder taxonomy would damage local contracts and make cross-repository navigation harder.

| Repository set | Existing authoritative organization |
|---|---|
| RS01 `welcome-to-github` | `docs/`, `docs/brain/inputs/archive/`, `horizon-cortex/`, `parallax/`, `AGI/`, `historical-audits/` |
| RS02 `zero-entropy-lab` | `data/inputs/archive/`, `ballast/evidence/`, `aegis-cortex/`, `src/`, `tests/`, `AGI/`, `historical-audits/` |
| RS03–RS04 | `RESEARCH/`, `METHODOLOGY/`, `ADR/`, `REFERENCES/`, `CODE/`, `AGI/`, `historical-audits/` |
| RS05 | `FOUNDATION/`, `docs/`, `AGI/`, `historical-audits/` |
| RS06–RS08 | `docs/01-source-and-explanation/`, `docs/02-examples-and-contracts/`, `docs/03-maintenance-and-audit/`, `maintenance/`, runtime modules, schemas and tests |
| RS09–RS10 | `reports/daily/YYYY/MM/YYYY-MM-DD/`, `history/`, `governance/`, `workstreams/`, `watchlist/`, `ledger/`, `maps/`, plus repository-specific SOP/source registry/taxonomy |
| CONTROL | `contract/`, `corpus/`, `baseline/`, `schedule/`, `schema/`, `monitoring/`, `observations/`, `evidence/`, `provenance/`, `analysis/`, `scholarly/`, `templates/`, `tools/`, `tests/`, `docs/` |

Document roles should be read in this order: repository README and domain index; current machine contract/schema/SOP; current implementation; dated maintenance/reconciliation; historical audit/source; imported archive. This is a navigation priority, **not** permission to erase earlier records. Current implementation does not retroactively alter an earlier source capture or frozen contract.

### Naming and cleanup decisions

- Preserve standard root names (`README.md`, `CITATION.cff`, `codemeta.json`, `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`) and repo-specific domain naming.
- Preserve dated event paths `YYYY-MM-DD/NN-lowercase-kebab/`, stable object IDs, source file names and established machine record variants.
- Preserve both `record.yaml` and `record.json` where they are historical accepted variants; no cosmetic conversion.
- Preserve `.note.md` sidecars under their own repository contract; do not merge them into their source documents.
- Preserve `original`, `recovered`, `archive`, `historical-audits`, `corrections`, `errata`, `reconciliation` and hash-suffixed imported source names.
- Do not rename a historical `wave` source label or a frozen path containing `current` when its actual semantics are already clarified by a dated alias/crosswalk.
- Exact same-blob groups in the existing RS01–RS10 ledger: **159 groups / 611 path entries**. They are exact byte-identical path pairs/groups, not proof of semantically redundant files. The existing ledger marks all `REVIEW_REQUIRED_NO_DELETE`.

**Cleanup result:** no rename, move, merge, or deletion is justified by current evidence. The next safe cleanup unit is a content/reference-aware candidate review: read body → inspect inbound/outbound references and manifests → read owning repo SOP → record disposition (`KEEP`, `SUPERSEDED_BUT_RETAIN`, `ALIAS`, `MOVE_WITH_MIGRATION`, or `DELETE_CONFIRMED`). No destructive bulk operation is authorized by a path or hash match alone.

## 4. OSF: frozen Registration and live Project are separate

The [public API surface ledger](osf-surface-register.csv) records exact endpoints, extractor receipt IDs, UTC-day acquisition labels and limits.

### Registration `5b329` — immutable research authority

- Public OSF API representation says accepted, approved, public, unembargoed and not withdrawn; original registered timestamp is `2026-10-05T14:04:13.783851Z`.
- The most recent registration-detail representation returned in this review was acquired **2026-11-04**, not Nov 6. The schema-response list representation was acquired **2026-10-31**. Do not call those live Nov 6 revision checks.
- Original Schema Response `6ac3ae5e6da32e3d0576ed72` and approved revision `6ac4c12fed97b8b77ce88a9c` remain separate authority versions. Preserve the existing exact field-diff and governance record.
- Registration native OSF Storage returns **zero files**. No OSF registration field, schema response, DOI or revision was changed.

### Associated Project `wa5v8` — small entry point plus GitHub provider projection

- Public project node read acquired **2026-11-06**; node reports public, `registration=false`, and `current_user_permissions=[]` / `current_user_is_contributor=false` in this unauthenticated read context.
- Child-node endpoint returns an empty list. Native OSF Storage returns **zero files**.
- GitHub provider exposes **33 top-level files/folders** over four pages, with per-entry `last_touched` up to **2026-11-06T15:55:26Z** in the source representation. This is a GitHub-connected view of the CONTROL repository, not an independent duplicate OSF upload.
- One Project Home Wiki page exists: ID `6973a`, version **4**, 742 bytes, last modified `2026-10-31T02:08:31.671891Z`. Its text explicitly describes the Project as an entry point only, points to the frozen registration DOI, Zenodo concept DOI and GitHub control repository, and says it holds no data or files.

**OSF action boundary:** this session has no authenticated OSF write connector. Public API `Allow: PUT/PATCH/DELETE` headers are not account authorization. No OSF write was attempted. No duplicate OSF uploads should be made simply to populate the file browser. If the user later wants a Project Wiki wording update or a native OSF upload, it requires an authenticated OSF session/authorized connector; it must not alter Registration `5b329`.

## 5. Historical source and contract integrity

- Fixed sample remains **RS01–RS10 only**; CONTROL and the three ancillary repositories are not additional study objects.
- Six analytical layers remain **60 object-layer units per eligible scheduled timepoint**. Seven operational platforms remain 70 possible checks, not 70 analytical units.
- Historical baseline cutoff and all dated source packages remain as pinned. This document is a retrospective cloud-asset inventory, not a prospective observation.
- No original OSF response, raw source evidence, historical event record, DOI, Release, or Git object was deleted or rewritten.

## 6. Verification and disposition

- 11 core repository recursive trees: complete; 8,806 current tracked blobs.
- Ten fixed research repository catalogs: exact path/blob/size match to current main.
- CONTROL: 661 current blobs; 4 additions / 2 navigation modifications relative to its 657-path prior catalog; no deleted paths.
- Three ancillary repositories recorded separately; the fork's recursive tree is truncated and explicitly partial.
- OSF: Registration and Project surfaces distinguished; no authenticated write permission available; no OSF mutation attempted.
- Duplicate candidates: 159 groups / 611 path entries retained for review; zero destructive cleanup.
- **Disposition:** `CLOUD_ASSET_INVENTORY_RECONCILED` · `REPO_NATIVE_DOCUMENT_TAXONOMIES_PRESERVED` · `NO_DELETE_OR_RENAME_WITHOUT_SEMANTIC_PROOF` · `OSF_PROJECT_GITHUB_PROVIDER_ONLY` · `OSF_WRITE_BLOCKED_NO_AUTH_CONNECTOR` · `FROZEN_REGISTRATION_UNCHANGED`
