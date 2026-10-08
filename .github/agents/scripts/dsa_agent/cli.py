"""Command-line entry point. GitHub Actions workflows call these subcommands;
they contain the orchestration so the YAML stays thin.

    check            validate config, roadmap, prompts, progress file
    plan             show what would be generated today (no AI calls)
    generate         plan + generate + validate a lesson into a staging dir
    validate         sandbox-validate a staging lesson, one day, or all days
    apply            merge a staging lesson into dsa/ and update progress
    run              generate + validate + apply in one go (local use)
    practice         run a day's tests against YOUR code in practice/
    practice-report  summarise practice attempts for every day (CI)
    reindex          recompute progress.json summary and dsa/README.md
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import tempfile
from datetime import date, datetime
from pathlib import Path
from typing import List, Optional

from . import log
from .ai import create_provider
from .config import Settings, load_settings
from .errors import AgentError, ConfigError
from .generate_lesson import generate_lesson
from .languages import get_profile
from .progress import load_progress, save_progress
from .prompts import check_templates
from .roadmap import Roadmap, load_roadmap
from .sandbox import create_sandbox
from .select_topic import LessonPlan, Request, plan_lesson
from .update_progress import apply_staging, load_record, write_index
from .validate_solution import run_practice, validate_lesson_dir

TRUE = {"1", "true", "yes", "on"}


def _env_flag(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in TRUE


def _today(settings: Settings, override: Optional[str]) -> date:
    if override:
        try:
            return date.fromisoformat(override)
        except ValueError as exc:
            raise ConfigError(f"date must be YYYY-MM-DD, got {override!r}") from exc
    from zoneinfo import ZoneInfo

    return datetime.now(ZoneInfo(settings.timezone)).date()


def _request(args: argparse.Namespace, settings: Settings) -> Request:
    problems_raw = args.problems or os.environ.get("DSA_PROBLEMS", "").strip()
    try:
        problems = int(problems_raw) if problems_raw else None
    except ValueError as exc:
        raise ConfigError(f"number of problems must be an integer, got {problems_raw!r}") from exc
    difficulty = (args.difficulty or os.environ.get("DSA_DIFFICULTY", "")).strip().lower()
    return Request(
        date=_today(settings, args.date or os.environ.get("DSA_DATE", "").strip() or None),
        topic=(args.topic or os.environ.get("DSA_TOPIC", "")).strip() or None,
        difficulty=None if difficulty in ("", "default") else difficulty,
        problems=problems,
        force=args.force or _env_flag("DSA_FORCE"),
        extra=args.extra or _env_flag("DSA_EXTRA_LESSON"),
    )


def _load() -> "tuple[Settings, Roadmap]":
    settings = load_settings()
    get_profile(settings.language)
    return settings, load_roadmap(settings.roadmap_path)


def _describe(plan: LessonPlan) -> str:
    return (
        f"Day {plan.day} ({plan.date}): {plan.topic.title} [{plan.topic.id}], {plan.kind}"
        f"{f' stage {plan.revision_stage}' if plan.kind == 'revision' else ''}, "
        f"{plan.problem_count} problems ({', '.join(plan.difficulties)}), mode={plan.mode}. Reason: {plan.reason}"
    )


# --------------------------------------------------------------------------- commands

def cmd_check(args: argparse.Namespace) -> int:
    settings, roadmap = _load()
    check_templates(settings.prompts_dir)
    progress = load_progress(settings.progress_path)
    for lesson in progress["lessons"]:
        if roadmap.get(lesson["topic"]) is None:
            log.warn(f"day {lesson['day']} uses topic '{lesson['topic']}' which is no longer in the roadmap")
    log.info(
        f"OK: language={settings.language}, roadmap={len(roadmap)} topics, lessons={len(progress['lessons'])}, "
        f"sandbox={settings.sandbox.mode}, provider={settings.ai.provider}"
    )
    return 0


def cmd_plan(args: argparse.Namespace) -> int:
    settings, roadmap = _load()
    plan, reason = plan_lesson(load_progress(settings.progress_path), roadmap, settings, _request(args, settings))
    log.info(_describe(plan) if plan else f"Nothing to generate: {reason}")
    return 0


def _generate(args: argparse.Namespace, staging: Path) -> Optional[LessonPlan]:
    settings, roadmap = _load()
    progress = load_progress(settings.progress_path)
    plan, reason = plan_lesson(progress, roadmap, settings, _request(args, settings))
    if plan is None:
        log.notice(f"Skipping generation: {reason}")
        log.set_output("skipped", True)
        log.summary(f"### DSA agent: nothing to do\n\n{reason}")
        return None

    log.notice(_describe(plan))
    provider = create_provider(settings.ai)  # fail fast on a missing key, before any work
    log.info(f"AI provider: {provider.name}, model: {provider.model}")
    sandbox = create_sandbox(settings.sandbox)

    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)
    record = generate_lesson(settings, plan, provider, sandbox, staging)

    entry = record["entry"]
    for key, value in (("skipped", False), ("day", plan.day), ("slug", plan.slug), ("topic", plan.topic.id), ("title", plan.topic.title)):
        log.set_output(key, value)
    problems = "\n".join(f"| {p['number']} | {p['title']} | {p['difficulty']} |" for p in entry["problems"])
    log.summary(
        f"### DSA agent: generated Day {plan.day}: {plan.topic.title}\n\n"
        f"- Type: {plan.kind}\n- Reason: {plan.reason}\n- Model: {provider.name}/{provider.model}\n\n"
        f"| # | Problem | Difficulty |\n|---|---------|------------|\n{problems}"
    )
    return plan


def cmd_generate(args: argparse.Namespace) -> int:
    _generate(args, Path(args.staging).resolve())
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    settings, _ = _load()
    if args.staging:
        staging = Path(args.staging).resolve()
        record = load_record(staging)
        targets = [staging / record["slug"]]
    elif args.day is not None:
        targets = [settings.lessons_dir / f"day-{args.day:03d}"]
    else:
        targets = sorted(p for p in settings.lessons_dir.glob("day-*") if p.is_dir())
        load_progress(settings.progress_path)  # also validates the progress file
        if not targets:
            log.info("No lessons to validate yet.")
            return 0

    sandbox = create_sandbox(settings.sandbox)
    failures = 0
    for day_dir in targets:
        with log.group(f"Validating {day_dir.name}"):
            if not day_dir.is_dir():
                log.error(f"{day_dir} does not exist")
                failures += 1
                continue
            result = validate_lesson_dir(day_dir, sandbox, settings.min_tests_per_problem)
            (log.info if result.ok else log.error)(result.report)
            failures += 0 if result.ok else 1
    log.info(f"{len(targets) - failures}/{len(targets)} lesson(s) valid")
    return 1 if failures else 0


def cmd_apply(args: argparse.Namespace) -> int:
    settings, roadmap = _load()
    result = apply_staging(settings, roadmap, Path(args.staging).resolve())
    (log.notice if result.applied else log.info)(result.message)
    if args.result_file:
        Path(args.result_file).write_text(
            json.dumps(
                {
                    "applied": result.applied,
                    "message": result.message,
                    "commitMessage": result.commit_message,
                    "day": result.day,
                    "lessonsDir": str(settings.lessons_dir.relative_to(settings.repo_root)),
                }
            ),
            encoding="utf-8",
        )
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    with tempfile.TemporaryDirectory(prefix="dsa-staging-") as tmp:
        staging = Path(tmp) / "staging"
        plan = _generate(args, staging)
        if plan is None:
            return 0
        settings, roadmap = _load()
        result = apply_staging(settings, roadmap, staging)
        log.notice(result.message)
    return 0


def cmd_practice(args: argparse.Namespace) -> int:
    settings, _ = _load()
    day_dir = settings.lessons_dir / f"day-{args.day:03d}"
    if not (day_dir / "lesson.json").is_file():
        raise ConfigError(f"{day_dir} is not a generated lesson")
    rows = run_practice(day_dir, create_sandbox(settings.sandbox), args.problem)
    failed = 0
    for row in rows:
        if not row["attempted"]:
            log.info(f"Problem {row['number']} ({row['title']}): not attempted yet (practice file unchanged)")
            continue
        status = "PASSED" if row["passed"] else "FAILED"
        failed += 0 if row["passed"] else 1
        with log.group(f"Problem {row['number']} ({row['title']}): {status}"):
            log.info(row["output"])
    return 1 if failed else 0


def cmd_practice_report(args: argparse.Namespace) -> int:
    settings, _ = _load()
    sandbox = None
    lines = ["### Practice report", "", "| Day | Problem | Result |", "|-----|---------|--------|"]
    for day_dir in sorted(p for p in settings.lessons_dir.glob("day-*") if (p / "lesson.json").is_file()):
        sandbox = sandbox or create_sandbox(settings.sandbox)
        for row in run_practice(day_dir, sandbox):
            if row["attempted"]:
                lines.append(f"| {day_dir.name} | {row['number']}. {row['title']} | {'✅ passed' if row['passed'] else '❌ failing'} |")
    if len(lines) == 4:
        lines.append("| - | No practice attempts found yet | - |")
    report = "\n".join(lines)
    log.info(report)
    log.summary(report)
    return 0


def cmd_reindex(args: argparse.Namespace) -> int:
    settings, roadmap = _load()
    saved = save_progress(settings.progress_path, load_progress(settings.progress_path), roadmap, settings)
    write_index(settings, saved)
    log.info(f"Rebuilt {settings.progress_path} and {settings.lessons_dir / 'README.md'}")
    return 0


# --------------------------------------------------------------------------- parser

def _add_request_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--topic", help="roadmap topic id or title (env DSA_TOPIC)")
    p.add_argument("--difficulty", help="progressive | easy | medium | hard (env DSA_DIFFICULTY)")
    p.add_argument("--problems", help="number of problems (env DSA_PROBLEMS)")
    p.add_argument("--force", action="store_true", help="regenerate today's lesson if it exists (env DSA_FORCE)")
    p.add_argument("--extra", action="store_true", help="add another lesson even if today's exists (env DSA_EXTRA_LESSON)")
    p.add_argument("--date", help="override today's date, YYYY-MM-DD (env DSA_DATE)")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="agent.py", description="Autonomous DSA learning agent")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("check", help="validate configuration").set_defaults(func=cmd_check)

    p = sub.add_parser("plan", help="show what would be generated (no AI calls)")
    _add_request_args(p)
    p.set_defaults(func=cmd_plan)

    p = sub.add_parser("generate", help="generate a lesson into a staging directory")
    _add_request_args(p)
    p.add_argument("--staging", required=True)
    p.set_defaults(func=cmd_generate)

    p = sub.add_parser("validate", help="sandbox-validate lessons")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--staging")
    group.add_argument("--day", type=int)
    group.add_argument("--all", action="store_true")
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("apply", help="merge a staging lesson into the repository")
    p.add_argument("--staging", required=True)
    p.add_argument("--result-file")
    p.set_defaults(func=cmd_apply)

    p = sub.add_parser("run", help="generate + apply in one go (local use)")
    _add_request_args(p)
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("practice", help="test your own solutions in practice/")
    p.add_argument("--day", type=int, required=True)
    p.add_argument("--problem", type=int)
    p.set_defaults(func=cmd_practice)

    sub.add_parser("practice-report", help="summarise practice attempts").set_defaults(func=cmd_practice_report)
    sub.add_parser("reindex", help="rebuild derived progress fields and dsa/README.md").set_defaults(func=cmd_reindex)
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except AgentError as exc:
        log.error(f"{type(exc).__name__}: {exc}")
        return 1
    except KeyboardInterrupt:
        log.error("interrupted")
        return 130
