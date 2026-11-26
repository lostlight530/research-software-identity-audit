# Independent research identity and archive verification — 2026-10-18

**Diagnostic monitoring.** Actual retrieval window: **22:41:00–22:42:22 Asia/Shanghai**. Fixed corpus: **RS01–RS10**. Six analytical layers, seven operational platforms and 60 planned analytical cells remain unchanged. No prospective cells are created.

## Findings

| Surface | Captured result |
| --- | --- |
| Fixed-ten checkpoint | 10 GitHub release tags, Zenodo version labels and findable DataCite DOI identities agree |
| DataCite ORCID enumeration | 76 distinct findable records: 56 Software, 19 Workflow, 1 StudyRegistration |
| OpenAlex | Author profile 29; author-filtered works query 30; author cited-by count 1 |
| ORCID | 17 groups; 89 work summaries |
| Zenodo fixed-ten family totals | 2,398 views / 17 downloads; summed unique fields 1,559 / 16 |
| SWH | Latest origin visit is full with a snapshot for each of ten origins |
| OpenAIRE | Each of ten checkpoint DOI queries returns one result |
| HAL / SciCrunch | HAL query returns zero; SciCrunch request returns 403 |

The [earlier October 18 record](../01-eleven-hour-workflow-ci-crosscheck/README.md) retains its DataCite 72/53/18/1 and OpenAlex 29 results. Later responses do not replace that earlier capture. Family unique fields are not globally deduplicated people.

The initial bare-ORCID DataCite query returned only 56 software records. The URI-compatible query enumerated 76 records on one page; every returned record was separately checked for the exact ORCID suffix in creator/contributor identifiers. Both queries remain in the capture manifest.

## Archive metadata drift: independently inspected bytes

The control release `v2026.10-evidence-integrity` and DOI `10.5281/zenodo.23446162` are published/findable. Its downloaded ZIP is **1,392,684 bytes**, with locally recomputed MD5 **dbc5b4bdbd5e5fbb3b6fb6eb5ec44fa3**, matching the Zenodo metadata.

Root `CITATION.cff` and `codemeta.json` inside that ZIP still declare `v2026.10-evidence-reconciliation`. The citation includes the previous version DOI `10.5281/zenodo.23284570`. At independently captured main commit `053bc6a6c6f3659d2f5c9cc0c0542760081c1218`, both metadata files declare `v2026.10-evidence-integrity`.

This adds binary inspection to the earlier [postpublication reconciliation](../../../scholarly/release-identity-reconciliation-2026-10-18.md), which explicitly had not recomputed the ZIP checksum. It does not rewrite that historical limitation or the immutable release.

## Supplementary research-software pilot

Life Science Ecosystem Lab `v0.4.0`, DOI `10.5281/zenodo.23447089`, is separate from the fixed corpus. Its ZIP is **290,240 bytes** and recomputed MD5 **d5e515de06f37f03c7118fcee617ccd3** matches the provider value. Two specified GitHub Actions runs each expose five successful jobs. WorkflowHub 2347 version 2 resolves to `10.48546/workflowhub.workflow.2347.2`; bio.tools exposes version 0.4.0 and MIT. OpenEBench exposes the named record with `validated: 0`, not a benchmark result.

WorkflowHub version-detail Activity is retained separately from the earlier Team Dashboard. No private LifeMonitor data, workflow UUID, local filesystem path, community correspondence or unrelated telemetry is published here. Downloaded source code was not executed.

## Reproduction and evidence scope

- [Machine record](record.json), [DataCite identifiers](datacite-identifiers.csv), [Zenodo family fields](zenodo-family-statistics.csv)
- [Evidence and capture representation](../../../evidence/2026-10-18/03-independent-research-verification/README.md)
- [Minimal field extracts](../../../evidence/2026-10-18/03-independent-research-verification/field-extracts.json)
- [Capture manifest](../../../evidence/2026-10-18/03-independent-research-verification/capture-manifest.json)

Run `python -B tools/check_research_capture_20261018.py` for offline consistency and artifact-hash verification. Original full response and ZIP bytes remain locally retained; this public package contains explicit field extracts and original response digests, not a raw transport archive. Offline checks do not independently authenticate unpublished raw bytes. Public archive URLs permit a new download, whose equality must be checked against the retained digests.

Current remote schedule still declares no concrete offsets. SWH origin-full results do not establish a tag→commit→directory chain. Failed attempts remain in the capture manifest, including the RSD 400 followed by a corrected 200 and the SciCrunch 403. No historical baseline, contract, schema, schedule or prospective dataset is edited.

## Pre-merge correction: fixed-corpus object identity

During review of PR #48, the initial field-extract package assigned the wrong RS labels to four otherwise repository-linked records: `RS06` had `china-agentic-observatory`, `RS07` had `agentic-frontier-observatory`, `RS09` had `auto-doc-engine`, and `RS10` had `epistemic-pipeline`. The frozen manifest instead maps RS06 to `auto-doc-engine`, RS07 to `epistemic-pipeline`, RS09 to `china-agentic-observatory`, and RS10 to `agentic-frontier-observatory`.

This correction rekeys and orders only the **derived** `fixed_objects` records to match the unchanged `corpus/object-manifest.csv`; repository URLs, version DOI values, Zenodo counters, SWH response fields and original capture timestamps are not re-observed or fabricated. The original pre-correction extract remains identifiable in this PR's Git history. The initial `offline-verification.json` (149 reported checks) is a **pre-correction historical execution receipt**, not a fresh check of the corrected payload; it passed because it validated RS ID presence but not the authoritative ID-to-repository contract. A new checker validates that contract, repository-origin links, CSV joins, and a swapped-record negative regression. GitHub Actions separately reruns the executable checker after this correction.

Neither the original source bytes retained locally nor the immutable archives are changed. SWH `full` origin visits are **not** evidence that the October 14 checkpoint tags themselves were preserved. A response digest recorded without public raw bytes is provenance, not public replay proof.
