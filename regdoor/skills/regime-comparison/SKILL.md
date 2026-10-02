---
name: regime-comparison
description: "Side-by-side comparison via RegDoor. Use automatically, without a command, for 'compare', 'difference between', 'vs', 'which modality to choose', 'passport' and cross-border questions: modalities within one jurisdiction (PSAV custodiante vs intermediária vs corretora; CASP classes), jurisdictions (Brazil vs EU vs UK on stablecoins, custody, travel rule) or rule versions (consultation vs final text). Triggers (pt/en): comparar, diferença entre, qual modalidade escolher; compare, versus. Loads every relevant consultant; dimension-by-dimension table with citations."
---

# Regime comparison

Follow `regdoor-routing` once **per side** of the comparison.

## Work

1. **Fix the axes.** Sides = modalities, jurisdictions or rule versions. Dimensions = what the
   user cares about; default set when unspecified:
   scope / who is covered · authorization or licensing requirement · prudential (capital,
   segregation, insurance) · conduct (KYC, AML/CFT, travel rule) · reporting & governance ·
   consumer protection · timeline & status · sanctions.
2. **Route each side.** For jurisdictions: `global_vault_skills(mode="route", jurisdiction=…)`
   per jurisdiction, load each consultant, then the matching topic per side. For modalities in
   one jurisdiction: one consultant, one subtopic per modality.
3. **Retrieve per side and per dimension.** `search_regulatory_content(contents_uuid=[…],
   query="<dimension theme>", limit=10–15)`. Keep the same `query` wording across sides so the
   comparison is fair.
4. **Record what is not defined.** A regime that has not ruled on a dimension is a finding,
   not a gap to fill with assumptions.

## Answer

One table (headers in the user's language), dimensions as rows, sides as columns:

| Dimension | <Side A> | <Side B> | (<Side C>) |
|---|---|---|---|

Each cell: the rule in one or two sentences + citation + status label (format and labels from
`regdoor-routing`). Write "Not defined" (in the user's language) when the regime is silent, and say so explicitly in the
synthesis. Draft the synthesis with `regulatory-style` (comparison register: thesis first,
repeated dimensions, operational difference last).

After the table: a synthesis paragraph (what is structurally different, what converges, what
each regime has *not yet* defined) and, when the user is choosing between modalities, the
three-part structure: current scenario → interpretation → open considerations.

Close with the disclaimer only when the user is choosing between the options compared (rule in
`regdoor-routing`).

## Do not

- Compare a consultation text against a rule in force without labelling the status in every cell.
- Reuse a UUID from one jurisdiction's skill for another jurisdiction.
- Collapse "not defined" into "not required".
- Mention coverage, vault structure or skill names.
