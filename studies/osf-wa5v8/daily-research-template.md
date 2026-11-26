# Study 1 daily research template — Project wa5v8 / Registration 5b329

> **Template only.** This file is not an observation, scheduled timepoint, release event, schedule declaration, or prospective dataset record. A calendar day does not automatically create a research unit.

## 1. Study identity and authority

- **OSF Project:** [wa5v8](https://osf.io/wa5v8/) · Project DOI [10.17605/OSF.IO/WA5V8](https://doi.org/10.17605/OSF.IO/WA5V8)
- **OSF Study Registration:** [5b329](https://osf.io/5b329/) · Registration DOI [10.17605/OSF.IO/5B329](https://doi.org/10.17605/OSF.IO/5B329)
- **Current approved authority:** Schema Response [6afdcc3a7fb0a89b0e3dd7e4](https://api.osf.io/v2/schema_responses/6afdcc3a7fb0a89b0e3dd7e4/)
- **Frozen contract:** [contract/preregistration.md](../../contract/preregistration.md)
- **Schedule authority and current representation:** [schedule/README.md](../../schedule/README.md)
- **Fixed corpus:** [corpus/object-manifest.csv](../../corpus/object-manifest.csv)
- **Layer / platform mapping:** [schema/infrastructure-layers.yaml](../../schema/infrastructure-layers.yaml) and [schema/platforms.yaml](../../schema/platforms.yaml)
- **Object-pair register:** [2026-11-26 OSF Project–Registration crosswalk](../osf-object-pairing-crosswalk-2026-11-26.md)

## 2. Daily gate — monitoring is not a prospective timepoint

The daily eligibility check is a **trigger gate**, not a 60-unit prospective observation. Do not collect or label a prospective timepoint merely because a day folder exists.

1. Read fresh main, open PRs, the frozen contract, the current approved Schema Response, the operational schedule declaration (if any), the fixed corpus, schemas, and latest relevant records.
2. Check whether the **first eligible new release event after registration** has been verified for any object in the fixed RS01–RS10 corpus. Preserve the exact repository/object ID, release tag or version, source timestamp, and evidence locator.
3. If no eligible event is verified, or the source evidence is insufficient, record the gate result as monitoring / unresolved only. Create **zero** prospective cells.
4. If an eligible release event is verified, check for a concrete follow-up schedule declaration committed **before** the observations it governs.
5. The current approved OSF response requires predefined/scheduled follow-up points but does not enumerate numerical offsets. The repository schedule currently records that no numerical offset table is declared. **Do not invent offsets or create a timepoint until an applicable schedule declaration exists.**
6. Only after both the eligible release trigger and a predeclared applicable schedule point are established may a prospective observation batch be initiated. Commit the precollection declaration before the first source request.

The gate labels below are workflow bookkeeping for this template; they do not add values to the preregistered observation-state taxonomy.

## 3. Fixed scope and denominators

- Fixed research objects: **RS01–RS10 (10)**
- Preregistered infrastructure layers: **6**
- Analytical denominator: **10 × 6 = 60 object-layer units per eligible scheduled timepoint**
- Operational platforms: **7**, allowing up to **10 × 7 = 70 platform checks**; this does not replace the 60-unit denominator
- Preserve every planned unit, including failed, partial, rate-limited, missing, and unresolved states
- OpenAIRE and OpenAlex are separate platforms mapped to the single discovery_graph layer

Use the existing [observation batch template](../../templates/observation-batch.template.yaml), [observation record template](../../templates/observation-record.template.json), and [evidence record template](../../templates/evidence-record.template.yaml). Do not create a second schema in this Markdown file.

## 4. Daily entry — copy only after the review

### Run identity

- Reporting date:
- Reporting timezone:
- Reviewer / collector:
- Precollection declaration commit (if acquisition is eligible):
- Actual source acquisition window (UTC):
- Asia/Shanghai equivalent:
- Daily record path:

### Eligibility gate

- First eligible post-registration fixed-corpus release event: VERIFIED / NOT_VERIFIED / UNRESOLVED
- Trigger object ID (RS01–RS10):
- Exact release tag / version:
- Source release timestamp and timezone:
- Trigger evidence reference:
- Schedule declaration path / commit:
- Schedule declaration predates acquisition: YES / NO / UNKNOWN
- Scheduled follow-up point ID (if applicable):
- Prospective batch initiated: YES / NO
- If not initiated, reason:

### Acquisition accounting — fill only when a scheduled point is eligible

- Planned object-layer units: 60
- Units attempted:
- Units with complete retrieval:
- Units partial:
- Units failed:
- Units unresolved:
- Omitted units and reasons:
- Platform checks attempted (separate 70-check operational grain):
- Source evidence index:
- Provenance / derived-output references:

### Daily disposition

Choose a bounded description; do not force a positive result:

- MONITORING_ONLY_NO_ELIGIBLE_EVENT_VERIFIED
- ELIGIBLE_EVENT_FOUND_SCHEDULE_NOT_DECLARED
- SCHEDULED_POINT_ATTEMPTED
- PARTIAL_OR_UNRESOLVED
- NO_CONCLUSION

### Corrections, deviations, and next review

- New correction event(s), if any:
- Deviation reference(s), if any:
- Unresolved questions:
- Next review trigger:
- Notes:

## 5. Interpretation and closure rules

- A successful source request is not proof of a verified cross-platform relationship.
- A missing, failed, rate-limited, or partial response is not global absence.
- A live read cannot be backdated into a historical baseline.
- A monitoring package is not promoted to a prospective observation by later schedule clarification.
- Keep raw evidence, normalized records, derived analysis, and interpretation separately traceable.
- Use descriptive counts and the preregistered analyses only; do not add unregistered inferential or causal models.
- Query failures do not automatically extend the preregistered observation window.

**Small and Stable · Contract before observation · Evidence before interpretation**
