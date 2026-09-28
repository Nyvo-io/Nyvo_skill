# Lecture Note and Learning-State Schema

## Contents

1. Note layers
2. Required sections
3. Concept ownership and structural coherence
4. Coverage and mastery
5. Concept index
6. Self-tests and assignment readiness

## 1. Note Layers

Make a long note navigable through three layers:

1. **快速主线**: five to ten bullets explaining what problem the lecture solves and how its major concepts connect.
2. **核心讲解**: use PDF order as the coverage spine, but locally group source items into coherent concept blocks under Section 3; fully teach first appearances and briefly reference repeats.
3. **复习与扩展**: formulas, confusion points, self-test, assignment readiness, and extended reading.

Keep derivations and examples complete, but avoid repeating the same derivation in the summary, core section, formula list, and conclusion. Formula lists should point back to their first full explanations.

## 2. Required Sections

Use continuously numbered top-level sections. Include:

- `0. 本讲覆盖清单`
- `1. 本讲主线` or an equivalent quick map
- teaching sections that cover every source item, with local regrouping allowed under Section 3
- `Assignment Readiness`
- `本讲必会公式`
- `容易混淆点`
- `自测题`
- `本讲小结`
- final `延伸阅读`, with `经典基础` and `前沿动态`

At the top, record:

```text
来源：lecture path, course offering, instructor
笔记规范：cs234-rl-tutor v2
外部资料核验日期：YYYY-MM-DD（only when external material is present）
```

## 3. Concept Ownership and Structural Coherence

Before drafting headings, assign every substantive concept or algorithm one **primary teaching section**. That section owns its definition, mechanics, main derivation, and complete example. Other sections may preview it or reuse it, but must not create a second disconnected full introduction.

Treat a major section title as a teaching contract. A section about MC may mention that TD will provide a bootstrapped alternative, but it should not interrupt the MC explanation with a full TD lesson. Teach TD in its own primary section, then place the detailed MC-versus-TD comparison after both methods are usable.

Apply this priority order: complete PDF coverage first, conceptual coherence and prerequisite flow second, original PDF order third. Preserve complete coverage without mechanically copying slide order into the note outline:

- Locally regroup or reorder source items when an animation, comparison slide, or recap appears before the source formally teaches all of its ingredients.
- At an early comparison, explain only the already-taught side and give at most a short forward pointer for the unfamiliar side; move the full comparison to the later primary section.
- At a later repeat, back-reference the primary section and add only the new role, assumption, or consequence.
- Keep source page references and the coverage checklist in PDF order, and record the destination note section for every regrouped item so no source content disappears during reordering.

During final QA, scan the collapsed Outline rather than only reading paragraphs. If one core concept has two nonadjacent full-teaching clusters, or a section repeatedly leaves its named topic to teach a future algorithm, merge the material into its primary section and leave a concise cross-reference behind.

## 4. Coverage and Mastery

Use the lecture checklist only for **source coverage**. A checked item means the note contains the material; it does not mean the learner has mastered it.

In `notes/learning_state.md`, maintain separate fields:

```text
Coverage: not started | in progress | complete
Mastery evidence: none recorded | quiz | explanation | derivation | implementation | assignment
```

Do not write “mastered” without concrete evidence. If no evidence was collected, say so plainly.

## 5. Concept Index

Maintain `notes/concept_index.md` with this table shape:

```markdown
| ID | 概念 | Aliases | 首次完整讲解 | 备注 |
|---|---|---|---|---|
| return | 回报（Return） | $G_t$, discounted return | Lecture 1 §15.2 | total-length convention |
```

The concept index is the authority for `首次完整讲解` back-references. Update it after subsection numbering stabilizes and before final QA.

## 6. Self-Tests and Assignment Readiness

Write self-test questions before answers. Prefer putting answers in collapsible Markdown so the learner can attempt retrieval first:

```markdown
<details>
<summary>查看答案</summary>

答案与推理。

</details>
```

In `Assignment Readiness`, separate:

- prerequisite topics already covered;
- remaining prerequisite topics;
- mastery evidence already observed;
- recommended next action.

Use `现在可以开始写 Assignment X。` only when the prerequisite material is covered. Clarify that this means “ready to begin,” not “already able to solve every part without practice.”
