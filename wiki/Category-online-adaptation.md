# 在线学习与市场适应

[返回首页](Home.md) · [完整目录](All-Papers.md)

研究模型如何应对数据分布漂移和市场状态变化。

| 编号 | 论文与阅读卡片 | 年份¹ | 关注的问题 | 原文 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 17 | [DoubleAdapt](Paper-017-DoubleAdapt.md) | 2023 | 利用元学习同时适应数据分布和模型参数，支持股票预测的增量更新。 | [原文](https://arxiv.org/abs/2306.09862) | [代码](https://github.com/SJTU-DMTai/DoubleAdapt) |
| 18 | [DDG-DA](Paper-018-DDG-DA.md) | 2022 | 预测未来分布变化，并据此调整训练样本分布来适应概念漂移。 | [原文](https://arxiv.org/abs/2201.04038) | 待补 |
| 19 | [Fast and Slow Streams / DSOF](Paper-019-DSOF.md) | 2025 | 以快流响应近期变化、慢流保存长期知识，同时规范在线时间序列评估。 | [原文](https://proceedings.iclr.cc/paper_files/paper/2025/hash/46e624c244cff669223d488defd4e835-Abstract-Conference.html) | [代码](https://github.com/yyalau/iclr2025_dsof) |
| 20 | [ReCAP](Paper-020-ReCAP.md) | 2026 | 检测市场状态并保存策略向量，通过门控组合历史策略以持续适应。 | [原文](https://arxiv.org/abs/2606.00143) | 待补 |

阅读完成后，再按 [复现规范](Reproduction-Guide.md) 记录数据、时间切分和实验结果。
