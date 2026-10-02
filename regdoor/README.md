# RegDoor Regulatory Intelligence

Regulatory research, obligation analysis and regime comparison for digital financial markets
(virtual assets, crypto, payments, capital markets and banking), grounded in the RegDoor
regulatory database. Answers cite the underlying instruments with links to the RegDoor library
and a status label (in force, public consultation, legislative proposal, and so on).

Requires a RegDoor account (https://app.regdoor.com, or https://app.us.regdoor.com for US accounts).

## What it adds

- **RegDoor connector (MCP)**: a remote server that gives Claude access to the RegDoor regulatory
  database, the knowledge vault and your company's RegDoor workspace (company profile, contacts,
  interactions, projects, notes, collections and company content).
- **Skills** that activate on their own when a question enters regulatory context:
  - `regulatory-research`: what a rule says, requires or allows, its status, deadlines, bills and
    public consultations;
  - `obligation-mapping`: which obligations apply to your company, checklists and gap analysis;
  - `regime-comparison`: side-by-side comparison of modalities, jurisdictions or rule versions;
  - `regdoor-routing`, `regulatory-style` and `regdoor-setup`: the search procedure, the writing
    standard and connection troubleshooting used by the skills above.
- **Command** `/regdoor <question>` as an optional shortcut.

## Setup

1. Install the plugin and choose your **RegDoor region**: `mcp.regdoor.com` (EU, default) or
   `mcp.us.regdoor.com` (US). If you sign in at app.us.regdoor.com, choose `mcp.us.regdoor.com`.
2. Connect the RegDoor connector and sign in with your RegDoor app account (single sign-on,
   Google login included). If you belong to more than one company, choose it on the consent
   screen.
3. Ask a regulatory question in natural language, for example: "What does Res. BCB 520 require
   from a PSAV custodian?"

## Data and privacy

The plugin contains only instructions; it runs no local code.

- **RegDoor server.** The questions you ask, the search parameters Claude derives from them and,
  when you ask Claude to record something, the content of that record are sent over HTTPS to the
  RegDoor MCP server for the selected region (`https://mcp.regdoor.com/mcp` or
  `https://mcp.us.regdoor.com/mcp`), under your own RegDoor login (OAuth). The server returns
  regulatory text and data from your company's RegDoor workspace (profile files, CRM records,
  notes, collections), which enter the conversation.
- **Write access.** The connector can create and update records in your company's RegDoor
  workspace (contacts, interactions, projects, notes, collections, company content). Writes
  happen only when you ask for them and follow your company's MCP permissions; an administrator
  can put the company in read-only mode.
- **Web fallback.** When the RegDoor database has nothing relevant, the skills may use Claude's
  own web search to find public official sources, and the answer marks those citations as
  *(Web Page)*. Those queries go through Claude's web tools, not through RegDoor.

The plugin contacts no other destination.

- Privacy policy: https://app.regdoor.com/policies/privacy_policy (US: https://app.us.regdoor.com/policies/privacy_policy)
- Terms of use: https://app.regdoor.com/policies/terms_of_use (US: https://app.us.regdoor.com/policies/terms_of_use)

## Support

Email support@regdoor.com. Common issues and what to include in your message:
https://github.com/RegDoor/regdoor_plugin/blob/main/SUPPORT.md

## Limitations

Output is regulatory intelligence, not legal advice. Coverage follows the RegDoor database for
your account.
