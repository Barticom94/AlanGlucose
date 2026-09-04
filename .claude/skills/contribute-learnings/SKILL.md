---
name: contribute-learnings
description: Send the general research facts this brain has looked up (docs/LEARNED.md) back to the AlanGlucose template, so every venture's knowledge base improves. Use when the founder says "share learnings", "contribute", "send the research back", or when session-handoff finds unshared rows in docs/LEARNED.md. Shares ONLY the research the brain did — never anything the founder typed, and never anything about their venture, customers, or competitors.
---

# Contribute learnings

**What is shared, exactly:** rows of `docs/LEARNED.md` — a general fact (a UK rule, a fee,
a benchmark, how a mechanism works) with its source, date, and confidence.

**What is never shared:** anything from `state/`, `research/`, `financials/`, `marketing/`,
or `legal/`; anything the founder typed; the venture's name; the founder's name or region;
customers, competitors, or any figure the founder set (their price, their costs, their
forecasts). If a row could identify the venture, it does not go.

## Process

1. **Consent, once.** If `CLAUDE.local.md` has no `share-learnings:` line, ask, in plain
   words: "When I look things up — tax rules, fees, benchmarks — may I send those facts back
   to the AlanGlucose template so other founders' brains know them too? Only the research I
   did. Nothing you tell me, and nothing about your business, ever leaves this folder.
   Yes / no / ask me each time." Record the answer as `share-learnings: yes|no|ask` in
   `CLAUDE.local.md`. If **no**: stop, and never ask again unless the founder raises it.
2. **Collect.** Rows in `docs/LEARNED.md` whose last column is not `shared`.
3. **Scrub.** Drop any row that mentions the venture or founder by name or region, says
   "our customer(s)" or "interview", names a competitor from `research/`, or contains a
   figure the founder set. When unsure, drop it — a missing fact costs nothing; a leaked one
   costs trust. Then show the founder the exact rows that will be sent, in full.
4. **Confirm.** If consent is `ask`, wait for a yes. If `yes`, proceed after showing the rows.
5. **Send**, by the first route that works:
   - `gh auth status` succeeds → `gh issue create --repo Barticom94/AlanGlucose
     --label learnings --title "Learnings: <YYYY-MM-DD> (<n> facts)" --body-file <tmp>`
     where the body is the rows in the learnings issue-template table.
   - Otherwise → build `https://github.com/Barticom94/AlanGlucose/issues/new?template=learnings.md&title=<title>&body=<url-encoded rows>`
     and give it to the founder: "open this link, sign in to GitHub if it asks, and press
     Submit". Keep the body under ~6,000 characters; batch if longer.
   - Otherwise (no GitHub account) → write the rows to `docs/learnings-to-share-<date>.md`
     and say it can be emailed to the maintainer whenever convenient.
6. **Mark** each sent row `shared` in its last column. One line to the founder: how many
   facts went, and where.

## Never
- Never send without showing the rows first. Never include file paths, names, or anything
  from `state/` or `research/`. Never send more than the scrubbed rows. Never nag: offer at
  most once per session, at the handoff.
