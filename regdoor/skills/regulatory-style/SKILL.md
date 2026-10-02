---
name: regulatory-style
description: "Writing and review layer of the RegDoor plugin. Use when drafting, rewriting, reviewing or formatting a regulatory answer, policy advice, regulatory report, regulatory update, newsletter or comparison — after regdoor-routing and the use-case skill have retrieved the sources. Covers legal modality (must, may, must not), procedural status, mechanism and actor-specific consequence, parenthetical provision locators, acronym expansion, the informational-value test and delivery registers. Do not use for routing or searching; do not use for grammar-only edits without regulatory substance."
---

# Master Regulatory and Policy Style

## RegDoor plugin context

This skill is the writing and review layer of the RegDoor plugin. Routing and retrieval are
done by `regdoor-routing` (consultant → topic → regulator → scoped search) and by the use-case
skill; do not repeat or replace that procedure here. The RegDoor database is the primary source
universe; official web sources come only after the database path is exhausted and are cited as
*(Web Page)*.

Citation format, the status vocabulary and the disclaimer rule are defined once, in the
"Citation and status" section of `regdoor-routing`. Where a list in these references differs from
that section, that section prevails.

Produce clear institutional analysis without overstating the law, the evidence, or the practical consequence.

## Select the task

Classify the request as one or more of:

1. analysis or answer;
2. rewrite or review;
3. regulatory update; or
4. comparison.

Select the requested delivery register separately from analytical depth. A policy advice, regulatory report, regulatory update, newsletter or news item, and comparison may require the same underlying legal work even though their ordering and language differ. Use [output-patterns.md](references/output-patterns.md) for that selection.

Follow the user's requested language, scope, length, audience, and output format. Preserve the predominant language when the user does not specify one.

## Set the analytical depth

Use the least intensive level that can answer responsibly:

1. **Editorial:** improve supplied text without expanding its factual or legal record.
2. **Regulatory-analytical:** explain status, architecture, mechanism, affected actors, uncertainty, and practical consequence.
3. **Provision-level legal-regulatory:** analyze a specific instrument or rule when the conclusion turns on its scope, wording, conditions, amendments, timing, obligations, prohibitions, permissions, exceptions, supervision, or enforcement.

Do not add provision-level formality to a conceptual explanation or style-only rewrite unless the legal distinction changes the answer.

## Load the required guidance

- Read [analytical-method.md](references/analytical-method.md) when the task requires substantive classification, mechanism, consequence, comparison, or compression.
- Read [legal-regulatory-quality.md](references/legal-regulatory-quality.md) for provision-level legal-regulatory work.
- Read [research-and-citations.md](references/research-and-citations.md) when using, checking, or citing sources, resolving a material gap, or assessing a claim that may have changed.
- Read [output-patterns.md](references/output-patterns.md) for a regulatory update, rewrite, comparison, or another requested delivery form whose structure must be adapted.

## Execute the workflow

1. Identify the object, actors, jurisdiction, relevant period, audience, and intended decision.
2. Select the analytical depth and load its required guidance.
3. Separate the instrument or technology, entity, regulated activity, use case, and jurisdictional perimeter when those distinctions matter.
4. Determine the legal or procedural status before stating the conclusion.
5. For provision-level work, map the operative rule and distinguish obligations, prohibitions, permissions or faculties, exceptions, conditions, alternatives, procedures, and supervisory powers that affect the conclusion.
6. Determine the document chain needed for the conclusion. For an amendment, inspect both the amending instrument and the affected base text; follow cross-references only when they are material to scope, meaning, status, or consequence. Never paraphrase a legal definition incorporated from another instrument unless you inspected and can identify the controlling provision; otherwise preserve the defined term and disclose the limitation.
7. Decide whether the task is limited to supplied material or requires current research. Use the RegDoor tools when a material claim may have changed; use official web sources only after the database path is exhausted.
8. Associate each material claim with adequate evidence. Verify that the cited provision actually addresses the proposition attributed to it, and distinguish the instrument's subject, the change it makes, and the analytical consequence.
9. Distinguish confirmed facts, reasoned inferences, and unresolved facts. Narrow or qualify the conclusion when the available source set is insufficient.
10. Explain the operative mechanism: identify the obligation, permission, process, cost, risk, liability, or bottleneck that changes.
11. Convert the analysis into a concrete consequence for the affected actors.
12. Choose the smallest structure that makes the answer clear.

## Resolve material gaps before limiting the answer

A gap is material when resolving it could change legal or procedural status, covered actors, normative modality, conditions, exceptions, timing, consequences, or the conclusion. Resolve it proportionately before qualifying the answer, following [research-and-citations.md](references/research-and-citations.md). If it remains unresolved, narrow the conclusion and identify only the missing substantive legal or factual basis.

## Isolate the finished deliverable

Treat audience, length, format, research instructions, identifiers, and retrieval context as execution parameters, not content. Unless expressly requested as part of the deliverable or materially necessary to evaluate the legal conclusion, do not mention the user, prompt, request, word limit, formatting instruction, research cutoff, UUID or other internal identifier, file path, research tool, database, search method, system coverage, or retrieval failure.

When methodology or a source universe must be disclosed, describe it substantively, such as `official Banco Central do Brasil instruments`, rather than naming the tool or internal repository used to retrieve it. Incorporate corrections directly into the analysis and state unresolved limitations in legal, impersonal terms.

## Maximize informational value

Prefer affirmative, direct formulations that state what the instrument does. Use a negative formulation only when it corrects a likely misconception or preserves a material legal distinction. Each sentence must add material information about nature, scope, mechanism, actor, condition, status, consequence, uncertainty, or evidence; remove or integrate a sentence whose deletion would not change the legal understanding or the reader's decision.

Do not preserve a negative contrast or background inventory merely because it appears in a source draft. When an amendment applies only named provisions of a broader base regime, identify the incorporated duties and stop; do not list every excluded chapter or control unless one exclusion affects the decision. For a regulatory update, name the concrete operative mechanism in the first substantive paragraph; a statement that the perimeter expands is incomplete when the amendment also creates or applies a specific hold, deadline, control, or procedure.

In a rewrite, `preserve the content` means preserve material legal propositions and supported consequences, not every sentence, example, historical detail, contrast, or inventory in the source. Identify the decision-driving mechanism from the entire source and move it to the opening even when the source introduces it later. Do not use the source paragraph order as the default analytical order.

State the legally material timing once. Give the commencement or compliance date when it affects the conclusion. Omit the act date, gazette publication date, research cutoff, and a separate `published but not yet enforceable` restatement unless one independently changes validity, applicability, temporal comparison, or the requested decision. Limit the base instrument, history, and inventories of controls or dates to what is needed to understand the principal change. Concision must not remove a material condition, exception, source, provision locator, legal qualification, acronym explanation, or actor-specific consequence.

## Apply mandatory language rules

- Expand every acronym or initialism at its first occurrence: write the full term followed by the shortened form in parentheses. Briefly explain its role when expansion alone would not make it clear. Expand a non-obvious abbreviation when needed for the intended reader; conventional legal notation such as `art.`, `§`, and `nº` need not be mechanically rewritten.
- Start with the core issue or answer, not a generic introduction.
- For a regulatory update, identify the instrument, principal change, and operative mechanism in the first substantive paragraph. Add commencement there only when it changes present or future obligations; do not add publication history or cutoff-based status narration merely because the dates are known. Integrate a necessary correction without allowing it to displace the main development.
- Use inline `(i)`, `(ii)`, `(iii)`, and at most `(iv)` when two to four parallel legal elements must be distinguished in the same analytical passage, such as cumulative requirements, alternative triggers, successive duties, exceptions, or separate powers. Introduce what the enumeration decomposes and preserve the logical relationship among its elements. Do not label the whole set cumulative when a later duty arises only if a separate event occurs; state the primary duty and the conditional trigger separately. Do not add numbering when it would not improve legal comprehension.
- In analytical prose, place material article, paragraph, item, and sub-item locators in parentheses next to the proposition they support, such as `(art. 3º)`, `(art. 88, § 2º)`, or `(arts. 1º, 4º e 6º-A)`. Make the rule, change, actor, condition, or consequence the grammatical subject; do not lead a sentence with the locator or use `O art. ...` as its default sentence frame. Preserve article markers inside direct quotations and formal citation fields when changing them would alter the quoted or requested format.
- Use the shortest parenthetical locator that remains unambiguous. Identify the instrument inside the locator when multiple acts, an amendment relationship, or an unclear antecedent could cause misattribution. Once the source is clear, do not repeat the same instrument or provision in successive sentences when one locator can support the cohesive passage without weakening traceability.
- When one article supports a compact enumeration or a cluster of related sentences, consolidate its caput, items, paragraphs, or other subdivisions into one locator at the end of that unit instead of citing the article after each element. Consolidation must not omit a different provision that independently supports status, commencement, scope, an exception, or another material proposition.
- Before delivering provision-level prose, scan narrative sentences for locator forms such as `art.`, `artigo`, `arts.`, `§`, `parágrafo`, `inciso`, `item`, and `alínea`. Recast every material numbered locator inside parentheses unless it appears in a direct quotation or user-required formal citation structure.
- Use precise institutional prose and define a technical term when the intended audience may not know it.
- Explain a legal term that materially defines the rule's scope or mechanism for a non-specialist audience. If the operative text incorporates that definition from another instrument, retrieve and identify the controlling provision; if it cannot be retrieved, say that the term is defined elsewhere and do not improvise its meaning.
- Avoid hype, vague claims, rhetorical flourishes, and unsupported legal conclusions.
- Treat formulaic phrases and headings as optional logic, never as text to repeat mechanically.

## Protect factual and legal integrity

- Never invent a source, citation, article, authority, license, date, obligation, status, or hyperlink.
- Never describe a proposal, consultation, guidance document, pilot, supervisory expectation, or private statement as binding law.
- State the relevant limitation when facts, jurisdiction, sources, or access are insufficient.
- Present conditional analysis when the conclusion depends on missing facts.
- Do not broaden a style-only rewrite beyond the supplied material unless the user asks for verification or the task cannot be completed responsibly without flagging a material uncertainty.

## Final check

Before delivering, confirm that the response:

- answers the real issue, leads a regulatory update with the principal change and mechanism, and explains the actor-specific consequence;
- preserves legal nature, status, modality, conditions, exceptions, attribution, uncertainty, and other propositions material to the conclusion;
- includes only decision-useful timing and does not reproduce publication history or cutoff-based status narration without independent legal relevance;
- uses a source set and parenthetical provision locators sufficient to support each material claim without invention or mechanical repetition;
- expands every acronym or initialism on first use, explains its role when needed, and defines a material technical or legal term for the intended reader; and
- follows the requested format while keeping the user, prompt, execution parameters, internal retrieval process, and unauthorized external mutations outside the deliverable.
