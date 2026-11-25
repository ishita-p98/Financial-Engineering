# Reproducibility and provenance

This is a curated copy of **collaborative group coursework**, not an independent clean-room implementation. The source code and model outputs come from the [shared course repository](https://github.com/benthebender/Financ-Engeneering). The three final presentations determine the selected cases and conclusions.

## Quick environment
Python 3.11+ recommended. Core packages used across the code include NumPy, pandas, SciPy, Matplotlib, openpyxl, pytest and (for some models) scikit-learn, statsmodels, arch, cvxpy and PyYAML. Exact versions were not locked in the original repository; see `requirements.txt` for a starting environment, **not** a guaranteed reproducible lockfile.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Canonical Case 3 model selection

Use **only the later integrated implementation** in the shared GitHub repository (`case3_model.py` + `cashflow_match_v2.py`) as the primary Case 3 model. The earlier archive versions are superseded and will not be combined with its results. Standalone mortality tests remain component-level evidence, not validation of the integrated pipeline. A complete end-to-end rerun still requires the matching workbooks.

## Data requirements and honest limits
Some scripts refer to Excel workbooks in the original directory structure, and the larger Bloomberg-derived datasets have **not** been republished in this curated repository. Source code is therefore available for inspection, but **end-to-end execution is not yet self-contained**.

- **Case 1:** `src/Final_version.py` expects `Swap curves.xlsx` in its current working directory. `src/hedge_backtest.py` and other helpers also reference shared curve-loading modules. See the [original shared data folder](https://github.com/benthebender/Financ-Engeneering/tree/main/Data).
- **Case 2:** `src/main.py` expects to find the shared `Swap curves.xlsx` via `curve_io.py` and `swap_curves.py`. The unit tests are included, but running the CLI requires the market-data workbook and original path conventions.
- **Case 3:** The integrated ALM model uses several Excel workbooks for swap curves, bond prices and portfolio optimization, alongside included CSV outputs. The full raw data package and all exploratory scripts have not been copied.

## Latest independently executed checks — 25 November 2026

I extracted the supplied `Financial Engineering.zip` and ran the original course tests in the execution environment:

- Callable-bond test suite: **66 passed** (8.79 seconds), with the archived shared `Case 1/Data` modules available.
- Mortality-model test suite: **10 passed** (2.12 seconds).
- Portfolio synthetic financial invariants: **6 passed** using Python `unittest`.

The callable-bond folder now contains local copies of the shared `forward_swap.py` and `swap_curves.py` dependencies, making its Python imports self-contained. **This does not make the Bloomberg curve workbook available** and does not establish a clean-clone run of the pricing CLI.

The original uploaded archive contains an earlier Case 3 model set than the shared GitHub repository's integrated `case3_model.py` and `cashflow_match_v2.py`. A complete integrated ALM run and numerical reconciliation have **not** been executed or validated. Do not interpret published VaR, solvency or IRR estimates as newly independently verified.

## Validation update — 25 November 2026

The supplied course archive was inspected locally and the following checks were run:

| Check | Result | Scope |
| --- | --- | --- |
| Callable-bond `pytest` suite | **66 passed** | Original archive layout with shared `forward_swap.py` available |
| Mortality `pytest` suite | **10 passed** | Standalone demographic model |
| VaR mathematical-invariant tests | **5 passed** | Gaussian VaR/ES, empirical tails, PSD covariance, simulated covariance and horizon aggregation |
| Original Case 1 `Final version.py` | **Completed successfully** | Supplied local Bloomberg workbook; source output is not independently audited |
| Syntax parsing of archive Python files | **33 parsed, 0 syntax errors** | Syntax only, not execution |

**Important calibration discrepancy:** The locally rerun Case 1 model produced PCA + GARCH VaR of approximately **€240.68m** and ES of **€322.63m**, while the historical CSV committed in this repository records **€241.48m** and **€324.79m**. Delta-Normal and Monte Carlo figures agree closely. Until calibration inputs and code revisions are reconciled, the PCA + GARCH results should be treated as **version-dependent**, not a single verified figure.

The published Case 1 curve loader has been modified to avoid loading licensed market data merely on import. The new five-test VaR suite is committed in `01-interest-rate-risk-var/src/tests/`. **These tests have not yet been executed from a fresh clone of this exact GitHub commit.**

**Outstanding:** run the integrated Case 3 optimization/Monte Carlo workflow with its full source workbooks and dependencies; validate final presentation figures against consistent model configurations; refactor and lint all Python modules; establish a fully self-contained, clean-clone execution path.

## Verification status
**Published:** selected Python models, callable-bond tests, historical CSV outputs, detailed assumptions and result documentation.

**Validation performed locally on the supplied course archive:** the callable-bond suite passed **66 tests** with the shared curve modules available; the independent mortality suite passed **10 tests**. All **33 Python files** extracted from the available archive passed syntax parsing. These tests do **not** validate the full Case 1 historical backtest, the integrated Case 3 ALM pipeline, market-data integrity or agreement with all presentation figures. The callable-bond suite was tested with its original archive layout and a shared-module search path, not by executing a clean GitHub clone.\n\n**Not claimed:** that all models have been rerun successfully in this reorganized folder layout, that historical market data can be freely redistributed, or that the results constitute live investment prices or regulatory certifications.

## Model variants
The shared repository contains multiple model iterations. Do not combine results from different valuation dates, liability definitions, portfolio deployment states, hedges or confidence levels. In particular, the Case 3 `€6.41bn` and `€6.81bn` liability PV views and the 99% / 99.5% VaR views are not the same configuration.

## Attribution
Group work is credited collectively. The original source repository is linked for transparency. Any changes made specifically for the portfolio should be identified separately from the group's historical deliverables.
