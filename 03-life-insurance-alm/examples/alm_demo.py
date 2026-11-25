"""Synthetic, dependency-free checks for the All-Kanns insurance ALM case.

This is an explanatory companion to the group's canonical integrated model,
NOT a replacement for the Bloomberg-calibrated investment engine.
All amounts are EUR. Contributions occur at the end of each year.
"""
from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Policy:
    lives: int = 100_000
    opening_balance: float = 50_000.0
    annual_contribution: float = 5_000.0
    contribution_years: int = 10
    retirement_year: int = 15
    guaranteed_rate: float = 0.01

    def __post_init__(self):
        if self.lives <= 0 or min(self.opening_balance, self.annual_contribution) < 0:
            raise ValueError("Invalid cohort or contribution amounts")
        if not 0 <= self.contribution_years <= self.retirement_year:
            raise ValueError("Invalid contribution period")
        if not isfinite(self.guaranteed_rate) or self.guaranteed_rate <= -1:
            raise ValueError("Invalid guaranteed rate")


def guaranteed_value(policy=None):
    """Accumulated guarantee at retirement, excluding mortality and expenses."""
    p = policy if policy is not None else Policy()
    growth = 1 + p.guaranteed_rate
    initial = p.opening_balance * growth ** p.retirement_year
    premiums = sum(
        p.annual_contribution * growth ** (p.retirement_year - t)
        for t in range(1, p.contribution_years + 1)
    )
    return p.lives * (initial + premiums)


def lump_sum_demand(share, policy=None):
    """Year-15 lump sum under a specified election fraction (0 to 1)."""
    if not isfinite(share) or not 0 <= share <= 1:
        raise ValueError("Election share must be between zero and one")
    return share * guaranteed_value(policy)


def present_value(cash_flows, discount_factors):
    """Discount aligned cash flows; curve interpolation is outside this example."""
    if not cash_flows or len(cash_flows) != len(discount_factors):
        raise ValueError("Cash flows and discount factors must align")
    if any(not isfinite(cf) or cf < 0 for cf in cash_flows):
        raise ValueError("Invalid cash flow")
    if any(not isfinite(df) or df <= 0 for df in discount_factors):
        raise ValueError("Invalid discount factor")
    return sum(cf * df for cf, df in zip(cash_flows, discount_factors))


def modified_duration(cash_flows, annual_yield):
    """Flat-curve annual-pay modified duration of nonnegative cash flows."""
    if not isfinite(annual_yield) or annual_yield <= -1:
        raise ValueError("Invalid annual yield")
    discount = [(1 + annual_yield) ** -t for t in range(1, len(cash_flows) + 1)]
    pv = present_value(cash_flows, discount)
    if pv <= 0:
        raise ValueError("Present value must be positive")
    macaulay = sum(t * cf * df for t, (cf, df) in enumerate(zip(cash_flows, discount), 1)) / pv
    return macaulay / (1 + annual_yield)


def surplus_pnl(asset_pnl, liability_pnl, hedge_pnl=0):
    """Change in economic surplus = asset P&L + hedge P&L - liability P&L."""
    if not all(isfinite(x) for x in (asset_pnl, liability_pnl, hedge_pnl)):
        raise ValueError("Invalid P&L")
    return asset_pnl + hedge_pnl - liability_pnl


def key_rate_gap(asset_dv01, liability_dv01):
    """Asset minus liability DV01 by tenor; no convexity or basis adjustment."""
    if not asset_dv01 or len(asset_dv01) != len(liability_dv01):
        raise ValueError("Key-rate vectors must align")
    if any(not isfinite(x) for x in (*asset_dv01, *liability_dv01)):
        raise ValueError("Invalid DV01")
    return tuple(a - l for a, l in zip(asset_dv01, liability_dv01))


if __name__ == "__main__":
    print(f"Year-15 guarantee: EUR {guaranteed_value()/1e9:.3f}bn")
    print(f"50% lump-sum election: EUR {lump_sum_demand(.5)/1e9:.3f}bn")
    print("Synthetic financial identities only; not a calibrated ALM simulation.")
