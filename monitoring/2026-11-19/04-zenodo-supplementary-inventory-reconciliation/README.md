# 2026-11-19 targeted Zenodo supplementary inventory reconciliation

**Record class:** supplementary diagnostic reconciliation; not a prospective observation  
**Retrieval window:** 2026-11-18T18:36:56.430Z – 2026-11-18T18:36:57.436Z UTC  
**Evidence package:** [04-zenodo-supplementary-inventory-reconciliation](../../../evidence/2026-11-19/04-zenodo-supplementary-inventory-reconciliation/README.md)

## Result

Both previously unkeyed 2026-11-15 supplementary releases now have confirmed canonical Zenodo record IDs and version DOIs:

| Repository | Role | Version | Record ID | Version DOI | Concept DOI | Zenodo | DataCite |
|---|---|---|---:|---|---|---|---|
| research-software-identity-audit | CONTROL_NOT_RS11 | v2026.11-nov15-identity-reconciliation | 24249720 | [10.5281/zenodo.24249720](https://doi.org/10.5281/zenodo.24249720) | [10.5281/zenodo.23166490](https://doi.org/10.5281/zenodo.23166490) | published, latest | findable |
| life-science-ecosystem-lab | SUPPLEMENTARY_NOT_SAMPLE | v0.5.1 | 24249719 | [10.5281/zenodo.24249719](https://doi.org/10.5281/zenodo.24249719) | [10.5281/zenodo.23447088](https://doi.org/10.5281/zenodo.23447088) | published, latest | findable |

Both GitHub release tags were independently found through the GitHub Releases API. Zenodo record identity, DataCite registration identity and GitHub release identity agree on the version labels and parent concept DOI.

## Inventory reconciliation

The previous 67-key inventory is retained unchanged. Two additional supplementary versions are now resolved, producing 69 known version identities in this bounded inventory view: 60 fixed RS01–RS10 versions, 6 CONTROL versions and 3 LSEL versions.

This does not add a research object, alter the six-layer contract, or turn 69 into a preregistered denominator. CONTROL is not RS11; LSEL remains supplementary. The original 458-request capture and the prior `zenodo-supplementary-inventory-gap.csv` remain immutable historical records.

## What this does not resolve

- The 100-view discrepancy in the maintainer-supplied 12-record page counters remains unresolved
- This targeted lookup does not establish global completeness of all Zenodo records
- No original provider response bytes or HTTP status codes were exposed by the retrieval connectors; see the evidence provenance

No OSF write, schedule change, new prospective cell, new Release or new DOI was created by this reconciliation.
