# Research-control session closeout and reproducibility handoff — 2026-10-18

**Status:** dated handoff for the [research-software-identity-audit](https://github.com/lostlight530/research-software-identity-audit) research-control repository. This document is **not** a replacement OSF registration, new data source, scheduled prospective observation, causal conclusion, immutable release, or historical transcript. The already retained source files and PR/commit history are authoritative for their own timestamps and original author identities.

**Scope:** summarize the established 2026-10-05–2026-10-18 repository maintenance, evidence-boundary corrections, cross-platform discovery footprint, October 18 control-software publication and later ORCID work refresh. The continuity status is resolved only as far as the evidence supports. Current `main` moves; a historical GitHub tag does not.

## A. Study identity and unchanging contract

- **Frozen OSF Registration:** [`10.17605/OSF.IO/5B329`](https://doi.org/10.17605/OSF.IO/5B329), registered October 5, 2026. [Associated OSF Project](https://osf.io/wa5v8) is a distinct live/project-materials surface; it does not amend the frozen registration.
- **Fixed corpus:** exactly **RS01–RS10** in [corpus/object-manifest.csv](../corpus/object-manifest.csv).
- **Six preregistered infrastructure layers:** `source_repository`, `archival_repository`, `identifier_registration`, `author_registry`, `preservation_archive`, `discovery_graph`.
- **Operational platforms:** GitHub, Zenodo, DataCite, ORCID, Software Heritage, OpenAIRE, OpenAlex. **OpenAIRE** and **OpenAlex** are separate checks mapping to the **same** `discovery_graph` analytical layer: **10 × 6 = 60** planned object-layer units per eligible scheduled timepoint; **10 × 7 = 70** possible platform checks, **not** 70 analytical units.
- **Control repo is never RS11.** Supplementary WorkflowHub, LifeMonitor, bio.tools, RSD, RRID, OpenEBench, and other ecosystem surfaces do not expand the registered platforms or sample.
- **Baseline cutoff:** 2026-10-05 23:59:59 **Asia/Shanghai**. Later reconciling a baseline is not historical proof. **No concrete operational schedule offsets** are declared in [schedule/README.md](../schedule/README.md); existing October diagnostic packages are **not automatically prospective observations**, even with later fixed-ten releases.
- Scientific chain: **source evidence → raw observation → normalized/derived observation → analysis → interpretation → reported conclusion**. Failed, unknown, 404, 429, access challenged, partial, conflicting, missing and unresolved states remain legitimate outcomes. Historical records preserved; corrections are append-oriented.

## B. Repository changes and primary audit anchors

| Merge / snapshot | Verified contribution | Scope and evidence |
| --- | --- | --- |
| [PR #43](https://github.com/lostlight530/research-software-identity-audit/pull/43), merge `62da3316082566db195fbbe36e83bcc4ad629dc1` | October 16 Zenodo **11-family** family-level total vs unique counter crosscheck; fixed ten separate from control | [10/16 diagnostic](../monitoring/2026-10-16/01-noon-counter-contract-recheck/README.md) |
| [PR #44](https://github.com/lostlight530/research-software-identity-audit/pull/44), `4e2274894507c71f15ae1866c98a1c95f27f761f` | Research repository navigation, ownership map and docs-only preservation boundaries | [Directory guide](README.md) |
| [PR #45](https://github.com/lostlight530/research-software-identity-audit/pull/45), `ffce1be75fa7f4bfb8f6e1a86dd51b9db60d922b` | Correct concatenated Zenodo UI fields; four WorkflowHub identities; public bio.tools record | [10/17 diagnostic](../monitoring/2026-10-17/01-field-boundary-cross-platform-recheck/README.md) |
| [PR #46](https://github.com/lostlight530/research-software-identity-audit/pull/46), `a78e5fdcac843c7752b2122f68267688a44674ef` | October 18 11-hour user page counters; independent DataCite 72/53/18/1; OpenAlex 29; GitHub CI success; initial **pre-package** review | [10/18 morning diagnostic](../monitoring/2026-10-18/01-eleven-hour-workflow-ci-crosscheck/README.md) |
| October 18 **later publication** | Fourth control-software GitHub release `v2026.10-evidence-integrity`, Zenodo record **23446162** | [Verified postpublication reconciliation](../scholarly/release-identity-reconciliation-2026-10-18.md). See original **immutable** tag for actual archived content. |
| October 18 ORCID refresh | User reports all **11 ORCID links** updated; Beta Work has **one explicit success receipt**; OpenAIRE source modified October 18 | [Attribution-preserving ORCID diagnostic](../monitoring/2026-10-18/02-orcid-openaire-work-refresh/README.md) |

Prior scholarly/counter diagnostics remain under [monitoring/](../monitoring/README.md), [evidence/](../evidence/README.md), [scholarly/](../scholarly/README.md), and [provenance/](../provenance/README.md). These paths are stable evidence links: do **not** reorganize dated source or byte-sealed artifacts merely for a shorter tree.

## C. Distinct counters, clocks and identities

| Surface | Bounded date/source | Reported or verified value | Important limitation |
| --- | --- | --- | --- |
| Zenodo family API | October 16 retained API | Fixed ten **2,283 total views / 1,449 summed unique views**, downloads **17 total / 16 unique**; separately control **103 total / 96 unique views**, downloads **3 / 3** | 10 fixed software objects vs independent control; aggregate unique fields are **not globally deduplicated people** |
| Zenodo landing page UI | October 17 page extract | Ten fixed: **1,511 page unique views / 16 page unique downloads** | Page display is **not API total** and may have a daily update clock |
| Zenodo flattened page UI | October 18 user 11-hour extract | Ten fixed: **1,533 page unique views / 16 page unique downloads** | `1895` means **189 Views + 5 Downloads**, not `1,895` views; exact user capture minute unavailable |
| WorkflowHub Team Dashboard | October 18 user 11-hour extract | **4 assets**, sums of displayed most-viewed **3,097** / most-downloaded **276** | Selected Dashboard Period/asset filter unknown; don't claim same-window growth or unique people |
| DataCite Commons | October 18 ORCID query, independently reproduced API counts | **72 DOI Works** = **53 Software + 18 Workflow + 1 Study Registration**; user's repository facet Zenodo 53 / WorkflowHub 18 / OSF 1 | 72 DOI metadata records, **not** 72 distinct research software families and **not** OpenAlex author works |
| OpenAlex author | October 18 author profile/API, author `A5151904252` | **29 author-filtered Works**, 1 citation; user's visible list held 29 unique Work IDs | Different discovery graph indexing/record-level semantics from DataCite; not an error requiring imputation |
| GitHub Actions for separate life-science source repo | October 18 `life-science-ecosystem-lab` main commit `d2a6ec6e943f0b8888e007053ddb0d3d9be47367` | [Run #39092740134](https://github.com/lostlight530/life-science-ecosystem-lab/actions/runs/39092740134) **5/5 jobs success** | GitHub CI is execution/contract evidence for represented checks, not scientific certification |
| LifeMonitor | October 18 user-authenticated **private** dashboard | Private `cwl` **1 Passed**, 0 Failed/Error; user attribution only | Not independently accessible by public API; no proved automatic WorkflowHub sync; no private access tokens/URLs archived |
| WorkflowHub, bio.tools, OpenEBench | October 17–18 source checks | WorkflowHub project 490 **four public workflows**; bio.tools record `life-science-protein-file-audit` public; OpenEBench link visible | Different supplementary identity surfaces; bio.tools raw `validated=0` flag not given unsupported semantics; OpenEBench benchmark score unknown |

The [October 18 field extracts](../monitoring/2026-10-18/01-eleven-hour-workflow-ci-crosscheck/record.json) and their CSVs should be preferred over any rounded narrative above. Counters above are **source-specific** and at different times, never a combined cross-platform traffic total.

## D. Author identity, ORCID update and provenance

Public ORCID: [`0009-0001-3617-0832`](https://orcid.org/0009-0001-3617-0832). For Beta control archive [`10.5281/zenodo.23166491`](https://doi.org/10.5281/zenodo.23166491), the user's authenticated interface explicitly confirmed **successful Update ORCID work** and displayed **two sources with one DOI**:

- **DataCite / Software:** user-visible `Added=2026-10-09`, `Last modified=2026-10-09`.
- **OpenAIRE / Dataset:** user-visible `Added=2026-10-05`, `Last modified=2026-10-18`.

These are **source-specific representations**, **not two distinct Beta archive DOI objects**. One detailed Beta success is shown, while updates to the other ten of eleven links are **user reported without independent item-level receipts**. A green OpenAIRE/ORCID icon or next full OpenAIRE synchronization is **not verified**. The independent public ORCID endpoint contains the Beta DOI and source channels, but its flattened response did not settle every per-source updated timestamp.

## E. Exact four control releases and metadata drift

| Tag | Actual archive DOI | Recorded state |
| --- | --- | --- |
| `beta` | `10.5281/zenodo.23166491` | Existing immutable October 5 archive |
| `v2026.10-initial-research-runtime` | `10.5281/zenodo.23176748` | Existing immutable October 6 archive |
| `v2026.10-evidence-reconciliation` | `10.5281/zenodo.23284570` | October 10 release **embeds October 6** version citation metadata |
| **`v2026.10-evidence-integrity`** | **`10.5281/zenodo.23446162`** | Published **2026-10-18T04:38:57Z**; latest independently verified release; its immutable tag **embeds October 10** version citation metadata |

Concept DOI stays [`10.5281/zenodo.23166490`](https://doi.org/10.5281/zenodo.23166490). The later **live `main`** citation/CodeMeta correction names the real October 18 tag/version **after publication**; it does **not** alter either archived mismatch. In the [Dated release reconciliation](../scholarly/release-identity-reconciliation-2026-10-18.md), the provider reports 1,392,684 bytes and ZIP MD5 `dbc5b4bdbd5e5fbb3b6fb6eb5ec44fa3`, **not independently rehashed**.

The morning [pre-package checklist](../scholarly/release-readiness-2026-10-18.md) was **true at its earlier review clock** and is not retrospectively altered. For the actual new release, further local strict/offline verification and tagged ZIP checksum replay **remain unperformed in this follow-up**; successful advisory CI is not enough to claim all those checks were done.

## F. Handoff for future work

Next work should begin from **fresh `main` and open PRs**, not this file's SHA. Before any change, inspect the frozen registration, manifest, schema, schedule, relevant dated evidence, git history, and actual present DOI/tag state.

Prioritize:
1. **Version integrity:** put a *before-publication* check in the normal release procedure to catch tag-embedded citation/CodeMeta drift. Only introduce an automated checker if the small maintenance contract actually requires it; Python stdlib is sufficient. No moving historical tags or changing old release objects.
2. **Evidence replay:** execute `python tools/check.py --mode strict` and `python tools/check_retained_all.py` locally on the actual chosen checkout and record stdout/stderr/exit status. These were not executed by this handoff.
3. **ORCID/OpenAIRE:** save only the minimal public identifiers and item-level success evidence needed; don't assert all eleven have independently confirmed update timestamps or a synchronized green icon.
4. **Prospective eligibility and schedule:** explicitly adjudicate the OSF eligible release event, then declare concrete operational schedule offsets **prospectively before** using `observations/raw/`; do not backfill.
5. **Public source quality:** reconcile supplementary bio.tools documentation drift in its *own* source repository if authorized, avoiding cross-repo silent writes; preserve private LifeMonitor status limits.

**Closure meaning:** this document archives what is established, which operations ran, and the unresolved gaps. It does not declare the research finished, all verification passed, or the longitudinal study completed. The current chat need not remain the sole handoff channel.
