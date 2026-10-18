# 19 · Fast and Slow Streams / DSOF

[返回首页](Home.md) · [在线学习与市场适应](Category-online-adaptation.md) · [全部论文](All-Papers.md)

**Fast and Slow Streams for Online Time Series Forecasting Without Information Leakage**

| 项目 | 内容 |
| --- | --- |
| 研究方向 | 在线学习与市场适应 |
| 所链接版本年份 | 2025，以原文页面的版本信息为准 |
| 原文入口 | [论文页面](https://proceedings.iclr.cc/paper_files/paper/2025/hash/46e624c244cff669223d488defd4e835-Abstract-Conference.html) |
| 配套代码 | [论文配套仓库](https://github.com/yyalau/iclr2025_dsof) |
| 首版整理状态 | 题录与原文入口已核对；本页为简要导读 |
| 独立复现状态 | 未开展 |
| 最近核对 | 2026-10-18 |

## 研究什么

以快流响应近期变化、慢流保存长期知识，同时规范在线时间序列评估。

## 阅读时关注什么

模型更新后不能再次在包含已见真实值的窗口上报告未见样本表现。

## 第一个实验可以怎么做

先画出预测、标签到达与参数更新的时间线，再比较在线模型。

这是一项待开展的实验建议。运行前请先确定 [数据与评估协议](Reproduction-Guide.md)；完成后附上代码版本、数据范围、命令和结果。

## 补充来源与版本

- [OpenReview](https://openreview.net/forum?id=I0n3EyogMi)

## 后续阅读记录

当前尚无本仓库独立实验记录。后续笔记应注明原文页码或章节；复现记录应说明完成的是环境检查、方法演示还是论文实验。
