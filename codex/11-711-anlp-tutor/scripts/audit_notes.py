#!/usr/bin/env python3
"""Audit 11-711 notes, concept back-references, and source mappings."""

from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path


SECTION_RE = re.compile(r"^#{2,4}\s+(\d+(?:\.\d+)*)(?:\.)?\s+(.+?)\s*$", re.MULTILINE)
BACKREF_RE = re.compile(
    r"首次完整讲解：Lecture\s+(\d+)\s+§(\d+(?:\.\d+)*)「([^」]+)」"
)
INDEX_TARGET_RE = re.compile(
    r"\|[^\n|]+\|\s*Lecture\s+(\d+)\s+§(\d+(?:\.\d+)*)「([^」]+)」\s*\|"
)
LOCAL_PATH_RE = re.compile(
    r"`((?:slides|code|assignments)/[^`\s]+?\.(?:pdf|md|py|ipynb|json|txt))`"
)


class Audit:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, path: Path, message: str) -> None:
        self.errors.append(f"ERROR {path}: {message}")

    def warn(self, path: Path, message: str) -> None:
        self.warnings.append(f"WARN  {path}: {message}")


def lecture_number(path: Path) -> int | None:
    match = re.match(r"0*(\d+)-", path.name)
    return int(match.group(1)) if match else None


def parse_sections(text: str) -> dict[str, str]:
    return {section: title.strip() for section, title in SECTION_RE.findall(text)}


def find_attention_signature(path: Path) -> list[str] | None:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except (OSError, SyntaxError):
        return None
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == "Attention":
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) and item.name == "compute_query_key_value_scores":
                    return [arg.arg for arg in item.args.args]
    return None


def audit_note(audit: Audit, course_root: Path, path: Path, text: str) -> None:
    required = ["本讲主线", "快速导航", "覆盖检查清单", "Assignment Readiness", "延伸阅读"]
    for marker in required:
        if marker not in text:
            audit.error(path, f"missing required marker: {marker}")

    if text.count("$$") % 2:
        audit.error(path, "unbalanced display-math delimiters ($$)")
    fence_count = sum(1 for line in text.splitlines() if line.lstrip().startswith("```"))
    if fence_count % 2:
        audit.error(path, "unbalanced fenced code blocks")

    top_sections = [int(value) for value in re.findall(r"^##\s+(\d+)\.\s+", text, re.MULTILINE)]
    if top_sections and top_sections != list(range(1, max(top_sections) + 1)):
        audit.error(path, f"non-continuous H2 numbering: {top_sections}")

    for line_number, line in enumerate(text.splitlines(), start=1):
        if r"\propto s_\theta" in line and not ("课件" in line and "简写" in line):
            audit.error(path, f"line {line_number}: score-to-probability shorthand lacks exp() caveat")

    forbidden = {
        "code/05_transformers/attention.py": "invented course code path",
        "compute_query_key_value_scores(self, Q, K, V, mask)": "stale assignment signature",
    }
    for pattern, message in forbidden.items():
        if pattern in text:
            audit.error(path, f"{message}: {pattern}")

    for relative in sorted(set(LOCAL_PATH_RE.findall(text))):
        if not (course_root / relative).exists():
            audit.error(path, f"referenced local source does not exist: {relative}")


def audit_assignment_reference(audit: Audit, course_root: Path, skill_root: Path) -> None:
    reference = skill_root / "references" / "assignments-and-assessment.md"
    if not reference.exists():
        audit.error(reference, "missing assignment reference")
        return
    text = reference.read_text(encoding="utf-8")
    required_symbols = [
        "LayerNorm._norm",
        "compute_query_key_value_scores",
        "LlamaLayer.forward",
        "Llama.generate",
        "apply_rotary_emb",
        "AdamW.step",
        "generate_addition_data",
        "train_one_epoch",
        "evaluate_loss",
    ]
    for symbol in required_symbols:
        if symbol not in text:
            audit.error(reference, f"Assignment 1 inventory omits {symbol}")

    llama_path = course_root / "assignments" / "assignment1_code" / "llama.py"
    if llama_path.exists():
        args = find_attention_signature(llama_path)
        if args is None:
            audit.error(llama_path, "cannot locate Attention.compute_query_key_value_scores")
        elif args != ["self", "query", "key", "value"]:
            audit.warn(llama_path, f"attention signature changed; refresh reference: {args}")
    else:
        audit.warn(llama_path, "assignment source missing; skipped signature check")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--course-root", type=Path, required=True)
    args = parser.parse_args()

    course_root = args.course_root.expanduser().resolve()
    skill_root = Path(__file__).resolve().parent.parent
    notes_root = course_root / "notes"
    note_dir = notes_root / "lec_notes"
    audit = Audit()

    note_paths = sorted(note_dir.glob("*.md")) if note_dir.exists() else []
    if not note_paths:
        audit.error(note_dir, "no lecture notes found")

    notes_by_lecture: dict[int, tuple[Path, str, dict[str, str]]] = {}
    for path in note_paths:
        text = path.read_text(encoding="utf-8")
        audit_note(audit, course_root, path, text)
        number = lecture_number(path)
        if number is not None:
            notes_by_lecture[number] = (path, text, parse_sections(text))

    index_path = notes_root / "concept_index.md"
    registered: set[tuple[int, str]] = set()
    if not index_path.exists():
        audit.error(index_path, "missing concept index")
    else:
        index_text = index_path.read_text(encoding="utf-8")
        for lecture, section, title in INDEX_TARGET_RE.findall(index_text):
            key = (int(lecture), section)
            registered.add(key)
            note = notes_by_lecture.get(int(lecture))
            if note is None:
                audit.error(index_path, f"target lecture note missing: Lecture {lecture} §{section}")
            elif section not in note[2]:
                audit.error(index_path, f"target section missing: Lecture {lecture} §{section}「{title}」")

    for path, text, _sections in notes_by_lecture.values():
        for lecture, section, title in BACKREF_RE.findall(text):
            key = (int(lecture), section)
            target = notes_by_lecture.get(int(lecture))
            if target is None or section not in target[2]:
                audit.error(path, f"unresolved first-teaching reference: Lecture {lecture} §{section}「{title}」")
            elif key not in registered:
                audit.error(path, f"back-reference is not registered in concept_index.md: Lecture {lecture} §{section}")

    state_path = notes_root / "learning_state.md"
    if not state_path.exists():
        audit.error(state_path, "missing learning state")
    else:
        state = state_path.read_text(encoding="utf-8")
        for relative in re.findall(r"`(lec_notes/[^`]+\.md)`", state):
            if not (notes_root / relative).exists():
                audit.error(state_path, f"missing note referenced by state: {relative}")
        for stale in ("已完整学习", "✅ 完成"):
            if stale in state:
                audit.error(state_path, f"coverage/mastery conflation remains: {stale}")

    protocol_path = notes_root / "learning_protocol.md"
    if not protocol_path.exists():
        audit.error(protocol_path, "missing learning protocol")

    audit_assignment_reference(audit, course_root, skill_root)

    for message in audit.errors + audit.warnings:
        print(message)
    if audit.errors:
        print(f"Audit failed: {len(note_paths)} note(s), {len(audit.errors)} error(s), {len(audit.warnings)} warning(s).")
        return 1
    print(f"Audit passed: {len(note_paths)} note(s), 0 error(s), {len(audit.warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
