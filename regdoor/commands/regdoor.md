---
description: RegDoor regulatory intelligence — research, obligations or comparison, with citations
argument-hint: <question in natural language, e.g. what does Res. BCB 520 require from a custodian? | PSAV obligations for us | custodian vs broker>
---

Handle the request below with the RegDoor connector.

1. If the RegDoor tools (`global_vault_skills`, `search_regulatory_content`) are not available, follow the `regdoor-setup` skill and stop.
2. Classify the request and apply the matching skill on top of `regdoor-routing`:
   - a factual question about what a rule says, requires, allows, its status, deadlines, recent publications, a bill or public consultation → `regulatory-research`;
   - "what applies to us / our company", checklist, gap analysis, what a new rule means for the company → `obligation-mapping`;
   - "compare", "vs", "difference between", choosing between modalities, jurisdictions or rule versions → `regime-comparison`.
   When the request mixes types, run `regulatory-research` first and then the other flow on its results. Draft the final text with `regulatory-style`.
3. If the request is empty, ask in one line what the user wants to know and offer the three modes as examples.

Never mention skill names, routing steps or vault coverage in the answer.

Request: $ARGUMENTS
