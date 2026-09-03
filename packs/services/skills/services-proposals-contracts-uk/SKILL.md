---
name: services-proposals-contracts-uk
description: Structure proposals, statements of work, and contract terms for a UK service business — payment terms, IP ownership, liability caps, IR35 awareness, late-payment law, and professional indemnity insurance. Use when the founder asks about proposals, contracts, SOWs, T&Cs, chasing a late payment, IR35, or "am I covered". Terms work is available from Phase 1 — a deposit or letter of intent is Phase 1 gate evidence and needs something in writing. Master agreements and multi-phase SOWs are Phase 2. Information, not legal advice.
---

# Services — Proposals & Contracts (UK)

Phase 1 onward. Written payment terms, an IP clause, and a liability cap belong on the first
paid pilot or deposit — that deposit is Phase 1 gate evidence, and a deposit taken on a
handshake is the risk this skill exists to prevent. Retainer master agreements and
multi-phase SOWs are Phase 2. This is information, not legal advice — a UK solicitor should
draft or review the actual contract before it is relied on for a real engagement.

## Proposal structure
1. **The problem**, stated back in the client's own words — proves the discovery was real.
2. **The deliverable and scope boundary** — what is included, what is explicitly excluded.
3. **Timeline** — milestones, not just a single end date.
4. **Price and payment terms** — see below.
5. **What we need from you** — client-side dependencies; late client input is the single
   most common cause of a slipped timeline.
6. **Next step** — one clear call to action, not three options that dilute the ask.

## Statement of Work (SOW)
For a retainer or a multi-phase engagement, a short SOW sits under the master contract and
covers just that phase: deliverables, dates, price, and acceptance criteria. Reissue a new
SOW for each phase rather than endlessly amending the first one — it keeps scope creep
visible instead of buried in an old document.

## Terms that matter most for a solo service business
- **Payment terms** — invoice on milestone or monthly, due within **14–30 days**
  [ASSUMPTION — low risk, common UK freelance practice, 2026]. A deposit (commonly 30–50%
  [ASSUMPTION — low risk, common UK freelance practice, 2026]) before starting protects
  cashflow and filters out non-serious clients.
- **IP ownership** — state explicitly when IP transfers to the client: on final payment
  (safer for the founder) or on delivery. Silence defaults to messy, case-by-case
  interpretation if it is ever disputed.
- **Liability cap** — cap liability at the fees paid for the engagement (or a stated
  multiple), and exclude indirect or consequential loss. An uncapped liability clause is a
  real personal and business risk for a solo operator.
- **Late payment** — UK law already gives a B2B supplier a fallback even with no clause: the
  **Late Payment of Commercial Debts (Interest) Act 1998** (as amended by the 2002/2013
  Regulations) entitles a supplier to statutory interest of **8% over the Bank of England
  base rate** (base rate held at 3.75% on 30 July 2026, giving roughly 11.75% total —
  verify the current rate at bankofengland.co.uk before invoicing) plus fixed compensation
  per unpaid invoice: **£40** under £1,000, **£70** for £1,000–£9,999.99, **£100** for
  £10,000+. State this right in the contract so it is not a surprise if it is ever invoked.
- **Unpaid invoices** — Money Claim Online (moneyclaim.gov.uk) accepts claims up to
  **£100,000** from litigants in person and is the cheapest way to issue. Allocation is
  separate: claims up to **£10,000** normally go to the small claims track (limited costs
  recovery, no solicitor needed), £10,000–£25,000 to the fast track, £25,000–£100,000 to the
  intermediate track, above that the multi-track. Take a solicitor's advice above the
  small-claims limit, where adverse costs become a real risk. [HMCTS / CPR Part 26 — verify
  at gov.uk]
- **Data processing** — if the engagement gives access to the client's customer or staff
  data, add a short data-processing clause covering what is accessed, retention, and
  deletion on offboarding. UK GDPR and the ICO apply regardless of contract wording — see
  `@docs/UK-LEGAL-TAX.md` for the current position.

## IR35 / off-payroll working — if trading through a limited company
- IR35 governs whether an engagement should really be taxed as employment. It matters when
  the founder works through a personal service company (Ltd) and, in practice, the
  engagement looks like employment by the client — fixed hours, their equipment, no
  substitution right, ongoing supervision.
- For a **medium or large private-sector client**, the client determines the engagement's
  status and, if "inside IR35", the fee-payer deducts tax at source (off-payroll working
  rules, in force since April 2021). **Small clients are exempt** from making that
  determination — from **6 April 2026**, a client counts as "small" if it meets 2 of 3:
  turnover ≤ **£15m**, balance sheet ≤ **£7.5m**, ≤ **50 employees** (financial thresholds
  rising from £10.2m/£5.1m; the effective date for any one client depends on their
  financial-year end — verify on gov.uk). Where the client is small, the founder's own
  limited company must self-assess status.
- Genuine substitution rights, control over how and when the work is done, and multiple
  concurrent clients all support "outside IR35" — but this is a facts-based test on the
  actual working pattern, not a checkbox exercise. HMRC's CEST tool is a starting point
  only; confirm any real IR35 position with a UK accountant.

## Professional indemnity (PI) insurance
- Covers a claim that the founder's advice, work, or a mistake caused the client a financial
  loss — the core risk in a services business, distinct from public liability (physical
  injury or property damage — see `docs/SERVICES-OPS.md`).
- Many corporate clients will not sign without proof of PI cover, sometimes at a stated
  minimum (commonly £1m [ASSUMPTION — low risk, common UK freelance practice, 2026]).
- Indicative cost is wide and profession-dependent: roughly **£150–£400/year** for £250k
  cover for a general freelancer, rising toward **£300–£900+/year** for higher-risk advisory
  work [ASSUMPTION — medium risk; comparison-site ranges, 2026 — get 2–3 live quotes, e.g.
  Hiscox or Simply Business, before budgeting a figure].
- Some professions (e.g. solicitors, financial advisers, insurance brokers) are legally or
  regulator-required to hold PI cover — check whether the founder's specific field carries a
  professional-body requirement before assuming it is optional.

## How to use this skill
1. Draft the proposal using the structure above; keep it to a page the client can decide
   from without needing a call.
2. Insert the payment-terms, IP, and liability clauses before the first client signs
   anything — do not add them retroactively once a dispute starts.
3. If trading through a Ltd, run the IR35 facts test against the actual working pattern of
   each engagement, not just the contract wording.
4. Get a PI quote before quoting any client who asks for proof of cover.
5. Route a real contract dispute or drafting question to a UK solicitor — this skill
   structures the conversation, it does not replace one.

## Output
Log the chosen payment terms, liability cap, and IP position in `state/decisions_log.md`.
Record the PI insurer, cover level, and premium in `state/financials.md` once bound.
