# Tools

This directory contains small validators, collectors, normalizers, and analysis helpers that implement the repository's explicit contracts.

Tooling must not silently change research semantics.

## Contract checker

Run:

```bash
# bootstrap/default: report findings without blocking work
python tools/check.py --mode advisory

# explicit enforcement when you intentionally want a hard gate
python tools/check.py --mode strict
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

GitHub Actions currently runs the checker in **advisory mode** on pull requests and pushes to `main`. Contract findings are surfaced as warnings but do not block ordinary repository work during bootstrap/baseline reconciliation. Strict mode is opt-in and should only become the default gate after the baseline/schema have stabilized.

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
