"""Validation of generated code.

A problem is accepted only if ALL of these hold:
  1. static safety checks pass on the solution, tests and starter stub
  2. the tests pass against the reference solution (in the sandbox)
  3. at least `minTestsPerProblem` tests actually ran
  4. the tests FAIL against the unimplemented starter stub, which proves they
     really exercise the solution instead of passing vacuously
"""

from __future__ import annotations

import hashlib
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence

from .errors import AgentError
from .fsutil import read_json, write_text
from .languages import LanguageProfile, check_rules, get_profile, strip_header
from .sandbox import Sandbox

MAX_CODE_CHARS = 200_000


@dataclass(frozen=True)
class ProblemCode:
    number: int
    exports: Sequence[str]
    solution: str
    tests: str
    starter: str


@dataclass(frozen=True)
class CheckResult:
    ok: bool
    report: str
    tests_run: int = 0


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def problem_files(profile: LanguageProfile, code: ProblemCode) -> Dict[str, str]:
    """Final on-disk content of a problem's code files, keyed by path in the day folder."""
    solution_file = profile.solution_file(code.number)
    return {
        f"solutions/{solution_file}": profile.assemble_solution(code.exports, code.solution),
        f"tests/{profile.test_file(code.number)}": profile.assemble_tests(code.number, code.exports, code.tests),
        f"practice/{solution_file}": profile.assemble_solution(code.exports, code.starter),
    }


def static_issues(profile: LanguageProfile, code: ProblemCode, check_starter: bool = True) -> List[str]:
    issues: List[str] = []
    parts = [("solution", code.solution, profile.solution_rules), ("tests", code.tests, profile.test_rules)]
    if check_starter:
        parts.append(("starter", code.starter, profile.solution_rules))
    for label, text, rules in parts:
        if not text.strip():
            issues.append(f"{label}: is empty")
        elif len(text) > MAX_CODE_CHARS:
            issues.append(f"{label}: is too large ({len(text)} characters)")
        issues.extend(f"{label}: {reason}" for reason in check_rules(text, rules))
    return issues


def _write_tree(root: Path, files: Dict[str, str]) -> None:
    for rel, content in files.items():
        write_text(root / rel, content)


def validate_problem(
    profile: LanguageProfile, sandbox: Sandbox, code: ProblemCode, min_tests: int
) -> CheckResult:
    issues = static_issues(profile, code)
    if issues:
        return CheckResult(False, "Static safety checks failed:\n" + "\n".join(f"- {i}" for i in issues))

    with tempfile.TemporaryDirectory(prefix="dsa-validate-") as tmp:
        root = Path(tmp)
        _write_tree(root, problem_files(profile, code))
        command = profile.command(profile.single_test_arg(code.number))

        run = sandbox.run(root, profile.image, profile.host_command, command, {"DSA_SOLUTIONS_DIR": "{root}/solutions"})
        if not run.ok:
            reason = "timed out" if run.timed_out else f"exit code {run.exit_code}"
            return CheckResult(False, f"Tests failed against the reference solution ({reason}). Output:\n{run.output}")
        count = profile.count_tests(run.output)
        if count is None:
            return CheckResult(False, f"Could not determine how many tests ran. Output:\n{run.output}")
        if count < min_tests:
            return CheckResult(False, f"Only {count} tests ran; at least {min_tests} are required.", count)

        stub = sandbox.run(root, profile.image, profile.host_command, command, {"DSA_SOLUTIONS_DIR": "{root}/practice"})
        if stub.ok:
            return CheckResult(
                False,
                "The tests PASS against the unimplemented starter stub, so they do not actually check the "
                "solution's behaviour. Tests must call the exported functions and assert on their results.",
                count,
            )
    return CheckResult(True, f"{count} tests passed; starter stub correctly fails", count)


def validate_lesson_dir(day_dir: Path, sandbox: Sandbox, min_tests: int) -> CheckResult:
    """Re-validate a complete lesson folder (used by the secret-less validate
    job and by the repository validation workflow)."""
    meta_path = day_dir / "lesson.json"
    if not meta_path.exists():
        return CheckResult(False, f"{meta_path} is missing")
    meta = read_json(meta_path)
    try:
        profile = get_profile(str(meta.get("language")))
    except AgentError as exc:
        return CheckResult(False, str(exc))

    problems = meta.get("problems") or []
    issues: List[str] = []
    if not (day_dir / "README.md").exists():
        issues.append("README.md is missing")
    if not problems:
        issues.append("lesson.json lists no problems")
    for problem in problems:
        files = problem.get("files") or {}
        missing = [
            f"problem {problem.get('number')}: {kind} file {files.get(kind)!r} is missing"
            for kind in ("exercise", "solution", "notes", "tests", "practice")
            if not _safe_file(day_dir, files.get(kind))
        ]
        if missing:
            issues.extend(missing)
            continue
        code = ProblemCode(
            number=int(problem["number"]),
            exports=problem.get("exports") or [],
            solution=(day_dir / files["solution"]).read_text(encoding="utf-8"),
            tests=strip_header((day_dir / files["tests"]).read_text(encoding="utf-8")),
            starter="",
        )
        # practice/ belongs to the learner, so it is not policed here.
        issues.extend(f"problem {code.number}: {i}" for i in static_issues(profile, code, check_starter=False))
    if issues:
        return CheckResult(False, "Lesson structure checks failed:\n" + "\n".join(f"- {i}" for i in issues))

    with tempfile.TemporaryDirectory(prefix="dsa-validate-") as tmp:
        root = Path(tmp)
        for sub in ("solutions", "tests"):
            shutil.copytree(day_dir / sub, root / sub)
        command = profile.command(profile.all_tests_glob)
        run = sandbox.run(root, profile.image, profile.host_command, command, {"DSA_SOLUTIONS_DIR": "{root}/solutions"})
    count = profile.count_tests(run.output) or 0
    if not run.ok:
        return CheckResult(False, f"Tests failed for {day_dir.name}. Output:\n{run.output}", count)
    required = len(problems) * min_tests
    if count < required:
        return CheckResult(False, f"{day_dir.name}: only {count} tests ran, expected at least {required}", count)
    return CheckResult(True, f"{day_dir.name}: {count} tests passed across {len(problems)} problems", count)


def _safe_file(day_dir: Path, rel: object) -> bool:
    return isinstance(rel, str) and not Path(rel).is_absolute() and ".." not in Path(rel).parts and (day_dir / rel).is_file()


def run_practice(day_dir: Path, sandbox: Sandbox, number: Optional[int] = None) -> List[dict]:
    """Run the tests against the learner's own code in practice/.

    Returns one row per problem: attempted (file differs from the generated
    starter), passed, and the test output.
    """
    meta = read_json(day_dir / "lesson.json")
    profile = get_profile(str(meta["language"]))
    rows = []
    for problem in meta.get("problems") or []:
        if number is not None and problem["number"] != number:
            continue
        files = problem["files"]
        practice = day_dir / files["practice"]
        attempted = practice.is_file() and sha256(practice.read_text(encoding="utf-8")) != problem.get("starterSha256")
        row = {"number": problem["number"], "title": problem.get("title", ""), "attempted": attempted, "passed": False, "output": ""}
        if attempted:
            with tempfile.TemporaryDirectory(prefix="dsa-practice-") as tmp:
                root = Path(tmp)
                shutil.copytree(day_dir / "practice", root / "practice")
                shutil.copytree(day_dir / "tests", root / "tests")
                run = sandbox.run(
                    root, profile.image, profile.host_command,
                    profile.command(profile.single_test_arg(problem["number"])),
                    {"DSA_SOLUTIONS_DIR": "{root}/practice"},
                )
            row.update(passed=run.ok, output=run.output)
        rows.append(row)
    return rows
