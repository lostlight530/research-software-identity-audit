# 2026-10-07 reconciliation addendum

## Purpose

This addendum clarifies later same-day evidence without rewriting the earlier
2026-10-07 independent-audit source summary. It remains
`pre_eligibility_monitoring` and does not create a preregistered prospective
timepoint.

## OpenAlex cross-snapshot state

The repository already preserves the 2026-10-06 checkpoint as two distinct
OpenAlex observations for author `A5151904252`:

- cached author-profile `works_count = 30`, with profile
  `updated_date = 2026-10-01T12:39:15`;
- live Works query count = `40`.

The supplied 2026-10-07 independent audit then reports:

- author work count = `41`;
- `40` Software works;
- `1` `other` work, the OSF registration;
- all 40 fixed-corpus DOI records matched;
- eight primary topics.

The supported historical chain is therefore:

```text
2026-10-06 cached author profile = 30
2026-10-06 live Works query      = 40
2026-10-07 supplied author count = 41
```

These values must not be collapsed into an unqualified `30 -> 41` delta.
The `30` and `40` values came from different OpenAlex query surfaces at the
same checkpoint. A numerical `+1` from the 2026-10-06 live query to the
2026-10-07 supplied count is retained only as a conditional delta whose strict
comparability depends on query-surface equivalence.

### Eight supplied primary topics

1. Scientific Computing and Data Management
2. Software Engineering Research
3. Multi-Agent Systems and Negotiation
4. Ethics and Social Impacts of AI
5. Security and Verification in Computing
6. Graph Theory and Algorithms
7. Artificial Intelligence Applications
8. Research Data Management Practices

These are preserved as OpenAlex discovery-layer classifications, not as a
researcher-declared ontology or a change to the preregistered infrastructure
layers.

## RRID state clarification

`SCR_029105` is preserved as an assigned RRID for Research Software Identity
Audit. The current state is represented on separate axes:

- identifier assignment: assigned;
- curation: ongoing;
- public indexing: pending;
- platform guidance supplied in the conversation: approximately two business
  days for public indexing;
- earlier resolver observations: one connection failure and one HTTP 403.

The resolver failures remain valid historical request outcomes. They do not
negate the assigned identifier and are not rewritten as evidence that the
resource does not exist.

## Beta creator-display lineage

The OpenAIRE-discovered beta record
`10.5281/zenodo.23166491` retains creator display `lostlight530`, matching the
beta metadata. The later archived release uses the normalized software-author
display `lightlost`.

This is retained as version-scoped metadata evolution, not silently normalized
backward and not classified as an identity error without evidence of incorrect
person aggregation.
