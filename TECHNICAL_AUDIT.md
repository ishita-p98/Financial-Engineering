# Technical audit and validation matrix

**Audit date: 25 November 2026.** This is an evidence-based record of the repository's checks and model reruns. The project is coursework for a fictional All-Kanns insurer and corporate finance risk case studies; it is not an institutional valuation or regulatory opinion.

## Validation status

| Requirement | Status | Evidence |
| --- | --- | --- |
| Scope limited to the assigned B cases | **Complete** | Main README and three project folders. |
| Case 1 code, data handling and risk tests | **Validated components** | Source scripts, saved model outputs and five independent mathematical tests. |
| Case 2 pricing engine | **Validated** | 66 original unit tests passed; NC4 scenario, duration, convexity and KRD rerun against the group's EUR swap curve. |
| Case 3 canonical source | **Pinned and matched** | Integrated scripts are checked byte-for-byte against the public shared course repository during CI. |
| Case 3 optimizer | **End-to-end passed** | Optimized EUR 5bn portfolio, cash-flow coverage, KRD table, report and chart generated. |
| Case 3 policyholder elections | **End-to-end passed** | 0/25/50/75/100% lump-sum sensitivity rerun. |
| Case 3 historical simulation | **End-to-end passed** | 468 overlapping 52-week scenarios with automatic equity-futures overlay. |
| Case 3 Monte Carlo | **End-to-end passed** | Student-t and Gaussian models; full output tables validated. |
| Case 3 receiver-IRS overlay | **End-to-end passed** | HS and MC rerun with 15Y €2.8bn + 30Y €0.3bn receiver swaps. |
| Source workbooks in portfolio repo | **Intentionally excluded** | Retrieved into ephemeral runner; no raw Excel workbooks are published. |
| Automated test workflow | **Passed** | [GitHub Actions](https://github.com/ishita-p98/Financial-Engineering/actions). |

## Case 1 — interest-rate VaR
The historical saved CSV and rerun differ slightly for the PCA + GARCH result. The earlier saved result is €241.48m 10-day 95% VaR; a local rerun gave approximately €240.68m. Delta-Normal and Monte Carlo agree more closely. The discrepancy is documented as version/calibration dependent; no silent replacement was made.

The exposure model uses an assumed five-year aggregate modified duration rather than instrument-by-instrument debt and derivative sensitivities. The results are therefore a simplified case model, not Vonovia's internal VaR.

## Case 2 — callable bond
The final recommendation is **7Y NC4 single-call**. The rerun uses the 31-Aug-2026 EUR swap curve, 15% volatility, Hull–White one-factor tree, mean reversion 3%, 12 steps/year, par call price and €500m notional.

- Bullet par coupon: **325.19bp**
- NC4 single-call par coupon: **340.7931bp**
- Call premium: **15.6031bp**
- Effective duration: **5.1266** callable vs **6.1602** bullet
- Effective convexity: **−83.6835** callable vs **+46.2016** bullet
- Price check: **100.00**

The prior shared NC3 single-call and NC2 Bermudan P&L examples are not NC4 results and are retained only as comparisons.

## Case 3 — All-Kanns

### Optimizer configuration
The two-stage optimizer reports liability PV **€6.41bn**, duration **20.0y**, convexity **472**. For the expanded ZCB/ultra-long universe, it uses 25 bonds, 7 zero-coupon, maximum maturity 94 years. Stage 2 yields an approximate surplus DV01 gap of **−€1.8m/bp** and no PV external top-up. Receiver-swap residual sizing is €2.79bn at 15Y and €0.27bn at 30Y.

### Integrated risk configuration
The integrated risk model reports liability PV **€6.81bn**, assets **€10bn**, surplus **€3.19bn** and funding ratio **1.47**. This liability valuation is different from the optimizer's €6.41bn view and is not combined with it.

| Configuration | 99% 1-year surplus VaR | Other result |
| --- | ---: | --- |
| HS automatic equity-futures overlay | **€1.195bn** | futures short about 13.8% of equity MV |
| HS with receive-fixed IRS, futures pinned to 0% | **€845m** | ES €1.001bn; 2008 replay surplus −€2.603bn |
| MC Student-t, no IRS | **€1.803bn** | 20,000 paths |
| MC Student-t with IRS | **€1.721bn** | 10,000 paths; ES €2.075bn |

These are distinct model configurations and path counts. They should not be interpreted as a controlled experiment varying only one hedge variable.

### Regulatory and economic interpretation
The Solvency II figures remain **illustrative**. They are not a regulator-approved internal model or Standard Formula calculation. The model simplifies risk margin, own-funds treatment, MCR mechanics and real-world insurance governance.

## Reproducibility
The integrated Case 3 GitHub Actions workflow:
1. Clones the canonical public course repository.
2. Verifies the selected Case 3 source files match this portfolio.
3. Loads the matching input workbooks into an ephemeral runner.
4. Runs the two-stage bond optimizer, policyholder elections, historical simulation, Monte Carlo and receiver-swap overlay.
5. Validates expected reports and non-empty numerical outputs.
6. Publishes derived reports, tables and charts without committing raw workbooks.

Latest successful end-to-end run: [Case 3 integrated ALM validation](https://github.com/ishita-p98/Financial-Engineering/actions/runs/45632960847).

## Remaining model limitations
- The Case 1 PCA + GARCH historical output differs slightly from one rerun; source calibration/version should be pinned before treating it as one exact result.
- The optimizer and integrated risk model use different liability PV configurations (€6.41bn and €6.81bn). These are identified separately, not falsely reconciled.
- The MC comparisons above use different path counts and model configurations; do not claim the delta is a pure IRS hedge effect.
- Bloomberg-derived source data are accessed from the public course repository at runtime; the portfolio itself does not distribute those workbooks.
- Source code is retained close to the canonical group implementation to preserve provenance. New validation wrappers and tests are separately identified.

