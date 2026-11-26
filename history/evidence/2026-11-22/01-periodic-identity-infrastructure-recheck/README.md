# November 22 identity and infrastructure evidence custody

This is the **existing November 22 diagnostic source-attempt package**, not a new retrieval, an official prospective observation, or an origin HTTP capture. This README was added after the original package was merged to restore the repository's required evidence entrypoint; original JSONL bytes and Git object identities are preserved.

## Retained source-ledger files

- [github-main-11.jsonl](github-main-11.jsonl): 11 exact GitHub main refs, compared with previously pinned Git objects
- [github-latest-releases-11.jsonl](github-latest-releases-11.jsonl): 11 latest public Release identities and publication clocks
- [github-open-prs-11.jsonl](github-open-prs-11.jsonl): 11 open-PR list attempts
- [zenodo-60-same-version-attempts.jsonl](zenodo-60-same-version-attempts.jsonl): 60 matched historical version IDs, typed same-key version counters and retrieval batch windows
- [zenodo-latest-ten.jsonl](zenodo-latest-ten.jsonl): ten new fixed-corpus version DOI/record identities, separate from the 60 historical version keys
- [datacite-ten-new-doi.jsonl](datacite-ten-new-doi.jsonl): ten matching DOI registry identities and `findable` fields
- [openaire-ten-new-doi.jsonl](openaire-ten-new-doi.jsonl): ten exact DOI-query result projections, not independent adoption/aggregation proofs
- [supplementary-source-attempts.jsonl](supplementary-source-attempts.jsonl): 34 fixed supplementary URLs, including errors and bounded extracts
- [rsd-11-software-project-person.jsonl](rsd-11-software-project-person.jsonl): 11 software records and two separately typed project/person page extracts
- [swh-ten-origin-probes.jsonl](swh-ten-origin-probes.jsonl): ten bounded SWH attempts; extracted documentation is not a structured visit census
- [public-interactions.jsonl](public-interactions.jsonl): RSD #1870/#1871, RSE #498 and epistemic-pipeline #261 read-only GitHub states

The machine summary holds **11 canonical Git blob SHA-1 identifiers** for these files and the precise record totals. Git blob identity verifies retained repository bytes, **not** authenticity of the provider's response. Extractor batch UTC bounds are not individual server-side HTTP arrival timestamps; provider HTTP bodies/status were unavailable in these captures. Failed/blocked reads, OpenAlex/ORCID/SWH unknowns and unverified adoption are preserved as such.

**Counting boundary:** RS01–RS10 only, CONTROL is not RS11, six preregistered layers yield 60 analytical units per eligible scheduled timepoint. Version-row totals or supplementary endpoints cannot replace that denominator. Prospective rows generated: **0**.

See [Nov22 monitoring report](../../../diagnostics/2026-11-22/01-periodic-identity-infrastructure-recheck/README.md), [machine summary](../../../diagnostics/2026-11-22/01-periodic-identity-infrastructure-recheck/summary.json) and [later entrypoint correction record](../../../diagnostics/2026-11-22/01-periodic-identity-infrastructure-recheck/record.json).

**Correction provenance:** [Prior merged PR #136](https://github.com/lostlight530/research-software-identity-audit/pull/136) produced [advisory Actions run 45036674186](https://github.com/lostlight530/research-software-identity-audit/actions/runs/45036674186); its record-path checker returned three errors although the overall advisory workflow concluded `success`. This README repairs the missing entrypoint without changing source data or claiming another capture.
