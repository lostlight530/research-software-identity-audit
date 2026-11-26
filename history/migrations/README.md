# Historical path migration records

This directory contains append-only records of repository path migrations. Each ledger describes only its own source commit and scope; it must not be used to reconstruct a provider's historical state.

- [2026-10-08 monitoring/evidence path migration](monitoring-path-migration-2026-10-08.csv) — original 33-path migration record
- [2026-11-25 documentation path migration](path-migration-2026-11-25.csv) — former flat documentation and historical documentation classification
- [2026-11-26 archive consolidation](path-migration-2026-11-26.csv) — current migration of 871 tracked paths into the unified `history/` archive and the current record-path convention document

The 2026-11-26 ledger records original Git blob identities at the source `main` commit. Unchanged source artifacts retain their blob SHA. Any separately rewritten navigation or governance document is identified by its transformation class; source payloads and embedded historical manifests are not rewritten merely to make their old locators look current.
