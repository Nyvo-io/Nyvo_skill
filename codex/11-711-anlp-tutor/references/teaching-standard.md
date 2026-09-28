# Teaching Standard

Use this reference for lecture writing, concept explanations, review questions, and pedagogical review.

## Contents

1. Concept lifecycle
2. Teaching patterns by concept type
3. Example quality and formula QA
4. Golden Examples
5. Lecture-note schema
6. Coverage, practice, and mastery

## 1. Concept lifecycle

### First full teaching

Teach an unfamiliar concept as one connected unit:

1. state the exact concept name in Chinese and English;
2. give its precise definition, formula, or operational rule;
3. explain every non-obvious symbol or tensor axis;
4. immediately give the smallest complete concrete example;
5. state the one idea the learner should retain;
6. connect to code or an assignment only when relevant;
7. register the location in `notes/concept_index.md`.

Do not place unrelated background between the formula and its example.

### Repeated concept

Use this exact pattern:

> 首次完整讲解：Lecture 2 §8.1.2「多分类交叉熵损失」。本节只补充：在语言模型中，类别变成词表中的 next token。

Do not repeat the full tutorial unless the learner asks or shows that it was forgotten.

### Forgotten concept

Use this pattern:

> 首次完整讲解：Lecture 2 §8.1.2「多分类交叉熵损失」。你现在记不清，下面重新完整讲解，并换一个语言模型例子。

Keep the original first-teaching location even when reteaching elsewhere.

## 2. Teaching patterns by concept type

### Mathematical or probabilistic concept

Use:

```text
precise definition/formula
→ symbols, domain, normalization, and assumptions
→ immediate numeric example
→ intuition
→ common failure mode
```

Examples: softmax, cross-entropy, KL divergence, perplexity, policy gradient, diffusion objective.

### Algorithmic concept

Use:

```text
problem and invariant
→ ordered steps or pseudocode
→ immediate trace on a tiny input
→ complexity or stopping rule
→ edge cases
```

Examples: BPE merging, beam search, top-p sampling, retrieval, backpropagation.

### Architecture or tensor concept

Use:

```text
what it does and why
→ complete input/intermediate/output shape trace
→ mathematical definition
→ verified code mapping
→ compute/memory trade-off
```

Examples: attention, RoPE, GQA, RNN cells, VQ-VAE, MoE routing.

### Systems concept

Use:

```text
measured bottleneck
→ accounting boundary and baseline numbers
→ technique and changed data flow
→ before/after numbers
→ limitations and when not to use it
```

Examples: quantization, tensor parallelism, KV caching, long-context attention.

Always say whether a memory number means weights only, inference state, optimizer state, or total training memory.

### Empirical or research-method concept

Use:

```text
research question or estimand
→ hypothesis and controls
→ metric and uncertainty
→ tiny worked result or table
→ valid conclusion and invalid overclaim
```

Examples: confidence intervals, ablations, significance tests, evaluation contamination, error analysis.

## 3. Example quality and formula QA

Every instructional example must be:

- **complete**: no hidden step needed to reach the result;
- **concrete**: include actual tokens, probabilities, dimensions, or observations;
- **minimal**: remove details that do not change the concept;
- **typed**: state what each axis, index, or random variable means;
- **sourced**: match a named source, or carry the label `自拟例子`;
- **locally adjacent**: appear immediately after the new definition or formula.

Before publishing a formula, check:

- probability values are nonnegative and normalize on the intended axis;
- log bases and averaging denominators are explicit;
- tensor contractions have compatible shapes;
- train-time and inference-time quantities are not mixed;
- approximate equalities are not presented as identities;
- a slide shorthand is distinguished from the fully normalized expression.

## 4. Golden Examples

### 4.1 Scores to probabilities

**从分数到概率（scores to probabilities）**：若分类 score 可以取任意实数，使用 softmax：

$$
p_\theta(y\mid x)
=
\frac{\exp s_\theta(x,y)}{\sum_{y'}\exp s_\theta(x,y')}.
$$

这里的分母对所有候选类别求和，所以概率总和为 1。

**自拟数值例子**：三个类别的 scores 是 `[2, 1, 0]`。

```text
exp(scores) ≈ [7.389, 2.718, 1.000]
Z           ≈ 11.107
probability ≈ [0.665, 0.245, 0.090]
```

最高 score 的类别概率最高，但其他类别仍保留非零概率。不要把 `p(y|x) ∝ s(x,y)` 当成对任意实数 score 都成立的完整概率定义；完整关系是 `p(y|x) ∝ exp(s(x,y))`。

### 4.2 BPE merge trace

**字节对编码（byte-pair encoding, BPE）**：每轮合并训练语料中频率最高的相邻 token pair。

**自拟例子**：语料编码为：

```text
[a, b, a, b, a]
```

相邻 pair 次数：`(a,b)=2`、`(b,a)=2`。若用固定 tie-break 选择 `(a,b)` 并令新 token 为 `X`，一次合并后的序列是：

```text
[X, X, a]
```

关键点：同一轮要按不重叠匹配执行，且训练得到的合并顺序必须在编码新文本时复用。

### 4.3 GQA shape flow

**分组查询注意力（grouped-query attention, GQA）**：多组 query heads 共享较少的 key/value heads，主要减少自回归推理时的 K/V cache。

**自拟张量例子，不是某个真实模型配置**：

```text
B=1, T=4, hidden_dim=8
query_heads=4, kv_heads=2, head_dim=2

Q: (1, 4, 4, 2)
K: (1, 2, 4, 2)
V: (1, 2, 4, 2)
```

每个 K/V head 服务两个 query heads。为批量计算，可在 head 轴逻辑复用 K/V，使 attention 看到兼容的 4 个 query groups；不要误写成产生了四份独立训练参数。

每个 token 的 K/V cache 元素数：

```text
MHA: 2 × 4 heads × 2 dims = 16
GQA: 2 × 2 heads × 2 dims = 8
```

这个自拟例子把 K/V cache 减半。真实模型配置必须另外查证：Llama 2 70B 使用 GQA；不要把 `32 query heads / 8 KV heads` 称为 Llama 2 7B 的真实配置。历史来源：<https://arxiv.org/abs/2307.09288>。

### 4.4 Verified assignment code mapping

Assignment 1 的 attention TODO 应映射到实际源码：

```text
assignments/assignment1_code/llama.py
Attention.compute_query_key_value_scores(self, query, key, value)
约第 90 行；causal mask 是模块 buffer，不是函数参数。
```

写笔记前重新读取函数签名；行号只能写“约”，函数和参数名必须精确。

## 5. Lecture-note schema

Each lecture note uses this order:

1. title and source scope;
2. `本讲主线一句话`;
3. `快速导航`;
4. `覆盖检查清单`;
5. continuously numbered teaching sections in slide order;
6. concise synthesis and recommended practice;
7. `Assignment Readiness` by component;
8. `延伸阅读`: official course readings first, then canonical or current material that is directly relevant.

Prefer a compact note that supports retrieval. Quote only source fragments needed for code mapping; do not copy entire notebooks. Use a short ASCII trace when a diagram's relationships matter.

## 6. Coverage, practice, and mastery

- Mark **coverage complete** after source and note QA.
- Mark **practice attempted/completed** only after an exercise or implementation attempt.
- Mark **mastery demonstrated** only after the learner explains, derives, predicts, or answers without being shown the result.
- Record confidence by concept when useful; do not convert a completed note into learner mastery.
- Store tutor-anticipated pitfalls under `待回收问题`, and user-reported confusion under `用户疑惑`.
