# Fixed-ten release-identity documentation closeout — 2026-10-10

**Change class:** cross-repository documentation/provenance reconciliation, **not** a baseline correction, new software release, extra scientific object, institutional affiliation, preregistration amendment, or new prospective observation.

**Review date:** 2026-10-10 (Asia/Shanghai). The date is the ledger's compilation date, **not** an invented individual API-retrieval timestamp. Individual GitHub `published_at` timestamps and Zenodo record identifiers are separately recoverable from their public endpoints and archived previous reviewer materials.

## Finding and adopted repair

An actual cross-repository documentation ambiguity was found: all ten fixed research software repositories retained an initial **2026-09-16** archival publication block in `RELEASE_POLICY.md`, headed "Current archived software publication", while all ten had subsequently published a **2026-09-30** month-close and **2026-10-04** software release with individually resolvable Zenodo Version DOIs.

**Actions:** one dedicated branch and one-file PR for each of RS01–RS10, appending the exact three Version DOI identities without erasing or backdating the September 16 source section. The older `CITATION.cff` and `codemeta.json` concept DOI references were **retained intentionally**. Version DOIs identify the archived snapshots; concept DOIs identify the evolving software family. No repository was told to re-release, move tags, backdate citation metadata or fabricate scholarly uptake.

The per-repository DOI structure was cross-checked with public Zenodo `conceptrecid` version enumeration (three version records per object), direct version record identities, and corresponding GitHub `releases/latest` pages. The archived version-level collection and its limits are in [independent reviewer verification](../monitoring/2026-10-10/02-reconciliation/independent-version-verification.md).

## Public release DOI traceability

All Zenodo numbers below have prefix `10.5281/zenodo.`; columns `concept` / `v1` / `v2` / `v3` are **record ID suffixes**, not new analytical units.

| Fixed object | Concept DOI suffix | 2026-09-16 version | 2026-09-30 version | 2026-10-04 version | Merged documentation PR / main SHA |
| --- | --- | --- | --- | --- | --- |
| RS01 [welcome-to-github](https://github.com/lostlight530/welcome-to-github) | `22790907` | `22790908` | `23068145` | `23137203` | [#726](https://github.com/lostlight530/welcome-to-github/pull/726) · [b5b197759b](https://github.com/lostlight530/welcome-to-github/commit/b5b197759b3574f319099423aae4f0b6eacc523e) |
| RS02 [zero-entropy-lab](https://github.com/lostlight530/zero-entropy-lab) | `22791081` | `22791082` | `23068144` | `23137204` | [#616](https://github.com/lostlight530/zero-entropy-lab/pull/616) · [6e9be5f58f](https://github.com/lostlight530/zero-entropy-lab/commit/6e9be5f58f497e9e88f38b3d35cbb3055cb11e8d) |
| RS03 [Axiom-0](https://github.com/lostlight530/Axiom-0) | `22791103` | `22791104` | `23068261` | `23137205` | [#361](https://github.com/lostlight530/Axiom-0/pull/361) · [5456ad2146](https://github.com/lostlight530/Axiom-0/commit/5456ad214613de9a6e4293f4f045909eafef53ea) |
| RS04 [reflective-continuum](https://github.com/lostlight530/reflective-continuum) | `22791141` | `22791142` | `23068260` | `23137206` | [#445](https://github.com/lostlight530/reflective-continuum/pull/445) · [ac08e2ba41](https://github.com/lostlight530/reflective-continuum/commit/ac08e2ba41303d5ebdd0666b2e9dbbc1d0865946) |
| RS05 [agent-foundations](https://github.com/lostlight530/agent-foundations) | `22791169` | `22791170` | `23068262` | `23137207` | [#268](https://github.com/lostlight530/agent-foundations/pull/268) · [00387b17d8](https://github.com/lostlight530/agent-foundations/commit/00387b17d81288ec829d4e4e28f5fd0aeef46763) |
| RS06 [auto-doc-engine](https://github.com/lostlight530/auto-doc-engine) | `22791404` | `22791405` | `23068471` | `23137215` | [#111](https://github.com/lostlight530/auto-doc-engine/pull/111) · [0cc065b3ae](https://github.com/lostlight530/auto-doc-engine/commit/0cc065b3ae34f888e26112fdccc27affb3291ca7) |
| RS07 [epistemic-pipeline](https://github.com/lostlight530/epistemic-pipeline) | `22791463` | `22791464` | `23068494` | `23137216` | [#110](https://github.com/lostlight530/epistemic-pipeline/pull/110) · [88c4406840](https://github.com/lostlight530/epistemic-pipeline/commit/88c44068405d5f998db5324ba214d9792ac39128) |
| RS08 [sci-render-kit](https://github.com/lostlight530/sci-render-kit) | `22791375` | `22791376` | `23068472` | `23137219` | [#112](https://github.com/lostlight530/sci-render-kit/pull/112) · [c99a959720](https://github.com/lostlight530/sci-render-kit/commit/c99a959720af848b38d430a7d93ffc5d324d9552) |
| RS09 [china-agentic-observatory](https://github.com/lostlight530/china-agentic-observatory) | `22791309` | `22791310` | `23068347` | `23137211` | [#135](https://github.com/lostlight530/china-agentic-observatory/pull/135) · [11617c4671](https://github.com/lostlight530/china-agentic-observatory/commit/11617c4671277dc925ae9fcdf10a11f3ac16d0d8) |
| RS10 [agentic-frontier-observatory](https://github.com/lostlight530/agentic-frontier-observatory) | `22791334` | `22791335` | `23068352` | `23137214` | [#136](https://github.com/lostlight530/agentic-frontier-observatory/pull/136) · [1c975a9353](https://github.com/lostlight530/agentic-frontier-observatory/commit/1c975a93531aa7ccfe87b6fe2fdc802bc183f983) |

**Verification of merge result:** each PR returned `merged=true`, and each repository's fresh `main` commit exactly matched the returned merge SHA. Each `RELEASE_POLICY.md` displayed the three Version DOIs and original Concept DOI following merge. All ten PR diffs had **one file, 12 additions, 0 deletions**.

**Merge strategy provenance:** nine repositories explicitly disallowed squash merges, so each used the allowed native merge-commit strategy; `auto-doc-engine` allowed squash and used it. Repository merge settings were not modified.

## Runtime checks and proof limits

- GitHub Pages/deployment and/or push workflows on the corresponding new `main` SHA reported **SUCCESS** for `welcome-to-github`, `zero-entropy-lab`, `Axiom-0`, `reflective-continuum`, `agent-foundations`, `china-agentic-observatory`, and `agentic-frontier-observatory`. These are *configured workflow statuses*, **not** independent evidence of scientific validity.
- No GitHub Actions run was exposed by the post-merge `main` runs query for `auto-doc-engine`, `epistemic-pipeline`, or `sci-render-kit` at this review. Their local test suites, strict checkers and offline retained evidence verification were **NOT_EXECUTED in this task**. Successful merge is not a replacement test.
- This was a targeted **citation and release-policy document audit**, not a claimed bytewise inspection of every file in ten repositories. Absent `.zenodo.json` in a given repository is **not automatically an error**; GitHub/Zenodo integration may use other metadata surfaces.
- No deliberate new GitHub release or change to the existing 2026-10-04 `v2026.10-open-research-production-framework` tags occurred.
- Current `main` is newer than archived releases. Historic release snapshots do not certify current implementation or research findings.

## Related institutional discovery review — no silent promotion

The already merged [2026-10-10 scholarly infrastructure review](infrastructure-review-2026-10-10.md) and its [public source cross-check](infrastructure-review-2026-10-10.md#supplemental-independent-public-cross-check-2026-10-10-14301434-utc) cover public RSD identity/person/project listings, **open** RSD upstream issues #1870/#1871, **open/unmerged** rseng PR #498, public SciCrunch RRID `SCR_029105`, OSF/DataCite/Internet Archive PID links, ORCID partial visibility, OpenAlex conflicting author-profile responses, and unresolved OpenAIRE/Software Heritage endpoints.

These existing read-only institutional observations are **not** our merged upstream changes, not evidence of platform maintainer adoption, employment/affiliation, scientific approval, or additional preregistered infrastructure layers. Their actual source and author identities remain with the original records.

**No additional institution-facing record merits an invented ACCEPTED/MERGED state.** Keep unresolved platform results unresolved. Do not turn RSD, SciCrunch, rseng, WorkflowHub, HAL, or Internet Archive surfaces into a seventh preregistered layer or eighth core operational platform.

## Contract boundary

OSF Registration `10.17605/osf.io/5b329` is the frozen prospective research contract. The fixed corpus remains RS01–RS10, six layers yield **60** object-layer units per eligible scheduled timepoint, and seven operational platforms yield **70 possible checks**, not 70 analytical units.

`research-software-identity-audit` is the independent control/provenance/software runtime with its own concept DOI `10.5281/zenodo.23166490` and two recorded version DOIs; it is **not RS11**.

**Disposition:** `DOCUMENTATION_LINEAGE_RECONCILED`; `NO_NEW_RELEASE`; `NO_INSTITUTIONAL_ACCEPTANCE_INFERRED`; `NO_PROSPECTIVE_OBSERVATION`.

Retest only when a new valid release actually exists, a named external institutional record changes with direct public evidence, a citation DOI identity is demonstrably wrong, or a documented contributor/maintainer raises a concrete discrepancy.
