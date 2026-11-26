# Independent public-endpoint verification — 2026-10-08

## Retrieval-time boundary

This verification was executed after the conversation supplied the local
08:12–08:26 Asia/Shanghai collection window. The connector used for most
independent reads does not expose one uniform exact retrieval timestamp for
every request. Therefore this file records the execution date and the endpoint
outcomes but does not invent timestamps or backdate them into the source window.

Raw response bytes are not persisted in this package.

## GitHub

Procedure: fetch the exact release page for
`v2026.10-open-research-production-framework` in each fixed repository.

Result: **10/10 readable**. Each page identifies the same tag and an October 4,
2026 publication timestamp. This independently supports the source statement
that no newer fixed-corpus release had replaced the October 4 release at this
check.

## Zenodo

Procedure:

1. fetch the ten current-version human record pages;
2. attempt the corresponding Zenodo REST record endpoints.

Result:

- human current-version pages: **10/10 readable**;
- audit-runtime current-version page: readable;
- file names, sizes, and MD5 checksums were exposed by the human-page extraction;
- REST record fetches returned `CRAWL_UNEXPECTED_CONTENT_TYPE` in the
  independent extractor;
- the human-page extraction did not expose view/download counters.

Therefore the source-reported 775 family views, 733 summed unique views, 70
current-version views, and audit-runtime 47/45 counters are **not independently
promoted** by this updater.

## DataCite

Procedure: exact fetch of all 40 DOI records in
`baseline/2026-10-05/doi-map.csv`.

Result:

- requested: 40
- DOI records readable: 40
- records typed `Software`: 40
- fetch errors: 0

This independently verifies the fixed-corpus 40/40 DataCite identity surface.

## ORCID

Procedure: read the public Works endpoint for
`0009-0001-3617-0832`.

The endpoint was readable. Flattened extraction contained:

- 35 `DataCite` source-label occurrences;
- 11 `OpenAIRE` source-label occurrences;
- current audit-runtime concept/current/beta DOI content.

The prior preserved 2026-10-07 source distribution was DataCite 33 / OpenAIRE
11 / author-added 10. The current endpoint therefore independently supports two
additional DataCite-source appearances relative to that prior source-label
count.

However, the extractor removed the XML group structure. It is not sufficient
for an independent exact reconstruction of **14 work groups / 56 source
summaries**. Those totals remain source-reported.

## Software Heritage

Procedure: fetch the ten directory SWHIDs preserved by the 2026-10-07
`swh-routes.csv`.

Result: **10/10 directory hashes readable**, no fetch errors.

This verifies current readability of those directory objects. It does not
rewrite the historical GitHub-origin Axiom connection failure preserved on
2026-10-07.

## OpenAIRE

Procedure: exact DOI search through the public OpenAIRE API for the ten current
2026-10-04 version DOI records.

Result: **10/10** queries returned exactly one research product; all ten were
typed Software and all ten exposed status `UNDER_CURATION`.

## OpenAlex

### Main author

Author: `A5151904252`, display name `lightlost`.

Independent results:

- cached/profile `works_count = 41`;
- profile `updated_date = 2026-10-06T12:31:48`;
- live Works query `meta.count = 43`.

This independently confirms the source-reported profile/list divergence.

### Fixed corpus

Procedure: exact DOI Work fetch for all 40 fixed-corpus DOI records.

Result:

- requested: 40
- readable: 40
- type Software: 40
- author `A5151904252`: 40

### Audit-runtime and OSF lineage

- concept DOI `10.5281/zenodo.23166490` ->
  `W7220365356`, Software, main author, cited_by_count 0
- current DOI `10.5281/zenodo.23176748` ->
  `W7220737563`, Software, main author, cited_by_count 0
- beta DOI `10.5281/zenodo.23166491` ->
  `W7220470293`, Software, secondary author `A5157531946`,
  cited_by_count 1
- OSF DOI `10.17605/osf.io/5b329` ->
  `W7220380722`, type other, main author, references beta work,
  cited_by_count 0

Within these checked audit-lineage works, the one observed citation into the
beta is accounted for by the OSF-registration -> beta relation. No additional
external citation is observed in this bounded check.

## Research Software Directory

The public audit-runtime software page and
`Agentic Research Constellation` project page were independently readable.
The audit-runtime page explicitly states that it is not an eleventh fixed-corpus
object.

The updater did not reconstruct the source-reported aggregate of 11 public
software records from a complete RSD listing, so that count remains
source-reported.

## Agent cohort

The 432-family cohort was **not independently rerun**.

Reason:

- the local cohort report and cohort input files were on the user's offline
  desktop device;
- the independent Zenodo path did not expose the counters required to recompute
  the ranking.

The four owned rows and ranks 8–11 are retained as source-reported exploratory
evidence, not re-labeled as independently verified.

## Remaining surfaces

- RSE PR #498: repository/URL unavailable to this updater -> `UNRESOLVED`
- HAL: source reported zero public results; no global absence conclusion
- RRID `SCR_029105`: assignment remains preserved; source reported resolver
  HTTP 403; independent public-resolution status remains `UNRESOLVED`

The governing rule remains:

```text
failed / blocked / flattened / unavailable
!=
object absent
```
