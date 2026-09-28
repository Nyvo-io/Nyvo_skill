# CS234 Teaching Standard

Use this file as the single detailed authority for teaching depth, first appearances, algorithms, repetition, and teaching-quality review. Source fidelity and note structure remain governed by `source-and-qa.md` and `note-schema.md`.

## 1. Choose Teaching Depth

Give a **first full teaching** when an item is new in `notes/concept_index.md`, formally introduced by the lecture, required as an unstated prerequisite, or reported as unfamiliar by the learner.

Treat an item as a **repeat** when the registry points to an earlier usable explanation and the learner has not requested reteaching.

Scale the response to the item:

- routine vocabulary: a short natural clarification;
- substantive concept or distinction: role, definition, operational evidence, and boundary;
- formula or algorithm: complete inputs, update or calculation, output, and interpretation;
- theorem: assumptions, claim, what is not guaranteed, and a small application or boundary case.

Do not expand every term into the same template. Add examples according to comprehension risk and formula complexity, not once per slide, symbol, or line. Do not create separate examples for every line of one coherent derivation; one complete shared example may serve the chain.

## 2. Teach a New Concept or Formula

Make the item usable before the next paragraph relies on it:

1. **Identify it.** Name it naturally as `中文术语（English term）` and state its mathematical type when relevant: scalar, function, mapping, operator, estimator, assumption, or property.
2. **Place it in the story.** Explain why it appears now, what problem it solves, and how it changes or repackages the preceding idea.
3. **Make it operational.** Give the definition or formula, add the semantic reading required below when applicable, identify inputs and output, then immediately show the smallest calculation, trajectory, or before/after result needed to use it.
4. **Close the loop.** Interpret the result and state one important contrast, assumption, edge case, or likely misreading.

At the first display of an important theorem or multi-part formula, immediately read the whole relation in connected Chinese before moving to derivation, notation caveats, or boundary conditions. State what local quantity is computed, what weights it, how terms are summed or averaged, and what the final output means. Keep this semantic reading to one or two sentences by default, using a third only when the formula has genuinely separate stages. Do not paraphrase every symbol or repeat conclusions that the next paragraph already explains; it is not a symbol glossary and does not need a fixed heading such as `白话解释`. Use the local order `formula -> semantic reading -> technical qualifications or derivation -> nearby concrete evidence`.

Use connected Chinese prose rather than mechanically printing labels such as `直觉`、`白话解释` and `符号解释`. A translation, symbol list, or phrase such as “直觉上很简单” is not a usable first teaching.

For time-indexed formulas, state the reward-timing and horizon convention first. Distinguish sample from expectation, arbitrary estimate from converged target, scalar from vector, state value from action value, and action from policy.

## 3. Teach an Algorithm

Do not require the learner to reconstruct purpose and dataflow from pseudocode. Use this sequence when the algorithm first matters:

1. State what earlier mechanisms it combines and what new capability the loop produces.
2. Give a three-to-six-step overview in ordinary Markdown.
3. Summarize the dataflow in one compact line or Obsidian callout.
4. Contrast the nearest predecessor only when the comparison clarifies why the new loop is needed.
5. Expand initialization, inputs, update order, conditions, outputs, and repetition rules; render mathematical updates under the step that uses them.
6. Run one complete iteration or episode and explain what feeds into the next iteration.

Fenced pseudocode is a secondary reference, never the primary explanation. Do not use a `text` fence merely to create a gray panel. Keep a fenced block only for literal executable code, terminal output, a compact raw trace, or syntax-sensitive material whose indentation matters. If source pseudocode is retained, introduce its variables and explain the same control flow before the block.

After the section, the learner should be able to answer: what is the loop for, what happens first, what changes, and what is used by the next iteration?

## 4. Require Concrete Evidence

Concrete evidence must be:

- **minimal**: no larger than needed to expose the idea;
- **specific**: actual states, actions, probabilities, rewards, values, or parameters;
- **complete**: all relevant intermediate steps are shown;
- **consistent**: notation and indexing match the surrounding section;
- **interpreted**: the computed result is explained.

For formulas, substitute values. For processes, show the necessary state-action-reward-next-state sequence. For comparisons, hold unrelated variables fixed.

Verify named course environments against the PDF or code. Do not borrow a course environment's name for constructed data. When provenance could be confused, identify it as `说明用数据，非课件原例`; otherwise, let the example title describe its teaching function rather than labeling it mechanically.

For concrete evidence, prefer an Obsidian `example` Callout with a descriptive title:

```markdown
> [!example] 具体计算：...
> 已知条件与问题。
>
> $$
> 代入与计算
> $$
>
> 结果及其与概念的关系。
```

Choose titles such as `具体计算`、`直观例子`、`反例对比`、`边界情况` or `风险链条` according to purpose. Keep one complete shared example for a coherent formula chain instead of manufacturing a separate example for every line. Every nontrivial example should state the known conditions, show the necessary intermediate steps, report the result, and interpret what it demonstrates. In a Callout, prefix every paragraph and every line of a display formula with `>` so Obsidian renders the entire block correctly.

## 5. Handle Repeats and the Registry

Start a later appearance with:

```markdown
*首次完整讲解：Lecture N §x.y「标题」。本节只补充：本次新增内容。*
```

Then give only the reminder, notation change, assumption, role, contrast, or consequence needed here. Repeat the full teaching only when the learner explicitly remains unfamiliar; keep the original first-location citation.

Maintain `notes/concept_index.md` as the authority:

- add an entry only after subsection numbering is stable;
- use a stable concept ID and searchable Chinese, English, abbreviation, and symbolic aliases;
- do not move the first location merely because a later explanation is better;
- verify every `首次完整讲解` line against the registry.

## 6. Run the Natural-Language Pass

Run this pass only after source coverage, mathematics, examples, and section order are stable. Review connected paragraphs rather than replacing isolated sentences. Natural prose is not casual prose: preserve technical density, formal distinctions, equations, citations, and the learner's established notation.

- Remove empty stage directions such as “本节将介绍”“下面来看” or “值得注意的是” when the next sentence can state the actual relation directly.
- Connect paragraphs through the real relation between ideas: prerequisite, cause, contrast, update, consequence, or boundary. Do not manufacture flow with the same generic transition at every paragraph.
- Use prose for a continuous explanation. Keep lists for genuinely parallel items, ordered procedures, checks, or comparisons; merge shallow one-line bullets that force the learner to reconstruct the argument.
- Avoid a repeated template of rhetorical heading, definition, “换句话说”, example, and summary. Vary the structure according to what the concept needs, and do not restate the same conclusion in body text, a Callout, a table, and the section ending.
- Prefer specific subjects and verbs: name which estimate, parameter, policy, distribution, or condition changes and what follows. Remove vague praise, artificial suspense, forced triads, and promotional contrasts that add no technical content.
- Preserve accepted terminology. Introduce an important term as `中文术语（English term）`, then use a concise, consistent form. Keep conventional English algorithm names, abbreviations, and phrases when translating them into everyday Chinese would weaken precision; explain their role instead of renaming them.
- Read formula-level semantic explanations as ordinary technical Chinese: keep a clear subject and action, remove clause stacking and translation-like phrasing, and do not make every formula begin with the same stock sentence such as “这个公式表示”。
- Read the finished section once from start to end. Fix consecutive paragraphs that begin the same way, abrupt changes of subject, sentence fragments, and overloaded sentences, while retaining useful emphasis and deliberate Obsidian Callouts.

This pass is a manual semantic review. Do not enforce it with brittle counts of sentence length, headings, English words, bold text, or Callouts; those forms are problems only when they do not serve the teaching.

## 7. Teaching-Quality Review

Before declaring a note complete, inspect every primary teaching section and confirm:

- the purpose and relation to preceding material appear before dense notation;
- every new mathematical object has a clear type, input, and output;
- the first display of an important theorem or multi-part formula is followed by a short, natural Chinese reading of the whole relation before technical qualifications;
- each nontrivial formula has nearby concrete evidence and an interpretation;
- each algorithm is narrative-first, with explicit update order and one complete iteration;
- fenced blocks are used for content that benefits from monospace formatting, not as a substitute for explanation;
- course content, derived explanation, invented data, and external connection are distinguishable;
- the natural-language pass removed scaffolding and repetition without colloquializing technical terms or changing meaning;
- repeats and concept-index locations are consistent.

A structural audit can check syntax and references but cannot prove that an explanation is understandable. This manual review remains required.
