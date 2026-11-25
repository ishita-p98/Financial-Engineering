"""Data-independent mathematical regression tests for the VaR engine.

These tests check numerical invariants, not the historical Bloomberg calibration.
Run from this folder: python -m pytest -q tests/test_risk_math.py
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import var_core as risk


def test_gaussian_var_and_expected_shortfall():
    sensitivity = np.array([2.0, -1.0])
    covariance = np.array([[4.0, 0.5], [0.5, 1.0]])
    value_at_risk, expected_shortfall = risk.delta_normal_var(
        sensitivity, covariance, alpha=0.05
    )
    sigma = np.sqrt(sensitivity @ covariance @ sensitivity)
    assert value_at_risk > 0
    assert expected_shortfall > value_at_risk
    assert np.isclose(value_at_risk / sigma, 1.6448536269514722)


def test_empirical_var_and_expected_shortfall():
    pnl = np.arange(-100, 100, dtype=float)
    value_at_risk, expected_shortfall = risk.var_es(pnl, alpha=0.05)
    assert value_at_risk > 0
    assert expected_shortfall > value_at_risk


def test_positive_semidefinite_projection():
    matrix = np.array([[1.0, 2.0], [2.0, 1.0]])
    projected = risk.nearest_psd(matrix)
    assert np.linalg.eigvalsh(projected).min() >= -1e-12
    assert np.allclose(projected, projected.T)


def test_correlated_scenario_covariance():
    covariance = np.array([[1.0, 0.4], [0.4, 2.0]])
    scenarios = risk.mvn_scenarios(covariance, 50_000, np.random.default_rng(42))
    assert scenarios.shape == (50_000, 2)
    assert np.allclose(
        np.cov(scenarios, rowvar=False), covariance, rtol=0.05, atol=0.05
    )


def test_ten_day_horizon_aggregation():
    changes = pd.DataFrame(
        np.full((15, 10), 0.0001), columns=risk.RISK_NODES
    )
    aggregated = risk.horizon_changes(changes, horizon=10)
    assert len(aggregated) == 6
    assert np.allclose(aggregated.values, 0.001)
