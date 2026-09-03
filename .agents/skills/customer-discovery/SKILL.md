---
name: customer-discovery
description: Prepare, run, and debrief customer interviews using The Mom Test. Use when the founder says "customer interviews", "talk to customers", "interview prep", "I spoke to someone", or is in Phase 1 validation. Produces interview scripts and synthesises results into evidence.
---

# Customer Discovery

Phase 1. Real evidence comes from real conversations. You can prepare the founder and
debrief them — you cannot be the customer. Never substitute synthetic reasoning for an
actual interview.

## The Mom Test — three rules (Fitzpatrick)
1. **Talk about their life, not your idea.** The moment you pitch, the data is contaminated.
2. **Ask about specific past behaviour, not hypotheticals.** "Would you buy this?" is
   worthless; "what did you do last time?" is gold.
3. **Talk less, listen more.** The founder should speak for under a third of the interview.

Avoid: compliments, fluff ("usually", "would", "might"), and pitching the idea instead of
gathering facts.

## Preparing an interview
Write a script to `research/customer-interviews/`. Structure it:
- Warm-up — who they are, their role, their day.
- The problem area — "Tell me about the last time you dealt with X."
- Specifics — what they did, what it cost in money / time / frustration, what they tried.
- Current solutions — what they use now, what they pay, what annoys them about it.
- Commitment asks (the real test) — would they introduce you to a budget-holder, commit
  time, pay a deposit, or join a waitlist with card details?
- Never end on "so, would you use this?"

## Running them
- 10 interviews minimum to clear the Phase 0->1 gate. Strangers — friends and family lie kindly.
- Take verbatim notes; quote the customer's exact words.
- One file per interview in `research/customer-interviews/`.

## Debriefing
After every 3 interviews, run the `red-team-devils-advocate` skill on the results so far.
After 10, spawn the `customer-interview-synthesiser` subagent to extract patterns, buying
signals, and a revised persona.

## What counts as a buying signal
A deposit. A pre-order. A signed letter of intent. A waitlist sign-up with card details. An
introduction to a budget-holder. Time committed. Nothing else — enthusiasm is not a signal.

## Gate to Phase 2
≥ 3 real commitments. If 10 interviews produce zero commitments, the thesis is wrong —
revise or kill it. Do not interview a 20th person hoping for a different answer.
