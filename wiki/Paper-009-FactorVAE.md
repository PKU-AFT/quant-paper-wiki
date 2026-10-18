# 09 · FactorVAE

[返回首页](Home.md) · [收益预测与监督设计](Category-return-prediction.md) · [全部论文](All-Papers.md)

**FactorVAE: A Probabilistic Dynamic Factor Model Based on Variational Autoencoder for Predicting Cross-Sectional Stock Returns**

| 项目 | 内容 |
| --- | --- |
| 研究方向 | 收益预测与监督设计 |
| 所链接版本年份 | 2022，以原文页面的版本信息为准 |
| 原文入口 | [论文页面](https://ojs.aaai.org/index.php/AAAI/article/view/20369) |
| 配套代码 | 尚未核实作者代码入口；不表示没有公开代码 |
| 首版整理状态 | 题录与原文入口已核对；本页为简要导读 |
| 独立复现状态 | 未开展 |
| 最近核对 | 2026-10-18 |

## 研究什么

把动态因子模型与 VAE 结合，以训练期后验指导预测期先验。

## 阅读时关注什么

训练后验可以使用标签；部署推理必须只使用历史信息。不要与解耦表征领域的同名 FactorVAE 混淆。

## 第一个实验可以怎么做

明确 prior、posterior 和 label 三条信息路径，再复现最小预测实验。

这是一项待开展的实验建议。运行前请先确定 [数据与评估协议](Reproduction-Guide.md)；完成后附上代码版本、数据范围、命令和结果。

## 后续阅读记录

当前尚无本仓库独立实验记录。后续笔记应注明原文页码或章节；复现记录应说明完成的是环境检查、方法演示还是论文实验。
