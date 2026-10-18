#!/usr/bin/env python3
"""Build the repository's paper navigation from the editable JSON catalog."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PAPERS = json.loads((ROOT/'data/papers.json').read_text())
GROUPS = json.loads((ROOT/'data/categories.json').read_text())
GROUP = {g['id']: g for g in GROUPS}


def filename(p):
    return f"Paper-{p['id']:03d}-{p['slug']}.md"


def page_link(p):
    return f"[{p['short_title']}]({filename(p)})"


def table(papers, root=False):
    rows=['| 编号 | 论文与阅读卡片 | 年份¹ | 关注的问题 | 原文 | 代码 |',
          '| --- | --- | --- | --- | --- | --- |']
    for p in papers:
        target=('wiki/' if root else '')+filename(p)
        code=f"[代码]({p['code_url']})" if p['code_url'] else '待补'
        rows.append(f"| {p['id']:02d} | [{p['short_title']}]({target}) | {p['year']} | {p['summary']} | [原文]({p['primary_url']}) | {code} |")
    return '\n'.join(rows)


def write(path, text):
    path.write_text(text.strip()+'\n')


intro='''# PKU-AFT · 量化研究论文导航

从读懂问题，到建立基线，再到可以核查的复现实验。

首版收录 **37 篇论文 · 7 个研究方向 · 17 个配套代码入口**，保留原清单编号。覆盖因子挖掘、收益预测、在线适应、组合构建、风险管理和交易执行。

**[按方向阅读](wiki/Home.md) · [37 篇完整目录](wiki/All-Papers.md) · [阅读与复现路线](wiki/Reading-Paths.md) · [复现记录规范](wiki/Reproduction-Guide.md) · [参与维护](CONTRIBUTING.md)**

首次整理：2026-10-18。卡片是简要导读，原文入口与题录已核对；**独立训练及回测尚未开展**。代码入口中的演示实现不等同于原论文完整复现。

## 从哪里开始

| 你想回答的问题 | 建议先读 |
| --- | --- |
| 怎样判断复杂模型是否有必要？ | [StockMixer](wiki/Paper-015-StockMixer.md)，先建立简单预测基线 |
| 训练标签一定要等于最终预测期限吗？ | [Label Horizon Paradox](wiki/Paper-013-Label-Horizon.md) |
| 模型如何适应市场变化？ | [DoubleAdapt](wiki/Paper-017-DoubleAdapt.md) 与 [DSOF](wiki/Paper-019-DSOF.md) |
| 如何自动搜索因子？ | [RD-Agent-Quant](wiki/Paper-002-RD-Agent-Quant.md)，再比较 [MCTS](wiki/Paper-003-Alpha-Jungle.md) 与 [AlphaPROBE](wiki/Paper-004-AlphaPROBE.md) |
| 盘口信号怎样变成可检验的预测？ | [OFI Cross-Impact](wiki/Paper-033-OFI-Cross-Impact.md)，再读 [DeepLOB](wiki/Paper-011-DeepLOB.md) |
| 风险与执行怎样影响净收益？ | [Graph-based HAR](wiki/Paper-030-Graph-HAR.md) 与 [Trading Volume Alpha](wiki/Paper-036-Trading-Volume-Alpha.md) |

## 按研究方向导航
'''
category_rows=['| 方向 | 篇数 | 主要内容 |','| --- | ---: | --- |']
for g in GROUPS:
    n=sum(p['category']==g['id'] for p in PAPERS)
    category_rows.append(f"| [{g['name']}](wiki/Category-{g['id']}.md) | {n} | {g['description']} |")
readme=intro+'\n'+'\n'.join(category_rows)+'\n\n## 全部论文\n\n'
for g in GROUPS:
    readme+='### '+g['name']+'\n\n'+table([p for p in PAPERS if p['category']==g['id']],root=True)+'\n\n'
readme+='''¹ 年份对应本导航所链接的首发预印本或会议、期刊版本，具体见原文页面。它不是统一口径的正式发表年份。

## 维护方式

论文卡片包含原文、代码、方法概述、阅读重点与首个实验建议。新增论文或纠正链接可提交 [Issue](https://github.com/PKU-AFT/quant-paper-wiki/issues/new/choose)；补充阅读笔记和复现记录可提交 Pull Request。请参阅 [贡献说明](CONTRIBUTING.md) 和 [来源与状态](wiki/Sources-and-Status.md)。

数据目录中的 [论文清单](data/papers.json) 是可编辑来源。修改后运行 `python3 scripts/build.py` 重新生成导航，再运行 `python3 scripts/check.py` 检查完整性。

论文、作者代码与实验数据的权利和使用条件以各原始来源为准。本仓库收录链接及简要导读，不镜像论文全文或数据集。
'''
write(ROOT/'README.md',readme)

home='''# 量化研究论文导航

欢迎来到 PKU-AFT 的论文阅读与复现 Wiki。

这里从 **37 篇论文**出发，把研究问题、原文入口、配套代码与实验建议放在同一张阅读卡片中。

**[完整目录](All-Papers.md) · [阅读路线](Reading-Paths.md) · [复现规范](Reproduction-Guide.md) · [来源与状态](Sources-and-Status.md)**

## 选择方向

'''
for g in GROUPS:
    subset=[p for p in PAPERS if p['category']==g['id']]
    home+=f"### [{g['name']}](Category-{g['id']}.md) · {len(subset)} 篇\n\n{g['description']}\n\n"
    home+=' · '.join(page_link(p) for p in subset)+'\n\n'
home+='''## 推荐起点

先读 StockMixer 与 Label Horizon，建立统一基线和标签口径；随后用 DoubleAdapt 研究市场适应，再根据数据条件选择 Agent、风险预测或盘口执行方向。完整顺序与阶段产出见 [阅读路线](Reading-Paths.md)。

当前仅完成导航与初步导读整理，所有独立复现实验均为“未开展”。
'''
write(ROOT/'wiki/Home.md',home)
all_papers='# 全部论文 · 原清单顺序\n\n[返回首页](Home.md) · [阅读路线](Reading-Paths.md)\n\n保留原清单 01–37 编号；点击论文名称打开独立阅读卡片。\n\n'+table(PAPERS)+'\n\n¹ 年份口径与版本说明见 [来源与状态](Sources-and-Status.md)。'
write(ROOT/'wiki/All-Papers.md',all_papers)
for g in GROUPS:
    content=f"# {g['name']}\n\n[返回首页](Home.md) · [完整目录](All-Papers.md)\n\n{g['description']}\n\n"
    content+=table([p for p in PAPERS if p['category']==g['id']])
    content+='\n\n阅读完成后，再按 [复现规范](Reproduction-Guide.md) 记录数据、时间切分和实验结果。'
    write(ROOT/f"wiki/Category-{g['id']}.md",content)

for p in PAPERS:
    g=GROUP[p['category']]
    code=f"[{p['code_note']}]({p['code_url']})" if p['code_url'] else p['code_note']
    sources='\n'.join(f"- [{s['label']}]({s['url']})" for s in p['extra_sources'])
    text=f'''# {p['id']:02d} · {p['short_title']}

[返回首页](Home.md) · [{g['name']}](Category-{g['id']}.md) · [全部论文](All-Papers.md)

**{p['title']}**

| 项目 | 内容 |
| --- | --- |
| 研究方向 | {g['name']} |
| 所链接版本年份 | {p['year']}，以原文页面的版本信息为准 |
| 原文入口 | [论文页面]({p['primary_url']}) |
| 配套代码 | {code} |
| 首版整理状态 | {p['verification_status']}；本页为简要导读 |
| 独立复现状态 | {p['reproduction_status']} |
| 最近核对 | {p['last_checked']} |

## 研究什么

{p['summary']}

## 阅读时关注什么

{p['reading_focus']}

## 第一个实验可以怎么做

{p['first_experiment']}

这是一项待开展的实验建议。运行前请先确定 [数据与评估协议](Reproduction-Guide.md)；完成后附上代码版本、数据范围、命令和结果。
'''
    if sources: text+='\n## 补充来源与版本\n\n'+sources+'\n'
    text+='''
## 后续阅读记录

当前尚无本仓库独立实验记录。后续笔记应注明原文页码或章节；复现记录应说明完成的是环境检查、方法演示还是论文实验。
'''
    write(ROOT/'wiki'/filename(p),text)

sidebar='# 导航\n\n[首页](Home.md)\n\n[全部 37 篇](All-Papers.md)\n\n[阅读路线](Reading-Paths.md)\n\n[复现规范](Reproduction-Guide.md)\n\n'
sidebar+='\n\n'.join(f"[{g['name']}](Category-{g['id']}.md)" for g in GROUPS)
sidebar+='\n\n[来源与状态](Sources-and-Status.md)'
write(ROOT/'wiki/_Sidebar.md',sidebar)
write(ROOT/'wiki/_Footer.md','PKU-AFT · 量化研究论文导航 · 首版 2026-10-18 · [来源与状态](Sources-and-Status.md)')
print(f'Built {len(PAPERS)} paper cards and {len(GROUPS)} category pages.')
