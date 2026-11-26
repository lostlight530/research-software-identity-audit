# 2026-11-19 web-assisted review of all 34 registered supplementary surfaces

**Record class:** supplementary diagnostic review; not a prospective observation.  
**Review date:** 2026-11-19 (Asia/Shanghai logical date).  
**Direct capture source:** [02-complete-institutional-recheck](../02-complete-institutional-recheck/README.md), GitHub Actions run [44356891292](https://github.com/lostlight530/research-software-identity-audit/actions/runs/44356891292).  
**Search method:** web search and direct public-page inspection, selecting API, HTML, registry, resolver, ontology, upstream PR, or standard-specific methods according to each surface's observable contract.

## Coverage and disposition

- All **34/34** listed surfaces were reviewed.
- The bounded direct collector returned **28/34 HTTP 200** and **6/34 blocked, failed or unresolved**: ScreenIT ASWG (URLError), dkNET (403), InterLex (403), HAL (404), Identifiers.org (404), N2T (403).
- Flexible web review recovered the same RRID record through ASWG and dkNET alternative pages. Bioregistry confirms RRID namespace/provider mappings for Identifiers.org and N2T, but does not prove that the exact target identifier resolves there.
- **InterLex and HAL remain UNKNOWN.** HTTP 403/404 and search non-return are not evidence of absence.
- Several HTTP-200 endpoints are still transport-only because their response format was not projected (HTML, RDF/XML, Handle JSON, Crossref JSON, CiteAs JSON, etc.). See the per-surface matrix.

## Confirmed structural results

### OpenAIRE

- 102/102 exact DOI queries complete; 94 positive queries.
- 66 distinct result IDs and 108 result occurrences across 12 Zenodo repository families.
- 11 aggregate result IDs and 14 split DOI queries.
- Each fixed sample repository RS01–RS10 has one aggregate result ID and one split DOI query; CONTROL has one aggregate and four split DOI queries; supplementary LSEL has neither.
- The 12 families are not 12 study objects: they comprise RS01–RS10, CONTROL (not RS11), and supplementary LSEL.

### OpenAlex

- 102/102 DOI queries succeeded; 34 exact canonical DOI matches and 34 distinct Work IDs.
- Author profile reports 35 works and 3 citations; profile count, DOI exact matches, Work IDs and software objects are separate units.
- Ten fixed Zenodo families map their concept/version DOI sets to one Work each. CONTROL and LSEL also each map their known DOI set to one Work.
- 21 WorkflowHub version DOI records are separately represented as Work IDs. In particular, versions 8 and 9 of WorkflowHub records 2332 and 2334 have separate Work IDs.
- OpenAlex documentation describes concept/version DOI aggregation and its DOI-to-Work matching semantics; a Work is not a software-object count.

### DataCite and ORCID

- Fixed DOI cohort: 102/102 DataCite DOI requests returned findable records; no selected-field change versus 2026-11-18.
- ORCID public works: 18 groups / 119 summaries, unchanged in selected counts versus 2026-11-18.
- The maintainer-supplied DataCite Commons query has 105 records. This is a different ORCID-filtered query scope from the fixed 102 DOI-key inventory; do not call the three-record scope difference a temporal delta without DOI-level reconciliation.

### Zenodo and usage counters

- All 67 DOI keys in the existing version inventory returned HTTP 200. The fixed RS01–RS10 subset contains 60 complete version rows, totaling 4,208 version views and 44 version downloads.
- The 67-key inventory contains 5 CONTROL and 2 LSEL versions, with latest known entries dated before the maintainer-supplied 2026-11-15 RSIA and LSEL v0.5.1 releases. Those two latest supplementary releases are **not represented in this 67-key inventory**; their DOI/record IDs must be reconciled before claiming complete current supplementary version coverage.
- Maintainer-supplied 12 record page counters total 3,489 views when the rows are summed, while the supplied total says 3,589; downloads sum correctly to 56. The 100-view discrepancy is preserved as UNKNOWN, not silently repaired.
- These page-level counters are not interchangeable with the 60 version-specific API counters. The unkeyed 2026-11-15 RSIA and LSEL v0.5.1 entries are separately listed in [zenodo-supplementary-inventory-gap.csv](zenodo-supplementary-inventory-gap.csv); their DOI and record IDs remain UNKNOWN.

## Other important findings

- WorkflowHub exposes 2332 v9, 2334 v9, 2337 v1 and 2347 v2. The NEXUS CORTEX organization entry has no ROR ID or institutional location metadata; this is a registry identity, not institutional endorsement.
- RSD publicly lists the control repository. Its indexed commit count differed across cached snapshots (107 vs 127); use GitHub main as the source of truth for repository state.
- Helmholtz RSD is a real directory, but adding entries is restricted to Helmholtz Association users; no target listing was confirmed.
- LifeMonitor exposes an OpenAPI REST API; registry-client actions require credentials. No authenticated workflow test was performed.
- RRID SCR_029105 is discoverable through SciCrunch/RRID/NIF/dkNET/ASWG surfaces. These are multiple views of a shared registry record, not five independent endorsements.
- Software Heritage reports all ten origins with latest visit status `full`; latest visits range from 2026-10-24 to 2026-11-11. This read-only check did not trigger new archival visits.
- GitHub main and release endpoints succeeded for 11 repositories. All ten sample main SHAs were unchanged; only the control repository main changed, from `78a617c1a4975da6b475a05b36e5ffe6487f1630` to `079b2053d9b600dee353350dd6fb7c7782b1f325`.
- EDAM's `EDAM.owl` is RDF/XML, so JSON parsing is the wrong extractor. The configured label "EDAM BioPortal" does not match the edamontology.org locator.
- The configured RO-Crate 1.1 URI resolves, but RO-Crate 1.3 is the current long-term specification.
- The configured "CodeMeta CFF" locator tests CFF only; CodeMeta was not separately tested. "CiteAs howfairis" similarly points to CiteAs, not a howfairis endpoint.

## Evidence and limits

- `surface-matrix.csv` contains all 34 surfaces, direct transport state, alternate search method, identity classification, source locators and limits.
- `maintainer-supplied-metrics.json` preserves the WorkflowHub team dashboard, Zenodo 12-row counters and DataCite Commons facets as maintainer-supplied context, not provider raw captures.
- The 02 package preserves 458 exact source request attempts, UTC clocks, response hashes and minimized selected fields. Provider response bodies and authorization headers were not retained.
- Web search snippets are discovery aids; the canonical source URLs are retained for independent rechecking. No UI claim, endorsement, live deployment, account-authenticated review or institutional acceptance is inferred.

## Contract boundary

- Fixed sample remains RS01–RS10.
- Control repository remains outside the sample and is not RS11.
- Six preregistered layers and 60 analytical units per eligible scheduled timepoint remain unchanged.
- Seven operational platforms and 70 possible platform checks remain a separate operational denominator.
- No OSF write, schedule change, new Release, new DOI or prospective observation was created by this review.
