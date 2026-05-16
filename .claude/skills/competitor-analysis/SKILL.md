---
name: competitor-analysis
description: Map the competitive landscape and assess industry attractiveness. Use when the founder asks about competitors, "who else does this", rivals, or industry forces. Applies Porter's Five Forces and the 7 Powers, and uses Companies House data for UK rivals.
user-invocable: true
---

# Competitor Analysis

"No competitors" almost always means "no market" or "I have not looked". For deep profiles,
spawn the `competitor-analyst` subagent — it uses the Companies House MCP for UK company data.

## 1. Map the competitive set
List 5-10 named competitors, including indirect ones and the do-nothing / DIY option (often
the real competitor). For each: what they sell, to whom, at what price, positioning in one
line. For UK companies, pull incorporation date, filed accounts, employee count, and
directors from Companies House — it reveals scale and health a website hides.

## 2. Porter's Five Forces — rate the industry
- **Competitive rivalry** — how many rivals, how aggressive, how differentiated.
- **Supplier power** — can suppliers squeeze your margin? Critical for ecommerce.
- **Buyer power** — can customers force the price down? Are switching costs low?
- **Threat of substitutes** — what else solves the problem, including doing nothing.
- **Threat of new entrants** — how easily can the next founder copy this?
Rate each High / Medium / Low with named evidence. A market that is High on every force is
a hard place to make money.

## 3. 7 Powers — find the credible moat (Helmer)
Which does the venture have a believable path to: scale economies, network effects,
counter-positioning, switching costs, branding, cornered resource, process power? At Phase 0
the honest answer is usually "none yet" — that is acceptable, but there must be a credible
path before Phase 4.

## Output
Write to `research/competitor-profiles/`. Update `state/product_context.md` with the
positioning gap and the moat hypothesis. End with the single competitor most likely to kill
this venture, and why.
