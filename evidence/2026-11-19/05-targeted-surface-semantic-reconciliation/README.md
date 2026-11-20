# 2026-11-19 targeted semantic surface evidence

This is a **new** targeted post-hoc diagnosis, not a retroactive reinterpretation
of prior raw responses. Source attempt keys and locators are in
[source-attempts.jsonl](source-attempts.jsonl); minimized identity fields in
[selected-fields.jsonl](selected-fields.jsonl); retrieval-method and timestamp
boundaries in [provenance.json](provenance.json).

The Exa-normalized source responses do **not** expose provider HTTP status or
original response bytes. The EDAM one-key GitHub Actions run **does** retain
original HTTP status, response size and digest, but not the original body bytes.
EDAM's actual RDF/XML parser returned nine matching term labels and version
`1.25-20260626T1230Z` — see [Run 44429333624](https://github.com/lostlight530/research-software-identity-audit/actions/runs/44429333624).
The run's artifact has a 30-day retention policy, so this package preserves a
stable subset and the digest rather than an expiring share URL.

InterLex and HAL remain UNKNOWN, and the 100-view Zenodo counter conflict remains
unresolved. No prospective dataset cells were created or changed. This package
makes no institution-endorsement, benchmark-success, or citation-usage claims.
