"""Validation of AI responses. Each validator returns a cleaned copy of the
payload or raises ValueError with a message the model can act on.

The model never chooses file names or paths: those are derived from problem
numbers by the agent, so a response cannot write outside the lesson folder.
"""

from __future__ import annotations

from typing import Any, Dict, List, Sequence

from .languages import IDENTIFIER


def _text(obj: Dict[str, Any], key: str, where: str, min_len: int = 1) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or len(value.strip()) < min_len:
        raise ValueError(f"{where}.{key} must be a non-empty string" + (f" (at least {min_len} chars)" if min_len > 1 else ""))
    return value.strip()


def _texts(obj: Dict[str, Any], key: str, where: str, min_items: int = 1) -> List[str]:
    value = obj.get(key)
    if not isinstance(value, list) or len(value) < min_items or not all(isinstance(v, str) and v.strip() for v in value):
        raise ValueError(f"{where}.{key} must be a list of at least {min_items} non-empty strings")
    return [v.strip() for v in value]


def _obj(obj: Dict[str, Any], key: str, where: str) -> Dict[str, Any]:
    value = obj.get(key)
    if not isinstance(value, dict):
        raise ValueError(f"{where}.{key} must be an object")
    return value


def validate_lesson(payload: Dict[str, Any], problem_count: int) -> Dict[str, Any]:
    w = "lesson"
    concept = _obj(payload, "concept", w)
    complexity = _obj(payload, "complexity", w)
    interview = payload.get("interview")
    if not isinstance(interview, list) or len(interview) < 3:
        raise ValueError("lesson.interview must be a list of at least 3 {question, answerHint} objects")
    problems = payload.get("problems")
    if not isinstance(problems, list) or len(problems) < problem_count:
        raise ValueError(f"lesson.problems must contain exactly {problem_count} problems")

    lesson = {
        "title": _text(payload, "title", w),
        "summary": _text(payload, "summary", w, 40),
        "objectives": _texts(payload, "objectives", w, 3),
        "concept": {
            key: _text(concept, key, f"{w}.concept", 40)
            for key in ("whatItIs", "whyItExists", "whenToUse", "whenNotToUse", "howItWorks")
        },
        "commonMistakes": _texts(concept, "commonMistakes", f"{w}.concept", 2),
        "realWorldApplications": _texts(concept, "realWorldApplications", f"{w}.concept", 2),
        "example": _text(payload, "example", w, 40),
        "visual": _text(payload, "visual", w, 10),
        "complexity": {
            "time": _text(complexity, "time", f"{w}.complexity"),
            "space": _text(complexity, "space", f"{w}.complexity"),
            "notes": _text(complexity, "notes", f"{w}.complexity"),
        },
        "interview": [
            {
                "question": _text(item, "question", f"{w}.interview[{i}]"),
                "answerHint": _text(item, "answerHint", f"{w}.interview[{i}]"),
            }
            for i, item in enumerate(interview)
            if isinstance(item, dict) or _fail(f"{w}.interview[{i}] must be an object")
        ],
        "conceptsCovered": _texts(payload, "conceptsCovered", w, 1),
        "problems": [_problem_spec(p, i) for i, p in enumerate(problems[:problem_count])],
    }
    titles = [p["title"].lower() for p in lesson["problems"]]
    if len(set(titles)) != len(titles):
        raise ValueError("lesson.problems must have distinct titles")
    return lesson


def _problem_spec(raw: Any, index: int) -> Dict[str, Any]:
    w = f"lesson.problems[{index}]"
    if not isinstance(raw, dict):
        raise ValueError(f"{w} must be an object")
    examples = raw.get("examples")
    if not isinstance(examples, list) or not examples:
        raise ValueError(f"{w}.examples must be a non-empty list")
    exports = raw.get("exports")
    if (
        not isinstance(exports, list)
        or not 1 <= len(exports) <= 6
        or not all(isinstance(e, str) and IDENTIFIER.match(e) for e in exports)
        or len(set(exports)) != len(exports)
    ):
        raise ValueError(f"{w}.exports must be a list of 1-6 distinct valid identifiers")
    return {
        "title": _text(raw, "title", w),
        "concept": _text(raw, "concept", w),
        "statement": _text(raw, "statement", w, 40),
        "input": _text(raw, "input", w),
        "output": _text(raw, "output", w),
        "constraints": _texts(raw, "constraints", w, 1),
        "examples": [
            {
                "input": _text(ex, "input", f"{w}.examples[{j}]"),
                "output": _text(ex, "output", f"{w}.examples[{j}]"),
                "explanation": str(ex.get("explanation") or "").strip(),
            }
            for j, ex in enumerate(examples)
            if isinstance(ex, dict) or _fail(f"{w}.examples[{j}] must be an object")
        ],
        "expectedApproach": _text(raw, "expectedApproach", w),
        "signature": _text(raw, "signature", w),
        "exports": list(exports),
    }


def validate_problem(payload: Dict[str, Any]) -> Dict[str, Any]:
    w = "problem"
    complexity = _obj(payload, "complexity", w)
    return {
        "approach": _text(payload, "approach", w, 20),
        "reasoning": _text(payload, "reasoning", w, 20),
        "algorithm": _texts(payload, "algorithm", w, 2),
        "complexity": {"time": _text(complexity, "time", f"{w}.complexity"), "space": _text(complexity, "space", f"{w}.complexity")},
        "edgeCases": _texts(payload, "edgeCases", w, 2),
        "solutionCode": _code(payload, "solutionCode", w),
        "testCode": _code(payload, "testCode", w),
        "starterCode": _code(payload, "starterCode", w),
    }


def validate_repair(payload: Dict[str, Any]) -> Dict[str, Any]:
    w = "repair"
    return {
        "diagnosis": _text(payload, "diagnosis", w),
        "solutionCode": _code(payload, "solutionCode", w),
        "testCode": _code(payload, "testCode", w),
        "starterCode": _code(payload, "starterCode", w),
    }


def _code(obj: Dict[str, Any], key: str, where: str) -> str:
    code = _text(obj, key, where)
    if code.startswith("```"):
        lines = code.splitlines()
        lines = lines[1:-1] if lines[-1].strip().startswith("```") else lines[1:]
        code = "\n".join(lines).strip()
    return code


def _fail(message: str) -> bool:
    raise ValueError(message)


def check_exports_defined(code: str, exports: Sequence[str]) -> List[str]:
    """Names listed as exports that never appear in the code (cheap sanity check)."""
    return [name for name in exports if name not in code]
