# October 8 retained morning identity evidence

This follows the original evidence → normalized observation → reconciliation structure
The capture was made by the original local collector on October 8 and imported after PR #19
It is not a new live observation or a prospective timepoint

`platform-responses.tar.gz` contains 17 exact public JSON responses
`response-manifest.json` records the original endpoint, timestamp, response status, byte size and SHA-256 for each archive member
`artifact-manifest.json` records the public supplement file digests
`verification.json` records the import verification result

Raw filenames retain the historical local RS IDs
The derived [Zenodo table](../../monitoring/2026-10-08-morning-recheck/zenodo-statistics.csv) joins repositories to `corpus/object-manifest.csv`
No corpus membership or preregistered layer changes are made

The [reconciliation addendum](../../monitoring/2026-10-08-morning-recheck/reconciliation-addendum.md) imports the collector's report
The [capture summary](../../monitoring/2026-10-08-morning-recheck/retained-capture-summary.json) records counts separately from the earlier updater's verification state
The original full local identity capture remains with the author; only responses needed for the imported counter and group/list claims are included here

Run `python -B tools/check_retained_morning_evidence.py` from the repository root to verify bytes, canonical joins and counts without network access
