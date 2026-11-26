# October 25 bounded seven-platform public identity recheck

**2026-10-25 Asia/Shanghai · diagnostic monitoring only · partial day, not day-end or prospective study data**

## Frozen research contract and provenance

The [OSF preregistration](../../../contract/preregistration.md) DOI `10.17605/OSF.IO/5B329` governs RS01–RS10, six analytical layers and 60 object-layer units **only at an eligible scheduled observation point**. Seven operational platforms / 70 possible platform checks are not a replacement denominator. The [operational schedule](../../../schedule/README.md) still has no declared concrete offsets. The October 14 checkpoint cohort is a documented post-registration Release candidate, not permission to backdate observations. CONTROL is not RS11; PILOT is separate. **Zero prospective cells added.**

Source attempts were made through GitHub's connected API or a web-content extractor reading official public API URLs. [46 source/attempt rows](source-attempts.csv) preserve exact endpoint shape, platform/scope, tool-client *batch bounds*, result and degraded state. These are **not unmodified origin HTTP bytes**, server Date headers, guaranteed fresh cache bypasses, or per-request clocks. Derived numbers are in [record.json](record.json); family-level arithmetic is in [zenodo-family-rollup.csv](zenodo-family-rollup.csv). The reported times are *retrieval batch* bounds, not release registration or ingestion clocks.

## Current bounded source findings

- **GitHub:** all twelve public Release lists returned fewer than 100 entries, ten fixed repos with four published Releases each, separate control with four and pilot with one (**45 descriptive releases**). The fixed ten latest tags remain `v2026.10-fourteen-day-evidence-checkpoint` (published October 14 UTC). CONTROL latest is `v2026.10-evidence-integrity`. No newer *published Release on these list endpoints* was observed, but this is not an exhaustive Git tag/event census. Preflight `main` was `b363d11c9c0013238817e3e7aaa2866721cd8358`, with no open PR and the previously successful October 24 CI run.
- **Zenodo:** twelve `/versions?size=25` families enumerated **45 versions** (40 fixed; 4 control; 1 pilot). Twelve internally matched version-view/download sums and attached family aggregate fields. Fixed ten: **2,545 non-unique Views**; control: **130**; pilot: **6**; twelve-family description: **2,681 Views / 27 Downloads**. Do **not** sum version-level unique views as unique persons or multiply attached family totals across versions. The October 24 **regular/diagnostic URL 2,681 vs 2,836** discrepancy remains **UNRESOLVED**; a repeated regular URL value cannot prove no growth, fresh origin responses or 155 new visits.
- **DataCite:** the exact ORCID-linked query yielded **76 findable distinct DOI identities**: 56 Software, 19 Workflow, 1 StudyRegistration. An independent DOI detail representation for OSF 5b329 is **findable StudyRegistration**. Neither 76 DOI identities nor 45 version records are additional research sample objects.
- **ORCID:** Works response became flattened text, not parseable group JSON. Today’s work-group/summary totals are **NOT_VERIFIED**; the October 20 17 groups / 89 summaries remain older evidence.
- **Software Heritage:** one separate control-origin visits endpoint hit an **Anubis anti-bot page**. Fixed ten origins were **not rechecked today through this attempt**. Structured preservation status is **BLOCKED**, not evidence of origin absence.
- **OpenAIRE:** ten exact `search/software` queries for the fixed cohort's October 14 checkpoint version DOIs each returned exactly **one typed software result**. Other versions were not recertified.
- **OpenAlex:** author Works-list API returned **32 distinct IDs (12 software, 20 other)**. Three author-profile URL shapes returned conflicting `works_count`: default **30**, minimal `?select=id,works_count,updated_date` **21**, and selected with `cited_by_count` **32**, with different `updated_date` values. This is a newly preserved **query-shape discrepancy**, not verified indexing loss, caching mechanism, or growth.

## OSF and supplementary boundaries

The OSF registration API extractor showed the registration object and its title, `date_created=2026-10-05T14:04:13.825314Z` and `date_modified=2026-10-06T09:49:34.548421Z`. A separate page-reader path returned 403. An extracted registration object and DOI existence do not prove the precise original-to-updated OSF field diff; 403 is not withdrawal. The registration has **not** been edited in this review.

Separately, institution-facing [RSE PR #498](https://github.com/rseng/software/pull/498) remains open/unmerged, [RSD #1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870) is closed (October 16) without evidence of deployed fix, and [RSD #1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871) remains open. They are supplementary surfaces, not extra preregistered platforms or objects.

## Limits, retention and corrections

This is selected-field evidence, not a preserved raw transport archive or an exhaustive 70-check prospective matrix. It creates no Release, DOI, OSF amendment, schedule, baseline rewrite, frozen sample expansion, prospective observation, causal/statistical claim, or inferred historical state. Source uncertainty and blocked states remain recorded. Earlier [October 24 family URL-shape reconciliation](../../2026-10-24/02-morning-infrastructure-and-zenodo-family-rollup/zenodo-query-shape-reconciliation-2026-10-24.md) is an immutable separate earlier diagnostic.
