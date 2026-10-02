# Research and citations

## Decide whether to research

Use current research when the answer depends on information that may have changed, including legal status, implementation dates, responsible authorities, licensing, enforcement, consultations, official guidance, or company disclosures.

For a rewrite explicitly limited to supplied material, do not silently expand the factual record. Preserve the source's scope and flag a material claim that cannot be supported from the supplied record.

If the source set remains insufficient after a proportionate attempt, identify the missing substantive basis and narrow the conclusion without describing tool access or the internal research process.

## Resolve material gaps proportionately

Before disclosing an evidentiary limitation:

1. State internally the pending proposition and the evidence needed to support it.
2. Treat the gap as material if it could change legal or procedural status, covered actors, normative modality, conditions, exceptions, timing, consequences, or the conclusion.
3. For an imprecise instrument identifier, search the issuer's record across instrument types, dates, subjects, and current or historical status. Do not infer identity from recency, topic, or numbering alone; retain multiple plausible matches until the intended act is supported.
4. For any other material gap, search the RegDoor database first (scoped `search_regulatory_content`, `list_contents`, `list_events`) and official sources afterwards for the controlling document, provision, definition, version, or fact.
5. Validate the result against the pending proposition. Confirm the document, version, provision, subject, modality, and conditions; retrieval of a related document does not resolve the gap.
6. Expand the search only while another source could materially change or qualify the conclusion. Stop when the proposition is supported, reasonable authoritative avenues are exhausted, or further research would be disproportionate to the requested decision.

If the gap remains unresolved, omit the unsupported claim or narrow, condition, or qualify the conclusion. Identify the missing legal definition, controlling provision, official status, actor-specific fact, or other substantive basis. Do not describe who failed to provide it, which system lacks it, or how retrieval failed.

Research under this skill is read-only.

## Use the source hierarchy

Prefer, in order appropriate to the claim:

1. legislation, regulation, gazettes, court materials, and official registers;
2. regulator, central bank, ministry, parliament, government, and other public-authority materials;
3. consultation papers, official guidance, supervisory statements, and legislative trackers;
4. company materials for claims about that company's product, reserves, strategy, or public position;
5. qualified secondary analysis for interpretation or context; and
6. media for reported developments or market context, not as the primary basis for a legal claim when an official source is available.

Match the source to the proposition. A company source cannot establish its own legal status merely by asserting it. A media report cannot turn a proposal into law.

## Build a sufficient source set

Use the smallest source set that is sufficient for the requested conclusion, not the smallest set that merely mentions the topic.

- For an amending instrument, inspect the amendment and the affected base text or an official consolidated version.
- Follow a cross-reference when it determines the governed actor, activity, definition, condition, exception, timing, procedure, or supervisory consequence used in the answer.
- Do not paraphrase an incorporated legal definition from general knowledge. Retrieve the controlling definition or preserve the term with a specific source limitation.
- Inspect an enabling law or higher-level act only when the answer depends on competence, hierarchy, perimeter, or validity; do not add it as ceremonial background.
- Use an official explanatory document only for context it actually supplies. Do not let a summary replace the operative text for a legal proposition.
- Stop expanding the chain when additional documents would not change or qualify a material claim.

Before drafting, record internally which source supports each material proposition. If no available source supports a proposition at the required level, narrow it, label it as an inference, or identify the missing document.

## Verify claim-to-source fit

For each material legal claim, confirm:

1. the cited document is the right instrument and version;
2. the cited provision addresses the stated subject;
3. the legal modality and conditions have not been changed in paraphrase;
4. the claim is not broader than the provision; and
5. an analytical consequence is presented as analysis rather than as wording of the norm.

If the claim defines a legal term, verify whether the cited provision defines it directly or incorporates a definition from another instrument. Cite or identify the controlling definition when the paraphrase affects scope.

When explaining an amendment, distinguish what the base norm already governed, what the amendment changes, and what operational consequence follows. Do not attribute the entire amended regime to the amending act.

## Verify status and freshness

- Check the document date, effective date, amendment history, implementation schedule, and current procedural position when material.
- Use an `as of` date when the status is time-sensitive.
- Distinguish the date of publication, adoption, commencement, compliance, transition, and expiration.
- Follow cross-references to the controlling instrument when an announcement or summary is not legally sufficient.

Verification does not require reproducing every verified date in the deliverable. Include only dates that change validity, applicability, temporal comparison, compliance, or the requested decision. Keep a research cutoff outside the body unless methodology is requested or the cutoff is itself necessary to understand the conclusion.

## Cite clearly

- Link directly to the source when the output format supports hyperlinks.
- Name the source in the body or source list; do not dump raw URLs.
- Place citations close to the claims they support.
- Identify the legal or procedural basis precisely enough for the reader to locate it.
- Keep legal basis, factual basis, and reported market context distinct.
- Do not cite a source that does not support the associated claim.

Use labels such as `Legal basis`, `Source basis`, or `Procedural status` only when they improve clarity.

## Keep research infrastructure out of the deliverable

- Apply audience, length, paragraph count, formatting, and research instructions without announcing them in the finished analysis.
- Do not expose UUIDs, internal record identifiers, file paths, search queries, tools, databases, repository names, retrieval mechanics, or system-coverage gaps.
- Incorporate an imprecise document name or status correction directly. Do not say that the user, prompt, request, supplied reference, or located record used the wrong description.
- Preserve genuine identification uncertainty. When more than one real act could match an imprecise label, identify the alternatives and condition the analysis rather than selecting one without adequate evidence.
- When methodology, a cutoff, or a source universe is expressly requested or legally material, disclose it without naming internal infrastructure. Prefer `official BCB instruments current through 19 August 2026` to a tool or database name.
- State an evidentiary limitation as a substantive legal boundary. Prefer `The covered class cannot be determined without the definition in the base regulation` to references to an excerpt, supplied record, available source set, located document, retrieved material, missing upload, search failure, RegDoor, another internal system, or a statement that a provision was not examined, accessed, verified, or reproduced.
- If an expressly requested independent verification cannot be performed, keep that execution note outside the policy advice when the interaction supports a separate status message. Never suggest that direct review was independent verification.
