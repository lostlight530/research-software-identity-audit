# Public data, privacy, and evidence handling

## Scope

This study audits public research-software and scholarly-infrastructure records.

The planned evidence concerns public objects and public metadata such as:

- public GitHub repositories, tags, releases, and timestamps;
- public Zenodo records and DOI metadata;
- public DataCite metadata;
- public ORCID work records and source summaries;
- public Software Heritage origins, visits, snapshots, and identifiers;
- public OpenAIRE records;
- public OpenAlex records;
- public OSF registration metadata and public archival copies.

The research does not require participant recruitment, private user telemetry, private communications, or behavioral tracking of visitors.

## De-identification policy

Public scholarly identifiers that are necessary to identify the research objects are preserved rather than pseudonymized.

Examples include DOI, repository URL, ORCID, public record identifier, release tag, timestamp, and public author name when directly relevant to attribution or propagation.

This is intentional: replacing canonical public identifiers would reduce reproducibility and make cross-infrastructure verification impossible.

## Do not collect or publish

Public accessibility does not authorize indiscriminate collection.

The repository must not intentionally retain:

- passwords, API keys, access tokens, cookies, session identifiers, or authorization headers;
- private or expiring share tokens when a stable public locator is available;
- IP addresses, device identifiers, analytics identifiers, or unrelated visitor telemetry;
- private email addresses, private messages, unpublished drafts, or restricted account data;
- personal information that is incidental to the infrastructure question and unnecessary for verification;
- material whose redistribution is prohibited even if it can be viewed in a browser.

If such material appears incidentally in a screenshot, response, log, or export, omit or redact it before committing evidence unless retention is necessary and separately justified.

## Evidence minimization

Capture the minimum evidence needed to verify the scholarly-infrastructure claim.

Prefer:

1. canonical public identifier or stable record URL;
2. relevant response fields;
3. retrieval timestamp and response state;
4. digest or archive reference where useful.

Avoid retaining full pages or payloads when a smaller evidence artifact proves the same point.

## Public does not mean historical

A public live endpoint observed today is evidence of the state visible at retrieval time.

It is not automatically evidence that the same representation was visible at an earlier historical time.

Historical claims require contemporaneous capture, immutable timestamps/records, or another source whose observable contract supports the historical inference.

## Research-control repository

`research-software-identity-audit` and its scholarly records are public meta-level evidence about the research infrastructure.

They may be recorded for provenance and scholarly-object propagation, but they are not an eleventh member of the fixed ten-object sample.
