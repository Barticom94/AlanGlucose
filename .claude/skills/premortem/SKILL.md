---
name: premortem
description: Run a structured premortem before any phase gate, major decision, or spend over £200. Use when the founder says "premortem", "/premortem", "what could go wrong", or "before I commit". Imagines the venture has already failed and works backwards to the causes.
user-invocable: true
---

# Premortem

A premortem (Klein, HBR 2007) imagines failure has already happened. Prospective hindsight —
treating a future event as a past fact — measurably improves the ability to identify the
causes of an outcome (Mitchell, Russo & Pennington, 1989: roughly a 30% improvement). It is
the cheapest risk tool the brain has. For facilitation in a clean context, spawn the
`premortem-facilitator` subagent.

## Process

### 1. Frame
"It is 12 months from now. This venture has failed badly — shut down, or clearly going
nowhere. We are not asking IF it failed. It failed. Now: why?"

### 2. Generate — independently, before any discussion
List failure causes exhaustively. Push for at least 10. No defending the idea yet. Prompt
across themes:
- Demand — no one actually wanted it.
- Channel — could not reach customers affordably.
- Unit economics — every sale lost money.
- Execution — too slow; five hours a week was not enough.
- Competition — an incumbent crushed it, or it already existed.
- Regulation — a UK rule made it unviable.
- Founder — capacity, motivation, or the day-job conflict.

### 3. Rank
For each cause, rate likelihood (H/M/L) and impact (H/M/L). Identify the top 5.

### 4. Test
For each of the top 5, design the single cheapest test that would falsify the assumption
behind it. A premortem with no resulting tests is theatre.

### 5. Record
Write to `state/risks.md` under `### [YYYY-MM-DD] Premortem: <topic>`. Update the open-risks
table. Carry the most dangerous assumption into the current task as the next thing to test.

## When to run it
Every phase gate. Before every spend over £200. Before any irreversible decision —
registering a company, signing a supplier contract, or quitting the Moda in Pelle job.
