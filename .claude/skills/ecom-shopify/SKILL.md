---
name: ecom-shopify
description: Build and run a Shopify store. Use when the founder asks about Shopify, setting up the online store, themes, apps, the product catalogue, checkout, or the storefront. Triggered at Phase 2 (MVP), not before validation.
user-invocable: true
---

# Ecommerce — Shopify

Shopify is the right platform for this founder — it matches an ecommerce-operations
background and handles hosting, payments, security, and PCI compliance. Do not build the
store until the Phase 1 gate is met — ≥ 3 real commitments. A store before validation is a
costly distraction.

## MVP store — the minimum that takes money
1. **Plan** — start on Basic (~£19/month). Do not pay for features you will not use.
2. **Theme** — a free Shopify theme, lightly customised. Speed and trust beat bespoke design.
3. **Products** — honest titles, real photos, accurate descriptions. Copy via the
   `copywriter-brand-voice` subagent.
4. **Payments** — Shopify Payments / Stripe. Know the fee (~1.5% + 20p on UK cards) and put
   it in `state/financials.md`.
5. **Policies** — returns, privacy, T&Cs, delivery. UK consumer law is not optional — see
   `@docs/UK-LEGAL-TAX.md` and the `legal/` folder.
6. **The funnel** — product page → cart → checkout. Test it on a phone; most UK ecommerce
   traffic is mobile.

## Apps — resist the temptation
Every app is a monthly cost and a speed cost. Install one only when a real problem demands
it. Klaviyo for email is the early exception (already connected).

## Wiring the brain in
At Phase 2, add the growth-pack MCPs as they become relevant — Shopify Dev MCP, Stripe,
Klaviyo (see `state/tech_context.md`).

## The discipline
- A working, plain store that takes money beats a beautiful one that never launches.
- Track conversion rate from day one. Traffic without conversion is a diagnosis, not a failure.
- Fulfilment and returns must be solved before launch, not after — see `ecom-fulfilment-uk`.
