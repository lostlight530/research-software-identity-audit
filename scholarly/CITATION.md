# Citation and identifier guidance

This research project has multiple linked scholarly identifiers with **different referents**. Cite the identifier for the actual object used; do not interchange the frozen study, evolving software family, and exact archived release.

## Frozen research design — OSF preregistration

**Jiang, X. (2026). _Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures_. OSF. https://doi.org/10.17605/OSF.IO/5B329**

This refers to the **preregistered study contract**, not the GitHub software runtime. The OSF registration remains frozen.

## Research-control software — concept DOI

Use **https://doi.org/10.5281/zenodo.23166490** when referring to the evolving `research-software-identity-audit` software family **across releases**.

The repository Zenodo badge intentionally points to this concept DOI. It does not identify a particular version and does not turn the repository into RS11.

## Exact archived software versions

| GitHub release tag | Published (UTC) | Zenodo version DOI |
| --- | --- | --- |
| `beta` | 2026-10-05 | [`10.5281/zenodo.23166491`](https://doi.org/10.5281/zenodo.23166491) |
| `v2026.10-initial-research-runtime` | 2026-10-06T02:48:16Z | [`10.5281/zenodo.23176748`](https://doi.org/10.5281/zenodo.23176748) |
| **`v2026.10-evidence-reconciliation`** | **2026-10-10T15:45:40Z** | **[`10.5281/zenodo.23284570`](https://doi.org/10.5281/zenodo.23284570)** |

The October 10 version DOI was registered at DataCite on `2026-10-10T15:45:48Z`; the October 6 initial-runtime DOI was registered `2026-10-06T02:48:21Z`. Use the **version DOI** when citing the exact archived snapshot actually used. Do not substitute the concept DOI or preregistration DOI for that snapshot.

**Software author:** lightlost — [ORCID `0009-0001-3617-0832`](https://orcid.org/0009-0001-3617-0832).

## Archived metadata discrepancy — not silently repaired

The October 10 `v2026.10-evidence-reconciliation` immutable GitHub tag was published with `CITATION.cff` and `codemeta.json` still describing the **previous October 6 version**. The version identity and registered DOI above were separately verified against the actual GitHub Release, [Zenodo record](https://zenodo.org/api/records/23284570) and [DataCite registration](https://api.datacite.org/dois/10.5281/zenodo.23284570).

Current `main` citation metadata was reconciled on October 11 to refer to the **latest archived release**, but this later edit **does not change the archived tag**. See [RELEASE_POLICY.md](../RELEASE_POLICY.md#archived-evidence-reconciliation-release--2026-10-10) for the correction note and the independent concept-DOI `HasVersion` vs version-DOI `IsVersionOf` difference.

The live `main` may contain work merged after the latest archival release; such later changes are **not part of the previous archived version** merely because the live citation metadata names that release.

## Boundary rule

OSF preregistration DOI, Zenodo concept DOI, Zenodo release DOI, GitHub repository URL, OSF project URL, ORCID and downstream registry identifiers refer to non-equivalent objects. No release here adds an eleventh object to the fixed RS01–RS10 sample or proves scientific validation, reuse or a prospective timepoint.

## Later verified control-software release — October 18, 2026

The existing archive table above is a **dated earlier view**. A **fourth control GitHub Release** was independently verified after the October 18 morning pre-package review:

| New GitHub release tag | GitHub published (UTC) | New Zenodo exact-version DOI |
| --- | --- | --- |
| [`v2026.10-evidence-integrity`](https://github.com/lostlight530/research-software-identity-audit/releases/tag/v2026.10-evidence-integrity) | **2026-10-18T04:38:57Z** | **[`10.5281/zenodo.23446162`](https://doi.org/10.5281/zenodo.23446162)** |

Zenodo confirms `conceptdoi=10.5281/zenodo.23166490`, and DataCite registered `10.5281/zenodo.23446162` at **2026-10-18T04:39:02Z** with `IsVersionOf` the same concept. The **new immutable October 18 tag still embeds October 10 version metadata** in `CITATION.cff` and `codemeta.json`. We retain that archived discrepancy and have only aligned **later live `main`** with the now-existing October 18 DOI; this does not change tag bytes or an already-created Zenodo ZIP.

See [2026-10-18 release identity reconciliation](release-identity-reconciliation-2026-10-18.md). Cite the **exact Oct 18 version DOI** for that archive and keep the concept DOI for the evolving research-control software family. The [OSF registration DOI](https://doi.org/10.17605/OSF.IO/5B329) continues to identify the frozen study design alone.

## Fifth control-software archive — October 31, 2026 (verified November 1)

The earlier October 18 text above is an as-of historical statement. A fifth GitHub control-software release now exists:

| GitHub release tag | Published (UTC) | Zenodo exact-version DOI |
| --- | --- | --- |
| [`v2026.10-control-lifecycle-reconciliation`](https://github.com/lostlight530/research-software-identity-audit/releases/tag/v2026.10-control-lifecycle-reconciliation) | `2026-10-31T15:55:06Z` | [`10.5281/zenodo.23839900`](https://doi.org/10.5281/zenodo.23839900) |

This is **one new version of the independent control software**, under the unchanged family concept DOI `10.5281/zenodo.23166490`. The version's [DataCite registration](https://api.datacite.org/dois/10.5281/zenodo.23839900) reports `IsVersionOf` the concept. The already published Git tag embedded October 18 `CITATION.cff` / `codemeta.json` metadata; this dated correction updates current `main` citation pointers **after** the release without altering immutable tagged or archived bytes. See [release policy correction history](../RELEASE_POLICY.md#postpublication-october-31-control-lifecycle-release--november-1-citation-reconciliation) and [November 1 bounded evidence record](../history/diagnostics/2026-11-01/01-periodic-identity-infrastructure-recheck/README.md) for provenance limitations.

The OSF preregistration DOI still refers to the frozen study design; no RS11, qualifying prospective event, new layer, unplanned timepoint or artificial DOI is introduced by this citation correction.

## November 17, 2026 GitHub-versus-Zenodo reconciliation / 2026-11-17 GitHub 与 Zenodo 版本身份校准

- **GitHub fact / GitHub 事实:** The repository has a later GitHub Release, [`v2026.11-nov15-identity-reconciliation`](https://github.com/lostlight530/research-software-identity-audit/releases/tag/v2026.11-nov15-identity-reconciliation), published 2026-11-15T15:55:57Z / 已存在 11 月 15 日发布的新 GitHub Release
- **Version DOI boundary / DOI 边界:** The last exact Zenodo version DOI independently documented by this repository's prior release reconciliation is `10.5281/zenodo.23839900`, belonging to the **October 31** release, not the November 15 tag / 已核实的 10 月 31 日 Zenodo DOI 不得转嫁给 11 月 15 日发行版
- **Unknown / 未核实:** No new Zenodo exact-version DOI for the November 15 GitHub Release was established in this November 17 review, so cite the November 15 GitHub tag URL for that precise GitHub object until its Zenodo archive identity is independently verified / 未核实新 DOI 前，精确引用 11 月 15 日 GitHub Release 链接
- **No retroactive edits / 不追溯改写:** No OSF preregistration change, RS11 addition, prospective observation, archive-byte revision, or automatically updated `CITATION.cff` / `codemeta.json` version identity follows from this documentation correction / 文档修正不改变冻结合同、研究总体、历史归档或机器元数据
