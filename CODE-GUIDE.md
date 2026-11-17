# Understand the decision code before the AI-off explanation

This is a study guide. Close AI during the Lab 20 prediction and six-minute partner explanation.

The app asks a simple question: among allocations that obey every rule, which has the lowest estimated volatility?

## The important block: `portfolio_metrics()` in `engine.py`

1. Read current holdings in the same ticker order used for all calculations.
2. Compute one-way turnover: half the sum of the absolute changes. Selling 25% of the portfolio and buying 25% elsewhere is 25% turnover, not 50%.
3. Calculate cost on both sides. At 10 basis points per side, that transition costs `2 × 0.25 × 10 / 10000 = 0.0005`, or 0.05% of portfolio value.
4. Compute gross estimated return as the weighted average of fund return estimates.
5. Compute portfolio variance using every pair of weights and covariances. Correlation matters because funds can move together; averaging individual volatilities would be wrong.
6. Take the square root of variance to obtain volatility, and subtract trading cost from the annual arithmetic return estimate.

## The gate: `mandate_checks()`

The function separately checks full investment, long-only weights, return target, volatility, single-fund exposure, BIL minimum, turnover and signal availability. A green total verdict requires every rule to pass. It reports measured values and thresholds, not only a green/red icon.

The signal can raise the BIL minimum. It cannot change the approved return target or silently permit higher risk.

## The choice: `optimize()`

The search tries 10,626 weight combinations in 5-percentage-point steps. It skips combinations that fail a limit, then keeps the feasible portfolio with the lowest estimated volatility. If nothing qualifies, it returns no portfolio. The decision layer then rejects a new allocation.

The base result's thin return margin matters: a small change in assumptions can require a different allocation. Lower equity return estimates may force more equity to satisfy an unchanged target, increasing risk. That is why the risk ceiling must be checked separately.

## The timing rule

The measured month is not the release date. A September unemployment observation published in October was unavailable at the September decision. `unemployment_signal()` first removes late publications, then selects the newest eligible revision of each month. It requires two consecutive months and refuses to invent missing data.

## What the historical test does and does not prove

`walk_forward()` estimates before each annual decision, earns the following months' returns, deducts costs and lets weights drift. It exposes baseline failures and blocked constrained orders. The test is retrospective and short; it does not prove that the chosen signal adds value, or that the portfolio will earn 6.5% in the future.

Personal checks, actual partner questions and the student's responses belong in the lab/AI record only after they occur.
