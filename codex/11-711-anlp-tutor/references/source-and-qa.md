# Source and QA Standard

Use this reference whenever course claims, formulas, code, PDFs, external readings, or artifacts are inspected or written.

## Contents

1. Source precedence and provenance
2. PDF and slide handling
3. Code and assignment fidelity
4. Mathematical and tensor QA
5. Modern context and extended reading
6. Note and state QA
7. Failure handling

## 1. Source precedence and provenance

Apply the most task-specific source first.

### Assignment task

1. current local assignment writeup;
2. assignment README and checklist;
3. tests and starter code;
4. lecture slides and official readings;
5. course notes;
6. external references.

Tests and starter code govern executable signatures and shapes. A prose summary must not override the live TODOs.

### Lecture or concept task

1. relevant local slide deck;
2. official course-provided code/notebook;
3. official main readings listed for that class;
4. existing notes and concept index;
5. external primary sources.

Notes are retrieval aids, not authority over the PDF or code.

### Provenance labels

Use explicit labels when needed:

- `课件定义` or `课件示例`;
- `配套代码`;
- `Assignment 要求`;
- `课程指定阅读`;
- `自拟例子`;
- `外部补充（截至 YYYY-MM-DD 核实）`;
- `助教推断`.

If the slide is shorthand or appears wrong, preserve what it says, state the correction separately, and show the check that justifies the correction.

## 2. PDF and slide handling

1. Inspect page count and extract text with a PDF tool.
2. Follow the slide order unless a concept answer requires a targeted lookup.
3. Render a page to an image when equations, arrows, diagrams, tables, or column groupings are ambiguous in extracted text.
4. When summarizing a table, preserve its row/column grouping and units.
5. Cite slide page numbers when a claim or assignment mapping benefits from traceability.
6. Do not infer an absent equation, architecture edge, or experimental result from a slide title.

## 3. Code and assignment fidelity

Before writing a code mapping:

1. verify that the path exists;
2. read the enclosing class/function and its callers;
3. copy the exact function name and signature;
4. derive shapes from the live code/config, not a generic implementation;
5. use notebook cell number plus a unique symbol/comment when line numbers are unstable;
6. quote source verbatim in a block labeled `代码映射`;
7. label all adapted snippets `改写示例` or `自拟实现骨架`.

Do not invent `.py` files for concepts that exist only in a notebook. Use approximate line numbers only after checking the current file.

For assignments, inventory every `TODO`, `NotImplementedError`, required output, and test before declaring a component complete. Compare the inventory to the README because summary writeups can omit application modules.

## 4. Mathematical and tensor QA

For every nontrivial formula:

- define the domain of each variable;
- identify the normalization or reduction axis;
- distinguish score, probability, log-probability, loss, and estimator;
- state averaging denominators and ignored/masked positions;
- check boundary cases such as zero probability or empty masks;
- verify a numeric example independently.

For every tensor trace:

- define axis order once, for example `(batch, heads, sequence, head_dim)`;
- verify matrix multiplication axes;
- distinguish a physical copy from broadcast/logical reuse;
- separate parameter memory, activation memory, KV cache, gradients, and optimizer states;
- state dtype when converting element counts to bytes.

Never call a model configuration “real” without a primary source or a checked local config. Prefer a clearly labeled small invented example when the exact model is irrelevant.

## 5. Modern context and extended reading

The course's official main readings come before optional web additions because they are part of the intended learning path and can be assessed.

For a lecture note, use this order:

1. `课程指定阅读`;
2. `经典基础` when it adds an origin or fuller derivation;
3. `现代延伸` with at most 2–4 directly relevant sources;
4. `动手资源` only when it supports an immediate practice task.

Do not force a source from every lab, region, model family, or framework into every lecture. Relevance beats coverage of the industry landscape.

Browse when a claim is time-sensitive, uncertain, or concerns a current model/tool. Prefer primary sources: original papers, official model cards, official documentation, or the course site. Confirm that each link resolves and supports the surrounding claim. Stamp only material actually rechecked in the current pass.

Use cautious language for proprietary systems. Publicly observed behavior does not prove a private training recipe or product architecture. State resource assumptions for claims such as “fits on one GPU”.

## 6. Note and state QA

Before declaring lecture coverage complete, check:

- the note follows the PDF's major topic order;
- its checklist describes coverage rather than mastery;
- all first-teaching locations are registered;
- every explicit first-teaching back-reference resolves;
- formulas, code fences, and display-math fences are balanced;
- code paths and signatures still exist;
- Assignment Readiness lists components separately;
- reading entries are relevant and accurately described;
- `learning_state.md` says coverage, practice, mastery, and readiness separately;
- `confusions.md` separates user confusion from tutor watch items.

Run `scripts/audit_notes.py` after writes. Treat a clean audit as necessary but not sufficient: manually inspect source fidelity and pedagogy.

## 7. Failure handling

- If PDF text is unreliable, render the relevant page; request a screenshot only if local rendering is impossible.
- If code is missing, search the local course tree before checking the official linked repository.
- If an upstream repository differs from the local assignment snapshot, report the version difference and use the source the user placed in scope.
- If a fact cannot be verified, omit it or label the uncertainty; do not fill gaps from memory.
- If a reference file required by the main Skill is unavailable, follow the core rules in `SKILL.md` and disclose the missing resource.
