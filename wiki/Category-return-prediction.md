# 收益预测与监督设计

[返回首页](Home.md) · [完整目录](All-Papers.md)

从简单基线、标签期限到关系和潜在因子建模。

| 编号 | 论文与阅读卡片 | 年份¹ | 关注的问题 | 原文 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 06 | [Progressive Dependency Representation Learning](Paper-006-PDU.md) | 2025 | 围绕不确定风险下的股票排序，研究渐进依赖表征。 | [原文](https://doi.org/10.1145/3690624.3709189) | [代码](https://github.com/xieyanzhe/PDU) |
| 07 | [RSAP-DFM](Paper-007-RSAP-DFM.md) | 2024 | 用连续市场状态调节动态因子模型，并用自适应后验改进收益映射。 | [原文](https://www.ijcai.org/proceedings/2024/676) | 待补 |
| 08 | [ADB-TRM](Paper-008-ADB-TRM.md) | 2024 | 结合元学习、对抗样本和全局局部交互，缓解时序及关系偏差。 | [原文](https://www.ijcai.org/proceedings/2024/221) | 待补 |
| 09 | [FactorVAE](Paper-009-FactorVAE.md) | 2022 | 把动态因子模型与 VAE 结合，以训练期后验指导预测期先验。 | [原文](https://ojs.aaai.org/index.php/AAAI/article/view/20369) | 待补 |
| 10 | [FactorGCL](Paper-010-FactorGCL.md) | 2025 | 通过超图和残差对比学习，提取已有因子之外的隐藏收益信号。 | [原文](https://arxiv.org/abs/2502.05218) | 待补 |
| 12 | [HIST](Paper-012-HIST.md) | 2021 | 分离预定义概念、隐藏概念和个股信息，建模股票间共享信号。 | [原文](https://arxiv.org/abs/2110.13716) | [代码](https://github.com/Wentao-Xu/HIST) |
| 13 | [The Label Horizon Paradox](Paper-013-Label-Horizon.md) | 2026 | 固定最终预测目标，研究训练标签期限及其权重如何影响样本外预测。 | [原文](https://arxiv.org/abs/2602.03395) | [代码](https://github.com/EFundAI/label-horizon-paradox) |
| 15 | [StockMixer](Paper-015-StockMixer.md) | 2024 | 使用 MLP 分别混合指标、时间和股票信息，提供较简单的股票预测架构。 | [原文](https://ojs.aaai.org/index.php/AAAI/article/view/28681) | [代码](https://github.com/SJTU-DMTai/StockMixer) |
| 16 | [RAVEN](Paper-016-RAVEN.md) | 2026 | 通过市场状态感知的多专家机制，为样本自适应选择历史上下文长度。 | [原文](https://arxiv.org/abs/2606.24062) | 待补 |
| 23 | [Multi-task RNN + Higher-order MRF](Paper-023-RNN-MRF.md) | 2019 | 把多任务循环网络与高阶 MRF 结合，建模股票群组间的价格方向关系。 | [原文](https://doi.org/10.1145/3292500.3330983) | 待补 |

阅读完成后，再按 [复现规范](Reproduction-Guide.md) 记录数据、时间切分和实验结果。
