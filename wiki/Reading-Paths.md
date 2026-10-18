# 阅读与复现路线

[返回首页](Home.md) · [全部论文](All-Papers.md)

下面是本导航的建议顺序。先完成一个小而完整的比较，再扩大模型和数据规模。

| 阶段 | 论文 | 要回答的问题 | 建议交付物 |
| --- | --- | --- | --- |
| 1. 标签与基线 | [Label Horizon](Paper-013-Label-Horizon.md)、[StockMixer](Paper-015-StockMixer.md) | 固定最终目标后，训练标签期限与模型架构分别贡献了多少？ | 数据说明、时间切分、简单模型与 StockMixer 对照表 |
| 2. 市场适应 | [DoubleAdapt](Paper-017-DoubleAdapt.md)、[DSOF](Paper-019-DSOF.md) | 增益来自持续更新还是更复杂的模型？在线评估是否符合标签到达顺序？ | 预测与更新时序图、滚动重训基线、计算开销 |
| 3. 因子研究自动化 | [RD-Agent-Quant](Paper-002-RD-Agent-Quant.md)、[Alpha Jungle](Paper-003-Alpha-Jungle.md)、[AlphaPROBE](Paper-004-AlphaPROBE.md) | 相同搜索预算下，自动化能否提高有效、低相关因子的产出？ | 实验台账、搜索费用、候选去重和留出集结果 |
| 4. 微观信号 | [OFI](Paper-033-OFI-Cross-Impact.md)、[DeepLOB](Paper-011-DeepLOB.md) | 复杂网络能否超越简单盘口信号，并覆盖实际执行成本？ | 同期解释与未来预测分表、延迟和成本敏感性 |
| 5. 风险与执行 | [Graph-based HAR](Paper-030-Graph-HAR.md)、[Trading Volume Alpha](Paper-036-Trading-Volume-Alpha.md) | 风险及成交量预测能否改善相同约束下的净收益？ | 风险校准、换手、跟踪误差和成本后的组合比较 |

## 按已有数据选择

- 只有日频价格和成交量：先做标签期限、简单预测基线、动量策略和在线适应。数据是否满足具体论文实验仍需逐篇检查。
- 有历史行业或概念快照：可以扩展到 HIST、关系模型与因子模型。
- 有盘口数据：从 OFI 与线性基线开始，再比较 DeepLOB。先明确事件顺序、交易时点和成交假设。
- 有已实现波动或高频价格：可以研究 HAR、GNNHAR、协方差和尾部风险。使用其他数据集时应标为“方法迁移实验”。

## 初次阅读怎么记录

每篇先写清一个问题：输入是什么、输出是什么、推理时能看到哪些信息、最简单的对照模型是什么。然后摘录方法与实验中最关键的原文位置，最后写一个能在已有数据上完成的小实验。

完成阅读与完成复现是两种进度，分别记录。
