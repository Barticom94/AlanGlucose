---
name: idea-interrogation
description: Interrogate a captured business idea hard, before any time or money is spent. Use after the business-intake skill has seeded state/business-brief.md, or when the founder says "interrogate this idea", "is this any good", "stress-test the idea", or is in Phase 0. Walks Disciplined Entrepreneurship steps 1-3 and prepares Mom Test customer discovery. The output is a defended thesis or a documented kill.
---

# Idea Interrogation

Phase 0. The goal is not to validate the idea — it is to find out, as cheaply and quickly
as possible, whether it is worth validating at all. Most ideas should die here. That is the
skill working, not failing.

Read `.claude/SYCOPHANCY.md` first. Lead with the hard questions, not encouragement — and
fill what you can: knowledge gaps from research, decision gaps with a recommendation,
evidence gaps with the cheapest test.

## Process

### 1. Start from the intake
The idea is captured first by the `business-intake` skill, which seeds `state/business-brief.md`
and the other state files. Read `state/business-brief.md` before anything else. If it is empty,
stop and run `business-intake` (or `/idea-intake`) — interrogation needs a full picture to
bite on, not a one-line thesis.

### 2. Disciplined Entrepreneurship, steps 1-3 (Aulet, MIT)
- **Step 1 — Market Segmentation.** List 6-12 candidate end markets. Do not choose yet.
- **Step 2 — Beachhead Market.** Choose ONE narrow market to dominate first. Its customers
  buy similar things, talk to each other, and are reachable. "UK consumers" is not a beachhead.
- **Step 3 — End User Profile.** A specific, named profile of the beachhead user.
Write the output to `state/24-steps.md` (create it) and update `state/product_context.md`.

### 3. Run the UK question bank
Put these to the founder directly. Weak answers are findings.
- **Demand:** "Walk me through the last three times you had this problem. What did you
  actually do? What did you spend?"
- **Willingness to pay:** "If I charged £29/month tomorrow, would you give me your card
  details right now? At what price would you?"
- **Channel:** "Where would a customer first hear about this — and is that channel
  reachable within your real month-1 budget (intake section 5.2)?"
- **Competition:** "Who else already does this, and what do these customers use today?"
  Then find the named UK operators yourself — a knowledge gap, yours to fill, not an evidence
  gap. "No differentiation", "thin moat", and "crowded" are claims about the world: a
  competitive verdict with no named, cited competitor — or a cited "searched, found none" —
  is opinion, and opinion cannot carry a position or a kill reason.
- **Moat:** "If I had £500k and 12 months, what would I build to beat you?"
- **Unit economics:** "What is the CAC? The gross margin? At what LTV/CAC does this work?"
- **UK-specific:** "Does this trip GDPR/PECR? Need a VAT-registered supplier? Cross any
  regulator — FCA, MHRA, Ofcom, ICO?" Any marketing list, customer record, or automated
  message makes the venture a data controller: ICO registration and PECR apply however
  mundane the data looks — say so even when nothing is sensitive.
- **Personal:** "Can you keep your day job while running this? What is the smallest test
  that fits the hours you actually have (intake section 5.1)?"

### 4. First-pass frameworks
Fill a Lean Canvas v0 (use the `gtm-positioning` skill). State founder-market fit honestly.

### 5. Premortem
Hand off to the `premortem` skill for an initial failure-mode list.

### 6. Position
Spawn the `devils-advocate` and `evidence-checker` subagents and wait for both — the position
is not final, and is not written to any state file, until both reviews have run.
`evidence-checker` audits every citation made this session: any citation that is not a URL
fetched this session is downgraded to `[ASSUMPTION — unverified]` before the position is
written. Quote each subagent's strongest findings before your position; a review with no
quoted findings did not happen. Then write your position to
`state/project_brief.md`:
**in** (a defended thesis with the beachhead identified); **in, if** (at most three
conditions, each with its fix or its test); or **not in** (a kill memo naming the weak
answer, and what would change your mind). A kill is a good outcome — it cost a week, not a year.

## Gate to Phase 1
The founder commits to interview 10 strangers — not friends, not family — who have the problem.
Hand straight to the `customer-discovery` skill for the interview script and, for a founder
with no contacts, a cold-approach list. Do not end on "go and interview ten strangers" alone.
