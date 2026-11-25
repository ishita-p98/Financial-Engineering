# Case 1b — Corporate interest-rate risk: present-value VaR

**Client: Vonovia SE | Final Group 2 presentation: 23 pages**

## Mandate and decision
The group presented a corporate treasury risk-management framework for Vonovia. The deck describes approximately **€31.4bn of financial liabilities**, including around **€14bn of floating-rate bank debt**. A +100bp move would imply approximately **€140m in additional annual interest cost** on €14bn of unhedged floating exposure; this is a **cash-flow sensitivity**, not the same metric as present-value VaR.

The assigned question was specifically **1b, interest-rate risk from a present-value perspective**, not the other Case Day 1 presentation topics. The common swap/forward-swap exercises support the hedging discussion.

## Methodology
The modelling uses historical EUR par swap curves (1Y–10Y), with independently cleaned tenor observations, rate changes and covariance estimation. The core model treats approximately €31.39bn of identified debt as a simplified rate-sensitive portfolio with an **assumed aggregate modified duration of 5 years**; it is not a security-by-security reconstruction of Vonovia's liabilities and derivatives.

Three models were compared at a **95% confidence level over ten trading days**:

| Model | 10-day VaR | Expected Shortfall |
| --- | ---: | ---: |
| Delta-Normal | €287.64m | €360.71m |
| Correlated Monte Carlo (100,000 simulations) | €288.31m | €362.55m |
| PCA + GARCH-style conditional volatility | €241.48m | €324.79m |

The three principal curve factors are reported to explain **99.34%** of standardized historical variation. These model outputs depend on the duration assumption, risk-factor mapping and historical calibration window.

## Validation and hedge selection
The final presentation includes backtesting rather than relying on in-sample VaR alone:

| Model | Reported breach rate | Target |
| --- | ---: | ---: |
| Delta-Normal | 7.6% | 5.0% |
| Monte Carlo | 11.4% | 5.0% |
| PCA + GARCH | 5.8% | 5.0% |

The group favored the conditional-volatility model **for this backtest**; it is not universally superior. It also compared spot and forward swap hedges. The final presentation recommends a **five-year spot payer interest-rate swap**, reporting a hedged VaR of approximately **€16m**, about **84% lower** than the unhedged backtest benchmark. A *payer* swap (pay fixed, receive floating) is the economically relevant hedge against floating-rate debt. The swap has approximately zero PV at inception, not zero future economic cost.

## What matters to a treasury
- Separate **earnings/cash-flow risk** from **PV risk**.
- Check model calibration and observed breach frequency, not just a VaR point estimate.
- Treat VaR as a loss quantile, **not a maximum loss**; use Expected Shortfall and stress tests for the tail.
- Compare hedge choices against maturity structure, basis risk, collateral, accounting and execution constraints.
- Recognize that using an assumed duration limits firm-specific precision.

## Actual model outputs

![Original group VaR method comparison](https://raw.githubusercontent.com/benthebender/Financ-Engeneering/main/output/charts/10_var_method_comparison.png)

*Source: shared group modelling repository; chart is linked, not recreated.*

![Original group hedge backtesting](https://raw.githubusercontent.com/benthebender/Financ-Engeneering/main/output/charts/12_hedge_var_backtest.png)

*Source: shared group modelling repository.*

[Inspect the model code, backtesting data and execution notes](IMPLEMENTATION.md).

## Evidence and source
- Final presentation: *Interest Rate Risk — Present Value View*, Group 2, especially slides on VaR methodologies, backtesting, hedge effectiveness and final recommendation.
- Shared implementation: [Vonovia conclusion and model outputs](https://github.com/benthebender/Financ-Engeneering/blob/main/output/Conclusion.md), [VaR core](https://github.com/benthebender/Financ-Engeneering/blob/main/var_core.py), [hedge backtest](https://github.com/benthebender/Financ-Engeneering/blob/main/hedge_backtest.py).

*The figures are historical group-model outputs, not Vonovia's published internal VaR. No independent rerun is claimed.*

[Back to main README](../README.md)
