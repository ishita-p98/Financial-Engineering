# Case 2b — Pricing callable debt and refinancing flexibility

**Client: Vonovia SE | Final Group 2 presentation: 18 pages**

## The final recommendation — 7Y NC4, single call
The group's final client pitch recommended a **seven-year fixed-rate bond with one issuer call at par at the end of year four (NC4)**. This is the presentation's selected structure. The shared code also evaluates NC2, NC3 and Bermudan alternatives, but **those are comparisons, not the final recommendation**.

| Item | Reported value |
| --- | ---: |
| Seven-year bullet par coupon | 3.2519% |
| Seven-year NC4 single-call par coupon | **3.4079%** |
| Coupon premium for call optionality | **15.60 basis points** |
| Volatility input | 15% |
| Model | Hull–White one-factor trinomial tree |
| Exercise | Single call at year 4, at par |

The final presentation describes the premium as the cost of retaining the option to refinance early if rates decline. I independently reran the group's Hull–White engine for the selected **NC4 single-call** structure at the stated curve date and €500m notional; the NC4-specific outputs are published below. This avoids reusing scenario results from NC2 Bermudan or NC3 single-call comparisons.

## Why an issuer pays for a call
A bullet bond provides fixed-rate certainty but no contractual early-redemption right. A callable bond adds the issuer's option to redeem at a predetermined price. That option benefits the issuer when the continuation value of the outstanding bond exceeds the call price, often when market rates fall.

**Investor perspective:** the bondholder is short the issuer's call and requires compensation in the coupon. **Issuer perspective:** the coupon premium buys contingent refinancing flexibility. The premium is paid even if the call is never exercised.

## Pricing logic
Under a simplified credit-free, single-curve framework:

```text
Value of callable debt to the investor
  = value of otherwise equivalent bullet bond
    - value of issuer's embedded call
```

The engine bootstraps discount factors from annual par swap rates. A Hull–White short-rate lattice is fitted to the initial curve; backward induction imposes the optimal issuer exercise decision at eligible dates. A root finder solves the coupon that prices the callable instrument at 100.

A **European receiver swaption** provides a useful analytical comparison for a single-call structure, although the synthetic and embedded forms need not be identical after credit spreads, funding terms, settlement and counterparty risks are introduced.

## Why NC4 rather than maximum flexibility?
The group framed the choice as an **economic trade-off**, not simply maximizing the number of call dates. Earlier or repeated exercise opportunities generally increase option value and required coupon compensation. NC4 was pitched as targeted refinancing flexibility tied to the client's financing needs, rather than paying continuously for every possible call window.

For comparison, the shared code's single-call ladder reports coupons of **3.5111% at NC2, 3.4652% at NC3, 3.4079% at NC4, 3.3537% at NC5 and 3.3010% at NC6**, under its stated curve and model settings.

## Reproduced NC4 scenario results\n\nThe rerun used the uploaded group model, EUR swap curve dated **31 August 2026**, 15% Black volatility input, Hull–White mean reversion of 3%, 12 tree steps per year, par call price and €500m notional. The model solves the NC4 coupon to par and applies the specified deterministic curve scenarios.\n\n| Measure | NC4 single-call result | Bullet comparison |\n| --- | ---: | ---: |\n| Par coupon | **3.4079%** | 3.2519% |\n| Coupon premium | **15.60bp** | — |\n| Initial issuer call value | **0.9647 points** | — |\n| Effective duration | **5.13** | 6.16 |\n| Effective convexity | **−83.68** | +46.20 |\n| DV01 on €500m | **€256,332/bp** | €310,983/bp |\n\nUnder a **100bp rate fall**, the callable instrument's issuer P&L is approximately −€23.1m versus −€32.3m for the bullet; the embedded call contributes about **€9.2m of relative protection**. Under a **200bp fall**, that relative contribution is approximately **€23.9m**. These are the model's issuer-side P&L conventions, not gains received immediately in cash.\n\nUnder a 100bp rise, issuer P&L is approximately +€26.8m for the callable structure versus +€30.0m for the bullet; the call option reduces the issuer's benefit from rates rising. This is the expected asymmetry of callable debt.\n\nThe actual generated data are available in [NC4 coupon ladder](results/nc4_single_coupon_ladder.csv), [NC4 scenario table](results/nc4_single_scenarios.csv), [effective risk](results/nc4_single_effective_risk.csv) and [key-rate DV01](results/nc4_single_key_rate_dv01.csv).\n\n## Risk and implementation
The key risks include:
- **Negative convexity:** as rates fall, the issuer call limits appreciation of the liability relative to a bullet.
- **Curve-shape risk:** parallel shifts do not capture every flattener, steepener or key-rate exposure.
- **Model risk:** 15% volatility and mean reversion are assumed, not fully calibrated to a swaption surface.
- **Issuer credit and refinancing risk:** the model excludes issuer-specific credit spread, transaction costs and market access.
- **Synthetic implementation:** receiver swaption plus bullet funding introduces counterparty, basis, collateral and operational considerations.

## Original pricing visuals

![Single-call coupon sensitivity, NC3 comparison](https://raw.githubusercontent.com/benthebender/Financ-Engeneering/main/CALLABLE%20BOND%207yrNCx/Outputs%20Task%202/7y%20NC3%20single/par_coupon__7y_NC3.png)

*Source: shared course model. This is an **NC3 comparison chart**, not the recommended NC4 payoff.*

[Inspect the pricing code, tests, assumptions and final NC4 coupon ladder](IMPLEMENTATION.md). The results in `results/nc4_single_*.csv` were generated from the group model using the local course curve workbook; the raw workbook is not included.

## Evidence and source
- Final presentation: *Callable Bonds*, Group 2, especially executive summary, proposal, single-versus-multi-call comparison and pricing discussion.
- Shared code: [pricing engine and assumptions](https://github.com/benthebender/Financ-Engeneering/tree/main/CALLABLE%20BOND%207yrNCx), [single-call scenario results](https://github.com/benthebender/Financ-Engeneering/tree/main/CALLABLE%20BOND%207yrNCx/Outputs%20Task%202/7y%20NC3%20single).

*Values are model-based coursework results, not a tradable Vonovia new-issue quote.*

[Back to main README](../README.md)
