# ALM implementation map

This is the portfolio's most substantial technical workstream. The files below are **selected group source code**, not individually authored claims.

## Validated actuarial component\n\nThe [mortality model](src/mortality.py) and its [10 unit tests](src/test_mortality.py) were checked against the supplied course archive: **10 passed**. Its [assumptions](MORTALITY_MODEL.md) and [example summary](results/mortality_summary.txt) are included. This is a standalone demographic component; it does not validate the integrated ALM or liability model.\n\n## Selected implementation

**Canonical:** the later integrated shared-GitHub version, centered on `case3_model.py` and `cashflow_match_v2.py`. It is the more complete implementation because it connects liability cash flows, dedicated bond optimization, the return book, derivative overlays and portfolio risk in one framework. The earlier course-archive prototypes are excluded from the main analytical narrative. The separately tested mortality component is supplementary.

This selection is based on documented model scope, **not** on a successful integrated execution. Reported results remain attributed to their saved configurations.

## Latest end-to-end run\n\nThe [integrated Case 3 GitHub Actions workflow](../../.github/workflows/case3-integrated-validation.yml) successfully ran the optimizer, policyholder election sensitivity, historical simulation, Monte Carlo and final-presentation receiver-IRS overlay. Reproduced reports and derived outputs are committed under [reproduced/](reproduced/). The workflow obtains the source workbooks from the public shared course repository in an ephemeral runner; raw Excel files are not stored here.\n\n## Model architecture
| Step | Code / output | Purpose |
| --- | --- | --- |
| 1. Liability cash flows | [case3_model.py](src/case3_model.py) | 1% guarantee, year-15 elections, pension tail and liability valuation |
| 2. Fixed-income optimization | [cashflow_match_v2.py](src/cashflow_match_v2.py) | Cash-flow dedication, KRD matching, constrained bond holdings |
| 3. Return-seeking sleeve | [return_book.py](src/return_book.py) | Contribution deployment, rebalancing, 90/10 profit sharing |
| 4. Full risk engine | [case3_model.py](src/case3_model.py) | Historical simulation, Monte Carlo, funding and stress analysis |
| 5. Life-cycle sensitivity | [mc_lifecycle.py](src/mc_lifecycle.py) | Stochastic long-horizon outcomes and election liquidity |
| 6. Derivatives | [futures.py](src/futures.py), [fx.py](src/fx.py), [vix.py](src/vix.py) | Equity futures, currency swaps and volatility modelling |

## Published model evidence
- [Fixed-income optimization report](results/fixed_income_optimization.md)
- [Bond allocations](results/portfolio_wide.csv) and [key-rate DV01](results/krd_wide.csv)
- [Policyholder election sensitivity](results/election_sensitivity.csv)
- [Receiver-IRS risk results](results/hedged_surplus_risk.md)
- [Monte Carlo life-cycle report](results/monte_carlo_lifecycle.md)
- [Illustrative Solvency II](results/solvency_ii.md)
- [Risk methodology and assumptions](VAR_METHODOLOGY.md)

## Analytical logic
The initial €5bn funds a **guarantee-matching fixed-income sleeve**, while the ten future €0.5bn contributions finance a **return-seeking sleeve**. The bond optimizer matches contractual cash flows and tenor-specific rate sensitivities; the receiver-IRS overlay addresses residual liability duration. Surplus VaR evaluates **asset minus liability P&L**, not asset P&L alone.

A key result is the reported reduction in one-year 99% surplus VaR from approximately **€1.21bn to €0.85bn** after a receive-fixed swap overlay, for one particular deployment/model configuration. The 99.5% SCR-based solvency calculation is **a different risk view**.

## Execution and data limitations
The shared integrated model expects Bloomberg-derived EUR/USD swap workbooks, fixed-income basket data and portfolio optimization workbooks that are not reproduced in this curated folder. Therefore the source is inspectable and results are documented, but **the complete end-to-end pipeline is not independently reproducible from this repository alone**.

For source workbooks and additional historical runs see the [original shared Case 3 directory](https://github.com/benthebender/Financ-Engeneering/tree/main/Case%203). Redistribution permissions and any identifying metadata should be checked before moving raw files into a public portfolio.

[Back to Case 3](README.md)
