# November 7 diagnostic schema, path index and historical compatibility correction

**Classification:** dated **derived-record / advisory-assurance correction**, not fresh platform retrieval, amendment to OSF 5b329, new eligible release, retrospective baseline replacement, or scheduled prospective observation

**Correction compiled:** `2026-11-07T11:34:55.789Z` UTC. The original diagnostic compilation and external extractor acquisition clocks in the source records are **not changed** by this later correction

## Evidence and defect

The [original November 7 diagnostic PR #99](https://github.com/lostlight530/research-software-identity-audit/pull/99) merged as `d5bddfd5b292f40e6c216e27ca03906fe3571d09`. The source-bound [PR workflow run 42343877684](https://github.com/lostlight530/research-software-identity-audit/actions/runs/42343877684) had an overall `success` result, but its **advisory** `Check dated record paths and ownership` step ran `python -B tools/check_record_paths.py` and exited **1**, reporting **three** actual failures:

1. November 6 machine record's original `osf_contract` key was incorrectly treated as missing by the more recent `contract`-only path guard
2. `monitoring/README.md` lacked the November 7 dated event's navigation entry
3. November 7 newly authored diagnostic machine summary and 34-row surface ledger used field aliases not accepted by the current checker

**Claim correction:** CI workflow `success` must not be interpreted as every advisory command `PASS`. The original GitHub Actions log is retained at the linked run; `continue-on-error` makes the overall workflow result nonblocking

## Exact object identities and correction action

| Artifact | Original Git blob at PR #99 main | Corrective treatment |
| --- | --- | --- |
| `monitoring/2026-11-07/01-periodic-identity-infrastructure-recheck/record.json` | `85b0cf60644b498349b20dcc2695789443b6aba8` | Normalize derived `surface_check` into `supplementary_surfaces`, add explicit non-prospective `contract` structure, preserve original compilation and acquisition provenance, append machine correction history |
| `monitoring/2026-11-07/01-periodic-identity-infrastructure-recheck/surface-access-recheck.csv` | `78a37acabe17d9c92ed211a3b80bcc05b2c2757c` | Map ten column headers to the existing repository `surface_id` / `exact_source_locator` / `access_state` / `tool_receipt_id` contract; **all 34 rows and field values retained exactly**, including six errors, original receipts and recorded acquisition-day labels |
| `monitoring/README.md` | `a3fb689deb8c1d2378b7645faa7b4c0d7869477b` | Add the missing November 7 dated event entry |
| `tools/check_record_paths.py` | `dbde659d402bd89847e7146a191c94efdf5c4d8f` | Permit historical `osf_contract` as a compatible source representation when `contract` is absent; keep the same hard non-prospective predicate |
| `monitoring/2026-11-06/01-periodic-identity-infrastructure-recheck/record.json` | Original retained source | **No edit**: checker compatibility updated instead of silently altering the previous day's source record |

The former `surface_check` fields and CSV header names remain available verbatim in Git history at PR #99 merge commit; the corrected projection is a **later** software-maintenance change. Neither the 34 surface IDs, error types, URLs, extractor receipts, Zenodo counts, release status, nor institutional interactions were remeasured or changed. This is not a replacement of original external HTTP response bytes, which were never fully retained in PR #99

## Repair and verification boundary

- Add synthetic-only tests for the `osf_contract` compatibility path and its rejection of illegal prospective promotion
- Re-run `python -B tools/check_record_paths.py` in CI and **inspect the command's actual log + exit code**, not only the overall advisory workflow conclusion
- Preserve as-is: original OSF Schema Response versions, frozen RS01–RS10 manifest, six-layer / 60-unit contract, baseline, undeclared operational schedule, all historical evidence blobs and released archive identities
- Maintain zero formal prospective observation cells, zero DOI or Release issuance, and no destructive cleanup without path ownership, evidence classification and inbound-reference proof

**Disposition:** `DERIVED_PROJECTION_RECONCILED` · `SOURCE_NOV6_PRESERVED` · `MONITORING_INDEX_REPAIRED` · `CI_ADVISORY_FAILURE_DISCLOSED` · `NO_HISTORICAL_SOURCE_REWRITE` · `PROSPECTIVE_CELLS_0`
