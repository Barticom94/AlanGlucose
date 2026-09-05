# Changelog

All notable changes to AlanGlucose. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions are git tags, and each tagged release on GitHub carries its section below as its notes.
"Tested" means run through the simulation harness (a scripted founder against the real contract files, graded
in a clean context) — not a live founder session.

## [Unreleased]

Candidates on `main` after v1.3.0, from intake iteration 21, post-intake round 3 and the Phase 3 round. Untested
as a set at the time of writing.

### Changed
- Assumption tags travel into the rule-12 `Reason n:` lines; a Reason line restating a tagged claim untagged is a defect.
- Runway is written as months with the division shown, or as "not computable until a recurring spend is chosen".
- Stored `docs/KNOWLEDGE.md` / `docs/LEARNED.md` rows cite with their own string (`from <file>, fetched <row date>`).
- Every clause about a customer, buyer, group, listing, platform or rival ends in its own tag, in every section.
- A `→` state line copies figures from the reply and never adds one; file-borne tags count in the quote audit.
- `Test:` lines end in the hours and pounds they cost; the `Strangers:` date is written as the sum it rests on.
- A computed paying count takes the lowest reading the founder's words allow and never a conditional; the
  `Carried:` line under an evidence-checker block records where its UNSUPPORTED verdicts went.
- Elapsed time is written as days with both dates; day names only after a calendar check.
- Rule 5 gains a Phase 2 reading (no code beyond what the current gate's evidence needs).
- `/status` answers "carry on" with the printed next step only; `risks.md` takes both the red-team and the
  devils-advocate headings.

## [1.3.0] — 2026-09-05

Confirmed on this tree: intake calibration 5/5 with zero invented evidence (iteration 21); 14 post-intake scenarios
70/80 with the anti-sycophancy floor clean throughout; the Phase 3 demotion path 7/7. One fabricated competitor
figure reached a research file and two generalisations went out untagged — fixed in the candidates above.

### Added
- **Gates run both ways.** A passed gate whose evidence stops being true is demoted by the weekly review, with
  `Now blocked:` / `Still in-phase:` lines and a logged entry.
- **Predictions scoreboard** (`state/predictions.md`): every forward-looking number or date becomes a row with a
  confidence and a resolve-by date; the weekly review resolves past-due rows by asking and reads the hit rate back.
- **Open conditions** in `state/active_context.md`: each *in, if* condition carries the gate it must be met before
  and blocks that gate until met or waived in the decisions log (`Whose:` field).
- **The Spine**: one number per phase in `state/progress.md`, read first at every review; an unchanged number opens
  the review with "Nothing moved".
- **Interview kit** in `customer-discovery`: a sourcing plan (`SOURCING.md`) with provenance on every source and
  slots only in the founder's typed hours; one file per interview from `INTERVIEW-TEMPLATE.md` with "not recorded"
  for anything the founder did not say; classify stranger / has-the-problem / real-conversation before counting.
- **`/status`**: one screen from the state files, no evaluation, ending with the next step (29 core skills).
- A Python-free after-compaction reminder hook shipped in `.claude/settings.json` (plain `cat`; tested in sh and
  PowerShell); `.claude/hooks/after-compact.md`.
- The partner reply shape mirrored to `.agents/output-style.md` so Codex, Gemini CLI and Cursor read it.

### Changed
- **The contract is consolidated**: `AGENTS.md` 192 → 175 lines and `partner.md` 144 → 105, from 184 inventoried
  constraints; every constraint now names a visible output form; the anti-sycophancy floor verified unchanged.
- Rule 12 reasons as labelled lines in fixed order: `Mine:` (what this venture holds that a competitor starting
  tomorrow would not, in the founder's words), then `Reason 1–3:` each with a `→ gate` / `→ condition` / `→ filled`
  bucket, then the steelman line.
- Every quoted reviewer block ends with `Audit: <n> corrected, <m> struck, <k> tags added` and the struck or
  corrected lines; the devils-advocate returns eight labelled lines and no longer writes `risks.md` itself.
- Rule 9 defines a decision: a closed hypothetical or an acknowledgement is never logged; founder-completed actions
  carry `pending —` until the founder says they are done.
- Decision gaps on three labelled lines (`Options:` / `Recommendation:` / `Risk:`); the next step on four
  (`Next step:` / `Then:` / `Carrying:` / `Strangers:`).
- `start`: on macOS, `xcode-select --print-path` runs first so a machine without Command Line Tools is not shown
  Apple's install dialog; Step 0 uses only commands that never prompt; "click Allow" is now "choose Yes".
- Codex: MCP keys forwarded with `env_vars`; state files, trust gating and the deny list stated for other harnesses.
- README: honest about what leaves the machine and about the relay route; `tools/` marked as not in the download.
- `docs/LEARNED.md` confidence is one word (the send route's enum); rows already in `docs/KNOWLEDGE.md` are not
  re-logged.

## [1.2.2] — 2026-09-04

### Changed
- A kill criterion is a pick like any other: the recommended threshold and the one way it misfires; parking a fork
  is naming it.
- A legal duty recited from memory carries a tag; the untagged sentence beside a cited one is checked first.
- The next step must produce a condition's input with the customers and kit the founder has today; a reviewer's
  test is carried in the same message, whole.

## [1.2.1] — 2026-09-04

### Changed
- The closing sentence exempts nothing: a mechanism, a design choice or a price sensitivity not fetched this turn
  carries a tag.
- The next step is read against the hours the founder typed; the venue or the hour moves, never the founder.
- Decision gaps named in a message (a kill criterion, an employment status) are filled in that message or not named.

## [1.2.0] — 2026-09-04

Hardened across 16 stress iterations (80 simulated intakes across a terrible-to-excellent idea spectrum): the
anti-sycophancy floor never broke; invented evidence driven to zero in the final Opus run.

### Added
- **Learnings phone home**: rule 13 and `docs/LEARNED.md` record general facts the brain looks up;
  `contribute-learnings` sends only those rows, with consent, never anything the founder typed; `docs/KNOWLEDGE.md`
  is the shared, reviewed knowledge base; a Cloudflare Worker relay (`tools/relay/`) so sending needs only an
  internet connection; `tools/harvest-learnings.py` and a weekly Action open a reviewed PR.
- Bracket audit before send: every citation is `[<full URL>, fetched <date>]` or `[from memory — not checked]`;
  a bracket covers only its clause; one competitor per line.
- Provenance check before any message that describes the founder back to them.
- Quoted reviews: findings are quoted and audited with three named checks; "they agreed" with nothing quoted is
  no review.

### Changed
- Rule 12: three conditions is a ceiling, not a target; the phase gate is never a condition; the position is bound
  to the devils-advocate's reasons one at a time.
- Rules converted from prohibitions to required output steps throughout (prohibitions did not bind in testing).

## [1.1.0] — 2026-09-04

### Changed
- **The partner frame.** The default output style is now an experienced founder doing diligence on a pitch to join
  as a partner: what would stop me · what I can fill (knowledge, decision, evidence gaps, each with its fill) ·
  what I'd be coming in for · my position (not in / in, if / in). Replaces the interrogator frame.
- Rule 13: bring what you know — check `docs/KNOWLEDGE.md` and `docs/LEARNED.md`, then search and cite, before
  asking the founder to prove anything.

## [1.0.0] — 2026-09-03

First public release.

### Added
- ZIP-first onboarding: download, extract, open in the Claude Code app, say hello. The `start` skill sets the
  machine up, briefs the founder and begins a one-question-at-a-time intake.
- Harness-agnostic core: `AGENTS.md` is the contract; `CLAUDE.md` imports it; `tools/build-adapters.py` mirrors
  skills to `.agents/skills/` and subagents and MCP config to `.codex/`, checked in CI.
- Vertical packs (`ecommerce`, `saas`, `services`, `physical`) installed by the intake; the core is vertical-neutral.
- UK-only context; Yorkshire- and founder-specific wording removed.
- Destructive commands blocked by `permissions.deny`; optional Python hooks wired per machine, never required.

[Unreleased]: https://github.com/Barticom94/AlanGlucose/compare/v1.3.0...HEAD
[1.3.0]: https://github.com/Barticom94/AlanGlucose/compare/v1.2.2...v1.3.0
[1.2.2]: https://github.com/Barticom94/AlanGlucose/compare/v1.2.1...v1.2.2
[1.2.1]: https://github.com/Barticom94/AlanGlucose/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/Barticom94/AlanGlucose/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/Barticom94/AlanGlucose/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Barticom94/AlanGlucose/releases/tag/v1.0.0
