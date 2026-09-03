# Pack — Services

Consulting, freelancing, agency, coaching, and any other venture whose core offer is the
founder's (or the venture's) time, expertise, or delivered work — rather than a physical
product, a digital product, or a marketplace.

## When the brain installs this pack
The `business-intake` skill installs this pack when the intake answer to section 1.2
("What you'll actually sell") describes the venture as a service — the founder is selling
their expertise, time, or a delivered piece of work, billed per engagement, per day, or on
retainer, rather than shipping a product. If the founder's answer mixes models (e.g. a
software product with a paid onboarding service, or physical goods with fitting/installation
included), install this pack alongside whichever other pack matches the other half of the
offer — see "Packs are additive", below.

## Skills in this pack
- **`services-productised-offer`** — turn expertise into a sellable, repeatable offer:
  productised packages, scope boundaries, fixed price vs day rate vs retainer, pricing from
  value rather than hours, and landing the first three clients.
- **`services-proposals-contracts-uk`** — proposal structure, statements of work, and UK
  contract terms: payment terms, IP ownership, liability caps, IR35 awareness, the Late
  Payment of Commercial Debts legislation, and professional indemnity insurance. Information,
  not legal advice.
- **`services-delivery-capacity`** — delivering without burning out: capacity planning
  against the founder's real hours, when to subcontract vs hire, client onboarding and
  offboarding, and referrals as the primary channel.

## Ops document
- **`docs/SERVICES-OPS.md`** — the engagement lifecycle end to end, invoicing and UK
  late-payment rules, professional indemnity and public liability insurance, scope-creep
  control, and the weekly/per-engagement/monthly operating rhythm. Load on demand via
  `@docs/SERVICES-OPS.md` — it is not auto-loaded at session start.

## Packs are additive
A venture is not limited to one pack. A software product sold with paid implementation
consulting, or a physical-goods business that also sells bespoke fitting services, can have
this pack installed alongside `ecommerce`, `saas`, or `physical` — each pack's skills and ops
doc apply to the slice of the venture they cover. Installing this pack does not remove or
override any other pack already installed, and none of the core skills in `.claude/skills/`
(financial modelling, UK tax, legal structure, pricing, sales, customer discovery, and so on)
change — this pack only adds the services-specific layer on top of them.
