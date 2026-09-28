#!/usr/bin/env python3
"""Audit CS234 lecture-note structure and cross-file state without dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path


UNICODE_SCRIPTS = re.compile("[⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉]")
NUMBERED_H2 = re.compile(r"^##\s+(\d+)\.\s+", re.MULTILINE)
FIRST_TEACHING = re.compile(r"首次完整讲解：Lecture\s+(\d+)\s+§(\d+(?:\.\d+)?)")
REGISTRY_LOCATION = re.compile(r"Lecture\s+(\d+)\s+§(\d+(?:\.\d+)?)")
PATH_IN_BACKTICKS = re.compile(r"`((?:lecture|notes|assignment)/[^`]+\.(?:pdf|md|py))`")
VERIFIED_DATE = re.compile(r"(?:截至|核验日期[:：]?)\s*(\d{4}-\d{2}(?:-\d{2})?)")


def section_exists(text: str, section: str) -> bool:
    pattern = re.compile(rf"^#{{2,6}}\s+{re.escape(section)}(?:\D|$)", re.MULTILINE)
    return bool(pattern.search(text))


def check_note(path: Path, errors: list[str], warnings: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    label = str(path)

    if sum(1 for line in text.splitlines() if line.strip() == "$$") % 2:
        errors.append(f"{label}: unbalanced display-math fences")
    if sum(1 for line in text.splitlines() if line.lstrip().startswith("```") and not line.lstrip().startswith("\\```")) % 2:
        errors.append(f"{label}: unbalanced code fences")
    if UNICODE_SCRIPTS.search(text):
        errors.append(f"{label}: contains Unicode superscript/subscript characters")

    numbers = [int(value) for value in NUMBERED_H2.findall(text)]
    if numbers and numbers != list(range(numbers[0], numbers[0] + len(numbers))):
        errors.append(f"{label}: discontinuous H2 numbering: {numbers}")

    required_groups = {
        "覆盖清单": ("Checklist", "覆盖清单"),
        "Assignment Readiness": ("Assignment Readiness", "Assignment 1 准备度", "准备度"),
        "本讲必会公式": ("本讲必会公式",),
        "容易混淆点": ("容易混淆点",),
        "自测题": ("自测题",),
        "本讲小结": ("本讲小结",),
        "延伸阅读": ("延伸阅读",),
        "经典基础": ("经典基础",),
        "前沿动态": ("前沿动态",),
    }
    for name, variants in required_groups.items():
        if not any(variant in text for variant in variants):
            errors.append(f"{label}: missing required section '{name}'")

    if re.search(r"T\[[^\n]+\]\s*\*\s*V\[[^\n]+\]", text):
        errors.append(f"{label}: suspicious transition/value code uses scalar V[...] instead of a value vector")
    if re.search(r"\bClass\s+[1-7]\b", text):
        errors.append(f"{label}: contains 'Class N', a known contamination of the CS234 Mars Rover example")
    if "前沿动态" in text:
        matches = VERIFIED_DATE.findall(text[text.rfind("延伸阅读") :])
        if not matches:
            errors.append(f"{label}: extended reading lacks a verification date")
        else:
            raw = matches[-1]
            fmt = "%Y-%m-%d" if len(raw) == 10 else "%Y-%m"
            verified = datetime.strptime(raw, fmt).date()
            age = (date.today() - verified).days
            if age > 100:
                warnings.append(f"{label}: current-reading verification is {age} days old")


def check_state(course_root: Path, errors: list[str]) -> None:
    state = course_root / "notes" / "learning_state.md"
    if not state.exists():
        errors.append(f"{state}: missing")
        return
    text = state.read_text(encoding="utf-8")
    for relative in PATH_IN_BACKTICKS.findall(text):
        if not (course_root / relative).exists():
            errors.append(f"{state}: recorded path does not exist: {relative}")


def check_concept_index(
    course_root: Path,
    notes: list[Path],
    errors: list[str],
) -> set[tuple[str, str]]:
    index = course_root / "notes" / "concept_index.md"
    if not index.exists():
        errors.append(f"{index}: missing")
        return set()

    cache = {path.name: path.read_text(encoding="utf-8") for path in notes}
    locations = set(REGISTRY_LOCATION.findall(index.read_text(encoding="utf-8")))
    for lecture, section in sorted(locations):
        target_name = f"lec{lecture}_notes.md"
        target = cache.get(target_name)
        if target is None:
            errors.append(f"{index}: registry target note is missing: {target_name}")
            continue
        if not section_exists(target, section):
            errors.append(f"{index}: registry target not found: Lecture {lecture} §{section}")
    return locations


def check_first_references(
    notes: list[Path],
    registry_locations: set[tuple[str, str]],
    errors: list[str],
) -> None:
    cache = {path.name: path.read_text(encoding="utf-8") for path in notes}
    for path in notes:
        text = cache[path.name]
        for lecture, section in FIRST_TEACHING.findall(text):
            target_name = f"lec{lecture}_notes.md"
            target = cache.get(target_name)
            if target is None:
                errors.append(f"{path}: first-teaching target note is missing: {target_name}")
                continue
            if not section_exists(target, section):
                errors.append(f"{path}: first-teaching target not found: Lecture {lecture} §{section}")
            if (lecture, section) not in registry_locations:
                errors.append(f"{path}: first-teaching target is not registered: Lecture {lecture} §{section}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--course-root",
        type=Path,
        default=Path("/Users/nyvo/course/cs234"),
    )
    args = parser.parse_args()
    course_root = args.course_root.resolve()
    notes_dir = course_root / "notes" / "lec_notes"
    notes = sorted(notes_dir.glob("lec*_notes.md"))

    errors: list[str] = []
    warnings: list[str] = []
    if not notes:
        errors.append(f"{notes_dir}: no lecture notes found")
    for note in notes:
        check_note(note, errors, warnings)
    check_state(course_root, errors)
    registry_locations = check_concept_index(course_root, notes, errors)
    check_first_references(notes, registry_locations, errors)

    for message in warnings:
        print(f"WARNING: {message}")
    for message in errors:
        print(f"ERROR: {message}")

    if errors:
        print(f"Audit failed: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1
    print(f"Audit passed: {len(notes)} note(s), {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
