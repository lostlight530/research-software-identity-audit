# Release-readiness review — 2026-10-18 (pre-package, no release)

**Status: CONDITIONAL / NOT YET PACKAGED.** This is a dated **documentation and source-checking checklist**, not a scientific observation, OSF amendment, automated release request, version declaration, GitHub tag, Zenodo upload, or DOI registration. No release is created by this review.

The control repository is a scholarly research **runtime** for the [frozen OSF registration](https://osf.io/5b329/overview); it is **not RS11**. The registered study has exactly **RS01–RS10**, six infrastructure layers (60 object-layer cells per eligible timepoint), and seven operational platforms. This PR's 2026-10-18 user-reported supplementary WorkflowHub/LifeMonitor/bio.tools/DataCite observation does **not** change the preregistered study design or start prospective data collection.

## 1. Frozen identity and existing immutable versions

| Source | Reviewed identity / boundary | Observed state |
| --- | --- | --- |
| Frozen design | [OSF 5b329](https://doi.org/10.17605/OSF.IO/5B329) | The frozen contract remains the scientific authority; no OSF writes |
| Live source | [`research-software-identity-audit`](https://github.com/lostlight530/research-software-identity-audit) | The latest base `main` was `ffce1be75fa7f4bfb8f6e1a86dd51b9db60d922b` **before** this documentation/monitoring branch. Confirm new `main` SHA and green CI **after** merge |
| Zenodo family DOI | [`10.5281/zenodo.23166490`](https://doi.org/10.5281/zenodo.23166490) | Version-independent identity and badge target; never replace with an invented new DOI |
| Existing release 1 | `beta` → [`10.5281/zenodo.23166491`](https://doi.org/10.5281/zenodo.23166491) | Archived historical release; do not move |
| Existing release 2 | `v2026.10-initial-research-runtime` → [`10.5281/zenodo.23176748`](https://doi.org/10.5281/zenodo.23176748) | Existing immutable archive; do not move |
| Existing release 3 | `v2026.10-evidence-reconciliation` → [`10.5281/zenodo.23284570`](https://doi.org/10.5281/zenodo.23284570) | **Latest verified published** control release at the time of this review (October 10), not necessarily current `main` contents |

The public GitHub Releases endpoint enumerated the three published control releases above. A public GitHub **tag-list API** attempt was blocked by the available connector, so this review **does not claim an independent exhaustive tag-ref verification** beyond Release identities.

## 2. Metadata crosswalk — changes required at actual next release

| File | Current verification | Preparation decision |
| --- | --- | --- |
| [`CITATION.cff`](../CITATION.cff) | Currently identifies `v2026.10-evidence-reconciliation`, October 10 and its **existing version DOI**; also states the **concept DOI** and frozen OSF DOI separately | **Do not predeclare a future version DOI.** At a real new Release event, set the actual new tag/date and record only DOI values that already exist |
| [`codemeta.json`](../codemeta.json) | Current `version`/`datePublished` refer to the October 10 release; `identifier` is the stable concept DOI | For a future release, align version/date to that release's actual published identity, keeping the concept DOI's role explicit |
| [`.zenodo.json`](../.zenodo.json) | Zenodo software metadata: MIT, software, creator/ORCID, study-registration and associated-project relationships | Check expected Zenodo landing-page metadata on a **new** archive independently; no existing archived bytes rewritten |
| [`scholarly/identifiers.yaml`](identifiers.yaml) | File `recorded_date: 2026-10-07` retains **then-current** top-level tag `v2026.10-initial-research-runtime`. Subsequent **append-only October 10 reconciliation** and separately dated release policy identify the later October 10 release | Historical top-level state is **not** evidence that the latest public release reverted to October 6. Preserve it as dated history; when preparing a new Release use a **new separately dated amendment/entry**, not a silent rewrite |
| [`RELEASE_POLICY.md`](../RELEASE_POLICY.md) | Requires reviewed/merged `main`, existing DOI identity checks, provenance, and immutable tag handling | **Follow as controlling release procedure**; no actual release/tag/DOI action is authorized by this checklist |

**Known archived discrepancy, not a reason to rewrite history:** the **immutable October 10 tag** embeds metadata that still pointed to the older October 6 release. See [the original release policy's correction history](../RELEASE_POLICY.md#archived-evidence-reconciliation-release--2026-10-10). Live citation metadata was later reconciled, but the old archived tag remains the old bytes. A future tag must be checked against its *own* metadata before publication.

## 3. Packaging gates and scientific scope

- [x] Read fresh `main`, open PRs, contract, corpus, schedule, monitoring evidence and scholarly/citation metadata for this maintenance cycle.
- [x] Identify already-published control-software Releases and exact version-vs-concept DOI roles.
- [x] Keep October 16–18 monitoring snapshots **append-only** and separately labelled by source (user page, public API, private LifeMonitor observation), metric semantics and retrieval clock limits.
- [x] Keep **DataCite Commons 72 DOI Works** distinct from **OpenAlex author 29 Works** and the fixed corpus of ten software objects; the full 72 DOI identifiers were **not** enumerated by this review.
- [x] Do not republish private LifeMonitor workflow/test-instance identifiers, cookies, tokens, share URLs or restricted records in a public evidence package.
- [ ] Verify final **merged** `main` SHA, complete PR diff, and post-merge advisory CI; **not yet fulfilled by this pre-merge review**.
- [ ] Run offline retained-evidence verification as appropriate (`python tools/check_retained_all.py`) on the actual packaged revision; **not executed** during this API-backed review.
- [ ] Run `python tools/check.py --mode strict` at packaging time as an explicit separate gate; **not executed** here. Advisory CI is not strict scientific validation.
- [ ] Review every file to be included in a new immutable artifact for research-purpose minimization, missing expected evidence, source attribution, correction histories and private material.
- [ ] Before any future publication, select the actual immutable tag/version and date, verify `CITATION.cff`, CodeMeta, Zenodo metadata, and archived source byte/tree identity **on that tag**, then inspect actual Zenodo/DataCite relations **after** publication.
- [ ] Only then publish and capture the actual GitHub Release, Zenodo version record and DOI registration/retrieval timestamps. **A new DOI cannot be safely predicted, reserved or inferred here.**

## 4. Decision

**Do not automatically package/release based on counts, successful advisory CI, or an 11:00 user dashboard.** The branch is ready for PR review and normal merge once its evidence/links are self-checked; a new archival **version is a later, separate, deliberately reviewed action**. Pending gates above are not failures to be filled with invented confirmations.

This is a small/stable maintenance closeout: preserve old evidence, identify current owner of every metadata role, avoid spec drift, and leave actionable but honest packaging prerequisites rather than growing a new framework.
