# Research templates

This directory contains reusable templates for executing the preregistered study.

Templates are **not observations, evidence, amendments, deviations, or results**. They become study records only after they are copied into the appropriate operational directory, assigned real identifiers/timestamps, and completed with evidence.

## Template set

- `observation-record.template.json` — one software object × one infrastructure layer × one observation timepoint
- `evidence-record.template.yaml` — provenance-bearing evidence record linked to an observation
- `observation-batch.template.yaml` — completeness manifest for one scheduled observation point
- `schedule-declaration.template.yaml` — operational schedule declaration without inventing preregistered offsets
- `provenance-record.template.yaml` — lineage from source evidence to reported output
- `correction-event.template.yaml` — append-only correction/state-transition record
- `analysis-manifest.template.yaml` — preregistered or exploratory derived-analysis declaration
- `amendment.template.md` — substantive post-registration change
- `deviation.template.md` — execution departure from a declared procedure
- `release-checklist.template.md` — scholarly/reproducibility release gate

## Non-data rule

Nothing under `templates/` is part of the prospective dataset.

Automated analysis must read operational records from their designated directories, never from `templates/`.
