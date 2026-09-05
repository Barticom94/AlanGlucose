# Services Operations Reference (2026 edition)

> Long-form reference. Load on demand via `@docs/SERVICES-OPS.md` — do not auto-load.
> Rates, fees, and legal thresholds below are time-sensitive — verify before relying on
> them. This document is information, not legal, tax, or insurance advice.

## The engagement lifecycle
1. **Enquiry** — qualify against the productised offer (see `services-productised-offer`);
   decline or redirect anything outside it rather than silently re-scoping to fit.
2. **Proposal** — see `services-proposals-contracts-uk` for structure and terms.
3. **Contract + deposit** — signed SOW and a deposit (commonly 30–50%
   [ASSUMPTION — L — common UK freelance practice, 2026]) before work starts.
4. **Onboarding** — kickoff call, access exchanged, first milestone dated (see
   `services-delivery-capacity`).
5. **Delivery** — against the stated milestones; log any out-of-scope request the day it
   happens (see Scope-creep control, below).
6. **Invoicing** — on milestone or monthly; see below.
7. **Offboarding** — handover, final payment cleared, referral ask, a short retrospective
   note in `state/decisions_log.md` on what to change for the next engagement.

## Invoicing and UK late-payment rules
- Standard commercial payment terms are **14–30 days** [ASSUMPTION — L — common UK
  freelance practice, 2026]; state the term on every invoice and in the contract, not just
  verbally.
- The **Late Payment of Commercial Debts (Interest) Act 1998** (as amended by the Late
  Payment of Commercial Debts Regulations 2002/2013) gives an automatic B2B right, even
  without a contract clause, to:
  - statutory interest at **8% over the Bank of England base rate** (base rate held at
    **3.75%** on 30 July 2026, giving roughly **11.75%** total — verify the current rate at
    bankofengland.co.uk before calculating), and
  - fixed compensation per unpaid invoice: **£40** (debt under £1,000), **£70** (£1,000 –
    £9,999.99), **£100** (£10,000 or more).
- Money Claim Online (moneyclaim.gov.uk) accepts claims up to **£100,000** from litigants in
  person and is the cheapest way to issue. Allocation is separate: claims up to **£10,000**
  normally go to the small claims track (limited costs recovery, no solicitor needed),
  £10,000–£25,000 to the fast track, £25,000–£100,000 to the intermediate track, above that
  the multi-track. Take a solicitor's advice above the small-claims limit, where adverse
  costs become a real risk. [HMCTS / CPR Part 26 — verify at gov.uk]
- Chase early and in writing: a polite reminder the day payment is overdue, a formal notice
  citing the statutory interest right around day 14, then escalate to Money Claim Online.
  See `services-proposals-contracts-uk` for putting the right to charge interest in the
  contract itself.
- Before court, escalate free to the **Small Business Commissioner**
  (smallbusinesscommissioner.gov.uk), which handles late-payment complaints against larger
  businesses at no cost.
- [Watch, not law yet] The **Small Business Protections Bill** (introduced in the Lords 19
  May 2026) would void payment terms over **60 days** imposed by large businesses on smaller
  suppliers and give the SBC investigation, fining, and binding-arbitration powers — expected
  in force 2027. Do not rely on it for a term signed today; verify status at
  legislation.gov.uk.

## Insurance

| Cover | Protects against | Indicative annual cost (2026) | Note |
|-------|-------------------|--------------------------------|------|
| **Professional indemnity (PI)** | A claim that advice or work caused the client a financial loss | roughly £150–£400 for £250k cover, general freelancer; £300–£900+ for higher-risk advisory work [ASSUMPTION — M — comparison-site ranges] | Many corporate clients require proof before signing, sometimes at a stated minimum (commonly £1m [ASSUMPTION — L — common UK freelance practice, 2026]) |
| **Public liability (PL)** | A claim of physical injury or property damage caused by the founder or the business | roughly £50–£300 for £1–2m cover; desk-based, low-footfall work sits at the lower end [ASSUMPTION — M — comparison-site ranges] | Relevant mainly if the founder visits client sites or hosts clients in person |
| **Employers' liability** | N/A until the first employee | Legally required from the first employee — statutory minimum **£5m** cover, **£2,500/day** penalty for trading uninsured. Status follows the working relationship, not the label: a labour-only subcontractor working under the founder's direction, hours, and equipment generally must be covered. A sole director who owns ≥50% of the share capital and is the only employee is exempt. [Employers' Liability (Compulsory Insurance) Act 1969 / HSE — verify at hse.gov.uk; confirm with the insurer before engaging the first subcontractor] | See `hiring-uk` |

Get 2–3 live quotes (e.g. Hiscox, Simply Business, AXA) before budgeting a figure into
`state/financials.md` — the ranges above can vary several hundred percent by insurer for the
same profession and cover level, so treat them as a starting point, not a quote.

## Scope-creep control
- Every deliverable has a written boundary (see `services-productised-offer`). Anything
  outside it is logged the day it is asked for, against the relevant engagement.
- Three or more out-of-scope requests on one engagement is the trigger to raise a paid
  change order, not to keep absorbing the work quietly [ASSUMPTION — L — heuristic, not
  a benchmark — replace with the founder's own logged data after the first two engagements].
- A change order is short: what is being added, the price, and the revised delivery date —
  sent and agreed before the extra work starts, not after it is already done.

## The operating rhythm
- **Weekly** — pipeline review (enquiries → proposals → signed), invoice status, and a
  capacity check against `services-delivery-capacity`.
- **Per engagement** — the onboarding checklist on start, the offboarding checklist and
  referral ask on close.
- **Monthly** — update `state/financials.md` with revenue, capacity/utilisation, and any
  insurance renewal date; run `weekly-review` for the phase-gate check.
- **Quarterly** — MTD for Income Tax submission if trading as a sole trader with qualifying
  income over **£50,000** (mandatory since 6 April 2026; threshold drops to £30,000 in April
  2027). Digital records are required from the start of the tax year, not retro-fitted — see
  `uk-tax-vat-mtd`.

---
*Reminder: verify late-payment interest rates, insurance costs, and IR35 thresholds against
gov.uk and live insurer quotes before relying on them.*
