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
