# 2026-10-07 independent facility audit reconciliation

## Classification

- record class: `pre_eligibility_monitoring`
- prospective dataset member: **false**
- fixed corpus changed: **no**
- preregistered layer denominator changed: **no**
- operational seven-platform vocabulary changed: **no**
- collection window reported by source: `2026-10-07T14:45:45.460815+08:00` to `2026-10-07T14:56:19.143805+08:00`
- timezone: `Asia/Shanghai`

The frozen contract starts the prospective dataset only after an eligible post-registration release event in the fixed ten-object corpus. No such event is recorded before this capture. This package is therefore monitoring/reconciliation evidence, not a preregistered prospective timepoint.

## Source boundary

The source supplied in the 2026-10-07 conversation describes an assistant-run independent public-platform audit and references local artifacts such as `Results.json`, `RequestLog.json`, `CollectionContract.json`, `EvidenceManifest.json`, a 70-row `PlatformMatrix.csv`, and two collection/derivation scripts.

Those row-level/raw artifacts are **not present on fresh `main` and were not supplied as files to this update agent**. This package therefore preserves the supplied summary and only derives facts that can be reconstructed from that summary. It does not fabricate the missing request log, response bytes, hashes, 70-row platform matrix, or collection scripts.

## Canonical object-ID reconciliation

The supplied table used the earlier display-order mapping for RS06–RS10:

- RS06 china-agentic-observatory
- RS07 agentic-frontier-observatory
- RS08 sci-render-kit
- RS09 auto-doc-engine
- RS10 epistemic-pipeline

Fresh `main` already contains a 2026-10-06 correction establishing `corpus/object-manifest.csv` as authoritative. Derived files in this package therefore use:

- RS06 auto-doc-engine
- RS07 epistemic-pipeline
- RS08 sci-render-kit
- RS09 china-agentic-observatory
- RS10 agentic-frontier-observatory

The supplied ordering is preserved as source history; only the derived join key is corrected.

See `mapping-reconciliation.md`.

## Supported snapshot-level results

### Fixed ten-object corpus

- GitHub: all ten supplied as having the 2026-10-04 third release tag `v2026.10-open-research-production-framework`
- Zenodo family counters: 695 views / 664 unique views / 7 downloads / 6 unique downloads
- current-version counters: 54 version views / 46 version unique views / 0 version downloads
- DataCite: 40 fixed-corpus DOI records reported findable and typed Software
- ORCID: ten fixed-corpus groups / 50 source summaries
- Software Heritage: ten Zenodo DOI-origin routes reported with full visit, deposit release 3, and resolvable directory SWHIDs
- OpenAIRE: ten current-version DOI matches reported with status `UNDER_CURATION`
- OpenAlex: all 40 fixed-corpus DOI records reported matched; author A5151904252 reported with 40 Software works plus one OSF-registration `other` work

### Supplementary institution-facing surfaces

The source also reports RSD, OSF/Internet Archive, HAL, and RRID/SciCrunch state. These are retained as supplementary context only. They do not expand the frozen six-layer contract or the seven-platform operational vocabulary.

- RSD: 11 published software records reported, comprising the ten fixed-corpus software objects plus the separate audit runtime; `Agentic Research Constellation` reported public
- OSF / Internet Archive: registration `5b329` API and archive.org metadata reported readable
- HAL: ORCID query returned zero public results; this is not treated as evidence that no deposit was submitted
- RRID: one resolver attempt failed and another official path returned 403; `SCR_029105` remains an assigned identifier from prior user-held registry evidence, while public resolver readability is unresolved in this capture

## Same-day reconciliation addendum

Later same-day clarification is preserved in
`reconciliation.md`. It links the 2026-10-06 OpenAlex
`30 cached / 40 live` checkpoint to the supplied 2026-10-07 count of 41,
records the eight supplied OpenAlex primary topics, separates RRID assignment
from public-index visibility, and preserves the beta `lostlight530` creator
display as version-scoped metadata history.

## Evidence gaps and unresolved discrepancies

### Missing row-level 70-check matrix

The source states that a 70-row seven-platform matrix exists, but that file is not available in the repository or current file inputs. The matrix is therefore not reconstructed here.

### Zenodo package-byte discrepancy

Earlier repository records preserve 29,261,316 bytes for the ten 2026-10-04 version packages. The supplied 2026-10-07 summary reports 29,282,855 bytes, a difference of **21,539 bytes**.

This package records the discrepancy as `UNRESOLVED`.

It does **not** infer artifact mutation, because the row-level file-size/checksum manifest referenced by the supplied audit is not available to this updater. Resolution requires direct comparison of the ten per-record file metadata/checksums against the prior preserved package manifest.

### DataCite scope

The supplied 44 DOI checks are a scope count:

- 40 fixed-corpus DOI records
- 1 OSF registration DOI
- 3 audit-runtime Zenodo DOIs

This must not be interpreted as a 43 -> 44 temporal registration event without a scope-stable query and comparable timestamps.

### ORCID source distribution

The source reports 54 total summaries with source distribution DataCite 33 / OpenAIRE 11 / author-added 10. A previous snapshot also had 54 total summaries with a different source split. Equal totals do not imply no change; put-code/source diffing is required.

## Files

- `source.md` — conversation-supplied audit summary, transport formatting normalized
- `record.yaml` — bounded machine-readable reconciliation
- `cross-platform-snapshot.csv` — canonical RS mapping with supplied Zenodo/OpenAlex/ORCID summary fields
- `software-heritage-routes.csv` — canonical RS mapping for supplied Software Heritage route evidence
- `mapping-reconciliation.md` — explicit RS06–RS10 join correction

## Interpretation rule

This package follows:

`source summary -> normalized monitoring record -> bounded interpretation`

It is intentionally **not** promoted to:

`prospective observation -> preregistered result`

until the frozen eligibility condition is met.
