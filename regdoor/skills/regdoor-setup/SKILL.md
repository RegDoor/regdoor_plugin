---
name: regdoor-setup
description: First-run setup and troubleshooting for the RegDoor connector (MCP). Use when the user just installed the RegDoor plugin, asks how to connect or log in to RegDoor, sees "not connected" / 401 / "missing company" / "re-authorization" errors, wants to switch company, or when RegDoor tools (search_regulatory_content, global_vault_skills, list_contents) are not available in the conversation.
---

# RegDoor connector setup

The RegDoor plugin bundles one remote MCP connector, `regdoor`. Its host depends on the region
chosen when the plugin was enabled (`mcp.regdoor.com` for EU accounts, `mcp.us.regdoor.com` for
US accounts). It authenticates with the same login as the RegDoor app (app.regdoor.com or app.us.regdoor.com; single sign-on, Google
login included). No API key, no token to paste.

## 1. Check the connection

Look at the tools available in this conversation. If you can see `search_regulatory_content`
and `global_vault_skills`, the connector is live: skip to step 3.

If you cannot see them, tell the user, in one short paragraph, how to connect on their surface:

| Surface | How to connect |
|---|---|
| claude.ai / Claude Desktop | *Customize → Plugins → RegDoor → Connect* (or *Customize → Connectors → RegDoor → Connect*). A RegDoor login page opens; sign in with the RegDoor app account. |
| Claude Code | Run `/mcp`, pick `regdoor`, choose *Authenticate*. The browser opens the RegDoor login. |
| Cowork | Same as claude.ai; connectors reach RegDoor through Anthropic's cloud. |

Users who belong to more than one company choose the company on the consent screen after login.
To switch company later, disconnect and connect again.

## 2. Common errors

| Symptom | Cause | What to say |
|---|---|---|
| `401` / "requires re-authorization" | Session expired | Reconnect (same steps as above). Nothing else to change. |
| `400 missing_company` | User belongs to several companies and none was chosen | Reconnect and pick the company on the consent screen. |
| Sign-in rejects a valid RegDoor account, or no company is found | Wrong region selected (EU accounts sign in at app.regdoor.com, US accounts at app.us.regdoor.com) | Change the plugin's *RegDoor region* setting to the other host (Claude Code: `/plugin` → RegDoor → configure; claude.ai / Desktop: *Customize → Plugins → RegDoor*), then reconnect. |
| Tools appear but write calls (create/update/delete) return `company_scope_denied` | The company is in read-only mode for MCP | Read tools still work; writes (create/update) are disabled by the company's admin. Do not retry. |

Never ask the user for a token, password or API key, and never suggest copying a bearer
token from the browser: the connector handles login itself.

## 3. Smoke test

Run, in this order, and report the result to the user in two plain-language lines (for
example "connected; the Brazilian knowledge base answered"). Never show tool names, parameters
or raw results to the user.

1. `global_vault_skills(mode="route", query="regras para PSAV no Brasil")` → expect `detected_jurisdictions: ["brazil"]` and a consultant.
2. `search_regulatory_content(query="autorização para prestação de serviços de ativos virtuais", jurisdiction_id=[32], limit=3)` → expect chunks with `content_uuid`.

If both work, the plugin is ready. Tell the user they can simply ask regulatory questions in
natural language (the skills activate on their own) or use `/regdoor <question>` as a shortcut.
