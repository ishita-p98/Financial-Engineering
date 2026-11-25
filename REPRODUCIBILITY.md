# Reproducibility and provenance

This is a curated copy of **collaborative group coursework**, not an independent clean-room implementation. The source code and model outputs come from the [shared course repository](https://github.com/benthebender/Financ-Engeneering). The three final presentations determine the selected cases and conclusions.

## Quick environment
Python 3.11+ recommended. Core packages used across the code include NumPy, pandas, SciPy, Matplotlib, openpyxl, pytest and (for some models) scikit-learn, statsmodels, arch, cvxpy and PyYAML. Exact versions were not locked in the original repository; see `requirements.txt` for a starting environment, **not** a guaranteed reproducible lockfile.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Data requirements and honest limits
Some scripts refer to Excel workbooks in the original directory structure, and the larger Bloomberg-derived datasets have **not** been republished in this curated repository. Source code is therefore available for inspection, but **end-to-end execution is not yet self-contained**.

- **Case 1:** `src/Final_version.py` expects `Swap curves.xlsx` in its current working directory. `src/hedge_backtest.py` and other helpers also reference shared curve-loading modules. See the [original shared data folder](https://github.com/benthebender/Financ-Engeneering/tree/main/Data).
- **Case 2:** `src/main.py` expects to find the shared `Swap curves.xlsx` via `curve_io.py` and `swap_curves.py`. The unit tests are included, but running the CLI requires the market-data workbook and original path conventions.
- **Case 3:** The integrated ALM model uses several Excel workbooks for swap curves, bond prices and portfolio optimization, alongside included CSV outputs. The full raw data package and all exploratory scripts have not been copied.

## Verification status
**Published:** selected Python models, callable-bond tests, historical CSV outputs, detailed assumptions and result documentation.

**Not claimed:** that all models have been rerun successfully in this reorganized folder layout, that historical market data can be freely redistributed, or that the results constitute live investment prices or regulatory certifications.

## Model variants
The shared repository contains multiple model iterations. Do not combine results from different valuation dates, liability definitions, portfolio deployment states, hedges or confidence levels. In particular, the Case 3 `€6.41bn` and `€6.81bn` liability PV views and the 99% / 99.5% VaR views are not the same configuration.

## Attribution
Group work is credited collectively. The original source repository is linked for transparency. Any changes made specifically for the portfolio should be identified separately from the group's historical deliverables.
