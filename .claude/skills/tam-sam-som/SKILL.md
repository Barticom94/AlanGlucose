---
name: tam-sam-som
description: Size a market with TAM, SAM, and SOM. Use when the founder asks about market size, "how big is this", addressable market, or needs market numbers for a pitch deck. Enforces a bottoms-up build plus a top-down cross-check, both with cited sources.
user-invocable: true
---

# TAM / SAM / SOM

Market sizing that survives an investor's scrutiny. A number with no working is worthless —
worse than worthless, because it looks like evidence. For heavy research, spawn the
`market-researcher` subagent.

## Definitions
- **TAM** — Total Addressable Market: everyone who could ever buy this category.
- **SAM** — Serviceable Addressable Market: the slice you can serve (geography, segment, channel).
- **SOM** — Serviceable Obtainable Market: what you can realistically win in 3-5 years.

## Method — do both, always
1. **Bottoms-up.** Number of customers x price x purchase frequency. Source every multiplier:
   customer count from a named statistic, price from comparables, frequency from behaviour
   data. This is the credible number.
2. **Top-down.** Take a published sector report's total and apply your segment percentage.
   Cite the report and its date.
3. **Reconcile.** If the two differ by more than 2x, do not average them — find out why one
   is wrong. The gap usually exposes a bad assumption.

## Output
- The SOM matters most for a bootstrap — it is the realistic prize, not the headline.
- Express SOM as a path: year 1, year 3, year 5, with the assumption behind each step.
- Write the sizing to `research/market-reports/`. Put headline figures in `state/financials.md`.

## Anti-patterns
- "1% of a £1bn market" is the oldest unfunded slide in existence. Build bottoms-up instead.
- A big TAM does not make a good business. A reachable SAM with healthy unit economics does.
- Tag every unsourced multiplier `[ASSUMPTION — H/M/L]`. See the `evidence-bar` skill.
