# Liability modelling: guarantees, mortality and payout choices

## Policyholder cash-flow timeline
- **Year 0 / age 50:** 100,000 policies × €50,000 = **€5bn** of existing assets.
- **Years 1–10:** €5,000 per person at each year-end = **€500m per year** in new premiums.
- **Years 11–14:** no further premiums in the assignment.
- **Year 15 / age 65:** election between lump sum and annuity; no deaths before this point.
- **Years 16 onward:** pension payments to survivors, with a ten-year minimum payment guarantee.

The case uses a **nominal 1% annual guarantee** on contributions accumulated to year 15. The model's reported aggregate guaranteed value is approximately **€11.303bn**.

## Liability election uncertainty
The final presentation uses a **50/50 lump-sum/pension base case**. This creates a substantial, concentrated liquidity demand at year 15: approximately **€5.65bn** in lump sums, plus a much longer pension tail. The portfolio therefore faces both **liquidity timing** and **long-duration interest-rate risk**.

The supporting model reruns elections from **0% to 100% lump sum**. Its liability PV and duration change materially across election assumptions. For example, a supporting report shows a liability duration of roughly **25.4 years** at 0% lump sum, **20.0 years** at 50%, and **15 years** at 100%. This is why matching only one average duration is insufficient.

## Mortality and valuation
Pension cash flows depend on the number of surviving policyholders at each future payment date, as well as the contractual minimum payment period. The shared repository includes mortality tables and a mortality-model prototype; those are **model inputs and assumptions**, not verified actuarial experience for a real insurer.

A valuation framework discounts expected future benefits using a EUR term structure and compares their present value with available assets and future premiums. The supporting reports include alternative liability valuations (for example **€6.41bn** and **€6.81bn**) under different model configurations. They are not interchangeable without matching valuation dates and assumptions.

## Visual evidence — liabilities and elections

![Annual policyholder cash flows](https://raw.githubusercontent.com/benthebender/Financ-Engeneering/main/Case%203/presentation/assets/cf_annual.png)

*Original group presentation: the timing of benefit cash flows matters as much as their present value.*

![Policyholder payout election scenarios](https://raw.githubusercontent.com/benthebender/Financ-Engeneering/main/Case%203/presentation/assets/election.png)

*Original group presentation: alternative payout choices affect year-15 liquidity and the long-dated pension tail.*

![Policyholder election sensitivity](https://raw.githubusercontent.com/benthebender/Financ-Engeneering/main/Case%203/presentation/assets/lc_06_policyholder_sensitivity.png)

*Original group presentation: modelled sensitivity to policyholder choices; compare with the independently reproduced election table in `reproduced/elections/`.*

## Analytical takeaway
The relevant liability is **a schedule of contingent future cash flows**, not a single €11.3bn payment. A robust investment strategy needs cash-flow dedication, long-end interest-rate hedging, sensitivity to pension elections and a funding-ratio view.

**Source:** Final presentation, client-profile and portfolio architecture sections; shared Case 3 pension, election and fixed-income modelling outputs.

[Back to Case 3](README.md)
