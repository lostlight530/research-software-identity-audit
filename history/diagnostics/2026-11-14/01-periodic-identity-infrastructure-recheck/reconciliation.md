# Correction: GitHub client batch clock applies only to branch SHA recheck

**Correction class:** derived provenance-scope clarification, made after independent 2026-11-14 self-tests. **Not** a new platform capture, new research sample, new prospective timepoint, new DOI, new Release, or OSF contract amendment

## Source and defect

The original diagnostic record was merged in [PR #113](https://github.com/lostlight530/research-software-identity-audit/pull/113) at [commit `f95efda3bc1bb0411a02d07cfc628a5193223260`](https://github.com/lostlight530/research-software-identity-audit/commit/f95efda3bc1bb0411a02d07cfc628a5193223260)

The machine summary originally used `github.client_batch_window_utc` without an explicit scope label. The human README grouped direct GitHub branch, PR and Release checks next to that time window. **Only the final repeated 11-repository `branches/main` request batch** is independently supported by:

- Client batch start: **2026-11-14T05:17:13.240Z**
- Client batch finish: **2026-11-14T05:17:14.548Z**

Other GitHub PR and Release requests were performed in separate earlier API calls. Their exact per-request client/server retrieval timestamps were not retained in the dated record. This provenance correction **does not reconstruct, assume, or backdate those times**. A common general-time label does not substitute for a real per-request receipt

## Bounded correction and retained evidence

- Keep `github.client_batch_window_utc` **byte-identical in value** and explicitly set its scope to `final_main_branch_sha_recheck_only` in the derived `record.json`
- Explicitly classify separate PR/Release request windows `NOT_RETAINED_DO_NOT_INFER_FROM_MAIN_BRANCH_BATCH`
- Clarify the README sentence and link to this correction. Original README and machine JSON remain recoverable at the pinned Git commit and their original blob SHAs
- Preserve the 11 GitHub source-head SHA entries, their Nov 13 comparators, `309 + 4 = 313` historical ahead counts, zero reported open PRs and fixed/release totals exactly as observed at their respective source reads
- Preserve all previously dated 34 surface access records and caches; no original or previous evidence file is rewritten
- This patch is **metadata interpretation only**; no new origin HTTP bodies, source timestamps, OSF prospective cells or institutional approvals are created

## Independent recheck, separate observation clock

Independent same-day audit at client **2026-11-14T09:20:50.441Z–09:21:36.638Z** found all fixed ten `main` SHAs had independently advanced **31 main-reachable commits in total**, each behind 0, relative to the earlier Nov 14 captured HEADs. Each compare returned **one changed D14 audit document** per repository. All 11 repositories had **0 open PRs** and published GitHub Release inventories remained six per fixed RS repository and five for CONTROL, with no newer published Release than the Nov 10 fixed-corpus checkpoint. These are **newly retrieved, distinct source clocks** and do not invalidate the prior immutable as-of snapshot

The independent file/source-level consistency audit also checked 22 direct assertions over the pinned study manifest, six-layer/60-unit contract, 34 exact URL identities and failure ledger, 11 captured prior-main joins, release counts, RS01 Zenodo attached-family arithmetic, old 458 attempts, and 67 old Zenodo version rows: **22 pass, 0 fail** at client **2026-11-14T09:19:54.873Z**. The repository's merged [Actions run 43561262184](https://github.com/lostlight530/research-software-identity-audit/actions/runs/43561262184) separately passed. This self-test is **not** a fresh seven-platform origin-source census or independent byte-for-byte replay of external caches

**Disposition:** `DERIVED_PROVENANCE_SCOPE_CLARIFIED`; no evidence values, historical source identity, frozen contract or original raw data changed; `NO_PROSPECTIVE_CELLS`
