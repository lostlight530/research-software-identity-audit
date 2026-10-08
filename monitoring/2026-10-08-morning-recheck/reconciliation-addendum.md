# 十仓与补充科研设施晨间复查｜2026-10-08

实际采集时间 Asia/Shanghai 2026-10-08T08:12:58.295848+08:00 至 2026-10-08T08:18:54.257041+08:00

固定十软件家族独立复查，伴随审计软件、OSF 与两个 WorkflowHub 工作流单列，记录阶段为 pre_eligibility_monitoring

## 核心结果

| 指标 | 10 月 7 日独立快照 | 本轮 10 月 8 日 | 差分 |
|---|---:|---:|---:|
| 十仓家族 views | 695 | 775 | +80 |
| 十仓家族 unique_views 求和 | 664 | 733 | +69 |
| 十仓家族 downloads | 7 | 7 | +0 |
| 十仓家族 unique_downloads 求和 | 6 | 6 | +0 |
| 当前版本 views | 54 | 70 | +16 |
| 当前版本 downloads | 0 | 0 | +0 |
| 文件元数据 size 字节求和 | 29282855 | 29282855 | +0 |
| OpenAlex 主作者列表 | 41 | 43 | +2 |
| ORCID 作品组 | 12 | 14 | +2 |
| ORCID 来源摘要 | 54 | 56 | +2 |

unique 计数是逐家族相加，不表示跨十仓去重的人数，采集时间跨度按实际请求使用

## 十仓逐项对账

| 软件 | 昨日家族 views | 本轮家族 views | 增加 | 本轮 downloads | 当前版本 views |
|---|---:|---:|---:|---:|---:|
| welcome-to-github | 90 | 98 | +8 | 4 | 4 |
| zero-entropy-lab | 66 | 75 | +9 | 0 | 10 |
| Axiom-0 | 85 | 93 | +8 | 0 | 4 |
| reflective-continuum | 44 | 52 | +8 | 0 | 2 |
| agent-foundations | 71 | 78 | +7 | 1 | 2 |
| china-agentic-observatory | 81 | 88 | +7 | 0 | 17 |
| agentic-frontier-observatory | 85 | 93 | +8 | 1 | 15 |
| sci-render-kit | 57 | 65 | +8 | 1 | 3 |
| auto-doc-engine | 52 | 59 | +7 | 0 | 7 |
| epistemic-pipeline | 64 | 74 | +10 | 0 | 6 |

十仓 GitHub 最新 release 均仍为 v2026.10-open-research-production-framework，十仓各四枚 DOI 共 40 枚逐号 findable，当前版本在 OpenAlex 10/10 可定位，OpenAIRE exact DOI 10/10 返回记录，SWH deposit snapshot → release → directory 10/10 本轮成功解析

SWH 成功解析与文件 metadata 未变分别记录，本轮未下载 ZIP 比较字节，也未运行仓库的软件测试

## OpenAlex 作者与伴随软件

主作者列表本轮返回 43 条：42 software + 1 other，40 条属于固定十仓的 concept 与三个版本，另两条是伴随审计软件 concept 与当前版本，一条是 OSF 注册

主作者资料接口 works_count 仍为 41，列表与资料汇总的差异保留；副作者资料 works_count 为 2，列表返回 1 条 Beta，未识别第二条

| 伴随对象 | OpenAlex | 作者 | Primary topic |
|---|---|---|---|
| https://doi.org/10.5281/zenodo.23166490 | W7220365356 | lightlost | Research Data Management Practices |
| https://doi.org/10.5281/zenodo.23176748 | W7220737563 | lightlost | Scientific Computing and Data Management |
| https://doi.org/10.5281/zenodo.23166491 | W7220470293 | lostlight530 | Research Data Management Practices |

主作者 topics 仍为 8，Beta cited_by_count 仍为 1，引用方向在 retained OSF Work response 核查，不当成新增外部引用

伴随审计软件 Zenodo 家族 views 47，unique_views 45，downloads 0，单列不计 RS11

## WorkflowHub 与 ORCID

两个 WorkflowHub 公开 JSON 均返回 latest_version 2，四个版本 DOI 在 DataCite 全部 findable

| DOI | 本轮 DataCite 标题 | 状态 |
|---|---|---|
| 10.48546/workflowhub.workflow.2332.1 | NEXUS CORTEX Life Cycle — welcome-to-github | findable |
| 10.48546/workflowhub.workflow.2332.2 | Title NEXUS CORTEX Life Cycle — welcome-to-github | findable |
| 10.48546/workflowhub.workflow.2334.1 | Title NEXUS CORTEX Life Cycle — zero-entropy-lab | findable |
| 10.48546/workflowhub.workflow.2334.2 | NEXUS CORTEX Life Cycle — zero-entropy-lab | findable |

四枚 WorkflowHub DOI 的 OpenAlex 单 DOI 查询均返回 404，本轮未观察到对应图谱实体，DataCite findable 与 OpenAlex 发现状态分别记录

RSE contribution PR #498 本轮仍为 open，merged=false，尚未合并

本轮 ORCID 公开记录只看到 welcome 2332.1 与 zero 2334.2 两条工作流来源摘要，welcome 2332.2 与 zero 2334.1 本轮未见，原因不从 API 缺席推断，用户先前手动清理测试项的陈述另存历史记录

ORCID 当前 14 组 / 56 摘要，DataCite 35 + OpenAIRE 11 + 作者 10；固定十仓占 10 组 / 50 摘要，其余 4 组为 OSF、伴随审计软件与两个工作流

## 补充设施与查询限制

RSD 查询返回 11 条，逐条 is_published 为 true，仍是十仓加伴随软件；HAL 按 ORCID 查询 numFound=0，本轮未观察到公开索引，不据此宣称 deposit 被拒；RRID resolver 返回 HTTP 403，当前公开解析无法验证

OSF 注册与 Internet Archive 保存副本本轮响应成功，固定软件未观察到新的 post-registration release，本轮不计正式 prospective 数据集

本轮逐号验证的 DataCite 范围为 48 枚：固定 40 + OSF 1 + 伴随 3 + 工作流 4，全部 findable，这不是作者全平台作品总数

## 采集与验收

身份链首轮 167 次请求，8 次连接超时分别作一次补查，补查及依赖目录查询 10 次全部成功，RRID 403 保留，主采集日志共 177 次，RSE 与工作流 OpenAlex 扩展另有 5 次
本轮数据检查 192 项，失败 0 项

[Public retained evidence](../../evidence/2026-10-08-morning-recheck/README.md) · [Public retained evidence](../../evidence/2026-10-08-morning-recheck/README.md) · [Public retained evidence](../../evidence/2026-10-08-morning-recheck/README.md) · [Public retained evidence](../../evidence/2026-10-08-morning-recheck/README.md)



Evidence import note: reports retain their original collection dates and local verification counts; public files are listed in [the evidence supplement](../../evidence/2026-10-08-morning-recheck/README.md)


## Cross-day notes checked against the original design

The existing baseline and monitoring notes already preserve these distinctions:

- baseline cutoff ledger 575 vs statistics actually retrieved after midnight at 581
- October 6 source-declared 09:15 snapshot 616 vs other captures at other times
- fixed-corpus 40 Software DOI identities vs author-list totals including OSF and the audit runtime
- canonical RS IDs joined by repository, with earlier source display order retained
- all three monitoring packages remain pre-eligibility records

Only the following capture remarks are added here:

1. Evidence was imported after PR #19 but retains the original per-request capture times; import time does not replace observation time
2. The earlier updater's blocked and source-reported outcomes describe that updater's access; retained collector responses now support Zenodo counter reconstruction and ORCID grouping without rewriting its history
3. Unique views use a one-hour visitor window; daily author visits can still contribute on successive days
4. Family minus current-version views increased from 641 to 705, a derived +64, while current-version views increased by 16; this is a counter distribution, not a visitor-origin measurement
5. Official statistics definition: https://support.zenodo.org/help/en-gb/4-usage-statistics/15-what-is-a-view-download-data-volume — consulted 2026-10-08, usage-metric clarification only

Rankings are not a study objective and no ranking artifacts are introduced by this supplement
Existing source-reported ranking references from the merged PR remain historical source content
