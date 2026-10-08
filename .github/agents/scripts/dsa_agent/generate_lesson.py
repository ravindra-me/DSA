"""Generates one complete lesson into a staging directory.

Nothing in the repository is touched here. The staging directory contains:

    <staging>/day-NNN/...   the complete lesson folder
    <staging>/record.json   the progress entry to merge (see update_progress)

Flow: lesson outline (1 AI call) -> for each problem: solution + starter +
tests (1 AI call) -> sandboxed validation -> up to N repair rounds -> render
Markdown -> final whole-lesson validation.
"""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

from . import __version__, log, schema
from .ai import Provider, complete_json
from .config import Settings
from .errors import ValidationFailed
from .fsutil import atomic_write_json, write_text
from .languages import LanguageProfile, get_profile
from .prompts import render
from .render import (
    problem_json_for_prompt,
    problem_paths,
    render_exercise,
    render_readme,
    render_solution_notes,
)
from .sandbox import Sandbox
from .select_topic import LessonPlan
from .validate_solution import (
    CheckResult,
    ProblemCode,
    problem_files,
    sha256,
    validate_lesson_dir,
    validate_problem,
)

RECORD_FILE = "record.json"
RECORD_SCHEMA = 1


def _revision_guidance(plan: LessonPlan) -> str:
    if plan.kind != "revision":
        return (
            "This is the learner's FIRST lesson on this topic: teach it from scratch, assume no prior "
            "knowledge of it, and build intuition before formal details."
        )
    return (
        f"This is a REVISION lesson (revision stage {plan.revision_stage}). The learner studied this topic "
        "before. Keep the concept explanation a concise but complete recap focused on the core invariants and "
        "the most common mistakes, then spend more effort on NEW, more challenging problems that combine this "
        "topic with others the learner already knows."
    )


def generate_lesson(
    settings: Settings, plan: LessonPlan, provider: Provider, sandbox: Sandbox, staging: Path
) -> Dict[str, Any]:
    profile = get_profile(settings.language)
    system = render(settings.prompts_dir, "system", {})
    attempts = settings.ai.max_attempts

    with log.group(f"Generating lesson outline: Day {plan.day}, {plan.topic.title}"):
        lesson_prompt = render(
            settings.prompts_dir,
            "lesson",
            {
                "day": plan.day,
                "topic_title": plan.topic.title,
                "topic_id": plan.topic.id,
                "phase_title": plan.topic.phase_title,
                "concepts": ", ".join(plan.topic.concepts) or plan.topic.title,
                "lesson_type": "revision" if plan.kind == "revision" else "new topic",
                "learned_topics": ", ".join(plan.learned_topics) or "none yet (this is the first lesson)",
                "language": profile.display_name,
                "revision_guidance": _revision_guidance(plan),
                "problem_count": plan.problem_count,
                "difficulties": ", ".join(plan.difficulties),
                "previous_problems": "; ".join(plan.previous_problems) or "none",
                "language_conventions": profile.conventions,
            },
        )
        lesson = complete_json(
            provider, system, lesson_prompt,
            lambda p: schema.validate_lesson(p, plan.problem_count), "lesson outline", attempts,
        )
        log.info(f"Outline OK: {lesson['title']} with problems: " + "; ".join(p["title"] for p in lesson["problems"]))

    problems: List[Dict[str, Any]] = []
    for number, spec in enumerate(lesson["problems"], 1):
        problem = {
            **spec,
            "number": number,
            "difficulty": plan.difficulties[number - 1],
            "paths": problem_paths(profile, number),
        }
        with log.group(f"Problem {number}/{plan.problem_count}: {problem['title']} ({problem['difficulty']})"):
            code, stats = _generate_problem(settings, plan, profile, provider, sandbox, system, problem)
        problems.append({**problem, "code": code, "stats": stats})

    day_dir = staging / plan.slug
    _write_lesson(settings, plan, profile, lesson, problems, day_dir, provider)

    with log.group("Validating the assembled lesson"):
        result = validate_lesson_dir(day_dir, sandbox, settings.min_tests_per_problem)
        log.info(result.report)
        if not result.ok:
            raise ValidationFailed(f"assembled lesson failed validation: {result.report}")

    entry = {
        "day": plan.day,
        "date": plan.date,
        "topic": plan.topic.id,
        "topicTitle": plan.topic.title,
        "phase": plan.topic.phase_title,
        "kind": plan.kind,
        "revisionStage": plan.revision_stage,
        "difficulty": plan.difficulty,
        "language": profile.name,
        "status": "generated",
        "problemsGenerated": len(problems),
        "problemsCompleted": 0,
        "problems": [
            {"number": p["number"], "title": p["title"], "difficulty": p["difficulty"], "concept": p["concept"]}
            for p in problems
        ],
        "conceptsCovered": lesson["conceptsCovered"],
        "path": f"{settings.lessons_dir.name}/{plan.slug}",
        "generatedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "generationId": uuid.uuid4().hex,
        "generator": {"provider": provider.name, "model": provider.model, "agentVersion": __version__},
        "requestRevision": False,
    }
    record = {"schemaVersion": RECORD_SCHEMA, "mode": plan.mode, "extraLesson": plan.extra, "slug": plan.slug, "reason": plan.reason, "entry": entry}
    atomic_write_json(staging / RECORD_FILE, record)
    return record


def _generate_problem(
    settings: Settings,
    plan: LessonPlan,
    profile: LanguageProfile,
    provider: Provider,
    sandbox: Sandbox,
    system: str,
    problem: Dict[str, Any],
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    number = problem["number"]
    common = {
        "day": plan.day,
        "topic_title": plan.topic.title,
        "number": number,
        "language": profile.display_name,
        "language_conventions": profile.conventions,
        "solution_file": profile.solution_file(number),
        "test_file": profile.test_file(number),
        "exports": ", ".join(problem["exports"]),
        "problem_json": problem_json_for_prompt(problem),
        "min_tests": settings.min_tests_per_problem,
    }
    prompt = render(
        settings.prompts_dir,
        "problem",
        {
            **common,
            "difficulty": problem["difficulty"],
            "starter_hint": profile.starter_hint,
            "timeout": settings.sandbox.timeout_seconds,
        },
    )
    code = complete_json(provider, system, prompt, schema.validate_problem, f"problem {number}", settings.ai.max_attempts)

    min_tests = settings.min_tests_per_problem
    max_repairs = settings.max_repair_attempts
    diagnoses: List[str] = []
    for attempt in range(max_repairs + 1):
        candidate = ProblemCode(number, problem["exports"], code["solutionCode"], code["testCode"], code["starterCode"])
        missing = schema.check_exports_defined(candidate.solution, candidate.exports)
        if missing:
            result = CheckResult(False, f"solutionCode does not define the exported symbol(s): {', '.join(missing)}")
        else:
            result = validate_problem(profile, sandbox, candidate, min_tests)
        if result.ok:
            log.info(f"Problem {number} validated: {result.report}" + (f" after {attempt} repair(s)" if attempt else ""))
            return code, {"testsRun": result.tests_run, "repairs": attempt, "diagnoses": diagnoses}

        # Never let a repair delete tests: future rounds must keep at least as many.
        min_tests = max(min_tests, result.tests_run)
        if attempt == max_repairs:
            raise ValidationFailed(
                f"problem {number} ('{problem['title']}') still fails validation after {max_repairs} repair attempt(s):\n"
                f"{result.report}"
            )
        log.warn(f"Problem {number} failed validation (repair {attempt + 1}/{max_repairs}): {result.report[:2000]}")
        repair_prompt = render(
            settings.prompts_dir,
            "repair",
            {
                **common,
                "title": problem["title"],
                "solution_code": _fenced(profile, code["solutionCode"]),
                "starter_code": _fenced(profile, code["starterCode"]),
                "test_code": _fenced(profile, code["testCode"]),
                "failure": f"```text\n{result.report[-6000:]}\n```",
                "attempt": attempt + 1,
                "max_attempts": max_repairs,
                "min_tests": min_tests,
            },
        )
        repaired = complete_json(provider, system, repair_prompt, schema.validate_repair, f"repair {number}", settings.ai.max_attempts)
        log.info(f"Repair diagnosis: {repaired['diagnosis']}")
        diagnoses.append(repaired["diagnosis"])
        code = {**code, **{k: repaired[k] for k in ("solutionCode", "testCode", "starterCode")}}
    raise AssertionError("unreachable")


def _fenced(profile: LanguageProfile, code: str) -> str:
    return f"```{profile.fence}\n{code}\n```"


def _write_lesson(
    settings: Settings,
    plan: LessonPlan,
    profile: LanguageProfile,
    lesson: Dict[str, Any],
    problems: List[Dict[str, Any]],
    day_dir: Path,
    provider: Provider,
) -> None:
    day_path = f"{settings.lessons_dir.name}/{plan.slug}"
    meta_problems = []
    for p in problems:
        code = p["code"]
        files = problem_files(profile, ProblemCode(p["number"], p["exports"], code["solutionCode"], code["testCode"], code["starterCode"]))
        for rel, content in files.items():
            write_text(day_dir / rel, content)
        solution_source = files[p["paths"]["solution"]]
        write_text(day_dir / p["paths"]["exercise"], render_exercise(plan, p, profile))
        write_text(day_dir / p["paths"]["notes"], render_solution_notes(p, code, solution_source, profile))
        meta_problems.append(
            {
                "number": p["number"],
                "title": p["title"],
                "difficulty": p["difficulty"],
                "concept": p["concept"],
                "exports": p["exports"],
                "files": p["paths"],
                "starterSha256": sha256(files[p["paths"]["practice"]]),
                "testsRun": p["stats"]["testsRun"],
                "repairs": p["stats"]["repairs"],
            }
        )
    write_text(day_dir / "README.md", render_readme(plan, lesson, problems, profile, day_path))
    write_text(
        day_dir / "lesson.json",
        json.dumps(
            {
                "schemaVersion": 1,
                "day": plan.day,
                "date": plan.date,
                "topic": plan.topic.id,
                "kind": plan.kind,
                "language": profile.name,
                "generator": {"provider": provider.name, "model": provider.model, "agentVersion": __version__},
                "problems": meta_problems,
            },
            indent=2,
            ensure_ascii=False,
        ),
    )
