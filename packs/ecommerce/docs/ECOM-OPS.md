# Ecommerce Operations Reference (2026 edition)

> Long-form reference. Load on demand via `@docs/ECOM-OPS.md` — do not auto-load.
> Pricing and carrier rates change frequently — verify before relying on them.

> **Phase gate.** Everything below is Phase 2+ operating detail. Reading it as research is
> fine at any phase; do not subscribe to, install, or pay for anything in it until the
> Phase 1 gate is met — ≥ 3 real commitments (`AGENTS.md`). The only Phase-1-safe row in the
> tool table is Carrd for smoke-test landing pages.

## Fulfilment — UK carriers

| Carrier | Indicative price (checked September 2026) | Best for |
|---------|--------------------------------------|----------|
| Royal Mail | 2nd-class small parcel from ~£4.19; 1st-class stamp £1.80, 2nd class 91p since 7 April 2026 [Royal Mail April 2026 tariff — verify at royalmail.com] | Letters and lightweight parcels; the only carrier with a Universal Service Obligation |
| Evri | ParcelShop drop-off from ~£2.62 (up to 5kg flat) [reported pricing, accessed September 2026 — verify at evri.com] | Cheapest SME standard delivery; good marketplace integrations; highest customer-complaint share [Ofcom, October 2025 — verify at ofcom.org.uk] |
| DPD | ~£5–£10+ next-day [reported pricing, accessed September 2026 — verify at dpd.co.uk] | Premium ecommerce: one-hour Predict window, >95% on-time [ASSUMPTION — M — not from a published source] |
| Yodel | Yodel Direct from ~£2.42–£2.50 via InPost lockers [reported pricing, accessed September 2026 — verify at yodel.co.uk] | Cheapest budget option; stricter size limits |

`fulfilment-shipping-uk` (physical-goods pack) owns carrier selection method; this table is
the indicative price reference only. Update prices here, and cross-check that skill when
Royal Mail reprices each spring.

Right-size packaging — oversized parcels pay for air and risk a higher price band. Build
the per-order fulfilment cost into `state/financials.md`.

## Selling to the EU after Brexit

- For consignments ≤ €150, IOSS still handles import VAT; a non-EU (UK) seller must appoint
  an EU-based intermediary (e.g. Taxually, Hellotax, EAS Project). [gov.uk / EU Commission,
  accessed September 2026]
- **Customs duty is no longer nil below €150.** The EU abolished the €150 duty de minimis
  from 1 July 2026; a temporary flat €3 duty applies per 4-digit tariff heading in the
  consignment (three headings in one parcel = €9), running until the EU Customs Data Hub
  goes live in mid-2028, after which standard tariff rates apply. Build this into per-order
  EU cost, not just VAT. [Council of the EU press release, 11 February 2026 — verify on
  consilium.europa.eu]
- Marketplaces (eBay, Etsy, Amazon) use their own IOSS — you do not need yours for sales
  made through them.
- The EU's ViDA package was adopted 11 March 2025 and entered into force 14 April 2025; its
  1 July 2028 deemed-supplier rule covers short-term accommodation and passenger-transport
  platforms, not goods. Mandatory IOSS was dropped from ViDA. [OJEU 25 March 2025 — verify
  before relying on it]

## Bookkeeping software

**Bookkeeping** — software choice and the FreeAgent/Xero/QuickBooks trade-off are core, not
ecommerce-specific: see the `bookkeeping-uk` skill. Pricing changes several times a year;
check the vendor's own page rather than any figure written down here.

## No-code / low-code tool stack for a bootstrapped UK founder

| Tool | Use | Indicative pricing | Note |
|------|-----|--------------------|------|
| Shopify | Ecommerce store | £25/mo Basic on monthly billing; £19/mo only if paying 12 months upfront [Shopify UK pricing page, accessed September 2026] | Native fit for an online store |
| Klaviyo | Email / SMS | Free under 250 contacts [Klaviyo pricing page, accessed September 2026] | Strong default for online stores |
| Carrd | Smoke-test landing pages | ~$9/yr [Carrd pricing page, accessed September 2026] | Cheapest for Phase 1 smoke tests |
| Framer / Webflow | Marketing site | £14–£15/mo [vendor pricing pages, accessed September 2026] | Upgrade post-validation |
| Tally | Forms | Free, unlimited [Tally pricing page, accessed September 2026] | Cheaper than Typeform |
| Notion | Docs / wiki | Free for solo [Notion pricing page, accessed September 2026] | Pairs with the Notion MCP |
| Cal.com | Bookings | Free self-hosted; ~£14/mo cloud [Cal.com pricing page, accessed September 2026] | Calendly alternative |
| PostHog | Product analytics | Free under 1m events/mo [PostHog pricing page, accessed September 2026] | Better data ownership than GA |
| Plausible | Web analytics | ~$9/mo for 10k pageviews [Plausible pricing page, accessed September 2026] | GDPR-friendly; no cookie banner needed |
| Stripe | Payments | ~1.5% + 20p UK cards [Stripe UK pricing page, accessed September 2026] | Mandatory |

## The operational layer (Phase 2+, once the venture is live)

- **Customer service** — start with Gmail or a Help Scout/Front trial; Chatwoot if
  self-hosting; Gorgias (~£50/mo) [ASSUMPTION — M — not from a published source]
  once tightly integrated with Shopify is worth it (~100+ tickets/month)
  [ASSUMPTION — M — not from a published source]. See the `ops-customer-service`
  skill.
- **Inventory** — Shopify native to ~£300k revenue [ASSUMPTION — M — not from a
  published source]; then Cin7 Core or Linnworks. Phase-gate threshold: 5,000+ SKUs or
  multi-warehouse [ASSUMPTION — M — not from a published source]. See
  `ops-inventory` (physical-goods pack — install `packs/physical` if you hold stock).
- **Returns** — pre-paid label via Royal Mail Tracked Returns or Evri Returns; refund within
  14 days per the Consumer Contracts Regulations. See `ops-returns` (physical-goods pack —
  install `packs/physical` if you hold stock) and `@docs/UK-LEGAL-TAX.md`.
- **Suppliers** — score each on lead time, MOQ, defect rate, and payment terms; use the
  Companies House MCP for due diligence. See `ops-suppliers` (physical-goods pack — install
  `packs/physical` if you hold stock).
- **SOPs** — every recurring task done more than once a week becomes an SOP in `docs/sops/`.
  See `ops-sops`.

## The automation ladder

- **Automate first:** order confirmations, shipping notifications, abandoned-cart, and
  low-stock alerts — low brand risk, high time saving.
- **Automate last:** customer-service replies (brand risk) and pricing changes (keep manual
  until the rules are clearly proven).

---
*This document is information, not legal, tax or accounting advice. Carrier rates, software
pricing and tax-adjacent figures change frequently — verify before relying on them. Before
any VAT-registration, IOSS, customs or returns-policy decision, engage a UK chartered
accountant or solicitor.*

## See also
- `ecom-marketplaces-uk` — selling via Amazon UK, Etsy, eBay, and TikTok Shop instead of, or
  alongside, an own store.
- `ecom-conversion-analytics` — GA4 setup, the five metrics that matter, and CRO.
