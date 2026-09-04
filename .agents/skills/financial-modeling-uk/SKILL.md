---
name: financial-modeling-uk
description: Build and stress-test UK unit-economics and cashflow models. Use when the founder asks about CAC, LTV, gross margin, runway, breakeven, pricing maths, "the numbers", "can I afford this", "/financial-stress-test", or faces any spend decision. Enforces evidence-tagged inputs and three scenarios.
---

# Financial Modeling (UK)

Money decisions need numbers — a feeling is not a financial model (`AGENTS.md`, rule 4).
This skill builds the model; the `financial-modeler-uk` subagent does heavy builds, and the
`financial-stress-tester` subagent reviews them in a clean context.

## The core numbers
- **Gross margin** = (price − COGS) / price. Below 40% is a warning for a product business.
- **CAC** — the fully loaded cost to acquire one paying customer, including the founder's time.
- **LTV** — gross-margin pounds from a customer over their lifetime, not their revenue.
- **LTV / CAC** — target ≥ 3. Below 3, the business does not work yet; say so.
- **Payback period** — months to recover CAC. Over 12 months strains a bootstrap's cash.
- **Runway** = cash ÷ monthly burn. **Breakeven** = units needed to cover fixed costs.

## UK specifics to bake in
- VAT: 20% standard; registration threshold £90,000 on a rolling 12 months. Model the
  margin step-change at registration — it is a real cliff, not a footnote.
- Corporation Tax: 19% on profits ≤ £50k, 25% ≥ £250k, marginal relief between.
- Card processing: roughly 1.5% + 20p on UK consumer cards.
- For physical goods: carrier, packaging, and returns cost per order — see the `ECOM-OPS`
  doc in the ecommerce pack (`packs/ecommerce/docs/ECOM-OPS.md`), if installed.
Verify every rate against gov.uk; UK tax figures move at 6 April and 1 February.

## Method
1. Pull every input from `state/financials.md`. Tag each `[ASSUMPTION — H/M/L]` if unsourced.
2. Build bottoms-up: revenue = units × price × frequency; cost it line by line.
3. Produce three cases — conservative, base, optimistic — and label which inputs move.
4. Model the cash curve, not just the P&L. A profitable plan can still run out of cash.
5. Write the model to `financials/`; update headline figures in `state/financials.md`. Every
   forecast figure with a date is a row in `state/predictions.md` (confidence, resolves by).
6. For any real decision, spawn `financial-stress-tester` before concluding.

## The honest test
If the model only works in the optimistic case, the venture is not yet viable. Relabel the
optimistic case as the base case and look again.
