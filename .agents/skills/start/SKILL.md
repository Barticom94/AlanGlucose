---
name: start
description: First-run onboarding for a new venture brain. Use the first time a freshly-downloaded AlanGlucose folder is opened (AGENTS.md's first-run check fires because `.claude/.initialised` is absent), or when the founder says "/start", "start", "get started", "begin", or just says hello in a brain that has not been initialised. Sets the machine up quietly, briefs the founder in plain English, shows the roadmap, and begins the idea intake one question at a time.
---

# Start — first-run onboarding

Runs once. Assume the founder may never have used a terminal, git, or an AI coding tool.
Plain English throughout; explain any technical word in the same sentence; never ask the
founder to run a command you can run yourself; never ask them to install anything. From
"hello" to the first intake question should take under three minutes.

## Step 0 — Look before you speak
Silently, with your file and shell tools, find out:
- Which harness you are running in (Claude Code, Codex, or something else — from your own
  tool names and surroundings). Steps marked *Claude Code only* are skipped elsewhere.
- Whether this folder is a git repository (`.git/` exists) and whether `git` is installed.
- Whether Python is available — run `python3 --version`, and on Windows also `py --version`,
  from the same shell tool the hooks will use. Note the exact launcher that worked; that is
  the one to write into the hooks block below. Whether Node is available (`node --version`).
- Which of `COMPANIES_HOUSE_API_KEY`, `EXA_API_KEY`, `FIRECRAWL_API_KEY` are set.
- Whether `~/.claude/CLAUDE.md` exists, and whether `CLAUDE.local.md` exists in this folder.

Do not report this list to the founder. It only shapes what you offer in Step 2.

## Step 1 — Say hello
Five sentences at most: you are their venture brain; in the next few minutes you will do a
short setup, give a briefing, show the road ahead, and then start asking about their idea;
the app will ask their permission a few times in the next minute or two — click Allow each
time, nothing leaves their computer; "I don't know" is always a fine answer; they can stop
at any point and pick up later.

## Step 2 — Quiet setup
Do these without asking. Say one line about each only if there is something they need to know.
- If `CLAUDE.local.md` is missing, copy `CLAUDE.local.md.example` to `CLAUDE.local.md` and
  fill in `{{ABSOLUTE_PATH}}` with this folder's full path.
- If `git` is installed and there is no `.git/`, run `git init` — nothing more yet; the first
  commit happens at the end of the intake, once the founder's name is known (a fresh machine
  has no git identity, and a commit would fail). If `git` is not installed, say once, plainly:
  "Version control isn't set up on this computer — your work still saves to the files in this
  folder, so back the folder up now and then." Do not tell them to install git.
- If `git remote -v` still points at the AlanGlucose template, run `git remote remove origin`.
- Do not touch anything outside this folder (no `~/.claude/CLAUDE.md`). If the founder later
  wants the honesty defaults everywhere, `GLOBAL-CLAUDE.md.example` explains the manual copy.

Then one optional extra, only if Python was found *(Claude Code only)*: "I can switch on a
few small helpers: a backup of our conversation before a long session gets compressed, a
restore of it afterwards, a session log, and an extra safety check on commands. Yes or no?
Saying no breaks nothing." If yes, write `.claude/settings.local.json` with the block below,
replacing `LAUNCHER` with the launcher that worked in Step 0. Do not offer research tools
now — that is the final section of this skill, for a later session.

Record what was set up in `state/tech_context.md` (its first two sections).

Hooks block for `.claude/settings.local.json`. Each command first changes into the project
folder, then runs the hook by a relative path — the one form found to work in every shell
(Git Bash, msys2, macOS/Linux `sh`) without tripping on Windows drive letters:
```json
{
  "hooks": {
    "SessionStart": [{ "matcher": "compact|clear", "hooks": [
      { "type": "command", "command": "cd \"$CLAUDE_PROJECT_DIR\" && LAUNCHER .claude/hooks/session-start.py" } ] }],
    "PreCompact": [{ "matcher": "auto|manual", "hooks": [
      { "type": "command", "command": "cd \"$CLAUDE_PROJECT_DIR\" && LAUNCHER .claude/hooks/pre-compact.py" } ] }],
    "Stop": [{ "hooks": [
      { "type": "command", "command": "cd \"$CLAUDE_PROJECT_DIR\" && LAUNCHER .claude/hooks/session-log.py" } ] }],
    "PreToolUse": [{ "matcher": "Bash|PowerShell", "hooks": [
      { "type": "command", "command": "cd \"$CLAUDE_PROJECT_DIR\" && LAUNCHER .claude/hooks/bash-guardrails.py" } ] }]
  }
}
```
On Windows without Git Bash (the shell tool is PowerShell), use this command form instead:
`cd $env:CLAUDE_PROJECT_DIR; LAUNCHER .claude/hooks/<hook>.py`.

## Step 3 — Brief the founder
One short paragraph, in your own words: AlanGlucose takes a business idea from "what if" to
"this works" — or to a fast, cheap "no" — by interrogating it hard, validating it with real
evidence from real people, and only then helping build it. It is deliberately blunt: its job
is to find the flaw before the founder spends money on it. Then, how to use it well: one
venture per folder; sessions of about two hours; when the brain pushes back, push back with
evidence, not conviction; run a reality check before any spend and a review every week; let
the phase gates hold — they are the point.

## Step 4 — The roadmap
Present the sequence — no dates, just what each phase proves and what unlocks the next:
- **Phase 0 — Idea.** Interrogate the idea before spending anything. *Gate:* 10 interviews
  with strangers who have the problem.
- **Phase 1 — Validation.** Prove strangers will commit something real. *Gate:* 3 real
  commitments — a deposit, a letter of intent, a paid pre-order, or a waitlist sign-up with
  card details.
- **Phase 2 — MVP.** Ship the smallest real thing people pay for. *Gate:* 10 paying customers
  and 7-day retention data.
- **Phase 3 — Traction.** Find one acquisition channel that pays back. *Gate:* CAC < LTV/3
  and gross margin above 40%.
- **Phase 4 — Growth.** Deepen the channel; remove the founder as the bottleneck. *Gate:*
  EBITDA-positive, or a credible, evidenced path to raising.
- **Phase 5 — Scale.** Grow it, raise for it, or run it profitably — the founder's call.

Say that the brain is in Phase 0 and that the first gate is those 10 interviews.

## Step 5 — Begin the intake
Hand straight to the `business-intake` skill in its default **conversation mode**: one
question at a time, starting with the founder's name and where in the UK they are. Do not
paste the whole framework at them. Do not wait to be asked.

## Step 6 — Mark the brain initialised
As soon as the first intake question has been asked, create `.claude/.initialised` containing
today's date and one line ("onboarded"). This stops onboarding re-running every session.
`/start` can still be run by hand any time the founder wants the briefing or roadmap again.

## Later — research tools (only when the founder says "set up research tools")
Not part of the first session. *(Claude Code only.)* Needs Node (`node --version`) and, for
most servers, a free API key. Walk the founder through it one server at a time:
- **Companies House** — free UK company data. Key from
  developer.company-information.service.gov.uk (free account).
- **Exa** (web search) and **Firecrawl** (web crawling) — free tiers; keys from exa.ai and
  firecrawl.dev.
- `filesystem` and `sequential-thinking` need no key.
Copy `.mcp.json.example` to `.mcp.json` keeping only the servers they want. Keys go in
environment variables, never in files (`CLAUDE.local.md.example` says where on each OS);
the app needs a restart to see a new variable, and it will ask once to approve the new
servers. If Node is missing, say so plainly — the built-in web search covers Phases 0 and 1.
Record the result in `state/tech_context.md`.
