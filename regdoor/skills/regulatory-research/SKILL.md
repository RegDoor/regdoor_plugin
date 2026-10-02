---
name: regulatory-research
description: "Directed regulatory research with citations via RegDoor. Use automatically, without a command, when the user asks what a rule says, requires or allows, requirements, deadlines, the status of a rule, article lookups, recent publications by a regulator, a bill or a public consultation — on virtual assets, crypto, payments, capital markets or banking, in any jurisdiction. Triggers (pt/en): o que a norma exige, é permitido, qual norma rege, prazo, requisitos para autorização, publicações recentes, projeto de lei, consulta pública; what does the rule say, is X allowed, which norm governs Y. Follows regdoor-routing; short cited answer."
---

# Regulatory research (directed)

Follow `regdoor-routing` steps 0–6. This skill fixes the shape of the work and of the answer.

## Work

1. Route → consultant → topic/subtopic → (org) — all before any search.
2. One `search_regulatory_content` per distinct sub-question, scoped with `contents_uuid`
   from the topic skill. `limit` 5–10. Add a second call with `organization_list` +
   `document_type` only if the first returns nothing relevant.
3. If the question is about *recent* rules: `list_contents(organization_list=…, type_list=…,
   published_from=<7 days ago>, sort_by="released_at")` first, then directed reads.
4. If the question names a bill / PL / consulta pública: `list_events` → `get_event` first.
5. Stop searching when every claim in your draft answer is backed by a retrieved chunk.

## Answer

- **Simple factual** ("what does Art. X say?"): 1–3 paragraphs, no headers.
- **Multi-point** (requirements, deadlines, obligations): short numbered list, each item with
  its citation and status.
- **History / evolution**: chronological prose, no tables.

Draft with `regulatory-style`. Cite as defined in `regdoor-routing` (link on the instrument,
locator in parentheses, one status label per instrument, normative chain named once). If the
database has nothing and you had to use the web, mark those sources *(Web Page)* and say the
official text should be confirmed.

Add the disclaimer only to decision-oriented interpretive answers (rule in `regdoor-routing`);
otherwise state the specific limitation.

## Do not

- Answer from memory when a search is possible.
- Put regulator names, country names or UUIDs in `query`.
- Present a consultation or bill as a rule in force.
- Mention vault coverage, skill names or routing steps to the user.
