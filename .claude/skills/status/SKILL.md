---
name: status
description: One-screen read of where the venture is, taken from the state files with no evaluation. Use when the founder says "status", "/status", "where are we", "where were we", "catch me up", "what's the situation", or opens a session in an initialised brain with a greeting and nothing else.
---

# Status — one screen, from the files

**Moment:** the founder asks where things stand, or opens a session with a greeting and
nothing else. **Output:** the screen below, printed in the reply, then one closing sentence.

## Read
`state/active_context.md`; `state/progress.md`; `state/decisions_log.md` (the top entry);
`state/financials.md`; `state/risks.md` (the count of rows whose status is `open`);
`docs/LEARNED.md` (the count of rows whose last column is not `shared`); the dated
interview files in `research/customer-interviews/`; `state/business-brief.md` section 5;
and `state/predictions.md`, if present.

## Print
In this order, at most fifteen lines, and nothing else:
1. Venture and founder — from `AGENTS.md` WHAT.
2. Phase and gate with the count — from `state/active_context.md`; and the Spine "Now"
   line, if that section is present.
3. Days since the last recorded interview (the newest `<YYYY-MM-DD>-*.md` in
   `research/customer-interviews/`) and since the last review (the newest dated line
   naming a weekly review in `state/active_context.md` or `state/decisions_log.md`).
4. Open conditions — one line each, if that section is present in the state files; when
   they would push the screen past fifteen lines, the last of them reads "and N more".
5. Open risks count — from `state/risks.md`.
6. Money spent against the budget — spent from `state/financials.md`, budget from
   `state/business-brief.md` section 5.
7. Predictions past their resolve-by date — from `state/predictions.md`, if present; one
   line with the count and their titles.
8. The last decision — title and date of the top entry in `state/decisions_log.md`.
9. Unshared learnings count — from `docs/LEARNED.md`.
10. The next concrete step — verbatim from `state/active_context.md`.

## Rules
- Every line comes from a file; a field the files do not hold prints "not recorded".
- Dates are computed from today's date and the dates written in the files; a file with no
  date prints "not recorded" for that half of the line.
- The screen carries no evaluation, no advice, and no praise — those belong to
  `weekly-review` and the partner frame.
- The last line is always the next step.

## Close
After the screen, one sentence: "Say 'weekly review' for the full picture, or carry on."
