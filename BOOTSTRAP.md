# BOOTSTRAP.md — the operating manual

Read this once, carefully, before you run a venture through the brain. Refer back at every
phase transition.

AlanGlucose is always in exactly one phase. The current phase lives at the top of
`state/active_context.md` and in `AGENTS.md`, and the brain refuses work that belongs to a
later phase. Progression is one-way and earned: each phase has a gate — a few hard,
falsifiable criteria, not a feeling.

## Day one — starting a new venture

1. Download the template ZIP (link in `README.md`), unzip it, rename the folder to your
   venture, and open it in the Claude Code app as a new session. Say yes to trusting the
   folder, choose Yes when the app asks permission for small actions, and say hello.
2. The `start` skill runs on its own: a quiet setup, a short briefing, the roadmap, then the
   intake — one question at a time. Answer honestly; "I don't know" is a real answer.
3. From your answers the brain writes `state/business-brief.md`, seeds every other `state/`
   file, installs the vertical pack(s) that fit your kind of business, and hands over to
   `idea-interrogation`.
4. Run `/premortem` and `/red-team-devils-advocate` (or just say "reality check") before
   the end of week one.
5. If git was set up, commit after every meaningful conversation — a versioned record of the
   brain's thinking. If not, back the folder up now and then.

If a question is hard, that is the question that mattered most.

## The phase model

### Phase 0 — Idea (week 1)
Find out whether the idea survives serious scrutiny before any time or money goes in. No
spending, no company registration, no domain purchase. You run the intake, the interrogation,
a premortem, and a red-team.
**Gate 0 → 1:** 10 interviews completed with strangers (not friends, not family) who have the
problem. Deliverables alongside the gate: a defended founder-market-fit statement and a named
beachhead persona. If you have no acknowledged risks, you have not interrogated hard enough.

### Phase 1 — Validation (weeks 2–4)
Find out whether real strangers want this badly enough to commit something tangible. You run
Mom Test interviews and deploy a cheap smoke test.
**Gate 1 → 2:** at least 3 real commitments — a deposit, a signed letter of intent, a paid
pre-order, or a waitlist sign-up with card details. Verbal enthusiasm is data, not evidence.

### Phase 2 — MVP (weeks 4–12)
Deliver the minimum viable version to ten real paying customers, and read what their
behaviour tells you. You build the offering, set up payments, register a legal entity if
going the Ltd route, and wire in the tools you actually need. The vertical pack's skills
come into play here.
**Gate 2 → 3:** 10 paying customers and 7-day post-purchase retention data.

### Phase 3 — Traction (months 3–9)
Find one repeatable acquisition channel where CAC is meaningfully below LTV. You run marketing
experiments, track real metrics, and set up proper bookkeeping.
**Gate 3 → 4:** CAC < LTV/3 in one repeatable channel, and gross margin above 40%.

### Phase 4 — Growth (months 9–18)
Deepen the channel that works, hire to remove your own bottlenecks, and either reach EBITDA
positivity or position cleanly for investment. You write SOPs for the recurring work.
**Gate 4 → 5:** EBITDA-positive, or a credible, evidenced path to raising — a strategic
choice, not just a metric.

### Phase 5 — Scale (month 18+)
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

## Files the brain maintains automatically (only if the optional helpers are on)
- `state/handover-latest.md` — rewritten before every context compaction.
- `state/session-log.md` — appended at the end of every session.
- `.claude/backups/` — raw transcripts saved before compaction; the last 10 are kept.

Without the helpers, context still survives: `CLAUDE.md` reloads `AGENTS.md` and the two
live state files after every compaction.

## Files you maintain (with the brain's help)
- `state/business-brief.md` — the full intake record; written once via `business-intake`.
- `state/project_brief.md` — the distilled thesis; rarely changed after Phase 0.
- `state/active_context.md` — updated whenever you change what you are working on.
- `state/decisions_log.md` — append-only; never edit past entries.
- `state/risks.md` — updated whenever a premortem or red-team runs.

Write all of these as if a stranger will pick them up cold — because a future you, or a
future instance of the brain, will.
