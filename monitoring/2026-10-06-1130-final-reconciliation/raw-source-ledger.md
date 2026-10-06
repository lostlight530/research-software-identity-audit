# 11:30 final reconciliation source ledger

Logical checkpoint: **2026-10-06 11:30 Asia/Shanghai**

This record preserves the final initial-stage reconciliation inputs without
rewriting actual platform timestamps.

## User-observed state

- ORCID top-level Works UI: 12 work groups.
- Ten fixed research-software families are represented as ten work groups.
- Research Software Identity Audit is one separate infrastructure work group.
- The OSF preregistration is one separate work group.
- Zero-Entropy Lab and Agent Foundations each returned from 6 sources to the
  standard 5-source pattern after deleting one redundant DataCite source.
- Project work-identification count: 43 under the declared counting convention.
- OpenAlex author-profile cached works count remains 30.

## External endpoint verification

### GitHub release

Release:
`v2026.10-initial-research-runtime`

Published:
`2026-10-06T02:48:16Z`

### DataCite

Current release DOI:
`10.5281/zenodo.23176748`

Registered:
`2026-10-06T02:48:21Z`

Concept DOI:
`10.5281/zenodo.23166490`

The concept record reports two versions:

- `10.5281/zenodo.23166491` — beta
- `10.5281/zenodo.23176748` — v2026.10-initial-research-runtime

The current release DOI reports one citation relationship whose target is the
OSF preregistration DOI `10.17605/osf.io/5b329`.

Because the preregistration and software are outputs of the same research
program/researcher, this record treats the relation as a metadata-defined
self-citation relation, not an independent external literature citation.

### ORCID duplicate correction

Deleted records:

- Zero-Entropy Lab put-code `228686992` -> HTTP 404 after deletion.
- Agent Foundations put-code `228686999` -> HTTP 404 after deletion.

Surviving records:

- Zero-Entropy Lab put-code `228686993` -> DataCite,
  version DOI `10.5281/zenodo.23137204`,
  concept DOI `10.5281/zenodo.22791081`.
- Agent Foundations put-code `228686998` -> DataCite,
  version DOI `10.5281/zenodo.23137207`,
  concept DOI `10.5281/zenodo.22791169`.

### OpenAlex

Author:
`A5151904252`

Author-profile cached `works_count`:
`30`

Author-profile `updated_date`:
`2026-10-01T12:39:15`

Live works query count for the same author:
`40`

Exact DOI query for `10.5281/zenodo.23176748`:
HTTP 404.

Exact DOI query for `10.17605/osf.io/5b329`:
HTTP 404.

The 404 responses are recorded as query outcomes and are not generalized into
claims that the scholarly objects do not exist.


### OpenAIRE

User-supplied public OpenAIRE page at the final checkpoint reports:

- ORCID-linked software result count: `11`;
- page count: 3;
- `lostlight530/research-software-identity-audit: Beta— Research Runtime Bootstrap`
  present as **Research software**;
- publisher: Zenodo;
- DOI: `10.5281/zenodo.23166491`;
- author display: `lostlight530`.

This source is retained as user-supplied public-page evidence because the
OpenAIRE page could not be independently fetched during this reconciliation.
The reported count is therefore not promoted beyond the supplied page state.
