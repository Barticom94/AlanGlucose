---
name: saas-onboarding-retention
description: Define the activation event, design onboarding, track D7/D30 retention, logo churn and NRR, build the cancellation flow, and apply UK consumer-subscription law. Use when the founder asks about onboarding, activation, "why are people not coming back", churn, retention metrics, cancellation, auto-renewal, or NRR. Phase 2 — MVP once there are live users; the retention metrics themselves are the Phase 2 → 3 gate.
---

# SaaS — Onboarding & Retention

Phase 2 — MVP, once real users exist to onboard. Do not build onboarding flows or retention
tooling before the Phase 1 gate — with no paying commitments yet, there is nothing to retain.
7-day retention data is a required input to the Phase 2 → 3 gate (10 paying customers and
7-day retention data), so this skill becomes central as soon as the MVP has live users.

## How to use this skill
1. Define the activation event (below) before building any onboarding flow — an onboarding
   flow with no defined destination is just a tour.
2. Instrument it. If the product cannot yet tell whether a user reached activation, that is
   the first build task, ahead of any onboarding polish.
3. Design the onboarding flow to get a new user to the activation event as fast as possible,
   cutting every step that does not serve that.
4. Track D7/D30 retention and logo churn from the first cohort onward — even 10 users produce
   a directionally useful number.
5. Build the cancellation flow to the current UK legal standard (below) before the first
   paying customer, not after a complaint.
6. Report retention and churn numbers in `state/progress.md` at every `weekly-review`.

## The activation event
The single action that most strongly predicts a user will stick around and pay — not "signed
up", not "logged in". Define it by working backwards from the job the beachhead persona hired
the product to do (`state/product_context.md`): the first moment they get real value, not the
first moment they touch the UI. Write it down as one specific, measurable event (e.g. "created
their first project and invited a teammate"), not a vague feeling.

## Onboarding
- Aim the whole flow at the activation event — every screen, field, and email should either
  move the user toward it or explain why it matters.
- Cut setup steps that can default sensibly or be asked for later. Every field is a chance to
  quit.
- Use in-product prompts (checklists, empty states with a clear next action) over a one-off
  welcome email — the moment of use beats the moment of signup.
- Re-test the flow after every material product change; onboarding rots quietly as the product
  grows around it.

## Retention metrics
- **D7 / D30 retention** — the share of a signup cohort still active 7 and 30 days later.
  Track by cohort (week or month of signup), not as a single rolling number, or product
  changes get hidden inside an average.
- **Logo churn** — the percentage of paying customers who cancel in a period. A commonly cited
  healthy range for small-business SaaS is under ~5% monthly, tightening toward under 1% for
  enterprise contracts [ASSUMPTION — M — a widely cited industry rule of thumb, not a
  single dated source — check current benchmark reports (e.g. ChartMogul, ProfitWell) before
  treating it as a target].
- **Net revenue retention (NRR)** — revenue from the existing customer base this period versus
  the same base last period, including upgrades, downgrades, and churn. Above 100% means
  expansion revenue outpaces churn; best-in-class B2B SaaS is commonly cited around 110–120%+
  [ASSUMPTION — M — a widely cited benchmark range, not a single dated source — verify
  against a current SaaS benchmark report before relying on it].
- Put all three in `state/financials.md` and re-check them at every `weekly-review`.

## Cancellation flow
- Cancellation must be at least as easy as sign-up — do not gate it behind a phone call, a
  "retention" chat requirement, or a hidden settings page. The Competition and Markets
  Authority has previously taken enforcement action against subscription businesses that made
  cancelling deliberately hard, under existing consumer-protection law.
- A save offer (discount, pause) can be presented once, but must not block or delay the actual
  cancellation if the customer declines it.
- Confirm the cancellation in writing (email) with the effective date and what happens to the
  customer's data.

## UK consumer law on subscriptions and auto-renewal
- **Current law:** the Consumer Contracts Regulations 2013 give consumers a 14-day
  cancellation right on most distance-sold services, though for digital content the right is
  lost once supply begins **only if** the consumer gave express consent, separately
  acknowledged that the cancellation right would be lost, and the trader confirmed both in the
  order confirmation on a durable medium (reg. 37, SI 2013/3134). Miss any one of the three and
  the 14-day right survives and the consumer pays nothing for what was supplied. The Consumer
  Rights Act 2015 makes unfair contract terms (e.g. an unreasonably hard cancellation process)
  unenforceable.
- **Coming law:** the Digital Markets, Competition and Consumers Act 2024 introduces a
  dedicated subscription-contracts regime — pre-contract information duties, mandatory
  renewal reminders before auto-renewal, and two statutory cooling-off periods and easy-exit
  rules. The Government's consultation response (2 April 2026) set commencement at spring 2027,
  but on 10 August 2026 the Prime Minister announced the go-live is being brought forward to
  **January 2027**. The confirmed regime includes two cooling-off periods, enhanced refund
  rules, and prescriptive pre-contract information and renewal-reminder duties. Plan to the
  January 2027 date and verify the current position on GOV.UK / legislation.gov.uk, as the date
  has moved in both directions.
- Build to the higher, coming standard now (clear pre-signup pricing, a reminder before any
  annual renewal, one-click cancellation) — it costs little extra at MVP stage and avoids a
  rebuild later.
- This is information, not legal advice — confirm the venture's actual obligations with a UK
  solicitor before launch, particularly once the DMCCA subscription regime has a firm date.

## Output
Update `state/product_context.md` with the defined activation event. Update
`state/financials.md` with D7/D30 retention, logo churn, and NRR each time they are measured.
Log the cancellation-flow design and its legal basis in `state/decisions_log.md`.
