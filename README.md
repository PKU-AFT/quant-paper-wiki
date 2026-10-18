# PKU-AFT · Quantitative Finance Paper Wiki

**37 papers · 7 research areas · 17 companion code links**

[Online Wiki](https://github.com/PKU-AFT/quant-paper-wiki/wiki) · [Full index](wiki/All-Papers.md) · [Reading paths](wiki/Reading-Paths.md) · [Experimental protocol](wiki/Reproduction-Guide.md) · [Sources & versions](wiki/Sources-and-Status.md)

## Research areas

| Research area | Papers | Scope |
| --- | --- | --- |
| [Factor Mining & Research Agents](wiki/Category-alpha-agents.md) | 5 | Hypothesis generation, search allocation and evolutionary research workflows. |
| [Return Prediction & Supervision](wiki/Category-return-prediction.md) | 10 | Simple baselines, label horizons, relational models and latent factors. |
| [Online Learning & Adaptation](wiki/Category-online-adaptation.md) | 4 | Concept drift, incremental updates and market regime changes. |
| [Portfolio Management & RL](wiki/Category-portfolio-management.md) | 3 | Representations and predictions translated into portfolio decisions. |
| [Risk, Covariance & Filtering](wiki/Category-risk-modeling.md) | 6 | Volatility, covariance, tail scenarios and latent-state estimation. |
| [Momentum & Asset Pricing](wiki/Category-asset-pricing.md) | 5 | End-to-end momentum, test portfolios and international return prediction. |
| [Microstructure & Execution](wiki/Category-microstructure.md) | 4 | Order books, lead-lag relationships, volume and execution costs. |

## Paper directory

### Factor Mining & Research Agents

| ID | Paper & notes | Year¹ | Research focus | Paper | Code |
| --- | --- | --- | --- | --- | --- |
| 01 | [AlphaAgent](wiki/Paper-001-AlphaAgent.md) | 2025 | Regularizes LLM factor generation through originality, hypothesis alignment and expression complexity constraints. | [Paper](https://arxiv.org/abs/2502.16789) | [Code](https://github.com/RndmVariableQ/AlphaAgent/tree/legacy-main) |
| 02 | [R&D-Agent-Quant](wiki/Paper-002-RD-Agent-Quant.md) | 2025 | Connects research hypotheses, code development and backtest feedback through joint factor and model optimization. | [Paper](https://arxiv.org/abs/2505.15155) | [Code](https://github.com/microsoft/RD-Agent) |
| 03 | [Navigating the Alpha Jungle](wiki/Paper-003-Alpha-Jungle.md) | 2025 | Combines LLM formula proposals with Monte Carlo tree search to allocate factor search effort. | [Paper](https://arxiv.org/abs/2505.11122) | To verify |
| 04 | [AlphaPROBE](wiki/Paper-004-AlphaPROBE.md) | 2026 | Tracks factor evolution in a DAG and uses Bayesian retrieval and ancestor traces to guide generation. | [Paper](https://arxiv.org/abs/2602.11917) | [Code](https://github.com/gta0804/AlphaPROBE) |
| 05 | [QuantaAlpha](wiki/Paper-005-QuantaAlpha.md) | 2026 | Mutates and recombines complete factor research trajectories to reuse useful construction and repair steps. | [Paper](https://arxiv.org/abs/2602.07085) | [Code](https://github.com/QuantaAlpha/QuantaAlpha) |

### Return Prediction & Supervision

| ID | Paper & notes | Year¹ | Research focus | Paper | Code |
| --- | --- | --- | --- | --- | --- |
| 06 | [Progressive Dependency Representation Learning](wiki/Paper-006-PDU.md) | 2025 | Studies progressive dependency representations for stock ranking under uncertain risk. | [Paper](https://doi.org/10.1145/3690624.3709189) | [Code](https://github.com/xieyanzhe/PDU) |
| 07 | [RSAP-DFM](wiki/Paper-007-RSAP-DFM.md) | 2024 | Conditions a dynamic factor model on continuous market regimes and adapts its posterior return mapping. | [Paper](https://www.ijcai.org/proceedings/2024/676) | To verify |
| 08 | [ADB-TRM](wiki/Paper-008-ADB-TRM.md) | 2024 | Combines meta-learning, adversarial examples and global-local interactions to address temporal and relational bias. | [Paper](https://www.ijcai.org/proceedings/2024/221) | To verify |
| 09 | [FactorVAE](wiki/Paper-009-FactorVAE.md) | 2022 | Combines a dynamic factor model with a VAE, using training posteriors to guide predictive priors. | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/20369) | To verify |
| 10 | [FactorGCL](wiki/Paper-010-FactorGCL.md) | 2025 | Uses hypergraphs and residual contrastive learning to extract signals beyond known factors. | [Paper](https://arxiv.org/abs/2502.05218) | To verify |
| 12 | [HIST](wiki/Paper-012-HIST.md) | 2021 | Separates predefined concepts, hidden concepts and stock-specific information to model shared stock signals. | [Paper](https://arxiv.org/abs/2110.13716) | [Code](https://github.com/Wentao-Xu/HIST) |
| 13 | [The Label Horizon Paradox](wiki/Paper-013-Label-Horizon.md) | 2026 | Studies how training label horizons and their weights affect performance at a fixed prediction horizon. | [Paper](https://arxiv.org/abs/2602.03395) | [Code](https://github.com/EFundAI/label-horizon-paradox) |
| 15 | [StockMixer](wiki/Paper-015-StockMixer.md) | 2024 | Mixes indicators, time and stocks with MLPs to provide a relatively simple forecasting architecture. | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/28681) | [Code](https://github.com/SJTU-DMTai/StockMixer) |
| 16 | [RAVEN](wiki/Paper-016-RAVEN.md) | 2026 | Uses regime-aware experts to adapt the historical context length for each sample. | [Paper](https://arxiv.org/abs/2606.24062) | To verify |
| 23 | [Multi-task RNN + Higher-order MRF](wiki/Paper-023-RNN-MRF.md) | 2019 | Combines multi-task recurrent networks and higher-order MRFs to model stock-group movement dependencies. | [Paper](https://doi.org/10.1145/3292500.3330983) | To verify |

### Online Learning & Adaptation

| ID | Paper & notes | Year¹ | Research focus | Paper | Code |
| --- | --- | --- | --- | --- | --- |
| 17 | [DoubleAdapt](wiki/Paper-017-DoubleAdapt.md) | 2023 | Uses meta-learning to adapt both input distributions and model parameters during incremental stock forecasting. | [Paper](https://arxiv.org/abs/2306.09862) | [Code](https://github.com/SJTU-DMTai/DoubleAdapt) |
| 18 | [DDG-DA](wiki/Paper-018-DDG-DA.md) | 2022 | Forecasts distribution changes and adjusts training distributions to address predictable concept drift. | [Paper](https://arxiv.org/abs/2201.04038) | To verify |
| 19 | [Fast and Slow Streams / DSOF](wiki/Paper-019-DSOF.md) | 2025 | Combines fast adaptation and slow memory streams while formalizing online forecasting without information leakage. | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/46e624c244cff669223d488defd4e835-Abstract-Conference.html) | [Code](https://github.com/yyalau/iclr2025_dsof) |
| 20 | [ReCAP](wiki/Paper-020-ReCAP.md) | 2026 | Detects market regimes and combines stored regime-specific policy vectors through a continually updated gate. | [Paper](https://arxiv.org/abs/2606.00143) | To verify |

### Portfolio Management & RL

| ID | Paper & notes | Year¹ | Research focus | Paper | Code |
| --- | --- | --- | --- | --- | --- |
| 14 | [ArchetypeTrader](wiki/Paper-014-ArchetypeTrader.md) | 2026 | Learns strategic archetypes from demonstration trajectories, then selects and refines actions with reinforcement learning. | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/40166) | To verify |
| 22 | [EarnMore](wiki/Paper-022-EarnMore.md) | 2023 | Uses maskable stock representations so one reinforcement learning model can serve different stock pools. | [Paper](https://arxiv.org/abs/2311.10801) | To verify |
| 24 | [MILLION](wiki/Paper-024-MILLION.md) | 2024 | Combines return prediction, ranking and portfolio objectives with a separate risk-control adjustment. | [Paper](https://arxiv.org/abs/2412.03038) | To verify |

### Risk, Covariance & Filtering

| ID | Paper & notes | Year¹ | Research focus | Paper | Code |
| --- | --- | --- | --- | --- | --- |
| 21 | [Deep Risk Model](wiki/Paper-021-Deep-Risk-Model.md) | 2021 | Learns latent risk factors to improve stock return covariance estimation. | [Paper](https://arxiv.org/abs/2107.05201) | [Code](https://github.com/linhx25/DeepRiskModel) |
| 29 | [Tail-GAN](wiki/Paper-029-Tail-GAN.md) | 2022 | Trains a scenario generator around joint VaR and ES scores to preserve portfolio tail-risk properties. | [Paper](https://arxiv.org/abs/2203.01664) | [Code](https://github.com/chaozhang-ox/Tail-GAN) |
| 30 | [Graph-based HAR](wiki/Paper-030-Graph-HAR.md) | 2025 | Adds graph-neighbor information to HAR forecasts of volatility and correlation, then constructs covariance forecasts. | [Paper](https://academic.oup.com/jfec/article/23/2/nbae026/7889003) | [Code](https://github.com/chaozhang-ox/Graph-based-HAR) |
| 31 | [GNNHAR](wiki/Paper-031-GNNHAR.md) | 2025 | Uses graph neural networks to model volatility spillovers and compares losses and neighborhood depths. | [Paper](https://www.sciencedirect.com/science/article/pii/S0169207024000967) | [Code](https://github.com/chaozhang-ox/GNNHAR) |
| 32 | [Intraday Commonality](wiki/Paper-032-Intraday-Commonality.md) | 2022 | Pools intraday volatility information across stocks and incorporates a market volatility proxy. | [Paper](https://arxiv.org/abs/2202.08962) | [Code](https://github.com/chaozhang-ox/IntradayVoltility) |
| 35 | [Deep Kalman Filters Can Filter](wiki/Paper-035-Deep-Kalman-Filters.md) | 2023 | Studies the theoretical ability of continuous-time deep filters to approximate conditional distributions. | [Paper](https://arxiv.org/abs/2310.19603v1) | To verify |

### Momentum & Asset Pricing

| ID | Paper & notes | Year¹ | Research focus | Paper | Code |
| --- | --- | --- | --- | --- | --- |
| 25 | [Deep Inception Networks](wiki/Paper-025-DIN.md) | 2023 | Learns temporal and cross-sectional features from returns and directly optimizes portfolio positions for Sharpe ratio. | [Paper](https://arxiv.org/abs/2307.05522) | To verify |
| 26 | [Spatio-Temporal Momentum](wiki/Paper-026-Spatio-Temporal-Momentum.md) | 2023 | Jointly learns time-series and cross-sectional momentum signals for portfolio trading. | [Paper](https://arxiv.org/abs/2302.10175) | To verify |
| 27 | [Forest through the Trees](wiki/Paper-027-Forest-through-Trees.md) | 2019 | Builds characteristic-based tree partitions and test portfolios for asset-pricing analysis. | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3493458) | To verify |
| 28 | [Alpha Go Everywhere](wiki/Paper-028-Alpha-Go-Everywhere.md) | 2025 | Studies international stock return prediction using local and US firm characteristics. | [Paper](https://doi.org/10.1093/rapstu/raaf005) | [Code](https://github.com/chaozhang-ox/AlphaGoEverywhere) |
| 37 | [Deep Momentum Networks](wiki/Paper-037-Deep-Momentum.md) | 2019 | Jointly learns trend signals and position sizing within volatility scaling, with turnover-aware objectives. | [Paper](https://arxiv.org/abs/1904.04912) | To verify |

### Microstructure & Execution

| ID | Paper & notes | Year¹ | Research focus | Paper | Code |
| --- | --- | --- | --- | --- | --- |
| 11 | [DeepLOB](wiki/Paper-011-DeepLOB.md) | 2018 | Uses convolutions for order-book structure and an LSTM for temporal dependencies in short-horizon prediction. | [Paper](https://arxiv.org/abs/1808.03668) | [Code](https://github.com/zcakhaa/DeepLOB-Deep-Convolutional-Neural-Networks-for-Limit-Order-Books) |
| 33 | [Cross-Impact of OFI](wiki/Paper-033-OFI-Cross-Impact.md) | 2021 | Combines multi-level order-flow imbalance and separates own impact, contemporaneous cross-impact and lagged prediction. | [Paper](https://arxiv.org/abs/2112.13213) | To verify |
| 34 | [Detecting Lead-Lag Relationships](wiki/Paper-034-Lead-Lag.md) | 2023 | Detects lead-lag relationships in stock returns and evaluates their economic relevance through portfolios. | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4599565) | To verify |
| 36 | [Trading Volume Alpha](wiki/Paper-036-Trading-Volume-Alpha.md) | 2024 | Turns trading volume forecasts into cost-aware rebalancing decisions and evaluates net portfolio performance. | [Paper](https://www.nber.org/papers/w33037) | To verify |

¹ Years refer to the linked preprint or publication version; see [Sources & versions](wiki/Sources-and-Status.md).

## Contribute

Suggest a paper or correct a link through an [Issue](https://github.com/PKU-AFT/quant-paper-wiki/issues/new/choose). Submit reading notes and experiment records through a pull request. See [Contributing](CONTRIBUTING.md).

The editable catalog is [data/papers.json](data/papers.json). Each entry includes primary sources, companion code, a method summary, reading questions and an experiment idea.
