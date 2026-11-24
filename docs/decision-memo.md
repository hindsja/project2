AI announcement: Codex (GPT-6) assisted with app implementation, data processing, validation and drafting. Sources, assumptions and actual checks are documented.

The submitting analyst is responsible for reviewing the analysis and owning the final decision. Education, not investment advice.

# Investment management decision memo

**Historical cutoff:** 2026-09-30. **Prepared:** 2026-11-23T16:52:13.505916+00:00.
Hypothetical seven-year investor; no withdrawals. Final analyst review/sign-off remains pending.

## Committee ask

**PILOT. Pilot only in a 5-10% shadow sleeve, with 0% live allocation; reverse to reject if the signal is unavailable or no allocation meets the mandate. Consider live adoption only after 12 prospective monthly observations, net return at least the benchmark, realized annualized volatility at most 15%, and no mandate breach at an annual rebalance.**

Live allocation range: **0%**. Research allocation range: **5-10% of a simulated portfolio**.
The weights below apply inside that shadow sleeve, not to actual investor wealth.

## Mandate and decision numbers

The evaluated hypothetical mandate requires a 6.50% estimated annual net return, at most 15.00% estimated volatility,
60.00% per fund, at least 10.00% BIL, no borrowing/shorting, and at most 25.00% one-way annual turnover.
The starting portfolio and benchmark are 60% VOO / 40% BIL. This is a new client policy, not the Lab 13 Meridian classroom case.

| Portfolio | EWY / QQQM / VOO / FNDX / BIL | Estimated net return | Estimated volatility | One-way turnover | Mandate verdict |
|---|---|---:|---:|---:|---|
| Equal weight | 20% / 20% / 20% / 20% / 20% | 8.75% | 14.62% | 60.00% | FAIL: Annual one-way turnover limit |
| 60/40 benchmark | 0% / 0% / 60% / 0% / 40% | 7.75% | 7.49% | 0.00% | PASS |
| Constrained portfolio | 0% / 0% / 35% / 5% / 60% | 6.57% | 4.90% | 25.00% | PASS |

The constrained portfolio clears the return target by only **0.07%**. Its lower risk comes with a larger Treasury-bill allocation.
Equal weight fails the transition-turnover limit despite its attractive estimated return.
Return estimates use historical arithmetic means, a disclosed 10% equity ceiling, and costs on both purchases and sales.
The ceiling is an AI-proposed assumption, not a validated forecast. Volatility is not a maximum-loss guarantee.

## What changes the decision

The equity-estimate stress (minus three percentage points) yields **PILOT**;
the 4% risk ceiling yields **REJECT**. The 60-month window, costs, fund caps and release lag are also tested in the
[full stress table](../outputs/decision-output.md). A weaker equity forecast can require MORE equity to meet a fixed return target;
the risk and turnover limits prevent unlimited compensation.

Only published UNRATE vintages enter the signal. A rise of at least 0.10 percentage point between consecutive knowable months
raises the BIL floor to 40%. Missing consecutive months, observations older than 100 days or no feasible allocation block new orders.
The threshold is experimental, not established predictive evidence.

## Historical reality check

| Process, October 2024–September 2026 | Cumulative return | Annualized compound return | Realized annualized volatility | Maximum monthly drawdown |
|---|---:|---:|---:|---:|
| Constrained | 19.69% | 9.40% | 5.56% | -3.25% |
| Equal weight | 63.39% | 27.82% | 19.29% | -9.37% |
| 60/40 benchmark | 24.51% | 11.58% | 7.60% | -4.21% |

The constrained process returned **9.40%** annualized versus **11.58%** for the benchmark.
Without the macro rule it returned **9.40%**. This sample provides no demonstrated incremental signal advantage.
The diagnostic is retrospective: 24 monthly returns, two annual decisions, and rules chosen after the period existed.
It is not an untouched holdout. Adjusted prices are revised snapshots; only UNRATE has publication-vintage filtering.

## Monitoring, limitations and reversal

Monitor release availability and weight drift monthly; assess return, risk and turnover at annual rebalances.
Block new orders on invalid data or an infeasible mandate; retain and review existing holdings rather than assume forced liquidation.
Consider live adoption only after at least 12 prospective monthly observations, net performance at least the benchmark,
realized annualized volatility at most 15%, no breach at annual rebalance and committee approval. Even that period is weak statistical evidence.

ETF overlap, covariance regime changes, falling bill yields, taxes, intramonth losses, execution approximation and selection bias remain material risks.
There is no seven-year funding simulation. Baselines trade even when failing a rule; failures and drift warnings are exposed in the logs.

Sources and evidence: [data card](data-card.md), [mandate](mandate.md), [actual results](../outputs/results.json),
[validation and AI use](validation-and-ai-use.md). The locked-record AI-off limitation is disclosed in the validation record.
