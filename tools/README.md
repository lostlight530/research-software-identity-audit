# Tools

This directory contains small validators, collectors, normalizers, and analysis helpers that implement the repository's explicit contracts.

Tooling must not silently change research semantics.

## Contract checker

Run:

```bash
python tools/check.py
```

The checker is dependency-free and currently verifies:

- the corpus remains exactly `RS01`–`RS10`;
- corpus repository identities remain unique and fixed;
- the preregistered infrastructure taxonomy remains exactly six layers;
- the operational platform vocabulary remains seven explicitly mapped platforms;
- OpenAIRE and OpenAlex remain distinct platforms under `discovery_graph`;
- the preregistered denominator remains 60 object-layer units;
- observation records require a concrete platform and evidence references;
- failed observations require a failure reason;
- no observation can introduce `RS11`;
- the initial baseline preserves its cutoff, reconciliation timestamp, Codex provenance, Zenodo counters, and Software Heritage `NOT_VERIFIED` boundary;
- live Zenodo counters cannot be backdated;
- the public-data handling policy retains its key exclusions.

GitHub Actions runs the checker on pull requests and pushes to `main`.

## General tooling responsibilities

Tools should:

- validate object IDs against the fixed manifest;
- validate infrastructure-layer and operational-platform IDs;
- validate observation records against the repository contract;
- check required provenance;
- preserve failed attempts;
- reject undeclared sample-object expansion;
- keep operational schedule labels traceable;
- distinguish warnings from evidence-backed conclusions.

No external API credentials, cookies, session data, or secrets belong in the repository.
