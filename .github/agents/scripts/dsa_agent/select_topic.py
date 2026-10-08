"""Decides what (if anything) to generate today. Pure logic: no I/O, no AI.

Decision order:
  1. Idempotency: if a lesson already exists for today's date, do nothing,
     unless `force` (regenerate today's lesson in place) or `extra`
     (deliberately add another lesson today) was requested.
  2. A manually requested topic always wins.
  3. A due revision, if at least `minNewLessonsBetweenRevisions` new lessons
     happened since the last revision (requested revisions skip this gap).
  4. The next roadmap topic not yet learned.
  5. Roadmap finished: revise whatever is due, else the least recently
     practised topic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any, Dict, List, Optional, Tuple

from . import revision
from .config import DIFFICULTY_LEVELS, Settings
from .errors import ConfigError
from .progress import find_by_date, learned_topics, lessons_sorted, max_day
from .roadmap import Roadmap, Topic

LADDER = ("Easy", "Easy/Medium", "Medium", "Medium/Hard", "Hard")
_RANGES = {"progressive": (0, 4), "easy": (0, 1), "medium": (1, 3), "hard": (3, 4)}


@dataclass(frozen=True)
class Request:
    date: date
    topic: Optional[str] = None
    difficulty: Optional[str] = None
    problems: Optional[int] = None
    force: bool = False
    extra: bool = False


@dataclass(frozen=True)
class LessonPlan:
    day: int
    date: str
    topic: Topic
    kind: str  # "new" | "revision"
    revision_stage: int
    mode: str  # "append" | "replace"
    difficulty: str
    difficulties: Tuple[str, ...]
    reason: str
    extra: bool = False
    learned_topics: Tuple[str, ...] = ()
    previous_problems: Tuple[str, ...] = field(default_factory=tuple)

    @property
    def slug(self) -> str:
        return f"day-{self.day:03d}"

    @property
    def problem_count(self) -> int:
        return len(self.difficulties)


def difficulty_ladder(count: int, level: str, kind: str = "new") -> Tuple[str, ...]:
    """Spread `count` problems across the difficulty range for `level`.

    progressive with 5 problems -> Easy, Easy/Medium, Medium, Medium/Hard, Hard.
    Revisions start one step harder, since the basics are already known.
    """
    lo, hi = _RANGES[level]
    if kind == "revision" and level == "progressive":
        lo = 1
    if count == 1:
        return (LADDER[(lo + hi) // 2],)
    return tuple(LADDER[lo + round(i * (hi - lo) / (count - 1))] for i in range(count))


def plan_lesson(
    progress: Dict[str, Any], roadmap: Roadmap, settings: Settings, request: Request
) -> Tuple[Optional[LessonPlan], str]:
    """Return (plan, reason). plan is None when nothing should be generated."""
    difficulty = (request.difficulty or settings.default_difficulty).lower()
    if difficulty not in DIFFICULTY_LEVELS:
        raise ConfigError(f"difficulty must be one of {DIFFICULTY_LEVELS}, got {request.difficulty!r}")
    count = request.problems or settings.problems_per_day
    if not 1 <= count <= settings.max_problems_per_day:
        raise ConfigError(f"number of problems must be between 1 and {settings.max_problems_per_day}")

    day_date = request.date.isoformat()
    todays = find_by_date(progress, day_date)
    replacing: Optional[Dict[str, Any]] = None

    if todays and not request.extra:
        if not request.force:
            days = ", ".join(str(l["day"]) for l in todays)
            return None, f"A lesson for {day_date} already exists (day {days}); nothing to do. Use force to regenerate it."
        replacing = todays[-1]

    if replacing is not None:
        day, mode = replacing["day"], "replace"
        history = [l for l in lessons_sorted(progress) if l["day"] != day]
    else:
        day, mode = max_day(progress) + 1, "append"
        history = lessons_sorted(progress)
        if history and history[-1]["date"] > day_date:
            raise ConfigError(
                f"date {day_date} is earlier than the last lesson ({history[-1]['date']}); refusing to go back in time"
            )

    topic, kind, reason = _choose_topic(history, roadmap, settings, request, replacing, day)

    intervals = settings.revision.intervals if settings.revision.enabled else ()
    stage = 0
    if kind == "revision":
        state = revision.topic_states(history).get(topic.id)
        stage = revision.stage_after_revision(state, intervals, day) if state else 0

    previous = tuple(
        p["title"]
        for l in history
        if l["topic"] == topic.id
        for p in l.get("problems", [])
        if isinstance(p, dict) and isinstance(p.get("title"), str)
    )
    return (
        LessonPlan(
            day=day,
            date=day_date,
            topic=topic,
            kind=kind,
            revision_stage=stage,
            mode=mode,
            difficulty=difficulty,
            difficulties=difficulty_ladder(count, difficulty, kind),
            reason=reason,
            extra=request.extra,
            learned_topics=tuple(learned_topics(history)),
            previous_problems=previous,
        ),
        reason,
    )


def _choose_topic(
    history: List[Dict[str, Any]],
    roadmap: Roadmap,
    settings: Settings,
    request: Request,
    replacing: Optional[Dict[str, Any]],
    day: int,
) -> Tuple[Topic, str, str]:
    learned = learned_topics(history)

    if request.topic:
        topic = roadmap.resolve(request.topic)
        kind = "revision" if topic.id in learned else "new"
        return topic, kind, f"manually requested topic '{topic.id}'"

    if replacing is not None:
        topic = roadmap.resolve(replacing["topic"])
        return topic, replacing["kind"], f"regenerating day {replacing['day']} ('{topic.id}') on request"

    next_new = next((t for t in roadmap.topics if t.id not in learned), None)
    if settings.revision.enabled:
        due = revision.due_revisions(history, settings.revision.intervals, day)
        if due:
            first = due[0]
            gap_ok = _new_lessons_since_last_revision(history) >= settings.revision.min_new_lessons_between
            if first.requested or gap_ok or next_new is None:
                topic = roadmap.get(first.topic_id)
                if topic is not None:
                    why = "requested revision" if first.requested else f"spaced revision due on day {first.due_day}"
                    return topic, "revision", f"{why} of '{topic.id}' (learned on day {first.learned_day})"

    if next_new is not None:
        return next_new, "new", f"next roadmap topic ({next_new.order + 1}/{len(roadmap)})"

    # Roadmap complete and nothing due: keep practising the stalest topic.
    states = revision.topic_states(history)
    stalest = min(
        (s for s in states.values() if roadmap.get(s.topic_id)),
        key=lambda s: (s.last_day, s.learned_day),
    )
    topic = roadmap.get(stalest.topic_id)
    assert topic is not None
    return topic, "revision", f"roadmap complete; revising least recently practised topic '{topic.id}'"


def _new_lessons_since_last_revision(history: List[Dict[str, Any]]) -> int:
    count = 0
    for lesson in reversed(history):
        if lesson["kind"] == "revision":
            break
        count += 1
    return count
