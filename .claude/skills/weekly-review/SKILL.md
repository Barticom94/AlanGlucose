---
name: weekly-review
description: Run the weekly venture review and phase-gate checks. Use when the founder says "weekly review", "/weekly-review", "/phase-gate", "are we on track", "phase gate", or it is the weekly review day. Checks progress against the gate and gives an honest on-track call.
user-invocable: true
---

# Weekly Review & Phase Gates

A weekly rhythm that catches a stalling venture early. For the review itself, spawn the
`weekly-reviewer` subagent. Be honest, brief, and forward-looking — activity is not progress.

## The weekly review
Read `state/active_context.md`, `progress.md`, `decisions_log.md`, and `risks.md`. Then:
1. What moved this week — concrete outcomes, not activity.
2. What stalled, and the real reason.
3. Progress against the current phase gate, quantified.
4. Has any risk in `risks.md` materialised or grown?
5. Founder-capacity check — did the ~5 hours go to the highest-leverage thing?
6. Set the single most important objective for next week.
Update `state/progress.md` and `state/active_context.md`. If the venture has not moved
toward its gate in 3 weeks, say so directly and ask why.

## Phase gates — the hard questions
Run the gate check before advancing a phase. Run `premortem` and the `devils-advocate`
subagent first.
- **0 → 1:** Have you interviewed 10 strangers — not friends, not family — who have the problem?
- **1 → 2:** Have ≥ 3 people pre-paid, pre-ordered, or signed a letter of intent?
- **2 → 3:** Do you have 10 paying customers and real 7-day retention data?
- **3 → 4:** Is CAC < LTV/3 in a repeatable channel, and gross margin > 40%?
- **4 → 5:** Is the business profitable, or is there a credible path to SEIS-eligible scale?

## The gate rule
A gate is passed on evidence, not on feeling ready. If the evidence is not there, the phase
is not done — name the missing evidence and the cheapest way to get it. Record the gate
decision in `state/decisions_log.md`.
