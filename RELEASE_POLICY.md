# Release and Archival Policy

This repository treats `main` as the current operational research state and
release tags as immutable point-in-time snapshots.

## Policy

- Create a release only from a reviewed and merged `main` revision.
- Do not move or rewrite an existing release tag to include later work.
- A release records repository state at publication time; it does not rewrite prior baseline, evidence, or preregistration history.
- Confirm citation, author, license, DOI-role, and related-identifier metadata before archival publication.
- Keep Zenodo concept DOI and version DOI semantically distinct.
- Add a version-specific DOI to release metadata only after that DOI actually exists.
- Preserve failed, partial, unresolved, and rate-limited research states in archived records.
- A release is not evidence that a scheduled observation executed or that a scientific conclusion is valid.

## Existing archive

The initial research-runtime release is:

- GitHub tag: `beta`
- title: `Beta— Research Runtime Bootstrap`
- release date: 2026-10-05
- Zenodo concept DOI: `10.5281/zenodo.23166490`
- archived beta DOI: `10.5281/zenodo.23166491`

The archived beta remains a historical snapshot.

Later changes to `main` must be represented by a later release if they are to
be included in a new archival snapshot.

## Metadata sources

For future GitHub-to-Zenodo releases:

- `.zenodo.json` is the Zenodo-specific archival metadata surface;
- `CITATION.cff` is the repository citation surface;
- `codemeta.json` is the general software metadata surface;
- `scholarly/identifiers.yaml` records identifier roles and provenance.

These files should agree on core repository metadata before a release is
published.

## Later formal runtime archive — 2026-10-06

The initial beta listing above is a historical snapshot, not a claim that the beta is the only published version.

- GitHub tag: `v2026.10-initial-research-runtime`
- GitHub published: `2026-10-06T02:48:16Z`
- Zenodo version DOI: `10.5281/zenodo.23176748`
- Existing concept DOI: `10.5281/zenodo.23166490`
- DataCite registered: `2026-10-06T02:48:21Z`

This is an **already archived** release, not a release performed by this documentation update. The original beta DOI `10.5281/zenodo.23166491` remains valid for citing that exact beta. For both version identities, see [scholarly/CITATION.md](scholarly/CITATION.md) and [scholarly/identifiers.yaml](scholarly/identifiers.yaml).

## Archived evidence-reconciliation release — 2026-10-10

The following is an **already published** immutable control-software release:

- GitHub tag: `v2026.10-evidence-reconciliation`
- GitHub release title: `Evidence & Scholarly Identity Reconciliation`
- GitHub published: `2026-10-10T15:45:40Z`
- Zenodo record: `23284570`, created `2026-10-10T15:45:46.175611Z`
- Zenodo version DOI: `10.5281/zenodo.23284570`
- DataCite version DOI registered: `2026-10-10T15:45:48Z`
- Unchanged repository concept DOI: `10.5281/zenodo.23166490`

Public identity evidence: [GitHub release](https://github.com/lostlight530/research-software-identity-audit/releases/tag/v2026.10-evidence-reconciliation), [Zenodo version record](https://zenodo.org/api/records/23284570), [DataCite version DOI](https://api.datacite.org/dois/10.5281/zenodo.23284570).

### Version-tag metadata discrepancy and later correction

The **already published, immutable** `v2026.10-evidence-reconciliation` tag still contains a `CITATION.cff` `version`, `date-released` and first version DOI, plus a `codemeta.json` `version`/`datePublished`, from **`v2026.10-initial-research-runtime` (October 6)**. See [tagged CITATION.cff](https://github.com/lostlight530/research-software-identity-audit/blob/v2026.10-evidence-reconciliation/CITATION.cff) and [tagged codemeta.json](https://github.com/lostlight530/research-software-identity-audit/blob/v2026.10-evidence-reconciliation/codemeta.json).

This is a genuine **archived-embedded citation metadata drift**, not an error in the existence of DOI `10.5281/zenodo.23284570`, which was independently registered. The **2026-10-11 live-main reconciliation** corrects current repository citation and CodeMeta pointers and documents the discrepancy; it **does not rewrite, move, or repair the tagged archival bytes**. For exact-archive citations use the registered version DOI and its actual GitHub release tag.

At the independent October 11 public comparison, Zenodo's [versions endpoint](https://zenodo.org/api/records/23284570/versions?allversions=true) enumerated **three** control-software versions, while the public DataCite [concept DOI metadata](https://api.datacite.org/dois/10.5281/zenodo.23166490) exposed `HasVersion` relationships only for the first **two**. DataCite's newly registered **version DOI** does independently expose `IsVersionOf=10.5281/zenodo.23166490`. This is a **bounded registry relation inconsistency**, not evidence that the third DOI is absent, nor a known sync mechanism or propagation-latency measurement.

These control-software releases are not RS01–RS10 eligible new-release events, and none starts the preregistered prospective dataset by itself.

## October 18, 2026 pre-package readiness — no new release

[The dated release-readiness review](scholarly/release-readiness-2026-10-18.md) checks the existing 3 control-software Release identities, concept/version DOI roles, citation/CodeMeta/Zenodo metadata boundaries, and actual pending archival gates. It does **not** change the immutable October 10 tag, predict a new DOI, publish a Release, or classify supplementary platform diagnostics as eligible prospective observations. Treat all unchecked items in the review as **not performed**, even when normal advisory CI succeeds.

## Postpublication October 18 evidence-integrity release — dated reconciliation

**This section was appended after the release.** The previous same-day [pre-package readiness](scholarly/release-readiness-2026-10-18.md) is retained as an **earlier** assessment, not erased or rewritten to pretend the future release already existed at that time.

- GitHub Release `v2026.10-evidence-integrity`: published **2026-10-18T04:38:57Z**, tagged source commit `a78e5fdcac843c7752b2122f68267688a44674ef`, independently compared with prepublication `main` as **identical**.
- Zenodo exact version record **23446162**, version DOI [`10.5281/zenodo.23446162`](https://doi.org/10.5281/zenodo.23446162), created **2026-10-18T04:39:01.101885Z**; stable **concept DOI** remains `10.5281/zenodo.23166490`.
- [DataCite](https://api.datacite.org/dois/10.5281/zenodo.23446162) reports registration **2026-10-18T04:39:02Z**, state `findable` and `IsVersionOf=10.5281/zenodo.23166490`.
- Zenodo exposes one ZIP (**1,392,684 bytes**) with provider-reported MD5 `dbc5b4bdbd5e5fbb3b6fb6eb5ec44fa3`. The actual ZIP was **not downloaded and locally rehashed** during this review.
- **New immutable-tag citation drift:** [October 18 tagged `CITATION.cff`](https://github.com/lostlight530/research-software-identity-audit/blob/v2026.10-evidence-integrity/CITATION.cff) and [tagged CodeMeta](https://github.com/lostlight530/research-software-identity-audit/blob/v2026.10-evidence-integrity/codemeta.json) embedded the earlier **October 10** version metadata. This new defect is independently verified and **not retroactively repaired in old archival bytes**.
- The *later live-main* `CITATION.cff`/`codemeta.json` correction to the new verified version DOI and date is a **different state** from the tagged archive. Dated evidence and corrective provenance: [scholarly/release-identity-reconciliation-2026-10-18.md](scholarly/release-identity-reconciliation-2026-10-18.md).

**Mandatory future release safeguard:** before creating the next immutable release, validate the exact proposed **tagged** `CITATION.cff` version/date/DOI and CodeMeta version/date against the intended new version; **never invent a Zenodo version DOI before registration**, and independently recheck after publication. A post-release live-`main` metadata fix is **not** tag repair or archival verification. The audit-control release is not RS11 and never automatically triggers a scheduled prospective observation.
