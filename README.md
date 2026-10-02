# regdoor-plugins

RegDoor plugins for Claude. One plugin today, `regdoor/`, which bundles:

- the `regdoor` MCP connector (`https://${user_config.region_host}/mcp`; the user picks `mcp.regdoor.com` (EU) or `mcp.us.regdoor.com` (US) through the plugin's `userConfig`; same login as the app);
- `regdoor-setup` — connection and troubleshooting;
- `regdoor-routing` — mandatory procedure (consultant → topic → regulator → scoped search → citation);
- three use-case skills, `regulatory-research`, `obligation-mapping` and `regime-comparison`, activated automatically by description whenever a question enters regulatory context (no command needed);
- `regulatory-style` — writing and review layer (legal modality, status, mechanism and consequence, provision locators, acronyms, delivery registers). Maintained directly in this repository;
- a single command, `/regdoor <question>`, that classifies the request and applies the right flow. In Claude Code the command carries the plugin namespace (`/regdoor:regdoor`).

The plugin ships **no vault content** (consultants, topics, regulators, UUIDs). That stays on the server and is read at runtime through `global_vault_skills`.

Language: every file is in English. Answers follow the language of the user's message; domain terms (PSAV, Resolução, article numbering) are never translated. Skill descriptions keep a short pt/en trigger vocabulary because that is what users type.

## Install for testing

### claude.ai / Claude Desktop (chat)

1. Build the package: `python scripts/pack.py` (or `./scripts/pack.ps1`) → `dist/regdoor-plugin-<version>.zip`. Do not use `Compress-Archive` directly: it writes entry names with backslashes and the upload is rejected with "Zip file contains path with invalid characters".
2. In Claude: **Customize → Plugins → upload a custom plugin** and pick the zip. Choose the *RegDoor region* (`mcp.regdoor.com` EU / `mcp.us.regdoor.com` US) when prompted; check that the prompt appears, since the connector URL depends on it.
3. Open the plugin, click **Connect** on the RegDoor connector and sign in with the app.regdoor.com (or app.us.regdoor.com) account. Users who belong to more than one company choose the company on the consent screen.
4. In a new conversation, ask in natural language (no slash): "What does Res. BCB 520 require from a PSAV custodian?" — the answer must cite `app.regdoor.com/library/detail/<uuid>` (US: `app.us.regdoor.com`) links with a status label.

Team/Enterprise Owners: under **Organization settings → Skills → Policy**, enable *Skill sharing* (and *Share with groups*) so members can share the plugin. Org-wide plugin management is announced by Anthropic as "coming"; until then each user installs.

### Claude Code

Single session, no install:

```bash
claude --plugin-dir ./regdoor
```

Install through the marketplace (this repository is one):

```bash
claude plugin marketplace add RegDoor/regdoor-plugins
claude plugin install regdoor@regdoor
```

Claude Code asks for the *RegDoor region* when the plugin is enabled. Then `/mcp` → `regdoor` → *Authenticate*.

Validation and inventory:

```bash
claude plugin validate ./regdoor --strict
claude plugin details regdoor@regdoor
```

### Development environment

To point at the dev MCP, add `dev-mcp.regdoor.com` (or `dev-mcp.us.regdoor.com`) to `userConfig.region_host.options` in `regdoor/.claude-plugin/plugin.json` and make it the `default` before packaging. Do not commit that change.

## Distribution to customers

| Channel | When |
|---|---|
| Zip upload | Pilot |
| This repository as a marketplace (public, or private with per-customer read access) | Contracted customers |
| Anthropic plugin directory (`claude.ai/directory/manage` → *Submit new* → *Plugin bundle*; public repository required) | After the PoC is validated |

## Directory submission checklist

What Anthropic reviews is the `regdoor/` folder only: `README.md` (user-facing, discloses the data flow), `LICENSE`, `logo.svg` and the listing URLs in `plugin.json`. `scripts/`, `dist/` and this README stay outside the plugin. Before submitting, add `repository` (and `supportUrl` / `documentationUrl` once public pages exist) to `plugin.json`.

## Editing the style skill

Citation format, status vocabulary and the disclaimer rule have a single source: the "Citation and status" section of `regdoor-routing`. Keep `regulatory-style` consistent with it.

## Versioning

`version` in `regdoor/.claude-plugin/plugin.json` and in `.claude-plugin/marketplace.json` (keep them equal). Skill text change = patch; flow or connector change = minor.
