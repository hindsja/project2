# Recording preparation — not a transcript or personal reflection

Record only after reviewing the app and completing the human evidence. These outlines help organize real explanations; they do not claim personal history, independent checks, partner exchanges or final decisions.

Open each video with two statements in your own accurate words:

1. Identify Codex (GPT-6) and its actual assistance: code, data processing, validation and drafting; identify what you personally checked.
2. State that you own the reviewed analysis and final decision, and that this is education, not investment advice. Make that ownership statement only after doing the review.

## Video 1 — at most 3 minutes

- Explain what actually changed from your earlier Lab 15/17 work to this app. The files establish a four-equity-fund exercise, an unemployment timing audit, and the later addition of BIL and explicit mandate constraints.
- Describe your real thinking, not an invented before-AI opinion. The earlier Lab 15 memo itself was AI-assisted and provisional.
- Show one consequential AI output you personally checked, the source/calculation/counterexample used, and why you accepted, modified or rejected it.
- Explain one limitation and how it affects your recommendation.

Possible evidence to inspect personally: recompute turnover as half the sum of absolute weight changes, or trace an excluded unemployment release to its publication date. These are study suggestions, not claims that you have performed those checks.

## Video 2 — at most 5 minutes

Show the actual source files while explaining this flow:

1. `load_prices()` converts monthly labels to month-end and rejects missing/duplicate months.
2. `estimate()` uses only trailing returns through the decision date, annualizes mean/covariance and applies the disclosed equity estimate ceiling.
3. `unemployment_signal()` filters by effective publication date, picks eligible vintages and refuses a missing consecutive month.
4. `portfolio_metrics()` computes return, risk, turnover and costs; `mandate_checks()` produces named pass/fail rules.
5. `optimize()` searches feasible 5-point allocations; `analyze()` produces PILOT or REJECT.
6. `walk_forward()` applies decisions to subsequent returns and records stopped orders/drift warnings.

Know why cost counts both buys and sells, why estimated volatility is not a loss ceiling, and why a portfolio can pass the return target but fail turnover.

## Video 3 — at most 5 minutes

**Open with the app already running live**, not only slides. Keep the required opening statements concise.

- State the investor, seven-year horizon, benchmark and mandate.
- Show the three portfolios and the exact failed rule for equal weight.
- Change a control and explain the actual new verdict. Use a separate demonstration from your already frozen AI-off record.
- State the decision, allocation range and reversal/monitoring triggers.
- Explain the historical diagnostic and why it does not establish an unemployment forecasting edge or justify live adoption.
- Make the committee ask explicit: a small simulated pilot with zero live allocation while prospective evidence is collected, or your own evidence-supported final alternative.

## After recording

Upload the three actual recordings to YouTube, enable transcripts/captions and correct finance terms, tickers and numbers. Save or link the actual transcripts as `docs/transcript-video-1.txt`, `docs/transcript-video-2.txt`, and `docs/transcript-video-3.txt`.

Update `docs/submission-manifest.md` with the real URLs, titles, durations, timestamp indices and access checks. An outline is not a transcript. Ensure the spoken numbers agree with the final memo and visible output.
