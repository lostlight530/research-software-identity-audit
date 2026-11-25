# VSHWK Day 2 — independent retained source attempts

The Day 2 precollection declaration was committed in `05325a1c2cf6b9289eac1a230743c8753bfd8576` before the first source read. These are new queries, **not reused Day 1 results**, and their invocation envelopes are preserved without inventing provider transaction clocks.

- [Primary GitHub attempts](github-primary-attempts.jsonl) — six exact manifest locator attempts; the GitHub workflow content endpoint returns plain YAML and the two Actions URLs were connector-rejected
- [External endpoint extraction attempts](external-extraction-attempts.jsonl) — 16 exact non-GitHub manifest URLs, including partial results, Zenodo 500 extraction errors and Software Heritage documentation false-positive risk
- [Supplementary pinned workflow and exact Actions URL checks](github-supplementary-file-and-actions.json) — two source-file Git blob identities plus two same-URL Actions attempts through another extractor, **not a rewriting of original GitHub connector outcomes**

**Source fidelity:** provider-origin HTTP bodies, response status, and headers are **not** saved. Returned third-party extractor snippets and connected GitHub selected fields are not equivalent to original transport receipts. A rendered documentation example is not a verified live Software Heritage visit. Distinct source identity and true retry attempt clocks are preserved.
