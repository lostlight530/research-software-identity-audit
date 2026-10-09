# 2026-10-09 facility recheck

An independently collected diagnostic monitoring record, with the fixed ten objects and the audit runtime kept separate

## Results

Fixed ten: 840 family views, 797 summed family unique views, 7 downloads and 6 unique downloads

DataCite: 40/40 fixed identifiers findable

ORCID: 14 public groups and 56 source summaries

OpenAlex main-author query: 43 works, {'software': 42, 'other': 1}

## Counter reconciliation

The user-supplied concatenated page values match all 11 pairs of unique_views and unique_downloads at the earlier 10:19 capture, including welcome-to-github 101 + 3 versus API total views 105 and total downloads 4

The initial conversation comparison mixed total views with unique views; the metric correction is retained here. The page values are user-supplied, not independently scraped HTML. The later facility capture has its own timestamps

Summed unique counters are not a deduplicated audience across software families. Visitor identity and referral causality were not measured

## Evidence and scope

[Capture summary](capture-summary.json) · [Zenodo counters](zenodo-statistics.csv) · [October 8 delta](zenodo-delta.csv) · [Platform states](platform-states.csv) · [DOI checks](datacite-identifiers.csv) · [Raw evidence](../../../evidence/2026-10-09/01-facility-recheck/README.md)

The 70 possible fixed-object/platform cells remain distinct from the 60 preregistered object/layer units. Request failures remain request outcomes. Other-platform states were not inferred from successful Zenodo requests. The 432-family ranking was not refreshed in this record

GitHub latest-release queries are retained separately from archived-tag lookups. No prospective timepoint is claimed by this unscheduled recheck. Historical October 8 records remain unchanged

## Failed requests

- RS01_openaire: HTTP None, The read operation timed out
- RS02_openaire: HTTP None, The read operation timed out
- RS03_openaire: HTTP None, The read operation timed out
- RS04_openaire: HTTP None, The read operation timed out
- RS05_openaire: HTTP None, The read operation timed out
- RS09_openaire: HTTP None, The read operation timed out
- RS10_openaire: HTTP None, The read operation timed out
- RS08_openaire: HTTP None, The read operation timed out
- RS06_openaire: HTTP None, The read operation timed out
- rrid: HTTP 403, HTTP Error 403: Forbidden
- RS07_openaire: HTTP None, The read operation timed out
- RS01_openaire_extended: HTTP None, <urlopen error [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。>
- workflow_openalex_2332_1: HTTP 404, HTTP Error 404: Not Found
- workflow_openalex_2332_2: HTTP 404, HTTP Error 404: Not Found
- workflow_openalex_2334_1: HTTP 404, HTTP Error 404: Not Found
- workflow_openalex_2334_2: HTTP 404, HTTP Error 404: Not Found

## Other surfaces

GitHub latest queries still return the October 4 tag for all ten fixed objects. SWH deposit release-to-directory chains resolve for 10/10 objects

OpenAlex profile now reports 43 works, matching the main-author live query; the secondary author profile and query both report 1 work

RSD returned 11 records, all 11 published. HAL's exact ORCID search returned 0 records. RRID resolver returned HTTP 403. RSE PR #498 remains open, merged=False

The HAL search does not establish deposit rejection; the RRID resolver failure does not establish identifier deletion. The four known workflow DOI OpenAlex endpoints returned 404; their DataCite responses are retained separately

## Reproduction

The response archive binds requests to timestamps and hashes. The offline verifier recomputes counters from raw responses, checks the canonical corpus, DOI fields, key platform chains and package hashes. Run it locally; no new cloud workflow is added

## Later independent reviewer record

[2026-10-09 evening independent review](independent-review.md) — separately recounts the retained manifest/CSVs, checks ten current GitHub Release lists and latest records plus selected DataCite/OpenAlex public endpoints, and explicitly preserves unexecuted/offline/blocked checks. This does not change the original collection or prospective eligibility.
