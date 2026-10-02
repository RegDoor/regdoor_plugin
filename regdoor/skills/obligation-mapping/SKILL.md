---
name: obligation-mapping
description: "Obligation map applied to the user's company via RegDoor. Use automatically, without a command, for 'which obligations apply to us', 'what must we comply with to operate as a PSAV, CASP or VASP', compliance checklist, gap analysis against a rule, impact or classification of a new rule for the company. Triggers (pt/en): quais obrigações se aplicam a nós, checklist de compliance, gap analysis, o que precisamos cumprir, impacto de regra nova; obligation mapping, what a new rule means for us. Combines the Company Vault (company.md, risk_profile.md) with topic skills and cited database text; outputs a table with source, status and applicability."
---

# Obligation mapping

Follow `regdoor-routing`. This skill adds the company dimension.

## Work

1. **Company first.** From the injected Company Vault, extract: legal entities, licenses /
   authorizations held or sought, products, jurisdictions, client portfolio, and the
   `risk_profile.md` classification scale. If a needed file is marked NOT INCLUDED, load it.
   If the company vault is empty, ask the user two things only: activity/modality and jurisdiction.
2. **Route and load.** Consultant → the topic that maps *general* obligations for the regime
   (e.g. `topic-psav-obrigacoes-gerais` for Brazil) → the subtopic for the company's modality
   (custodiante / intermediária / corretora, CASP class, …) → AML/CFT topic when relevant.
3. **Retrieve every obligation you list.** One `search_regulatory_content(contents_uuid=[…])`
   per instrument in the topic's normative chain, `limit` 10–20, query on the obligation theme
   ("governança", "segregação de ativos", "capital mínimo", "comunicação ao COAF", "prazo").
4. **Classify** each obligation for this company: applies / applies with conditions / does not
   apply / undefined (regulator has not ruled). Use `risk_profile.md` to state the notification
   action owed when the user asks about a *new* development.

## Answer

Open with two sentences: which regime and modality you assumed for the company, and the
instruments in scope with their status.

Then one table (headers in the user's language):

| Obligation | Source | Rule status | Applies to the company | Practical note |
|---|---|---|---|---|

- **Source**: `[Res. BCB 520/2025](https://app.regdoor.com/library/detail/<content_uuid>) (art. 12)` (library link per the citation rule in `regdoor-routing`, region host included)
- **Rule status**: one label from the status table in `regdoor-routing`
- **Applies**: Yes / Yes, with conditions / No / Undefined
- **Practical note**: deadline, who in the company owns it, dependency on another norm

After the table: 3–5 sentences, drafted with `regulatory-style`, on the items that need a
decision (undefined, conditional) and what may still change (open consultations, bills). If any
item came from web sources, say so.

This is a decision-oriented deliverable: close with *"Regulatory intelligence only, not legal advice."*

## Do not

- List an obligation you did not retrieve from the database in this conversation.
- Mix modalities silently: if the company holds more than one, produce one table per modality.
- Turn "undefined" into "not applicable".
- Disclose the company's risk classification rules to third parties in shared outputs; they are
  internal to the company.
- Mention vault coverage, skill names or routing steps to the user.
