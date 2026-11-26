# October 27 bounded seven-platform public recheck

**2026-10-27 (Asia/Shanghai) · diagnostic monitoring, NOT prospective research data**

## Authority and exact scope

The [frozen OSF registration](../../../contract/preregistration.md) remains the research contract for RS01–RS10, six analytical layers and **60 object-layer units per eligible scheduled timepoint**. GitHub, Zenodo, DataCite, ORCID, Software Heritage, OpenAIRE and OpenAlex are seven **operational platforms**, **not** seven preregistered layers. OpenAIRE and OpenAlex both map to `discovery_graph`. CONTROL is the separate audit runtime, not RS11.

The [schedule](../../../schedule/README.md) still has no declared concrete offsets. The ten October 14 fixed-corpus releases are known, but release existence **alone** does not authorize backdated scheduled observations. This package adds **zero prospective cells**, does not amend OSF and does not introduce additional objects, layers, releases, tags or DOI records.

**Bounded tool-call window:** `2026-10-27T15:23:29.374Z` to `2026-10-27T15:23:31.596Z` (UTC, corresponding to 2026-10-27 23:23:29–23:23:31 Asia/Shanghai). The connected GitHub API read 11 repository release lists; a separate live public-content extractor sampled eleven official API URLs. The exact [22-row source/attempt ledger](source-attempts.csv) retains the queried locator, reported fields, access condition and extraction limits. The batch window is a **client-tool envelope, not a server response date or individual-request timestamp**. No unmodified third-party HTTP response bytes, headers or source cache-freshness proof were retained. The [machine record](record.json) preserves selected values and those limits.

## Bounded findings

| Surface | Current return and interpretation |
| --- | --- |
| **GitHub** | All ten fixed repositories return **four published Releases** on `?per_page=100`, latest `v2026.10-fourteen-day-evidence-checkpoint` (2026-10-14 UTC). CONTROL independently returns four published Releases, latest `v2026.10-evidence-integrity` (2026-10-18 UTC). Not a Git tag/event census |
| **Zenodo** | RS01 latest-version endpoint `23365504/versions/latest`: `views=328`, `unique_views=239`, `downloads=6`, `version_views=13`. The **same URL and fields** in the October 26 evening [retained extract](../../../evidence/2026-10-26/02-evening-institutional-recheck/zenodo-family-statistics.csv) yielded `322/233/6/12` respectively; returned-field difference `+6/+6/0/+1`. No inference of distinct users, origin freshness or platform processing mechanism |
| **DataCite** | The **OSF registration DOI**, separately from software DOIs, is `findable` as a `StudyRegistration`, with metadata `updated=2026-10-06T09:49:36Z`. This is not a frozen-revision diff or a new registration |
| **ORCID** | Public Works endpoint was readable through the extractor, but the representation flattened source/group structure; **group and summary counts remain not re-certified** |
| **Software Heritage** | RS01 latest visit returned `full` / visit `4` dated `2026-10-24T15:41:45.044000+00:00`, not a new October 27 capture. The CONTROL origin endpoint returned Anubis anti-bot HTML: **BLOCKED**, not preservation absence |
| **OpenAIRE** | One exact RS01 latest-release DOI `10.5281/zenodo.23365504` returned one software entry, marked `UNDER_CURATION` in the extracted response. Nine other fixed objects were **not queried** on this bounded platform sample |
| **OpenAlex** | Same author, different official query shapes: full profile `works_count=30` (source updated 2026-10-01), minimal selected profile `21` (updated 2026-10-11), selected including `cited_by_count` `32` (updated 2026-10-19); author Works-list meta returns `32`. **UNRESOLVED_QUERY_SHAPE_CONFLICT**, not justified as a temporal transition |
| **OSF Registration** | API extract exposes `public=true`, `reviews_state=accepted`, `date_modified=2026-10-06T09:49:34.548421Z`. No independently preserved OSF original-to-updated wording diff was obtained; the already documented crosswalk ambiguity remains |

## Evidence and interpretation limits

The source extracts are **selected-field projections**, not independently replayable retained origin bytes. Do not call this a full ten-object/seven-platform sweep, a complete all-DOI re-enumeration, a fresh 60-cell timepoint, a longitudinal propagation-latency observation or a full preservation verification. A blocked, stale, failed or flattened representation is not evidence of absence. A source `updated_date` is not the tool retrieval time. GitHub's last published Release is not an exhaustive assertion about tags, drafts or unlisted release events.

Historical October 26 evidence stays immutable. The new response-level differences are append-only diagnostic claims and can be corrected by an attributed later reconciliation.

**Operational policy watch (outside the study dataset):** [OSF's published transition guidance](https://help.osf.io/article/768-osf-projects-transition-registration-questions-and-use-cases) says existing associated OSF Projects become read-only on **2027-02-19**, while Registrations remain independent and continue. This changes neither the Oct 5 research contract nor the present GitHub runtime and does not trigger a project migration or amendment here. Verify applicable project conditions before future operational migration.

## Scope exclusions and verification

- No change to `contract/`, `corpus/`, `schema/`, `baseline/`, `schedule/`, `observations/`, existing `evidence/`, archived releases, DOI identities or substantive analysis
- No API writes to OSF, Zenodo, ORCID, DataCite or discovery platforms
- No identity inference from a 404, zero returned results, anti-bot challenge or unrelated external object
- This file plus the ledger and machine record are new evidence-scoped research **monitoring** material, not executable checks, source-response archives or a new study timepoint
- PR/CI outcome must be checked independently; passing structural verification cannot establish the truth or contemporaneous freshness of external data
