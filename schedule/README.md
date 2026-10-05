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
