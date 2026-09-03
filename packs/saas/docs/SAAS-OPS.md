# SaaS Operations Reference (2026 edition)

> Long-form reference. Load on demand via `@docs/SAAS-OPS.md` — do not auto-load.
> Hosting prices, ICO fees, and legal commencement dates change — verify before relying on them.

## Hosting and cost basics (MVP stage)

| Layer | Option | Indicative pricing (2026) | Note |
|-------|--------|---------------------------|------|
| App hosting | Vercel | Hobby free; Pro from $20/seat/mo + usage | Strong default for a Next.js-style front end |
| App hosting | Render | Free tier for static/limited web-service hours; Standard ~$25/mo/service for always-on | Simple full-stack hosting |
| App hosting | Railway | ~$5/mo Hobby, ~$20/mo Pro, after an initial trial credit | Good for a small backend + database together |
| Database | Supabase | Free tier; paid from ~$25/mo | Postgres + auth + storage in one; pairs with any front end |
| Domain + SSL | Any registrar + host | Domain from ~£10/year; SSL is free (Let's Encrypt, or bundled by the host) | Do not pay extra for SSL — it should be included |
| Transactional email | Postmark / Resend | Free tiers up to a few hundred–thousand emails/mo, then usage-based | Needed for password resets, receipts, dunning emails |
| Error tracking | Sentry | Free tier for low volume | Turn on before launch, not after the first bug report |
| Uptime monitoring | UptimeRobot / Better Stack | Free tier for a handful of monitors | Alerts the founder before a customer does |
(vercel.com/pricing, render.com/pricing, railway.com/pricing, supabase.com/pricing,
postmarkapp.com/pricing, resend.com/pricing, sentry.io/pricing, uptimerobot.com/pricing —
checked Sept 2026; verify current tiers before committing, as these change often.)

**The rule at MVP stage:** stay on free or near-free tiers until real usage forces an upgrade.
A £0–£30/month stack is enough to run a live SaaS product for the first paying customers —
match spend to the founder's real budget from the intake (`state/business-brief.md`, section
5), not to what looks professional.

## Uptime and support expectations

- Do not publish a formal uptime SLA (e.g. "99.9% uptime") at MVP stage unless the
  infrastructure genuinely supports it — an unmet promise is worse than none. State what is
  true: "we monitor uptime and respond to incidents promptly."
- Set and meet a stated support response time (e.g. "within one working day") — see
  `ops-customer-service` for the general pattern; a SaaS product adds the need for an
  incident/status update when the product itself is down, not just when a ticket is raised.
- A free status page (e.g. a simple hosted status page, or even a pinned note in the support
  inbox) beats silence during an outage — tell customers you know before they have to ask.
- Log every incident (what broke, for how long, who was affected, the fix) — this becomes the
  first entry in a postmortem habit worth keeping as the venture grows.

## Data protection / UK GDPR for a SaaS

A SaaS product holds personal data by default — at minimum, user accounts and login records.
This is information, not legal advice; confirm the venture's specific obligations with a UK
solicitor or a suitably qualified adviser.

- **ICO registration and the data protection fee** — most organisations processing personal
  data must pay the ICO's data protection fee. As of the rates set from 17 February 2025:
  Tier 1 (micro) £52, Tier 2 (small/medium) £78, Tier 3 (large) £3,763, each £5 lower by direct
  debit (ico.org.uk fee guidance — verify current tiers before paying, as SI 2025/63 was the
  most recent change).
- **Sub-processors** — every hosting, email, analytics, or payment tool that touches customer
  personal data is a sub-processor. Keep a list of them and confirm each has a UK-GDPR-
  compliant Data Processing Agreement (most mainstream providers publish one).
- **International transfers** — if any sub-processor stores or processes data outside the UK
  (common with US-based hosting), a transfer mechanism is required — typically the UK
  International Data Transfer Agreement (IDTA) or the UK Addendum to the EU Standard
  Contractual Clauses. Check each provider's own transfer documentation.
- **PECR** — cookie banners and any tracking script need equal-prominence Accept/Reject
  options; PECR fines now match UK GDPR levels (up to £17.5m or 4% of global turnover, raised
  by the Data (Use and Access) Act 2025) — see `@docs/UK-LEGAL-TAX.md`.
- **Breach notification** — a personal data breach likely to risk individuals' rights must be
  reported to the ICO within 72 hours of the venture becoming aware of it.
- **Privacy policy and DPIA** — write a plain-language privacy policy before the first signup;
  if the product processes any special-category data or does large-scale profiling, a Data
  Protection Impact Assessment is likely required — get this assessed properly rather than
  guessing.

## The metrics dashboard

Track these from the first paying customer, in one place (`state/financials.md` at MVP stage;
a proper dashboard tool such as ChartMogul, Baremetrics, or a PostHog + spreadsheet
combination once volume justifies the cost):

- **MRR / ARR** — monthly and annualised recurring revenue, split into new, expansion,
  contraction, and churned.
- **Logo churn and revenue churn** — see `saas-onboarding-retention` for definitions.
- **NRR** — net revenue retention; see `saas-onboarding-retention`.
- **Activation rate** — the share of signups reaching the defined activation event.
- **D7 / D30 retention** — by signup cohort.
- **CAC, LTV, gross margin** — see `financial-modeling-uk`; a SaaS venture must also net off
  the payment-processor fee (see `saas-pricing-billing-uk`) before margin is real.
- **Runway** — cash ÷ monthly burn, updated whenever a real cost changes.

## The operating rhythm

- **Daily (founder, a few minutes):** check for support requests, failed payments, and any
  monitoring alert.
- **Weekly:** run `weekly-review` — refresh the metrics dashboard, review the phase gate, and
  check the risk register (`state/risks.md`).
- **Monthly:** review pricing and churn trends together — a rising churn rate is often a
  pricing or onboarding signal, not a product-quality one alone.
- **At every phase gate:** re-run `premortem` before committing more spend or founder time to
  the next phase.

---
*Reminder: verify hosting prices, ICO fee tiers, and legal commencement dates against the
current source before relying on them.*
