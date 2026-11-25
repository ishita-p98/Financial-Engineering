# Callable-bond implementation and tests

## Source structure
- [main.py](src/main.py): CLI to compare maturity, call dates and single/Bermudan structures.
- [curve_io.py](src/curve_io.py): market curve input and discount-factor bootstrap.
- [engine.py](src/engine.py): Hull–White trinomial tree and Black single-call comparison.
- [pricer.py](src/pricer.py): par-coupon root solving and call-date ladder.
- [scenarios.py](src/scenarios.py): issuer P&L, effective duration/convexity and key-rate DV01.
- [plots.py](src/plots.py): figures.
- [Unit tests](src/tests/test_pricer.py): par pricing, curve fit, exercise structure and option-value checks.

## Final presentation versus comparison
The final recommendation is **7Y NC4 single-call**. The [reproduced NC4 coupon ladder](results/nc4_single_coupon_ladder.csv) shows the 7Y NC4 model coupon at **340.7931bp** versus a **325.19bp** bullet coupon. NC4 scenario, effective-risk and key-rate outputs are preserved under `results/`. The source repository also includes a 7Y NC3 single-call scenario analysis and a 7Y NC2 Bermudan analysis; neither should be presented as the selected final deal.

## Run (with source workbook available)
From the `src/` directory, and with the original curve workbook accessible to `curve_io.py`:

```bash
python main.py --maturities 7 --nc 4 --call-type single --vol 0.15 --nc-table
python main.py --maturities 7 --nc 4 --call-type single --vol 0.15 --scenarios
python -m pytest -q
```

The curve and volatility inputs are **coursework assumptions and historical data**, not an issuer-specific market-calibrated credit and swaption surface. No claim is made that the commands were rerun in this repackaged repository.

[Back to Case 2](README.md)
