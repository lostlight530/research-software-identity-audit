# Derived artifact-manifest self-reference correction — 2026-11-13

**Class:** additive correction history for a derived integrity index, not a rewrite of source attempts, an external platform event, an OSF amendment or a prospective observation

- Original cloud-source capture: GitHub Actions [43265914410](https://github.com/lostlight530/research-software-identity-audit/actions/runs/43265914410), immutable attempt source ledger SHA-256 `d52b84134f0e88f30c71cee87d1718ae34d34b0863726c35cc4c271c06e8084e`
- The one-shot artifact archiver ran repeatedly on the PR branch. A later generated `artifact-manifest.json` enumerated **six** paths, including its own previous iteration. This makes a self-referential manifest entry, which cannot be validated as a stable published file
- Independent advisory CI [43267644575](https://github.com/lostlight530/research-software-identity-audit/actions/runs/43267644575) reported `row 2: external or self-referential artifact evidence/2026-11-13/01-full-institutional-recheck/artifact-manifest.json`; overall workflow `success` is not evidence that this advisory step passed
- The minimally scoped correction removed **only the self-reference** from `evidence/2026-11-13/01-full-institutional-recheck/artifact-manifest.json`, changing the derived manifest list from six entries to five. The hash/length references to source-attempts, selected-fields, summary, README and original sha256-manifest were not changed
- Correcting commit: [fb651c9e6bac3c4c67d210ee34f5adaebdfde0a5](https://github.com/lostlight530/research-software-identity-audit/commit/fb651c9e6bac3c4c67d210ee34f5adaebdfde0a5)
- The earlier generated file remains traceable in branch commit and CI history, not silently represented as having passed. This is a pre-merge correction to a derived verification index
- No OSF write, dataset cell, prior raw observation, platform account state, release, Zenodo DOI or study denominator changed

Disposition: `DERIVED_MANIFEST_CORRECTED_PENDING_INDEPENDENT_RETEST` at this correction event. The later exact GitHub Actions verification is an independent event and must not be backdated into this note
