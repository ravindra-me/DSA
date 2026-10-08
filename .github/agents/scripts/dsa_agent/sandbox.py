"""Runs untrusted, AI-generated code.

DockerSandbox (default, always used in GitHub Actions):
  * no network (--network none), read-only root filesystem, small tmpfs
  * unprivileged user, all capabilities dropped, no-new-privileges
  * memory / CPU / process-count limits and a wall-clock timeout
  * only the lesson's code is mounted (read-only); no repository checkout,
    no environment variables from the host, so no API keys or tokens

ProcessSandbox runs the tests as a plain subprocess with a scrubbed
environment. It provides NO real isolation and exists only for local
development and the agent's own self-tests (DSA_SANDBOX=process).
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Mapping, Set

from . import log
from .config import SandboxSettings
from .errors import AgentError

OUTPUT_LIMIT = 12000


@dataclass(frozen=True)
class RunResult:
    exit_code: int
    output: str
    timed_out: bool
    seconds: float

    @property
    def ok(self) -> bool:
        return self.exit_code == 0 and not self.timed_out


def _truncate(text: str) -> str:
    if len(text) <= OUTPUT_LIMIT:
        return text
    return "...[output truncated]...\n" + text[-OUTPUT_LIMIT:]


def _timeout_output(exc: subprocess.TimeoutExpired) -> str:
    parts = []
    for chunk in (exc.stdout, exc.stderr):
        if isinstance(chunk, bytes):
            chunk = chunk.decode("utf-8", "replace")
        parts.append(chunk or "")
    return _truncate("".join(parts) + "\n[sandbox timeout: tests took too long - infinite loop or too slow?]")


def make_readable(root: Path) -> None:
    """The container runs as `nobody`, so the mounted tree must be world-readable."""
    os.chmod(root, 0o755)
    for dirpath, dirnames, filenames in os.walk(root):
        for d in dirnames:
            os.chmod(os.path.join(dirpath, d), 0o755)
        for f in filenames:
            os.chmod(os.path.join(dirpath, f), 0o644)


class Sandbox:
    name = "abstract"

    def run(self, workdir: Path, image: str, host_command: str, command: List[str], env: Mapping[str, str]) -> RunResult:
        """Run `command` with `workdir` as the current directory.

        `env` values may contain "{root}", replaced by the workdir path as
        seen from inside the sandbox.
        """
        raise NotImplementedError


class DockerSandbox(Sandbox):
    name = "docker"

    def __init__(self, settings: SandboxSettings) -> None:
        self.settings = settings
        self._pulled: Set[str] = set()
        if shutil.which("docker") is None:
            raise AgentError("sandbox mode 'docker' requires Docker, which was not found on PATH")

    def ensure_image(self, image: str) -> None:
        if image in self._pulled:
            return
        for attempt in range(1, 4):
            result = subprocess.run(["docker", "pull", "--quiet", image], capture_output=True, text=True)
            if result.returncode == 0:
                self._pulled.add(image)
                return
            log.warn(f"docker pull {image} failed (attempt {attempt}/3): {result.stderr.strip()[:300]}")
            time.sleep(5 * attempt)
        raise AgentError(f"could not pull sandbox image {image}")

    def run(self, workdir: Path, image: str, host_command: str, command: List[str], env: Mapping[str, str]) -> RunResult:
        self.ensure_image(image)
        make_readable(workdir)
        name = f"dsa-sandbox-{uuid.uuid4().hex[:12]}"
        args = [
            "docker", "run", "--rm", "--name", name,
            "--network", "none",
            "--read-only",
            "--tmpfs", "/tmp:rw,noexec,nosuid,size=64m",
            "--memory", self.settings.memory,
            "--memory-swap", self.settings.memory,
            "--cpus", self.settings.cpus,
            "--pids-limit", str(self.settings.pids_limit),
            "--cap-drop", "ALL",
            "--security-opt", "no-new-privileges",
            "--user", "65534:65534",
            "--volume", f"{workdir}:/work:ro",
            "--workdir", "/work",
            "--env", "HOME=/tmp",
        ]
        for key, value in env.items():
            args += ["--env", f"{key}={value.replace('{root}', '/work')}"]
        args += [image, *command]
        start = time.monotonic()
        try:
            proc = subprocess.run(
                args, capture_output=True, text=True, timeout=self.settings.timeout_seconds, stdin=subprocess.DEVNULL
            )
        except subprocess.TimeoutExpired as exc:
            subprocess.run(["docker", "kill", name], capture_output=True)
            return RunResult(124, _timeout_output(exc), True, time.monotonic() - start)
        return RunResult(proc.returncode, _truncate(proc.stdout + proc.stderr), False, time.monotonic() - start)


class ProcessSandbox(Sandbox):
    name = "process"

    def __init__(self, settings: SandboxSettings) -> None:
        self.settings = settings

    def run(self, workdir: Path, image: str, host_command: str, command: List[str], env: Mapping[str, str]) -> RunResult:
        executable = sys.executable if host_command == "python" else shutil.which(host_command)
        if executable is None:
            raise AgentError(f"'{host_command}' is required to run tests locally but was not found")
        argv = [executable, *command[1:]] if command and command[0] == host_command else command
        clean_env: Dict[str, str] = {
            "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "HOME": str(workdir),
            "PYTHONDONTWRITEBYTECODE": "1",
            "LANG": "C.UTF-8",
        }
        clean_env.update({k: v.replace("{root}", str(workdir)) for k, v in env.items()})
        start = time.monotonic()
        try:
            proc = subprocess.run(
                argv, cwd=workdir, env=clean_env, capture_output=True, text=True,
                timeout=self.settings.timeout_seconds, stdin=subprocess.DEVNULL,
            )
        except subprocess.TimeoutExpired as exc:
            return RunResult(124, _timeout_output(exc), True, time.monotonic() - start)
        return RunResult(proc.returncode, _truncate(proc.stdout + proc.stderr), False, time.monotonic() - start)


def create_sandbox(settings: SandboxSettings) -> Sandbox:
    if settings.mode == "docker":
        return DockerSandbox(settings)
    if os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("DSA_ALLOW_PROCESS_SANDBOX") != "true":
        raise AgentError("refusing to run generated code without isolation in GitHub Actions (sandbox mode 'process')")
    log.warn("sandbox mode 'process': generated code runs WITHOUT isolation (local development only)")
    return ProcessSandbox(settings)
