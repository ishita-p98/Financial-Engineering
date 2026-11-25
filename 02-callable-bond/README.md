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

The final presentation describes the premium as the cost of retaining the option to refinance early if rates decline. It also reports scenario benefits of approximately **€18.6m for a 100bp fall** and **€43.6m for a 200bp fall** in its executive summary. The precise payoff and notional conventions must be read with the corresponding scenario tables before extrapolating those figures.

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

## Risk and implementation
The key risks include:
- **Negative convexity:** as rates fall, the issuer call limits appreciation of the liability relative to a bullet.
- **Curve-shape risk:** parallel shifts do not capture every flattener, steepener or key-rate exposure.
- **Model risk:** 15% volatility and mean reversion are assumed, not fully calibrated to a swaption surface.
- **Issuer credit and refinancing risk:** the model excludes issuer-specific credit spread, transaction costs and market access.
- **Synthetic implementation:** receiver swaption plus bullet funding introduces counterparty, basis, collateral and operational considerations.

## Evidence and source
- Final presentation: *Callable Bonds*, Group 2, especially executive summary, proposal, single-versus-multi-call comparison and pricing discussion.
- Shared code: [pricing engine and assumptions](https://github.com/benthebender/Financ-Engeneering/tree/main/CALLABLE%20BOND%207yrNCx), [single-call scenario results](https://github.com/benthebender/Financ-Engeneering/tree/main/CALLABLE%20BOND%207yrNCx/Outputs%20Task%202/7y%20NC3%20single).

*Values are model-based coursework results, not a tradable Vonovia new-issue quote.*

[Back to main README](../README.md)
