"""Logging helpers that emit GitHub Actions workflow commands when running in
Actions (collapsible groups, annotations, step outputs, job summary) and plain
text everywhere else."""

from __future__ import annotations

import contextlib
import os
import sys
import uuid
from typing import Iterator


def _in_actions() -> bool:
    return os.environ.get("GITHUB_ACTIONS") == "true"


def _escape(message: str) -> str:
    return message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def info(message: str) -> None:
    print(message, flush=True)


def notice(message: str) -> None:
    print(f"::notice::{_escape(message)}" if _in_actions() else f"NOTE: {message}", flush=True)


def warn(message: str) -> None:
    print(f"::warning::{_escape(message)}" if _in_actions() else f"WARNING: {message}", flush=True)


def error(message: str) -> None:
    stream = sys.stdout if _in_actions() else sys.stderr
    print(f"::error::{_escape(message)}" if _in_actions() else f"ERROR: {message}", file=stream, flush=True)


@contextlib.contextmanager
def group(title: str) -> Iterator[None]:
    if _in_actions():
        print(f"::group::{title}", flush=True)
    else:
        print(f"\n== {title}", flush=True)
    try:
        yield
    finally:
        if _in_actions():
            print("::endgroup::", flush=True)


def set_output(name: str, value: object) -> None:
    """Expose a step output (no-op outside GitHub Actions)."""
    path = os.environ.get("GITHUB_OUTPUT")
    text = str(value).lower() if isinstance(value, bool) else str(value)
    if not path:
        return
    with open(path, "a", encoding="utf-8") as fh:
        if "\n" in text:
            delimiter = f"EOF_{uuid.uuid4().hex}"
            fh.write(f"{name}<<{delimiter}\n{text}\n{delimiter}\n")
        else:
            fh.write(f"{name}={text}\n")


def summary(markdown: str) -> None:
    """Append Markdown to the job summary (no-op outside GitHub Actions)."""
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(markdown.rstrip() + "\n\n")
