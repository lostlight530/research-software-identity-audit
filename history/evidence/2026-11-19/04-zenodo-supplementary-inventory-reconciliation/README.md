# 2026-11-19 supplementary Zenodo version identity reconciliation

**Record class:** targeted supplementary inventory reconciliation; not a prospective observation  
**Logical date:** 2026-11-19 (Asia/Shanghai)  
**Retrieval window:** 2026-11-18T18:36:56.430Z – 2026-11-18T18:36:57.436Z (UTC)

## Purpose

Resolve the two rows previously marked `UNKNOWN` in [the 2026-11-19 web-assisted inventory gap](../../../diagnostics/2026-11-19/03-web-assisted-surface-review/zenodo-supplementary-inventory-gap.csv). This is an additive reconciliation. The original 67-key Zenodo inventory, its 458-request cohort, and the earlier gap record remain unchanged.

## Resolved identities

| Repository | Role | Version | Zenodo record ID | Version DOI | Concept DOI | Zenodo latest | DataCite |
|---|---|---|---:|---|---|---|---|
| `research-software-identity-audit` | `CONTROL_NOT_RS11` | `v2026.11-nov15-identity-reconciliation` | 24249720 | [10.5281/zenodo.24249720](https://doi.org/10.5281/zenodo.24249720) | [10.5281/zenodo.23166490](https://doi.org/10.5281/zenodo.23166490) | `true` | `findable` |
| `life-science-ecosystem-lab` | `SUPPLEMENTARY_NOT_SAMPLE` | `v0.5.1` | 24249719 | [10.5281/zenodo.24249719](https://doi.org/10.5281/zenodo.24249719) | [10.5281/zenodo.23447088](https://doi.org/10.5281/zenodo.23447088) | `true` | `findable` |

## Independent identity checks

Each version was checked against three public identity surfaces:

- Zenodo Records API: record ID, version DOI, concept record ID/DOI, version label, publication date, created timestamp, version index, `is_last`, publication state and repository locator
- DataCite exact DOI query: version DOI, version label, registration timestamp, `findable` state and `IsVersionOf` relation
- GitHub Releases API: exact release tag, published timestamp and canonical release URL

The two Zenodo records report version indices 5 and 2 respectively, and both report `is_last = true`. Their DataCite version DOI records are `findable`.

## Inventory effect and boundaries

The earlier inventory remains **67 rows** as captured by the 458-request run. This additive reconciliation resolves two supplementary version identities, yielding **69 currently known version identities in this bounded inventory view**:

- RS01–RS10: 60 version identities
- CONTROL: 6 version identities; CONTROL is not RS11
- LSEL: 3 version identities; LSEL remains supplementary and outside the fixed sample

This is not a claim of global Zenodo inventory completeness, and 69 is not a study-unit denominator. The six preregistered layers, 60 analytical units per eligible timepoint, seven operational platforms and 70 possible platform checks remain unchanged.

No OSF write, schedule change, prospective cell, release, or DOI was created by this reconciliation. The separate 100-view discrepancy in the maintainer-supplied page counters is not addressed here.

## Evidence representation

- [Source attempt projections](source-attempts.jsonl)
- [Selected fields](selected-fields.jsonl)
- [Capture provenance](provenance.json)
- [Machine summary](summary.json)
- [SHA-256 manifest](sha256-manifest.txt)
- [Published artifact manifest](artifact-manifest.json)

The retrieval connectors returned normalized content and selected metadata but did not expose original provider HTTP response bytes or HTTP status codes. No original response bytes are claimed to have been retained. The stable public source locators and bounded retrieval window are preserved for independent rechecking.
