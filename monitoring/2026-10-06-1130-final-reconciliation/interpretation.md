# 11:30 final reconciliation interpretation

## Status

This is the final reconciliation record for the completed initial stage.

It is **not** a prospective fixed-corpus observation. The new release belongs to
the research-control repository, which remains outside RS01-RS10.

## Work-identification count

The project uses a 43-work identification count at this checkpoint:

```text
40 fixed-corpus DOI work records
+ 2 Research Software Identity Audit version records
+ 1 OSF preregistration record
= 43 identified works
```

The Research Software Identity Audit concept DOI is retained as an additional
family identifier. Therefore the physical DOI identifier inventory is 44.

This distinction prevents a family-level concept identifier from being silently
reclassified as another independent work.

## Research Software Identity Audit family

The infrastructure software family now has two archived versions:

```text
concept  10.5281/zenodo.23166490
├─ beta  10.5281/zenodo.23166491
└─ v2026.10-initial-research-runtime
         10.5281/zenodo.23176748
```

The new GitHub Release was published at 02:48:16Z. DataCite registered the
version DOI at 02:48:21Z, a five-second observed interval.

The ORCID DataCite-source current-version record appeared at
02:48:22.765Z, giving a 6.765-second release-to-ORCID first-observation interval
for this propagation path.

## Citation relation

DataCite reports one citation relationship for the current release DOI, pointing
to the OSF preregistration DOI.

This is interpreted as a metadata-defined self-citation/supplement relation
inside the same research lineage. It is **not** counted as an independent
external literature citation.

## ORCID cleanup

Zero-Entropy Lab and Agent Foundations had one redundant DataCite source summary
removed from each work group.

Both groups now match the standard five-source fixed-corpus pattern.

The deleted put-codes return HTTP 404, while the surviving canonical DataCite
put-codes continue to resolve to the correct latest-version and concept DOI
pairs.

The correction changes ORCID source-summary state; it does not change the
underlying software objects, DOI families, or fixed sample size.

## OpenAlex cache divergence

OpenAlex currently exposes two different counts for the same author identity:

- Author profile cached `works_count = 30`;
- live Works query count = 40.

The current infrastructure release DOI and the OSF registration DOI both return
404 from exact OpenAlex DOI lookup at this checkpoint.

Therefore no 43- or 44-work OpenAlex claim is made.

The cached 30 is preserved as a platform-returned state, while the live 40 is
preserved as a separate query result.

## Final initial-stage boundary

At this checkpoint:

```text
10 fixed research-software objects
+ 1 research-control repository
+ 1 preregistration scholarly object
```

remain analytically distinct.

The initial research runtime, baseline, release lineage, ORCID aggregation,
duplicate corrections, and post-release scholarly propagation have now been
reconciled without expanding the preregistered sample.


## OpenAIRE discovery state

The user-supplied OpenAIRE public page reports 11 ORCID-linked software results
and includes the research-control repository beta DOI
`10.5281/zenodo.23166491` as a Zenodo **Research software** record.

This is retained as evidence that the control repository has propagated onto the
OpenAIRE discovery surface.

The reported `11` is an OpenAIRE search/link count, not a new preregistered
sample size. The fixed corpus remains RS01-RS10.

Because the OpenAIRE page could not be independently fetched during this
reconciliation, the exact current page state remains source-reported rather
than independently re-observed.
