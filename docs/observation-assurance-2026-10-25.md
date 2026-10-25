# Observation assurance and claim boundaries — operational logic review (2026-10-25)

**Classification:** repository implementation/assurance guide, **not** an OSF amendment, preregistration update, observation, synthetic result, new schedule, research finding, or release. Source for study authority: [frozen registration mapping](../contract/preregistration.md) and [OSF crosswalk](../contract/osf-overview-crosswalk-2026-10-08.md). Current GitHub implementation may be corrected without changing what was originally registered.

## The distinction being protected

The study does not ask whether an endpoint returns an attractive result. It asks what can be warranted by an observation of a *specific object*, through a *specific platform and observable contract*, at a *specific time*, under a *stated source and evidence boundary*.

For every future claim, separate:

| Dimension | Question | Do not substitute |
| --- | --- | --- |
| Research identity | Is it one of the **fixed RS01–RS10**? | CONTROL, pilot, related DOI, mirrored software or author Work |
| Observation unit | Which **object × one of six layers × timepoint**? | Number of HTTP requests, retries, platforms, returned DOI rows or summaries |
| Platform | Which of seven *operational* platforms emitted the response? | Another platform in the same layer; OpenAIRE ≠ OpenAlex |
| Target | Exact repository/release, family DOI, version DOI, Work, group, origin, snapshot or query? | A similarly titled but non-equivalent object |
| Transport | Did the request complete, return HTTP status, time out or encounter a challenge? | Object-level existence, acceptance, validation or indexing |
| Field representation | What was actually returned in which response/query shape? | UI screenshot, other query shape, other endpoint, reinterpretation |
| Clock | Event, registration, source-updated, request start/end, retrieval or review time? | One universal propagation clock or historical state inferred from a later read |
| Claim | Presence, attribution, preservation, discoverability, grouping, latency, consistency? | Global success/quality/impact/endorsement |
| Authority | Original source, researcher manual check, Codex extraction, reviewer verification? | Treating a downstream agent summary as a second independent source |
| Evidence level | Original retained bytes, digested local-only source, selected-field projection, transcription, interpretation? | SHA of absent bytes as if the bytes were public and reproducible |

The **60** fixed object-layer units per eligible scheduled timepoint are not **70** possible platform checks; repeated queries and retries are separate attempt evidence, not new units.

## What the executable guards now cover

`tools/check.py` supplements (but does not implement in full) the declared JSON Schema and source policies:

1. The **full seven-platform mapping** is checked against expected layer IDs, not only existence of seven legal names. Both OpenAIRE and OpenAlex remain independent `discovery_graph` platforms.
2. A candidate observation's platform/layer pair must match that mapping; it is not enough for both strings to independently be legal.
3. Retrieval and any supplied release-event timestamps must be valid ISO-8601 with **explicit timezone offsets**. For a prospective candidate, the source release time cannot be later than its retrieval time. This is an ordering check, not proof of a real eligible release.
4. `attempt_status` must be `completed` or `failed`; failures retain `failure_reason` and cannot **themselves** be called `fully_verified`. A failed, rate-limited or unresolved attempt remains an allowed research outcome.
5. Evidence references cannot be blank or knowingly left as the example locator. A nonblank reference is **not** by itself evidence authenticity, byte availability, licensing permission or independent verification.
6. A candidate explicitly marked `prospective` needs a release-event timestamp and cannot at the same time be flagged as retrospective reconstruction.
7. Files added under `observations/raw/` require `dataset_phase=prospective` and the presence of a repository-side **active** schedule declaration. The checker does **not** prove that this declaration predates results, covers every timepoint, establishes eligible first-release status, or matches all 60 cells.

This is deliberately **preflight validation**, not scientific acceptance. The current [schedule status](../schedule/README.md) records no active concrete offsets. An absence of qualifying raw prospective records is not a statement that all future observation logic has been executed.

**Test recipe**, offline and without new research observations:

```sh
python -m unittest discover -s tests -p "test_observation_semantics.py" -v
python tools/check.py --mode advisory
# Optional diagnostics, not the routine enforcement gate:
python tools/check.py --mode strict
```

Synthetic test inputs are deliberately labeled and stay in temporary test storage. Both GitHub Actions checks and strict-mode invocation report *implementation* properties; they do not create first-release evidence, a timepoint or a reviewer-signed research conclusion. The CI test step remains `continue-on-error` while the schema and baseline are still evolving.

## Independently checkable public artifact integrity

The existing October 25 published field-projection manifest is checked by a new **read-only standard-library verifier**: `python -B tools/check_public_artifact_manifest.py`. It compares each declared repository-relative published file's byte count and SHA-256 and rejects missing, duplicate, self-referential and traversal paths. The verifier accepts the historical `artifacts` or later `files` manifest lists without migrating either format. Synthetic negative tests demonstrate detection of tampered bytes and mismatched paths; GitHub CI executes them **advisory**, not as a strict study-enforcement gate.

**Scope:** verifying the manifest-listed *public bytes* does not independently replay the locally held original HTTP responses. It cannot establish a server signature, historical transport truth, platform ingestion time, scholarly acceptance or the authenticity of manually transcribed page observations. Existing evidence hashes remain attached to their original provenance; no source package is silently replaced.

## Researcher/agent provenance and independent evidence

A proper narrative does not describe “Codex verified X” if the **researcher checked a UI page** and Codex only transcribed or compared it with an API. Track these roles separately:

- **Original publisher/host:** source of the public API/object metadata and its observable guarantees
- **Researcher:** author of a manual page reading, timestamp/period if known, and a substantive interpretation or approval
- **Collector / Codex:** agent or local runtime that actually requested a particular API response, recorded output and constructed a field projection
- **Reconciler:** agent or human that compares two known source representations without rewriting either
- **Verifier:** independently checks the indicated *scope* (e.g., byte hashes, arithmetic, object joins or original API) and discloses whether original bytes and credentials were available

These are **activities and responsibility boundaries**, not automatically independent sources or cryptographic identities. A Git commit, successful CI check, digest and DOI each establish narrower facts than a scientifically valid observation.

This is consistent with the [W3C PROV-O entity/activity/agent separation](https://www.w3.org/TR/prov-o/), but this repository intentionally does **not** introduce an RDF store, PROV-O serialization dependency or new provenance framework. It retains explicit source/derived/reference links in the existing artifact structure.

For author registry interpretation, [ORCID documents source versus assertion origin](https://info.orcid.org/documentation/integration-and-api-faq/) and DOI-based grouping relationships. A source-summary count is not an independent-work count, the source of an assertion need not be the original publisher, and grouping does not establish legal identity proof.

For DOI-version relationships, [DataCite documents `HasVersion` and `IsVersionOf`](https://support.datacite.org/docs/versioning). They may be asserted independently, so a missing reverse `HasVersion` should be reported as a **directional relationship state**, not automatic invalidity of a resolvable version DOI. FORCE11 [software citation principles](https://force11.org/info/software-citation-principles-published-2016/) motivate distinct persistent/version-specific software identities, not an additional research sample.

## Conditional scientific acceptance gates (human/source-evidence review)

| Proposed claim | Sufficiently scoped evidence to seek | If unavailable |
| --- | --- | --- |
| Prospective dataset has started | Dated **active operational schedule**, eligible fixed-corpus release proof after registration, retrieval window, original study-unit mapping and contemporaneous evidence | `NOT_READY`; keep work in diagnostic `monitoring/` |
| A platform represents an object | Exact target identifier + query shape + returned identity fields + retrieval time | `UNRESOLVED` or `PARTIAL` |
| Object does not exist | Platform-specific authoritative absence contract and fully scoped request, not 404/empty alone | `NOT_FOUND_AT_THIS_ENDPOINT`, no global absence |
| Layer-level discovery is present | Positive evidence from one identified discovery platform, plus explicit attribution | Name the platform; do not infer the other discovery platform also has it |
| Layer-level discovery is absent | Evidence justifying absence for **both** relevant discovery systems and the intended universe; never infer from one blocked request | Unknown/unresolved at layer level |
| A state transitioned at time T | Directly evidenced platform event time or bounded before/after capture series | Only `first_observed_at` / interval bounds, not internal ingest time |
| Two reported counters are comparable | Same metric field, entity grain, query mode, aggregation semantics and compatible windows | Two separate source observations, **no delta** |
| A manual page and API agree | Researcher attribution + page value + matching API field ID and unit + both source periods if known | Describe equality of retained values only; capture time may be unknown |
| An independently reproducible result exists | Available original/publicly accessible evidence or declared restricted local archive, exact hashes and access limits, deterministic derivation | `PROJECTION_VERIFIED` rather than “raw evidence independently reproduced” |
| A correction supersedes an earlier interpretation | Original dated state + correction reason/evidence/time + affected downstream outputs + preserved historical path | `UNRESOLVED` / addendum, never silent rewrite |

**A supported absence, a failed HTTP request, a citation count, a “verified” field and an API transport success all answer different questions.** There is no global composite quality score.

## Repository operational decision procedure

For each substantive change:

1. Identify the **owning surface** first: frozen registration mapping, implementation, dated monitoring, raw evidence, derived observation, provenance, correction or navigation. Do not promote monitoring into `observations/` through a file move.
2. Trace `source evidence → raw observation → normalized/derived → interpretation → reported claim`, keeping source identities and missing links visible.
3. Check the smallest falsifiable contract: object identity, platform/layer, scope, time, metric definition, evidence and failure outcome. A reproducible counterexample is better than a decorative matrix.
4. If the source is ambiguous, return **UNKNOWN / BLOCKED / DEGRADED / PARTIAL / NO_CONCLUSION / NOT_EXECUTED** with a reason and retest condition. Preserve failed attempts.
5. For substantive correction, use dated append-oriented reconciliation instead of retroactively editing raw captures or the OSF preregistration.
6. Apply smallest repair, test on **synthetic** positive/negative cases, review diff, run advisory CI, disclose gaps, and verify merge/main. New tests do not make old observations more historically authoritative.
7. Keep the original [OSF registration](https://osf.io/5b329/overview) authoritative even when its interface permits later transparent/timestamped updates: later wording is **not** automatically original preregistration wording.

## Deliberately out of scope

No new software family or study layer, no arbitrary scheduled offsets, no platform discovery claims, no migration or reclassification of existing 2026 records, no additional release/DOI, no statistics/causal model, no mandatory JSON-LD/RDF/database, no LLM API, no added scheduled requests or external service calls.

The **current implementation is an advisory safety net**. It does not prove completeness of the future prospective denominator, full JSON Schema 2020-12 compliance, platform-native identity semantics, file-level evidence validity, researcher permission, or real-world truth.
