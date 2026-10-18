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
