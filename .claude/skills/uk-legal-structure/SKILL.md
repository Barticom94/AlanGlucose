---
name: uk-legal-structure
description: Decide and set up the UK business structure. Use when the founder asks about sole trader vs limited company, registering a company, Companies House, business structure, or liability. Triggered around Phase 2. Information, not legal advice.
user-invocable: true
---

# UK Legal Structure

The sole trader vs limited company decision interacts with tax, liability, credibility, and
SEIS eligibility. This is information — a UK chartered accountant makes the call. Detailed
figures: `@docs/UK-LEGAL-TAX.md`.

## Sole trader
- Simplest and cheapest. Register with HMRC for Self Assessment.
- The founder and the business are one legal person — personal liability for debts.
- Profits taxed as income. Fine for early bootstrapping and small-scale testing.

## Limited company (Ltd)
- A separate legal entity — limited liability (subject to any personal guarantees).
- Register at Companies House. The digital incorporation fee rose to £100 from 1 February
  2026 (confirmation statement £50). Verify current fees on gov.uk.
- Profits taxed via Corporation Tax; the founder draws salary and/or dividends.
- **Required for SEIS/EIS** — if there is any equity-raise route, a Ltd is needed.
- Identity verification is now mandatory for new directors and PSCs — verify on gov.uk.

## The decision rule
- Bootstrapping, testing, low liability risk → start as a sole trader; switch later.
- Investor route, real liability exposure, or supplier credibility matters → Ltd.
- Do not register anything until the Phase 1 gate is met. Validation first, structure second.

## When the venture goes Ltd
- Register the company name — check availability first (see `brand-naming`).
- Open a business bank account (Mettle/NatWest enables free FreeAgent — see `bookkeeping-uk`).
- Apply for SEIS advance assurance early if raising (see `uk-funding`); allow 4-6 weeks.
- Get an EORI number if moving goods across the UK border (free at gov.uk/eori).

## Always
End with: "Confirm this with a UK chartered accountant before registering." Structure
mistakes are expensive to unwind later.
