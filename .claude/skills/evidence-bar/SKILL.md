---
name: evidence-bar
description: The proof standard for AlanGlucose. Use when any claim is made about demand, market size, pricing, channels, or retention, and to audit documents for unsourced claims. Defines exactly what evidence each type of claim requires before it can be treated as fact.
user-invocable: true
---

# Evidence Bar

Every claim is cited, tagged `[ASSUMPTION — H/M/L]`, or treated as fiction. This skill
defines what "cited" actually requires. Apply it to the founder's claims, to research
documents, and to financial models. For a full document audit, spawn the `evidence-checker`
subagent.

## The bar, by claim type

| Claim | What it takes to count as evidence |
|-------|-----------------------------------|
| "X% of people want this" | At least 10 named interviewees with verbatim quotes, OR a smoke-test landing page with at least 100 unique visitors and a measured conversion rate. |
| "The market is worth £X m" | A bottoms-up build (users x price x frequency, every multiplier sourced) AND a top-down cross-check from a cited sector report. |
| "We can charge £Y" | At least 3 customers said yes to that exact price, OR documented comparable products selling at that price. |
| "Channel Z will work" | Cited CPC / CAC data for that channel, plus an organic-reach baseline if relevant. |
| "Customers will switch to us" | Evidence of a switching cost and an actual trigger event — not "our product is better". |
| "Retention will be healthy" | Real cohort data, or a named comparable. Projected retention is an assumption, full stop. |

## How to apply it
1. When the founder states a claim, name its type and quote the relevant bar above.
2. If the evidence meets the bar — accept it, and record the source.
3. If it does not — tag it `[ASSUMPTION — H/M/L]` and state the cheapest test to clear the bar.
4. Never let an assumption quietly become a "fact" through repetition or the passage of time.

## The cheapest-test instinct
For every unmet claim, the question is not "is it true?" but "what is the cheapest, fastest
test that would tell us?" A £20 smoke test usually beats a £2,000 market report.
