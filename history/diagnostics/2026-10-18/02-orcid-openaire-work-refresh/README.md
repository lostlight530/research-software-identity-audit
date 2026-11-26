# 2026-10-18 ORCID–OpenAIRE link refresh — attributed success and bounded identity recheck

**Record type:** supplementary diagnostic account-action reconciliation, **not an OSF prospective observation**. This retains the researcher's 2026-10-18 **confirmed action outcome** without trying to replay restricted ORCID/OpenAIRE account transactions. The *exact time of the clicks* is not preserved; the date is user-reported. The private authenticated response is transcribed in the conversation, **not** reproduced as private raw response bytes in the public repository.

## A. What the user demonstrated

The user's OpenAIRE **My ORCID links** page stated **11 ORCID links** across **3 pages**. The user reported refreshing **all** links through the `Update ORCID work` action. **Only one individually shown success receipt** was provided:

> You have successfully updated work "lostlight530/research-software-identity-audit: Beta— Research Runtime Bootstrap" in your ORCID record!

This is enough to classify the **Beta work** as **USER_CONFIRMED_UPDATE_SUCCESS**, and the other links as **ELEVEN_ACTIONS_USER_REPORTED**, with no invented per-item confirmations. Do not transform a batch action report into eleven independently verified successes.

## B. Same Beta DOI: distinguish source descriptions and clocks

| Evidence | DataCite source | OpenAIRE source |
| --- | --- | --- |
| DOI | [`10.5281/zenodo.23166491`](https://doi.org/10.5281/zenodo.23166491) | **Same DOI**, not a new object |
| Work type in **user's ORCID UI** | **Software** | **Dataset** |
| Added (user's UI) | 2026-10-09 | 2026-10-05 |
| Last modified (user's UI) | 2026-10-09 | **2026-10-18** |
| Exact account transaction timestamp | Not available | Not available |
| Preferred source selection | **Not observed** | **Not observed** |

The archived **Beta release date remains 2026-10-05**; the source-specific ORCID **Last modified** date is **an aggregation metadata update**, not a republishing of Zenodo software. The version is `IsVersionOf` concept DOI [`10.5281/zenodo.23166490`](https://doi.org/10.5281/zenodo.23166490). The control repo stays separate from RS01–RS10.

The OpenAIRE PID search in the user's earlier page listed **two matching research-product representations for the same DOI**, one Software and one Dataset:

- [Software search](https://explore.openaire.eu/search/software?pid=10.5281%2Fzenodo.23166491)
- [Dataset search](https://explore.openaire.eu/search/dataset?pid=10.5281%2Fzenodo.23166491)

The user's later ORCID Work detail displayed the DataCite Software and OpenAIRE Dataset **source-level variants**. This is an identifiable cross-platform **classification distinction**, not two independent DOI/software identities. Neither reclassifies the original Zenodo software upload nor authorizes deleting a source record.

## C. Independent public check and what it cannot prove

The [public ORCID Works endpoint](https://pub.orcid.org/v3.0/0009-0001-3617-0832/works?format=json) was read during reconciliation. It exposed the Beta DOI and references to both **DataCite** and **OpenAIRE** source channels, but the flattened extraction did not establish a separately retrievable **post-click 2026-10-18 OpenAIRE source-specific timestamp**. The authenticated user's 2026-10-18 Last modified field remains explicitly attributed rather than silently claimed as independent public API verification.

The OpenAIRE interface also displayed a last ORCID synchronization notice **2026-08-10** (as supplied by user); this notice and its icon status are a **different service synchronization surface** from today's successful `Update ORCID work` response. This review cannot confirm a fresh OpenAIRE icon or synchronization schedule.

**Observed:** Beta UI success; public DOI/source-channel presence. **User-reported without individual receipt:** all 11 link actions. **Unknown:** each other link's completed server write; green icon refresh; changed preferred-source selection; exact click time.

## D. Contract and privacy

No account-authenticated cookies, user sessions, private URLs, or restricted response payloads are saved. Public ORCID and canonical DOI are legitimate scholarly reproducibility identities. No OSF registration, baseline, historical raw bytes, prospective timepoint, sample IDs, or workflow definitions change from this diagnostic note.

[Machine summary](record.json) · [research-control citation guidance](../../../scholarly/CITATION.md).
