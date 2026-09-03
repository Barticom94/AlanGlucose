---
name: session-handoff
description: Checkpoint the venture's state at a task boundary or end of session. Use when the founder says "/session-handoff", "/checkpoint", "save state", "wrap up", "let's stop here", or before a long break. Updates the memory bank and writes a clean handover.
---

# Session Handoff

Long Opus sessions get compacted; sessions end. This skill makes the next session — yours
or a future one — resume cleanly. Run it at every task boundary. Do not rely on the
optional PreCompact hook alone: it is an opt-in helper, wired only when a founder's machine
has Python and the `start` skill switched it on, and even when it fires, acting on the
restored context is not guaranteed (see the brain's caveats).

## Checkpoint procedure
1. **`state/active_context.md`** — update the current focus, add a dated line to recent
   changes, and write the next concrete step. Make that step specific enough to start cold.
2. **`state/progress.md`** — move items between Done / In progress / Not started. Update the
   phase-gate progress count.
3. **`state/decisions_log.md`** — if a decision was made this session, append an entry
   (newest at the top): decision, context, alternatives, why.
4. **`state/risks.md`** — if a new risk surfaced, add it with a test and a mitigation.
5. **`state/financials.md`** — if any number changed, update it with its source.
6. **Open question** — write the single most important open question into `active_context.md`.
7. **Commit** — stage and commit `state/` to git with a short message. This is the
   git-anchored checkpoint the brain relies on.

## For `/checkpoint <message>`
A lightweight version: update `active_context.md` and commit `state/` with the supplied
message. Use it mid-task; use the full handoff at session end.

## Quality bar
A good handoff lets someone with no memory of this session pick up the exact next action in
under two minutes. If your handoff fails that test, it is not finished.
