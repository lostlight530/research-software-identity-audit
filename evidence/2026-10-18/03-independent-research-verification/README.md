# Evidence representation — independent research verification, 2026-10-18

This package publishes **minimal derived field extracts**, request URLs, per-request local timestamps, response status, original transport length and SHA-256, and recomputed archive digests. Full raw response bytes and the two downloaded source archives remain in the maintainer's local audit package; they are **not included** here. No claim of a public raw-byte replay is made.

`field-extracts.json` records the fields used for identity joins, field sums, origin-visit status, DOI search counts, release metadata and archive-member inspection. Each source key maps to its endpoint in `capture-manifest.json`. GitHub/Zenodo/DataCite/ORCID/SWH/OpenAIRE/OpenAlex/OSF/bio.tools/OpenEBench records retain their original attribution and applicable terms. Repository licensing does not relicense the external source records.

`artifact-manifest.json` binds the public artifacts. `offline-verification.json` records a local offline verification, not a cloud CI outcome. The checker verifies hashes, joins and internal calculations; it does not replay the live collection or prove scientific accuracy of the archived software.

Private LifeMonitor identifiers, communications, access material, local paths and unrelated GitHub Traffic are excluded. Historical evidence packages are unchanged.

See [the dated monitoring record](../../../monitoring/2026-10-18/03-independent-research-verification/README.md).
