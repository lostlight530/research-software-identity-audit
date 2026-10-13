# 第 11 仓研究控制基础设施独立复核 — 2026-10-13 中午

**复核对象：** `lostlight530/research-software-identity-audit` 一个仓库。本仓是研究协议、证据、provenance 和 analysis runtime，**永远不是 RS11**。本次未修改 RS01–RS10、冻结 OSF registration、历史 baseline、schema、operational schedule，也不是 prospective 观测。

**真实取数时间：** 2026-10-13 **12:47:55.192–12:51:01.217 Asia/Shanghai**，即 **2026-10-13T04:47:55.192Z–04:51:01.217Z**。这是包含多个独立请求的**最外层批次起止时间**，不是声称每一个 HTTP 请求恰好在该时间开始/完成，更不是“12:00:00 整”的历史快照。实测发生在 12 点时段，后续整理、校验、GitHub PR/CI/merge 则是**更晚**的仓库维护活动，不得倒填为实测时间。

## 证据目录与复现入口

- [platform-attempts.csv](platform-attempts.csv)：**37 个**独立端点/仓库检查的来源定位符、结果状态、短值与精确外层请求时间窗，包括连接器不支持、非 JSON、受挑战的合法失败结果。记录行表示检查活动，不是 37 个 preregistered 分析单元或 37 个成功 HTTP 200 响应
- [zenodo-version-attempts.csv](zenodo-version-attempts.csv)：Zenodo 三个版本 **3 次直接请求成组**，共 9 行原字段摘录，**保留首轮不一致**与两次后来收敛的取数窗口、URL、八项统计字段
- [record.yaml](record.yaml)：界定本次实际范围、状态、来源与边界的机器可读摘要
- GitHub 的 [初始 main](https://github.com/lostlight530/research-software-identity-audit/commit/de45b364050c7f4916484cb1226a80567f022426) 为复核的代码状态与数据合同基准
- [2026-10-12 上一次控制仓复核](../../../scholarly/control-repository-review-2026-10-12.md) 与 [2026-10-11 Zenodo 33-version 复核](../../2026-10-11/01-zenodo-33-version-recheck/verification.md) 保持原始身份，不覆盖日期、数值或 provenance

**证据级别：** GitHub 授权连接器执行只读 GET 并返回源码/元数据；外部 API 使用公开内容提取器要求 live fetch，获得可解析 JSON 或呈现的文本，**未得到字节原样 HTTP 响应、单请求服务器 Date/Headers、响应原始 SHA-256**。外部平台的 `registered`/`updated_date` 是平台声明的**对象字段**，不是本轮请求完成时间，也不是独立观测到的首次索引时间。对 nonce 的使用不保证穿过所有缓存。不要把这些派生摘录冒充带哈希的原始 HTTP 档案。

## 真实请求分组时间（北京时间及 UTC）

| 取证步骤 | UTC 外层窗口 | 北京时间窗口 | 范围与结果 |
| --- | --- | --- | --- |
| GitHub fresh main、open PR、发布、main CI 与文件树 | 04:47:55.192–04:47:57.029 | 12:47:55.192–12:47:57.029 | main `de45b364...`；open PR **0**；3 Release；对应 main CI **SUCCESS** |
| GitHub 14 个关键合同、引用元数据、baseline、schedule 文件 | 04:48:21.352–04:48:24.702 | 12:48:21.352–12:48:24.702 | 源码逐项读到，全部 10 个固定样本与 6/7 层级边界保留 |
| 核心 Zenodo、DataCite、OpenAIRE、OpenAlex、ORCID、SWH、RSD、RRID、OSF 公开请求 | 04:48:47.388–04:48:51.310 | 12:48:47.388–12:48:51.310 | 有成功、非 JSON 及 challenge，见请求台账 |
| 三个新 WorkflowHub DOI 的 DataCite/OpenAlex 双重核验与控制仓三个 Zenodo 版本首次直接取数 | 04:49:35.646–04:49:40.185 | 12:49:35.646–12:49:40.185 | 三个 DOI 已注册且关联同一 ORCID；**Zenodo 初次计数不一致** |
| Zenodo 两轮独立 nonce、全族搜索和 family `/versions` | 04:50:02.337–04:50:07.311 | 12:50:02.337–12:50:07.311 | **两轮均全族相符**，保留首次异常 |
| GitHub traffic views/clones 只读尝试 | 04:50:40.056–04:50:40.451 | 12:50:40.056–12:50:40.451 | 连接器 `INVALID_ARGUMENT` 拒绝该 URL 家族，**无流量数据** |
| OpenAIRE 全三个版本 DOI 与概念 DOI 分开精确复核 | 04:50:59.795–04:51:01.217 | 12:50:59.795–12:51:01.217 | 三版本 PID 各命中 1；Concept PID 命中 0 |

以上每组的日期都是 **2026-10-13**；不可把北京时间和 UTC 日期混用。每个请求具体 URL、时间窗与状态以 [platform-attempts.csv](platform-attempts.csv) 为准。

## 1. GitHub、元数据与冻结研究边界

- [控制仓](https://github.com/lostlight530/research-software-identity-audit) initial main SHA = `de45b364050c7f4916484cb1226a80567f022426`，最新已发布 GitHub Release **`v2026.10-evidence-reconciliation`**，历史 `beta` 和 `v2026.10-initial-research-runtime` 仍存在，**本轮没有建立 Release/Tag/DOI**
- 现行 main `CITATION.cff` 正确指向版本 `v2026.10-evidence-reconciliation`、version DOI `10.5281/zenodo.23284570`、release date 2026-10-10、`lightlost`、ORCID、MIT；`codemeta.json` version/date 一致，`identifier` 指向**全族 Concept DOI** `10.5281/zenodo.23166490`，这是不同语义而非冲突；`.zenodo.json` 创作者、OSF `isSupplementTo` 和 MIT 一致
- 发布于 10 月 10 日的**不可变 Tag 内部** CFF/CodeMeta 依然保留旧 10 月 6 日版信息。此前 PR #34 只修了后续 main，并在 [RELEASE_POLICY.md](../../../RELEASE_POLICY.md) 留痕；该归档内容**没有且不应被追写**
- [固定 manifest](../../../corpus/object-manifest.csv) 仍恰好 **RS01–RS10**；[六层 schema](../../../schema/infrastructure-layers.yaml) 和七个平台 `platforms.yaml` 未改：**10×6=60** 个 preregistered units、**10×7=70** possible object×platform checks
- [OSF preregistration](../../../contract/preregistration.md) 是 frozen contract；[baseline](../../../baseline/2026-10-05/manifest.yaml) 截止 `2026-10-05T23:59:59+08:00`，不能倒填 live 查询；[schedule](../../../schedule/README.md) 仍未声明具体 operational offsets。本次**没有重新独立检查十个研究样本仓库的 eligible release 列表**，因此**不声称**由本次观测证明十仓无新发布
- GitHub traffic `views` 与 `clones` 接口被当前 authorized fetch 连接器以 `INVALID_ARGUMENT` 阻断；这是**连接器 API 不支持**，不代表仓库无浏览或克隆，也未试图通过其它凭据绕过

## 2. Zenodo 三版本——必须保留首轮不一致

控制仓 Concept `23166490`，三个 version record IDs：`23166491` beta、`23176748` initial-runtime、`23284570` evidence-reconciliation。这些都是**控制软件版本，不是 RS11**。

**12:49:35–12:49:40 第一次直接分别读取（原样字段摘录）**：

| Record | attached `views` / `unique_views` / `downloads` | `version_views` / `version_downloads` |
| --- | ---: | ---: |
| beta `23166491` | **91 / 87 / 3** | **21 / 0** |
| initial `23176748` | **51 / 49 / 0** | **32 / 0** |
| newest `23284570` | **74 / 71 / 3** | **0 / 0** |

由这些首次直接响应得到版本浏览量局部合计 `21+32+0=53`、版本下载 `0+0+0=0`，与任一统一的家族浏览、下载状态**不一致**。研究状态为 `INITIAL_FAMILY_AGGREGATE_CONFLICT`，不能直接采用 91、51、74 任一单条家族字段作为全族权威状态；也不能把这种不一致解释为统计下降、访问来源或已知缓存机制。

**12:50:02–12:50:07 后续独立同窗交叉读**：

- 3 个版本各自的两轮 nonce 直接读取 **都返回一致字段**：`version_views = 21 / 54 / 16`，`version_downloads = 0 / 3 / 0`
- 3 个版本附带的 `stats.views=91`、`unique_views=87`、`downloads=3`、`unique_downloads=3` **全部相同**
- 全族 `GET /api/records?q=conceptrecid:23166490&all_versions=true` 和独立 `GET /api/records/23284570/versions?allversions=true` **均枚举到相同 3 IDs**，且其版本字段对齐
- 求和严格通过 `21 + 54 + 16 = 91`、`0+3+0=3`，所以**后续时间窗**的状态为 `LATER_CROSS_ENDPOINT_FAMILY_MATCHED`
- 相对 10 月 12 日独立留存的**最新版本记录附带家族值** `74 / 71 unique / 3 downloads`，此次后续一致值是 `91 / 87 unique / 3 downloads`，差额为 **+17 views / +16 unique-views 计数 / +0 downloads**，**不是 17 位新增独立人类访问者**。该差额只是不同时间的字段比较，不是逐请求事件来源分析

**关键解释边界：** 首轮的 `51/74/91` 冲突**真的在这次提取接口中出现**，后两轮收敛也**真的出现**。不据此宣称内部数据库、CDN、索引或缓存的确定性机制，也不隐去原始失败/不一致。抓取层未公开源 HTTP header、raw bytes；nonce 不保证 cache bypass。即使本次后来计数匹配，也不回写 Oct10、Oct11、Oct12 旧 snapshot。

## 3. 七个平台逐项判定

| 核心 operational platform | 本次控制仓的独立观测 | 裁定 |
| --- | --- | --- |
| GitHub | main、Release、PR、CI、14 文件源码合同已核；traffic API connector 拒绝 | `REPOSITORY_VERIFIED / TRAFFIC_UNAVAILABLE` |
| Zenodo | 3 版本身份确认，**初轮字段分裂，后两轮与全族端点一致 91/87/3** | `LATER_MATCHED_AFTER_INITIAL_CONFLICT`，机制未知 |
| DataCite | 新版 DOI `10.5281/zenodo.23284570` 已注册并指向 `IsVersionOf` 概念 DOI；**Concept DOI `HasVersion` 仍仅列两条**，其元数据 `updated=2026-10-06T02:48:22Z` | `VERSION_VALID / CONCEPT_REVERSE_RELATION_PARTIAL` |
| ORCID | 公开 `/works` 返回展平文本，可见控制仓新版 DOI `23284570`；不具备结构化 groups/summaries 可复算 JSON | `PUBLIC_TEXT_ONLY / GROUP_COUNT_UNRESOLVED` |
| Software Heritage | 控制仓 GitHub origin 访问 API 返回 Anubis challenge；Zenodo concept origin 返回 HTML 导航而非 JSON visit 列表 | `ACCESS_CHALLENGED / VISITS_NOT_VERIFIED` |
| OpenAIRE Graph v1 | 精确 `pid` 查询 beta / initial / latest 三个**版本 DOI 各 `numFound=1`**；Concept DOI `23166490` 的同一 exact PID 查询 `numFound=0` | `VERSION_DOIS_OBSERVABLE / CONCEPT_QUERY_ZERO` |
| OpenAlex | `author.id=A5151904252` filtered Works **24 条**，返回行均含该作者；控制仓 Concept Work `W7220365356` 与最新版本 Work `W7221337741` 均可观察；selected profile `works_count=21` vs full profile `works_count=30`，其各自更新时间不同 | `AUTHOR_QUERY_24 / PROFILE_FIELD_CONFLICT` |

OpenAIRE 概念 PID 查询 0、DataCite HasVersion 缺第三条和 SWH 挑战，都不是“研究软件整体不存在”的证据。

## 4. OpenAlex 新增三个相关 DOI 的独立验证

这部分是**作者身份发现图谱的补充解释**，不是允许把相关 WorkflowHub 对象写成第 11、12、13 个研究样本。

此前 10 月 12 日留存的同类 author-filtered Works 为 **21**；今天 12:48 独立列表返回 **24**，并通过逐 Work endpoint 和 DataCite DOI 元数据完成以下 3 条交叉核对：

| 相关 DOI | OpenAlex Work ID | DataCite `registered` (UTC) |
| --- | --- | --- |
| `10.48546/workflowhub.workflow.2332.5` | `W7221441548` | `2026-10-11T14:54:21Z` |
| `10.48546/workflowhub.workflow.2334.5` | `W7221460162` | `2026-10-11T14:54:17Z` |
| `10.48546/workflowhub.workflow.2337.1` | `W7221455900` | `2026-10-11T14:54:13Z` |

三条都在 DataCite 返回 creator `Jiang, Xuanyi` 和 canonical ORCID `0009-0001-3617-0832`，OpenAlex 对应 Work 的 author 也是 `A5151904252` / 同一 ORCID，类型均为 `other`。三条 Work 自报 `updated_date=2026-10-12T09:40:04.860316`，这是 **platform field update**，不作为实际首次索引/传播延迟测量。

结合上次独立对照的 53 个**已知 DOI 身份清单**，这 3 个新增确认的身份使列表至少达到 **56 个已知 DOI**。这**不是** 56 DOI 全平台实时普查、不是 56 个独立科研对象，也不保证没有其它未发现的 DOI。新增 workflow `2337.1` 亦不能仅凭发现记录声称其 WorkflowHub API 内容已经成功复核：本轮 `/workflows/2337.json` 在提取器里返回 `fetch_error`（上游提示 200，content null），保留失败。

OpenAlex 的 `24` 是列表查询结果，`21` 是 **field-selected 作者档案**自报 `works_count`（`updated_date=2026-10-11T12:31:35`），`30` 是 **unselected/full 作者档案**返回的另一个旧更新时间（`2026-10-01T12:39:15`）。不同路径的计数和更新时间**真实不一致，根因 UNKNOWN**，不能混成单一“真实总数”。

## 5. 附加公共身份入口

- RSD 公开 API 返回研究控制仓**一条 `is_published=true` 软件记录**，Concept DOI 与 Zenodo 一致；项目是否收录更多样本不是本次控制仓的结论
- SciCrunch 官方 `SCR_029105` Resource Report 可读，标题、URL 正确；`Claim ownership` UI 提示不等于已证实 ownership 或 curator 完成
- OSF `/v2/registrations/5b329/` 在提取器中呈现混入 endpoint 文档的**非原生结构化 JSON**，所以本次不声称完成新的 OSF registration-state JSON 对账。DataCite `10.17605/osf.io/5b329` 存在，原有非规范 extra identifier `my-orcid?orcid=0009-0001-3617-08` 仍可观察；不要自行替 OSF 纠正官方来源或据此推断身份变化
- 没有额外注册账号、提交平台修改、索取私人流量数据或解安全质询

## 6. 明确未完成项与下一次复核触发条件

- DataCite concept `HasVersion` 仍未列出最新归档 DOI，尽管 latest version `IsVersionOf` 已正确；下次应按**相同两个 DOI 接口**复核，不能单凭本次断言同步机制
- Zenodo 一次初始版本字段冲突和后续一致读取，后续可再跑三版全量直接 GET＋全族两个枚举端点，保留失败、不一致和真实窗，不补造历史
- OpenAlex 24 / selected 21 / full 30 的 profile/list 意义和可能的数据源版本差异仍未解决；需要保留各查询形式、参数、字段、返回值
- ORCID 精确 group、SWH visits、GitHub traffic 和 OSF 真正的结构化 API 回包，因接口/提取边界不能完成，不记为 `0`
- 未执行 RS01–RS10 的新 release 普查，不新增正式 observation schedule，不启动 prospective dataset。没有创建新 DOI、Tag、Release、preregistration amendment 或额外研究样本

**结论：** `CONTROL_ONLY_NOON_REVIEW_COMPLETED_WITH_OBSERVABLE_IDENTITY_LINKS_AND_RETAINED_FAILURES`；`ZENODO_INITIAL_FIELD_CONFLICT_LATER_MATCHED`；`DATACITE_CONCEPT_RELATION_PARTIAL`；`OPENAIRE_VERSION_PIDS_VISIBLE`；`OPENALEX_AUTHOR_FILTERED_WORKS_24_WITH_PROFILE_CONFLICT`。本次独立复核完成的是**允许明确失败/未知的、有时间边界的控制仓诊断**，不是所有外部平台都成功的一张绿色通过证明。
