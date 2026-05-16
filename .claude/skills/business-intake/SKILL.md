---
name: business-intake
description: Capture a new business idea in full and seed the brain with it. Use at the very start of a new venture, or when the founder says "new idea", "new venture", "I've got an idea", "/idea-intake", "let's start", or "evaluate this idea". Presents a structured intake framework, probes the gaps, then seeds every state file. Runs before idea-interrogation.
user-invocable: true
---

# Business Intake

The first thing a new venture runs. Its job is to transfer the founder's complete picture of
the idea into the brain — so every later skill, subagent, and state file starts from a full,
shared understanding rather than a one-line thesis.

Intake captures; `idea-interrogation` attacks. Do this first, then hand off.

## Important framing
Everything the founder writes here is their **belief**, not established fact. Seed it all as
`[ASSUMPTION]`. The intake produces a complete first-draft picture of the venture and a clear
sense of what it depends on — it does not produce a *proven* plan. Phase 1 turns the
assumptions into evidence. Tell the founder this, so the intake is not mistaken for validation.

## Process

### 1. Present the framework
Give the founder the intake framework in `references/intake-framework.md` — 7 sections plus a
capstone question. Tell them: fill it as fully and honestly as they can, at their own pace,
even offline; "I don't know" is a valid answer; this is a diagnosis, not a pitch. They paste
it back when done.

### 2. Gap-probe pass
When the framework comes back, read all of it, then probe — but **only** the gaps and the
vague answers. Do not re-ask what is already answered well. Apply the `evidence-bar` mindset:
- "Lots of people want this" → who, specifically, and how do you know?
- A number with no basis → tag it, and ask what it is anchored to.
- A blank or "not sure" → ask one focused follow-up to draw it out, or record it as an open
  unknown if the founder genuinely cannot answer it yet.
Keep the probe light — a handful of targeted questions, not a second questionnaire.

### 3. Seed the brain
Write the completed, probed intake to `state/business-brief.md` — the durable raw record.
Then propagate it:
- `state/project_brief.md` — the distilled thesis, founder-market fit, success definition, kill criteria.
- `state/product_context.md` — the problem, the job-to-be-done, the beachhead persona, the alternatives, why now.
- `state/financials.md` — every number the founder gave, each tagged `[ASSUMPTION — H/M/L]`.
- `state/risks.md` — section 5's worry and the capstone (the riskiest assumption) become the opening risk register.
- `state/system_patterns.md` — section 7's working preferences (cadence, challenge level, decision style).
- `CLAUDE.md` — fill the `{{PLACEHOLDERS}}`: venture name, one-line description, current phase (0), gate criteria.

### 4. Hand off
Confirm the seeded picture with the founder, then hand to the `idea-interrogation` skill —
which now has a full picture to interrogate. Set the focus to the Phase 0 → 1 gate: 10
interviews with strangers.

## Quality bar
The intake is done when someone who has never heard the idea could read
`state/business-brief.md` and explain the venture, the customer, the model, and the single
biggest risk. If they could not, keep probing.
