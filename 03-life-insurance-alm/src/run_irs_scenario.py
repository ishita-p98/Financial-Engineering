"""Run the group's published All-Kanns receiver-swap overlay configuration.

The underlying risk engine is the canonical shared-course case3_model.py.
This wrapper only selects the final presentation's receive-fixed IRS overlay
(2.8bn at 15Y and 0.3bn at 30Y) and pins the equity-futures overlay to zero,
so the effect of the interest-rate hedge can be evaluated separately.
"""
from case3_model import Config, run_hs, run_mc


def main() -> None:
    config = Config(
        deployment="full",
        future_hedge_ratio=0.0,
        irs_receiver=((15.0, 2.8e9), (30.0, 0.3e9)),
    )
    run_hs(config, tag="full_irs")
    run_mc(config, n_paths=10_000, tag="mc_full_irs")


if __name__ == "__main__":
    main()
