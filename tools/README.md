# Tools

This directory is reserved for validators, collectors, normalizers, and analysis helpers that implement the repository's explicit contracts.

Tooling must not silently change research semantics.

Expected responsibilities include:

- validate object IDs against the fixed manifest;
- validate infrastructure-layer IDs;
- validate observation records against the JSON Schema;
- check required provenance;
- preserve failed attempts;
- reject undeclared sample-object expansion;
- keep operational schedule labels traceable;
- distinguish warnings from evidence-backed conclusions.

No external API credentials or secrets belong in the repository.
