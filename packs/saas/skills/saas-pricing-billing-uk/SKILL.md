---
name: saas-pricing-billing-uk
description: Set SaaS pricing tiers and trials, choose a billing processor, and handle UK VAT on digital services and failed payments. Use when the founder asks about SaaS pricing, subscription tiers, free trials, monthly vs annual billing, Stripe vs Paddle vs Lemon Squeezy, VAT on software sales, selling to EU customers, or failed/declined payments. Phase 2 — MVP, pricing test-ready from Phase 1.
---

# SaaS — Pricing & Billing (UK)

Phase 2 — MVP, once a price can be tested against real commitments. Do not build a billing
system before the Phase 1 gate (≥ 3 real commitments) — a Typeform and a manual invoice is
enough to take the first payments. See `pricing-strategy` for the underlying pricing method;
this skill covers what is SaaS- and UK-specific on top of it.

## How to use this skill
1. Set the price using `pricing-strategy` first — cost floor, competitor band, value ceiling.
2. Design the tier structure and trial (below) against the beachhead persona's actual buying
   pattern, not a generic 3-tier template copied from a competitor.
3. Choose a billing processor (below) based on whether the founder wants to own tax compliance
   or hand it off.
4. Decide the VAT treatment before the first live sale — get this wrong and it is expensive to
   unwind (see UK VAT section).
5. Build the failed-payment (dunning) flow before launch, not after the first customer churns
   silently from a card decline.
6. Feed the chosen price and processor fee into `financial-modeling-uk` and confirm gross
   margin still clears 40% and LTV/CAC still clears 3.

## Tiers and trials
- Start with 2–3 tiers, not more — each extra tier adds a decision the customer has to make,
  and decision friction costs conversions. Anchor the middle tier as the one most customers
  should pick (the classic "decoy" pattern).
- A free trial (7–14 days) suits a low-touch, self-serve product; a free tier suits a
  product with strong network or habit effects but risks attracting non-payers who never
  convert — decide which problem the venture actually has before choosing.
- Require a card upfront for a trial where the product is genuinely disposable once tried; a
  no-card trial removes friction but produces a weaker signal — the `evidence-bar` standard
  (a real commitment) still applies when reading trial-to-paid conversion as evidence.

## Annual vs monthly
- Annual billing improves cash flow and lowers churn exposure (a customer cannot cancel
  monthly), but defers the founder's read on whether the price and product are working.
  Offer both; a common discount for paying annually is one to two months free (roughly
  15–17%) [ASSUMPTION — low risk: a market convention, not a rule].
- Do not push annual-only before the venture has 7-day/30-day retention data — locking in a
  customer who was going to churn just delays the evidence.

## Stripe vs a merchant of record (Paddle, Lemon Squeezy)
- **Stripe** — the founder is the merchant of record: the venture registers for and remits VAT
  itself. UK standard cards 1.5% + 20p, EEA cards 2.5% + 20p, international cards 3.15% + 20p,
  each +2% where currency conversion is required (premium UK cards 2.8% + 20p), plus Stripe
  Billing at 0.7% of Billing volume on the pay-as-you-go plan (Stripe merged the old 0.5%
  Starter and 0.8% Scale tiers into a flat 0.7% in July 2024) (stripe.com/gb/pricing, Sept
  2026). Cheaper at scale; more admin.
- **Paddle** — a merchant of record: Paddle collects and remits VAT/sales tax on the venture's
  behalf worldwide. Standard fee ~5% + 50¢ per transaction, no separate tax-compliance charge
  (paddle.com pricing pages, 2026 — verify before relying on it). Costs more per transaction;
  removes the VAT-registration and multi-country filing burden entirely.
- **Lemon Squeezy** — also a merchant of record, now owned by Stripe; as of 2026 Stripe is
  building "Stripe Managed Payments" as its own merchant-of-record product and has said Lemon
  Squeezy customers will eventually be migrated to it (lemonsqueezy.com/blog/2026-update) —
  check current status before building on it, since the product's long-term shape is actively
  changing.
- **The decision rule:** a UK-only, VAT-registered founder comfortable with quarterly VAT
  returns can save money on Stripe direct. A founder selling internationally, not yet
  VAT-registered, or who wants zero tax-compliance admin should pay the extra fee for a
  merchant of record. This is information, not tax advice — confirm the choice with a UK
  chartered accountant.

## UK VAT on digital services
- **UK customers:** normal VAT rules apply once the venture crosses the £90,000 registration
  threshold (see `uk-tax-vat-mtd`) — there is no separate digital-services threshold for
  domestic sales.
- **EU consumers (B2C), post-Brexit:** there is no minimum threshold — VAT is due in the
  customer's country from the first sale. A UK seller must either register for VAT in each EU
  member state sold into, or register once for the **non-Union OSS (One Stop Shop)** scheme in
  a single EU member state and file one quarterly return covering all EU sales (commenda.io /
  avask.com, 2026 guidance — verify current mechanics on the EU Commission's OSS pages before
  relying on it). A merchant of record (Paddle, Lemon Squeezy) removes this obligation entirely
  by collecting and remitting the VAT itself.
- **B2B EU sales:** the reverse charge can apply if the business customer provides a valid VAT
  number — verify the current process before relying on it.
- This is information, not tax advice — engage a UK chartered accountant before registering
  for OSS or deciding the VAT treatment of the first international sale.

## Failed-payment handling (dunning)
1. Retry automatically — Stripe's and most processors' default smart-retry logic covers most
   temporary declines (expired card, insufficient funds on payday-adjacent dates).
2. Email the customer at the first failure with a direct link to update their card — do not
   wait for the final retry.
3. Set a grace period (commonly 3–7 days) before suspending access, and say so clearly in the
   emails — a sudden lockout reads as broken software, not a billing issue.
4. Distinguish voluntary churn (cancelled) from involuntary churn (card failed) in
   `state/financials.md` — they need different fixes, and conflating them hides which one the
   venture actually has.

## Output
Update `state/financials.md` with the chosen price, tier structure, processor and its fee, and
the VAT treatment. Log the pricing and processor decision, with reasoning, in
`state/decisions_log.md`.
