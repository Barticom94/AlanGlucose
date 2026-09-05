---
name: weekly-review
description: Run the weekly venture review and phase-gate checks. Use when the founder says "weekly review", "/weekly-review", "/phase-gate", "are we on track", "phase gate", or it is the weekly review day. Checks progress against the gate and gives an honest on-track call.
---

# Weekly Review & Phase Gates

A weekly rhythm that catches a stalling venture early. For the review itself, spawn the
`weekly-reviewer` subagent. Be honest, brief, and forward-looking — activity is not progress.

## The weekly review
Read `state/active_context.md`, `progress.md`, `predictions.md`, `decisions_log.md`, and
`risks.md`. Then, in this order:
1. **Spine first.** State the phase's one number from the Spine in `state/progress.md`, with
   its source and date, against the last review's. If it is unchanged, the review's first
   sentence is "Nothing moved: <number> has not changed in N weeks."
2. **Resolve predictions.** For every row in `state/predictions.md` past its resolve-by
   date, ask the founder for the actual — one row per question — and write actual, hit/miss,
   and lesson into the row. State the brain's running hit rate in one line: "my last N
   predictions: k right."
3. **Open conditions.** Read each condition in `state/active_context.md` back with its
   status. One due before a gate that is being checked in this review is a blocker; name it
   as such.
4. What moved this week — concrete outcomes, not activity.
5. What stalled, and the real reason.
6. Has any risk in `risks.md` materialised or grown?
7. Founder-capacity check — did the founder's available hours go to the highest-leverage thing?
8. Next week's single objective, written as a prediction row — a number and a date — to
   `state/predictions.md`.
Then update `state/progress.md` (Spine: move Now to Last review, write the new Now) and
`state/active_context.md`. If the venture has not moved toward its gate in 3 weeks, say so
directly and ask why.

## Phase gates — the hard questions
Run the gate check before advancing a phase. Run `premortem` and the `devils-advocate`
subagent first. Then read Open conditions: any condition in `state/active_context.md` due
before this gate that is still open is named; the gate does not pass until it is met or the
founder logs the decision to proceed without it in `state/decisions_log.md`.
- **0 → 1:** Have you interviewed 10 strangers — not friends, not family — who have the problem?
- **1 → 2:** Have ≥ 3 people pre-paid, pre-ordered, or signed a letter of intent?
- **2 → 3:** Do you have 10 paying customers and real 7-day retention data?
- **3 → 4:** Is CAC < LTV/3 in a repeatable channel, and gross margin > 40%?
- **4 → 5:** Is the business profitable, or is there a credible path to SEIS-eligible scale?

## Gates run both ways
The demotion triggers are the ones in `AGENTS.md`: commitments withdrawn; retention below the
2 → 3 bar; the channel's CAC above LTV/3 for eight weeks; EBITDA negative for a quarter. Check
them at every review, after step 7; when one is true, name it and move the phase back. On
demotion or advance, update the Phase and Gate lines in the WHY section of `AGENTS.md`,
`state/active_context.md` (phase, gate), and `state/progress.md` (status, Spine), and append
an entry titled "Phase N → M" to `state/decisions_log.md`.

## The gate rule
A gate is passed on evidence, not on feeling ready. If the evidence is not there, the phase
is not done — name the missing evidence and the cheapest way to get it. Record the gate
decision in `state/decisions_log.md`.
