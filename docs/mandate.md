# Mandate and implementation assumptions

## Approved hypothetical investor mandate

Approved by the user in conversation on November 16, 2026. This is a new hypothetical client policy; the Lab 13 file contains the separate Meridian classroom case. No prior client mandate or pre-AI prediction is invented. The [Lab 13 follow-on instructions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-08/lab-13-portfolio-mandate.md#after-this-lab-your-project-2-mandate) explicitly ask for the student's own client mandate and allow AI. This policy is that follow-on mandate; it is not represented as the Meridian exercise or as a policy already submitted during Lab 13.

| Item | Policy |
|---|---|
| Intended user | Analyst advising a hypothetical long-term investor; final action requires committee review |
| Horizon and spending | Seven years; no withdrawals during that horizon |
| Universe | EWY, QQQM, VOO, FNDX, and a Treasury-bill ETF, implemented as BIL |
| Objective | Estimated annual arithmetic return at least 6.5%, net of modeled implementation trading costs |
| Benchmark | Fixed 60% VOO / 40% BIL, rebalanced annually |
| Risk measure | Annualized standard deviation from monthly sample covariance; limit 15% at allocation decisions |
| Concentration | At most 60% per ETF at allocation decisions; underlying overlap remains a limitation |
| Defensive sleeve | At least 10% BIL at allocation decisions |
| Trading | Long-only, fully invested, no leverage/shorting; annual rebalancing |
| Turnover | At most 25% one-way turnover per annual transition |
| Monitoring | Monthly data availability and weight drift; annual return/risk/turnover feasibility |

The target is an estimate, not a guaranteed compound return. The seven-year horizon is a planning assumption, not the length of the available test or a seven-year funding simulation. No tax or withdrawal model is claimed.

## Explicit AI-proposed modeling choices

- Starting holdings: 60% VOO / 40% BIL. Turnover is measured relative to these holdings in the snapshot, and relative to drifted holdings in the chronological diagnostic.
- Cost: 10 basis points per dollar traded on each side, varied in stress tests. One basis point is 0.01 percentage point. The charge is `2 × one-way turnover × cost_bps / 10000`.
- Expected returns: annualized arithmetic historical means; each equity mean is capped at 10% before adding the stress shift. BIL retains its estimated historical mean. ETF expenses already embedded in adjusted prices are not subtracted again.
- Search: enumerate 10,626 long-only portfolios in 5-percentage-point steps; select the lowest estimated volatility among feasible candidates. Tie-break by lower turnover, then fixed ticker order. No claim of a continuous global optimum.
- Signal: a UNRATE rise of at least 0.10 percentage point between consecutive knowable months raises the BIL minimum to 40%. Publication date plus an optional lag determines availability. Maximum age is 100 days since measured month-end. These choices were not tuned through a parameter search, but were selected after the data existed and remain subject to selection bias.
- On missing signal or no feasible allocation: block NEW constrained orders and retain existing holdings for committee review. This is not automatic liquidation and does not assert that retained holdings remain compliant.
- Drift: limits apply at annual allocation decisions, with monthly breach alerts between them. Unscheduled remediation would require approval and a new turnover assessment.
- Research allocation: 5–10% shadow sleeve, 0% live allocation. This research sizing is a proposed governance choice, not an estimated optimal capital allocation.

## Equations

For fund `i`, monthly simple return is `r[i,t] = adjusted_price[i,t] / adjusted_price[i,t-1] - 1`.

`mean_annual[i] = 12 × mean(r[i])`; `cov_annual[i,j] = 12 × sample_covariance(r[i], r[j])`.

`portfolio_gross_estimate = Σ weight[i] × adjusted_mean_annual[i]`.

`portfolio_volatility = sqrt(Σ_i Σ_j weight[i] × weight[j] × cov_annual[i,j])`.

`one_way_turnover = 0.5 × Σ abs(new_weight[i] - current_weight[i])`.

`estimated_net_return = portfolio_gross_estimate - 2 × turnover × cost_bps / 10000`.

The net-return screen deducts the proposed transition's trading cost from a one-year arithmetic estimate. It does not estimate every future year's trading costs. Historical wealth uses exact multiplicative cost treatment: `(1 - cost) × (1 + monthly_portfolio_return)`.

## Stop/reversal policy

Stop new allocations on missing/invalid data, stale or nonconsecutive signal observations, or no feasible grid allocation. Review any monitoring breach rather than silently relaxing the mandate. The pilot should be rejected if these conditions prevent a defensible process. Consider live adoption only after at least 12 prospective monthly observations, net performance at least the benchmark, realized annualized volatility at most 15%, no breach at annual rebalance, and committee approval. This minimum observation period is still statistically weak evidence.

## Client question and decision consequence

AI-assisted proposed question: Is a shadow research pilot with zero live allocation acceptable while prospective evidence is collected? This is not a recorded client exchange. If immediate live allocation or a dependable 6.5% compound outcome is required, reject this process: the historical arithmetic estimates and short diagnostic do not establish either. The planning mandate has no withdrawal obligation; introducing one requires a new funding model and renewed suitability review.
