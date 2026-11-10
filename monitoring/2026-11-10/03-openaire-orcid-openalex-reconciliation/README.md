# November 10 user-supplied OpenAIRE, OpenAlex and ORCID-link reconciliation

**Record class:** user-supplied scholarly-interface observation and retrospective diagnostic reconciliation. This is **not** a fresh API capture, not a scheduled OSF prospective timepoint, and not a new research object.

**Source clock:** source-page capture time was not supplied. The text was received in this conversation at approximately **2026-11-10 20:55 Asia/Shanghai**; this is a receipt time, not provider retrieval time. No original screenshots, HTTP response bytes, response headers, or per-request timestamps were supplied.

## OpenAIRE exact-PID result counts supplied by the maintainer

| PID | UI result count | Visible result-type split | November 8 exact API query total |
| --- | ---: | ---: | ---: |
| OSF Registration `10.17605/osf.io/5b329` | 13 | 1 Software / 12 Dataset | 0 |
| CONTROL Zenodo version `10.5281/zenodo.23446162` | 8 | 2 Software / 6 Dataset | 0 |
| Associated OSF Project `10.17605/osf.io/wa5v8` | 10 | 0 Software / 10 Dataset | 0 |
| CONTROL beta version `10.5281/zenodo.23166491` | 4 | 2 Software / 2 Dataset | 1 |

The prior API totals are from the retained November 8 complete diagnostic's `openaire-cross-type-inventory.json`, with HTTP 200 and complete query pagination. The new numbers are user-interface result counts, not API totals or distinct OpenAIRE result-ID counts. The new source capture time is unknown and the interface query contract is not demonstrated to be identical to the November 8 API query. This is therefore a **cross-surface discrepancy / new-match candidate**, not a numeric propagation delta or first-seen timestamp.

The OSF Registration, associated OSF Project, and CONTROL records remain outside RS01–RS10. CONTROL is not RS11.

## OpenAlex author and Work display

The supplied author display reports author `A5151904252`, ORCID `0009-0001-3617-0832`, **33 Works**, **1 citation**, **H-index 1**, and a blank I10-index. Displayed Work types are `other=20`, `software=12`, `preprint=1`. Displayed topic counts are Scientific Computing and Data Management 26; Software Engineering Research 1; Multi-Agent Systems and Negotiation 1; Ethics and Social Impacts of AI 1; Security and Verification in Computing 1. These displayed topic rows sum to 30; the excerpt does not establish that the topic list is exhaustive.

The supplied Work is `W7220380722`, DOI `10.17605/osf.io/5b329`, titled *Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures*. The supplied display classifies it as `preprint` and names source `OSF Preprints` (`S4306401127`). The October 10 retained author-Works CSV recorded the same Work ID and DOI with `work_type=other`. Preserve this as a dated classification/surface discrepancy; current source capture time and endpoint are unknown, so no exact reclassification event is inferred.

The November 8 complete diagnostic recorded 32 enumerated OpenAlex Works. The new **33** is an author-profile display count, not a fresh author-filtered enumeration. A comparable +1 Works delta is therefore **NOT_DERIVABLE** from these two surfaces alone.

## OpenAIRE “My ORCID links” page

The supplied page text reports **15 ORCID links across three pages**, with latest synchronization displayed as **October 10, 2026**. Only pages **2 and 3** were supplied. Those pages display the ten fixed-corpus software families RS01–RS10, each with four DOI identifiers. DOI roles in the CSV are mapped against the frozen October 5 `baseline/2026-10-05/doi-map.csv`; the CSV also preserves the DOI display order.

This is an OpenAIRE “My ORCID links” interface count. It is **not** a reconstructed ORCID Registry group count or Work-summary count, and it does not establish a new ORCID synchronization time. The displayed 15-link count matches the November 8 user-page observation, while both source capture times remain unknown.

## The welcome-to-github version aggregation case

The November 8 retained OpenAIRE DOI-group ledger maps all four baseline DOI identities for RS01 `welcome-to-github`—concept `22790907`, initial version `22790908`, September 30 version `23068145`, and October 4 version `23137203`—to one OpenAIRE software result ID:

`doi_dedup___::99673829fdd66f7c398d1e25300ce755`

Thus the two later version DOIs `23068145` and `23137203` are distinct DOI identifiers represented under the same OpenAIRE result ID in that retained query. This is an aggregation/deduplication observation at the OpenAIRE result layer; it does **not** mean Zenodo or DataCite merged the version records or DOI identities. The supplied “My ORCID links” row independently displays all four DOI values on the RS01 family card.

## Contract and interpretation boundary

- Fixed sample remains **RS01–RS10**; CONTROL is not RS11
- Six preregistered layers × ten objects = **60** analytical units per eligible scheduled timepoint
- Seven operational platforms may yield **70** checks, not 70 preregistered analytical units
- OpenAIRE and OpenAlex remain separate operational platforms within the single `discovery_graph` layer
- OSF Registration, OSF Project, and CONTROL are supplementary scholarly objects, not fixed-corpus sample members
- No OSF write, amendment, schedule change, baseline rewrite, prospective observation, or sample expansion was made

**Disposition:** `USER_SUPPLIED_UI_ONLY` / `OPENAIRE_CROSS_SURFACE_RECONCILIATION_REQUIRED` / `OPENALEX_PROFILE_COUNT_33_NOT_COMPARABLE_TO_NOV8_ENUMERATION_32` / `OPENAIRE_MY_ORCID_LINKS_15` / `RS01_FOUR_DOIS_ONE_OPENAIRE_RESULT_ID` / `NO_PROSPECTIVE_CELLS`.
