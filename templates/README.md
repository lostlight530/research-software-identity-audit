# Research templates

This directory contains reusable templates for executing the preregistered study.

Templates are **not observations, evidence, amendments, deviations, or results**. They become study records only after they are copied into the appropriate operational directory, assigned real identifiers/timestamps, and completed with evidence.

## Study-specific daily workflow templates

- `studies/osf-wa5v8/daily-research-template.md` — Study 1 release-event eligibility gate, predeclared follow-up schedule, and 60 object-layer units per eligible scheduled timepoint
- `studies/osf-vshwk/daily-research-template.md` — Study 2 trigger surveillance, documented cycle initiation, and the immutable 22-endpoint manifest

These are navigation and workflow templates only. They do not create a schedule, observation, timepoint, cycle, endpoint attempt, or prospective dataset record. The two protocols have different initiation rules and must not share one execution template.

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
