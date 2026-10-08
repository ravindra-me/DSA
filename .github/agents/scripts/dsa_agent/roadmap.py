"""The ordered learning roadmap (.github/agents/roadmap/roadmap.json)."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .errors import ConfigError
from .fsutil import read_json

TOPIC_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass(frozen=True)
class Topic:
    id: str
    title: str
    phase_id: str
    phase_title: str
    concepts: Tuple[str, ...]
    order: int


class Roadmap:
    def __init__(self, topics: List[Topic]) -> None:
        self.topics = topics
        self._by_id: Dict[str, Topic] = {t.id: t for t in topics}

    def __len__(self) -> int:
        return len(self.topics)

    def get(self, topic_id: str) -> Optional[Topic]:
        return self._by_id.get(topic_id)

    def resolve(self, query: str) -> Topic:
        """Find a topic by id or (case-insensitive) title."""
        needle = query.strip().lower()
        topic = self._by_id.get(needle) or next(
            (t for t in self.topics if t.title.lower() == needle), None
        )
        if topic is None:
            ids = ", ".join(t.id for t in self.topics)
            raise ConfigError(f"unknown topic {query!r}. Valid topic ids: {ids}")
        return topic

    def next_after(self, topic_id: str) -> Optional[Topic]:
        topic = self._by_id.get(topic_id)
        if topic is None or topic.order + 1 >= len(self.topics):
            return None
        return self.topics[topic.order + 1]


def load_roadmap(path: Path) -> Roadmap:
    try:
        data = read_json(path)
    except (OSError, ValueError) as exc:
        raise ConfigError(f"cannot read roadmap {path}: {exc}") from exc

    topics: List[Topic] = []
    seen = set()
    phases = data.get("phases")
    if not isinstance(phases, list) or not phases:
        raise ConfigError("roadmap must contain a non-empty 'phases' list")
    for phase in phases:
        phase_id, phase_title = phase.get("id"), phase.get("title")
        if not isinstance(phase_id, str) or not isinstance(phase_title, str):
            raise ConfigError(f"roadmap phase needs string 'id' and 'title': {phase!r}")
        for raw in phase.get("topics") or []:
            topic_id = raw.get("id")
            if not isinstance(topic_id, str) or not TOPIC_ID.match(topic_id):
                raise ConfigError(f"invalid topic id {topic_id!r} (use kebab-case)")
            if topic_id in seen:
                raise ConfigError(f"duplicate topic id {topic_id!r} in roadmap")
            title = raw.get("title")
            concepts = raw.get("concepts") or []
            if not isinstance(title, str) or not title.strip():
                raise ConfigError(f"topic {topic_id!r} needs a title")
            if not isinstance(concepts, list) or not all(isinstance(c, str) for c in concepts):
                raise ConfigError(f"topic {topic_id!r} 'concepts' must be a list of strings")
            seen.add(topic_id)
            topics.append(Topic(topic_id, title, phase_id, phase_title, tuple(concepts), len(topics)))
    if not topics:
        raise ConfigError("roadmap has no topics")
    return Roadmap(topics)
