---
name: ecom-conversion-analytics
description: Set up store measurement and improve conversion. Use when the founder asks about GA4, analytics setup, conversion rate, AOV, sessions, returning-customer rate, product-page or checkout CRO, or "should I A/B test this". Measurement planning is validation-safe from Phase 1; CRO work and paid analytics tools apply from Phase 2 (MVP), after the ≥ 3 real commitments gate (`AGENTS.md`).
---

# Ecommerce — Conversion & Analytics

A store the founder cannot measure is a store the founder is guessing about. Planning what
to measure, and why, is useful before a line of the store exists. Do not install paid
analytics or CRO tools, and do not run a formal A/B test, before the Phase 1 gate — ≥ 3 real
commitments.

## How to use this skill
1. Set up measurement before launch, not after the founder notices sales are flat: GA4 (free)
   on the store, plus the platform's native analytics (Shopify Analytics if applicable — see
   `ecom-shopify`).
2. Decide the analytics tool before the banner, because the tool decides whether you need
   one. Since 5 February 2026 the Data (Use and Access) Act 2025 has exempted first-party
   cookies used solely for statistical purposes to improve the service from PECR consent,
   provided visitors get clear information and a simple, free way to object (ICO guidance
   finalised 29 April 2026 — verify on ico.org.uk before relying on it). **GA4 does not
   qualify** — Google processes the data for its own advertising and AI purposes and acts as
   a joint controller, so GA4 still needs opt-in consent behind a compliant banner. A
   first-party tool used purely for aggregate statistics (e.g. Plausible, or PostHog
   configured with no ad linkage) can run without one. Note PECR fines rose to £17.5m / 4%
   of global turnover on the same date. This is information, not legal advice.
3. Define the five metrics that matter (below) and where each one lives in `state/financials.md`.
4. Set up GA4 ecommerce events — `view_item`, `add_to_cart`, `begin_checkout`, `purchase` — using
   the platform's built-in integration where one exists (Shopify's GA4 integration covers this
   without custom code); do not hand-roll event tracking before checking for a native option.
5. Review the funnel weekly at first: sessions → product views → add-to-cart → checkout
   start → purchase. The step with the steepest drop is the priority, not the whole page.
6. Fix the biggest, cheapest thing first — usually the product page or checkout (see CRO
   below) — before reaching for a formal test.
7. Only run an A/B test once traffic can support one (see "Honest A/B testing" below).
   Otherwise, ship the change and watch the trend.

## The five metrics that matter
- **Sessions** — traffic volume, split by source (organic, paid, direct, social, email).
  Volume without the other four metrics is vanity.
- **Conversion rate** — purchases ÷ sessions. All-industry UK benchmark reported around
  1.9-3.4%, varying widely by category — luxury/jewellery under 1%, food and beverage above
  6% [industry benchmark aggregators — IRP Commerce, Charle, others, accessed September
  2026 — treat as a rough band, not a target, and verify current figures before quoting
  them to anyone]. Compare the store against its own trend, not a generic number.
- **AOV (average order value)** — revenue ÷ number of orders. UK all-industry AOV reported
  around £120-130 in 2026, with wide variation by vertical — roughly £60-95 for beauty/
  supplements up to £150-250 for home and jewellery [industry benchmark aggregators,
  accessed September 2026 — verify current figures before relying on them]. A small AOV lift
  (bundling, a free-shipping threshold) is usually cheaper to win than a traffic increase.
- **CAC (customer acquisition cost)** — see `financial-modeling-uk` for the full build; this
  skill supplies the conversion-rate input CAC depends on.
- **Returning-customer rate** — repeat purchasers ÷ total customers in a period. The cheapest
  revenue in the business; a store that cannot get anyone to buy twice does not yet have a
  retention problem solved by more traffic.

## Product-page and checkout CRO
- **Product page** — real photos (multiple angles), an honest description that answers the
  actual buying question, visible price and delivery cost, and genuine reviews. Do not use
  fake urgency or fabricated stock counts — see the review and claims rules in
  `ecom-marketplaces-uk` and `@docs/UK-LEGAL-TAX.md`; the Digital Markets, Competition and
  Consumers Act 2024 makes fake urgency and fake reviews unlawful commercial practices
  (in force from 6 April 2025 — verify current guidance on gov.uk before relying on it). This
  is information, not legal advice; check any claims-and-reviews decision with a UK solicitor
  if there is real doubt.
- **Checkout** — the single highest-leverage page, and the one with a hard legal floor. The
  DMCC Act 2024's drip-pricing ban (in force 6 April 2025) requires the total price,
  including every unavoidable mandatory charge, to be shown in the invitation to purchase —
  not revealed at the last step. Treat "all-in price visible up front" as a compliance
  requirement, not a CRO test. Then: offer guest checkout, minimise form fields, and show
  accepted payment methods early. [DMCC Act 2024 Sch. 20 / CMA unfair commercial practices
  guidance — verify current guidance on gov.uk; information, not legal advice] Cart
  abandonment is often a cost-surprise problem, not a design problem — check the numbers
  before redesigning anything.
- Test on a real phone. Most UK ecommerce sessions are mobile; a desktop-only review misses
  the majority of the funnel.

## Honest A/B testing at small volumes
A standard 95%-confidence test needs roughly 1,000+ conversions per variant to detect a
realistic (10-20%) uplift reliably; detecting a small lift on a 2-5% converting page can need
tens of thousands of visitors per variant [CRO industry guides — Convertize, CXL, and
others, accessed September 2026 — treat the exact numbers as directional, not a formula, and
recompute for the actual baseline conversion rate]. A pre-revenue or early-Phase-2 store
rarely has that traffic. Below that volume:
- Test large, obvious changes (a rewritten headline, a different hero image) — small tweaks
  need more data than the store has to detect reliably.
- Prefer sequential before/after comparison with a clearly logged change date over a split
  test the store cannot power properly, and say so plainly rather than reporting a false
  "winner".
- Do not stop a test early because it looks good — that is the single most common way small
  stores fool themselves.

## Output
Update `state/financials.md` with the five metrics and their current values. Log any CRO
change and its measured effect in `state/decisions_log.md`; note the analytics setup in
`state/tech_context.md`.
