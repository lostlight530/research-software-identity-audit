# October 10 final documentary and scholarly-infrastructure closeout

**Class:** additive control-repository quality review / existing-evidence reconciliation. **Review logical date:** 2026-10-10 (Asia/Shanghai), late evening. The repository GitHub base SHA for this review is `5f8f8cc900c3f555681847b0ea94a9a4e729c442`. Public API reviewer tools did not expose exact individual HTTP completion timestamps or raw HTTP response bytes; use this dated review as a *bounded current read*, **never** as an earlier historical state.

**Maintained scope:** only `lostlight530/research-software-identity-audit` is changed by this closeout. The ten fixed software objects and their current `RESEARCH_TEMPLATE.md` files were independently inspected **read-only**. PR #26–#29 were already merged into main at cold start, and open PR count was **zero**. Do not reattribute their original human/agent work to this closeout.

## 1. Frozen method and provenance gate

| Surface checked | Disposition |
| --- | --- |
| OSF Registration `10.17605/osf.io/5b329`, `contract/preregistration.md`, `contract/contract-map.yaml` | **UNCHANGED**: frozen research contract, not operationally rewritten by GitHub |
| `corpus/object-manifest.csv` and baseline `2026-10-05` | **UNCHANGED**: RS01–RS10 fixed; original baseline and later reconciliation retain separate timestamps |
| `schema/` and `schema/counting-rules.md` | **UNCHANGED**: 6 preregistered layers, 60 object-layer units / scheduled point, 7 operational platforms, 70 possible platform checks; OpenAIRE and OpenAlex both map to discovery_graph |
| `schedule/README.md`, `AMENDMENTS.md`, `DEVIATIONS.md` | **UNCHANGED**: no declared concrete observation offsets; no eligible post-registration release established in the retained October 10 source check; no new amendment/prospective dataset invented |
| `monitoring/` / `evidence/` dated October 6–10 | **PRESERVED**: October 10 01 source capture, 02 separately attributed correction, and original raw response archive remain distinct |
| `tools/check.py`, local retained evidence checkers and workflows | **UNCHANGED**: existing advisory CI is a governance guardrail, not scientific validation or confirmation the local-only evidence checker ran |
| `RESEARCH_TEMPLATE.md` and machine templates | **RETAIN**: human-facing bounded records and machine operational schema/templates have distinct purposes; do not retrofit old observation records |
| `scholarly/` release/PID and external institution ledger | **ADD CLARIFICATION**: source-specific current responses, external PR ownership, metadata anomaly, and links to latest release DOI |

No `RS11` or extra preregistered layer/platform, inferential model, artificial eligible release, manually manufactured schedule or global composite score is introduced.

## 2. Independently checked external institution/registry status

| Surface / source locator | Current bounded evidence | Correct scope |
| --- | --- | --- |
| RSD [control repository](https://research-software-directory.org/software/research-software-identity-audit) | Public software record accessible in a secondary independent extraction path | **Public directory record**, not scientific endorsement or RS11 |
| RSD [ten-software constellation](https://research-software-directory.org/projects/agentic-research-constellation) | Public project describes exactly ten related software objects; also independently web-indexed | **Project relationship**, not an eleventh sample |
| RSD [issue #1870](https://github.com/research-software-directory/RSD-as-a-service/issues/1870) | GitHub REST: `open`, seven comments, last `updated_at=2026-10-09T12:26:40Z` | Actual update timestamp is *not* this review's retrieval time; **FIX NOT VERIFIED** |
| RSD [issue #1871](https://github.com/research-software-directory/RSD-as-a-service/issues/1871) | GitHub REST: `open`, one comment, last `updated_at=2026-10-09T11:12:04Z` | UI feedback remains unresolved; deployment **NOT VERIFIED** |
| rseng [upstream PR #498](https://github.com/rseng/software/pull/498) | GitHub REST: contributor `lostlight530`, head repo `lostlight530/software`, target repo `rseng/software`, `open`, `merged_at=null`, `mergeable=true`, **0 reviews** | **Our contributor's proposed external PR, not an accepted/merged change to someone else's repository**; no catalog indexing claim |
| SciCrunch [RRID official resolver](https://scicrunch.org/resolver/SCR_029105) | Independent secondary public extraction: Resource Report correctly identifies **Research Software Identity Audit**, `SCR_029105`, control GitHub URL | **Public resolver visible**; curator workflow completion, ORCID ownership association and index-transition timestamp remain **UNKNOWN** |
| OSF [registration](https://osf.io/5b329) | Public registration was observable; DataCite record separately gives study DOI `10.17605/osf.io/5b329` as `StudyRegistration` | Frozen preregistration ≠ mutable software record; no new registration created |
| DataCite [OSF DOI metadata](https://api.datacite.org/dois/10.17605/osf.io/5b329) | Read-only fresh public JSON: `StudyRegistration`; archive `IsIdenticalTo` to Internet Archive; `References` to control beta and formal Zenodo DOIs | Present **metadata relationships**, not propagation-timing proof |
| OpenAlex [author A5151904252](https://api.openalex.org/authors/A5151904252) | Fresh `full-profile` and `select=id,orcid,works_count,updated_date` reads both exposed `works_count=16`, `updated_date=2026-10-09T12:31:04`; earlier dated observations had 30/43 | **TIME/INTERFACE-VARIANT COUNT CONFLICT**, do not infer deletion, reassign historic counts, or claim exact transition instant |
| OpenAlex author-Works list | `filter=author.id:A5151904252` attempted, returned **HTTP 400** in that review path | **QUERY_UNSUPPORTED_OR_FAILED**, not evidence of zero Works or stable count |
| Zenodo version identity/statistics | [October 10 independent 32-version extract](../monitoring/2026-10-10/02-reconciliation/independent-version-verification.md) covers 11 concept families, 32 version records | Ten fixed: `1813` version-summed views and `7` downloads; control: `51/0`; combined display `1864/7`. No inferred human/referrer cause |
| ORCID, OpenAIRE, Software Heritage, HAL, WorkflowHub DOI, RSE catalog | Earlier dated records carry accessible/partial/error evidence; **not all independently re-executed in this final audit** | **PARTIAL / UNRESOLVED / NOT_RERUN** as applicable; no absence or acceptance manufactured |

**Newly detected public metadata integrity detail (DataCite OSF registration):** the DOI response's `creators[0].nameIdentifiers` includes a valid canonical ORCID URL `https://orcid.org/0009-0001-3617-0832` **alongside** a separately listed noncanonical/truncated-looking string `my-orcid?orcid=0009-0001-3617-08` labeled `ORCID`. These are distinct field values in the **same public record**, not two researchers. Mark `EXTERNAL_METADATA_FIELD_ANOMALY`; possible origin and edit permissions **UNKNOWN**. Do **not** change the frozen OSF registration or privately-held account data, imply identity loss, or present this secondary extraction as an authenticated edit. Retest only using the exact authoritative field and current DOI API response.

The original scholarly-infrastructure reviewer ledger and its prior source attribution are preserved; this document is a **later reviewer snapshot**, not their replacement.

## 3. All ten pre-existing research templates: read-only audit

Independently fetched `RESEARCH_TEMPLATE.md` from the *current `main`* of all ten distinct repositories, comparing the section inventory and repository-specific method boundary. The same shared shell is present: Research identity → question → falsifiable claim → source/evidence → object boundary → controls → executed bounded procedure → raw observations → counterexample → interpretation → provisional conclusion → research increment → retest. Each template also has a **repository-specific research surface** and **permanent separation rules**. Historical rewrite prohibition and the supremacy of repository-native method/SOP contracts are present.

| Repositories checked | Applicable owned research detail | Recommendation |
| --- | --- | --- |
| `welcome-to-github` / `zero-entropy-lab` | Parallax `METHOD`/templates and Ballast `METHOD`/templates, respectively, remain task-specific authority | **NO_TEMPLATE_CHANGE_REQUIRED** |
| `Axiom-0` / `reflective-continuum` | Data/canonicalization contracts vs SQLite graph-store/version evidence identity | **NO_TEMPLATE_CHANGE_REQUIRED** |
| `agent-foundations` | Source/claim/implementation/validation axes and bilingual epistemic classification | **NO_TEMPLATE_CHANGE_REQUIRED** |
| `auto-doc-engine` / `epistemic-pipeline` / `sci-render-kit` | Distinct artifact-lineage, runtime state, and rendering/uncertainty contracts | **NO_TEMPLATE_CHANGE_REQUIRED** |
| `china-agentic-observatory` / `agentic-frontier-observatory` | Their own `METHODOLOGY` and Daily/Weekly/Monthly SOPs govern dated observation | **NO_TEMPLATE_CHANGE_REQUIRED** |

**Boundary of template review:** actual ten `RESEARCH_TEMPLATE.md` file contents were inspected; this is **not** an executed test of all ten runtime methods, internal repository validators or CI, nor a claim that every file in each repository was exhaustively audited. No ten-repository file or release was modified by **this** closeout. If a later concrete template drift is found, fix that repository under its own contract instead of auto-copying the audit-control template.

## 4. Document-level repairs justified by current state

1. `RELEASE_POLICY.md` historically described only the beta snapshot while the current formal **2026-10-06** runtime release and separate DOI already existed: append an explicit current-formal-release paragraph without removing or rewriting the beta history.
2. Append an institution-facing ledger addendum for the latest exact GitHub PR/Issue states and the OSF DataCite irregular creator identifier, preserving prior reviewer observations.
3. Add navigation to this closeout for future independent reviewers; keep `scholarly/identifiers.yaml` older historical `pending` field and its dated current verification *in separate sections*, never overwrite older evidence.
4. No unnecessary new CI, data schema, dependency, release, platform account, or PR to external organizations.

## 5. Execution and disposition

- Executed: authorized GitHub repository and PR/Issue REST reads; ten research templates read from current main; current code/contract/template/document static inspection; secondary public extraction of RRID/RSD/DataCite/OpenAlex; fixed existing Zenodo source/derived review checked for consistency of claimed method.
- **NOT_EXECUTED:** direct raw-byte replay of all 32 independently extracted Zenodo versions, full local-only retained-evidence verifier, current OpenAIRE/SWH end-to-end pipeline, all ten repositories' local test suites, manually authenticated institutional accounts. Independent shell `git ls-remote` failed with `Could not resolve host: github.com`; GitHub connector remained available.
- **Contract drift detected:** **none** in fixed corpus, six layers, seven operational platforms, prospective admission rules, frozen registration, baseline, or template method boundaries.
- **Documentary drift detected:** current formal release absent in `RELEASE_POLICY.md` historical archive explanation; corrected append-only, not a new release.
- **Supplementary metadata anomaly detected:** OSF DOI's extra noncanonical ORCID name-identifier field; separately recorded, **not externally repaired**.
- **Overall:** `DOCUMENTARY_CLOSEOUT_WITH_EXPLICIT_EXTERNAL_GAPS`; no claim of scientific validation, 11th sample inclusion, institutional endorsement, external PR acceptance or completed prospective data collection.

**Retest triggers:** explicitly eligible new fixed-corpus software release accompanied by a provenance-bearing operational schedule; change to a cited public RSD/RRID/rseng state; a stable OpenAlex API read with preserved raw JSON/query provenance; or primary-source correction to the inconsistent DataCite creator name identifier. Otherwise keep the frozen research system **small and stable**.
