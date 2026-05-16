---
name: ecom-fulfilment-uk
description: Plan UK and EU order fulfilment — carriers, shipping costs, packaging, returns logistics, and post-Brexit EU sales. Use when the founder asks about shipping, delivery, couriers, Royal Mail, Evri, DPD, postage costs, or selling to the EU.
user-invocable: true
---

# Ecommerce — Fulfilment (UK)

Shipping cost and reliability sit directly on the P&L and on customer satisfaction. Get the
carrier choice and the per-order cost into `state/financials.md` before launch.

## UK carriers — match the carrier to the parcel
- **Royal Mail** — best for letters and lightweight parcels; the only carrier with a
  Universal Service Obligation. 2nd-class small parcel from roughly £3.99.
- **Evri** — typically cheapest for SME standard delivery, with good marketplace
  integrations; but it carries the highest customer-complaint share, so weigh price against
  experience.
- **DPD** — premium: a one-hour delivery window and strong on-time performance. Best for
  higher-value orders where the experience matters.
- **Yodel** — budget option via lockers; stricter size limits.
Compare live rates — carrier prices change (Royal Mail typically reprices in spring).

## Packaging
- Right-size the box — oversized parcels pay for air and risk a higher price band.
- Branded but cheap beats expensive. Factor packaging into COGS, not "marketing".

## Returns logistics
A returns process is a legal requirement, not a nicety — see `ops-returns`. Decide pre-paid
vs customer-paid labels and build the cost into the model.

## Selling to the EU after Brexit
- For consignments ≤ €150, use **IOSS** (Import One-Stop Shop). A non-EU (UK) seller must
  appoint an EU-based intermediary — e.g. Taxually, Hellotax, EAS.
- Marketplaces (eBay, Etsy, Amazon) use their own IOSS — you do not need yours for those sales.
- Above €150: standard customs and destination import VAT apply.
- EU sales add real cost and complexity — do not assume they are free upside. Model them.

## Method
1. Estimate parcel weight and dimensions for the actual product.
2. Get live quotes from 2-3 carriers; choose on total cost plus reliability.
3. Put the per-order fulfilment cost into `state/financials.md` and the unit economics.
