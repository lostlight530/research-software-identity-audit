# vshwk cycle 01 — retained capture attempts and provenance

Study scope: OSF vshwk approved amended Project 490 with workflow lineages 2332 and 2334. All collection was read-only, and all repository writes were restricted to the existing 11th CONTROL repository.

## Source ledgers (original retained, not overwritten)

- [github-attempts.jsonl](evidence/github-attempts.jsonl) — 6 row(s), blob `53550bd57e00530e58aad39756bfc50af94f6904`
- [external-attempts-batch-01.jsonl](evidence/external-attempts-batch-01.jsonl) — 4 row(s), blob `cd6c8ebdcdd8e23d0547d2380be1384927fb3a76`
- [external-attempts-batch-02.jsonl](evidence/external-attempts-batch-02.jsonl) — 4 row(s), blob `bb427834da8e2053295221b7afccd5161ce8f7c8`
- [external-attempts-batch-03.jsonl](evidence/external-attempts-batch-03.jsonl) — 4 row(s), blob `179216715a4ab4fa4b103ee192637615b6684cc8`
- [external-attempts-batch-04.jsonl](evidence/external-attempts-batch-04.jsonl) — 4 row(s), blob `29019357332fe3bdec108044b73c7912a65a57e2`
- [external-error-followup.jsonl](evidence/external-error-followup.jsonl) — 5 row(s), blob `b9e7fbd3db888738e7e91e8260861d77714a2e8a`
- [github-workflow-content-crosscheck.jsonl](evidence/github-workflow-content-crosscheck.jsonl) — 2 row(s), blob `2bb44d3c3caf5ae6187b1561be1b3df2d91f5121`
- [registered-source-version-crosscheck.jsonl](evidence/registered-source-version-crosscheck.jsonl) — 2 row(s), blob `28a5e7507bd8b3d54f644049d3e6fcd095f24006`

Exactly **22** predeclared endpoint attempts were retained in the first five files, followed by **five** separately timed individual error investigations and **four** exact-commit GitHub workflow-file crosschecks. The latter never replace the original connector status.

Source authenticity boundary: these files preserve GitHub connector representations and bounded Exa extractor output, not provider-origin HTTP body bytes, response headers, independently verified HTTP status codes, or complete pagination receipts.

Five bounded extractor fragments contain or may contain a neighboring page/header/error line from batch concatenation. The [normalized endpoint index](../endpoint-outcomes.jsonl) flags this and uses only exact source-specific supported fields. The original fragments remain unchanged.

Software Heritage API documentation is not a real visit response; CRAWL_HTTP_500, CRAWL_EMPTY_CONTENT, timeout, connector blocked and SOURCE_NOT_AVAILABLE do not prove record absence.

Reading order: [manifest](../../../contract/endpoints-v1.json) → [precollection intent](../intent.json) → original source ledgers → separately timed follow-ups → [per-endpoint index](../endpoint-outcomes.jsonl) → [machine summary](../summary.json) → [bounded report](../README.md).
