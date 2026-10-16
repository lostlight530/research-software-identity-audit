# Contributing

Contributions are welcome when they improve the study runtime, evidence quality,
reproducibility, validation, documentation, metadata, or developer experience
without changing the frozen research contract by implication.

## Start from the owning surface

Before proposing a change, identify what owns it:

- `contract/` — local mapping and documentation of the frozen preregistration;
- `corpus/` — fixed RS01–RS10 sample manifest;
- `baseline/` — historical/initial baseline and reconciliation records;
- `schedule/` — operational observation scheduling;
- `schema/` — machine-readable research and platform contracts;
- `observations/` — raw and derived study observations;
- `evidence/` and `provenance/` — claim support and traceability;
- `analysis/` — bounded descriptive analysis;
- `scholarly/` — citation, archive, and identifier metadata;
- `templates/` — prospective record templates;
- `tools/` and `.github/` — deterministic validation and repository automation.
- `docs/` and `README.md` — human navigation and documentation-maintenance guidance (see [documentation map](docs/README.md)).

A change in one surface does not automatically authorize changes in another.

## Documentation-only contributions

For link/navigation improvements, prose clarification, maintainer guidance, and non-data documentation hygiene, use the [docs-only guide](docs/README.md#4-docs-only-maintenance-workflow).

- A docs-only change must **not** modify observation or counter data, raw evidence, archived packages, schema/contract files, the fixed corpus, an operational schedule, or executable validation/analysis logic.
- Do not move previously published baseline, monitoring, evidence, or provenance directories to make the repository tree visually tidier. Old evidence locators, Git paths and checksums are part of reproducibility.
- A dated observation or experimental result belongs in its dated owning record, not as an undated repository status or a rewritten source report.
- Check relative links against the branch tree, independently inspect the diff, and distinguish **actually executed** validation from planned/not-executed verification.
- Advisory CI protects repository invariants but does not certify an external API observation or scholarly interpretation.

## Research boundaries

Preserve these separations:

```text
OSF frozen contract != GitHub operational implementation
10 research objects != this research-control repository
6 preregistered layers != 7 operational platforms
historical baseline != prospective dataset
live endpoint != historical proof
raw evidence != derived observation != interpretation
HTTP 404 != global absence
HTTP 429 != absence
checker pass != scientific truth
```

Do not introduce `RS11`.

Do not convert an unresolved, rate-limited, partial, failed, blocked, or
unqueried state into success merely to complete a matrix.

## Historical records and corrections

Historical records are append-oriented.

When a material error is found, prefer an explicit correction,
reconciliation, amendment, or deviation record that preserves:

- the prior assertion;
- the new evidence;
- the reason for change;
- the retrieval timestamp;
- the affected analysis or conclusion.

Do not silently rewrite point-in-time evidence.

## Public data and privacy

Follow `DATA_HANDLING.md`.

Canonical public identifiers such as DOI, ORCID, repository URL, release tag,
SWHID, OpenAlex Work ID, and public record timestamps may be retained when they
are necessary for reproducibility.

Do not commit secrets, private communications, private/expiring access tokens,
IP addresses, unrelated telemetry, or incidental personal information.

## Verification

Run the checks appropriate to the changed surface.

The repository checker is currently advisory by default:

```bash
python tools/check.py --mode advisory
```

Use strict mode only when intentionally testing hard enforcement:

```bash
python tools/check.py --mode strict
```

Report what was actually executed. Do not describe an unrun check as passed.

## Pull requests

Keep pull requests small and reviewable. State:

- the problem and bounded change;
- affected research surfaces;
- evidence or metadata impact;
- checks actually run;
- known limitations or unresolved evidence;
- historical or prospective impact;
- security/privacy impact;
- the smallest practical rollback.

## License and attribution

Repository-owned contributions are submitted under the current `LICENSE`.
Third-party evidence retains its own attribution and licensing.

See `LICENSING.md` for scope details.
