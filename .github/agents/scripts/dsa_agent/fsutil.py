"""Filesystem helpers. All writes into the repository go through these so a
crash mid-write can never leave a half-written progress file or lesson."""

from __future__ import annotations

import contextlib
import json
import os
import shutil
import tempfile
from pathlib import Path
from typing import Any


def read_json(path: Path) -> Any:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def atomic_write_text(path: Path, content: str) -> None:
    """Write via a temp file in the same directory + os.replace (atomic on POSIX)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    except BaseException:
        with contextlib.suppress(OSError):
            os.unlink(tmp)
        raise


def atomic_write_json(path: Path, data: Any) -> None:
    atomic_write_text(path, json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content if content.endswith("\n") else content + "\n", encoding="utf-8")


def replace_directory(source: Path, target: Path) -> None:
    """Install `source` at `target`, replacing any existing directory.

    The new tree is first copied next to the target, then swapped in with
    renames, so the target is either fully old or fully new.
    """
    target.parent.mkdir(parents=True, exist_ok=True)
    incoming = target.parent / f".{target.name}.incoming"
    backup = target.parent / f".{target.name}.backup"
    for leftover in (incoming, backup):
        if leftover.exists():
            shutil.rmtree(leftover)
    shutil.copytree(source, incoming)
    if target.exists():
        os.replace(target, backup)
    try:
        os.replace(incoming, target)
    except BaseException:
        if backup.exists():
            os.replace(backup, target)
        raise
    if backup.exists():
        shutil.rmtree(backup)

