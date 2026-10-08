# Operational observation schedule

The frozen OSF registration requires predefined/scheduled observation points but the frozen text export does not enumerate concrete offsets.

This directory is the authoritative repository-side location for operational schedule declarations, not for rewriting the preregistration.

## Rules

1. A schedule declaration must be committed before the observations it governs are interpreted.
2. Every declaration records declaration timestamp and effective scope.
3. Concrete offsets introduced here are operational specifications unless the frozen registration independently supports a stronger claim.
4. Schedule changes do not overwrite history.
5. Substantive procedural changes are also logged in `AMENDMENTS.md`.
6. Deviations from a declared schedule are logged in `DEVIATIONS.md`.
7. Query failure, rate limiting, missing records, or unresolved states do not automatically extend the observation window.

## Current state

No concrete operational offsets are declared by this bootstrap commit.

That is intentional: the repository does not invent a schedule absent from the frozen registration text.

## Supplied OSF Overview alignment (2026-10-08)

The supplied registration Overview says the prospective window starts on the **first eligible new fixed-corpus release after registration**, continues at **predefined** observation points, and stops after the final planned follow-up point is **attempted** across all ten objects and six layers. Access errors or unresolved observations do not automatically extend the window.

This repository still has **no declared concrete offsets or fully specified timepoint list**. The text supplied for comparison provides no such offsets. That remains an operational prerequisite/gap, **not** permission to invent preregistered times, backdate an operational schedule, or promote the 2026-10-06–08 monitoring packages into prospective evidence.

See [OSF Overview crosswalk](../contract/osf-overview-crosswalk-2026-10-08.md). No schedule declaration is created by this note.
