---
name: idea-interrogation
description: Interrogate a captured business idea hard, before any time or money is spent. Use after the business-intake skill has seeded state/business-brief.md, or when the founder says "interrogate this idea", "is this any good", "stress-test the idea", or is in Phase 0. Walks Disciplined Entrepreneurship steps 1-3 and prepares Mom Test customer discovery. The output is a defended thesis or a documented kill.
user-invocable: true
---

# Idea Interrogation

Phase 0. The goal is not to validate the idea — it is to find out, as cheaply and quickly
as possible, whether it is worth validating at all. Most ideas should die here. That is the
skill working, not failing.

Read `.claude/SYCOPHANCY.md` first. Lead with the hard questions, not encouragement.

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
  reachable on £0 marketing in month 1?"
- **Moat:** "If I had £500k and 12 months, what would I build to beat you?"
- **Unit economics:** "What is the CAC? The gross margin? At what LTV/CAC does this work?"
- **UK-specific:** "Does this trip GDPR/PECR? Need a VAT-registered supplier? Cross any
  regulator — FCA, MHRA, Ofcom, ICO?"
- **Personal:** "Can you keep your day job while running this? What is the smallest test
  that fits five hours a week?"

### 4. First-pass frameworks
Fill a Lean Canvas v0 (use the `gtm-positioning` skill). State founder-market fit honestly.

### 5. Premortem
Hand off to the `premortem` skill for an initial failure-mode list.

### 6. Verdict
Spawn the `devils-advocate` subagent. Then write a verdict to `state/project_brief.md`:
either a defended thesis with the beachhead identified, or a **kill memo** naming the weak
answer that killed it. A kill is a good outcome — it cost a week, not a year.

## Gate to Phase 1
The founder commits to interview 10 strangers — not friends, not family — who have the problem.
