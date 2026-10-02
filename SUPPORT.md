# Support — RegDoor plugin for Claude

## Contact

Email **support@regdoor.com** with:

- the Claude surface you use (claude.ai, Claude Desktop, Cowork or Claude Code);
- the RegDoor region selected in the plugin (`mcp.regdoor.com` or `mcp.us.regdoor.com`);
- the error message or a short description of what happened.

Do not send passwords, tokens or confidential company information by email.

## Common issues

| Symptom | What to do |
|---|---|
| RegDoor tools are not available in the conversation | Connect the RegDoor connector: on claude.ai / Claude Desktop / Cowork, *Customize → Plugins → RegDoor → Connect*; on Claude Code, `/mcp` → `regdoor` → *Authenticate*. |
| Sign-in rejects a valid account, or no company is found | The region is probably wrong. EU accounts sign in at app.regdoor.com and use `mcp.regdoor.com`; US accounts sign in at app.us.regdoor.com and use `mcp.us.regdoor.com`. Change the plugin's *RegDoor region* setting (Claude Code: `/plugin` → RegDoor → configure; claude.ai / Desktop: *Customize → Plugins → RegDoor*) and reconnect. |
| `401` or "requires re-authorization" | The session expired. Reconnect the connector. |
| `400 missing_company` | You belong to more than one company. Reconnect and choose the company on the consent screen. |
| Write actions return `company_scope_denied` | Your company's administrator set the connector to read-only. Read features keep working. |

## Documentation

How the plugin works, setup and data handling:
[regdoor/README.md](regdoor/README.md)

- Privacy policy: https://app.regdoor.com/policies/privacy_policy (US: https://app.us.regdoor.com/policies/privacy_policy)
- Terms of use: https://app.regdoor.com/policies/terms_of_use (US: https://app.us.regdoor.com/policies/terms_of_use)
