# 十仓研究软件身份传播原始记录

记录日期：2026-10-06，Asia/Shanghai

本轮采集时间：2026-10-06T00:33:54+08:00 前后

记录范围：2026-10-06 之前已经发生并能在本轮通过公开 API、既有冻结证据或用户提供页面复核的数据

本文件是新增时间点记录，不回写或覆盖 2026-10-03、2026-10-04、2026-10-05 历史快照

## 一、当前结论

截至本轮采集：

- 固定研究样本仍为十个研究软件家族
- 十仓共有 10 个 Concept DOI 与 30 个 Version DOI，合计 40 个 DOI
- OpenAlex Works 查询与用户页面均显示 40 条，全部为 `software`，Open Access 为 100%
- 十个 2026-10-04 最新版本 DOI 已全部进入 OpenAlex
- 十个 2026-10-04 最新版本 DOI 已全部进入 OpenAIRE，类型均为 `software`，状态均为 `UNDER_CURATION`
- OpenAlex 作者对象 `A5151904252` 的 `works_count` 仍为 30，作者对象更新时间停在 2026-10-01，与当前 40 条 Works 集合不同步
- ORCID 当前为 12 个作品组与 54 条来源摘要
- 十仓本体仍占 10 个作品组与 52 条来源摘要
- 新增两组分别是 OSF 正式注册和研究伴随仓 Beta 版本
- OSF 注册、DataCite DOI、ORCID 作品组与 Internet Archive 副本已形成
- 研究伴随仓已形成 GitHub、Zenodo、DataCite、OpenAIRE、ORCID 链路，但没有进入固定十仓样本
- Software Heritage 的十月最新版本内容同一性尚未完成十仓全量复核，不能记录为 10／10 或 60／60 完全验证

## 二、对象与计数总账

| 范围 | 数量 | 定义 |
|---|---:|---|
| 固定研究软件家族 | 10 | RS01–RS10，不含研究伴随仓 |
| 十仓 Concept DOI | 10 | 每个软件家族一个聚合入口 |
| 十仓 Version DOI | 30 | 每仓三个真实发行版本 |
| 十仓 DOI | 40 | 10 Concept + 30 Version |
| OpenAlex Works | 40 | 十仓 40 枚 DOI 全部有独立 Work 表示 |
| OpenAIRE 最新版本命中 | 10 | 十仓 2026-10-04 版本逐 DOI 命中 |
| ORCID 作品组 | 12 | 十仓 10 + OSF 注册 1 + 伴随仓 1 |
| ORCID 来源摘要 | 54 | DataCite 33 + OpenAIRE 11 + 作者 10 |
| OSF 注册 DOI | 1 | `10.17605/OSF.IO/5B329` |
| 研究伴随仓 DOI | 2 | 1 Concept + 1 Beta Version |
| 本记录覆盖的相关 DOI | 43 | 十仓 40 + OSF 1 + 伴随仓 2 |

## 三、十仓四十 DOI 映射

| 编号 | 仓库 | Concept DOI | 初始版本 DOI | 2026-09-30 版本 DOI | 2026-10-04 最新版本 DOI |
|---|---|---|---|---|---|
| RS01 | welcome-to-github | `10.5281/zenodo.22790907` | `10.5281/zenodo.22790908` | `10.5281/zenodo.23068145` | `10.5281/zenodo.23137203` |
| RS02 | zero-entropy-lab | `10.5281/zenodo.22791081` | `10.5281/zenodo.22791082` | `10.5281/zenodo.23068144` | `10.5281/zenodo.23137204` |
| RS03 | Axiom-0 | `10.5281/zenodo.22791103` | `10.5281/zenodo.22791104` | `10.5281/zenodo.23068261` | `10.5281/zenodo.23137205` |
| RS04 | reflective-continuum | `10.5281/zenodo.22791141` | `10.5281/zenodo.22791142` | `10.5281/zenodo.23068260` | `10.5281/zenodo.23137206` |
| RS05 | agent-foundations | `10.5281/zenodo.22791169` | `10.5281/zenodo.22791170` | `10.5281/zenodo.23068262` | `10.5281/zenodo.23137207` |
| RS06 | china-agentic-observatory | `10.5281/zenodo.22791309` | `10.5281/zenodo.22791310` | `10.5281/zenodo.23068347` | `10.5281/zenodo.23137211` |
| RS07 | agentic-frontier-observatory | `10.5281/zenodo.22791334` | `10.5281/zenodo.22791335` | `10.5281/zenodo.23068352` | `10.5281/zenodo.23137214` |
| RS08 | sci-render-kit | `10.5281/zenodo.22791375` | `10.5281/zenodo.22791376` | `10.5281/zenodo.23068472` | `10.5281/zenodo.23137219` |
| RS09 | auto-doc-engine | `10.5281/zenodo.22791404` | `10.5281/zenodo.22791405` | `10.5281/zenodo.23068471` | `10.5281/zenodo.23137215` |
| RS10 | epistemic-pipeline | `10.5281/zenodo.22791463` | `10.5281/zenodo.22791464` | `10.5281/zenodo.23068494` | `10.5281/zenodo.23137216` |

十仓统一最新发行名：`v2026.10-open-research-production-framework`

## 四、十仓最新版本逐仓传播状态

| 仓库 | 最新版本 DOI | OpenAlex Work | OpenAIRE | OpenAIRE 类型 | OpenAIRE 状态 |
|---|---|---|---|---|---|
| welcome-to-github | `10.5281/zenodo.23137203` | `W7219674182` | 命中 1 条 | software | UNDER_CURATION |
| Zero-Entropy Lab | `10.5281/zenodo.23137204` | `W7219850859` | 命中 1 条 | software | UNDER_CURATION |
| Axiom-0 | `10.5281/zenodo.23137205` | `W7219917759` | 命中 1 条 | software | UNDER_CURATION |
| Reflective Continuum | `10.5281/zenodo.23137206` | `W7219566156` | 命中 1 条 | software | UNDER_CURATION |
| Agent Foundations | `10.5281/zenodo.23137207` | `W7219738811` | 命中 1 条 | software | UNDER_CURATION |
| China Agentic Observatory | `10.5281/zenodo.23137211` | `W7219788805` | 命中 1 条 | software | UNDER_CURATION |
| Agentic Frontier Observatory | `10.5281/zenodo.23137214` | `W7219897209` | 命中 1 条 | software | UNDER_CURATION |
| sci-render-kit | `10.5281/zenodo.23137219` | `W7219708281` | 命中 1 条 | software | UNDER_CURATION |
| auto-doc-engine | `10.5281/zenodo.23137215` | `W7219899314` | 命中 1 条 | software | UNDER_CURATION |
| Epistemic Pipeline | `10.5281/zenodo.23137216` | `W7219690058` | 命中 1 条 | software | UNDER_CURATION |

OpenAlex 十个最新 Work 的共同更新时间：`2026-10-05T09:50:58.205359`

OpenAlex 十个最新 Work 的共同 `indexed_in`：`datacite`

## 五、OpenAlex 当前内部不同步

本轮同时观察到：

```text
Works endpoint count = 40
OpenAlex website work list = 40
Author entity works_count = 30
Author entity updated_date = 2026-10-01T12:39:15
```

这说明作品集合已经接收十个 2026-10-04 最新版本，但作者对象摘要字段尚未同步刷新

该差异记录为同一平台内部的缓存或派生字段更新延迟，不把 `works_count=30` 解释为十个最新版本缺失

用户提供的 OpenAlex 页面状态：

```text
Works = 40
Publication Year 2026 = 40
Open Access = 100%
Type software = 40
```

用户页面显示的 Topic 计数：

```text
Scientific Computing and Data Management = 4
Software Engineering Research = 1
Multi-Agent Systems and Negotiation = 1
Ethics and Social Impacts of AI = 1
Security and Verification in Computing = 1
```

Topic 页面计数不等于十仓 canonical positioning，也不用于修改仓库类型

## 六、ORCID 当前结构

公共 Works API 当前返回：

```text
work groups = 12
work summaries = 54
```

来源分布：

| 来源 | 标识 | 条目数 |
|---|---|---:|
| DataCite | `0000-0001-8099-6984` | 33 |
| OpenAIRE | `APP-IN0O56SBVVTB7NN4` | 11 |
| Xuanyi Jiang | `0009-0001-3617-0832` | 10 |

十仓软件组仍为：

```text
10 work groups
52 work summaries
DataCite 32
OpenAIRE 10
Author 10
```

新增两组：

| 标题 | 类型 | 来源 | DOI |
|---|---|---|---|
| Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures | other | DataCite | `10.17605/osf.io/5b329` |
| lostlight530/research-software-identity-audit: Beta— Research Runtime Bootstrap | software | OpenAIRE | `10.5281/zenodo.23166491` |

54 条来源摘要不是 54 个独立作品，12 个作品组也不是 12 个固定研究样本

## 七、OSF 正式注册记录

| 字段 | 值 |
|---|---|
| 标题 | Longitudinal Audit of Research Software Identity Propagation Across Open Scholarly Infrastructures |
| OSF 注册 | `https://osf.io/5b329/overview` |
| DOI | `10.17605/OSF.IO/5B329` |
| Associated Project | `https://osf.io/wa5v8` |
| 作者 | Xuanyi Jiang |
| ORCID | `0009-0001-3617-0832` |
| DataCite resourceType | Pre-registration |
| DataCite resourceTypeGeneral | StudyRegistration |
| 许可 | CC BY 4.0 |
| Internet Archive | `https://archive.org/details/osf-registrations-5b329-v1` |

已核时间线：

| 事件 | 北京时间 |
|---|---|
| OSF registration frozen | 2026-10-05 22:04:13 |
| DataCite DOI created | 2026-10-05 22:05:58 |
| DataCite DOI registered | 2026-10-05 22:05:59 |
| Internet Archive added | 约 2026-10-05 22:08:25 |

本轮发现状态：

| 设施 | 状态 |
|---|---|
| OSF | 已公开 |
| DataCite | 已注册 |
| ORCID | 已形成独立作品组 |
| Internet Archive | 已形成公开副本 |
| OpenAIRE | DOI 查询 0 条 |
| OpenAlex | DOI 查询返回 404 |

## 八、研究伴随仓记录

仓库：`https://github.com/lostlight530/research-software-identity-audit`

仓库边界：研究协议、schema、观测、证据、来源与分析的执行载体，不属于固定十仓样本

GitHub 创建时间：`2026-10-05T14:59:45Z`，即北京时间 2026-10-05 22:59:45

Zenodo 与 DataCite：

| 字段 | 值 |
|---|---|
| Concept DOI | `10.5281/zenodo.23166490` |
| Beta Version DOI | `10.5281/zenodo.23166491` |
| Version | beta |
| Zenodo 创建时间 | 2026-10-05 23:45:49，北京时间 |
| DataCite created | 2026-10-05 23:45:50，北京时间 |
| DataCite registered | 2026-10-05 23:45:50，北京时间 |
| 文件大小 | 23,857 bytes |
| MD5 | `fe987a5fed8d0fb8aa543dfc9105fd72` |

传播状态：

| 设施 | 状态 |
|---|---|
| GitHub | 已公开 |
| Zenodo | 已发布 |
| DataCite | Concept 与 Beta Version 均已注册 |
| OpenAIRE | Beta Version 命中 1 条，software，UNDER_CURATION |
| ORCID | 已形成一个软件作品组，来源为 OpenAIRE |
| OpenAlex | Beta Version DOI 查询返回 404 |

DataCite 中该伴随仓 creator 为 `lostlight530`，当前没有 ORCID nameIdentifier，因此按 ORCID 查询 DataCite 得到的 40 条只覆盖固定十仓，不包含伴随仓两枚 DOI

## 九、Zenodo 十仓当前统计与文件信息

**时间口径补注：本轮统计采集于 2026-10-06T00:33:54+08:00 前后；当前十个最新版本发布于 2026-10-04 21:00—21:01（Asia/Shanghai）。以下实时统计属于 2026-10-06 本轮采集时点，不倒写为 2026-10-04 发布时刻统计。**

字段定义：

- `views` 与 `downloads` 是软件家族累计值
- `unique_views` 与 `unique_downloads` 是相应累计唯一计数
- `version_views` 与 `version_downloads` 是当前 2026-10-04 版本记录的计数
- 十个 2026-10-04 最新版本本轮合计 `version_unique_views = 13`；逐仓值未在本表展开
- 实时统计会变化，必须和采集时间一起使用

| 仓库 | Record | views | unique views | version views | downloads | unique downloads | version downloads | Bytes | MD5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| welcome-to-github | 23137203 | 78 | 76 | 0 | 4 | 3 | 0 | 11,095,238 | `d2283b879c6d25563e63ddeb1ed6be1f` |
| Zero-Entropy Lab | 23137204 | 54 | 50 | 5 | 0 | 0 | 0 | 12,728,661 | `c37e31b66de62e49abec7062675a95ff` |
| Axiom-0 | 23137205 | 75 | 71 | 2 | 0 | 0 | 0 | 896,794 | `c8d389bca1267da645e4421f37c9fe28` |
| Reflective Continuum | 23137206 | 38 | 37 | 0 | 0 | 0 | 0 | 645,244 | `5473247d7d47712ad47e30318750d383` |
| Agent Foundations | 23137207 | 63 | 58 | 1 | 1 | 1 | 0 | 1,140,108 | `e1249d15935e916f5f990ee0df4febbd` |
| China Agentic Observatory | 23137211 | 62 | 59 | 3 | 0 | 0 | 0 | 751,981 | `963e6ef5b3f41a87bdbf2a4fb1420b3a` |
| Agentic Frontier Observatory | 23137214 | 65 | 61 | 0 | 1 | 1 | 0 | 718,863 | `1389072888492917df227a8991c53b3e` |
| sci-render-kit | 23137219 | 50 | 50 | 1 | 1 | 1 | 0 | 405,188 | `458665b81bf9db3be1bb33da52b69427` |
| auto-doc-engine | 23137215 | 39 | 38 | 2 | 0 | 0 | 0 | 483,651 | `d1df434fbd7e03b6ec7af08ea8378248` |
| Epistemic Pipeline | 23137216 | 57 | 56 | 1 | 0 | 0 | 0 | 417,127 | `726213c9129422f39aa131cad65b5c68` |
| **合计** |  | **581** | **556** | **15** | **7** | **6** | **0** |  |  |

本轮准确总量口径：家族累计 `views=581`、`unique_views=556`、`downloads=7`、`unique_downloads=6`；2026-10-04 最新十版本合计 `version_views=15`、`version_unique_views=13`、`version_downloads=0`。

China Agentic Observatory 的正确文件值以本表为准，旧生成文本中的 `732,840 bytes` 与 `73a11f23783a48e71bd973a9856bf891` 不采用

## 十、Software Heritage 当前证据边界

2026-10-05 正式补充证据记录的本轮覆盖：

| 状态 | 数量 | 对象 |
|---|---:|---|
| 完整复核 | 2 | welcome-to-github、Axiom-0 |
| 部分复核 | 1 | epistemic-pipeline |
| HTTP 429 后停止同域继续请求 | 2 | reflective-continuum、agent-foundations |
| 本轮未请求 | 5 | auto-doc-engine、sci-render-kit、china-agentic-observatory、agentic-frontier-observatory、zero-entropy-lab |

当时明确记录：

```text
latest_october_version_content_identity = NOT_VERIFIED
```

因此本记录不建立十仓最新版本 SWHID 总表，不宣称十仓十月包全部冻结，不宣称 60／60 fully verified

旧生成文本中的 `swh:1:snp:china-obs-baseline` 不是合法散列形式，不作为证据

## 十一、平台分层

本轮开始将 OpenAIRE 和 OpenAlex 分开记录，不再合并成一个发现层

固定十仓后续观测层：

```text
GitHub
Zenodo
DataCite
ORCID
Software Heritage
OpenAIRE
OpenAlex
```

固定网格因此为 `10 × 7 = 70` 个平台观测单元

OSF 注册和研究伴随仓属于研究设施与研究对象外围记录，不进入固定十仓分母

## 十二、状态解释规则

| 观察结果 | 允许解释 |
|---|---|
| HTTP 200 且返回匹配记录 | 本次查询观察到记录 |
| HTTP 404 | 本次指定查询没有找到记录 |
| 空结果集 | 本次查询条件下没有返回匹配记录 |
| HTTP 403 | 请求被拒绝，原因需要结合响应内容判断 |
| HTTP 429 | 明确受到速率限制 |
| UNDER_CURATION | OpenAIRE 已有记录，仍处于其处理状态 |
| DOI 已注册 | 标识符和元数据登记完成 |
| ORCID 有来源摘要 | 作者记录中存在对应来源声明 |
| OpenAlex 有 Work | 发现图谱已经建立对应表示 |
| SWH 有 visit／snapshot | 仅证明被实际查询到的归档访问和快照 |

404 或空数组不直接证明对象脱网，DOI、来源摘要、归档快照和图谱记录也不证明软件正确性或科学结论真实

## 十三、复核端点

```text
DataCite 十仓 DOI
https://api.datacite.org/dois?query=creators.nameIdentifiers.nameIdentifier:0009-0001-3617-0832&page[size]=100

ORCID Works
https://pub.orcid.org/v3.0/0009-0001-3617-0832/works

OpenAlex 作者 Works
https://api.openalex.org/works?filter=author.orcid:0009-0001-3617-0832&per-page=100

OpenAlex 作者对象
https://api.openalex.org/authors/https://orcid.org/0009-0001-3617-0832

OpenAlex 单 DOI
https://api.openalex.org/works/https://doi.org/{DOI}

OpenAIRE 单 DOI
https://api.openaire.eu/search/researchProducts?doi={DOI}&format=json

Zenodo 单记录
https://zenodo.org/api/records/{record_id}

OSF 注册
https://osf.io/5b329/overview

Internet Archive 注册副本
https://archive.org/details/osf-registrations-5b329-v1
```

## 十四、来源等级

### 本轮亲自通过公开 API 复核

- DataCite 十仓 40 DOI
- DataCite OSF 注册 DOI
- DataCite 研究伴随仓 Concept 与 Beta DOI
- ORCID 12 组、54 条来源摘要及来源分布
- OpenAlex 十仓 40 Works
- OpenAlex 十个最新版本 DOI
- OpenAlex 作者对象旧 `works_count=30`
- OpenAIRE 十个最新版本 DOI
- OpenAIRE 研究伴随仓 Beta DOI
- OpenAIRE 未找到 OSF 注册 DOI
- Zenodo 十个最新记录文件字段与实时统计
- Zenodo 研究伴随仓 Beta 记录
- GitHub 十仓与研究伴随仓公开元数据

### 用户提供并由当前 API 结果支持

- OpenAlex 网页显示 40 Works
- Open Access 100%
- Type software 40
- 页面 Topic 计数

### 历史冻结证据

- 2026-10-03 与 2026-10-04 Software Heritage 复核范围
- 十仓合并、发行、DataCite 注册和 ORCID 通知时间线
- 2026-10-05 三篇稿件和统一补充数据

## 十五、不得写入基线的说法

- `60 / 60 fully_verified`
- `FailureRate = 0%`
- 十仓十月 Software Heritage 内容全部完成复核
- OpenAlex 与 OpenAIRE 是同一个观察层
- 404 证明对象不存在或脱网
- 403 必然是限流
- 54 条 ORCID 摘要等于 54 个作品
- 40 条 OpenAlex Works 等于 40 个软件家族
- 研究伴随仓是第十一个固定样本
- 实时 Zenodo 统计可以倒写成没有原始响应的历史时刻值

## 十六、当前可用基线

```yaml
observation_date: 2026-10-06
timezone: Asia/Shanghai
fixed_corpus_objects: 10
fixed_corpus_concept_dois: 10
fixed_corpus_version_dois: 30
fixed_corpus_total_dois: 40
openalex_work_records: 40
openalex_latest_versions_found: 10
openaire_latest_versions_found: 10
orcid_work_groups_total: 12
orcid_work_summaries_total: 54
orcid_fixed_corpus_groups: 10
orcid_fixed_corpus_summaries: 52
osf_registration_doi: 10.17605/OSF.IO/5B329
companion_repository_concept_doi: 10.5281/zenodo.23166490
companion_repository_version_doi: 10.5281/zenodo.23166491
software_heritage_october_content_identity: NOT_VERIFIED
```