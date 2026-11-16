# Initial baseline

## 中文专业对应与范围 / Chinese subject counterpart and scope

**实质研究对象 / Exact subject:** 最初历史基线应固定到原截点，后来的来源恢复与 correction 不能倒填成当时的实时采集

**English owning title:** Initial baseline

**单位与版本 / Unit and version:** 读者需要同时确认 RS01–RS10、六层与七具体平台的不同口径，以及原始研究、版本化软件发行、实时外部平台数据的独立身份，任何未知保持未核实 / Keep distinct denominators, exact release identity, observation clocks, unknown source responses and the frozen preregistered boundary

| English original section / 原文章节 | 中文定位 / Chinese mapping |
| --- | --- |
| Boundary | 对应的受限研究过程与原始记录 |
| Current baseline cutoff | 对应的受限研究过程与原始记录 |
| Immutability rule | 不可改写规则 |

**历史不回写 / Non-retroactivity:** 此语言补充不改变原始 OSF、历史样本、注册版本、计数或先前失败记录 / This explanatory layer does not modify any historical observation or external registration


This directory preserves the historical/initial evidence state used to contextualize the prospective longitudinal study.

## Boundary

The frozen OSF registration requires the historical baseline to remain distinct from the prospective dataset.

Baseline material therefore:

- may describe events that occurred before the prospective window;
- may be reconciled after the fact from public APIs, frozen evidence, or previously captured pages;
- must preserve the distinction between contemporaneous capture and retrospective reconstruction;
- must not be silently rewritten to match later platform state;
- must not be counted as prospective observations.

## Current baseline cutoff

The first baseline package is organized under `2026-10-05/` and uses:

- **cutoff:** 2026-10-05T23:59:59+08:00
- **timezone:** Asia/Shanghai
- **reconciliation execution:** 2026-10-06T00:33:54+08:00 approximately
- **scope:** events/states attributable to the cutoff or earlier and supportable by public API evidence, frozen evidence, or user-supplied public pages

A live API response collected after the cutoff may verify a historical timestamp or currently visible state, but it must not be backdated into an unsupported historical platform response.

## Immutability rule

Raw reconciliation records are append-only source records.

Corrections should be recorded as new reconciliation/correction artifacts with explicit provenance rather than silently replacing historical assertions.
