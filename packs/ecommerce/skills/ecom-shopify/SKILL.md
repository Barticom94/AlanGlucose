---
name: ecom-shopify
description: Build and run a Shopify store. Use when the founder asks about Shopify, setting up the online store, themes, apps, the product catalogue, checkout, or the storefront. Triggered at Phase 2 (MVP), not before validation.
---

# Ecommerce — Shopify

Shopify is the default platform for an online store — it handles hosting, payments,
security, and PCI compliance. Do not build the
store until the Phase 1 gate is met — ≥ 3 real commitments. A store before validation is a
costly distraction.

## MVP store — the minimum that takes money
1. **Plan** — start on Basic (£25/month on monthly billing, £19/month if you prepay a year —
   model the monthly figure unless the cash is already committed). Do not pay for features
   you will not use.
2. **Theme** — a free Shopify theme, lightly customised. Speed and trust beat bespoke design.
3. **Products** — honest titles, real photos, accurate descriptions. Copy via the
   `copywriter-brand-voice` subagent.
4. **Payments** — Shopify Payments or Stripe; the rate differs. Shopify Payments is charged
   by plan (~2% + 25p on UK online cards on Basic, falling to ~1.5% on Advanced); standalone
   Stripe is ~1.5% + 20p on UK cards. Use the rate for the plan you are actually on and put
   it in `state/financials.md`. [Shopify and Stripe UK pricing pages, accessed September
   2026 — verify before modelling]
5. **Policies** — returns, privacy, T&Cs, delivery. UK consumer law is not optional — see
   `@docs/UK-LEGAL-TAX.md` and the `legal/` folder.
6. **The funnel** — product page → cart → checkout. Test it on a phone; most UK ecommerce
   traffic is mobile.

## Apps — resist the temptation
Every app is a monthly cost and a speed cost. Install one only when a real problem demands
it. An email tool with automated flows (e.g. Klaviyo) is the early exception.

## Wiring the brain in
At Phase 2, connect tools as they become relevant, not before: the Shopify Dev MCP (via the
Shopify AI Toolkit), Stripe's hosted MCP, and your email platform's MCP if it has one. Record
each in `state/tech_context.md`.

## The discipline
- A working, plain store that takes money beats a beautiful one that never launches.
- Track conversion rate from day one. Traffic without conversion is a diagnosis, not a failure.
- Fulfilment and returns must be solved before launch, not after — see
  `fulfilment-shipping-uk` and `ops-returns` (physical-goods pack; install `packs/physical`
  if you ship goods yourself), or `@docs/ECOM-OPS.md` for UK carrier rates.
