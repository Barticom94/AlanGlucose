---
name: business-intake
description: Capture a new business idea in full and seed the brain with it. Use at the very start of a new venture (the start skill hands over to it), or when the founder says "new idea", "new venture", "I've got an idea", "/idea-intake", "let's start", or "evaluate this idea". Asks the intake questions one at a time by default, probes the gaps, installs the vertical pack(s) that fit, then seeds every state file. Runs before idea-interrogation.
---

# Business Intake

The first thing a new venture runs. Its job is to transfer the founder's complete picture of
the idea into the brain — so every later skill, subagent, and state file starts from a full,
shared understanding rather than a one-line thesis.

Intake captures; `idea-interrogation` attacks. Do this first, then hand off.

## Framing — say this once, early
Everything the founder says here is their **belief**, not established fact. It is all seeded
as `[ASSUMPTION]`. The intake produces a first-draft picture of the venture and what it
depends on; Phase 1 turns the assumptions into evidence. "I don't know" is a good answer —
gaps get tested, not judged.

## Mode
**Conversation mode is the default.** One question at a time, in plain words, short. Wait
for the answer. Reflect it back in one line only when you need to check you understood.
Offer **form mode** — the whole framework in `references/intake-framework.md`, filled in
offline and pasted back — only if the founder asks to write it all down, or says they would
rather do it in their own time.

## 1. The short intake — about 13 questions, 10–15 minutes
Ask these in order, one per message — never two in a turn, however related, however quick the
founder seems. Two questions in one message is a defect, not efficiency: ask the first, wait,
then ask the second. Follow up at most once per answer, and only on a gap. A question is
closed only by the founder's own words: never mark one answered because you can infer it —
"that also closes 2.4, they cope by word of mouth" is invented evidence however obvious the
inference. Inferred, it stays open and still gets asked. Where an item below lists two facts
(name and place; how it makes money and the price; money to invest and money to lose), that
is two messages.
The numbers refer to the full framework.

1. **5.0** Their name, and where in the UK they are (region or nearest city).
2. **1.1** The idea in a paragraph — who it is for, what they get, why they pay.
3. **1.4** The unique insight — what they understand about the customer or the problem that
   most people don't, and what they saw that made the idea obvious to them. (The framework's
   most important question; the seed of founder-market fit.)
4. **1.2** What is actually sold: a physical product, an online store, software or an app, or
   a service? (More than one is fine. This decides which pack is installed — see step 4.)
5. **1.3** What stage it is at — idea, sketched, talked to people, built, already selling.
6. **2.1** The problem, in the customer's own words. How often it bites, how much it stings.
7. **2.3** The beachhead — the one narrow group to win first.
8. **2.4** How those people cope today, and what that costs them.
9. **3.1 + 3.2** How it makes money, and the price — and what the price is anchored to.
10. **5.1** Hours a week, realistically, and when.
11. **5.2** Money they can invest, and money they can afford to lose. What covers living costs.
12. **6.3** Kill criteria — "if X is not true by date Y, I stop." If they have none, do not
    leave it open: propose one concrete number and one date drawn from their own answers
    ("no third café signed by 31 December — stop") and let them accept, change, or refuse it. Check it against the phase gates: a Phase 0 or 1
    deadline cannot demand a Phase 2 outcome such as paying customers.
    A missing kill criterion is a decision gap, and a decision gap gets a labelled
    recommendation, not a note in the register.
13. **Capstone** — of everything said, the one assumption that would kill the idea if wrong.

Then say: "That is enough to start. There are about twenty more questions — competition,
channels, your edge, and how you want me to work with you. Now, later, or as they come up?"
Respect the answer. If "now", continue through the remaining framework sections (2.2, 2.5,
2.6, 3.3–3.7, 4.x, 5.3–5.6, 6.1–6.2, 7.x) the same way. If "later", record them as open in
`state/active_context.md` and raise them one at a time when they become relevant.

## 2. Gap-probe pass — light
Probe only the gaps and the vague answers; never re-ask what was answered well. Apply the
`evidence-bar` mindset: "lots of people want this" → who, specifically, and how do you know?
A number with no basis → tag it and ask what it is anchored to. A blank → one focused
follow-up, or record it as an open unknown. A handful of questions, not a second questionnaire.

## 3. Seed the brain
Write the intake yourself into `state/business-brief.md`, using the framework's section
structure: answered questions filled in the founder's words, unanswered ones marked
"not yet answered". The founder never has to fill a form. Then propagate:
- `state/project_brief.md` — distilled thesis, founder-market fit, success definition, kill criteria.
- `state/product_context.md` — problem, job-to-be-done, beachhead persona, alternatives, why now.
- `state/financials.md` — every number given, each tagged `[ASSUMPTION — H/M/L]`.
- `state/risks.md` — the worry (5.6, if answered) and the capstone open the risk register.
- `state/system_patterns.md` — working preferences from section 7, if answered.
- `state/predictions.md` — the founder's kill criterion as row 1, in their words (who:
  founder; resolves by its date).
- `state/progress.md` — the Spine line: `Now: 0/10 stranger interviews — intake — <date>`.
- `state/active_context.md` — Open conditions: "none yet — written at the position".
- `AGENTS.md` — fill the `{{PLACEHOLDERS}}`: venture name, one-line description, founder name
  and region, current phase (0), gate criteria (10 stranger interviews). Also replace
  `{{VENTURE_NAME}}`, `{{DATE}}`, and `{{DAY_OF_WEEK}}` in every `state/` file, `docs/BRAND-VOICE.md`,
  `financials/*`, and `legal/*`. Use today's date; ask for the weekly-review day if unknown.

## 4. Install the pack(s) that fit
From the answer to 1.2:
- physical product → `physical` · online store or marketplace → `ecommerce` (usually with
  `physical` too, if they hold stock) · software, app, or subscription → `saas` · service,
  consulting, agency, coaching → `services`.
For each pack: copy every folder under `packs/<pack>/skills/` into `.claude/skills/` (and into
`.agents/skills/` as well, if that directory exists); copy `packs/<pack>/docs/*` into `docs/`.
Never delete anything. Record the installed packs in `state/tech_context.md`. Tell the founder
in one line which pack(s) were installed and that they add later-phase know-how, not work to
do now.

## 5. First commit, then hand off
If this folder is a git repository: check `git config user.email`; if it is empty, set a
repo-local identity from the intake (`git config user.name "<founder's name>"` and
`git config user.email "<first-name>@<venture-name>.local"` — local only, never pushed
anywhere). Then `git add -A` and commit ("Seed the brain from the intake"). Say one line
about it. If git is not set up, skip silently.

Confirm the seeded picture in a short paragraph, then hand to the `idea-interrogation` skill.
Set the focus to the Phase 0 → 1 gate: 10 interviews with strangers. Add one closing line:
when they have ten spare minutes some other day, saying "set up research tools" walks them
through free keys for UK company data and web search — nothing needed for now.

## Quality bar
The intake is done when someone who has never heard the idea could read
`state/business-brief.md` and explain the venture, the customer, the model, and the single
biggest risk. If they could not, keep probing.
