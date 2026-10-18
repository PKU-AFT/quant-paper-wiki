# 31 · GNNHAR

[返回首页](Home.md) · [风险、协方差与状态估计](Category-risk-modeling.md) · [全部论文](All-Papers.md)

**Forecasting Realized Volatility with Spillover Effects: Perspectives from Graph Neural Networks**

| 项目 | 内容 |
| --- | --- |
| 研究方向 | 风险、协方差与状态估计 |
| 所链接版本年份 | 2025，以原文页面的版本信息为准 |
| 原文入口 | [论文页面](https://www.sciencedirect.com/science/article/pii/S0169207024000967) |
| 配套代码 | [论文配套仓库](https://github.com/chaozhang-ox/GNNHAR) |
| 首版整理状态 | 题录与原文入口已核对；本页为简要导读 |
| 独立复现状态 | 未开展 |
| 最近核对 | 2026-10-18 |

## 研究什么

用图神经网络刻画波动溢出，并比较不同损失函数与邻居范围。

## 阅读时关注什么

更多邻居未必更好；需区分损失函数选择与网络结构带来的收益。

## 第一个实验可以怎么做

先比较 MSE 与 QLIKE，再消融零跳、一跳和多跳邻居。

这是一项待开展的实验建议。运行前请先确定 [数据与评估协议](Reproduction-Guide.md)；完成后附上代码版本、数据范围、命令和结果。

## 补充来源与版本

- [作者论文稿](https://web.media.mit.edu/~xdong/paper/ijf25.pdf)

## 后续阅读记录

当前尚无本仓库独立实验记录。后续笔记应注明原文页码或章节；复现记录应说明完成的是环境检查、方法演示还是论文实验。
