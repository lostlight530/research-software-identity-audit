# Contract implementation / vshwk

Source of scientific authority: OSF registration `vshwk`, **approved** amended schema response `6afdcc7108de91a0f0cefd6c`, submitted 2026-11-18T18:58:20.050020Z. OSF's outer registration `description` may still describe its original 2347 v2 and is **not** the latest-response authority. This control file is an implementation index only, not an amendment or replacement of OSF.

## Physical and logical separation

- The single existing control repo may own evidence for both studies; no new repo, no changes in any of RS01–RS10 or external platforms
- Study 1 `5b329` continues to own `contract/`, `monitoring/`, `evidence/` and its conditional `observations/`, including its still-undeclared concrete operational offsets. Nothing in vshwk initiates or completes a 5b329 prospective observation
- Study 2 `vshwk` owns `studies/osf-vshwk/contract/` and `studies/osf-vshwk/cycles/`; no implied reuse of RSIA historical diagnostic cells
- Pre-amendment records are historical context; read-only source repositories and existing GitHub historical audit files are neither raw vshwk prospective observations nor workflow execution receipts by mere path proximity

## Contract before observation

- Keep `endpoints-v1.json` immutable in published Git history; publish changed future manifest version rather than rewriting original. First cycle starts **after** this declaration and its own timestamped initiation reason
- A complete cycle must attempt each endpoint in the versioned manifest or explicitly record **why not attempted**, over both lineages and all eight layers
- Keep endpoint retrieval status, identity/relationship status, record-condition flags and testing/execution conclusion **separate**. `404` / timeout / CRAWL_NOT_FOUND / empty / rate-limited is not global absence
- A WorkflowHub registered v9 identity ≠ current main workflow SHA; no GitHub Actions status is inferred from a manifest file. Only same-workflow run IDs, attempts, heads and artifacts may support execution evidence
- Captures through an extractor lack direct origin HTTP bytes and possibly HTTP status: label `normalized_connector_representation` and preserve `original_provider_http_status: null`; do not silently call such fields HTTP 200
- Raw source custody, derived description, interpretation, correction and unresolved cells all remain individually attributable and append-only. No imputation, causal inference, inference of adoption or global quality composite
- Temporal reporting: maintain actual source timestamps UTC and Asia/Shanghai per OSF; America/Los_Angeles only as *reporting-day label*, never as a replacement scientific timestamp

## Scope-limited endpoint selection

Endpoint v1 uses 22 explicit source locators covering all eight layers. Each result, including failed/unrelated records, is separately retained. The shared project record is collected once. Other named discovery/monitoring services without a verified exact query contract are candidates, **not silent replacement endpoints or proof of no record**. If later judged required, record a protocol deviation and versioned change before future cycles; do not retroactively mutate this manifest.
