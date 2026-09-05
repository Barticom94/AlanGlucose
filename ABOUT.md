# About AlanGlucose

## What it is
AlanGlucose is a venture "brain" — a structured AI workspace that helps a single founder
interrogate, validate, and build a business idea, one phase at a time. It is not a chatbot
wrapper or a notes folder. It is an opinionated process for taking an idea from "what if"
to "this works" — or, just as valuably, to a fast and cheap "no".

## The name
The brain's core is an interrogation pipeline modelled on a hard-nosed investor — the kind
who asks the uncomfortable question before you have spent the money. The source
specification calls it the "Alan Sugar interrogation pipeline". Glucose is sugar. So:
**AlanGlucose** — Alan Sugar, distilled. The name is a joke; the interrogation is not.

## Why it exists
Most business ideas fail for reasons that were knowable early — no real demand, a channel
that cannot be reached affordably, unit economics that never worked. They fail late and
expensively because nobody asked the hard questions, or because the people asked were too
kind to answer honestly.

AI is, by default, too kind. It is trained to be agreeable. AlanGlucose is built to
counteract that, deliberately:

- **Anti-sycophancy is a file, not a hope.** `AGENTS.md` and `.claude/SYCOPHANCY.md` are a
  contract: lead with the critique, three failure modes before any approval, no reversal
  without new evidence.
- **Evidence over opinion.** Every claim is cited or tagged as an assumption. A dedicated
  skill, `evidence-bar`, defines exactly what proof each kind of claim requires.
- **Phase gates.** You cannot build before you validate. The brain refuses later-phase work
  until the current gate is met — on evidence, not on a feeling of being ready.
- **Builder / reviewer subagents.** One model builds; a separate one, in a clean context,
  tries to break it — never having seen the optimism that produced the work.

## How it is built
- **`AGENTS.md`** — the behavioural contract, read by every harness; `CLAUDE.md` imports it.
- **`state/`** — a memory bank of plain markdown, updated at every task boundary, so the
  thread survives long sessions and compaction.
- **`.claude/skills/`** — 29 core, vertical-neutral skills, from idea interrogation to UK tax.
- **`packs/`** — four vertical packs (ecommerce, saas, services, physical), installed by the
  intake so no kind of business is privileged.
- **`.claude/agents/`** — 14 subagents, used in builder→reviewer pairs.
- **`.claude/settings.json`** — the deny rules that block destructive commands; four optional
  Python helpers in `.claude/hooks/` are switched on per machine.
- **`docs/`** — UK-specific legal, tax, funding, and brand reference material.

## The phases
`0 Idea → 1 Validation → 2 MVP → 3 Traction → 4 Growth → 5 Scale`

Each phase has named deliverables and one hard gate. Phase 0 is a single week spent asking
whether the idea has earned a Phase 1 at all.

## Who it is for
A single, first-time founder in the UK, usually running the venture alongside other
commitments on limited hours and a small starting budget — any kind of business. The tax,
legal, funding, and operations knowledge throughout is UK-specific.

## Getting started
Download the ZIP, unzip it, rename the folder, open it in the Claude Code app, and say hello
— see `README.md`. The `start` skill onboards you from there: a quiet setup, a briefing, the
roadmap, then the idea intake one question at a time.

One folder per venture. Built to the "Claude Brain" specification.
