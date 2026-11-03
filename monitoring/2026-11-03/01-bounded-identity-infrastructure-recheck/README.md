# November 3 bounded research-software identity and infrastructure patrol

**Classification:** append-only diagnostic / selected-field reconciliation; not a scheduled prospective observation, an OSF amendment, new DOI census or original HTTP response archive

**Logical date:** 2026-11-03 Asia/Shanghai. **Compiled client UTC:** 2026-11-03T03:12:24.536Z. **Last eleven-core main-read completed client UTC:** 2026-11-03T03:09:19.860Z. Source reads are distributed over this task, **not** an atomic simultaneous snapshot.

## Contract and comparison clocks

- The frozen [OSF registration](https://osf.io/5b329/overview) and current [manifest](../../../corpus/object-manifest.csv) identify **RS01–RS10**, excluding the control repository and supplementary life-science software. Six layers give **60 object-layer units per eligible scheduled timepoint**. Seven concrete platforms give **70 possible object-platform checks**, not 70 preregistered units
- The repository [operational schedule](../../../schedule/README.md) contains no concrete declared offsets; **0 prospective cells** are added. No original OSF schema, baseline, schedule, raw historical evidence, release or DOI is edited
- The prior [OSF original-versus-approved revision reconciliation](../../2026-10-30/01-osf-schema-response-version-reconciliation/README.md) found **29 compared fields / one changed exploratory field `344-83`**. We did not obtain a new original-provider full-byte registration revision capture
- Main-SHA comparisons use the explicitly retained **2026-11-01T11:49:20.853Z** eleven-head ledger for RS01–RS10. The control head is separately compared with its **2026-11-02T13:23:13Z** main, and institutional / Zenodo counters retain their actual Nov 2 batch windows. This must **not** be described as a Nov 2-to-Nov 3 Git commit delta

## GitHub direct connected source result

- [Exact eleven-head SHA ledger](github-main-deltas.csv) records ten fixed mains ahead of the retained Nov 1 source reads, **219 total main-reachable commits**, **0 behind**, and **161 total two-endpoint changed file paths** (per-repo path differences summed, not unique global files). These include daily/weekly research production and other maintenance; they are not ten new software Releases or DOI events
- All **11 core repositories had zero open PRs** at the checked point. All ten fixed repositories show **5 published GitHub Releases and 5 Git tag refs** each; latest remains `v2026.10-30-evidence-snapshot`. CONTROL has **5 Releases / 5 tag refs** and previously published `v2026.10-control-lifecycle-reconciliation`. No new published Release or tag was identified by these queries
- CONTROL `main` before this monitoring PR: `c12c56bf4a9ffc6b8b972b42efebdb3446bfdeb1`; prior main [GitHub Actions run 41452532533](https://github.com/lostlight530/research-software-identity-audit/actions/runs/41452532533) completed `success`, which is advisory validation, not a scientific certification
- At one independent CI read, recently executed main-head Pages/push workflows were successful in several repositories; `zero-entropy-lab` NEXUS workflow was **in_progress** on a later head. For `auto-doc-engine`, `epistemic-pipeline`, and `sci-render-kit` the queried main workflow-run listing was empty. Do not infer all possible checks green

## Seven operational platforms and 34 supplementary surfaces

- Seven platforms were checked at **heterogeneous source freshness**: GitHub live via connected API; Zenodo one selected latest-version representation carrying UTC-day 2026-11-03 extractor acquisition; DataCite (2026-10-30), ORCID (2026-10-27), SWH (2026-10-27), OpenAIRE (2026-10-27), OpenAlex (2026-10-06) representative extracts are older. **This is not a fresh seven-platform full census**
- [Exact 34-row URL access ledger](surface-access-recheck.csv): **34 requests**, **28 extracted representations**, **6 access/extraction errors**, including **2 additionally independently checked live GitHub statuses**. Only one extract has a 2026-11-03 UTC-day acquisition stamp and one 2026-11-02; the remaining non-GitHub successes are older cached/day-labeled content. Batch receipts are recorded, not original source-response bytes
- Error rows retained: (11) ScreenIT ASWG `connect_error`, (13) dkNET specified `/data/source` HTTP 404, (14) InterLex specified page HTTP 404, (15) EDAM file extraction error with reported HTTP 200, (24) Identifiers.org HTTP 404, (25) N2T HTTP 403. A 404 on one path is **not** a global nonexistence finding. The [Nov 2 institutional review](../../2026-11-02/01-complete-institutional-recheck/README.md) used **other object-specific JSON paths** on some surfaces; no regression between different endpoints is inferred
- Historical **Nov 2** values remain **90 DOI identities; 17 ORCID groups / 106 summaries; OpenAlex 32 enumerated author works; Zenodo 57 versions (50 fixed), 3,308 fixed-ten views / 17 downloads**, and OpenAIRE **88/90 attempts returned with 2 failures**. These are **not November 3 counters or changes**. Current like-for-like metric delta, latest preservation of all new main SHAs, fresh DOI-wide cross-platform convergence and external user identities remain `UNKNOWN`

## Independent upstream institutional interaction checks

- [RSE #498](https://github.com/rseng/software/pull/498): `OPEN`, unmerged, **0 Reviews**. [RSD #1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870): `CLOSED / completed` (2026-10-16), not a new confirmed live UI retest. [RSD #1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871): `OPEN`. RSD upstream latest GitHub Release: `v6.7.5` (2026-10-27)
- The RRID `SCR_029105` resource is externally resolvable, but new curation completion, ownership claim, citation/adoption, formal researcher affiliation or institutional acceptance are **not verified**. RSD's previous **12 software records** are not claimed as a fresh today census

## Scope, provenance, and disposition

- Source basis: connected GitHub commits/main, compare URLs, PRs, tags, Releases, workflow-run status, RSE PR metadata/reviews, RSD Issue state, and public URL extractor receipts `extract_5c758ed8ca2a63c31e027a01cf0f3a9a` / `extract_fdb7b82b7cffffcd2dbd004dec6a7999`. Connector results are selected structured state or excerpts; **no full original HTTP bodies, per-request provider timestamps or byte SHA-256** are represented as retained
- Result: **`SOURCE_MAIN_DELTA_10` + `NO_NEW_FIXED_RELEASE_OR_TAG` + `SAME_ACCESS_CLASS_ONLY` + `EXTERNAL_PARTIAL_UNKNOWN`**. No demonstrated defect in current scientific source, citation, schema or frozen contract: **`NO_CHANGE_REQUIRED`**. This record is a legitimate dated monitoring entry, not a manufactured scientific result
- Machine summary: [record.json](record.json). GitHub ledger and 34 exact URLs form bounded inspectable receipts; unverified states and historical corrections remain unchanged
