# Technical audit and validation matrix

**Updated 25 November 2026.** The project is a curated copy of collaborative coursework. This page separates tests that have actually run from model outputs that still need a source-data rerun.

## Latest automated validation

The GitHub Actions workflow now requests syntax parsing and the original callable-bond, VaR and mortality suites, in addition to the synthetic financial checks. **Workflow publication is not evidence of a successful run.** Verify the latest commit in [Actions](https://github.com/ishita-p98/Financial-Engineering/actions/workflows/synthetic-tests.yml). The integrated Case 3 model is not covered by these data-independent checks.

## Executed checks

| Component | Status | Evidence and scope |
| --- | --- | --- |
| Callable-bond pricing | **66 unit tests passed** | Run in the extracted original course archive, with shared modules present. Not a clean clone of this reorganized repository. |
| Mortality model | **10 unit tests passed** | Standalone actuarial component in the original archive. |
| VaR mathematical functions | **5 tests passed** | Synthetic covariance, scenario generation, VaR/ES and horizon invariants in a local validation environment. |
| Cross-case financial invariants | **6 tests passed** | Synthetic, data-independent tests: guarantee accumulation, par bullet, call-option value, surplus identity and tail ordering. Run locally with Python's unittest. |
| Original Case 1 VaR script | **Executed with original workbook** | Historical inputs available in the uploaded archive. Not an independent audit of the reported financial exposure. |
| Full Case 3 integrated ALM | **Not yet validated** | The uploaded course archive lacks the later integrated `case3_model.py` and `cashflow_match_v2.py` source revisions found in the shared GitHub repository. Reproducing their reported outputs requires the exact input workbooks, model versions and run configurations. |

## Results reconciliation: what must not be mixed

### Case 1 — Vonovia
The saved CSV gives Delta-Normal **€287.64m**, Monte Carlo **€288.31m**, and PCA + GARCH **€241.48m** 10-day 95% VaR. A prior local run yielded approximately **€240.68m** for the PCA + GARCH result. The source code and model inputs must be version-matched before calling this difference resolved. A VaR backtest breach rate is not proof of predictive accuracy without sample size and test details.

### Case 2 — Callable bond
The final pitch selected **7Y NC4 single-call**, with model coupon **340.79bp** versus **325.19bp** bullet. The saved **NC3** scenario output and **NC2 Bermudan** scenario output are *not* the final NC4 scenario results. Their rate-shock P&L figures must not be presented as NC4 P&L. The pricing model assumes an annual single curve and uncalibrated short-rate volatility.

### Case 3 — All-Kanns
Different saved configurations report **€6.41bn** and **€6.81bn** guaranteed-liability PV, and different 99% historical-simulation versus 99.5% capital views. The 15-year IRR, election mix, investment deployment and receive-fixed IRS overlay must all be fixed before comparing model outputs. The simplified Solvency II figures are not a regulatory filing.

## Reproducibility without licensed market data

- Keep Bloomberg-derived raw workbooks out of this public repository pending permission.
- Preserve original group source links and record which models require workbooks.
- Use synthetic tests for mathematical identities; do not present them as validation of market calibration.
- Do not silently modify historical numerical outputs. Record any corrected version separately, including input date, model settings, tests and original comparison.
- Use the [reproducibility guide](REPRODUCIBILITY.md) to distinguish inspectable code from an independently reproducible pipeline.

## Chart integrity
The six original chart paths embedded in the case READMEs were checked against the shared course repository's file tree. They exist there, but the figures are **externally hosted** rather than committed to this repository.

## Remaining engineering tasks
A full clean-clone build, integrated Case 3 rerun, lint/refactor across all Python files and a complete numerical reconciliation **remain open**. The source archive and shared repository contain different revisions of Case 3; selecting and pinning a consistent model/data snapshot is required before claiming those tasks complete.
