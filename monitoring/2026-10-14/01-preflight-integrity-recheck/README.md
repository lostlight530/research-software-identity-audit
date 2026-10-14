# Preflight identity and release-gate recheck — 2026-10-14

**Scope:** diagnostic preflight/readiness only, performed on **2026-10-14 Asia/Shanghai**. The frozen research corpus is RS01–RS10; `research-software-identity-audit` is a separate control/runtime repository, **not RS11**. This is not a preregistered observation timepoint or a prospective dataset entry.

**Initial GitHub main:** [`b158a00856a15e91bd2799f0d2ff2c37ba9f32df`](https://github.com/lostlight530/research-software-identity-audit/commit/b158a00856a15e91bd2799f0d2ff2c37ba9f32df), with **0 open PRs** and most recent configured [main advisory CI successful](https://github.com/lostlight530/research-software-identity-audit/actions/runs/38392790556). Repository contract, baseline, schedule and fixed manifest were read from that commit. No new eligible fixed-corpus release was established.

## Evidence identity and retrieval bounds

- [Source-attempt ledger](source-attempts.csv) records **37 rows** comprising 20 GitHub Release/tag checks, 7 Zenodo direct/enumeration checks, 2 DataCite DOI checks, 3 OpenAlex query shapes, 2 OSF presentation/extractor reads, and 3 **tool-level blocked** targeted checks. These rows describe attempts, not independent study observations, not 37 HTTP 200 responses, and not 37 platform checks in the prospective denominator
- GitHub ten-repository Release and tag-ref GET batch: **2026-10-14T07:14:19.236Z–2026-10-14T07:14:21.265Z** (outer concurrent tool window)
- DataCite, OpenAlex and first Zenodo version-list/bare-document extraction: **2026-10-14T07:13:08.171Z–2026-10-14T07:13:09.719Z** and the more detailed bare Zenodo/OSF extraction **2026-10-14T07:13:36.895Z–2026-10-14T07:13:38.127Z**
- Zenodo three-version nonce recheck: **2026-10-14T07:15:07.678Z–2026-10-14T07:15:12.457Z**
- OpenAIRE, ORCID and Software Heritage follow-up attempt: **2026-10-14T07:15:35.781Z–2026-10-14T07:15:36.672Z**, **blocked by extractor service rate limit**, not target API failure
- GitHub source responses were handled through the authorized GitHub connector; external responses are extractor-produced field/text excerpts. **No raw HTTP response bytes, original headers, per-response server Date, SHA-256 or validated cache bypass** were retained. These are outer tool-call windows rather than exact provider response completion timestamps

## 1. Fixed RS01–RS10 release eligibility gate — former tag-check gap reduced

All ten fixed repositories returned **three current public Release entries** and **three current Git tag refs** per repository. The observed Git tags are `v2026.09-open-research-baseline`, `v2026.09-natural-month-close`, `v2026.10-open-research-production-framework`. All Release lists name `v2026.10-open-research-production-framework` as the newest public release, dated **2026-10-04 UTC**. All current tag refs target commit objects.

Yesterday's [2026-10-13 gate](../../2026-10-13/02-fixed-corpus-release-gate/README.md) retained ten `CONNECTOR_INVALID_ARGUMENT` failures for `/tags?per_page=100`. **Today a distinct supported GET `/git/matching-refs/tags` succeeded for all ten**. This does **not** rewrite yesterday's failed attempts or prove that no tag ever existed and was deleted, or establish historical tag-ref creation timestamps.

**Today’s bounded conclusion:** no post-registration **public GitHub Release or currently visible additional tag ref** was found in these ten repositories. GitHub commits, deleted/renamed refs, unlisted release-event types and other contract eligibility details are not exhaustively ruled out. **Prospective start is not established**.

## 2. Control Zenodo counter consistency — raw-field conflicts kept

The direct **bare** extract of `23166491 / 23176748 / 23284570` returned attached family views **91 / 51 / 74**, version views **21 / 32 / 0**, and attached family downloads **3 / 0 / 3**. As with Oct 13, these responses are **not a mutually consistent family snapshot**.

The later separate nonce-labeled three-version extraction returned version views **21 / 55 / 18**, sum **94**, version downloads **0 / 3 / 0**, sum **3**, with **attached family views=94, family unique_views=90 and family downloads=3** on each version response. A version-list endpoint excerpt was also obtained, but the full native response and exhaustive array membership were **not independently parsed** in this pass. This is a **later cross-version match after earlier inconsistent fields**, not proof of a specific cache/synchronization mechanism. Nonce query parameters do not guarantee cache freshness.

Compared with the **separate Oct 13 later matched** `91 views / 87 unique_views / 3 downloads` snapshot, the comparable family fields changed by **+3 views / +3 unique-view counter units / 0 downloads**. This is not a headcount of newly identified people or a causal traffic explanation.

## 3. Other bounded platform checks and unresolved distinctions

| Surface | October 14 evidence | Interpretation |
| --- | --- | --- |
| **DataCite** | Control Concept DOI `10.5281/zenodo.23166490` still exposes **2** `HasVersion` identifiers (`23166491`, `23176748`); latest version DOI `23284570` exposes `IsVersionOf` the Concept | Observable reverse-link asymmetry; metadata update mechanism and whether automatic synchronization is required are **UNKNOWN**. Do not call the newer DOI nonexistent |
| **OpenAlex** | Author Works query `meta.count=26`; field-selected author `works_count=24`, `updated_date=2026-10-12T12:34:37`; full-profile author `works_count=30`, `updated_date=2026-10-01T12:39:15` | Query and profile response surfaces remain different; not 26 independent software families, not proven ingestion latency, no invented explanation |
| **OSF Registration** | Public [Overview](https://osf.io/5b329/overview) shows an **update banner dated 2026-10-06**. Its displayed justification says links/descriptions for supporting research materials were added and claims no change to preregistered study design, hypotheses, sampling or analysis plan | **Current page display and submitter's update statement**, not a byte-level before/after diff or proof that every `Updated` field was unchanged. The original frozen object and subsequent transparent update must remain distinguishable |
| **OSF API** | Public extractor returned documentation-style Registration Detail rather than a trusted parsed native response plus a verified revision history | Keep complete native API JSON / exact version-diff state **NOT_VERIFIED** |
| **OpenAIRE, ORCID, Software Heritage** | Targeted follow-up requests were blocked by the external extraction service's free-tier rate limit | **TOOL_BLOCKED / NOT_RECHECKED**; do not replace Oct 13 observations, infer API HTTP response, infer absence, or log 0 |

The OSF page update date narrows the [Oct 8 OSF Overview crosswalk](../../../contract/osf-overview-crosswalk-2026-10-08.md)'s previously unresolved chronology, **but it does not supply an original-versus-updated field diff**. The October 8 crosswalk is kept intact as a dated statement of then-available evidence; this record adds the later verification, not a silent rewrite.

## Research governance and preflight closeout

- No edits to [frozen contract](../../../contract/preregistration.md), [manifest](../../../corpus/object-manifest.csv), [baseline](../../../baseline/2026-10-05/manifest.yaml), [schema](../../../schema/counting-rules.md), [schedule](../../../schedule/README.md) or archived release/tag
- Exactly **10 × 6 = 60** preregistered object-layer units per **eligible scheduled timepoint**; **10 × 7 = 70** possible concrete object-platform checks. This diagnostic report contributes **zero** new prospective cells
- No release, tag, DOI, OSF amendment, new analytic model, numerical imputation, inferred propagation latency or constructed start timepoint
- Earlier Oct 13 snapshots/failed attempts remain intact. The source-locator and status ledger reports this review's actual supported checks and unobserved paths
- **Preflight outcome:** `TAG_REFERENCE_GATE_RECHECKED`, `PROSPECTIVE_NOT_STARTED`, `ZENODO_LATER_MATCHED_AFTER_BARE_CONFLICT`, `DATACITE_REVERSE_RELATION_ASYMMETRY`, `OPENALEX_COUNT_SURFACES_DIVERGENT`, `OSF_OCT06_UPDATE_BANNER_VISIBLE`, `OTHER_PLATFORMS_TOOL_BLOCKED`
