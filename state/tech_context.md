# Tech Context

> Tools, stack, and integrations for this venture.

## Active stack
- Claude Code brain — this folder
- Python 3.13 (`py`) — runs the hooks in `.claude/hooks/`
- Node / `npx` — runs MCP servers
- git (optional) and a GitHub repo, if you want version control

## MCP servers — starter pack (active in `.mcp.json`)
`companies-house`, `exa`, `firecrawl`, `filesystem`, `sequential-thinking`. All five run via
`npx` (Node.js). The first three need the API keys listed in `CLAUDE.local.md.example`; the
other two need nothing.

## MCP servers — growth pack (wire in at Phase 2+, once the venture is live)
- Shopify Dev MCP — via the Shopify AI Toolkit (only if the venture is an online store)
- Klaviyo — Claude Settings → Connectors, or `https://mcp.klaviyo.com`
- Stripe — `https://mcp.stripe.com` (OAuth) or `npx -y @stripe/mcp`
- Notion — the hosted remote MCP (OAuth)
- Linear — `https://mcp.linear.app/mcp`
- Playwright — `npx @playwright/mcp@latest`
- PostHog — `https://mcp.posthog.com/sse` (EU: set `POSTHOG_BASE_URL`)
- GitHub — remote MCP at `https://api.githubcopilot.com/mcp/` with a personal access token
- basic-memory — `uvx basic-memory mcp` (needs `uv` installed)

Keep total active servers to roughly 5–8 — more crowds the context with tool schemas.

## No good MCP exists for
Trademark/domain checking, Royal Mail / DPD / Evri, HMRC. Use the gov.uk sites,
carrier APIs, or aggregators (Sendcloud, Easyship) directly.

## Tooling decisions
- {{DATE}} — {{ decision and reason }}
