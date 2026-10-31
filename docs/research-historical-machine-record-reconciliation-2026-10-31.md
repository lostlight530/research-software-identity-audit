# Retrospective machine-index reconciliation — 2026-10-31

**Correction class:** additive, explicitly retrospective *derived metadata index*, **not** a restored original raw observation, prospective dataset, recaptured October 29/30 origin response, or modification of OSF registration

The October 31 post-merge PR #77 [path check](https://github.com/lostlight530/research-software-identity-audit/actions/runs/41176771769) correctly reported two existing historical monitoring event directories without the expected `record.yaml` or `record.json`. A successful advisory workflow conclusion did **not** make those checker errors disappear.

| Previously missing machine index | Existing source material | Repair |
| --- | --- | --- |
| [October 29 independent GitHub Release-gate check](../monitoring/2026-10-29/02-independent-release-gate-recheck/README.md) | Original README and [11-row selected field ledger](../monitoring/2026-10-29/02-independent-release-gate-recheck/source-ledger.csv) | New [record.json](../monitoring/2026-10-29/02-independent-release-gate-recheck/record.json) |
| [October 30 OSF Schema Response version comparison](../monitoring/2026-10-30/01-osf-schema-response-version-reconciliation/README.md) | Original README and [29-field structured difference](../monitoring/2026-10-30/01-osf-schema-response-version-reconciliation/field-diff.json) | New [record.json](../monitoring/2026-10-30/01-osf-schema-response-version-reconciliation/record.json) |

Both new machine records carry their **true later assembly timestamp**, exact original source paths, earlier *tool-envelope* clocks and source-scope limits. `historical_source_record_existed=false` and `raw_origin_http_bytes_recovered=false` prevent confusing retrospective indexing with an authenticated historical raw response.

The October 29 record **only reindexes** the 11 GitHub Release-list fields already present in the historical CSV. The October 30 record **only reindexes** the two OSF Schema Response IDs and 29/28/1 field comparison already present in the historical JSON. No uncaptured old fields, per-origin clocks, absent DOI responses or inferred visits are supplied.

These additions do not rewrite any original README, CSV, field diff, original OSF registration, release, DOI, baseline, research sample, schema, schedule or prospective observation. Their purpose is to give an explicit machine-readable derived navigation surface while preserving a visible missing-original-source distinction. The repository path checker may now pass structurally; **that would not validate scientific conclusions or create historical raw evidence**.

**Validation scope:** path/ownership, existing source references, no prospective cells; only an actual runner outcome may be reported as checker PASS.
