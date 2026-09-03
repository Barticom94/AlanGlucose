# Physical Operations Reference (2026 edition)

> Long-form reference. Load on demand via `@docs/PHYSICAL-OPS.md` — do not auto-load.
> Licence fees, rates, and thresholds change often — verify every figure before relying on it.
> This document is information, not legal advice.

## The physical operating loop

Source → Stock → Sell → Ship or serve → Returns, repeating. Each stage carries its own UK
rule and its own skill:

1. **Source** — vet suppliers, order samples before volume, get lead time and defect rate in
   writing. See `ops-suppliers`.
2. **Stock** — hold only what cash allows; track reorder point and days of cover. See
   `ops-inventory`.
3. **Sell** — a till or card reader on a premises, a stall or van in person, or a booked
   service visit. The channel decides which licences (below) apply.
4. **Ship or serve** — dispatch and carrier if physical goods move to the customer (see
   `fulfilment-shipping-uk`), or the service delivery itself if the "product" is the founder's
   or a contractor's time on site.
5. **Returns** — faulty goods, cancellations, and complaints, on the clock UK consumer law
   sets. See `ops-returns`.

## Premises basics

- A lease, a licence to occupy, or no fixed premises (mobile/pop-up) are three different
  commitments with different exit costs — see `premises-licensing-uk` for the full breakdown
  of leases, business rates, and planning use classes.
- Business rates and Small Business Rate Relief apply to a fixed premises; a mobile stall
  instead needs a street trading licence, not a rates bill.
- A market stall, van, or short pop-up is often the cheapest way to test in-person demand
  before committing to a fixed lease — treat it as the Phase 1/2 validation step for a
  physical venture, the same role a smoke-test landing page plays for an online one.

## Product safety and marking

- The General Product Safety Regulations 2005 remain the current baseline in Great Britain:
  products placed on the market must be safe, and producers/distributors carry due-diligence
  duties (gov.uk). A government consultation to overhaul this framework — aligning closer to
  the EU's 2023 General Product Safety Regulation — closed in June 2026; check gov.uk for
  whether it has become law before relying on the 2005 regime as the final word.
- UKCA marking: for most product categories the UK government has confirmed that CE marking
  continues to be accepted in Great Britain indefinitely, so either UKCA or CE marking
  currently satisfies GB market requirements for most goods. Some sectors (construction
  products, medicines) run different timelines. Verify the current position for the specific
  product category on gov.uk before finalising labels or packaging artwork
  [verify on gov.uk — position confirmed as of Sep 2026].
- Selling into Northern Ireland or the EU still requires CE marking (and UKNI marking in some
  NI cases) — do not assume a GB-only marking strategy covers all four nations.

## Labelling

- Pre-packed goods sold by weight or volume must be accurately labelled (Weights and Measures
  Act 1985; Price Marking Order 2004 for unit pricing).
- Food prepacked for direct sale (PPDS) — sandwiches, cakes, salads made and packaged on the
  premises before sale — must show the food name, a full ingredients list, and all 14 major
  allergens emphasised within it ("Natasha's Law", in force since 1 October 2021). There is no
  small-business or market-stall exemption.
- General product labelling — country of origin, safety warnings, care instructions — varies
  by sector; check the specific category's rules via gov.uk's Business Companion guidance
  before a print run.

## Food hygiene

- Register any food business with the local authority, free of charge, at least 28 days
  before trading (Food Standards Agency, gov.uk).
- The Food Hygiene Rating Scheme (0–5 in England, Wales, and Northern Ireland; Pass /
  Improvement Required in Scotland) is public and searchable — a poor first inspection is a
  trading risk, not paperwork. Prepare with the FSA's Safer Food Better Business pack.
- See `premises-licensing-uk` for the licensing detail and `ops-customer-service` for handling
  a complaint that touches food safety.

## Packaging waste — Extended Producer Responsibility (pEPR)

- Since April 2025, UK producers of packaging pay fees under the revised Extended Producer
  Responsibility for Packaging scheme, administered by PackUK.
- Obligation thresholds: no obligation below £1m annual turnover **and** under 25 tonnes of
  packaging supplied/imported a year. Between £1–2m turnover (or 25–50 tonnes) makes a
  business a "small producer" with reporting duties only. £2m+ turnover **and** 50+ tonnes
  makes it a "large producer" with reporting **and** fee-paying duties (gov.uk / DEFRA,
  verified Sep 2026).
- 2026/27 base fees are higher than year 1 — indicatively around £455/tonne for plastic and
  £205/tonne for glass, up from £423 and £192 in 2025/26 (PackUK, verify the confirmed figures
  on gov.uk before modelling). From 2026/27 fees are also modulated by a red/amber/green
  recyclability rating under PackUK's Recyclability Assessment Methodology, with a 1.2×
  multiplier on red-rated packaging rising in later years.
- Most bootstrap-stage physical ventures sit below the £1m/25-tonne threshold and carry no
  obligation yet — but model the cliff into `state/financials.md` once turnover approaches
  £1m, with the same discipline as the VAT threshold in `uk-tax-vat-mtd`.

## The UK rules that bite, at a glance

| Rule | Trigger | Who enforces |
|---|---|---|
| Food business registration | Selling, preparing, or storing any food or drink | Local authority, via the FSA |
| Premises and personal alcohol licence | Selling alcohol | Local authority licensing team |
| Street trading licence | Trading from a stall, market, or the street | Local authority |
| TheMusicLicence | Playing recorded or live music (inc. radio) on premises | PRS for Music / PPL |
| UKCA/CE marking | Manufacturing or importing most regulated goods | OPSS / Trading Standards |
| Natasha's Law (PPDS labelling) | Prepacking food for direct sale | Local authority, via the FSA |
| pEPR packaging fees | £1m+ turnover and 25+ tonnes of packaging a year | PackUK / Environment Agency |
| Employers' liability insurance | Any employee | HSE-enforced; sold by FCA-regulated insurers |
| Written H&S policy and recorded risk assessment | 5+ employees (policy and written record); a risk assessment is owed by every business regardless of size | HSE |

## The discipline

Do not build a premises-heavy physical venture before the Phase 1 gate (≥ 3 real
commitments). A market stall, a short pop-up, or a handful of paid in-person pilots is a
legitimate, low-cost way to gather those commitments — treat it as validation, not the MVP.

---
*Reminder: verify every fee, threshold, and rule against gov.uk or the relevant regulator
before relying on it. This is information, not legal advice.*
