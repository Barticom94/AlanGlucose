# Tech Context

> Tools, stack, and integrations for this venture. The `start` skill fills the first two
> sections on day one; update them whenever something is added.

## What is set up on this machine
- Harness: {{ Claude Code (desktop app / terminal) or other }}
- Version control: {{ git initialised — yes / no }}
- Optional helpers (Python hooks): {{ on / off }}
- Research tools (MCP servers): {{ none / list }}

## Packs installed
- {{ none yet — the intake installs ecommerce, saas, services, and/or physical }}

## Optional research tools — `.mcp.json.example`
`companies-house` (free UK company data — free key), `exa` and `firecrawl` (web search and
crawling — free tiers, keys needed), `filesystem`, `sequential-thinking`. All run via `npx`,
so they need Node. The built-in web search covers Phases 0 and 1 without any of them.

## Growth-pack tools (wire in at Phase 2+, only if the venture needs them)
- Stripe — `https://mcp.stripe.com` (OAuth) or `npx -y @stripe/mcp`
- Notion, Linear, PostHog — each has a hosted remote MCP
- Playwright — `npx @playwright/mcp@latest`
- GitHub — remote MCP at `https://api.githubcopilot.com/mcp/` with a personal access token
- basic-memory — `uvx basic-memory mcp` (needs `uv`)
- Vertical-specific tools (store platforms, email platforms, carriers) are listed in the
  installed pack's ops document.

Keep active servers to roughly 5–8 — more crowds the context with tool schemas.

## No good MCP exists for
Trademark and domain checking, HMRC. Use the official sites directly.

## Tooling decisions
- {{DATE}} — {{ decision and reason }}
