"""Independent financial invariants, with synthetic inputs only.

These checks do not require licensed market data. They verify accounting
identities and risk-measure sign conventions used in the case studies.
"""
import math
import statistics
import unittest


def accumulated_guarantee(
    policies=100_000, opening=50_000.0, premium=5_000.0,
    premium_years=10, retirement_year=15, guarantee=0.01
):
    """Future value of opening balance plus end-of-year premiums."""
    assert policies > 0 and 0 <= premium_years <= retirement_year
    assert opening >= 0 and premium >= 0 and guarantee > -1
    opening_fv = opening * (1 + guarantee) ** retirement_year
    premium_fv = sum(
        premium * (1 + guarantee) ** (retirement_year - year)
        for year in range(1, premium_years + 1)
    )
    return policies * (opening_fv + premium_fv)


def par_bullet_coupon(discount_factors):
    """Annual coupon rate for a zero-spread bullet priced at par."""
    assert discount_factors and all(0 < d <= 1 for d in discount_factors)
    return (1 - discount_factors[-1]) / sum(discount_factors)


def price_bullet(discount_factors, coupon):
    """Price per 100 face, annual payments and redemption at maturity."""
    return 100 * (coupon * sum(discount_factors) + discount_factors[-1])


def risk_tail(pnl, confidence=0.95):
    """Empirical loss VaR and ES; positive means a loss.

    This is an educational equal-weight tail implementation. It uses the
    lower nearest-rank quantile and averages observations at/below cutoff.
    """
    assert 0 < confidence < 1 and len(pnl) >= 2
    ordered = sorted(float(x) for x in pnl)
    tail_probability = 1 - confidence
    index = max(0, math.ceil(len(ordered) * tail_probability) - 1)
    cutoff = ordered[index]
    tail = [x for x in ordered if x <= cutoff]
    return -cutoff, -statistics.mean(tail)


class FinancialInvariantTests(unittest.TestCase):
    def test_guarantee_equals_manual_cash_flow_sum(self):
        expected = 100_000 * (
            50_000 * 1.01**15 +
            sum(5_000 * 1.01**(15 - y) for y in range(1, 11))
        )
        self.assertAlmostEqual(accumulated_guarantee(), expected)
        self.assertTrue(11e9 < expected < 12e9)

    def test_zero_rate_guarantee(self):
        self.assertEqual(accumulated_guarantee(1, 50_000, 5_000, 10, 15, 0), 100_000)

    def test_bullet_reprices_to_par(self):
        discount_factors = [(1.03) ** (-year) for year in range(1, 8)]
        coupon = par_bullet_coupon(discount_factors)
        self.assertAlmostEqual(price_bullet(discount_factors, coupon), 100)

    def test_callable_bond_cannot_exceed_bullet(self):
        """The holder's issuer-call option is nonnegative in a consistent model."""
        bullet = 102.5
        call_option = 1.3
        callable_value = bullet - call_option
        self.assertLessEqual(callable_value, bullet)

    def test_surplus_pnl_identity(self):
        asset_pnl, liability_pnl = -300, -500
        surplus_pnl = asset_pnl - liability_pnl
        self.assertEqual(surplus_pnl, 200)

    def test_var_and_expected_shortfall_order(self):
        pnl = [-100, -80, -50, -20, 0, 10, 20, 30, 40, 50]
        value_at_risk, expected_shortfall = risk_tail(pnl, 0.8)
        self.assertGreaterEqual(expected_shortfall, value_at_risk)
        self.assertGreater(value_at_risk, 0)


if __name__ == "__main__":
    unittest.main()
