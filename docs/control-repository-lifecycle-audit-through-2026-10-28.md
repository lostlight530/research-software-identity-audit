# Research-control repository lifecycle and OSF contract reconciliation — 2026-10-05 through 2026-10-28

> **Scope:** retrospective GitHub history and research-contract reconciliation, assembled **after** the cutoff. NOT a new prospective observation, source capture at the historical cutoff, OSF registration amendment, release, DOI, or research sample.
>
> **Historical cutoff:** `2026-10-28T23:59:59+08:00` (`2026-10-28T15:59:59Z`), inclusive. The subsequently merged Oct 29 PR #69 is **not** in the historical inventory.

## 1 · Sources, exact identity, and reproducibility

The pinned [historical `main` commit](https://github.com/lostlight530/research-software-identity-audit/commit/4cacb9b617d2e0383ffca8c757e66c5a44a5a793) is `4cacb9b617d2e0383ffca8c757e66c5a44a5a793`, committed `2026-10-27T15:56:04Z` / October 27 23:56:04 Beijing. GitHub's [recursive tree](https://api.github.com/repos/lostlight530/research-software-identity-audit/git/trees/4cacb9b617d2e0383ffca8c757e66c5a44a5a793?recursive=1) returned `truncated=false`. Its [reachable commit API](https://api.github.com/repos/lostlight530/research-software-identity-audit/commits?sha=4cacb9b617d2e0383ffca8c757e66c5a44a5a793&per_page=100) returned 87 main-reachable commits.

- [Machine-readable as-of snapshot](research-control-lifecycle-summary-through-2026-10-28.json) — source URLs, cutoff, exact ref, category counts, eligibility limits
- [Full 87-commit ledger](control-repository-main-history-through-2026-10-28.csv) — SHA, Git **committer** UTC timestamp, Beijing-local committer day and original subject
- [Full 437-file tracked tree](control-repository-tracked-files-through-2026-10-28.csv) — repo-relative path, original Git blob SHA and owning surface

These files reflect **later retrieval of earlier Git objects**, not contemporaneous 2026-10-28 API captures, an exhaustive all-branch history, untracked local files, external origin response bytes, or every PR conversation. Git **committer** clocks are not automatically Git author, merge, platform-response, release or DOI registration timestamps. The October 21 [older inventory](control-repository-inventory-2026-10-21.md) and [71-commit ledger](control-repository-main-commit-ledger-2026-10-21.csv) retain their independent original scope.

| Git-history property | Confirmed as of cutoff | Qualification |
| --- | --- | --- |
| GitHub repo `created_at` | `2026-10-05T14:59:45Z` | 22:59:45 Beijing, separate from registration |
| First reachable `main` commit | `e5ba0a0e7dc548bd5bd3e79b4d7fc0cb95e528aa`, 14:59:46Z Oct 5 | First commit tree had one README, not the whole later runtime |
| Reachable `main` history | **87 commits** | Not all Git refs, branches or draft PR edits |
| Pinned Git tree | **437 tracked files** | Not 437 independent scientific observations |
| Post-Oct21 inventory `main` tree (`cf8ae14f...`) | **303 files** | Compared against the pinned historical Git tree |
| Oct21-to-Oct28 two-tree delta | **134 added paths / 10 changed existing blobs / 0 removed paths** | Two endpoints only; does not rule out intermediate edits or renames |
| October 28 Beijing-local `main` commits | **0** | Not proof of no research work or platform events |
| Last reachable `main` commit at cutoff | `4cacb9b6...`, Oct 27 local | Subsequent Oct 29 additions explicitly excluded |

## 2 · From preregistration to executable runtime

| Time / period | Source-supported research-engineering event | What it does **not** establish |
| --- | --- | --- |
| **Oct 5, 2026 22:04 Beijing** | [OSF Registration 5b329](https://osf.io/5b329/overview), DOI `10.17605/OSF.IO/5B329`, independently separate from [associated project wa5v8](https://osf.io/wa5v8) | The OSF registration is a plan, not a completed research result; the exact initial-vs-updated version diff is not available in this audit |
| **Oct 5, 22:59** | GitHub control repository created after registration; README/bootstrap, governance, initial baseline material followed | A GitHub `main` snapshot is not an OSF frozen-revision proof |
| **Oct 5 cutoff / Oct 6** | [Initial baseline](../baseline/2026-10-05/README.md), cutoff **Oct 5 23:59:59 Beijing**, later approximately Oct 6 00:33:54 reconciliation and preserved original Codex source record | Later reconciliation collection is **retrospective reconstruction**; do not place its retrieval clock at cutoff |
| **Oct 6–13** | Dated monitoring, failure recording, original [RS object-ID correction](../baseline/2026-10-05/correction-object-id-mapping-2026-10-06.md), exploratory Zenodo benchmark, direct scholarly-source verification, [OSF Overview crosswalk](../contract/osf-overview-crosswalk-2026-10-08.md), [Oct 13 prerelease gate](../monitoring/2026-10-13/02-fixed-corpus-release-gate/README.md) | Diagnostic source labels “Wave 1” or exploratory scripts are not preregistered observations |
| **Oct 14** | Fixed ten public [Release ledger](../monitoring/coverage/release-event-ledger-2026-10-24.csv) records the new published checkpoint releases | A new fixed-corpus release **by itself** is not a fully authorized scheduled prospective timepoint |
| **Oct 14–21** | Retained source packages and corrections, [Oct 18 immutable release/archive reconciliation](../scholarly/release-identity-reconciliation-2026-10-18.md), historical file inventory | Git tag, `main`, archived Zenodo ZIP and DataCite record have different identities and timestamps |
| **Oct 22–24** | [Source coverage and release calendar](../monitoring/coverage/README.md), [created-at-to-Oct24 gap ledger](../monitoring/coverage/creation-calendar-reconciliation-2026-10-24.md), [local evidence handoff](../evidence/2026-10-24/04-local-history-evidence-handoff/README.md), [path classification](record-path-classification-review-2026-10-24.md) | Calendar entries for unsupported days are not imputed traffic, requests or successful runs |
| **Oct 25–27** | [Observation semantics and acceptance gates](observation-assurance-2026-10-25.md), [seven platform-specific observable contracts](platform-evidence-semantics-2026-10-25.md), [manifest coverage repair](public-manifest-coverage-reconciliation-2026-10-26.md), [Oct 27 diagnostics](../monitoring/2026-10-27/01-bounded-seven-platform-recheck/README.md), and PR #68 source-ledger checker | Checker PASS or public byte hash matching does not certify scholarly truth, origin freshness or external API state |
| **Oct 28** | No new reachable `main` commit on that Beijing-local day | No dated Oct 28 original platform source response is fabricated here |

## 3 · Clause-level OSF ↔ GitHub ownership and alignment

**Scientific authority:** the [OSF registration](https://doi.org/10.17605/OSF.IO/5B329) is the registered research contract. [`contract/preregistration.md`](../contract/preregistration.md) is its GitHub operational **mapping**, not an authoritative replacement of an OSF revision. The author-supplied [October 8 clause crosswalk](../contract/osf-overview-crosswalk-2026-10-08.md) notes that `Other planned analysis` was marked **Updated**, without original-versus-updated history or effective edit timestamp. **Unknown stays unknown**, not silently backported to October 5.

| OSF contract clause | GitHub source of implementation/evidence | State at Oct 28 |
| --- | --- | --- |
| Purposive fixed corpus | [RS01–RS10 manifest](../corpus/object-manifest.csv) | **ALIGNED:** exactly 10 objects; research-control repo is not RS11 |
| Exactly six analytical infrastructure layers | [layer taxonomy](../schema/infrastructure-layers.yaml) | **ALIGNED:** `source_repository`, `archival_repository`, `identifier_registration`, `author_registry`, `preservation_archive`, `discovery_graph` |
| Seven concrete operational platforms | [platforms](../schema/platforms.yaml) | **ALIGNED OPERATIONALLY:** GitHub, Zenodo, DataCite, ORCID, Software Heritage, OpenAIRE, OpenAlex; last two separately queried under **one** discovery layer |
| Predefined analytical unit | [counting rules](../schema/counting-rules.md) | **ALIGNED:** **10 × 6 = 60** object-layer units per eligible scheduled timepoint; **10 × 7 = 70** *possible checks*, never 70 study units |
| Historical / prospective separation | [baseline](../baseline/2026-10-05/README.md), [raw observations](../observations/raw/README.md) | **ALIGNED POLICY:** Oct 5 cutoff, later true retrieval clocks, retrospective flag and no backfill |
| First eligible new release | [release ledger](../monitoring/coverage/release-event-ledger-2026-10-24.csv) and [schedule](../schedule/README.md) | **PARTIAL:** Oct 14 fixed-corpus releases are recorded, but qualifying study execution is not established |
| Scheduled timepoints and fixed stop | [operational schedule](../schedule/README.md) | **UNRESOLVED OPERATIONAL PREREQUISITE:** no concrete offsets or complete timepoint list declared; no retrospective T0/+24/+72/+7d inventions or failure-driven extensions |
| Observations, incomplete states and evidentiary absence | [taxonomy](../schema/state-taxonomy.yaml), [observation schema](../schema/observation.schema.json) | **ALIGNED PREFLIGHT:** not-found, 403/404/429, rate limits, anti-bot, blocked, partial and unresolved remain distinct from global absence |
| Original evidence and correction lineage | [evidence](../evidence/README.md), [provenance](../provenance/README.md), [assurance](observation-assurance-2026-10-25.md) | **PARTIAL:** some retained raw bytes and digests publicly available; other origin bodies local-only or unavailable; interpretation must follow the source and the correction chain |
| Amendments, deviations, exploratory | [`AMENDMENTS.md`](../AMENDMENTS.md), [`DEVIATIONS.md`](../DEVIATIONS.md), [analysis](../analysis/README.md) | **ALIGNED GOVERNANCE:** no unlogged substantive change, no post-hoc outcome promoted to registered hypothesis |
| Research interpretation | [analysis](../analysis/README.md), [OSF crosswalk](../contract/osf-overview-crosswalk-2026-10-08.md) | Descriptive counts, proportions, comparable timestamp differences, transitions, source-specific consistency only; **no** NHST, regression, ANOVA, Bayesian inference, imputation, causality or global score |

The status `ALIGNED POLICY` means the corresponding repo-native representation is consistent with the mapped contract, **not** that every historic attempt is scientifically valid or that the OSF original revisions have been independently replayed. This review does not alter a single registered analytical unit or the frozen OSF content.

## 4 · All five research questions: readiness, not fictitious results

| OSF RQ | Already retained and usable as historical / diagnostic context | Prospective answer at cutoff |
| --- | --- | --- |
| **RQ1** — identity propagation and temporal order | GitHub Release timestamps; bounded DOI/version identity checks; source-specific discovery representations | **NOT_EXECUTED / NOT_DERIVABLE** without eligible scheduled first observation by layer |
| **RQ2** — cross-layer semantic consistency/divergence | Retained Zenodo family/version, ORCID grouping/source and OpenAlex/OpenAIRE query shape evidence | Only **historical diagnostics**; compare equivalent fields and record types, not mere strings |
| **RQ3** — directly measurable propagation latency | Release clocks and some retrieval-window receipts | **NOT_DERIVABLE** as registered latency; first observed at sampling is not backend ingestion/transition time |
| **RQ4** — aggregation recurrence | Historical groups versus source summaries, OpenAlex Work query-shape conflicts | No **prospective recurrence** can be asserted |
| **RQ5** — failures, partial, rate-limited, unresolved, correction | Retained 403/404/429, SWH anti-bot and source discrepancy/correction evidence | No scheduled **60-cell frequency** or causal attribution; diagnostic failure modes remain informative |

The [crosswalk's 12 measured-variable categories](../contract/osf-overview-crosswalk-2026-10-08.md) cover identity, layer, release timestamp, actual retrieval timestamp, state, identifier type/value, identity and source attribution, aggregation, discovery, preservation, HTTP/pagination/rate limiting, and corrections. The six registered derived outputs are **latency, order, semantic consistency, aggregation recurrence, state-transition sequences, and failure/partial frequency**. Their existence as plans/schemas does **not** show they have been calculated over a prospective dataset. Preserve missing/censored/unknown and ties, do not impute.

## 5 · Coverage and evidence transparency at exact pinned tree

| Counted Git-tree property | Value | Unit interpretation |
| --- | ---: | --- |
| Dated `monitoring/YYYY-MM-DD/NN-*` directories | **40** across **21** observed date folders | Distinct diagnostic packages, not registered timepoints |
| Corresponding `evidence/YYYY-MM-DD/NN-*` directories | **14** | Companions, not additional monitoring events or source requests |
| `evidence/**/artifact-manifest.json` files | **13** | Manifest files; they cover listed public bytes, not necessarily all original HTTP bodies |
| Tracked `raw-responses.tar.gz` | **3** | Byte archives for particular captures, not full longitudinal research |
| `observations/raw/` prospective JSON records | **0** | README-only directory |
| `observations/derived/` prospective JSON records | **0** | README-only directory |

The Oct 24 [coverage calendar](../monitoring/coverage/README.md) is derived from known repository creation dates and retained source records; **empty coverage ≠ zero activity or a failed observation**. Some evidence captures have original HTTP response bytes retained locally but only public field projections in this repo. Hash checking supports integrity of stated published artifacts **only**.

## 6 · Immutable historical anomalies and corrections that must remain visible

- **Baseline identity join:** the original Codex record contained display-order mismatches; the [Oct 6 correction](../baseline/2026-10-05/correction-object-id-mapping-2026-10-06.md) keeps original raw identity and uses the canonical manifest
- **Zenodo counter grains:** version-local `version_views`, concept-family attached `views`, published page views and unique fields are not interchangeable; an older RS07 +101 discrepancy remains valid historical evidence even if later snapshots converge
- **Immutable citation drift:** Oct 10 and Oct 18 released source archives carried earlier embedded `CITATION.cff`/`codemeta.json` versions; [Oct 18 correction](../scholarly/release-identity-reconciliation-2026-10-18.md) does not rewrite old Git tags or Zenodo ZIP bytes
- **OpenAlex query conflict:** full-profile, field-selected profile and author-filtered Works-list counters have historically disagreed; neither changes nor merge of old query results can establish a platform transition without matched evidence
- **ORCID groups/summaries:** a selected flattened reader cannot recertify 17 groups/89 summaries from a different dated structured capture; group, summary, DOI and independent Work are different units
- **Software Heritage / blocked queries:** `404`, Anubis, timeout and challenge mean the **specified request path** did not yield a complete result, not that the source was never preserved
- **Supplementary institutional platforms:** RSD, RRID, RSE, WorkflowHub, HAL and pilot systems are supplementary, not silent additions to the preregistered seven operational platforms or six layers
- **OSF revision evidence:** a later OSF `date_modified` and `Updated` indicator do not prove which exact text was present on the first frozen registration version

## 7 · Explicit remaining gates / future retests

1. **Study start gate:** establish a dated, committed operational schedule **before** any claimed schedule-governed future observations; a post-event schedule cannot recreate October 14 planned timepoints. Current `schedule/` contains no concrete offsets
2. **Frozen-version comparison:** obtain the authenticated OSF initial/updated version history and clause-level diffs if available; otherwise `NOT_VERIFIED`
3. **Original evidence:** for each source-based public claim, pin exact DOI/repo/work/endpoint/query version and real acquisition clock, original public bytes or declared local retention, digest, selected-field projection, actor attribution and correction lineage
4. **Layer aggregation:** keep OpenAIRE and OpenAlex as separate vector entries under discovery; only claim layer absence when supported across its relevant contracts; no sample denominator drift
5. **Reproduction:** distinguish local replay, public artifact integrity, CI structural guard and independent scientific validation

**After-cutoff correction:** the later [October 29 diagnostic record](../monitoring/2026-10-29/01-bounded-contract-recheck/README.md) contains author-entered exact batch timestamps unsupported by retained clock receipts. See its explicit [clock-provenance correction](../monitoring/2026-10-29/01-bounded-contract-recheck/clock-provenance-correction.md). This correction is not a new Oct 28 event.

## 8 · Independent reproduction recipe

From a checkout containing full history at the pinned SHA, verify:

```sh
git rev-list --count 4cacb9b617d2e0383ffca8c757e66c5a44a5a793
git ls-tree -r --name-only 4cacb9b617d2e0383ffca8c757e66c5a44a5a793 | wc -l
git ls-tree -r 4cacb9b617d2e0383ffca8c757e66c5a44a5a793
git show --no-patch --format=fuller 4cacb9b617d2e0383ffca8c757e66c5a44a5a793
python tools/check.py --mode advisory
python -B tools/check_record_paths.py
```

Expected Git history/tree counts are **87 / 437**. The commands are reproducibility **instructions**; this audit used the authorized GitHub connector, and **did not claim a local full Git checkout executed**. Current `main` checker results are post-cutoff software verification and cannot prove the original OSF revision or historical platform-source state.

## 9 · Future OSF project-service transition (not historical source reconstruction)

OSF's [official transition guide](https://help.osf.io/article/768-osf-projects-transition-registration-questions-and-use-cases) says existing associated Projects become read-only on **2027-02-19**, while Registrations continue independently. This is a **future workspace maintenance watch** only. It neither changes the Oct 5 frozen research contract nor authorizes new observations, project migration, DOI reminting or amendment.
