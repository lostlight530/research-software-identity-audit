# Research-control complete tracked-file and dated-event taxonomy — 2026-11-18

**Snapshot identity:** [CONTROL `78a617c1a4975da6b475a05b36e5ffe6487f1630`](https://github.com/lostlight530/research-software-identity-audit/tree/78a617c1a4975da6b475a05b36e5ffe6487f1630) acquired/assembled at **2026-11-18T15:37:08.881Z UTC**. The snapshot contains **803 tracked Git blobs**, **77 monitoring event directories**, **28 evidence event directories**, and a 45-day calendar from the **2026-10-05 registration/baseline** through **2026-11-18**. Counts are tree-navigation metrics, *not* preregistered observation units or a claim of tests run on every historic day

- [All tracked files, role, original Git blob SHA and explicit keep/alias action](tracked-file-classification.csv) — path-derived classification, not semantic authentication
- [Every dated event directory and evidence companion](dated-event-catalog.csv) — machine summary variant, local README, file count and paired directory
- [Calendar coverage including days without an event folder](first-day-through-nov18-calendar.csv) — no folder never proves missing a scheduled point
- [Frozen snapshot machine summary](snapshot.json) — count and category arithmetic, source commit and limitations

## Classification and renaming decision

**No destructive bulk rename.** The canonical event envelope is `monitoring/YYYY-MM-DD/NN-event-slug/`, with analogous `evidence/`. Retain `record.yaml` and `record.json` historical variants, byte-identified original artifacts, `source-attempts.jsonl` as client source projections rather than HTTP original bytes, all old source links and manifest hashes. The legacy `monitoring/2026-10-06/01-wave-01/` remains a **pre-eligibility diagnostic**, not a preregistered prospective wave; its preferred *display classification* is `PRE_ELIGIBILITY_DIAGNOSTIC_ALIAS` without changing its historical path. New files should use their role's stable names: `README.md`, `record.json` or inherited `record.yaml`, `source-attempts.jsonl`, `reconciliation.md`, `artifact-manifest.json` as appropriate. Do not rename unrelated domain-standard filenames or code files.

A file tagged `REPO_METADATA_OR_UNCLASSIFIED` or `PATH_BLOB_ONLY_NOT_SOURCE_REVALIDATION` is deliberately **not** represented as scientifically verified; a later file-level semantic review must identify its owning contract before any rename. No OSF, archive, old evidence, baseline, schedule, DOI, Release, or prospective timepoint is written here
