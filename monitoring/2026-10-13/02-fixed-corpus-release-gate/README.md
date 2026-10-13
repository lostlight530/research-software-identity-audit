# Fixed-corpus public release gate — 2026-10-13 evening

**Class:** `diagnostic_monitoring`, independent supplement to the [October 13 noon control-only audit](../01-control-noon-recheck/README.md), **not** a preregistered prospective observation or a schedule declaration

**Scope:** the frozen `RS01–RS10` repository mapping in [the object manifest](../../../corpus/object-manifest.csv). The independent audit-control repository is **not** RS11. This review checks only public GitHub Release listings and attempts to check public Git tag listings. It does not claim a simultaneous multi-platform identity census or alter the frozen [OSF contract](../../../contract/preregistration.md).

## Direct source and retrieval provenance

- GitHub connector public Releases list, `GET /repos/{owner}/{repo}/releases?per_page=5`, for ten fixed repositories, **outer request window** `2026-10-13T11:44:24.854Z`–`2026-10-13T11:44:26.211Z` = **2026-10-13 19:44:24.854–19:44:26.211 Asia/Shanghai**
- GitHub connector `GET /repos/{owner}/{repo}/tags?per_page=100` attempted for the same ten repositories, outer window `2026-10-13T11:44:57.876Z`–`2026-10-13T11:44:58.261Z` = **2026-10-13 19:44:57.876–19:44:58.261 Asia/Shanghai**; the connector rejected every attempted URL with `INVALID_ARGUMENT`. **No Git tag data were returned.** This is a connector restriction, not GitHub evidence that tags do not exist
- [source-attempts.csv](source-attempts.csv) preserves **20 independent endpoint-attempt records**: ten parsed Release lists and ten blocked tag-list attempts, with exact requested URLs and bounded batch time windows
- [record.yaml](record.yaml) is a bounded machine summary. These are **outer concurrent tool-call windows**, not per-response HTTP completion, GitHub server Date headers, raw transport bytes, or verified historical snapshots. This review did not preserve byte-identical response bodies or response hashes

## Observed public GitHub Release state

All ten Release-list queries returned **three listed releases per repository**. The newest returned public Release for every fixed corpus repository was `v2026.10-open-research-production-framework`, with individual published timestamps **2026-10-04 13:00:12Z–13:00:39Z** (October 4, 21:00:12–21:00:39 Beijing time).

| Object ID | Repository | Latest returned public GitHub Release published (UTC) |
| --- | --- | --- |
| `RS01` | [`welcome-to-github`](https://github.com/lostlight530/welcome-to-github/releases/tag/v2026.10-open-research-production-framework) | `2026-10-04T13:00:12Z` |
| `RS02` | [`zero-entropy-lab`](https://github.com/lostlight530/zero-entropy-lab/releases/tag/v2026.10-open-research-production-framework) | `2026-10-04T13:00:14Z` |
| `RS03` | [`Axiom-0`](https://github.com/lostlight530/Axiom-0/releases/tag/v2026.10-open-research-production-framework) | `2026-10-04T13:00:17Z` |
| `RS04` | [`reflective-continuum`](https://github.com/lostlight530/reflective-continuum/releases/tag/v2026.10-open-research-production-framework) | `2026-10-04T13:00:21Z` |
| `RS05` | [`agent-foundations`](https://github.com/lostlight530/agent-foundations/releases/tag/v2026.10-open-research-production-framework) | `2026-10-04T13:00:23Z` |
| `RS06` | [`auto-doc-engine`](https://github.com/lostlight530/auto-doc-engine/releases/tag/v2026.10-open-research-production-framework) | `2026-10-04T13:00:32Z` |
| `RS07` | [`epistemic-pipeline`](https://github.com/lostlight530/epistemic-pipeline/releases/tag/v2026.10-open-research-production-framework) | `2026-10-04T13:00:36Z` |
| `RS08` | [`sci-render-kit`](https://github.com/lostlight530/sci-render-kit/releases/tag/v2026.10-open-research-production-framework) | `2026-10-04T13:00:39Z` |
| `RS09` | [`china-agentic-observatory`](https://github.com/lostlight530/china-agentic-observatory/releases/tag/v2026.10-open-research-production-framework) | `2026-10-04T13:00:26Z` |
| `RS10` | [`agentic-frontier-observatory`](https://github.com/lostlight530/agentic-frontier-observatory/releases/tag/v2026.10-open-research-production-framework) | `2026-10-04T13:00:29Z` |

**Result, limited to this interface:** none of the ten freshly retrieved public GitHub Release listings showed a published Release after the **2026-10-05** OSF registration. Therefore this check provides **no evidence of a new eligible fixed-corpus GitHub Release event**. It does **not** prove that every possible tag, commit, private release, release-like external event, or contract-specific eligibility condition has been fully examined. The ten tag-list attempts were blocked and remain explicitly `NOT_VERIFIED`.

The frozen preregistration's first-eligible-release gate and absent concrete [operational offsets](../../../schedule/README.md) are **not satisfied or waived by this negative scoped listing result**. No prospective start, planned observation denominator, new timepoint, inferred propagation latency, or zero-count cross-platform observation matrix is declared.

## Governance and next retest

- No amendments, deviations, frozen baseline edits, release/tag/DOI creation, object expansion, or schema changes
- Keep this follow-up separate from the noon seven-platform **control-repository-only** review: the two reviews have different subjects and evidence windows
- Recheck current fixed-corpus releases when a concrete post-registration candidate event or schedule declaration is available; verify any candidate against the real frozen eligibility terms **before** classifying prospective data
- Re-attempt tag enumeration only via an authorized, supported public read path, recording its actual retrieval time. Do not relabel the connector's unsupported response as a GitHub 404 or as proof of no tags

**Assessment:** `PUBLIC_GITHUB_RELEASE_GATE_NO_NEW_RELEASE_OBSERVED`; `GIT_TAG_ENUMERATION_BLOCKED`; `PROSPECTIVE_START_NOT_ESTABLISHED`
