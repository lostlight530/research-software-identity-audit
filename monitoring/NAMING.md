# Naming and path migration (2026-10-08)

This document is a **repository presentation-path convention**, not an OSF preregistration amendment.

## Record paths

- Monitoring: `monitoring/YYYY-MM-DD/NN-<event-slug>/`
- Retained evidence: `evidence/YYYY-MM-DD/NN-<event-slug>/`
- `YYYY-MM-DD` = declared observation/capture date, **not** ingestion time.
- `NN` = ordering within the day, **not** a prospective wave index.
- Lowercase kebab-case for project directories and research record filenames.
- Preserve standard ecosystem filenames, Python `snake_case.py`, and established fixed corpus identifiers.
- Do not use `latest`, `current`, or `final` as canonical long-lived **path-state markers**.
- A source's original self-label (such as "Wave 3 final") is still retained **inside the historical record**, not promoted to contract authority.

## Record file roles

| Canonical name | Role |
| --- | --- |
| `README.md` | Human-readable entrypoint to the record |
| `record.yaml` | Normalized, bounded machine summary |
| `source.md`, `source-01-*.md` | Preserved source identity and claims |
| `verification.md` | Independent verifier's procedure and outcomes |
| `reconciliation.md` | Correction/addendum interpretation, source preserved in Git history |
| `capture-summary.json` | Derived retained-capture counters and scope |
| `*-statistics.csv`, `*-delta.csv`, `*-routes.csv` | Domain-specific tabular products |
| `capture-manifest.json` | Endpoints, capture timestamps, status, and raw-response digests |
| `artifact-manifest.json` | Public package paths and their expected byte digests |
| `raw-responses.tar.gz` | Byte-preserved compressed raw response evidence |
| `offline-verification.json` | Retained local verification report, **not** a GitHub runner result |

## Preservation and traceability

This migration relocates 33 tracked paths; every old path and its **original Git blob SHA** appears in [path-migration-2026-10-08.csv](path-migration-2026-10-08.csv).

- Source records that are only renamed reuse their exact Git blobs.
- Captured response archive bytes, archive member filenames, source response manifests, and canonical DOI/RS identity values remain unchanged.
- A small number of README/derived documentation and machine locator strings change **only** for internal links and paths. The migration ledger marks them.
- `artifact-manifest.json` is updated to bind the same retained artifact identities to their new paths; changed presentation files receive new SHA-256 digests. This is not a recapture.
- `offline-verification.json` preserves the previously run local checker report. It does not assert that the migration itself reran the checker.
- Historical prose in source records may mention old filenames; the mapping is the resolution contract. Do not silently change original source narratives.
- The original local names inside `raw-responses.tar.gz` include obsolete RS display mappings and are intentionally left intact. Derived CSV uses `corpus/object-manifest.csv`.

**Research semantics unchanged:** 10 fixed objects; 6 layers/60 object-layer units; 7 concrete platforms/70 possible checks; baseline cutoff; pre-eligibility classification; no RS11; no prospective promotion.

The existing `tools/check.py` remains the advisory GitHub CI check. `tools/check_retained_morning_evidence.py` remains an explicitly **local/offline** verifier and is not added to cloud CI.
