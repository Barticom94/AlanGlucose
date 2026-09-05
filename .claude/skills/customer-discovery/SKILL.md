---
name: customer-discovery
description: Prepare, run, record, and debrief customer interviews using The Mom Test, and source the strangers to interview. Use when the founder says "customer interviews", "talk to customers", "interview prep", "I spoke to someone", "who should I talk to", "where do I find people", or is working toward the Phase 0 → 1 gate (ten strangers who have the problem) or the Phase 1 → 2 gate (three real commitments). Produces the sourcing plan, one file per interview, and synthesised evidence.
---

# Customer Discovery

This skill's ground is two gates. **Phase 0 → 1:** ten interviews with strangers who have
the problem. **Phase 1 → 2:** three real commitments — a deposit, a letter of intent, a paid
pre-order, or a waitlist sign-up with card details. Read the current phase and the gate
count from `state/active_context.md` at the start of every task under this skill and work
the gate that is open. Real evidence comes from real conversations: you prepare the founder
and debrief them; the founder holds the conversation, and every fact on file about an
interviewee or a source is the founder's typed words.

## The Mom Test — three rules (Fitzpatrick)
1. **Talk about their life, not your idea.** The moment you pitch, the data is contaminated.
2. **Ask about specific past behaviour, not hypotheticals.** "Would you buy this?" is
   worthless; "what did you do last time?" is gold.
3. **Talk less, listen more.** The founder should speak for under a third of the interview.

Avoid: compliments, fluff ("usually", "would", "might"), and pitching the idea instead of
gathering facts.

## Preparing an interview
Write a script to `research/customer-interviews/SCRIPT-<YYYY-MM-DD>.md`. Structure it:
- Warm-up — who they are, their role, their day.
- The problem area — "Tell me about the last time you dealt with X."
- Specifics — what they did, what it cost in money / time / frustration, what they tried.
- Current solutions — what they use now, what they pay, what annoys them about it.
- Commitment asks (the real test) — would they introduce you to a budget-holder, commit
  time, pay a deposit, or join a waitlist with card details?
- Never end on "so, would you use this?"

## Sourcing the strangers
**Moment:** at the first debrief, at the position, or whenever the founder asks who to talk
to or where to find people. **Output:** `research/customer-interviews/SOURCING.md`, copied
from `research/customer-interviews/SOURCING-TEMPLATE.md` and filled with:
- The segment, in the founder's words.
- Three to five named sources — a group, a venue, a counter, a forum, or a referrer who is
  not the interviewee. Each line either quotes the founder's own words with "(founder)"
  after it, or carries `[ASSUMPTION — unverified]` and the one-visit test that settles it:
  one visit, message, or post by the founder, and the result that confirms the source.
- How many strangers each source could yield — tagged the same way, line by line.
- The calendar slots, taken only from the hours the founder typed in
  `state/business-brief.md` section 5. Re-read section 5 against every slot before the file
  is written; a slot outside those hours is a defect, corrected before the file is saved.
  Where section 5 holds no hours, the slots read "not recorded" and the reply ends with one
  question: which hours.
- The one-sentence ask — what the founder says to get a twenty-minute conversation, with no
  pitch in it.
- The calendar date the ten are done by.

Every later "who next and when" answer names the next open slot in that file with its
calendar date. When the founder's hours change, rewrite the slots in the same session.

## Running them
- 10 interviews minimum to clear the Phase 0->1 gate. Strangers — friends and family lie kindly.
- Take verbatim notes; quote the customer's exact words.
- One file per interview in `research/customer-interviews/` — see "Recording an interview".

## Recording an interview
**Moment:** at every debrief, after step 1 of "Debriefing" and before its step 6.
**Output:** one file per interview at
`research/customer-interviews/<YYYY-MM-DD>-<first-name-or-role>.md`, copied from
`research/customer-interviews/INTERVIEW-TEMPLATE.md` and filled only from the founder's
words. Every field the founder did not give reads "not recorded". Quotation marks in the
file hold the founder's transcription of the interviewee, marked "(founder's
transcription)" after each; anything you restate is written without quotation marks. The
date is the interview date the founder gave; where they gave none, the debrief date, marked
"(debrief date)".

## Debriefing
**Moment:** every time the founder reports a conversation. Steps, in this order:
1. **Classify** each interview on three facts, each from the founder's words: *stranger*
   (how they were found; friend, family, colleague, and existing customer are not
   strangers); *has the problem* (the last time it happened, in the interviewee's words);
   *a real conversation* (twenty minutes or more, notes taken). Ask one question per
   missing fact before anything else.
2. **Recount.** Read the "Counts toward the gate?" line of every
   `research/customer-interviews/<YYYY-MM-DD>-<first-name-or-role>.md` file, add this
   debrief's classifications, and count the interviews that pass all three. Write it as
   "N of 10 confirmed, M pending <the missing fact>".
3. **Facts against opinions.** What they did, paid, and felt, set against what they said
   they would do and the compliments.
4. **Update the gate count** in `state/active_context.md` and `state/progress.md` (and the
   Spine line there, if present).
5. After every third confirmed interview, run `red-team-devils-advocate` on the results so
   far. After the tenth, spawn the `customer-interview-synthesiser` subagent to extract
   patterns, buying signals, and a revised persona.
6. **Close** with the next open slot from `research/customer-interviews/SOURCING.md` and
   its calendar date. At the first debrief, write that file first (see "Sourcing the
   strangers"), then close from it.

## What counts as a buying signal
A deposit. A pre-order. A signed letter of intent. A waitlist sign-up with card details. An
introduction to a budget-holder. Time committed. Nothing else — enthusiasm is not a signal.

## Gate to Phase 2
≥ 3 real commitments. If 10 interviews produce zero commitments, the thesis is wrong —
revise or kill it. Do not interview a 20th person hoping for a different answer.
