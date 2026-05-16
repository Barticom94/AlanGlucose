# Ecommerce Operations Reference (2026 edition)

> Long-form reference. Load on demand via `@docs/ECOM-OPS.md` — do not auto-load.
> Pricing and carrier rates change frequently — verify before relying on them.

## Fulfilment — UK carriers

| Carrier | Indicative price (2025 / early 2026) | Best for |
|---------|--------------------------------------|----------|
| Royal Mail | 2nd-class small parcel from ~£3.99; 1st-class stamp rising to £1.80 on 7 Apr 2026 | Letters and lightweight parcels; the only carrier with a Universal Service Obligation |
| Evri | ParcelShop drop-off from ~£2.62 (up to 5kg flat) | Cheapest SME standard delivery; good marketplace integrations; highest customer-complaint share (Ofcom, Oct 2025) |
| DPD | ~£5–£10+ next-day | Premium ecommerce: one-hour Predict window, >95% on-time |
| Yodel | Yodel Direct from ~£2.42–£2.50 via InPost lockers | Cheapest budget option; stricter size limits |

Right-size packaging — oversized parcels pay for air and risk a higher price band. Build
the per-order fulfilment cost into `state/financials.md`.

## Selling to the EU after Brexit

- For consignments **≤ €150**, use **IOSS** (Import One-Stop Shop). A non-EU (UK) seller
  must appoint an **EU-based intermediary** — e.g. Taxually, Hellotax, EAS Project.
- Marketplaces (eBay, Etsy, Amazon) use **their own IOSS** — you do not need yours for
  sales made through them.
- Above €150: standard customs and destination-country import VAT apply.
- The EU's **ViDA** reforms (adopted 18 July 2025) will, from **1 July 2028**, make non-EU
  sellers and marketplaces liable for import VAT in the destination member state.

## Bookkeeping software (December 2025 pricing)

| Software | Cost | Best for | Verdict |
|----------|------|----------|---------|
| **Xero** | Ignite £16, Grow £37, Comprehensive £50, Ultimate £65 /mo | Growing ecommerce SMEs; widest UK accountant adoption; 1,000+ integrations | Recommended once VAT-registered |
| **FreeAgent** | £29/mo, or **free** via NatWest/RBS/Ulster/Mettle (one transaction/month) | Sole traders and freelancers; UK-specific tax workflow | Recommended at the start if banking with Mettle/NatWest |
| **QuickBooks** | Sole Trader £10, Simple Start £14, Essentials £30, Plus £42 | Cheapest sole-trader entry | OK; less ecommerce-strong than Xero |

**Recommendation:** start on FreeAgent (free via Mettle/NatWest); switch to Xero when
crossing the VAT threshold or making the first hire.

## No-code / low-code tool stack for a bootstrapped UK founder

| Tool | Use | Indicative pricing | Note |
|------|-----|--------------------|------|
| Shopify | Ecommerce store | from £19/mo Basic | Native fit for an ecommerce-ops founder |
| Klaviyo | Email / SMS | Free under 250 contacts | Already connected |
| Carrd | Smoke-test landing pages | ~$9/yr | Cheapest for Phase 1 smoke tests |
| Framer / Webflow | Marketing site | £14–£15/mo | Upgrade post-validation |
| Tally | Forms | Free, unlimited | Cheaper than Typeform |
| Notion | Docs / wiki | Free for solo | Pairs with the Notion MCP |
| Cal.com | Bookings | Free self-hosted; ~£14/mo cloud | Calendly alternative |
| PostHog | Product analytics | Free under 1m events/mo | Better data ownership than GA |
| Plausible | Web analytics | ~$9/mo for 10k pageviews | GDPR-friendly; no cookie banner needed |
| Stripe | Payments | ~1.5% + 20p UK cards | Mandatory |

## The operational layer (Phase 2+, once the venture is live)

- **Customer service** — start with Gmail or a Help Scout/Front trial; Chatwoot if
  self-hosting; Gorgias (~£50/mo) once tightly integrated with Shopify is worth it
  (~100+ tickets/month). See the `ops-customer-service` skill.
- **Inventory** — Shopify native to ~£300k revenue; then Cin7 Core or Linnworks. Phase-gate
  threshold: 5,000+ SKUs or multi-warehouse. See `ops-inventory`.
- **Returns** — pre-paid label via Royal Mail Tracked Returns or Evri Returns; refund within
  14 days per the Consumer Contracts Regulations. See `ops-returns` and `@docs/UK-LEGAL-TAX.md`.
- **Suppliers** — score each on lead time, MOQ, defect rate, and payment terms; use the
  Companies House MCP for due diligence. See `ops-suppliers`.
- **SOPs** — every recurring task done more than once a week becomes an SOP in `docs/sops/`.
  See `ops-sops`.

## The automation ladder

- **Automate first:** order confirmations, shipping notifications, abandoned-cart, and
  low-stock alerts — low brand risk, high time saving.
- **Automate last:** customer-service replies (brand risk) and pricing changes (keep manual
  until the rules are clearly proven).

---
*Reminder: verify carrier rates, software pricing, and tax-adjacent figures before relying on them.*
