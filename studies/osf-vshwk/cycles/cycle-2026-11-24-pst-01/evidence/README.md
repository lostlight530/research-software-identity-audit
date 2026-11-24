# VSHWK Cycle 02 evidence custody

All files in this directory belong to Cycle 02, reporting day 2026-11-24 America/Los_Angeles. Actual acquisition clocks are recorded in UTC and Asia/Shanghai in the corresponding source ledgers.

| File | Purpose | Representation / limitation |
|---|---|---|
| `github-attempts.jsonl` | Four L1 GitHub source reads and two L6 Actions endpoint attempts | GitHub connector output; workflow YAML text initially triggered a local JSON parse error, corrected by the separate raw-text follow-up |
| `workflow-A-current-main.yml`, `workflow-B-current-main.yml` | Raw current workflow source text | Connector-returned YAML, not origin HTTP bytes |
| `workflow-content-followup.json` | Append-only record of the YAML parser correction | No provider response was overwritten |
| `registered-source-version-crosscheck.jsonl` | Current main workflow blob SHA vs immutable registered v9 blob | Supplementary source-file readback |
| `external-attempts-batch-01.json` | WorkflowHub, Zenodo, DataCite and DOI resolver | Exa normalized extraction; no origin HTTP bytes/status |
| `external-attempts-batch-02.json` | SWH, ORCID, OpenAIRE and OpenAlex | Exa normalized extraction; preserves partials/errors |
| `external-error-followup.json` | One exact-endpoint retry for both Zenodo searches | Both returned the same connector error |

Do not convert connector errors into provider HTTP statuses, negative query results, or global absence. Do not infer a workflow run from a workflow file or WorkflowHub record.