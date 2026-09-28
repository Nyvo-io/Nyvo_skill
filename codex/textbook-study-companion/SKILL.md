---
name: textbook-study-companion
description: Coordinate long-running, material-grounded textbook study in a local course folder. Use when a learner is studying a textbook, PDF, lecture notes, or manual across sessions and needs durable progress, source-faithful notes, teacher-side practice logs, and adaptive mastery checks alongside course-study-tutor and learn-anything.
---

# Textbook Study Companion

Use this skill as the persistence layer for textbook study. Let `course-study-tutor` manage source materials and complete notes; let `learn-anything` manage adaptive teaching and retrieval. Do not duplicate either skill's lesson content.

## Course folder

At the start of a session, read `progress.md`, `learning_protocol.md`, the active chapter folder, its chapter note, and its matching chapter QA file. Inspect only the source pages required for the current segment. If no course package exists, create this structure:

```text
<course-root>/
  README.md
  progress.md
  learning_protocol.md
  notes/
    chXX/
      chXX-<topic>.md
      chXX-<topic>-qa.md
  attachments/
    chXX/
      fig-<source-figure>.png
```

Treat the supplied textbook or local material as the primary source. Clearly distinguish the source's claims, the tutor's explanation, and any optional application connection.

## Session loop

1. State the current segment and a small mastery target.
2. Before asking about a newly introduced diagram, mechanism, device, or notation, extract the source figure (or its relevant crop) to `attachments/chXX/`, embed it in the chapter note and QA file, then display it and explain the parts, fixed elements, connections, and allowed motion. Do not pose a counting or derivation question that depends on an unseen structure.
3. Teach one source-grounded concept in the material's order.
4. Set the expected answer or rubric before posing a retrieval or transfer question.
5. Give feedback; if the learner is stuck, give the smallest missing idea and retry at a smaller scope.
6. Update the chapter note and `progress.md` before ending the session.
7. Log the teacher-side interaction design in the current chapter's `chXX-<topic>-qa.md`.

Do not mark a segment complete merely because it was explained. Require a source-appropriate demonstration: independent explanation, a calculation, or an application to a new case.

## Status and records

- Mark only the currently active chapter subsection with `（进行中）`.
- When it is finished, remove that suffix; do not add `（已完成）`.
- In the current chapter's QA file, record the prompt, any follow-up prompt, reference answer, teaching intent, and next step.
- Never store the learner's original response unless the learner explicitly asks to retain it.
- Keep facts separated: `progress.md` is current state; chapter notes contain durable explanations; the matching QA file contains the teaching sequence.

## Mathematics and scope

Use `$...$` for inline mathematics and `$$...$$` for display mathematics. Explain key formulas through purpose, symbols, and intuition. Keep terminal/chat output interactive; keep durable detail in the course files. Do not prewrite a whole textbook or substitute generic summaries for reading the active source segment.
