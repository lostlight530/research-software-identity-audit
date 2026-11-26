# October 25 retained public field projections

Companion of [monitoring record](../../../monitoring/2026-10-25/02-independent-institutional-recheck/README.md)

- [Source attempts](source-attempts.csv): actual request clocks, endpoint/Accept shape, HTTP or transport outcome, original local response byte count and SHA-256
- [Canonical object fields](canonical-object-fields.json): fixed IDs, DOI families/versions, release commits and chain predicates
- [Zenodo statistics](zenodo-family-statistics.csv), [DataCite identities](datacite-identifiers.csv), [OpenAlex identities](openalex-works.csv)
- [Researcher transcription](user-page-transcription.json), [page/API reconciliation](user-page-api-reconciliation.json), [WorkflowHub representations](workflowhub-source-comparison.csv)
- [Institutional selected fields](institutional-state-extract.json)

These are minimized, attributed projections from locally retained public responses, not raw HTTP byte artifacts. Original response hashes remain inspectable in the attempt ledger; those hashes do not imply the original bytes are included in this PR. Local response digests were verified before projection. Researcher-provided counts are a structured transcription, not a screenshot or original HTML. Failed access paths remain in the ledger

Public identifiers required for research traceability remain. Private test workflow/suite UUIDs, incidental personal fields, credentials, emails, local absolute paths, full HTML, internal automation methods and SOPs are omitted
