# 17 · DoubleAdapt

[返回首页](Home.md) · [在线学习与市场适应](Category-online-adaptation.md) · [全部论文](All-Papers.md)

**DoubleAdapt: A Meta-learning Approach to Incremental Learning for Stock Trend Forecasting**

| 项目 | 内容 |
| --- | --- |
| 研究方向 | 在线学习与市场适应 |
| 所链接版本年份 | 2023，以原文页面的版本信息为准 |
| 原文入口 | [论文页面](https://arxiv.org/abs/2306.09862) |
| 配套代码 | [作者独立 API 实现](https://github.com/SJTU-DMTai/DoubleAdapt) |
| 首版整理状态 | 题录与原文入口已核对；本页为简要导读 |
| 独立复现状态 | 未开展 |
| 最近核对 | 2026-10-18 |

## 研究什么

利用元学习同时适应数据分布和模型参数，支持股票预测的增量更新。

## 阅读时关注什么

更新只能使用已经完成的标签；需与滚动重训比较成本和效果。

## 第一个实验可以怎么做

接到已有简单预测器上，对比冻结模型、增量微调与滚动重训。

这是一项待开展的实验建议。运行前请先确定 [数据与评估协议](Reproduction-Guide.md)；完成后附上代码版本、数据范围、命令和结果。

## 后续阅读记录

当前尚无本仓库独立实验记录。后续笔记应注明原文页码或章节；复现记录应说明完成的是环境检查、方法演示还是论文实验。
