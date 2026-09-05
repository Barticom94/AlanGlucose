---
name: session-handoff
description: Checkpoint the venture's state at a task boundary or end of session. Use when the founder says "/session-handoff", "/checkpoint", "save state", "wrap up", "let's stop here", or before a long break. Updates the memory bank, writes a clean handover, and offers to share any new research learnings with the template.
---

# Session Handoff

Long sessions get compacted; sessions end. This skill makes the next session — yours or a
future one — resume cleanly. Run it at every task boundary. Do not rely on the optional
PreCompact hook alone: it is an opt-in helper, wired only when a founder's machine has
Python and the `start` skill switched it on, and even when it fires, acting on the restored
context is not guaranteed.

## Checkpoint procedure
1. **`state/active_context.md`** — update the current focus, add a dated line to recent
   changes, and write the next concrete step. Make that step specific enough to start cold.
2. **`state/progress.md`** — move items between Done / In progress / Not started. Update the
   phase-gate progress count, and the Spine line if the number moved.
3. **`state/decisions_log.md`** — if a decision was made this session, append an entry
   (newest at the top): decision, context, alternatives, why.
4. **`state/predictions.md`** — any forward-looking number or date given this session (by
   you or the founder) becomes a row.
5. **`state/risks.md`** — if a new risk surfaced, add it with a test and a mitigation.
6. **`state/financials.md`** — if any number changed, update it with its source.
7. **Open question** — write the single most important open question into `active_context.md`.
8. **Commit** — stage and commit `state/` and `docs/LEARNED.md` to git with a short message,
   if git is set up. This is the git-anchored checkpoint the brain relies on.
9. **Learnings** — if `docs/LEARNED.md` has rows not yet marked `shared`, and
   `CLAUDE.local.md` does not say `share-learnings: no`, run the `contribute-learnings`
   skill. It shares only the research the brain did, never the founder's inputs, and shows
   every row before anything is sent. Offer at most once per session.

## For `/checkpoint <message>`
A lightweight version: update `active_context.md` and commit `state/` with the supplied
message. Use it mid-task; use the full handoff at session end.

## Quality bar
A good handoff lets someone with no memory of this session pick up the exact next action in
under two minutes. If your handoff fails that test, it is not finished.
