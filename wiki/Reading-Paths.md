# Reading Paths

[Home](Home.md) · [Full index](All-Papers.md)

## Research tracks

| Track | Papers | Research question | Suggested output |
| --- | --- | --- | --- |
| Labels & baselines | [Label Horizon](Paper-013-Label-Horizon.md), [StockMixer](Paper-015-StockMixer.md) | At a fixed evaluation horizon, what comes from label design and what comes from architecture? | Data specification, time splits and a controlled baseline comparison |
| Market adaptation | [DoubleAdapt](Paper-017-DoubleAdapt.md), [DSOF](Paper-019-DSOF.md) | Do gains come from continual updates or model complexity? Does evaluation respect label arrival? | Prediction/update timeline, rolling-retraining baseline and computation costs |
| Automated factor research | [RD-Agent-Quant](Paper-002-RD-Agent-Quant.md), [Alpha Jungle](Paper-003-Alpha-Jungle.md), [AlphaPROBE](Paper-004-AlphaPROBE.md) | Under equal budgets, does automation produce more effective, less redundant factors? | Experiment ledger, search costs, deduplication and held-out results |
| Microstructure signals | [OFI](Paper-033-OFI-Cross-Impact.md), [DeepLOB](Paper-011-DeepLOB.md) | Does a complex model improve on simple order-book signals after execution costs? | Separate contemporaneous and predictive results, with latency/cost sensitivity |
| Risk & execution | [Graph-based HAR](Paper-030-Graph-HAR.md), [Trading Volume Alpha](Paper-036-Trading-Volume-Alpha.md) | Can risk and volume forecasts improve net performance under matched constraints? | Risk calibration, turnover, tracking error and net portfolio comparisons |

## Match the track to available data

| Available data | Candidate topics | Checks before starting |
| --- | --- | --- |
| Daily prices and volume | Label horizons, simple predictors, momentum and online adaptation | Check each paper's feature and label requirements |
| Historical industry or concept memberships | HIST, relational models and factor models | Use point-in-time membership snapshots |
| Limit order books | OFI and DeepLOB | Define event ordering, prediction time, latency and fill assumptions |
| Realized volatility or high-frequency prices | HAR, GNNHAR, covariance and tail risk | Check licensing, sampling rules and timestamp alignment; label substitute-data work as a transfer experiment |

## Reading note fields

| Field | Record |
| --- | --- |
| Question | What problem does the paper address? |
| Information set | What are the inputs, outputs and information available at inference? |
| Baseline | What is the simplest credible comparison? |
| Evidence | Which pages, sections, equations and tables support the method and claims? |
| Next experiment | What bounded comparison can be completed with available data? |

Track reading progress separately from experiment completion.
