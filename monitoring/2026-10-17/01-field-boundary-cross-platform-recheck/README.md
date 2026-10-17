# 2026-10-17 field-boundary and cross-platform catalogue recheck

**Record class:** diagnostic monitoring / **not** an eligible prospective OSF observation  
**Actual public-page extraction window:** 2026-10-17 23:38:44–23:39:21 Asia/Shanghai (2026-10-17T15:38:44Z–15:39:21Z); outer batch only, not per-request timestamps  
**Frozen scope:** RS01–RS10, six preregistered infrastructure layers, seven operational platforms. WorkflowHub and bio.tools are supplementary discovery surfaces in this review, not additions to the preregistered platform set.

This package corrects a **field-boundary parsing issue**, rechecks ten current Zenodo release pages, records the separately reported control page's partial state, verifies four WorkflowHub workflow identities under project 490, and captures the public bio.tools metadata fields. It does not change the OSF Registration, sample manifest, schedule, schema, baseline, or checker.

## 1. Correction: concatenated page text is not a counter

The supplied flattened text contains tokens such as `1875`, `1682`, and `1671`. They are **adjacent UI fields concatenated after whitespace was lost**:

- `1875` = **187 Views** + **5 Downloads**
- `1682` = **168 Views** + **2 Downloads**
- `1671` = **167 Views** + **1 Download**

They are not 1,875 / 1,682 / 1,671 views. The field labels and source record IDs are retained in [the Zenodo field extract](zenodo-page-field-extract.csv), with the parsing correction preserved separately in [field-boundary-correction.md](field-boundary-correction.md).

Zenodo's [official usage-statistics guidance](https://support.zenodo.org/help/en-gb/4-usage-statistics/15-what-is-a-view-download-data-volume) says the public page primarily displays **unique** views/downloads, counts repeats within a one-hour visitor window once, aggregates all versions by default, and updates usage statistics once daily. Thus the column names use page-visible unique counts rather than API total counts. A sum across ten records is still **not** a global count of unique people.

## 2. Zenodo: ten fixed-sample records

| Sample | Version record | All-version page unique views | All-version page unique downloads | Current-version page unique views | Current-version page unique downloads | Δ views vs 2026-10-16 API unique field |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| RS01 | [23365504](https://zenodo.org/records/23365504) | 187 | 5 | 3 | 1 | +6 |
| RS02 | [23365551](https://zenodo.org/records/23365551) | 145 | 1 | 2 | 1 | +7 |
| RS03 | [23365534](https://zenodo.org/records/23365534) | 167 | 1 | 2 | 1 | +6 |
| RS04 | [23365567](https://zenodo.org/records/23365567) | 120 | 1 | 1 | 1 | +5 |
| RS05 | [23365540](https://zenodo.org/records/23365540) | 146 | 2 | 2 | 1 | +7 |
| RS06 | [23365510](https://zenodo.org/records/23365510) | 138 | 0 | 5 | 0 | +6 |
| RS07 | [23365517](https://zenodo.org/records/23365517) | 148 | 1 | 1 | 1 | +6 |
| RS08 | [23365525](https://zenodo.org/records/23365525) | 137 | 2 | 2 | 1 | +7 |
| RS09 | [23365548](https://zenodo.org/records/23365548) | 155 | 1 | 1 | 1 | +5 |
| RS10 | [23365543](https://zenodo.org/records/23365543) | 168 | 2 | 3 | 1 | +7 |
| **Ten fixed samples** | — | **1,511** | **16** | **22** | **9** | **+62** |

The prior comparison endpoint is the retained 2026-10-16 family API field extract, which summed **1,449 unique views / 16 unique downloads** across RS01–RS10. The current public page display sums to **1,511 / 16**. This is a descriptive cross-source snapshot difference of **+62 unique-view counts and 0 unique-download counts**, not an exact event-time delta and not proof of why the counters changed. The ten per-record page values, source URLs, prior fields and arithmetic deltas are machine-readable in [zenodo-page-field-extract.csv](zenodo-page-field-extract.csv).

The latest-version-specific page values sum to **22 unique views / 9 unique downloads**. They are the per-record counters for the current version only; do not sum them with the all-version fields. Do not compare the all-version page counts with the old API `stats.views` total field; that would mix total and unique semantics.

**Control repository:** the public page for [Zenodo record 23284570](https://zenodo.org/records/23284570) returned identity metadata, but the extracted excerpt did not include its usage counters. State is **PARTIAL / counters not extracted**, not zero. It remains separate from RS01–RS10 and is not RS11. This review did not repeat a complete three-version control-family API enumeration or a 43-version census.

## 3. WorkflowHub: project 490 now lists four workflow identities

The public [NEXUS CORTEX Research Workflows project](https://workflowhub.eu/projects/490/workflows) lists four workflow records:

| Workflow | DOI / version | Current page evidence |
| --- | --- | --- |
| [NEXUS CORTEX Life Cycle — welcome-to-github](https://workflowhub.eu/workflows/2332) | `workflowhub.workflow.2332.8` | Version 8 created display: 14 Oct 2026 12:22 |
| [NEXUS CORTEX Life Cycle — zero-entropy-lab](https://workflowhub.eu/workflows/2334) | `workflowhub.workflow.2334.8` | Version 8 created display: 14 Oct 2026 12:20; supplied project listing says last updated 11 Oct 2026 15:53 — **date-field semantics unresolved** |
| [Brain Evolution — welcome-to-github](https://workflowhub.eu/workflows/2337) | `workflowhub.workflow.2337.1` | Historical precursor, created display: 11 Oct 2026 15:49; keep distinct from the later NEXUS workflow |
| [Life Science Knowledge Workflow](https://workflowhub.eu/workflows/2347) | `workflowhub.workflow.2347.1`, UI version `0.4.0` | Public page confirms DOI, project association, `records` JSON and `topics` JSON inputs, and 199 KB preview; created display: 17 Oct 2026 16:00 |

WorkflowHub times above are **page-displayed strings**; the pages did not establish a timezone in the extracted output. For 2334, the current page version-history field and the supplied project-listing field are preserved separately instead of forcing a single date. WorkflowHub's current Team Dashboard counters were **not** retrieved in this pass. The prior supplied top-three values (2,511 views / 204 downloads) are not re-labelled as current, and the addition of workflow 2347 does not justify inventing its usage counts.

The supplied excerpt describes 2347 as a Work-in-progress CWL v1.2 workflow with bounded, offline transformation of supplied evidence records. That operational description is **attributed to the supplied excerpt**; the independently extracted public page verifies identity/DOI and visible input/preview fields only. WorkflowHub remains outside the OSF preregistered seven operational platforms.

## 4. bio.tools: public registry identity is now present

The [public bio.tools API record](https://bio.tools/api/t/life-science-protein-file-audit) returned HTTP 200 with:

- `biotoolsID=life-science-protein-file-audit`
- Name: **Life Science Protein File Audit**
- Homepage: [life-science-ecosystem-lab/bio_tool](https://github.com/lostlight530/life-science-ecosystem-lab/tree/main/bio_tool)
- License `MIT`, type `Command-line tool`, language `Python`, cost `Free of charge`
- `additionDate=2026-10-17T14:35:25.534070Z`; `lastUpdate=2026-10-17T14:35:25.536758Z`
- Raw returned flags: `validated=0`, `homepage_status=0`; `version=[]`, `maturity=null`, `publication=[]`, `documentation=[]`, `download=[]`

These are the returned fields, not a claim that the record is invalid or that its homepage is broken. The original API bytes/headers were not retained; see [biotools-record-summary.json](biotools-record-summary.json).

**Cross-repository documentation drift identified:** at the inspected source-repository `main` commit `98c46c6d4d472626b51b673b415add61e919bf35`, `bio_tool/README.md` still calls the bio.tools metadata a candidate and says an actual public accession is independently required. The public accession now exists. This target PR records the drift; it does not silently modify the separate source repository. A source-repository docs-only update should reconcile that sentence with the public record and keep the draft JSON's role clear.

## 5. Evidence level and research-contract boundary

- Public pages/API were parsed through a third-party text extraction path. **No unmodified HTTP response bytes, response headers, response digests, or per-request server timestamps** were captured. This is not byte-level archival evidence.
- The flattened-source concatenation was resolved by labelled page fields; the malformed token itself is not preserved as a counter.
- The control record's usage fields, current WorkflowHub Dashboard metrics, and exact WorkflowHub per-request times remain **unavailable in this extraction**.
- No live OSF native-version diff was run, no OSF object was edited, and no prospective schedule offsets were declared.
- No files under `contract/`, `corpus/`, `baseline/`, `schedule/`, `schema/`, `observations/`, `evidence/`, `provenance/`, or executable `tools/` were modified. No release, DOI, tag, or new formal analysis unit was created.

The [frozen OSF registration](https://osf.io/5b329/overview) remains authoritative. The repository's schedule still declares no concrete offsets. This is a **diagnostic monitoring record**, not a prospective observation, and the control repository is not RS11.

Machine summary: [record.json](record.json) · [source/attempt ledger](source-attempts.csv) · [Zenodo field extract](zenodo-page-field-extract.csv) · [WorkflowHub identity extract](workflowhub-asset-identities.csv) · [bio.tools field extract](biotools-record-summary.json) · [correction note](field-boundary-correction.md)
