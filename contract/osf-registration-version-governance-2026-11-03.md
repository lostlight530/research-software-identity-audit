# OSF original-registration and approved-revision authority — 2026-11-03

**Classification:** retrospective contract version/authority reconciliation. This is **not** a new OSF registration, OSF API write, revision submission, preregistration amendment, eligible research observation, reconstruction of an original HTTP response, or claim of latest live account/admin state.

## Distinct authority objects and clocks

| Object | Identifier and primary locator | Historical registered/source dates | Authority |
| --- | --- | --- | --- |
| Original registered study | [OSF 5b329](https://osf.io/5b329/overview), DOI [10.17605/OSF.IO/5B329](https://doi.org/10.17605/OSF.IO/5B329) | registration `2026-10-05T14:04:13.783851Z` (provider field in previously extracted registration response) | Original, publicly time-stamped research plan; not mutable GitHub runtime |
| Original Schema Response | [`6ac3ae5e6da32e3d0576ed72`](https://api.osf.io/v2/schema_responses/6ac3ae5e6da32e3d0576ed72/) | created `2026-10-05T14:04:14.757212Z`; modified `2026-10-05T14:06:00.148012Z` (OSF fields) | Original recorded `revision_responses` language |
| Later approved Schema Response revision | [`6ac4c12fed97b8b77ce88a9c`](https://api.osf.io/v2/schema_responses/6ac4c12fed97b8b77ce88a9c/) | created `2026-10-06T09:36:47.653316Z`; submitted `2026-10-06T09:58:52.719704Z`; modified `2026-10-06T09:59:27.955055Z` | Subsequent **approved** version; not evidence that its additions were in the original preregistration |
| Associated OSF Project | [`wa5v8`](https://osf.io/wa5v8) | separate project lifecycle | Supporting workspace, not the registration text or study denominator |
| Executable research control repo | [GitHub](https://github.com/lostlight530/research-software-identity-audit) | created `2026-10-05T14:59:45Z`, first reachable main commit `e5ba0a0e7dc548bd5bd3e79b4d7fc0cb95e528aa` at `14:59:46Z` | Mutable operational implementation, **never RS11** |

The registration **precedes** GitHub control-repository creation. GitHub source history cannot retroactively define what OSF initially contained.

## What is actually different between original and later approved response

The independently retained [October 30 version comparison](../monitoring/2026-10-30/01-osf-schema-response-version-reconciliation/field-diff.json) compared the accessible structured `revision_responses` values of **29 fields**. **28 were unchanged** and **one changed:** `344-83`, labelled **Other planned analysis** in the supplied Overview.

- **Original response:** permitted explicitly labelled secondary exploratory/post hoc work about unexpected state transitions, new aggregation, anomalies or unplanned infrastructure behaviors
- **Later approved response:** additionally gave *examples* including contextual family benchmarking, bounded sensitivity of engagement counters and tie-aware rank or percentile summaries, still labelled exploratory or post hoc
- These later examples are **not original preregistered primary analyses**, and the revision's supplied explanatory/justification text is not a substitute for independently comparing changed field values
- The field comparison does not prove that attachments, project resources, OSF backend state or unmodified raw source HTTP transport were completely compared
- The public extractor returned original/revised response representations with **2026-11-01 UTC-day acquisition labels** during this later review; the earlier Oct 30 machine diff preserves its own separate collector window. Neither is a newly acquired November 3 uncached original-provider byte capture

## Non-negotiable study units and naming contracts

- Fixed corpus is exactly **RS01–RS10** according to [`corpus/object-manifest.csv`](../corpus/object-manifest.csv). The distinct **CONTROL** repository, supplementary PILOT and external directories/standards are not RS11/RS12
- Six registered analytical layers are `source_repository`, `archival_repository`, `identifier_registration`, `author_registry`, `preservation_archive`, `discovery_graph`
- Seven operational platforms are GitHub, Zenodo, DataCite, ORCID, Software Heritage, OpenAIRE and OpenAlex; the last two map to the **same** `discovery_graph` layer. **60 object-layer units per eligible scheduled timepoint**, not 70 analysis units
- The initial-baseline historical cutoff is `2026-10-05T23:59:59+08:00`, with authentic later `retrieved_at` clocks on reconciliations. Current endpoint response cannot prove historical cutoff state
- Prospective data require a qualifying fixed-corpus new release **and** a valid declared operational observation schedule. The [current schedule](../schedule/README.md) does **not** declare numerical offsets. A new release alone must not backdate or manufacture timepoints
- Failed, blocked, partial, unresolved, HTTP 404 and HTTP 429 states are preserved by source and endpoint; none is automatically global nonexistence
- Planned analyses remain descriptive; no new inference, causal claim, imputation, global quality index or unlabelled benchmarking is introduced here

## What the November 3 full-history repository correction does and does not do

- **Done:** classifies pinned GitHub objects and existing dated diagnostic packages, indexes the original versus revised OSF authority with links to the already retained 29-field diff, and identifies historical naming aliases without moving sealed source paths
- **Not done:** modifying the original OSF registration or submitting another OSF revision; this GitHub-only session has **no authorized OSF write connector or authenticated administrative OSF session**. A read-only public extractor cannot be treated as edit authorization
- **Not justified:** an OSF amendment solely to rename local GitHub files, alter existing DOI identities, improve apparent completeness or turn prior monitoring into scheduled prospective observations

**Governance rule for any genuine future substantive change:** preserve the original and already approved version; use OSF's explicit revision/amendment process if authorized, retain the new OSF version ID, exact changed fields, submitted/approved times and rationale, and separately log corresponding GitHub `AMENDMENTS.md` or `DEVIATIONS.md` entries as applicable. A GitHub correction can never silently claim to be an OSF-approved substantive amendment.

## Reproducibility and evidence chain

- Previous exact field-level [OSF diff](../monitoring/2026-10-30/01-osf-schema-response-version-reconciliation/field-diff.json)
- Original/revised [dated source overview](../monitoring/2026-10-30/01-osf-schema-response-version-reconciliation/README.md)
- Existing [clause-level initial crosswalk](osf-overview-crosswalk-2026-10-08.md) remains an as-of-October-8 artifact, **not** silently rewritten to pretend it already knew the later verified version history
- [Canonical local contract mapping](preregistration.md) / [known limits](known-limitations.md) / [operational schedule](../schedule/README.md)
- [November 3 first-day-to-current Git provenance and file taxonomy](../docs/research-control-first-day-to-current-governance-audit-2026-11-03.md)

No frozen registration, historical raw evidence, metadata archive, Git tag, previous correction, schema, baseline, study corpus or prospective observation is changed by this documentation.
