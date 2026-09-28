# Assignments and Assessment

Use this reference for assignment coaching, component readiness, research exercises, quizzes, exams, and mastery tracking.

## Contents

1. General assignment workflow
2. Assignment 1 verified inventory
3. Assignment 2 workflow
4. Assignments 3 and 4 workflow
5. Lecture-to-task readiness
6. Quiz, exam, and mastery workflow

## 1. General assignment workflow

Always re-read the local writeup, README/checklist, tests, and live TODOs before coaching. The lists below are routing aids, not replacements for the files.

For each component:

1. state the concrete deliverable and its source;
2. map the minimum prerequisite concepts to exact lecture sections;
3. inspect the actual signature, input/output shapes, and caller expectations;
4. explain the concept and a small example before implementation details;
5. build or debug in small testable steps;
6. run the narrowest relevant test, then the integration check;
7. record practice separately from mastery.

Report readiness per component:

```text
ready now | can preview | concept missing | source/code missing | attempted | test passing
```

Do not say an entire assignment is unavailable when some components are already teachable.

## 2. Assignment 1 verified inventory

Read at minimum:

```text
assignments/assignment1.md
assignments/assignment1_code/README.md
assignments/assignment1_code/checklist.md
assignments/assignment1_code/llama.py
assignments/assignment1_code/rope.py
assignments/assignment1_code/optimizer.py
assignments/assignment1_code/addition_data_generation.py
assignments/assignment1_code/addition_run.py
```

The Spring 2026 local snapshot contains these implementation areas:

| File | Symbol or area | Main concepts | Narrow check |
|---|---|---|---|
| `llama.py` | `LayerNorm._norm` | mean, variance, epsilon, affine scale/bias | `sanity_check.py` |
| `llama.py` | `Attention.compute_query_key_value_scores(query, key, value)` | scaled dot-product attention, causal mask | `sanity_check.py` |
| `llama.py` | `LlamaLayer.forward` | pre-norm block, residual paths, attention, FFN | `sanity_check.py` |
| `llama.py` | `Llama.generate` top-p branch | temperature, sorting, cumulative probability, sampling | generation checks |
| `rope.py` | `apply_rotary_emb` | complex/2-D rotations, broadcasting, position | `rope_test.py` |
| `optimizer.py` | `AdamW.step` | moments, bias correction, decoupled weight decay, clipping | `optimizer_test.py` |
| `addition_data_generation.py` | `generate_addition_data` | unique commutative pairs, formatting | direct unit examples |
| `addition_run.py` | `train_one_epoch`, `evaluate_loss` | shifting targets, masking question tokens, CE loss | short training/eval run |

Re-scan `NotImplementedError` and TODO markers because line numbers and required areas can change.

### Accurate attention mapping

In the checked local snapshot, the signature is:

```python
Attention.compute_query_key_value_scores(self, query, key, value)
```

It is near line 90. The causal mask is stored on the module and applied inside the computation; it is not a fourth `mask` parameter.

### Readiness by lecture

- Lecture 2: embeddings, neural-network and gradient foundations.
- Lecture 3: autoregressive objective, logits, cross-entropy, sampling loop, training basics.
- Lecture 4: useful sequence-model context, not a hard dependency for every A1 TODO.
- Lecture 5: core transformer block, attention, LayerNorm/RMSNorm distinction, residuals, RoPE, GQA.
- Lecture 9: top-p and other decoding algorithms.
- AdamW: combine the assignment's stated algorithm with Lecture 3 optimization foundations; do not invent a later dedicated lecture prerequisite.

After Lecture 5, most architecture TODOs and the addition training pipeline can be attempted even if top-p still awaits Lecture 9.

## 3. Assignment 2 workflow

Read `assignments/assignment2.md`, `assignments/assignment2_code/README.md`, and the provided leaderboard queries before choosing an architecture.

Treat it as an end-to-end factual QA system:

```text
data acquisition
→ parsing and provenance
→ chunking/indexing
→ sparse/dense/hybrid retrieval
→ context construction
→ generation
→ citation/error analysis
→ evaluation
```

Lecture 10 is the direct conceptual anchor. Lectures 5–7 help explain the generator and prompting but should not be treated as absolute blockers for building a retrieval baseline.

Use a small end-to-end baseline before adding complexity. Measure retrieval recall separately from answer quality so retrieval and generation failures are not conflated. Verify current assignment constraints before recommending libraries or external services.

## 4. Assignments 3 and 4 workflow

For the original assignment specification, read `assignments/assignment3_4.md` before every major decision.

### Proposal

- define a falsifiable question rather than a broad theme;
- organize literature by problem, assumptions, method, evidence, and limitations;
- choose a competitive reproducible baseline;
- estimate compute, data, evaluation, and schedule;
- distinguish an observed gap from a speculative opportunity.

### Baseline reproduction

- follow the stated baseline and data constraints;
- match the reported setup before modifying it;
- generate the required predictions locally;
- compare results with uncertainty and document deviations;
- perform error analysis before proposing improvements.

The checked Spring 2026 brief says that scaling down the baseline architecture is not permitted. Do not recommend a smaller baseline as if it satisfied the original assignment. For personal study, a reduced experiment is fine only when explicitly labeled `自学改编版`, not as completion of the original specification.

### Full project

- define baselines and ablations before running the main experiment;
- keep evaluation conditions comparable;
- report negative results and uncertainty honestly;
- connect each conclusion to a table, plot, or qualitative analysis;
- separate completed evidence from future work.

## 5. Lecture-to-task readiness

Use concept-level dependencies rather than rigid lecture gates.

| Task | Direct anchor | Helpful earlier/later material |
|---|---|---|
| A1 language-model objective and generation loop | Lecture 3 | Lecture 9 for top-p |
| A1 transformer architecture | Lecture 5 | Lectures 2–4 foundations |
| A1 optimizer and addition training | assignment algorithm + Lectures 2–3 | Lecture 5 for model internals |
| A2 RAG | Lecture 10 | Lectures 5–7, 9 |
| evaluation and error bars | Lecture 13 | Lecture 14 experimental design |
| proposal and reproduction | Lectures 13–14 plus topic lectures | current primary literature |
| RL for language models | Lectures 16–17 | Lecture 3 LM objective, Lecture 8 fine-tuning |
| efficiency work | Lectures 19–23 | Lecture 5 architecture, Lecture 9 inference |

When a user asks “现在可以开始吗？”, answer with a component table and the smallest productive next step.

## 6. Quiz, exam, and mastery workflow

The course includes quizzes and an exam, so assessment is a core tutor mode.

### Build a review set

1. collect covered concepts from `notes/concept_index.md`;
2. include slide material and official main readings assigned to those classes;
3. sample across definition, derivation, shape tracing, algorithm execution, comparison, and error diagnosis;
4. do not reveal solutions before the learner commits to an answer;
5. grade the reasoning, then give a targeted reteach and a transfer question.

### Mastery evidence

Use these labels:

- `not assessed`;
- `recognizes with cues`;
- `recalls independently`;
- `applies to a new example`;
- `explains trade-offs and failure modes`.

Update mastery only from observed responses. A checked coverage list or copied derivation is not mastery evidence.
