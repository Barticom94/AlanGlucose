@AGENTS.md
@state/active_context.md
@state/progress.md

## Claude Code
This file is the Claude Code entry point. The contract itself is `AGENTS.md`, imported above
so that Codex and other harnesses read the same rules; the two state files load with it at
every session start and after every compaction, so no hook is needed to restore context.

- Skills: `.claude/skills/` — model-invoked by description, or typed as `/skill-name`.
- Subagents: `.claude/agents/` — spawned by name (`devils-advocate`, `evidence-checker`, …).
- Destructive commands are blocked by `permissions.deny` in `.claude/settings.json`.
- Optional Python hooks (`.claude/hooks/`: transcript backup before compaction, session log,
  extra command guardrail) are wired per machine in the git-ignored
  `.claude/settings.local.json` by the `start` skill, only when Python is present.
- Output style `reviewing` is set in `.claude/settings.json`: critique first, always.
- `CLAUDE.local.md` (git-ignored) holds the founder's personal notes; `start` creates it.
