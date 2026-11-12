# November 13 cloud source recheck evidence

Public read-only diagnostics captured by GitHub Actions, corrected collector run [43265914410](https://github.com/lostlight530/research-software-identity-audit/actions/runs/43265914410)

- Source: authenticated-to-GitHub-only GitHub Actions runner; all scholarly endpoints read without user account sessions
- Scope: 34 established source surfaces, 102 known DOI identifiers, Zenodo versions, public GitHub repositories, Software Heritage and upstream public interactions
- Record identity: source-attempts.jsonl stores bounded per-request URL, UTC start/end, HTTP/error, source SHA-256, byte length, and minimized selected fields
- No original HTTP response bodies are archived in the repository; hashes alone do not allow independent historical byte replay
- Source artefact lineage: [first cloud run 43265103686](https://github.com/lostlight530/research-software-identity-audit/actions/runs/43265103686) retained as original diagnostic; second cloud run is a corrective collector rerun, not an alteration of the first
- All source API and UI results are exploratory/diagnostic only, never 60 preregistered prospective cells
- Failed and incomplete accesses remain in the attempt ledger; HTML success and canonical DOI mismatch require semantic scrutiny

This evidence directory contains public fields and source references, not credentials or private session state
