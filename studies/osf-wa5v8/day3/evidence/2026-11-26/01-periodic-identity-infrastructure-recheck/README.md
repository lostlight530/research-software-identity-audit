# Day 3 source evidence index

This package retains minimized source connector/extractor representations, source locators and actual collector invocation windows. It is not provider-origin HTTP bytes/status custody. Git blob SHA identifies the retained content, not external authenticity; no origin-body SHA-256 is fabricated. Exact list of 53 retained pre-index file paths and blob hashes is in the [machine record](../../../monitoring/2026-11-26/01-periodic-identity-infrastructure-recheck/record.json).

Selected source groups:
- GitHub: `github-rs*.jsonl`, pinned citation receipts and `github-comparison-derived.jsonl`; citation literal follow-ups preserve earlier filter limitations.
- Zenodo matched cohort: `zenodo-same-version-*.jsonl` (70 unique rows); `zenodo-usage-exa-batch*.jsonl` earlier independent pass (70 rows, same values, not additional versions). Concept-latest receipts are separate from same-version usage counts.
- Registry/discovery: DataCite concept/exact-version and follow-ups; OpenAIRE concept/exact-version and timed-out follow-up; OpenAlex concept and exact-version quota/error receipts.
- SWH and ORCID: `swh-orcid-control.jsonl`, plus later SWH quota gap and separate follow-up. Documentation-style responses cannot establish live visits.
- Supplementary: use `supplementary-surfaces-01-09.jsonl`, `10-18.jsonl`, `19-26.jsonl`, `27-34.jsonl` as the selected 34-row cohort (the names share the supplementary-surfaces prefix); overlapping 19–27 and 28–34 records are additional attempts, not a second population.
- Institutional interactions and explicit PR merge-status receipts; OSF authority follow-up; CONTROL archive and tagged citation receipts.

[Evidence minimization correction](evidence-minimization-correction.json) preserves original blob identities and redacted proposed-main replacements. The two repeated batches, failures and unknowns are not silently overwritten. Source-level clocks are not observation schedule dates. No global absence inference.
