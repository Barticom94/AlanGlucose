# BOOTSTRAP.md — read this before you start

The operating manual for AlanGlucose. Read it once, carefully, before you run a venture
through the brain. Refer back at every phase transition.

AlanGlucose is always in exactly one phase. The current phase lives at the top of
`state/active_context.md`, and the brain refuses work that belongs to a later phase.
Progression is one-way and earned: each phase has a gate — a few hard, falsifiable criteria,
not a feeling.

## Day one — starting a new venture

1. Clone or copy the template into a new folder named for the venture.
2. Open it in Claude Code. Let the brain read `CLAUDE.md` and `state/active_context.md`.
3. Run `/idea-intake`. The `business-intake` skill hands you a structured framework — fill it
   in honestly, paste it back. The brain probes the gaps, then seeds every `state/` file.
4. The brain hands off to `idea-interrogation`, then `/premortem` and `/reality-check` before
   the end of week one.
5. Commit `state/` to git after every meaningful conversation — a versioned record of the
   brain's thinking.

Answer everything honestly. If a question is hard, that is the question that mattered most.

## The phase model

### Phase 0 — Idea interrogation (week 1)
Find out whether the idea survives serious scrutiny before any time or money goes in. No
spending, no company registration, no domain purchase. You run the intake, the interrogation,
a premortem, and a red-team.
**Gate 0 → 1:** 10 interviews completed with strangers — not friends, not family — who have
the problem; a defended founder-market-fit statement and a named beachhead persona. If you
have no acknowledged risks, you have not interrogated hard enough.

### Phase 1 — Validation (weeks 2–4)
Find out whether real strangers want this badly enough to commit something tangible. You run
Mom Test interviews and deploy a cheap smoke-test landing page.
**Gate 1 → 2:** at least 3 real commitments — a deposit, a signed letter of intent, a paid
pre-order, or a card-verified waitlist. Verbal enthusiasm is data, not evidence.

### Phase 2 — MVP (weeks 4–12)
Deliver the minimum viable business product to ten real paying customers, and read what their
behaviour tells you. You build the offering, set up payments, register a legal entity if
going the Ltd route, and wire in the tools you actually need.
**Gate 2 → 3:** 10 paying customers and 7-day post-purchase retention data.

### Phase 3 — Early traction (months 3–9)
Find one repeatable acquisition channel where CAC is meaningfully below LTV. You run marketing
experiments, track real metrics, and set up proper bookkeeping.
**Gate 3 → 4:** CAC < LTV/3 in at least one channel, and gross margin above 40%.

### Phase 4 — Growth (months 9–18)
Deepen the channel that works, hire to remove your own bottlenecks, and either reach EBITDA
positivity or position cleanly for investment. You write SOPs for the recurring work.
**Gate 4 → 5:** a strategic choice, not a metric — EBITDA-positive and choosing whether to
keep bootstrapping, or hitting the limits of bootstrapping and choosing to raise.

### Phase 5 — Scale or fundraise (month 18+)
Whichever path you chose. If raising: SEIS advance assurance, pitch deck, cap table, data
room. If bootstrapping: the brain shifts from strategist to operations.

## When you disagree with the brain

Push back with evidence, not emotion. Find the specific assumption the brain has wrong and
present what contradicts it. If you cannot name the assumption, your conviction is probably
emotional — pause before overriding.

When you genuinely have the evidence, or have simply decided to accept a risk, say so
explicitly: *"I've decided to proceed despite this risk."* The brain will respect that,
record the disagreement in `state/decisions_log.md`, and help you execute — but it keeps the
phase gates intact. An override is not a free pass past the next gate.

## Files the brain maintains automatically
- `state/handover-latest.md` — rewritten by the PreCompact hook before every compaction.
- `state/session-log.md` — appended by the Stop hook at the end of every session.
- `.claude/backups/` — raw transcripts saved by the PreCompact hook; it keeps the last 10.

## Files you maintain (with the brain's help)
- `state/business-brief.md` — the full intake record; written once via `business-intake`.
- `state/project_brief.md` — the distilled thesis; rarely changed after Phase 0.
- `state/active_context.md` — updated whenever you change what you are working on.
- `state/decisions_log.md` — append-only; never edit past entries.
- `state/risks.md` — updated whenever a premortem or red-team runs.

Write all of these as if a stranger will pick them up cold — because a future you, or a
future instance of the brain, will.
