# Tools

## Read-only retained-evidence verification

Run `python tools/check_retained_all.py` to verify the retained October 14–15 diagnostic packages without rewriting their `offline-verification.json` files. The command calls the existing verification functions, prints an aggregate summary and returns a nonzero exit code if any check fails. It makes no network requests and does not create a new observation.

Run `python tools/check.py --mode strict` separately for the research contract. The aggregate command is limited to its listed retained packages; it does not claim verification of every historical package or a live institutional state. The targeted `.gitattributes` rules preserve their sealed LF bytes on Windows checkout. Neither command is added to cloud CI by this update.

This directory contains small validators, collectors, normalizers, and analysis helpers that implement the repository's explicit contracts.

Tooling must not silently change research semantics.

## Contract checker

Run:

```bash
# bootstrap/default: report findings without blocking work
python tools/check.py --mode advisory

# explicit enforcement when you intentionally want a hard gate
python tools/check.py --mode strict
```

The checker is dependency-free and currently verifies:

- the corpus remains exactly `RS01`–`RS10`;
- corpus repository identities remain unique and fixed;
- the preregistered infrastructure taxonomy remains exactly six layers;
- the operational platform vocabulary remains seven explicitly mapped platforms;
- OpenAIRE and OpenAlex remain distinct platforms under `discovery_graph`;
- the preregistered denominator remains 60 object-layer units;
- observation records require a concrete platform and evidence references;
- failed observations require a failure reason;
- no observation can introduce `RS11`;
- the initial baseline preserves its cutoff, reconciliation timestamp, Codex provenance, Zenodo counters, and Software Heritage `NOT_VERIFIED` boundary;
- live Zenodo counters cannot be backdated;
- the public-data handling policy retains its key exclusions.

GitHub Actions currently runs the checker in **advisory mode** on pull requests and pushes to `main`. Contract findings are surfaced as warnings but do not block ordinary repository work during bootstrap/baseline reconciliation. Strict mode is opt-in and should only become the default gate after the baseline/schema have stabilized.

## General tooling responsibilities

Tools should:

- validate object IDs against the fixed manifest;
- validate infrastructure-layer and operational-platform IDs;
- validate observation records against the repository contract;
- check required provenance;
- preserve failed attempts;
- reject undeclared sample-object expansion;
- keep operational schedule labels traceable;
- distinguish warnings from evidence-backed conclusions.

No external API credentials, cookies, session data, or secrets belong in the repository.

## October 10 Zenodo version extract

The 32-row independent [version-counters-independent.csv](../monitoring/2026-10-10/02-reconciliation/version-counters-independent.csv) is a **derived** public-field extract reviewed against Zenodo search, `/versions`, and individual-version endpoints. It is **not** a preserved 32-response raw HTTP transport archive, and its batch windows are not per-request server times.

Its contract is specified in [schema/counting-rules.md](../schema/counting-rules.md#supplementary-zenodo-version-family-reconciliation-2026-10-10). Any locally executed replay/checker must retain per-family identifier joins and flag attached aggregate disagreements instead of fabricating missing counts. **No new retained-evidence checker is added to GitHub Actions**; the existing advisory CI validates only its configured contract checks.

## October 14 retained diagnostics

Run `python tools/check_retained_reconciliation_20261014.py` locally to verify the three October 14 packages, canonical IDs, hashes, source fields, DOI route convergence, counters and source separation. It makes no network calls and is not added to GitHub Actions

## Evening new-release verification

Run `python tools/check_retained_evening_20261014.py` locally for the new release/DOI/version/page joins. It makes no network requests and is not added to cloud CI

## October 15 morning retained evidence

Run `python tools/check_retained_morning_20261015.py` locally for the new source, aggregation, version-count and identity joins. The checker is offline and not added to cloud CI

## October 18 research capture

Run `python -B tools/check_research_capture_20261018.py` for read-only public-artifact hashes, field joins and count consistency. Original raw response/ZIP bytes are locally retained and not included in this public field-extract package. This command is not added to cloud CI.

## October 20 research recheck

`python -B tools/check_research_recheck_20261020.py` verifies the new diagnostic package offline without writes or network. It is not added to cloud CI.
