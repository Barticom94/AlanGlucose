---
name: uk-tax-vat-mtd
description: Handle UK tax questions — VAT, Corporation Tax, Making Tax Digital, registration thresholds. Use when the founder asks about VAT, tax, "/uk-tax-check", MTD, the £90k threshold, or tax on profit. Information, not advice — figures are time-sensitive.
---

# UK Tax — VAT & Making Tax Digital

UK tax figures change at 6 April and 1 February. Always verify against gov.uk before a real
decision. Full figures: `@docs/UK-LEGAL-TAX.md`. This is information, not tax advice.

## VAT
- **Registration threshold £90,000** of VAT-taxable turnover on a rolling 12 months.
  Deregistration threshold £88,000.
- Standard rate 20%. The **Flat Rate Scheme** is available if VAT-taxable turnover is
  ≤ £150,000 excl. VAT — it can simplify admin for a small business.
- Crossing the threshold is a margin cliff for B2C: you either absorb 20% or raise prices.
  Model it with `financial-modeling-uk` well before you near £90k.
- You can register voluntarily before the threshold — sometimes worth it to reclaim input VAT.

## Corporation Tax (limited companies)
- 19% on profits up to £50,000; 25% on profits from £250,000; marginal relief between.

## Making Tax Digital for Income Tax (MTD-IT)
- Mandatory from **6 April 2026** for the self-employed and landlords with qualifying income
  over £50,000. The threshold drops to £30,000 (April 2027), then £20,000 (April 2028).
- It requires MTD-compatible software and quarterly updates — see `bookkeeping-uk`.

## How to use this skill
1. Identify which tax the question touches.
2. State the current rule and threshold, flagged as needing a gov.uk check.
3. If the venture is near a threshold, model the impact — do not just note it.
4. Recommend a UK chartered accountant for the actual filing and any decision.
