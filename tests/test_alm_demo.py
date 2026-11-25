"""No Bloomberg data needed: test the mathematical ALM building blocks."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "03-life-insurance-alm" / "examples"))
from alm_demo import (
    Policy, guaranteed_value, lump_sum_demand, present_value,
    modified_duration, surplus_pnl, key_rate_gap,
)


class TestALMIdentities(unittest.TestCase):
    def test_guarantee(self):
        expected = 100_000 * (50_000 * 1.01**15 + sum(5_000 * 1.01**(15-t) for t in range(1, 11)))
        self.assertAlmostEqual(guaranteed_value(), expected, places=3)

    def test_zero_rate(self):
        self.assertEqual(guaranteed_value(Policy(lives=1, guaranteed_rate=0)), 100_000)

    def test_election_half(self):
        self.assertAlmostEqual(lump_sum_demand(.5), guaranteed_value() / 2)

    def test_election_bounds(self):
        with self.assertRaises(ValueError):
            lump_sum_demand(1.2)

    def test_single_payment_duration(self):
        self.assertAlmostEqual(modified_duration([0, 0, 100], .04), 3 / 1.04)

    def test_present_value(self):
        self.assertAlmostEqual(present_value([0, 100], [1, .9]), 90)

    def test_mismatched_curve(self):
        with self.assertRaises(ValueError):
            present_value([100], [.9, .8])

    def test_surplus_sign(self):
        self.assertEqual(surplus_pnl(-300, -500, 0), 200)

    def test_hedge(self):
        self.assertEqual(surplus_pnl(-300, -500, 100), 300)

    def test_key_rate_gap(self):
        self.assertEqual(key_rate_gap([10, 30], [8, 33]), (2, -3))

    def test_invalid_policy(self):
        with self.assertRaises(ValueError):
            Policy(contribution_years=16)


if __name__ == "__main__":
    unittest.main()
