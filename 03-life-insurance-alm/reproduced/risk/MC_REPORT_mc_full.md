# Case 3b - Monte-Carlo 1-year 99% VaR  (full)

20,000 paths x 52 weekly Student-t (dof 5) steps, PCA curve, Heston stochastic vol + leverage. Book repriced with the HS engine.

- assets EUR 10.00bn | liability PV EUR 6.81bn | economic surplus EUR 3.19bn
- equity 99% 1y VaR limit EUR 201m | unhedged equity VaR EUR 1,405m -> hedge 85.7%

## MC VaR / ES (1-year, EUR)

| model | Asset VaR | Asset ES | Surplus VaR | Surplus ES |
|---|--:|--:|--:|--:|
| student_t_nu5 | 2,284.0m | 2,429.9m | 1,803.0m | 1,922.6m |
| gaussian | 2,290.6m | 2,410.9m | 1,803.7m | 1,944.4m |

## VIX (Heston kappa 4.0, theta 0.028, xi 0.65, rho -0.75)

VIX_t = 100 sqrt(A(tau) v_t + (1-A) theta), A(tau) = 0.852.

- median VIX terminal / path-max: 13.6 / 27.5  (99th-pct path-max 50.4)
- corr(path-max VIX, 1y equity return): -0.42
- VIX at the crash week: 23.7 (all) vs **41.9** (99% equity tail)
- share of 99%-tail paths with VIX > 40 / > 50 at the crash week: 64% / 16%

=> VIX spikes coincide with the crash paths -> a VIX-gated no-trade band (`vix_gated_band`) is meaningful.
