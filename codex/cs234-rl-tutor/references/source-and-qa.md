# Source Fidelity and Quality Assurance

## Contents

1. Source fidelity
2. Mathematical integrity
3. Code integrity
4. Visual integrity
5. Extended reading
6. Final three-pass review

## 1. Source Fidelity

For each major section, know whether the content is:

- explicitly present in the lecture or assignment;
- a derivation from course definitions;
- explanatory data constructed for teaching;
- a modern connection or analogy.

Do not attribute invented details to the lecture. Before using a named environment, verify its state space, action space, rewards, transition probabilities, terminal behavior, and indexing against the PDF or code.

Prefer small, self-contained examples whose title states their purpose, using an Obsidian `> [!example]` Callout for concrete calculations, contrasts, boundary cases, or risk chains. Do not mechanically label every constructed calculation `自拟例子`; add `说明用数据，非课件原例` only when a reader could mistake it for a named course example. Keep course examples traceable to the PDF or code and preserve their original names only after verification.

When the slide notation is ambiguous, quote or paraphrase the source convention, state the convention adopted in the note, and explain how formulas change under the alternative convention.

## 2. Mathematical Integrity

Before finalizing a formula or derivation, check:

- **type**: scalar, vector, matrix, action, policy, random variable, expectation, or estimator;
- **conditioning**: what is fixed and what randomness is averaged over;
- **indexing**: reward timing, terminal state, total horizon, remaining horizon, and episode index;
- **assumptions**: finite state/action, Markov representation, stationarity, bounded rewards, discounting, or termination;
- **edge cases**: $\gamma=0$, $\gamma=1$, terminal transitions, ties, and unvisited states;
- **units and arithmetic**: substitute numbers and recompute every intermediate value.

For finite-horizon values, use time- or remaining-horizon-dependent notation such as $V_t(s)$ or $V_h(s)$. Use stationary $V(s)$ only when the horizon convention or augmented state makes it valid.

Do not infer an estimator is unbiased merely because a small displayed sample happens to average to the true value. Unbiasedness is an expectation over repeated datasets.

## 3. Code Integrity

Map formulas to the actual starter-code shapes, not remembered conventions. For Assignment 1:

```text
R[state, action]                    scalar
T[state, action, next_state]        transition probability
V[next_state]                       next-state value
T[state, action, :] * V             elementwise vector product before summing
```

Run a minimal numerical test whenever a note includes executable code or a formula-to-code mapping. If the starter repository has tests or a sanity check, run them after implementation.

Never silently replace an entire value vector with `V[state]`, transpose a transition axis, or reverse a transition probability to make an example easier.

## 4. Visual Integrity

Inspect rendered source pages rather than relying only on extracted text. PDF text tools often omit vector diagrams, plots, animations, and spatial relationships.

Embed a visual only when it materially improves understanding. Prefer the final complete frame of an incremental slide sequence; omit decorative art and near-duplicate frames. Preserve the part of the page that carries the concept, including necessary labels, axes, legends, and terminal or boundary markers.

Store extracted or rendered images under `attachments/` with stable descriptive names. Use a resolution that remains legible at the note's intended embed width, place the image adjacent to the explanation it supports, and put it before a table when the table summarizes the image.

Caption each embedded source visual with its relative source path and physical PDF page. Clearly label any crop, annotation, reconstruction, or interpretation added by the note so it is not mistaken for the original course artifact. Before finalizing, confirm that the asset exists, the Obsidian embed resolves, no important content is cropped, and the rendered image is readable.

## 5. Extended Reading

Every completed lecture note ends with two short tiers:

1. **经典基础**: two to four canonical sources directly tied to the lecture's core concepts.
2. **前沿动态**: zero to four genuinely relevant recent primary sources, with the verification date.

Keep the section relevant rather than exhaustive. Do not search every frontier lab or model family for every lecture. It is acceptable to state that no separate frontier item is necessary when adding one would be forced.

Before writing current claims:

- check today's date;
- browse the web;
- prefer papers, official documentation, official repositories, or official lab posts;
- open each cited page and verify that it directly supports the wording;
- avoid unsupported superlatives such as “best,” “first,” or “state of the art” unless the cited source establishes them;
- link an open-source claim to the release or repository, not merely to a model announcement;
- stamp the tier `截至 YYYY-MM-DD 核实`;
- refresh current items when the stamp is older than roughly three months.

Canonical items do not need artificial recency. Bellman, Sutton and Barto, and foundational algorithm papers often belong in `经典基础`; current product announcements do not.

## 6. Final Three-Pass Review

Perform all three passes in order:

### Pass A: Source and Semantics

- Cover every item in the source checklist.
- Verify named examples against source files.
- Recalculate numeric examples.
- Check formula types, assumptions, and indices.
- Verify code against actual shapes and tests.
- Verify embedded visuals against their exact source pages and captions.
- Verify first-teaching references against `notes/concept_index.md`.

### Pass B: Artifact Quality

- Ensure headings and numbering are continuous.
- Ensure math and code fences are balanced.
- Ensure image embeds resolve and remain legible at their specified width.
- Remove Unicode superscripts/subscripts.
- Remove duplicated full explanations of repeated concepts.
- Ensure coverage and mastery are not conflated.
- Ensure the note ends with the required reading tiers and verification stamp.
- Run `scripts/audit_notes.py` and fix every error.

### Pass C: Natural Language

After Passes A and B are stable, run `teaching-standard.md` §6 over each revised teaching section. Read paragraphs in order, remove mechanical scaffolding and duplicated conclusions, and restore explicit logical connections where lists or fragments broke the explanation. Preserve established bilingual terminology, formulas, source attribution, and technical distinctions; naturalness is not permission to replace precise terms with casual paraphrases.
