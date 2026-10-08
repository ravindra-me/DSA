"""Renders the Markdown prompt templates in .github/agents/prompts/.

Placeholders are written as {{name}}. Rendering fails loudly on a missing
value or a leftover placeholder, so template typos surface immediately.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Mapping

from .errors import ConfigError

PLACEHOLDER = re.compile(r"\{\{\s*([a-z_]+)\s*\}\}")
TEMPLATES = ("system", "lesson", "problem", "repair")


def render(prompts_dir: Path, name: str, values: Mapping[str, object]) -> str:
    path = prompts_dir / f"{name}.md"
    try:
        template = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ConfigError(f"cannot read prompt template {path}: {exc}") from exc

    missing = sorted({m for m in PLACEHOLDER.findall(template) if m not in values})
    if missing:
        raise ConfigError(f"prompt {name}.md uses undefined placeholders: {', '.join(missing)}")
    # Substitute in a single pass so values containing "{{...}}" are left untouched.
    return PLACEHOLDER.sub(lambda m: str(values[m.group(1)]), template).strip() + "\n"


def check_templates(prompts_dir: Path) -> None:
    for name in TEMPLATES:
        if not (prompts_dir / f"{name}.md").is_file():
            raise ConfigError(f"missing prompt template {prompts_dir / (name + '.md')}")
