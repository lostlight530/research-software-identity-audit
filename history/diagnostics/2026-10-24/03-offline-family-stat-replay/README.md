# Retained Zenodo rollup offline replay — 2026-10-24

This is an **offline cross-file validation addition**, not a new public Zenodo query or a new observation. It supplements, and never edits, the attributed October 24 early-morning [12-family version/DOI evidence package](../02-morning-infrastructure-and-zenodo-family-rollup/README.md).

Run from repository root:

```bash
python -B tools/check_zenodo_family_rollup.py
```

The checker is **Python 3 standard-library-only**, read-only and deterministic. It joins the frozen `corpus/object-manifest.csv` identities to the existing family rollup (12 rows), regular-URL version evidence (45 rows), dual-URL family comparison (12 rows), and dual-URL version comparison (45 rows). It tests DOI consistency, family-versus-version arithmetic for Views and Downloads, retained attached family fields, source URLs, and per-version/per-family URL-shape differences.

**Crucial interpretation:** the reported regular-URL **2,681** versus diagnostic-URL **2,836** Views may **both pass structural validation** even while conflicting. The checker reports `UNRESOLVED_TWO_URL_REPRESENTATIONS` and **does not turn +155 into observed traffic growth**, select a preferred uncached source, sum per-version unique viewers as people, or rewrite older capture clocks. Failing a join or arithmetic invariant is a validator error; a real source conflict is retained as a legitimate research result.

The check runs in CI as **advisory** (does not gate repository iteration). It establishes only that the preserved **selected-field CSVs** reconcile with each other; there is no retained raw HTTP body/server Date proof, no new live Zenodo capture, and no impact on OSF frozen study contract, six infrastructure layers, 60 units at eligible timepoints, or sample RS01–RS10. Control is not RS11 and the pilot is outside the sample. **Prospective cells created: 0**.

For a later dataset use `--directory PATH` with an equivalent package structure. Do not silently modify the existing historical CSVs to make an inconsistent later measurement pass.
