# Financial Engineering | Three Applied Group Case Studies

**Financial Engineering · Group 2 · Corporate risk, callable debt and insurance asset–liability management**

Three client-facing financial-engineering assignments completed collaboratively during the course. **Only the B assignment from each case day** is represented here. The final group presentations are the primary record of the conclusions; supporting code and spreadsheets in the [shared course repository](https://github.com/benthebender/Financ-Engeneering) provide implementation context.

| Case | Client problem | Final deliverable |
| --- | --- | --- |
| [01 · Interest-rate risk — PV / VaR](01-interest-rate-risk-var/README.md) | Quantify and hedge a corporate borrower's interest-rate exposure | Vonovia VaR model comparison, backtesting and hedge recommendation |
| [02 · Callable bond](02-callable-bond/README.md) | Buy refinancing flexibility without overpaying for optionality | **7Y NC4 single-call** structure and relative-value assessment |
| [03 · Life-insurance ALM](03-life-insurance-alm/README.md) | Invest for guaranteed policyholder benefits and long-tail liabilities | **All-Kanns** two-sleeve investment mandate, fixed-income matching, derivatives and solvency analysis |

## Case 3: verified financial building blocks

A [synthetic ALM example](03-life-insurance-alm/examples/alm_demo.py) demonstrates the policy guarantee, lump-sum election, discounted cash flows, duration and surplus accounting without proprietary data. It is **not** the full investment engine. The example has [11 independent unit tests](tests/test_alm_demo.py), executed locally before publication.

## Latest validation

The callable-bond NC4 result has been repriced from the group model, and the canonical Case 3 optimizer, policyholder election sensitivity, historical simulation, Monte Carlo and final-presentation receiver-swap overlay have completed successfully in [GitHub Actions](https://github.com/ishita-p98/Financial-Engineering/actions/runs/45634187841). Reproduced Case 3 reports, tables and charts are stored in `03-life-insurance-alm/reproduced/`.

## Source code and verification

Selected original group Python models, test files and result tables are included under each case. See [technical audit and validation matrix](TECHNICAL_AUDIT.md), [reproducibility and data limitations](REPRODUCIBILITY.md) and [dependencies](requirements.txt). The complete raw Bloomberg workbooks are not included, so full end-to-end execution requires the original data.

## Automated model checks

[GitHub Actions](https://github.com/ishita-p98/Financial-Engineering/actions/workflows/synthetic-tests.yml) runs the synthetic financial tests and, following the latest update, the callable-bond, VaR and mortality regression suites. A successful run of the **latest commit** is required before calling the expanded checks verified. Full Bloomberg-calibrated ALM reproduction remains separate.

## How to read this portfolio

Each case separates the **assignment**, **the group's final presentation**, **model assumptions**, **reported outputs**, and **limitations**. Results are historical coursework outputs, not live prices, current investment advice or independently audited regulatory metrics.

The projects build from **measuring risk**, to **pricing optionality**, to **designing and managing a liability-aware institutional portfolio**.

## Collaboration

These were collaborative Group 2 course projects. Thanks to **Jonas, Kira Pedersen, Ben Lösche, David Wolter, Manuel Blasco Blázquez, Wiktor Murawski and Zhuoran Wang** for their contributions.

*The source presentations contain participant identifiers and are not redistributed here. This repository presents a written, attributed synthesis.*
