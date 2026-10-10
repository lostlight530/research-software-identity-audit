# 2026-10-10 / 03 — OpenAlex author Works aggregation and WorkflowHub DOI reconciliation

**Record class:** `diagnostic_monitoring` / supplementary discovery-and-author-identity comparison; **not** an eligible OSF prospective observation. User-reported trigger: "作品聚合了"; reviewer interpretation is limited to directly checked public endpoints. **Not** a new software release or an expansion from RS01–RS10 to eleven objects.

**Independent public extraction interval:** `2026-10-10T15:32:12Z–15:34:52Z` (Asia/Shanghai: 23:32:12–23:34:52). The canonical 18-row work-list extraction was `15:34:31.408Z–15:34:52.266Z`. These are **outer tool execution windows**, not original per-request HTTP completion timestamps, server `Date` headers, or evidence of indexing-event time. The public extraction tool returned parsed JSON, **not raw byte-preserving HTTP evidence**.

## Actually executed

1. Public OpenAlex [author-filtered Works API](https://api.openalex.org/works?filter=author.id:A5151904252&per-page=50&select=id,doi,display_name,type,publication_date,updated_date) returned `meta.count=18` and **18/18 returned rows**. Each had a distinct Work ID and DOI. An independent non-`select` query and a `corpus=all` query each also returned **18**. Its normalized query identified `authorships.author.id:A5151904252`.
2. Independently queried the **six** returned WorkflowHub Work IDs via individual OpenAlex `/works/W...` endpoints. Each response had the expected DOI and an `authorships.author.id=A5151904252` relation.
3. OpenAlex [author profile](https://api.openalex.org/authors/A5151904252), queried in two forms during this review, returned **incompatible nested `works_count` values**: field-selected `16`, `updated_date=2026-10-09T12:31:04`; unselected/full `30`, `updated_date=2026-10-01T12:39:15`. These are separate current response observations, **not** the author-filtered Works query count and not evidence that 12 works were deleted.
4. DataCite separately returned the DOIs `10.48546/workflowhub.workflow.2332.4` and `10.48546/workflowhub.workflow.2334.4`, each `resourceTypeGeneral=Workflow` with creator ORCID `0009-0001-3617-0832`. The exact OpenAlex DOI-filtered query for these two **v4** records returned `meta.count=0` in this access window. This is **query-level not observed**, not a global absence or proof of permanent non-indexing.
5. The public [ORCID Works endpoint](https://pub.orcid.org/v3.0/0009-0001-3617-0832/works) was readable only as flattened extracted text in this review, and did expose WorkflowHub DOI suffixes including `2332.4` and `2334.4`. Because its structural JSON/XML grouping was not retained by this extraction, the reviewer **did not** calculate a new exact ORCID group or summary count.

## Author-filtered Work identity inventory

The machine-readable 18-row derived field inventory is [openalex-author-works.csv](openalex-author-works.csv), retaining Work ID, DOI, title as returned, type, dated Work `updated_date`, classification, source URL and the outer read window.

| DOI identity class | OpenAlex Work rows observed | What this measures |
| --- | ---: | --- |
| Ten fixed-corpus Zenodo **concept** DOIs | 10 | One DOI-level author Work relation per fixed software family; not 30 release-version Works |
| Independent audit-control Zenodo **concept** DOI | 1 | Public control-software Work relation, **not RS11** |
| Frozen OSF preregistration DOI | 1 | Separate research-plan object, **not software sample** |
| Two WorkflowHub workflow identifiers, versions 1–3 each | 6 | **Six version DOI Work rows**, not six independent workflow families |
| **Total** | **18** | Author-filtered OpenAlex returned Works for this query, not a globally authoritative author `works_count` or research impact measure |

### Six WorkflowHub version-specific mappings verified

| Workflow lineage | Version DOI suffix | OpenAlex Work ID |
| --- | --- | --- |
| `welcome-to-github`, WorkflowHub workflow 2332 | `2332.1` | `W7220969795` |
| `welcome-to-github`, workflow 2332 | `2332.2` | `W7220962531` |
| `welcome-to-github`, workflow 2332 | `2332.3` | `W7221188636` |
| `zero-entropy-lab`, workflow 2334 | `2334.1` | `W7220948089` |
| `zero-entropy-lab`, workflow 2334 | `2334.2` | `W7220966944` |
| `zero-entropy-lab`, workflow 2334 | `2334.3` | `W7221127912` |

The `updated_date` on five of these Works is `2026-10-10T09:11:00.788812`; one is `2026-10-09T09:14:12.587421`. **Neither is a verified first-indexing timestamp.** Their appearance in the current OpenAlex list reconciles earlier dated WorkflowHub DOI OpenAlex 404 results **as a later successful observation**, without rewriting those actual earlier failed requests or attributing an exact transition time.

## Important incongruities / unverified interpretations

- **`PROFILE_VS_QUERY_COUNT_DIVERGENCE`:** exact filtered Works query `18`, selected author response `16`, full author response `30`; queries exposed different `updated_date` values. Do not simply select the largest profile count or infer object disappearance. OpenAlex's published [counting guidance](https://help.openalex.org/how-to/counting/) documents precomputed author counts and corpus/query-semantic differences as possible causes, but this particular mismatch's actual cause is **UNKNOWN**.
- **`VERSION_DISCOVERY_PARTIAL`:** DataCite returned two public, creator-ORCID-linked WorkflowHub v4 DOI metadata objects, while OpenAlex's bounded author list `18` and DOI-filtered v4 query `0` did **not** show those exact DOI Work records. This is an **observable cross-platform representational difference at query time**, not proof that Zenodo DOI concept/version aggregation or ORCID grouping operates identically.
- **`ORCID_GROUPING_NOT_RECONSTRUCTED`:** DOI strings visible in flattened ORCID Works extraction do not establish a new exact ORCID work-group or summary count. Preserve original ORCID source groups from independently retained structured evidence instead of inventing one here.
- **`NO_CAUSAL_CHAIN`:** the existence of a WorkflowHub DOI, DataCite registry metadata, ORCID textual association and OpenAlex author-work relation cannot by itself establish the platform-to-platform ingestion route, internal lag, visitor identity, independent reproducibility or adoption.
- **`PROSPECTIVE_DATASET_MEMBER=false`:** workflow registry versions and author-indexed Works are supplementary monitoring. No eligible post-OSF RS01–RS10 GitHub release is established here, no operational prospective schedule is silently created, and the six-layer/60-unit analytical contract remains intact.

**Result:** `AUTHOR_WORK_AGGREGATION_CONFIRMED_WITH_CROSS_PLATFORM_GAPS`. Relevant current work-to-author associations **are observable**; full synchronization across all registry versions and consistent profile counts remain **UNRESOLVED**.

**Evidence limit:** this second-party public field extraction and its CSV are *not a raw original-response archive*, exact event/ingestion provenance, completed endpoint census for every service, or a re-execution of local retained-evidence checkers. If an exact first-seen or propagation-latency claim is later needed, it requires a true earlier negative observation of the **same DOI/query contract**, a later contemporaneous positive capture and clearly bounded `first_seen` language—not the Work `updated_date`.

**Retest when:** an independently retained structured ORCID Works response is available, OpenAlex author count/list representations converge or change, or the two workflow v4 DOIs become observable in OpenAlex. Do not treat an inaccessible endpoint or 404 as globally nonexistent.
