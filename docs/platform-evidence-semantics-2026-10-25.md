# Seven-platform observable contracts — reviewer decision map (2026-10-25)

**Status:** explanatory implementation/review guidance for the already-registered research, not an OSF amendment, new sampling frame, schedule declaration, tool/API migration, research observation, or additional layer. Read together with [observation assurance](observation-assurance-2026-10-25.md), the [frozen-contract mapping](../contract/preregistration.md), [counting rules](../schema/counting-rules.md), and [concrete platform mapping](../schema/platforms.yaml). Primary sources below describe capabilities, **not** proof of this cohort's current state.

Every entry answers: what exactly can this endpoint establish, what cannot be inferred, and what source-dependent evidence is required for a stronger claim. Endpoint and response vocabulary may evolve; retain query and Accept/API version rather than silently normalizing across historical retrievals.

## Shared decision rule

The study has **six analytical infrastructure layers** and **seven operational platforms**. Positive evidence at one platform cannot be described as confirmed at an unrelated platform. Discovery has **two distinct platform interpretations**, OpenAIRE and OpenAlex, both under one preregistered layer. A supplementary RSD, RRID, RSE, WorkflowHub, HAL, or institutional landing-page check is not an eighth operational platform by implication.

- **API transport outcome:** HTTP 200, 404, 401/403, 429, rate-limit headers, unexpected HTML, timeout, parse failure, pagination/degraded source
- **Observable target:** exact canonical object, family/version, endpoint namespace, source-of-record, record relation and query/search filter
- **Source state:** platform fields as returned for the exact query shape and timestamp, including missing or conflicting fields
- **Interpretation:** bounded claim only for the source contract and object grain, leaving unproven alternatives explicit

A returned 200 on a list endpoint proves **a request succeeded**, not that every expected matching row was returned. A returned 404 on one exact-path request proves at most **not resolved by that endpoint under that query/authorization state**. A source summary, author entity, DOI, archived snapshot, current `main`, or institutional software record can each refer to *different* objects.

## 1 · GitHub — `source_repository`

**Target grain:** repository, commit, tag reference, GitHub Release object, asset, `published_at`, `created_at`, tag target commit, release status.

**Claim supported:** a particular Release record exists with the returned `tag_name`, timestamps and flags; a tag points to a particular Git object as currently observed, if the tag ref/commit is separately queried. A GitHub Release listing is **not a complete tag list**, since plain tags without Releases are excluded.

**Not supported:** that the latest Release API lists every tag, that GitHub `created_at` equals release publication date, that one Repo Release represents all deposited Zenodo versions, that `main` today proves historical tag contents, or that the repository has been read/adopted by humans.

**Positive gate:** object ID → canonical source repository → exact Release/tag/commit → timestamp type/precision → source response/evidence. To assert an *eligible first post-registration study release*, corroborate the OSF-trigger meaning and operational schedule, **not** just existence of a newer control-repo release.

**Negative gate:** 404 at `releases/latest` does **not** establish no tags, repository nonexistence or global lack of qualifying releases. Check the distinct resource kinds and access state where necessary.

**Official reference:** [GitHub REST Releases](https://docs.github.com/en/rest/releases/releases), including list-vs-tags and the `latest` release's selection/clock semantics.

## 2 · Zenodo — `archival_repository`

**Target grain:** concept/family DOI, version DOI, immutable deposited record, deposit metadata and version relations, version-level and attached family usage fields.

**Claim supported:** a given DOI or record resolves and describes a deposited version/archival family at the observed retrieval time, with distinct version IDs. The landing page and API often expose **different statistic fields**; the displayed usage figures are not automatically the API's nonunique totals.

**Not supported:** family DOI = specific Version DOI; family `unique_views` = globally deduplicated people; sum of version-local unique values = a global unique audience; `views` = scientific influence; one record's attached aggregate field necessarily matches another version's attached aggregate field at every read.

**Positive gate:** exact family/version record IDs + DOI relationship + query/pagination form + selected `stats` field name + timestamp + the same entity grain on both sides before computing differences. Show method and preserve mismatching fields (including the historical RS07 difference) without inventing a synchronization cause.

**Negative gate:** record 404, unexpected HTML or counter mismatch = **unresolved under that query path**, not proof a DOI or all versions are absent. An unrelated URL or cache-busting parameter is not evidence of fresh origin semantics.

**Official reference:** [Zenodo statistics definition](https://support.zenodo.org/help/en-gb/4-usage-statistics/15-what-is-a-view-download-data-volume). Zenodo defines unique counts per user/record **within a one-hour window**, not an all-time independent-researcher audience. The [migration note](https://help.zenodo.org/docs/about/whats-changed/) distinguishes landing-page display and API totals.

## 3 · DataCite — `identifier_registration`

**Target grain:** a particular DOI, current registered metadata, registration state, `RelatedIdentifier` edges and their **direction**.

**Claim supported:** the exact DOI has a retrievable registered metadata record with the returned state and relationship attributes.

**Not supported:** a DataCite `findable` DOI is indexed in ORCID/OpenAIRE/OpenAlex; a missing reverse family `HasVersion` invalidates a version's actual `IsVersionOf`; 76 enumerated DOI rows mean 76 separate exact DOI GET attempts; a DOI is an additional study object.

**Positive gate:** preserve exact `doi`, status, resource type, relationship direction/source DOI, request shape/selection/page count and retrieval time. When two relation edges are asymmetric, describe **which side was and was not seen**, not “all DOI lineage is broken”.

**Negative gate:** a DOI registered with DataCite but not found on a Crossref-specific lookup is **not a nonexistent DOI**. No unique scientific quality or provenance signature follows from DOI registration alone.

**Official reference:** [DataCite Versioning](https://support.datacite.org/docs/versioning) explicitly describes `HasVersion` / `IsVersionOf` as relations usable **together or separately**. [DataCite schema history](https://schema.datacite.org/versions.html) records 4.7 in March 2026; persist any applicable API/schema version rather than assuming 4.6 remains the most recent.

## 4 · ORCID — `author_registry`

**Target grain:** researcher ORCID record, Works **group**, individual **source summary/assertion**, external identifier and relationship, assertion `source`, preferred record/display index.

**Claim supported:** a particular ORCID public Works response represents a work group and its source summaries, with identities attributed to the source that added the assertion.

**Not supported:** number of summaries = number of distinct independent Works or research software objects; source organization = external endorsement; ORCID token/account access is implied by public record reading; an absent ORCID Work means a DOI is unregistered elsewhere.

**Positive gate:** parse **structured** group and summary records when available; preserve `put-code`, source (researcher versus approved member), `external-id-type`, `external-id-value`, `external-id-relationship`, and retrievable group shape. A flattened text excerpt cannot establish precise group cardinality.

**Negative gate:** distinguish `SELF`, `VERSION_OF`, `PART_OF` and other relationship roles when interpreting grouping; lack of an item in one group/query does not prove global software absence or failure of upstream registration.

**Official references:** [ORCID grouping rules](https://info.orcid.org/ufaqs/how-are-items-grouped-together-in-an-orcid-record/) and [source-of-assertion documentation](https://info.orcid.org/documentation/integration-and-api-faq/).

## 5 · Software Heritage — `preservation_archive`

**Target grain:** software origin URL, crawl/visit event, visit status, snapshot, branch/ref, revision, directory/content identifiers (SWHIDs).

**Claim supported:** a specific preserved snapshot/ref/revision/directory is available when directly returned or resolvable in the preservation archive.

**Not supported:** a successful origin lookup = latest GitHub release preserved; a visit proves every requested tag/directory was saved; an Anubis/HTML response or 404 proves source disappearance; the current GitHub `main` corresponds to a historical SWH snapshot.

**Positive gate:** origin URL → visit time/status → snapshot identifier → relevant ref/tag → revision/tree/directory SWHID, preserving partial results if any join is missing. Report chain depth and what has actually been verified.

**Negative gate:** classify origin-unresolved, visit-missing, missing branch in a snapshot, API/transport-blocked and directory-unresolvable **separately**. A positive preservation conclusion is *content-specific*, not a blanket platform claim.

**Official reference:** [Software Heritage FAQ / APIs](https://www.softwareheritage.org/software-heritage-faq/) describes origin visits and snapshot relationships. [Software Heritage archive implementation](https://docs.softwareheritage.org/_modules/swh/web/utils/archive.html) documents limits on retrieved snapshot branches, so partial listings must not be presumed exhaustive.

## 6 · OpenAIRE — `discovery_graph`

**Target grain:** an exact research-product DOI query, returned software/publication/other product record, matched source identifiers, query filter, page and API version.

**Claim supported:** the OpenAIRE Graph returned a matching representation under the queried parameters at the capture window.

**Not supported:** OpenAIRE and OpenAlex are interchangeable; a DOI result proves ORCID association or actual transfer path; an exact query with no match proves permanent lack of all discoverability.

**Positive gate:** exact API version/endpoint + DOI filter + response type + match fields + pagination boundaries + retrieval clock. A concept DOI and a version DOI may have distinct coverage; they must be queried separately for a claim about each.

**Negative gate:** distinguish 0 matches for exact DOI, pagination truncation, API version mismatch, blocked query and an unexpectedly typed result. No inferred internal ingestion timestamp.

**Official reference:** [OpenAIRE Graph API](https://graph.openaire.eu/docs/apis/graph-api/) documents distinct parameter/filter forms, pagination and API variants; the [parameter-based API guide](https://graph.openaire.eu/docs/apis/graph-api/overview/) documents v3 routes. Historical queries must retain their own exact version/shape.

## 7 · OpenAlex — `discovery_graph`

**Target grain:** OpenAlex Author entity, author-profile `works_count`, filtered Works list `meta.count`, per-Work ID, DOI/locations, type, source update dates, query `select` shape.

**Claim supported:** the OpenAlex API returned a specific Work ID or set of matches in a specified query representation. Exact DOI matching is stronger for a particular DOI than title similarity alone.

**Not supported:** one profile `works_count` equals a simultaneously exhaustive author-filtered list; 21/30/32 field-response variations indicate actual work deletion or new indexing without extra evidence; a work's `cited_by_count` proves external independent impact; `OpenAlex Work` is an additional RS software object.

**Positive gate:** retain query path, filters, `select` set, `per_page`/pagination, `meta.count`, individual IDs/DOIs, entity update timestamps and capture clock. Compare only genuinely like-for-like query representations and distinguish profile, list, and individual Work responses.

**Negative gate:** a zero `meta.count`, a failed exact DOI request, or a changed author profile query is **query-scoped**, not permanent global absence. Treat profile/list inconsistencies as explicit **UNRESOLVED_QUERY_SHAPE_CONFLICT** until reproduced and explained.

**Official references:** [OpenAlex API reference](https://help.openalex.org/api/), [filters](https://help.openalex.org/api/filtering/), and [Works data model](https://help.openalex.org/data/works/) distinguish entity, list/query semantics and PID versus fuzzy matching.

---

## When the two discovery systems disagree

Keep two independent observation rows keyed by:

`(object_id, discovery_graph, operational_platform, exact_query, retrieval_window)`

For a **positive presence** claim at the layer level, cite the supporting named platform(s); do not imply that *both* independently saw the same object. For a **negative or coverage-completeness** claim, do **not** collapse an unknown, blocked, unqueried or incomplete platform state into `absent`. Either retain a vector of OpenAIRE/OpenAlex statuses or explicitly state the limited decision rule for that particular analysis. This is a **review principle**, not a newly preregistered numerical aggregation rule.

An observed order across source → archive → PID → registry → preservation → discovery is an order of **first observed evidence**, not proof of a single causal linear propagation route or backend internals.

## Cross-platform claim checklist (manual review)

A claim should be rejected or narrowed when any of the following is not established: canonical RS identity, source object grain, exact endpoint/query form, status versus returned fields, source clock semantics, caller/collector provenance, appropriate evidence type, pagination/completeness, like-for-like comparison, and correct analytical denominators.

For uncertain access and semantic differences prefer `UNKNOWN`, `BLOCKED`, `DEGRADED`, `PARTIAL`, `UNRESOLVED`, `NO_CONCLUSION` and a bounded retest condition over fabricated zero or global success. This is about **epistemic limits** of observation, not an invented scoring model.

**Out of scope:** no migration of historical source records, no new seven-platform scheduled run, no retroactive platform-version normalization, no OSF editing, no addition of inferential methods or extra research samples.
