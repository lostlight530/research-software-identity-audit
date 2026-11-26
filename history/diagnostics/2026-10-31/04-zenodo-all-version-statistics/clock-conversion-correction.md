# Clock-conversion correction — October 31, 2026

**Classification:** additive diagnostic interpretation correction, not a new observation, OSF amendment, changed schedule, release, or prospective timepoint

**Original source UTC timestamps:**
- start: `2026-10-31T05:41:22.929537+00:00`
- end: `2026-10-31T05:42:26.138306+00:00`

**Correct Asia/Shanghai timestamps (UTC+08:00):**
- start: `2026-10-31 13:41:22.929537`
- end: `2026-10-31 13:42:26.138306`

The initial draft of PR #77 incorrectly labeled this window **14:41:22–14:42:26 Asia/Shanghai**, effectively applying UTC+09:00. This was a report-layer timezone conversion error, not a new/future provider capture. The source-attempt ledger, `record.json`, and `evidence/2026-10-31/04-zenodo-all-version-statistics/source-provenance.json` already retain the actual UTC timestamps and remain unchanged.

The affected [04 interpretation](README.md), [02 cross-reference](../02-noon-user-page-reconciliation/README.md) and [monitoring index](../../README.md) now use the correct local-hour labels. The two affected public artifact manifests were updated against the corrected published README bytes. The original PR commits preserve the pre-correction text in Git history. No external raw response or historical evidence is rewritten.

**Verified against:** source UTC field and UTC+08:00 conversion, GitHub PR #77 creation at 2026-10-31T05:54:11Z (after the 05:42 UTC source window). This correction does not prove original provider bytes were independently recaptured.
