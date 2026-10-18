# 2026-10-18 research-control archival identity reconciliation

**Classification:** dated **postpublication** release/metadata reconciliation. This is not a replacement for the frozen OSF Registration or an amendment to an already sealed GitHub tag/Zenodo ZIP. It supersedes the *current-state interpretation* in the earlier [pre-package review](release-readiness-2026-10-18.md) **only from the later publication event onward**. The old checklist remains a valid dated pre-release result, not a false statement retroactively.

## Verified new release identity

| Identity and evidence | Verified value |
| --- | --- |
| GitHub release | [`v2026.10-evidence-integrity`](https://github.com/lostlight530/research-software-identity-audit/releases/tag/v2026.10-evidence-integrity), **Evidence Integrity & Retained Verification** |
| GitHub published at | **2026-10-18T04:38:57Z** |
| GitHub tag source tree | Tag is **identical** to already-merged `main` commit [`a78e5fdcac843c7752b2122f68267688a44674ef`](https://github.com/lostlight530/research-software-identity-audit/commit/a78e5fdcac843c7752b2122f68267688a44674ef), from a GitHub compare (0 ahead/behind, zero changed files). A future `main` is not this tag. |
| Zenodo version record | [`23446162`](https://zenodo.org/records/23446162), created **2026-10-18T04:39:01.101885Z** |
| Zenodo **version DOI** | [`10.5281/zenodo.23446162`](https://doi.org/10.5281/zenodo.23446162) |
| Zenodo **concept DOI** | [`10.5281/zenodo.23166490`](https://doi.org/10.5281/zenodo.23166490) — unchanged |
| DataCite DOI registration | **2026-10-18T04:39:02Z**, state `findable`, relation **IsVersionOf = `10.5281/zenodo.23166490`** from [DataCite public DOI API](https://api.datacite.org/dois/10.5281/zenodo.23446162) |
| Zenodo file metadata | `lostlight530/research-software-identity-audit-v2026.10-evidence-integrity.zip`; **1,392,684 bytes**; **provider-reported** `md5:dbc5b4bdbd5e5fbb3b6fb6eb5ec44fa3` |
| Independent binary/ZIP verification | **NOT EXECUTED**; reported provider checksum is **not** a locally recomputed integrity verification |

The new archived release is the **fourth GitHub release** including `beta`, not a fourth experimental RS object. The frozen research sample remains **ten** fixed `RS01–RS10`; the analytical contract is **10 × 6 = 60** planned object-layer cells per eligible scheduled timepoint. Release success is **not** an eligible prospective-release judgment for the study.

## New confirmed embedded metadata drift

The **immutable new October 18 tag** contains:

- [Tagged `CITATION.cff`](https://github.com/lostlight530/research-software-identity-audit/blob/v2026.10-evidence-integrity/CITATION.cff): `version: v2026.10-evidence-reconciliation`, `date-released: 2026-10-10`, and previous version DOI `10.5281/zenodo.23284570`.
- [Tagged `codemeta.json`](https://github.com/lostlight530/research-software-identity-audit/blob/v2026.10-evidence-integrity/codemeta.json): `version: v2026.10-evidence-reconciliation` and `datePublished: 2026-10-10`.

These old values are valid **metadata inside the sealed tag**, but **incorrect as a self-description of the October 18 release**. The public new Zenodo record and DataCite DOI independently establish that the October 18 release exists; the metadata drift does **not** negate it.

This is the **second observed class instance** of already-archived embedded version metadata drift (after the earlier October 10 tag's October 6 embedded values). Its root cause **has not been independently established**; we do not infer that future Zenodo imports repaired the ZIP. Neither the October 10 nor October 18 old tag is rewritten.

## After-publication live-`main` correction

The separately reviewed correction on a **later GitHub branch** updates live `CITATION.cff` and `codemeta.json` to the **already verified** October 18 version tag and DOI. This is a **present-current** metadata change after the fact. It:

1. changes **only live repository metadata** after merge, not any immutable old tag nor the historical Release/Zenodo record;
2. retains the **concept DOI** as the family identifier and **OSF registration DOI** as frozen protocol identity;
3. appends a new dated block to `scholarly/identifiers.yaml` rather than editing the historically recorded top-level October 7 release fields;
4. adds a release checklist guard for future publication: **verify tag-embedded CITATION/CodeMeta against the target version before publishing**, and verify published external DOI relations after publication.

**No claim of complete historical tag byte inspection:** tagged citation and CodeMeta files and public GitHub tag compare were checked; the ZIP checksum was **not recomputed** from downloaded archive bytes.

## Study/source boundary and next action

The preceding [2026-10-18 diagnostic source record](../monitoring/2026-10-18/01-eleven-hour-workflow-ci-crosscheck/README.md) contains DataCite 72 DOI Works, OpenAlex 29 Work IDs, Zenodo/WorkflowHub counts and private LifeMonitor status attribution. The [later ORCID Beta Work update](../monitoring/2026-10-18/02-orcid-openaire-work-refresh/README.md) is a distinct **user-initiated scholarly metadata refresh**, not a new release.

**For a future release:** a checked pre-tag worktree, actual strict/offline evidence checks, source ZIP integrity checks where available, and post-publication DOI relation verification are pending, not retroactively marked successful. CI advisory success alone cannot supply these gates.
