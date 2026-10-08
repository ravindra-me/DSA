"""Merges a validated staging lesson into the repository.

This step only copies files and updates JSON/Markdown; it never executes
generated code, which is why the publish job (the only job holding a write
token) can run it safely.

It re-checks idempotency against the *current* progress file, so if two runs
race, or the publish step is retried, the same lesson is never added twice.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

from . import log
from .config import Settings
from .errors import ConfigError
from .fsutil import atomic_write_text, read_json, replace_directory
from .generate_lesson import RECORD_FILE, RECORD_SCHEMA
from .progress import find_by_date, find_by_day, load_progress, save_progress, upsert_lesson, validate_progress
from .render import render_index
from .roadmap import Roadmap

SLUG = re.compile(r"^day-\d{3,}$")


@dataclass(frozen=True)
class ApplyResult:
    applied: bool
    message: str
    commit_message: str = ""
    day: int = 0


def load_record(staging: Path) -> Dict[str, Any]:
    path = staging / RECORD_FILE
    try:
        record = read_json(path)
    except (OSError, ValueError) as exc:
        raise ConfigError(f"cannot read staging record {path}: {exc}") from exc
    if record.get("schemaVersion") != RECORD_SCHEMA:
        raise ConfigError("staging record has an unsupported schemaVersion")
    if record.get("mode") not in ("append", "replace"):
        raise ConfigError("staging record 'mode' must be append or replace")
    entry = record.get("entry")
    validate_progress({"schemaVersion": 1, "lessons": [entry]})
    slug = record.get("slug")
    if not isinstance(slug, str) or not SLUG.match(slug) or slug != f"day-{entry['day']:03d}":
        raise ConfigError(f"staging record has an invalid slug {slug!r}")
    if not (staging / slug / "lesson.json").is_file():
        raise ConfigError(f"staging lesson folder {staging / slug} is missing or incomplete")
    return record


def write_index(settings: Settings, progress: Dict[str, Any]) -> None:
    atomic_write_text(settings.lessons_dir / "README.md", render_index(progress, settings.lessons_dir.name))


def apply_staging(settings: Settings, roadmap: Roadmap, staging: Path) -> ApplyResult:
    record = load_record(staging)
    entry, mode, slug = record["entry"], record["mode"], record["slug"]
    day = entry["day"]
    progress = load_progress(settings.progress_path)
    existing = find_by_day(progress, day)

    if existing is not None and existing.get("generationId") == entry.get("generationId"):
        return ApplyResult(False, f"day {day} from this run is already published; nothing to do", day=day)

    if mode == "append":
        if existing is not None:
            raise ConfigError(
                f"day {day} already exists in progress.json (another run published first). "
                "Re-run the workflow to generate the next day."
            )
        same_date = find_by_date(progress, entry["date"])
        if same_date and not record.get("extraLesson"):
            return ApplyResult(False, f"a lesson for {entry['date']} was already published (day {same_date[-1]['day']})", day=day)
    else:
        if existing is None or existing["date"] != entry["date"]:
            raise ConfigError(f"cannot regenerate day {day}: it no longer matches progress.json")

    target = settings.lessons_dir / slug
    if mode == "append" and target.exists():
        log.warn(f"{target} exists but is not in progress.json (left over from a failed run); replacing it")
    replace_directory(staging / slug, target)

    saved = save_progress(settings.progress_path, upsert_lesson(progress, entry), roadmap, settings)
    write_index(settings, saved)

    verb, done = ("regenerate", "regenerated") if mode == "replace" else ("add", "added")
    kind = " (revision)" if entry["kind"] == "revision" else ""
    commit = f"chore(dsa): {verb} day {day} - {entry['topicTitle']}{kind}"
    return ApplyResult(True, f"{done} day {day}: {entry['topicTitle']}{kind}", commit, day)
