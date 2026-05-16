---
name: start
description: First-run onboarding for a new venture brain. Use at the very start of a freshly-cloned AlanGlucose brain, when the founder says "/start", "get started", or "begin", or when CLAUDE.md's first-run check fires because `.claude/.initialised` is absent. Runs first-time setup, briefs the founder, shows the roadmap, and launches the idea intake.
user-invocable: true
---

# Start — first-run onboarding

This runs once, when a venture brain is opened for the first time. `CLAUDE.md`'s first-run
check triggers it automatically when `.claude/.initialised` is absent; it can also be run
manually with `/start`. Work through all five steps in order, then stop.

## Step 1 — Finish setup

Check the environment and report it plainly to the founder:
- `py` (Python 3.x) runs the hooks; `node` / `npx` run the MCP servers; `git` is version control.
- Which API-key environment variables are set: `COMPANIES_HOUSE_API_KEY`, `EXA_API_KEY`,
  `FIRECRAWL_API_KEY`, `GITHUB_PAT`. Missing keys are fine — the brain's core works without
  them; the matching MCP server simply stays offline until the key is set.

Then put the two optional decisions to the founder, one at a time, with the impact of each:
- **Global config.** "Shall I apply the anti-sycophancy defaults to *every* Claude Code
  project on this machine? Impact: it copies `GLOBAL-CLAUDE.md.example` to `~/.claude/CLAUDE.md`
  and every Claude session everywhere gets blunter — not only this brain. Skip it and this
  brain still enforces anti-sycophancy on its own."
- **MCP keys.** "Which of the four API keys do you have to hand? I'll note the rest as
  pending so the brain knows which MCP servers are live."

Record the decisions in `CLAUDE.local.md` and `state/tech_context.md`.

## Step 2 — Brief the founder

Give this summary, in plain prose and in your own words:
- **What AlanGlucose is** — a structured workspace that takes a business idea from "what if"
  to "this works", or to a fast and cheap "no", by interrogating it hard, validating it with
  real evidence, and only then helping build it. It is deliberately anti-sycophantic: its job
  is to find the flaw before the founder spends money on it.
- **How to use it well** — one venture per brain; sessions of about two hours; commit
  `state/` to git after every real decision; when the brain pushes back, push back with
  *evidence*, not conviction; run `/reality-check` before any spend and `/weekly-review`
  weekly; let the phase gates hold — they are the point.

## Step 3 — Show the roadmap

Present the journey from idea to success — no dates, just the sequence and what each phase
proves:

- **Phase 0 — Idea** — interrogate the idea before spending anything. *Gate:* 10 interviews
  with strangers who have the problem.
- **Phase 1 — Validation** — prove strangers will commit something real. *Gate:* 3 real
  commitments (a deposit, a letter of intent, or a paid waitlist).
- **Phase 2 — MVP** — ship the smallest real thing people pay for. *Gate:* 10 paying
  customers and 7-day retention.
- **Phase 3 — Traction** — find one acquisition channel that pays back. *Gate:* CAC < LTV/3
  and gross margin above 40%.
- **Phase 4 — Growth** — deepen the channel and remove the founder's bottlenecks. *Gate:*
  profitable, or cleanly positioned to raise.
- **Phase 5 — Success** — scale, raise, or bootstrap to profit. The destination.

State which phase the brain is in (Phase 0) and name the immediate gate.

## Step 4 — Start the work

Hand straight off to the `business-intake` skill: present the intake framework and begin the
intake. Do not wait to be asked.

## Step 5 — Mark the brain initialised

Once the founder is into the intake, create the file `.claude/.initialised` (the date plus a
one-line note as its content). This stops the onboarding auto-running every session. `/start`
can still be run manually any time the founder wants the summary or roadmap again.
