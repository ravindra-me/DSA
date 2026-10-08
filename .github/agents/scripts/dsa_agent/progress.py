"""dsa/progress.json: the single source of truth for what has been learned.

The `lessons` list is the history. Everything else in the file (currentDay,
topicsCompleted, upcomingRevisions, stats, each lesson's revisionRequired) is
derived from it and recomputed on every save, so hand edits can never leave
the summary inconsistent.

Fields a learner may edit by hand on a lesson:
    status             generated | in-progress | completed | skipped
    problemsCompleted  how many problems you solved yourself
    requestRevision    true -> schedule a revision of this topic ASAP
    notes              free text
"""

from __future__ import annotations

import copy
import re
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import revision
from .config import Settings
from .errors import ConfigError
from .fsutil import atomic_write_json, read_json
from .roadmap import Roadmap

SCHEMA_VERSION = 1
STATUSES = ("generated", "in-progress", "completed", "skipped")
KINDS = ("new", "revision")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def empty_progress() -> Dict[str, Any]:
    return {"schemaVersion": SCHEMA_VERSION, "lessons": []}


def load_progress(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return empty_progress()
    try:
        data = read_json(path)
    except (OSError, ValueError) as exc:
        raise ConfigError(f"{path} is not valid JSON: {exc}") from exc
    validate_progress(data)
    return data


def validate_progress(data: Any) -> None:
    if not isinstance(data, dict):
        raise ConfigError("progress.json must contain a JSON object")
    if data.get("schemaVersion") != SCHEMA_VERSION:
        raise ConfigError(f"progress.json schemaVersion must be {SCHEMA_VERSION}")
    lessons = data.get("lessons")
    if not isinstance(lessons, list):
        raise ConfigError("progress.json 'lessons' must be a list")
    days = set()
    for i, lesson in enumerate(lessons):
        where = f"progress.json lessons[{i}]"
        if not isinstance(lesson, dict):
            raise ConfigError(f"{where} must be an object")
        day = lesson.get("day")
        if not isinstance(day, int) or isinstance(day, bool) or day < 1:
            raise ConfigError(f"{where}.day must be a positive integer")
        if day in days:
            raise ConfigError(f"{where}: duplicate day {day}")
        days.add(day)
        if not isinstance(lesson.get("date"), str) or not DATE_RE.match(lesson["date"]):
            raise ConfigError(f"{where}.date must be YYYY-MM-DD")
        date.fromisoformat(lesson["date"])
        if not isinstance(lesson.get("topic"), str):
            raise ConfigError(f"{where}.topic must be a string")
        if lesson.get("kind") not in KINDS:
            raise ConfigError(f"{where}.kind must be one of {KINDS}")
        if lesson.get("status") not in STATUSES:
            raise ConfigError(f"{where}.status must be one of {STATUSES}")
        generated = lesson.get("problemsGenerated")
        completed = lesson.get("problemsCompleted", 0)
        if not isinstance(generated, int) or generated < 0:
            raise ConfigError(f"{where}.problemsGenerated must be a non-negative integer")
        if not isinstance(completed, int) or not 0 <= completed <= generated:
            raise ConfigError(f"{where}.problemsCompleted must be between 0 and problemsGenerated")
        if "requestRevision" in lesson and not isinstance(lesson["requestRevision"], bool):
            raise ConfigError(f"{where}.requestRevision must be true or false")


def lessons_sorted(progress: Dict[str, Any]) -> List[Dict[str, Any]]:
    return sorted(progress["lessons"], key=lambda l: l["day"])


def find_by_date(progress: Dict[str, Any], day_date: str) -> List[Dict[str, Any]]:
    return [l for l in lessons_sorted(progress) if l["date"] == day_date]


def find_by_day(progress: Dict[str, Any], day: int) -> Optional[Dict[str, Any]]:
    return next((l for l in progress["lessons"] if l["day"] == day), None)


def max_day(progress: Dict[str, Any]) -> int:
    return max((l["day"] for l in progress["lessons"]), default=0)


def learned_topics(lessons: List[Dict[str, Any]]) -> List[str]:
    """Topic ids in the order they were first taught."""
    seen: List[str] = []
    for lesson in sorted(lessons, key=lambda l: l["day"]):
        if lesson["topic"] not in seen:
            seen.append(lesson["topic"])
    return seen


def upsert_lesson(progress: Dict[str, Any], entry: Dict[str, Any]) -> Dict[str, Any]:
    """Return a copy of `progress` with `entry` added (or replacing the same day).

    Generating a revision clears any `requestRevision` flags on that topic.
    """
    updated = copy.deepcopy(progress)
    updated["lessons"] = [l for l in updated["lessons"] if l["day"] != entry["day"]]
    if entry.get("kind") == "revision":
        for lesson in updated["lessons"]:
            if lesson["topic"] == entry["topic"]:
                lesson["requestRevision"] = False
    updated["lessons"].append(copy.deepcopy(entry))
    updated["lessons"].sort(key=lambda l: l["day"])
    return updated


def recompute(progress: Dict[str, Any], roadmap: Roadmap, settings: Settings) -> Dict[str, Any]:
    """Rebuild every derived field from the lesson history."""
    lessons = lessons_sorted(copy.deepcopy(progress))
    intervals = settings.revision.intervals if settings.revision.enabled else ()
    states = revision.topic_states(lessons)
    for lesson in lessons:
        state = states[lesson["topic"]]
        lesson.setdefault("problemsCompleted", 0)
        lesson.setdefault("requestRevision", False)
        lesson["revisionRequired"] = state.requested or revision.next_due_day(state, intervals) is not None

    learned = learned_topics(lessons)
    remaining = [t.id for t in roadmap.topics if t.id not in learned]
    last = lessons[-1] if lessons else None
    derived: Dict[str, Any] = {
        "schemaVersion": SCHEMA_VERSION,
        "currentDay": last["day"] if last else 0,
        "lastLessonDate": last["date"] if last else None,
        "currentTopic": last["topic"] if last else None,
        "topicsCompleted": learned,
        "nextRoadmapTopic": remaining[0] if remaining else None,
        "roadmapProgress": f"{len(roadmap) - len(remaining)}/{len(roadmap)}",
        "upcomingRevisions": revision.upcoming(lessons, intervals),
        "stats": {
            "lessons": len(lessons),
            "newTopicLessons": sum(1 for l in lessons if l["kind"] == "new"),
            "revisionLessons": sum(1 for l in lessons if l["kind"] == "revision"),
            "problemsGenerated": sum(l["problemsGenerated"] for l in lessons),
            "problemsCompleted": sum(l.get("problemsCompleted", 0) for l in lessons),
            "lessonsCompleted": sum(1 for l in lessons if l["status"] == "completed"),
        },
        "lessons": lessons,
    }
    return derived


def save_progress(path: Path, progress: Dict[str, Any], roadmap: Roadmap, settings: Settings) -> Dict[str, Any]:
    data = recompute(progress, roadmap, settings)
    validate_progress(data)
    atomic_write_json(path, data)
    return data
