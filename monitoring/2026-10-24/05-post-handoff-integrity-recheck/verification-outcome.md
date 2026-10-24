# October 24 post-handoff review outcome — attributed CI evidence

**Status: deterministic transport / structural replay passed for the stated scope**, not a claim of scientific interpretation or external API authenticity

## Executed evidence, distinct from the initial PR draft

- [PR #60 CI run 40053930687](https://github.com/lostlight530/research-software-identity-audit/actions/runs/40053930687) completed successfully for source head `3bf742a103528d1cf5425f30f50bcecde850a24b`
- The **specific** `Verify October 24 local-history handoff transport (advisory)` step completed with a `success` conclusion, not merely an overall green job
- The Python checker reported **22,485 checks, 0 failed**, independently validating **28 manifest-listed files + 1 self-excluded manifest**, **4,444 request-attempt projection rows**, **1,162 SHA-256 content-addressed objects**, and **4,267 ledger rows**
- Exactly **21 attempt rows have no public_endpoint locator** in the retained projection. These still retain the original available attempt metadata and must not be silently dropped, relabeled as disallowed hosts, reconstructed as HTTP requests to a guessed URL, or mistaken for an absence of attempts
- The first advisory CI run [40053852170](https://github.com/lostlight530/research-software-identity-audit/actions/runs/40053852170) had an **overall green workflow but a failing transport step** because the first checker incorrectly expected 29 `artifacts` entries (the self-excluded manifest leaves 28) and required a URL in all rows. It was corrected in subsequent commits without editing the historical evidence files
- The existing contract checker, historical retained-evidence checkers, and October 24 Zenodo arithmetic checker also have separate successful step results on the linked CI run

## Review status and remaining boundaries

This outcome is attached to the **specific CI run and source SHA** above; its success does not retroactively prove earlier runs passed or predict later runs. Historical raw external HTTP response headers and missing public URLs cannot be reconstructed by the offline checker. Source copyright/license, API-server freshness, scientific discovery, and alternative interpretations remain separate responsibilities

The **frozen** OSF registration remains authoritative. RS01–RS10 / six analytical layers / seven operational platforms / 60 eligible object-layer units are unchanged. This follow-up adds **zero prospective cells**, no schedule offset, no release, no imputed history, no sample expansion. The separate Zenodo 2,681 vs 2,836 source representations remain `UNRESOLVED`, not proven +155 traffic

See [same-day bounded source review](README.md), [machine record](record.json), and [release inventory](github-release-inventory.csv)
