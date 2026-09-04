# AlanGlucose — a brain for evaluating and building a business

A per-venture "brain": a structured AI workspace that interrogates a business idea hard,
validates it with real evidence from real people, then helps build it — one phase at a time,
with anti-sycophancy enforced and context that survives long sessions.

Built for a single UK founder. One folder per venture. Works in Claude Code (the desktop app
or the terminal) and in other AI harnesses that read `AGENTS.md`, such as Codex.

## Start a new venture — no terminal needed

You need the Claude Code app (desktop) with a Claude subscription. Nothing else.

1. Download the latest release: [AlanGlucose.zip](https://github.com/Barticom94/AlanGlucose/releases/latest/download/AlanGlucose.zip)
   (or pick a version on the [releases page](https://github.com/Barticom94/AlanGlucose/releases)).
2. Unzip it properly — on Windows right-click → *Extract All…*; on a Mac double-click it.
   You get a folder called `AlanGlucose`. Rename it to your venture's name and put it
   somewhere sensible, like Documents.
3. Open the Claude Code app, start a new session, and choose that folder as the project.
   The app asks whether you trust the folder — say yes. It will also ask permission for a
   few small actions in the first minute or two; choose Yes each time (one of them says
   "allow Claude to edit its own settings": that is the brain writing its own notes inside
   this folder). Nothing in those steps leaves your computer.
4. Say hello.

The brain takes it from there: a quiet setup, a short briefing, the roadmap, then it starts
asking about your idea — one question at a time, "I don't know" always allowed. It offers
one optional helper if your computer has Python; saying no breaks nothing. Research tools
(free UK company data, web search) can be added any later day by saying "set up research tools".

### Already use Claude Code or git?
Either clone it — `git clone https://github.com/Barticom94/AlanGlucose.git "<venture-name>"` —
then open the folder as a new session; the brain detaches it from the template itself. Or
paste this into any Claude Code session:

```
Set up a new AlanGlucose venture brain: ask me for a short, folder-safe venture name; run
git clone https://github.com/Barticom94/AlanGlucose.git "<name>"; then show me the new
folder's full path and tell me to open it as a new session. Do nothing else in this window.
```

### Using it with Codex or another harness
`AGENTS.md` is the contract (Claude Code imports it from `CLAUDE.md`). Skills are mirrored in
`.agents/skills/`, subagents in `.codex/agents/`, and MCP servers in `.codex/config.toml`
(keys are forwarded from your shell). Open the folder in your harness, accept its trust prompt
for the folder (or `.codex/` is ignored), and say hello. Hooks are Claude Code only; the
`partner` reply shape is mirrored to `.agents/output-style.md` and `AGENTS.md` tells other
harnesses to read it. Not yet tested end-to-end in Codex — tell the maintainer what breaks.

## How it works

- **`AGENTS.md`** — the behavioural contract: phases, gates, and the operating rules.
- **`CLAUDE.md`** — Claude Code's entry point; imports `AGENTS.md` and the two live state files.
- **`state/`** — the memory bank: plain markdown, updated at every task boundary, with a
  predictions scoreboard and an open-conditions list the weekly review reads back.
- **`.claude/skills/`** — 28 core skills, vertical-neutral, from idea interrogation to UK tax.
- **`packs/`** — vertical packs (`ecommerce`, `saas`, `services`, `physical`) installed by
  the intake. More than one can apply.
- **`.claude/agents/`** — 14 subagents, run in builder→reviewer pairs to fight optimism bias.
- **`.claude/settings.json`** — the `partner` output style (diligence first, then fill the
  gaps), the destructive-command deny rules, and one built-in hook that prints a short
  reminder after a long session is compressed (plain `cat`, no Python).
- **`.claude/hooks/`** — 4 *optional* Python helpers (transcript backup before compaction,
  context restore after it, session log, extra command guardrail), switched on per machine
  by the `start` skill. Nothing depends on them.
- **`.claude/SYCOPHANCY.md`** — the full anti-flattery contract.
- **`docs/`** — UK legal, tax, funding, and brand reference, loaded on demand.

## Phases

`0 Idea → 1 Validation → 2 MVP → 3 Traction → 4 Growth → 5 Scale`

Each phase has one hard gate (in `AGENTS.md`). The brain refuses later-phase work until the
current gate is met — that is a feature, not a bug. `BOOTSTRAP.md` is the operating manual.

## Conventions

- Skills are chosen by their `description`; in Claude Code they are also `/slash-commands`.
- The command map ("When the founder says…") lives in `AGENTS.md`.
- All numbers live in `state/financials.md` — one source of truth.
- UK tax, legal, and funding figures are time-sensitive (2026 edition); verify on gov.uk
  before relying on any number in a real decision.

## Directory map

```
.
├── AGENTS.md                 The contract — read by every harness
├── CLAUDE.md                 Claude Code entry point (imports AGENTS.md + state)
├── ABOUT.md                  What AlanGlucose is, and why
├── BOOTSTRAP.md              The operating manual
├── CLAUDE.local.md.example   Personal notes template — start copies it
├── GLOBAL-CLAUDE.md.example  Optional honesty defaults for every project on a machine
├── .mcp.json.example         Optional research tools — start enables what it can
├── .claude/
│   ├── settings.json      Output style, deny rules, one plain-text reminder hook
│   ├── SYCOPHANCY.md      Anti-sycophancy contract
│   ├── agents/            14 subagents
│   ├── skills/            28 core skills
│   ├── hooks/             4 optional Python helpers
│   └── output-styles/     partner (default), reviewing, planning, building, presenting
├── .agents/               Generated mirror of the skills and the reply shape for Codex, Gemini CLI, Cursor
├── .codex/                Generated Codex subagents + MCP config
├── packs/                 ecommerce, saas, services, physical
├── state/                 The memory bank
├── docs/                  UK-LEGAL-TAX, UK-FUNDING, BRAND-VOICE, sops/
├── research/              customer-interviews, competitor-profiles, market-reports
├── financials/            unit-economics & cashflow templates, scenarios/
├── marketing/             landing-pages, email-flows, ad-creatives
├── legal/                 T&Cs, privacy, returns, supplier-contracts/
├── tasks/                 Markdown to-do tracking
└── tools/                 build-adapters.py — maintainer only; not in the download
```

## For the template maintainer (not for founders)

After editing anything under `.claude/skills/`, `.claude/agents/`, or `.mcp.json.example`,
run `python tools/build-adapters.py` and commit the regenerated `.agents/` and `.codex/`
folders. CI fails if they are stale. Founders using a venture never need this.

Learnings arrive as issues labelled `learnings` (see `.github/ISSUE_TEMPLATE/learnings.md`),
posted by the relay in `tools/relay/` (deploy once; its README has the steps) or by a founder's
own GitHub account.
`python tools/harvest-learnings.py` reviews them into `docs/KNOWLEDGE.md`; a weekly Action
opens a PR with the proposed rows, so nothing enters the knowledge base unreviewed.

To publish a new version: `git tag v1.x.y && git push --tags`. CI builds `AlanGlucose.zip`
from the tag (tracked files only; `tools/` and `.github/` excluded) and creates the release,
so the README's "latest release" link always serves the newest one.

## What leaves your computer

Nothing goes back to this template unless you say yes to one thing. (The brain's web
searches and page fetches go to the web like any browser's, and the conversation goes to
Anthropic like any Claude session.) When the brain looks up a general fact, such as a tax
rule, a fee, or a benchmark, it records it in `docs/LEARNED.md`. At a session handoff it
asks, once, whether it may send those facts back to this template so other founders' brains
know them too. It shows you every row before sending. Sending goes one of two ways: through
a small relay the maintainer runs (it sees the rows and your IP, stores nothing) once this
copy has been given the relay address, otherwise through a link that opens a pre-filled
GitHub issue for you to submit, which needs a free GitHub account. Only the research it did
is shared:
never what you typed, never your venture's name, customers, competitors, or numbers. Say no
and it never asks again. The merged facts live in `docs/KNOWLEDGE.md`, which every brain
checks before searching.

## Caveats

AI harnesses change fast — verify hook and MCP behaviour before depending on them. Legal and
tax content is information, not advice; engage a UK chartered accountant for SEIS, VAT, and
company-structure decisions. The brain does not replace talking to real customers.
