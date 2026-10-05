# Deviations

Append-only ledger for departures from a declared procedure that do not silently redefine the research contract.

No deviations are recorded by the bootstrap commit.

## Entry template

### DEV-YYYYMMDD-NN — Short title

- **Observed:** ISO-8601 timestamp
- **Expected procedure:** what was planned
- **Actual event:** what happened
- **Cause:** known cause or unresolved
- **Affected observations:** IDs/timepoints/layers
- **Handling:** retained, retried, marked failed, partial, etc.
- **Interpretive impact:** none / bounded / material / unresolved
- **Related evidence/PR/commit:** references

A deviation is evidence about execution and should not be hidden merely because it is inconvenient.
