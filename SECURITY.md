# Security Policy

## Supported state

Security fixes apply to the latest commit on `main`.

Historical releases, baseline records, archived evidence, feature branches, and
pull requests are not maintained as independent security release lines.

## Private reporting

Report suspected vulnerabilities through GitHub Private Vulnerability Reporting:

https://github.com/lostlight530/research-software-identity-audit/security/advisories/new

Do not open a public issue containing credentials, tokens, private data,
working exploit details, or unpatched workflow weaknesses.

A useful report includes the affected path, commit SHA, reproducible steps,
expected boundary, observed behavior, and potential impact.

Reports are reviewed on a best-effort basis. No automated system accepts,
triages, or resolves security reports without human review.

## Security-relevant surfaces

Relevant surfaces include:

- GitHub Actions workflows and repository write permissions;
- evidence-collection or normalization tooling;
- parsers and validators that consume external records;
- provenance and correction ledgers;
- release and scholarly-metadata automation;
- any future networked collector introduced by an explicit change.

## Data and credential boundary

This public research repository does not require committed API keys, access
tokens, cookies, authorization headers, session identifiers, private emails, or
private messages.

If a collector later requires authentication, credentials must remain outside
the repository and outside committed evidence artifacts.

## Historical evidence

Historical evidence is preserved for auditability and is not active executable
content by default.

A historical error is normally corrected through a new correction,
reconciliation, amendment, or deviation record rather than silent replacement.
