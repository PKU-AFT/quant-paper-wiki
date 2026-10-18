# 量化研究论文导航

欢迎来到 PKU-AFT 的论文阅读与复现 Wiki。

这里从 **37 篇论文**出发，把研究问题、原文入口、配套代码与实验建议放在同一张阅读卡片中。

**[完整目录](All-Papers.md) · [阅读路线](Reading-Paths.md) · [复现规范](Reproduction-Guide.md) · [来源与状态](Sources-and-Status.md)**

## 选择方向

### [因子挖掘与研究 Agent](Category-alpha-agents.md) · 5 篇

从假设生成、搜索分配到因子谱系，比较自动化研究流程。

[AlphaAgent](Paper-001-AlphaAgent.md) · [R&D-Agent-Quant](Paper-002-RD-Agent-Quant.md) · [Navigating the Alpha Jungle](Paper-003-Alpha-Jungle.md) · [AlphaPROBE](Paper-004-AlphaPROBE.md) · [QuantaAlpha](Paper-005-QuantaAlpha.md)

### [收益预测与监督设计](Category-return-prediction.md) · 10 篇

从简单基线、标签期限到关系和潜在因子建模。

[Progressive Dependency Representation Learning](Paper-006-PDU.md) · [RSAP-DFM](Paper-007-RSAP-DFM.md) · [ADB-TRM](Paper-008-ADB-TRM.md) · [FactorVAE](Paper-009-FactorVAE.md) · [FactorGCL](Paper-010-FactorGCL.md) · [HIST](Paper-012-HIST.md) · [The Label Horizon Paradox](Paper-013-Label-Horizon.md) · [StockMixer](Paper-015-StockMixer.md) · [RAVEN](Paper-016-RAVEN.md) · [Multi-task RNN + Higher-order MRF](Paper-023-RNN-MRF.md)

### [在线学习与市场适应](Category-online-adaptation.md) · 4 篇

研究模型如何应对数据分布漂移和市场状态变化。

[DoubleAdapt](Paper-017-DoubleAdapt.md) · [DDG-DA](Paper-018-DDG-DA.md) · [Fast and Slow Streams / DSOF](Paper-019-DSOF.md) · [ReCAP](Paper-020-ReCAP.md)

### [组合管理与强化学习](Category-portfolio-management.md) · 3 篇

把预测或市场表示转化为仓位和动态组合决策。

[ArchetypeTrader](Paper-014-ArchetypeTrader.md) · [EarnMore](Paper-022-EarnMore.md) · [MILLION](Paper-024-MILLION.md)

### [风险、协方差与状态估计](Category-risk-modeling.md) · 6 篇

研究波动、协方差、尾部场景与隐藏状态。

[Deep Risk Model](Paper-021-Deep-Risk-Model.md) · [Tail-GAN](Paper-029-Tail-GAN.md) · [Graph-based HAR](Paper-030-Graph-HAR.md) · [GNNHAR](Paper-031-GNNHAR.md) · [Intraday Commonality](Paper-032-Intraday-Commonality.md) · [Deep Kalman Filters Can Filter](Paper-035-Deep-Kalman-Filters.md)

### [动量策略与资产定价](Category-asset-pricing.md) · 5 篇

连接端到端策略、测试组合构造与跨市场预测。

[Deep Inception Networks](Paper-025-DIN.md) · [Spatio-Temporal Momentum](Paper-026-Spatio-Temporal-Momentum.md) · [Forest through the Trees](Paper-027-Forest-through-Trees.md) · [Alpha Go Everywhere](Paper-028-Alpha-Go-Everywhere.md) · [Deep Momentum Networks](Paper-037-Deep-Momentum.md)

### [微观结构与交易执行](Category-microstructure.md) · 4 篇

从盘口信号、领先滞后关系到成交量和执行成本。

[DeepLOB](Paper-011-DeepLOB.md) · [Cross-Impact of OFI](Paper-033-OFI-Cross-Impact.md) · [Detecting Lead-Lag Relationships](Paper-034-Lead-Lag.md) · [Trading Volume Alpha](Paper-036-Trading-Volume-Alpha.md)

## 推荐起点

先读 StockMixer 与 Label Horizon，建立统一基线和标签口径；随后用 DoubleAdapt 研究市场适应，再根据数据条件选择 Agent、风险预测或盘口执行方向。完整顺序与阶段产出见 [阅读路线](Reading-Paths.md)。

当前仅完成导航与初步导读整理，所有独立复现实验均为“未开展”。
