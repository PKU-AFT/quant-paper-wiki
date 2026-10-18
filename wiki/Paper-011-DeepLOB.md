# 11 · DeepLOB

[返回首页](Home.md) · [微观结构与交易执行](Category-microstructure.md) · [全部论文](All-Papers.md)

**DeepLOB: Deep Convolutional Neural Networks for Limit Order Books**

| 项目 | 内容 |
| --- | --- |
| 研究方向 | 微观结构与交易执行 |
| 所链接版本年份 | 2018，以原文页面的版本信息为准 |
| 原文入口 | [论文页面](https://arxiv.org/abs/1808.03668) |
| 配套代码 | [作者 FI-2010 演示](https://github.com/zcakhaa/DeepLOB-Deep-Convolutional-Neural-Networks-for-Limit-Order-Books) |
| 首版整理状态 | 题录与原文入口已核对；本页为简要导读 |
| 独立复现状态 | 未开展 |
| 最近核对 | 2026-10-18 |

## 研究什么

用卷积学习盘口空间结构，再以 LSTM 学习时间依赖，预测短期价格方向。

## 阅读时关注什么

分类精度不能直接代表可交易收益；数据标准化与窗口切分需要防止泄露。

## 第一个实验可以怎么做

先跑作者的 FI-2010 演示，再加延迟、成交和成本约束。

这是一项待开展的实验建议。运行前请先确定 [数据与评估协议](Reproduction-Guide.md)；完成后附上代码版本、数据范围、命令和结果。

## 后续阅读记录

当前尚无本仓库独立实验记录。后续笔记应注明原文页码或章节；复现记录应说明完成的是环境检查、方法演示还是论文实验。
