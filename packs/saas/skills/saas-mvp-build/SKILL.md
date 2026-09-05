---
name: saas-mvp-build
description: Decide how to build the smallest sellable version of the software — no-code/low-code, AI-assisted code, or hiring a developer — and what to build at each stage. Use when the founder asks about building the MVP, "should I code this myself", no-code tools, hiring a developer, a concierge or Wizard-of-Oz test, or is ready to build after validation. Nothing is built before the Phase 1 gate; full build from Phase 2 — MVP.
---

# SaaS — MVP Build

Phase 2 — MVP, once the Phase 1 gate is met (≥ 3 real commitments — a deposit, a letter of
intent, or a waitlist sign-up with card details). Before that gate, build nothing. A working
product before validation is not progress — it is the most expensive way to avoid talking to
customers.

## How to use this skill
1. Confirm the Phase 1 gate is actually met — check `state/progress.md`. If not, redirect to
   `customer-discovery` and stop here.
2. Establish what the smallest sellable version actually needs to do — the one job the
   beachhead persona (`state/product_context.md`) is paying to get done. Cut everything else.
3. Choose the build route (below) against the founder's real skills, budget, and hours from
   the intake (`state/business-brief.md`, section 5) — not a fixed assumption.
4. Before committing money or a developer's time, run a concierge or Wizard-of-Oz test if one
   is possible — it is almost always cheaper and faster.
5. Record the decision and the reasoning in `state/decisions_log.md`.
6. Run the `red-team-devils-advocate` skill before a build that costs more than a token amount
   of money or takes more than a couple of weeks — building the wrong thing well is still
   failure.

## Concierge and Wizard-of-Oz — build nothing, prove the job
- **Concierge:** deliver the outcome by hand — spreadsheets, email, a manual process behind
  the scenes — while charging as if the product existed. Proves people will pay before a
  line of code is written.
- **Wizard-of-Oz:** a real-looking front end where a human does the work behind the curtain.
  Proves the interaction model, not just the willingness to pay.
- Both only count as evidence under `evidence-bar` if the founder actually charged, or asked
  for a real commitment — free trials of a fake product prove nothing.
- Graduate off concierge/Oz once it stops scaling with the founder's real hours from the
  intake (section 5) — that ceiling is itself useful data for the pricing and ops model.

## The three build routes
1. **No-code / low-code** — Bubble (Starter $59/mo billed annually; Growth $209/mo —
   bubble.io/pricing, Sept 2026; note workload-unit overage at $0.30/1K WU is uncapped), Glide
   (Business ~$199/mo, has a free tier to prototype on), Softr (Basic $59/mo, ~$49/mo billed
   annually; Professional $167/mo — softr.io/pricing, Sept 2026) [verify current pricing on
   each platform before committing]. Fastest to a sellable product; weakest on complex logic,
   and migrating off later is real work. Best when the product is mostly forms, workflows, and
   a database.
2. **AI-assisted code** — tools such as Lovable, Bolt.new, Replit, or Claude Code paired with a
   framework; entry tiers cluster around $20–$25/month plus usage-based credits, but the credit
   component dominates real cost — price the specific tool on its own pricing page before
   committing [ASSUMPTION — M — entry-tier band, not a vendor quote]. Good middle ground
   for a founder with some technical comfort who wants real code without hiring.
3. **Hiring a developer** — median UK contractor day rate ~£500 (itjobswatch.co.uk, data to 21
   Apr 2026), with a London premium of roughly 20–30%; junior work runs lower, senior/
   specialist work higher [source: itjobswatch.co.uk, Apr 2026 — verify current rate before
   budgeting]. Justified when the product needs real engineering the founder cannot supply and
   the commitments already taken (Phase 1 gate) support the spend — check the numbers in
   `financial-modeling-uk` first.

## When real code is justified
Real code (hired or AI-assisted) earns its cost when: the no-code platform cannot express the
core logic, the product needs to scale past a no-code platform's workload/row limits, or the
founder plans to raise investment and needs defensible IP in owned code rather than a
third-party platform. Otherwise, the fastest route to a paying customer wins — the platform
can always be replaced once revenue proves the model.

## UK specifics
- If hiring a developer, get IP assignment in writing. Under the Copyright, Designs and
  Patents Act 1988, a freelance contractor owns the copyright in what they build **unless** a
  written contract assigns it to the venture — get this before work starts, not after.
- If the product handles personal data (almost all SaaS does — at minimum, user accounts),
  registering with the ICO and paying the data protection fee applies once trading — see
  `@docs/SAAS-OPS.md`.
- This is information, not legal advice — for the IP contract and any employment-status
  question (a long-term contractor may fall inside IR35), engage a UK solicitor or chartered
  accountant.

## Output
Record the build-route decision, the reasoning, and the cost in `state/decisions_log.md`.
Update `state/tech_context.md` with the chosen stack/platform and its constraints. Update
`state/financials.md` with the build cost and any ongoing platform fee.
