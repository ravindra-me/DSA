"""Spaced-revision bookkeeping, derived purely from the lesson history.

A topic is "learned" on the day of its first non-revision lesson (L). With
intervals [7, 21, 45] its revisions become due on days L+7, L+21 and L+45
(lesson days, not calendar days, so skipped runs never cause a pile-up).

Each revision lesson records `revisionStage`: how many scheduled stages are
satisfied after it. A late revision satisfies every stage that is already due,
so a backlog collapses instead of growing without bound.

A learner can also set `"requestRevision": true` on any lesson in
progress.json to get that topic revised as soon as possible.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Mapping, Optional, Sequence


@dataclass
class TopicState:
    topic_id: str
    learned_day: int
    last_day: int
    stages_done: int = 0
    requested: bool = False


@dataclass(frozen=True)
class DueRevision:
    topic_id: str
    due_day: int
    learned_day: int
    requested: bool


def topic_states(lessons: Iterable[Mapping[str, object]]) -> Dict[str, TopicState]:
    states: Dict[str, TopicState] = {}
    for lesson in sorted(lessons, key=lambda l: int(l["day"])):
        topic_id, day = str(lesson["topic"]), int(lesson["day"])
        state = states.get(topic_id)
        if state is None:
            state = states[topic_id] = TopicState(topic_id, learned_day=day, last_day=day)
        state.last_day = max(state.last_day, day)
        if lesson.get("kind") == "revision":
            state.stages_done = max(state.stages_done, int(lesson.get("revisionStage") or 0))
        if lesson.get("requestRevision") is True:
            state.requested = True
    return states


def next_due_day(state: TopicState, intervals: Sequence[int]) -> Optional[int]:
    if state.stages_done >= len(intervals):
        return None
    return state.learned_day + intervals[state.stages_done]


def due_revisions(
    lessons: Iterable[Mapping[str, object]], intervals: Sequence[int], day: int
) -> List[DueRevision]:
    """Revisions due on `day`, most urgent first (requested, then most overdue)."""
    due: List[DueRevision] = []
    for state in topic_states(lessons).values():
        nxt = next_due_day(state, intervals)
        if state.requested:
            due.append(DueRevision(state.topic_id, 0, state.learned_day, True))
        elif nxt is not None and nxt <= day:
            due.append(DueRevision(state.topic_id, nxt, state.learned_day, False))
    return sorted(due, key=lambda d: (not d.requested, d.due_day, d.learned_day))


def stage_after_revision(state: TopicState, intervals: Sequence[int], day: int) -> int:
    """Stages satisfied once a revision of this topic happens on `day`."""
    satisfied = sum(1 for interval in intervals if state.learned_day + interval <= day)
    return max(state.stages_done, satisfied)


def upcoming(lessons: Iterable[Mapping[str, object]], intervals: Sequence[int]) -> List[dict]:
    rows = []
    for state in topic_states(lessons).values():
        nxt = next_due_day(state, intervals)
        if nxt is not None or state.requested:
            rows.append(
                {
                    "topic": state.topic_id,
                    "dueDay": nxt,
                    "stage": state.stages_done + 1,
                    "requested": state.requested,
                }
            )
    return sorted(rows, key=lambda r: (not r["requested"], r["dueDay"] or 0))
