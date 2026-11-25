# Implementation and model validation

## Source files
- [Final_version.py](src/Final_version.py): historical EUR curve cleaning, VaR and scenario analytics.
- [var_core.py](src/var_core.py): rate-factor panel, covariance, scenario generation and VaR/ES utilities.
- [hedge_backtest.py](src/hedge_backtest.py): historical backtesting and hedge comparisons.
- [swap_curves.py](src/swap_curves.py), [forward_swap.py](src/forward_swap.py): curve loading and bootstrapping helpers.

## Inspect the results
- [Base-case VaR](results/base_case_var_results.csv)
- [Backtest breaches](results/hedge_backtest_breaches.csv)
- [Hedge comparison](results/hedge_backtest_savings.csv)

## Technical interpretation
A 95% ten-day VaR estimate is a conditional loss threshold, not a maximum possible loss. Delta-Normal and covariance Monte Carlo may agree closely under linear duration exposures; PCA with conditional volatility can differ because it responds to volatility regimes. Backtesting is essential: the presentation reports 7.6%, 11.4% and 5.8% breach rates against a 5% nominal target.

**Sign convention:** a pay-fixed/receive-floating interest-rate swap can hedge floating-rate borrowing costs. Receiver swaps are not equivalent protection against rising floating borrowing costs. The portfolio's **present-value** exposure and **cash-flow** exposure must still be analysed separately.

## Limitations
The original aggregate duration was assumed at five years, not derived from all debt instruments. The included scripts retain their original workbook paths and may require the original Bloomberg data files. The figures have not been independently recalculated after reorganization.

[Back to Case 1](README.md)
