# PKU-AFT · 量化研究论文导航

从读懂问题，到建立基线，再到可以核查的复现实验。

当前收录 **37 篇论文 · 7 个研究方向 · 17 个配套代码入口**，保留原清单编号。覆盖因子挖掘、收益预测、在线适应、组合构建、风险管理和交易执行。

**[在线 Wiki](https://github.com/PKU-AFT/quant-paper-wiki/wiki) · [按方向阅读](wiki/Home.md) · [37 篇完整目录](wiki/All-Papers.md) · [阅读与复现路线](wiki/Reading-Paths.md) · [复现记录规范](wiki/Reproduction-Guide.md) · [参与维护](CONTRIBUTING.md)**

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

| 方向 | 篇数 | 主要内容 |
| --- | ---: | --- |
| [因子挖掘与研究 Agent](wiki/Category-alpha-agents.md) | 5 | 从假设生成、搜索分配到因子谱系，比较自动化研究流程。 |
| [收益预测与监督设计](wiki/Category-return-prediction.md) | 10 | 从简单基线、标签期限到关系和潜在因子建模。 |
| [在线学习与市场适应](wiki/Category-online-adaptation.md) | 4 | 研究模型如何应对数据分布漂移和市场状态变化。 |
| [组合管理与强化学习](wiki/Category-portfolio-management.md) | 3 | 把预测或市场表示转化为仓位和动态组合决策。 |
| [风险、协方差与状态估计](wiki/Category-risk-modeling.md) | 6 | 研究波动、协方差、尾部场景与隐藏状态。 |
| [动量策略与资产定价](wiki/Category-asset-pricing.md) | 5 | 连接端到端策略、测试组合构造与跨市场预测。 |
| [微观结构与交易执行](wiki/Category-microstructure.md) | 4 | 从盘口信号、领先滞后关系到成交量和执行成本。 |

## 全部论文

### 因子挖掘与研究 Agent

| 编号 | 论文与阅读卡片 | 年份¹ | 关注的问题 | 原文 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 01 | [AlphaAgent](wiki/Paper-001-AlphaAgent.md) | 2025 | 约束 LLM 因子生成的原创性、假设一致性和公式复杂度。 | [原文](https://arxiv.org/abs/2502.16789) | [代码](https://github.com/RndmVariableQ/AlphaAgent/tree/legacy-main) |
| 02 | [R&D-Agent-Quant](wiki/Paper-002-RD-Agent-Quant.md) | 2025 | 把研究假设、代码开发、回测反馈与因子和模型联合优化串成迭代流程。 | [原文](https://arxiv.org/abs/2505.15155) | [代码](https://github.com/microsoft/RD-Agent) |
| 03 | [Navigating the Alpha Jungle](wiki/Paper-003-Alpha-Jungle.md) | 2025 | 结合 LLM 的公式生成与蒙特卡洛树搜索，分配因子搜索预算。 | [原文](https://arxiv.org/abs/2505.11122) | 待补 |
| 04 | [AlphaPROBE](wiki/Paper-004-AlphaPROBE.md) | 2026 | 用有向无环图记录因子演化，以贝叶斯检索和祖先路径引导后续生成。 | [原文](https://arxiv.org/abs/2602.11917) | [代码](https://github.com/gta0804/AlphaPROBE) |
| 05 | [QuantaAlpha](wiki/Paper-005-QuantaAlpha.md) | 2026 | 对完整因子研究轨迹进行变异与交叉，复用有效的构造和修复步骤。 | [原文](https://arxiv.org/abs/2602.07085) | [代码](https://github.com/QuantaAlpha/QuantaAlpha) |

### 收益预测与监督设计

| 编号 | 论文与阅读卡片 | 年份¹ | 关注的问题 | 原文 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 06 | [Progressive Dependency Representation Learning](wiki/Paper-006-PDU.md) | 2025 | 围绕不确定风险下的股票排序，研究渐进依赖表征。 | [原文](https://doi.org/10.1145/3690624.3709189) | [代码](https://github.com/xieyanzhe/PDU) |
| 07 | [RSAP-DFM](wiki/Paper-007-RSAP-DFM.md) | 2024 | 用连续市场状态调节动态因子模型，并用自适应后验改进收益映射。 | [原文](https://www.ijcai.org/proceedings/2024/676) | 待补 |
| 08 | [ADB-TRM](wiki/Paper-008-ADB-TRM.md) | 2024 | 结合元学习、对抗样本和全局局部交互，缓解时序及关系偏差。 | [原文](https://www.ijcai.org/proceedings/2024/221) | 待补 |
| 09 | [FactorVAE](wiki/Paper-009-FactorVAE.md) | 2022 | 把动态因子模型与 VAE 结合，以训练期后验指导预测期先验。 | [原文](https://ojs.aaai.org/index.php/AAAI/article/view/20369) | 待补 |
| 10 | [FactorGCL](wiki/Paper-010-FactorGCL.md) | 2025 | 通过超图和残差对比学习，提取已有因子之外的隐藏收益信号。 | [原文](https://arxiv.org/abs/2502.05218) | 待补 |
| 12 | [HIST](wiki/Paper-012-HIST.md) | 2021 | 分离预定义概念、隐藏概念和个股信息，建模股票间共享信号。 | [原文](https://arxiv.org/abs/2110.13716) | [代码](https://github.com/Wentao-Xu/HIST) |
| 13 | [The Label Horizon Paradox](wiki/Paper-013-Label-Horizon.md) | 2026 | 固定最终预测目标，研究训练标签期限及其权重如何影响样本外预测。 | [原文](https://arxiv.org/abs/2602.03395) | [代码](https://github.com/EFundAI/label-horizon-paradox) |
| 15 | [StockMixer](wiki/Paper-015-StockMixer.md) | 2024 | 使用 MLP 分别混合指标、时间和股票信息，提供较简单的股票预测架构。 | [原文](https://ojs.aaai.org/index.php/AAAI/article/view/28681) | [代码](https://github.com/SJTU-DMTai/StockMixer) |
| 16 | [RAVEN](wiki/Paper-016-RAVEN.md) | 2026 | 通过市场状态感知的多专家机制，为样本自适应选择历史上下文长度。 | [原文](https://arxiv.org/abs/2606.24062) | 待补 |
| 23 | [Multi-task RNN + Higher-order MRF](wiki/Paper-023-RNN-MRF.md) | 2019 | 把多任务循环网络与高阶 MRF 结合，建模股票群组间的价格方向关系。 | [原文](https://doi.org/10.1145/3292500.3330983) | 待补 |

### 在线学习与市场适应

| 编号 | 论文与阅读卡片 | 年份¹ | 关注的问题 | 原文 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 17 | [DoubleAdapt](wiki/Paper-017-DoubleAdapt.md) | 2023 | 利用元学习同时适应数据分布和模型参数，支持股票预测的增量更新。 | [原文](https://arxiv.org/abs/2306.09862) | [代码](https://github.com/SJTU-DMTai/DoubleAdapt) |
| 18 | [DDG-DA](wiki/Paper-018-DDG-DA.md) | 2022 | 预测未来分布变化，并据此调整训练样本分布来适应概念漂移。 | [原文](https://arxiv.org/abs/2201.04038) | 待补 |
| 19 | [Fast and Slow Streams / DSOF](wiki/Paper-019-DSOF.md) | 2025 | 以快流响应近期变化、慢流保存长期知识，同时规范在线时间序列评估。 | [原文](https://proceedings.iclr.cc/paper_files/paper/2025/hash/46e624c244cff669223d488defd4e835-Abstract-Conference.html) | [代码](https://github.com/yyalau/iclr2025_dsof) |
| 20 | [ReCAP](wiki/Paper-020-ReCAP.md) | 2026 | 检测市场状态并保存策略向量，通过门控组合历史策略以持续适应。 | [原文](https://arxiv.org/abs/2606.00143) | 待补 |

### 组合管理与强化学习

| 编号 | 论文与阅读卡片 | 年份¹ | 关注的问题 | 原文 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 14 | [ArchetypeTrader](wiki/Paper-014-ArchetypeTrader.md) | 2026 | 从示范轨迹学习策略原型，再用强化学习选择和精修交易行为。 | [原文](https://ojs.aaai.org/index.php/AAAI/article/view/40166) | 待补 |
| 22 | [EarnMore](wiki/Paper-022-EarnMore.md) | 2023 | 用可遮罩股票表示，让同一强化学习模型适应不同股票池。 | [原文](https://arxiv.org/abs/2311.10801) | 待补 |
| 24 | [MILLION](wiki/Paper-024-MILLION.md) | 2024 | 联合收益预测、排序与组合目标，再以组合调整实现风险偏好控制。 | [原文](https://arxiv.org/abs/2412.03038) | 待补 |

### 风险、协方差与状态估计

| 编号 | 论文与阅读卡片 | 年份¹ | 关注的问题 | 原文 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 21 | [Deep Risk Model](wiki/Paper-021-Deep-Risk-Model.md) | 2021 | 学习潜在风险因子，为股票收益协方差估计提供输入。 | [原文](https://arxiv.org/abs/2107.05201) | [代码](https://github.com/linhx25/DeepRiskModel) |
| 29 | [Tail-GAN](wiki/Paper-029-Tail-GAN.md) | 2022 | 围绕 VaR 和 ES 的联合评分训练场景生成器，保留组合尾部风险特征。 | [原文](https://arxiv.org/abs/2203.01664) | [代码](https://github.com/chaozhang-ox/Tail-GAN) |
| 30 | [Graph-based HAR](wiki/Paper-030-Graph-HAR.md) | 2025 | 把图邻居信息加入 HAR，预测波动和相关性，并形成协方差预测。 | [原文](https://academic.oup.com/jfec/article/23/2/nbae026/7889003) | [代码](https://github.com/chaozhang-ox/Graph-based-HAR) |
| 31 | [GNNHAR](wiki/Paper-031-GNNHAR.md) | 2025 | 用图神经网络刻画波动溢出，并比较不同损失函数与邻居范围。 | [原文](https://www.sciencedirect.com/science/article/pii/S0169207024000967) | [代码](https://github.com/chaozhang-ox/GNNHAR) |
| 32 | [Intraday Commonality](wiki/Paper-032-Intraday-Commonality.md) | 2022 | 汇集多股票的日内波动信息，并加入市场波动代理来预测已实现波动。 | [原文](https://arxiv.org/abs/2202.08962) | [代码](https://github.com/chaozhang-ox/IntradayVoltility) |
| 35 | [Deep Kalman Filters Can Filter](wiki/Paper-035-Deep-Kalman-Filters.md) | 2023 | 研究连续时间深度滤波模型逼近条件分布的理论能力。 | [原文](https://arxiv.org/abs/2310.19603v1) | 待补 |

### 动量策略与资产定价

| 编号 | 论文与阅读卡片 | 年份¹ | 关注的问题 | 原文 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 25 | [Deep Inception Networks](wiki/Paper-025-DIN.md) | 2023 | 从收益序列联合学习时序和截面特征，直接输出组合仓位并优化 Sharpe。 | [原文](https://arxiv.org/abs/2307.05522) | 待补 |
| 26 | [Spatio-Temporal Momentum](wiki/Paper-026-Spatio-Temporal-Momentum.md) | 2023 | 把时序动量与截面动量联合建模，学习组合交易信号。 | [原文](https://arxiv.org/abs/2302.10175) | 待补 |
| 27 | [Forest through the Trees](wiki/Paper-027-Forest-through-Trees.md) | 2019 | 根据股票特征构造树分割和测试组合，用于刻画资产定价关系。 | [原文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3493458) | 待补 |
| 28 | [Alpha Go Everywhere](wiki/Paper-028-Alpha-Go-Everywhere.md) | 2025 | 比较不同市场的股票收益预测，以及本地特征和美国市场特征的作用。 | [原文](https://doi.org/10.1093/rapstu/raaf005) | [代码](https://github.com/chaozhang-ox/AlphaGoEverywhere) |
| 37 | [Deep Momentum Networks](wiki/Paper-037-Deep-Momentum.md) | 2019 | 在波动缩放框架内联合学习趋势与仓位，并用目标函数和换手正则影响交易行为。 | [原文](https://arxiv.org/abs/1904.04912) | 待补 |

### 微观结构与交易执行

| 编号 | 论文与阅读卡片 | 年份¹ | 关注的问题 | 原文 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 11 | [DeepLOB](wiki/Paper-011-DeepLOB.md) | 2018 | 用卷积学习盘口空间结构，再以 LSTM 学习时间依赖，预测短期价格方向。 | [原文](https://arxiv.org/abs/1808.03668) | [代码](https://github.com/zcakhaa/DeepLOB-Deep-Convolutional-Neural-Networks-for-Limit-Order-Books) |
| 33 | [Cross-Impact of OFI](wiki/Paper-033-OFI-Cross-Impact.md) | 2021 | 整合多档盘口 OFI，区分自身冲击、跨股票同期解释和滞后预测。 | [原文](https://arxiv.org/abs/2112.13213) | 待补 |
| 34 | [Detecting Lead-Lag Relationships](wiki/Paper-034-Lead-Lag.md) | 2023 | 识别股票收益间的领先滞后关系，并以组合策略检验经济意义。 | [原文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4599565) | 待补 |
| 36 | [Trading Volume Alpha](wiki/Paper-036-Trading-Volume-Alpha.md) | 2024 | 把成交量预测转成交易成本和调仓决策，研究成本后的组合改善。 | [原文](https://www.nber.org/papers/w33037) | 待补 |

¹ 年份对应本导航所链接的首发预印本或会议、期刊版本，具体见原文页面。它不是统一口径的正式发表年份。

## 维护方式

论文卡片包含原文、代码、方法概述、阅读重点与首个实验建议。新增论文或纠正链接可提交 [Issue](https://github.com/PKU-AFT/quant-paper-wiki/issues/new/choose)；补充阅读笔记和复现记录可提交 Pull Request。请参阅 [贡献说明](CONTRIBUTING.md) 和 [来源与状态](wiki/Sources-and-Status.md)。

数据目录中的 [论文清单](data/papers.json) 是可编辑来源。修改后运行 `python3 scripts/build.py` 重新生成导航，再运行 `python3 scripts/check.py` 检查完整性。

论文、作者代码与实验数据的权利和使用条件以各原始来源为准。本仓库收录链接及简要导读，不镜像论文全文或数据集。
