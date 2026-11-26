# Public evidence — independent research recheck, 2026-10-20

`field-extracts.json` contains the minimum public scholarly fields used for the dated research claims. `capture-manifest.json` preserves endpoint, per-request retrieval interval, status, original byte count and SHA-256 for every attempt. Full response bytes remain locally retained and are not included here; these artifacts are **derived public extracts**, not a transport archive.

The archive digest checks rehash locally retained October 18 ZIP bytes against October 20 provider metadata. They are not new download events. The public record contains canonical archive URLs, sizes, digests and selected root-member metadata, without redistributing complete source ZIPs.

User-source page values remain explicitly separate from independent API and version-detail Activity. Public scientific identifiers remain necessary for matching. No private monitoring IDs, local paths, correspondence, access material or unrelated telemetry is included. External records retain their original attribution and applicable source terms under `LICENSING.md`.

`artifact-manifest.json` seals the public artifacts. `offline-verification.json` is a local result, not a GitHub runner result. The checker is read-only, offline and not added to cloud CI.

[Research record](../../../monitoring/2026-10-20/01-independent-research-recheck/README.md)

## Correction history

Review of PR #50 found four derived object-ID labels inconsistent with the frozen object manifest. See [correction reconciliation 01](correction-reconciliation-01.md) for the exact old-to-canonical mapping, preserved pre-correction commit, and verification boundary. The original `capture-manifest.json` and all source-attempt metadata are unchanged. The previous `offline-verification.json` result is superseded because it predates the identity-mapping assertion; the corrected checker runs in the existing advisory GitHub Actions workflow.
