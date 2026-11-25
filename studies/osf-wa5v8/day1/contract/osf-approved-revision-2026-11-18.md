# OSF 5b329 approved revision authority crosswalk — 2026-11-18

## Record identity

- **Registration:** [OSF 5b329](https://osf.io/5b329/overview)
- **Registration DOI:** [10.17605/OSF.IO/5B329](https://doi.org/10.17605/OSF.IO/5B329)
- **Current approved Schema Response:** [6afdcc3a7fb0a89b0e3dd7e4](https://api.osf.io/v2/schema_responses/6afdcc3a7fb0a89b0e3dd7e4/)
- **Created:** 2026-11-18T16:03:06.533991Z
- **Submitted:** 2026-11-18T18:58:21.950303Z
- **Modified:** 2026-11-18T18:58:29.183773Z
- **OSF review state:** `approved`
- **Updated response keys:** `344-47`, `344-86`
- **Source list:** [OSF registration schema responses](https://api.osf.io/v2/registrations/5b329/schema_responses/)

This is the current approved revision of the existing registration. It is not a new registration, a new study, a new sample, or a prospective observation record.

## What the approved revision clarifies

### 1. Fixed analytical scope

The registered study remains:

- Ten fixed research-software objects: RS01–RS10
- Six predefined scholarly-infrastructure layers
- Seven operational platforms: GitHub, Zenodo, DataCite, ORCID, Software Heritage, OpenAIRE, and OpenAlex
- Sixty object-layer analytical units per scheduled observation point: 10 × 6 = 60

OpenAIRE and OpenAlex are separate operational platforms within the same `discovery_graph` layer. The seven-platform operational scope does not create a seventh layer or replace the 60-unit analytical denominator.

### 2. Research Software Identity Audit (RSIA) role

The approved response explicitly defines RSIA as supporting research-control, evidence, provenance, and reproducibility infrastructure.

RSIA is not:

- an eleventh sampled research-software object;
- an additional operational platform;
- an additional infrastructure layer;
- a prospective observation unit; or
- an independent research finding merely because its software releases, inventories, validation records, or operational monitoring are archived.

Its machine-readable contract mapping, fixed-corpus manifest, observation schemas, state taxonomy, counting rules, evidence/provenance conventions, retained-evidence packages, and append-oriented correction documentation support execution and reproducibility of the registered study.

### 3. What did not change

The revision justification explicitly states that no changes were made to:

- the five research questions;
- the fixed RS01–RS10 corpus;
- the six infrastructure layers;
- the seven operational platforms;
- the 60 object-layer analytical units per observation point;
- the sampling strategy;
- the observation schedule;
- measured variables and derived-variable definitions;
- primary descriptive analyses and inference criteria;
- missing-data handling; or
- non-causal interpretation.

The updated registered response fields are 344-47 and 344-86. The current approved response therefore supplements the earlier original-versus-2026-10-06 revision history; it does not erase or rewrite those historical versions.

## Current prospective timing contract

The currently approved registered response retains the following timing rules:

1. The prospective window begins only after the first eligible new software-release event following registration.
2. Observations are made at preregistered observation time points following eligible release events.
3. The observation window ends after the final preregistered follow-up point has been attempted for all ten objects across all six infrastructure layers.
4. Query failures, rate limits, missing records, and unresolved states remain outcomes and do not by themselves extend the observation window.
5. No additional objects, layers, or follow-up observations are added in response to interim results; any extension or exploratory check is documented separately.

The approved response does not enumerate a numerical offset table or a numbered list of timepoint offsets. That limitation must not be turned into a claim that the formal prospective OSF contract is absent or merely diagnostic. Nor may an operational offset be invented or backdated.

## Authority and repository mapping

Authority order for Study 1:

1. Original OSF 5b329 registration and its time-stamped original response.
2. The approved 2026-10-06 Schema Response revision, retained as a distinct historical version.
3. The current approved 2026-11-18 Schema Response `6afdcc3a7fb0a89b0e3dd7e4`.
4. Timestamped repository-side operational specifications and execution records, which implement but do not rewrite the OSF contract.

Repository owners:

- `contract/`: frozen contract mapping and version authority;
- `corpus/`: fixed RS01–RS10 manifest;
- `schema/`: six-layer, seven-platform, state, and counting rules;
- `schedule/`: operational schedule declarations and their provenance;
- `monitoring/`: diagnostic and pre-eligibility records;
- `observations/raw/` and `observations/derived/`: eligible prospective records and traceable derivations;
- `evidence/` and `provenance/`: retained source evidence and lineage.

A monitoring record remains a monitoring record unless it independently satisfies the registered eligibility and observation rules. This evidence classification does not downgrade the formal status of OSF 5b329.

## Scope of this crosswalk

This document records the current approved OSF authority and its repository implications. It does not write to OSF, alter the frozen registration, change the observation schedule, create a new observation, or reinterpret external-provider failures as global absence.