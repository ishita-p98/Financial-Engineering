# Surplus risk, scenario analysis and illustrative solvency

## Why surplus risk is the objective
For a life insurer, a change in bond prices cannot be judged in isolation. Lower rates can increase the PV of long-dated guarantees even as fixed-income assets appreciate. The relevant economic quantity is **surplus = market value of assets − present value of liabilities**.

A receive-fixed IRS can increase gross asset sensitivity while reducing **surplus** sensitivity. This is the central reason the group recommended a liability-aware overlay.

## Reported risk-model outputs
The final presentation and supporting models include:
- Historical simulation using overlapping one-year windows of weekly market-factor changes.
- VaR and Expected Shortfall for assets and economic surplus.
- Rate, equity, credit, FX and longevity scenarios.
- Monte Carlo paths incorporating heavier-tailed innovations and a stochastic-volatility/VIX layer.
- A proposed equity futures overlay controlled by an economic risk budget.

One documented supporting run reports **99% one-year surplus VaR falling from about €1.21bn to €0.85bn after the receiver-IRS overlay**, roughly a **30% reduction**. The presentation also shows a **99.5% one-year** risk/SCR view, with a reported **€0.94bn** SCR and approximately **340%** solvency ratio. These figures have **different confidence levels and configurations**; they should not be conflated.

## Risk budget and equity overlay
The presentation describes approximately **€3.19bn economic surplus** and a board funding-ratio floor of **1.20**, used to derive a tolerable loss budget. In the recommended configuration, the **equity-futures hedge is 0%** because the interest-rate overlay is presented as sufficient to bring surplus risk within the limit. Other model runs explore dynamic equity hedging.

## Stress testing
The shared scenario suite includes:
- EUR rates ±100bp and ±200bp,
- equity drawdowns of 20–40%,
- high-yield spread widening,
- 2008- and 2022-style combined shocks,
- and a longevity shock.

These are deterministic or historical-replay scenarios, **not forecasts**. The presentation also explores 15-year portfolio outcomes and funding under different lump-sum elections.

## Solvency II interpretation
The supporting report uses **own funds ≈ economic surplus** and **SCR ≈ 99.5% one-year internal-model surplus VaR**, producing a headline solvency ratio near **340%** with the receiver overlay. It estimates MCR from a simplified regulatory corridor.

This is **not an independently validated Solvency II Standard Formula calculation or regulatory submission**. The shared documentation explicitly notes omitted or simplified risk margin, expected profits in future premiums and MCR components.

## Model limitations worth discussing in interviews
- **Historical dependence:** risk-factor correlations and volatility can shift under stress.
- **Overlapping scenarios:** one-year windows are not statistically independent.
- **Long-end extrapolation:** liabilities extend beyond readily observable swap maturities.
- **Repricing approximation:** bond shocks use duration/convexity in some model variants, while liabilities are more fully repriced.
- **Credit/liquidity:** government/SSA spread risk, collateral calls and forced liquidation can matter.
- **Election and mortality assumptions:** cohort behavior may differ from a fixed 50/50 base case.
- **Profit sharing:** policyholder distributions alter the insurer's retained asset path.

**Sources:** Final presentation, risk map, risk budget, stress testing and recommendation slides; shared Case 3 historical simulation, Monte Carlo and Solvency II reports.

[Back to Case 3](README.md)
