# Experimental Protocol

[Home](Home.md) · [Reading paths](Reading-Paths.md)

## Experiment specification

| Item | Required record |
| --- | --- |
| Version | Paper version, code commit, patches, dependencies and random seeds |
| Data | Source, access conditions, date range, historical universe, features and label definitions |
| Information timing | Feature availability, label maturity, prediction time and parameter-update time |
| Splits | Training, validation and final test periods; treatment of labels crossing split boundaries |
| Trading assumptions | Rebalancing time, fill prices, suspensions, price limits, shorting/position constraints, fees and impact |
| Search budget | Candidate evaluations, LLM backend, token/currency costs, tuning budget and stopping rule |
| Results | IC/RankIC, returns and risk, turnover, net performance, annual stability and runtime costs |

Use training and validation data for model selection and search decisions. Evaluate the final test period after freezing the design. If its results guide another decision, treat that period as validation.

## Evidence levels

| Status | Evidence required |
| --- | --- |
| Not started | Navigation, reading or an experiment plan only |
| Environment check | Dependencies install and an entry point runs; include commands and logs |
| Method demonstration | Core idea runs on synthetic or substitute data; explain differences from the paper |
| Paper reproduction | Match the paper's experimental conditions and report matches, deviations, results and failures |

Public code does not establish access to the original data. A successful run does not independently validate a return claim.

## Minimum experiment record

| Field | Details to supply |
| --- | --- |
| Paper | Catalog ID and paper version |
| Question | Hypothesis and simple baseline |
| Implementation | Code commit, environment and patches |
| Data | Source, period, universe and information availability |
| Evaluation | Train/validation/test splits and trading/cost assumptions |
| Execution | Commands, seeds and search budget |
| Artifacts | Result files and logs |
| Interpretation | Differences from the paper, failures and the scope of the conclusion |

Reading notes should cite pages, sections or equations. Preserve failures and negative results alongside successful runs.
