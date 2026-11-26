# OSF Project–Registration pair register and DataCite Commons reconciliation — 2026-11-26

**Record class:** dated scholarly-identity crosswalk; not a protocol amendment, observation cycle, prospective timepoint, or new study.

## Governing distinction

The research programme has **two independent OSF studies**, each represented by a public OSF **Project** and a distinct OSF **Study Registration**. The four OSF/DataCite records form **two one-to-one pairs (2 Projects : 2 Study Registrations)**. They are not four studies or four research samples.

A Project DOI identifies a project-level record. A Study Registration DOI identifies the frozen research plan and its revision history. Cite the identifier for the object actually used. Project descriptions and DataCite Work descriptions do not supersede the approved OSF Schema Response governing a study's protocol.

## Canonical 2 × 2 object mapping

| Pair | Study | OSF Project | Project DOI / DataCite type | DOI registered | OSF Study Registration | Registration DOI / DataCite type | DOI registered | Protocol authority |
|---|---|---|---|---|---|---|---|---|
| 1 | Research software identity propagation | [wa5v8](https://osf.io/wa5v8/) | [10.17605/OSF.IO/WA5V8](https://doi.org/10.17605/OSF.IO/WA5V8) · `Project` | 2026-10-31 | [5b329](https://osf.io/5b329/) | [10.17605/OSF.IO/5B329](https://doi.org/10.17605/OSF.IO/5B329) · `Study Registration` | 2026-10-05 | Approved response [6afdcc3a7fb0a89b0e3dd7e4](https://api.osf.io/v2/schema_responses/6afdcc3a7fb0a89b0e3dd7e4/) |
| 2 | Open research workflow identity | [AUHJF](https://osf.io/auhjf/) | [10.17605/OSF.IO/AUHJF](https://doi.org/10.17605/OSF.IO/AUHJF) · `Project` | 2026-11-12 | [VSHWK](https://osf.io/vshwk/) | [10.17605/OSF.IO/VSHWK](https://doi.org/10.17605/OSF.IO/VSHWK) · `Study Registration` | 2026-11-12 | Approved response [6afdcc7108de91a0f0cefd6c](https://api.osf.io/v2/schema_responses/6afdcc7108de91a0f0cefd6c/) |

Dates are the DataCite DOI registration dates displayed in the supplied Works listing. They are not OSF project creation dates or OSF registration submission/approval timestamps.

## Supplied DataCite Commons Works result

The owner supplied a text transcription of a DataCite Commons Works search filtered by ORCID `0009-0001-3617-0832`, Registration Agency `DataCite`, and client `cos.osf`:

[DataCite Commons Works query](https://commons.datacite.org/doi.org/?query=creators_and_contributors.nameIdentifiers.nameIdentifier%3A%280009-0001-3617-0832+OR+%22https%3A%2F%2Forcid.org%2F0009-0001-3617-0832%22%29&registration-agency=datacite&client-id=cos.osf)

The supplied listing reports four matching Works, with resource-type facets `Project = 2` and `Study Registration = 2`. The other displayed facets also report four results (creator Xuanyi Jiang, publication year 2026, DataCite, and Open Science Framework). These are counts inside this filtered Works result, not a census of all OSF objects or all works by the researcher.

**Source fidelity:** received 2026-11-26; original UI retrieval time, screenshot/HTML, and provider-origin API bytes were not supplied. This is an owner-supplied rendered-text transcription, not an independently recaptured DataCite response. No more precise retrieval clock is inferred.

## Pairing basis

- **Pair 1:** the Study 1 frozen-contract mapping explicitly names Registration 5b329 and associated Project wa5v8. The two DataCite Works have the same study title and distinct resource types.
- **Pair 2:** the current Study 2 record identifies Project AUHJF and separate Registration VSHWK. The two supplied DataCite Works have the same study title and distinct resource types. This is the owner-confirmed pair mapping; the DataCite facet counts alone are not a relationship assertion.

## AUHJF / VSHWK description representations — preserve separately

The supplied DataCite Commons listing describes the AUHJF Project Work using WorkflowHub Project 490, Lineage A (2332 v9), Lineage B (2334 v9), and 2347 v2 as historical context, while retaining the phrase about "three prospective observation waves". The supplied VSHWK Registration Work description also retains the three-wave phrase.

The repository separately preserves the owner-confirmed AUHJF OSF Project Description verbatim at [public-project-description.md](osf-vshwk/public-project-description.md). That retained text describes the earlier 2347 v2 focal case and three-wave framing. The DataCite Work description and this OSF Project Description are **different source representations**. The supplied listing does not establish whether they are the same underlying metadata field, when either representation changed, or whether one was synchronized from the other. Do not overwrite the preserved text or infer a provider-side edit timestamp.

The current VSHWK protocol authority is approved Schema Response `6afdcc7108de91a0f0cefd6c`: it defines the current Project 490 case with paired lineages 2332 v9 / 2334 v9 and event- or documented-review-initiated cycles, with no fixed interval, wave count, or end date. Project/registration descriptions are not protocol amendments.

The 2026-11-15 maintainer crosswalk remains an as-of record before the 2026-11-18 approved VSHWK amendment; it is not rewritten here.

## Non-actions and counting boundary

This reconciliation changes no OSF object, protocol, research question, sample, layer count, denominator, schedule, or historical record. It creates no observation, timepoint, or VSHWK cycle.

- **OSF object count in this mapping:** 2 Projects + 2 Study Registrations = 4 records
- **Independent studies:** 2
- **Study 1 analytical denominator:** 10 × 6 = 60 object-layer units per eligible scheduled timepoint
- **Study 2 case:** one WorkflowHub Project 490 case; eight project-layer bundles and sixteen nested lineage-layer evidence bundles per complete cycle; the sixteen nested bundles are not independent samples
- The shared CONTROL repository is research-control/evidence infrastructure, not RS11 or an additional study sample
