# AlanGlucose — a Claude Code template for evaluating and building a business

A per-venture "brain": a structured Claude Code workspace that interrogates a business
idea hard, validates it with real evidence, then helps build it — phase by phase, with
anti-sycophancy enforced and context that survives long sessions.

Clone this folder once per venture. Built for a single UK founder with an
ecommerce-operations background.

## Starting a new venture

In the Claude Code desktop app, paste this prompt into any session:

```
Bootstrap a new AlanGlucose venture brain:
1. Ask me for a short, folder-safe venture name.
2. Clone the template into a new folder with that name:
   git clone https://github.com/Barticom94/AlanGlucose.git "<venture-name>"
3. Give the venture a clean history: delete the cloned .git folder, then run `git init`.
4. Inside the new folder, copy CLAUDE.local.md.example to CLAUDE.local.md.
5. Open the new folder in File Explorer, and copy its full absolute path to the clipboard.
6. Show me the path, and tell me to open that folder as a new session in the Claude Code
   desktop app. Do not start the intake in this window.
```

Then, in the desktop app, start a new session with that folder as the Project folder — its
path is already on your clipboard, so just paste it. The brain onboards you automatically
from there: it finishes setup, briefs you, shows the roadmap, and runs the idea intake. The
"First-time setup" and "Starter sequence" sections below are reference; the bootstrap and
the `start` skill do them for you.

## How it works

- **`CLAUDE.md`** — the behavioural contract Claude reloads every session and after compaction.
- **`state/`** — the memory bank: hand-maintained markdown, updated at every task boundary.
- **`.claude/skills/`** — 32 progressive-disclosure skills, from idea interrogation to operations.
- **`.claude/agents/`** — 14 subagents, run in builder→reviewer pairs to fight optimism bias.
- **`.claude/hooks/`** — 4 Python hooks: back up context, restore it, log sessions, block destructive commands.
- **`.claude/SYCOPHANCY.md`** — the anti-flattery contract.
- **`docs/`** — long-form UK reference material, loaded on demand.

## Phases

`0 Idea Interrogation → 1 Validation → 2 MVP → 3 Early Traction → 4 Growth → 5 Scale/Fundraise`

Each phase has a hard gate (see `CLAUDE.md`). The brain refuses later-phase work until the
current gate is met — that is a feature, not a bug.

## First-time setup

1. (Once, ever) Copy `GLOBAL-CLAUDE.md.example` to `~/.claude/CLAUDE.md` — optional but
   recommended; it sets anti-sycophancy defaults for every Claude Code session.
2. Read `BOOTSTRAP.md` — the phase model, the gates, and the order to do things in.
3. Copy `CLAUDE.local.md.example` to `CLAUDE.local.md` and set the API-key environment
   variables it lists.
4. Review `.mcp.json` and verify each MCP install command — the ecosystem moves fast.
5. Confirm hooks: `.claude/settings.json` invokes `py .claude/hooks/*.py` (Python 3.13).

## Starter sequence for a new venture

1. Run `/idea-intake` → the `business-intake` skill hands you the intake framework. Fill it
   in, paste it back; the brain probes the gaps and seeds every `state/` file — including the
   `CLAUDE.md` placeholders and the phase.
2. The brain hands off to `idea-interrogation` — Disciplined Entrepreneurship steps 1–3 and
   Mom Test preparation.
3. Run `/premortem` → capture initial failure modes into `state/risks.md`.
4. Commit `state/` to git — the first checkpoint.
5. Open the Phase 0 task: interview 10 strangers about the problem.
6. Keep sessions ≤ 2 hours; run `/session-handoff` at the end of each.
7. After ~1 week, run `/reality-check` and the Phase 0 gate. Advance, or revise the thesis.

## Conventions

- Skills are model-invoked by their `description`; several are user-invocable as slash commands.
- The command map ("When the founder says…") lives in `CLAUDE.md`.
- All numbers live in `state/financials.md` — one source of truth.
- UK tax/legal/funding figures are time-sensitive (2026 edition); verify against gov.uk
  before relying on any number in a real decision.

## Directory map

```
.
├── CLAUDE.md                 Behavioural contract
├── ABOUT.md                  What AlanGlucose is, and why
├── BOOTSTRAP.md              The operating manual — read this first
├── CLAUDE.local.md.example   Personal config — copy to CLAUDE.local.md
├── GLOBAL-CLAUDE.md.example  Optional global config for ~/.claude/
├── .mcp.json                 MCP server registry
├── README.md
├── .claude/
│   ├── settings.json      Hooks, permissions, output style
│   ├── SYCOPHANCY.md      Anti-sycophancy contract
│   ├── agents/            14 subagents
│   ├── skills/            32 skills (each a dir with SKILL.md)
│   ├── hooks/             session-start, pre-compact, session-log, bash-guardrails
│   ├── output-styles/     planning, building, reviewing, presenting
│   └── backups/           PreCompact transcript snapshots
├── state/                 The memory bank (12 files)
├── docs/                  UK-LEGAL-TAX, UK-FUNDING, ECOM-OPS, BRAND-VOICE, sops/
├── research/              customer-interviews, competitor-profiles, market-reports, sector-notes
├── financials/            unit-economics & cashflow templates, scenarios/
├── marketing/             landing-pages, email-flows, ad-creatives
├── legal/                 T&Cs, privacy, returns, supplier-contracts/
└── tasks/                 Markdown to-do tracking
```

## Caveats

Built to the "Claude Brain" specification. Claude Code changes fast — verify MCP commands
and hook behaviour before depending on them. Legal and tax content is information, not
advice; engage a UK chartered accountant for SEIS, VAT, and company-structure decisions.
The brain does not replace talking to real customers.
