---
name: fulfilment-shipping-uk
description: Plan UK and EU order fulfilment — carriers, shipping costs, packaging, returns logistics, and post-Brexit EU sales. Use when the founder asks about shipping, delivery, couriers, Royal Mail, Evri, DPD, postage costs, or selling to the EU. Phase 2 and beyond — get quotes at Phase 1, but do not sign a carrier account or buy packaging before the Phase 1 gate.
---

# Fulfilment & Shipping (UK)

A physical venture may hand goods over in person or deliver locally with no carrier involved
at all — this skill applies only once goods move to the customer by carrier.

Shipping cost and reliability sit directly on the P&L and on customer satisfaction. Get the
carrier choice and the per-order cost into `state/financials.md` before launch.

## How to use this skill
1. Confirm the gate first — check `state/progress.md`. Get quotes at Phase 1 as research; do
   not sign a carrier account or buy packaging stock before the Phase 1 gate.
2. Confirm the goods actually need a carrier — in-person handover or local delivery may make
   this skill unnecessary.
3. Match the carrier to the parcel (below) and get live quotes from 2-3 carriers.
4. Right-size the packaging and cost it into COGS, not marketing.
5. Decide the returns-logistics route alongside `ops-returns`.
6. If selling to the EU, work through the IOSS section below before quoting a landed price.
7. Put the per-order fulfilment cost into `state/financials.md` and the unit economics.

## UK carriers — match the carrier to the parcel
- **Royal Mail** — best for letters and lightweight parcels; the only carrier with a
  Universal Service Obligation. 2nd-class small parcel from about £4.19 online [Royal Mail
  tariff from 7 April 2026 — verify; it now reprices more than once a year].
- **Evri** — typically cheapest for SME standard delivery, with good marketplace
  integrations; but it has sat at or near the bottom of Citizens Advice's annual parcel
  league table in recent years — check the current table, and weigh price against experience.
- **DPD** — premium: a one-hour delivery window and strong on-time performance. Best for
  higher-value orders where the experience matters.
- **Yodel** — budget option via lockers; stricter size limits.
Compare live rates — every carrier reprices at least yearly, some more often.

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
- This is information, not tax advice. IOSS registration, choosing an intermediary, and
  destination-VAT treatment above €150 all carry real liability — engage a UK chartered
  accountant with cross-border VAT experience before registering or shipping. See
  `uk-tax-vat-mtd`.

## Method
1. Estimate parcel weight and dimensions for the actual product.
2. Get live quotes from 2-3 carriers; choose on total cost plus reliability.
3. Put the per-order fulfilment cost into `state/financials.md` and the unit economics.

## Output
Update `state/financials.md` with the per-order fulfilment cost. Log the carrier choice in
`state/decisions_log.md`.
