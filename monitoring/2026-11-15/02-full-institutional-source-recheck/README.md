# November 15 full bounded public-source attempt recapture

**UTC capture:** 2026-11-15T14:13:01.443173+00:00 – 2026-11-15T14:13:54.131351+00:00

**Requests:** 458/458 expected, HTTP-200 with no recorded failure 451/458; failed/partial by scope: surface=7

## Scope

34 existing supplementary URLs; 102 known DOI queries each at DataCite, OpenAIRE and OpenAlex; 67 Zenodo versions; eleven GitHub main and releases, eleven RSD software entries, ten SWH origins, two RSD issues, RSD person/project, four WorkflowHub JSON. All endpoint attempts preserve actual per-request UTC clocks and status/errors.

## Measured diagnostic fields (not study units)

- DataCite findable: 102/102
- OpenAIRE query positive: 94/102 (not distinct software)
- OpenAlex exact canonical DOI matches: 33/102; distinct returned Work IDs: 33 (HTTP 200 alone is not canonical match)
- Zenodo fixed ten: 4059 version views, 39 downloads with 60/60 valid record responses; a null total means unavailable, not zero
- ORCID groups / summaries: 18 / 117; SWH full latest origins: 10/10; WorkflowHub metadata successes: 4/4

## Evidence and limits

[Source attempts](../../../evidence/2026-11-15/02-full-institutional-source-recheck/source-attempts.jsonl) · [source hashes](../../../evidence/2026-11-15/02-full-institutional-source-recheck/sha256-manifest.txt) · [provenance](../../../evidence/2026-11-15/02-full-institutional-source-recheck/provenance.json) · [458-key changes](request-delta-vs-2026-11-13.csv) · [machine comparison](comparison-vs-2026-11-13.json)

Original provider HTTP body bytes are NOT retained, only SHA-256, lengths, UTC receipts and minimized public fields. The captured full request cohort is not a full positive indexing census, nor authenticated platform/UI state. No changes to frozen OSF, RS01–RS10, baseline, schedule, Releases, DOI, or original historical evidence. Six layers / 60 eligible point units, seven operational platforms / 70 possible checks; **zero prospective cells**.
