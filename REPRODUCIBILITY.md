# Reproducibility and validation

**Updated 25 November 2026.** This repository contains three collaborative Financial Engineering case studies. The quantitative implementations and selected results are documented with clear distinctions between group-presentation figures, original saved outputs and fresh reruns.

## Executed validation

| Area | Result | Evidence |
| --- | --- | --- |
| Python syntax | **Passed** | 33 Python files in the uploaded course archive parsed without syntax errors. |
| Callable-bond unit tests | **66 passed** | Original course test suite executed in the extracted archive with its shared curve modules available. |
| Mortality component tests | **10 passed** | Original actuarial mortality test suite. |
| VaR mathematical tests | **5 passed** | Synthetic tests for covariance projection, Gaussian scenarios, horizon aggregation and loss-tail measures. |
| Synthetic ALM identities | **11 passed** | Guarantee accumulation, election fractions, discounting, duration, key-rate DV01 and surplus sign. |
| Callable NC4 pricing | **Repriced** | Seven-year, NC4, single-call, 15% volatility, 31-Aug-2026 EUR swap curve. Price check = 100. |
| Integrated Case 3 | **Successful end-to-end run** | GitHub Actions run [#45632960847](https://github.com/ishita-p98/Financial-Engineering/actions/runs/45632960847). |
| Case 3 two-stage optimizer | **Passed output checks** | Full EUR 5bn allocation, portfolio/KRD outputs, cash-flow report and chart generated. |
| Case 3 election sensitivity | **Passed** | Re-optimized 0%, 25%, 50%, 75% and 100% lump-sum elections. |
| Case 3 historical simulation | **Passed** | 468 overlapping one-year scenarios; tagged outputs and stress results generated. |
| Case 3 Monte Carlo | **Passed** | Student-t and Gaussian paths generated and validated. |
| Case 3 receiver-IRS overlay | **Passed** | Final-presentation 15Y/30Y receive-fixed overlay rerun under HS and MC. |
| GitHub CI | **Passed** | Latest synthetic/pricing/mortality test workflow completed successfully. |

## Canonical Case 3 implementation

The selected implementation is the later integrated shared-course version:
- `case3_model.py` — liabilities, portfolios, FX, futures, historical simulation, Monte Carlo, VIX/Heston and stress tests.
- `cashflow_match_v2.py` — two-stage cash-flow dedication and key-rate DV01 optimization.
- `alm_fixed_income_.py` — curve, liability, bond-universe and analytics helpers.
- `return_book.py` — contribution deployment and the 90/10 profit-sharing projection.

The GitHub Actions workflow clones the public shared course repository at run time, checks that the canonical source files match this portfolio copy, and runs the model using the corresponding workbooks in an ephemeral runner. Raw workbooks are **not committed** to this repository. The resulting derived reports and tables are published under [Case 3 reproduced outputs](03-life-insurance-alm/reproduced/).

## Reproduced Case 3 results: keep configurations separate

### Fixed-income optimizer
The run using the two-stage KRD optimizer reports a liability PV of **€6.41bn**, liability duration **20.0 years**, and liability convexity **472**. With the expanded ZCB/ultra-long bond universe, Stage 2 uses 25 instruments (7 zero-coupon, longest maturity 94 years), achieves an approximately **€1.8m/bp surplus DV01 gap**, and reports **zero PV external top-up**. The residual receiver-swap sizing is approximately **€2.79bn at 15Y and €0.27bn at 30Y**.

### Integrated market-risk engine
The integrated risk engine uses a separate liability valuation setup and reports liability PV **€6.81bn**, assets **€10.0bn** and economic surplus **€3.19bn**. Do not combine its risk values with the optimizer's €6.41bn liability PV as though they were a single valuation snapshot.

- **HS, automatic equity-futures overlay:** 1-year 99% surplus VaR **€1.195bn**; applied equity-futures short about **13.8%**.
- **HS, receiver-IRS overlay, no equity-futures overlay:** surplus VaR **€845m**, ES **€1.001bn**; 2008 replay surplus P&L **−€2.603bn**. The overlay is 15Y €2.8bn and 30Y €0.3bn receive-fixed.
- **MC, no IRS overlay:** Student-t 20,000-path 1-year 99% surplus VaR **€1.803bn**.
- **MC, receiver-IRS overlay:** Student-t 10,000-path surplus VaR **€1.721bn**, ES **€2.075bn**.

These outputs correspond to **different risk configurations and path counts**. The difference between them must not be interpreted as a pure hedge effect without matching every setting.

## Case 2 — final NC4 single-call rerun

The final presentation selects **7Y NC4 single-call**, not the NC3 or NC2 Bermudan examples. On the saved 31-Aug-2026 EUR curve and the group's Hull–White assumptions, the model reprices the coupon at **340.7931bp**, versus **325.19bp** for the bullet. Effective duration is **5.13** versus **6.16**, and effective convexity is **−83.68** versus **+46.20**. NC4-specific scenario and key-rate CSVs are included in the repository.

## Market data and licensing

Bloomberg-derived and other workbook inputs remain outside this public repository. The integration workflow obtains the publicly available source workbooks from the shared course repository into a temporary runner; it publishes only derived outputs and no raw workbooks. This setup relies on the continued public availability and permissions associated with the source repository. The models should not be represented as independent Bloomberg-data validation or regulatory certification.

## What the tests do and do not establish

Tests verify selected code paths, mathematical identities, model output structure and key constraints. They do not prove that the financial assumptions are economically correct, that historical input data are error-free, or that simplified models meet regulatory standards. The All-Kanns insurer is fictional and the Solvency II analysis is illustrative, not a regulatory submission.

## Running the checks

- Lightweight tests: `python -m unittest discover -s tests -p "test_*.py" -v`
- Callable bond: from `02-callable-bond/src`, run `python -m pytest -q tests`
- VaR mathematical tests: from `01-interest-rate-risk-var/src`, run `python -m pytest -q tests/test_risk_math.py`
- Mortality tests: `python -m pytest -q 03-life-insurance-alm/src/test_mortality.py`
- Full Case 3 optimization and risk pipeline: use the [Case 3 integrated ALM GitHub Actions workflow](.github/workflows/case3-integrated-validation.yml). Its generated summaries are published to the Case 3 `reproduced/` folder.
