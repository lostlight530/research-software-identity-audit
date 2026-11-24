# VSHWK Cycle 01 — original capture ledgers and provenance

**Study scope:** OSF VSHWK approved amended Project 490 with paired lineages 2332 v9 and 2334 v9. All source collection was read-only; only the existing CONTROL repository received evidence writes.

## Original source ledgers — immutable

| File | Rows | Git blob |
|---|---:|---|
| [github-attempts.jsonl](github-attempts.jsonl) | 6 | `53550bd57e00530e58aad39756bfc50af94f6904` |
| [external-attempts-batch-01.jsonl](external-attempts-batch-01.jsonl) | 4 | `cd6c8ebdcdd8e23d0547d2380be1384927fb3a76` |
| [external-attempts-batch-02.jsonl](external-attempts-batch-02.jsonl) | 4 | `bb427834da8e2053295221b7afccd5161ce8f7c8` |
| [external-attempts-batch-03.jsonl](external-attempts-batch-03.jsonl) | 4 | `179216715a4ab4fa4b103ee192637615b6684cc8` |
| [external-attempts-batch-04.jsonl](external-attempts-batch-04.jsonl) | 4 | `29019357332fe3bdec108044b73c7912a65a57e2` |
| [external-error-followup.jsonl](external-error-followup.jsonl) | 5 | `b9e7fbd3db888738e7e91e8260861d77714a2e8a` |
| [github-workflow-content-crosscheck.jsonl](github-workflow-content-crosscheck.jsonl) | 2 | `2bb44d3c3caf5ae6187b1561be1b3df2d91f5121` |
| [registered-source-version-crosscheck.jsonl](registered-source-version-crosscheck.jsonl) | 2 | `28a5e7507bd8b3d54f644049d3e6fcd095f24006` |

The first five files contain exactly **22 predeclared endpoint attempts**. The five-row error follow-up is one separately retained, bounded multi-URL batch with per-endpoint outcomes; it is not five separately timed collection windows. The two workflow-file reads and two registered-source comparisons are supplementary crosschecks, not extra manifest endpoints.

## Source authenticity boundary

These files preserve GitHub connector representations and bounded extractor output. They do **not** preserve provider-origin HTTP body bytes, response headers, independently verified provider HTTP status codes, or complete pagination receipts. A missing origin status remains `null`; it must not be rewritten as HTTP 200.

Five bounded extractor fragments contain or may contain a neighboring page/header/error segment from batch concatenation. The original fragments remain unchanged. The normalized index flags this condition and uses only exact source-specific supported fields.

## Reading order

1. [Immutable manifest v1](../../../contract/endpoints-v1.json)
2. [Precollection intent snapshot](../precollection-intent.json)
3. Original source ledgers listed above
4. [Separately retained error follow-up batch](external-error-followup.jsonl)
5. [Supplementary GitHub workflow-file crosschecks](github-workflow-content-crosscheck.jsonl)
6. [Registered-versus-current source-version crosschecks](registered-source-version-crosscheck.jsonl)
7. [Normalized endpoint outcome index](../endpoint-outcome-index.jsonl)
8. [Derived machine summary](../cycle-summary.json)
9. [Human-readable cycle report](../README.md)

Software Heritage API documentation is not a live visit receipt. `CRAWL_HTTP_500`, `CRAWL_EMPTY_CONTENT`, timeouts, connector-policy rejection, and `SOURCE_NOT_AVAILABLE` do not prove record absence.
