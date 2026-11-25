# Portfolio engineering: fixed-income dedication, KRD matching and overlays

## 1. Liability-Matching Portfolio
The final presentation assigns the initial **€5bn** to a fixed-income LMP. The objective is to match the **timing** and **rate sensitivity** of guaranteed liabilities, not merely to achieve a high bond yield.

The supporting work uses two optimization stages:

1. **Cash-flow dedication:** select bonds so coupon and redemption cash flows cover required payouts, with reinvestment assumptions and a quantified external top-up where needed.
2. **Key-rate risk shaping:** minimize the mismatch between asset and liability **DV01 at individual tenors**, rather than relying only on aggregate modified duration.

The model includes issuer and instrument concentration constraints. Ultra-long nominal bonds and zero-coupon securities extend the available maturity profile and improve matching of the distant pension tail.

## 2. Why duration alone is not enough
Two portfolios can have the same total duration but different exposures to curve steepening, flattening and long-end shocks. **Key-rate DV01** measures the change in PV for a small shift at each maturity bucket. The presentation therefore combines:
- cash-flow matching,
- aggregate duration matching,
- key-rate DV01 matching,
- and a receive-fixed interest-rate swap overlay.

The group reports liability duration of approximately **20 years** and a cash-bond portfolio whose duration varies with the chosen universe (roughly **17–29 years** across versions). It should not be described as a perfect duration or convexity hedge.

## 3. Receiver swap overlay
The final recommendation adds approximately **€2.8bn notional at 15Y** and **€0.3bn at 30Y** in **receive-fixed swaps**. Receiving fixed adds positive rate duration to the asset side and is designed to offset the liability's sensitivity to falling EUR rates.

A par swap has **approximately zero market value at inception** and does not exchange principal, but it is **not free of risk or cash demands**: variation margin, collateral liquidity, counterparty exposure, basis and roll considerations remain.

The group presents this as a hedge of **surplus risk**, not a strategy to eliminate asset-price fluctuations.

## 4. Return-Seeking Portfolio
New contributions of **€0.5bn annually** fund a diversified RSP. The presentation's approximate target composition is:
- **93% equities**,
- **4% high-yield credit**,
- **2% gold**,
- **1% EUR / cash-like exposure**.

These approximate categories summarize fourteen index sleeves. The group discusses annual rebalancing and USD exposure hedged to EUR through FX swaps, with a residual rate-differential and rollover risk.

## 5. Policyholder profit sharing
The proposed rule allocates **90% of the return book's yearly investment profit to policyholders**, with **10% retained** by the insurer. The supporting model specifies profit sharing from the benefit phase, distinguishes investment profit from new contributions and includes a loss carry-forward rule.

A high simulated RSP value **before profit sharing** is not equivalent to retained insurer capital **after profit sharing**. Both should be identified separately.

## 6. Rebalancing and glidepath
The final recommendation calls for annual review of the two-sleeve allocation, a **de-risking glidepath during years 11–15**, and a liquidity reserve of at least **1.1× the next twelve months' outflows** in cash and sovereign assets. This is the group's proposed implementation policy, not a regulatory requirement independently verified here.

**Sources:** Final presentation, portfolio architecture, bond matching, RSP, profit-sharing and recommendation sections; shared `results_v2/REPORT.md`, `return_book.py` and `case3_model.py`.

[Back to Case 3](README.md)
