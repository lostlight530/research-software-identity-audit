# Manuscript series: Research Software Identity, Propagation, and Governance

**Revision date:** 2026-11-19  
**Status:** Three integrated working manuscript revisions; author review and source-level final verification remain required  
**Series scope:** Research-software identity engineering, cross-infrastructure identity propagation, and trust/evidence governance

## Manuscripts

1. [From Git Tag to Scholarly Record: Engineering an Auditable Identity Pipeline for Research Software](01-identity-pipeline.md) — engineering architecture, field contracts, a worked release-to-identity case, and a reproduction checklist.
2. [Identity Propagation of Research Software Across Open Scholarly Infrastructures](02-identity-propagation-case-study.md) — the historical ten-object case, source-specific results, and the boundary to the preregistered longitudinal design.
3. [Who Guarantees What? Trust Boundaries and Failure Modes in Open Scholarly Infrastructure](03-trust-boundaries-and-governance.md) — guarantee classes, typed failure modes, evidence semantics, and append-oriented correction governance.

## Relationship between the papers

The papers are complementary, not three versions of the same narrative:

- Paper 01 explains how the identity pipeline is configured and made auditable.
- Paper 02 reports what the historical case and later diagnostic records actually show.
- Paper 03 defines which inferences those records can and cannot support.

Paper 01 is primarily an engineering contribution; Paper 02 is an empirical case study and research-design account; Paper 03 is a governance and methods contribution.

## Evidence and authority rules

The manuscript series follows the repository's existing authority order:

1. The frozen OSF registration governs what was preregistered.
2. Dated source evidence and historical baseline records govern claims about what was observed at their own capture times.
3. The live repository governs the current operational implementation and current manuscript sources.
4. Later diagnostics are dated diagnostics; they do not rewrite historical states or become prospective observations.
5. External standards documentation supports descriptions of provider mechanisms, not claims about the current state of this particular cohort.

Non-negotiable distinctions:

- RS01–RS10 remain the fixed research corpus; the control repository is not RS11.
- Six analytical layers and sixty preregistered object-layer units are distinct from seven operational platforms and seventy possible platform checks.
- The October 2026 historical case, the 18 November 2026 diagnostic, and any future prospective dataset are separate evidence regimes.
- HTTP transport, exact identity matching, registration, attribution, preservation, discovery, and scientific acceptance are different claim classes.
- Missing, blocked, rate-limited, partial, unqueried, and unresolved states must not be imputed as success or global absence.
- A source-attempt projection or digest is not the original provider response bytes.
- No causal, population-level, or general provider-latency claim is made.

## Source case and revision basis

These revisions are based on the three supplied 5 October 2026 manuscripts:

- *From Git Tag to Scholarly Record: Engineering the Identity Pipeline for Research Software*
- *Identity Propagation of Research Software Across Open Scholarly Infrastructures: An Auditable Case Study*
- *Who Guarantees What? Trust Boundaries and Failure Modes in Open Scholarly Infrastructure*

They are reconciled against the current `main` research-control repository, including the frozen OSF contract mapping, corpus manifest, platform and counting schemas, schedule, evidence and provenance rules, 18 November 458-request diagnostic, and the 19 November source-specific semantic extractor revision.

## Publication readiness

These are Markdown manuscript sources for review and version control. They are not represented as peer-reviewed, accepted, or published papers. Before external submission, the author should:

- verify every numerical claim against the exact retained evidence package and its declared timestamp;
- verify all references, version-specific standards, and access dates;
- review the AI-use disclosure and make any required venue-specific changes;
- decide target venue, article type, word limit, reference style, and supplementary-material policy;
- approve the final author contribution, conflict-of-interest, funding, and data-availability statements.

The current repository does not contain a completed prospective observation wave. Manuscript wording must not imply otherwise.
