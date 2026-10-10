"""Language profiles: file layout, test runner, prompt conventions and static
safety rules for each supported lesson language.

To add a language, add a LanguageProfile to PROFILES. Nothing else in the
agent is language-specific.

Generated test files get a deterministic import header written by the agent
(never by the AI). It imports the problem's exported symbols from
`solutions/` by default, or from the directory in DSA_SOLUTIONS_DIR, which is
how learners run the same tests against their own code in `practice/`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Sequence, Tuple

from .errors import ConfigError

HEADER_END = "---- End of generated header"
IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

Rule = Tuple[str, str]  # (regex, human-readable reason)


@dataclass(frozen=True)
class LanguageProfile:
    name: str
    display_name: str
    fence: str
    image: str  # sandbox container image, pinned by digest
    host_command: str  # executable used by the (unisolated) process sandbox
    solution_pattern: str  # e.g. "problem_{nn}.py"
    test_pattern: str
    test_arg_prefix: str  # prepended to a test file name to form the runner argument
    all_tests_glob: str
    test_command: Tuple[str, ...]  # "{tests}" is replaced by a file name or glob
    tests_run_regex: str
    conventions: str
    starter_hint: str
    header: Callable[[str, str, Sequence[str]], str]  # (nn, solution_file, exports)
    footer: Callable[[Sequence[str], str], str]  # (exports, solution_code)
    solution_rules: Tuple[Rule, ...]
    test_rules: Tuple[Rule, ...]

    def solution_file(self, number: int) -> str:
        return self.solution_pattern.format(nn=f"{number:02d}")

    def test_file(self, number: int) -> str:
        return self.test_pattern.format(nn=f"{number:02d}")

    def single_test_arg(self, number: int) -> str:
        return self.test_arg_prefix + self.test_file(number)

    def command(self, tests: str) -> List[str]:
        return [part.replace("{tests}", tests) for part in self.test_command]

    def count_tests(self, output: str) -> Optional[int]:
        matches = re.findall(self.tests_run_regex, output, flags=re.MULTILINE)
        return int(matches[-1]) if matches else None

    def assemble_solution(self, exports: Sequence[str], code: str) -> str:
        return code.rstrip() + "\n" + self.footer(exports, code)

    def assemble_tests(self, number: int, exports: Sequence[str], code: str) -> str:
        header = self.header(f"{number:02d}", self.solution_file(number), exports)
        return header + code.strip() + "\n"


def strip_header(content: str) -> str:
    """Return only the AI-written part of an assembled test file."""
    index = content.find(HEADER_END)
    if index == -1:
        return content
    newline = content.find("\n", index)
    return content[newline + 1 :] if newline != -1 else ""


def check_rules(code: str, rules: Sequence[Rule]) -> List[str]:
    return [reason for pattern, reason in rules if re.search(pattern, code, flags=re.MULTILINE)]


def validate_exports(exports: Sequence[str]) -> None:
    if not exports or len(exports) > 6:
        raise ConfigError("each problem must export between 1 and 6 symbols")
    for name in exports:
        if not isinstance(name, str) or not IDENTIFIER.match(name):
            raise ConfigError(f"invalid exported symbol name {name!r}")


# --------------------------------------------------------------------------- python

def _py_header(nn: str, solution_file: str, exports: Sequence[str]) -> str:
    module = solution_file[: -len(".py")]
    return (
        "# ---- Generated import header (do not edit) ----\n"
        "# Runs these tests against ../solutions by default. To test your own code, run\n"
        "# from the day folder:\n"
        f"#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_{nn}.py\n"
        "import os\n"
        "import sys\n"
        "import unittest\n"
        "from unittest import TestCase  # noqa: F401  (models often use the bare name)\n"
        "\n"
        "_SOLUTIONS_DIR = os.environ.get(\"DSA_SOLUTIONS_DIR\") or os.path.join(\n"
        "    os.path.dirname(os.path.abspath(__file__)), \"..\", \"solutions\"\n"
        ")\n"
        "sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))\n"
        f"from {module} import {', '.join(exports)}  # noqa: E402\n"
        f"# {HEADER_END} ----\n\n"
    )


_PY_DANGEROUS: Tuple[Rule, ...] = (
    (
        r"^\s*(?:import|from)\s+(?:os|subprocess|socket|shutil|ctypes|multiprocessing|threading|urllib|http|"
        r"requests|pathlib|importlib|pickle|marshal|signal|asyncio|ftplib|smtplib|webbrowser|tempfile|io|builtins)\b",
        "imports a module with filesystem, process or network access (only pure-computation stdlib modules are allowed)",
    ),
    (r"(?<![\w.])(?:eval|exec|compile|__import__|open|input|breakpoint|globals|setattr|delattr)\s*\(",
     "calls a forbidden builtin (eval/exec/compile/__import__/open/input/breakpoint/globals/setattr/delattr)"),
    (r"__(?:builtins|subclasses|globals|code|loader)__", "accesses interpreter internals"),
    (r"\bsys\.(?:exit|modules|stdin|path)\b", "uses sys.exit / sys.modules / sys.stdin / sys.path"),
)

PYTHON = LanguageProfile(
    name="python",
    display_name="Python 3.12",
    fence="python",
    image="python:3.12-slim@sha256:05cda9777409a9c3ffddd94a4c476b79f0769a0b4857f0c7ed9226b6800b0d6f",
    host_command="python",
    solution_pattern="problem_{nn}.py",
    test_pattern="test_problem_{nn}.py",
    test_arg_prefix="",
    all_tests_glob="test_problem_*.py",
    test_command=("python", "-m", "unittest", "discover", "-s", "tests", "-p", "{tests}", "-v"),
    tests_run_regex=r"^Ran (\d+) tests? in",
    conventions=(
        "- Target Python 3.12 using only the standard library.\n"
        "- Use snake_case names, type hints and short docstrings. No prints, no input(), no top-level code "
        "other than definitions.\n"
        "- Allowed imports: math, random, itertools, collections, heapq, bisect, functools, string, typing, "
        "dataclasses, sys (only for sys.setrecursionlimit). Nothing with file, process or network access.\n"
        "- Tests use `unittest`: one or more `unittest.TestCase` subclasses with methods named `test_*`. "
        "`unittest`, `TestCase` and every exported symbol are ALREADY imported by a generated header: do "
        "not import them again and do not import the solution module.\n"
        "- For large-input tests build data deterministically (e.g. `random.Random(42)`) and keep each "
        "test well under one second.\n"
        "- If inputs need helper types (ListNode, TreeNode, ...) define them in the solution and list them "
        "in exports so tests can construct inputs."
    ),
    starter_hint="Same signatures and docstrings, function bodies replaced with `raise NotImplementedError`; "
    "helper data types (e.g. ListNode) must be complete and working.",
    header=_py_header,
    footer=lambda exports, code: "",
    solution_rules=_PY_DANGEROUS,
    test_rules=_PY_DANGEROUS
    + ((r"^\s*(?:from|import)\s+problem_\d+", "imports the solution module itself (the generated header already does)"),),
)


# --------------------------------------------------------------------------- javascript

def _js_header(nn: str, solution_file: str, exports: Sequence[str]) -> str:
    return (
        "// ---- Generated import header (do not edit) ----\n"
        "// Runs these tests against ../solutions by default. To test your own code, run\n"
        "// from the day folder:\n"
        f"//   DSA_SOLUTIONS_DIR=practice node --test tests/problem-{nn}.test.js\n"
        "'use strict';\n"
        "const path = require('node:path');\n"
        "const { describe, test } = require('node:test');\n"
        "const assert = require('node:assert/strict');\n"
        f"const {{ {', '.join(exports)} }} = require(\n"
        "  path.resolve(process.env.DSA_SOLUTIONS_DIR || path.join(__dirname, '..', 'solutions'), "
        f"'{solution_file}')\n"
        ");\n"
        f"// {HEADER_END} ----\n\n"
    )


def _js_footer(exports: Sequence[str], code: str) -> str:
    if re.search(r"\bmodule\.exports\b", code):
        return ""
    return f"\nmodule.exports = {{ {', '.join(exports)} }};\n"


_JS_DANGEROUS: Tuple[Rule, ...] = (
    (r"\brequire\s*\(", "calls require() (no modules are allowed; the harness handles imports/exports)"),
    (r"\bimport\s*\(|^\s*import\s", "uses ES module imports"),
    (r"\bprocess\s*[.\[]", "accesses the process object"),
    (r"\b(?:eval|Function)\s*\(|\bnew\s+Function\b", "uses eval / Function constructor"),
    (r"\b(?:fetch|XMLHttpRequest|WebSocket)\b", "uses network APIs"),
    (r"\bglobalThis\b|\b__proto__\b|\bconstructor\s*\.\s*constructor\b", "accesses global or prototype internals"),
)

JAVASCRIPT = LanguageProfile(
    name="javascript",
    display_name="JavaScript (Node.js 22)",
    fence="javascript",
    image="node:22-slim@sha256:c3de60bf2f9dd0ac6370e6117950ff62d6e339527e7472301c9c78a017978392",
    host_command="node",
    solution_pattern="problem-{nn}.js",
    test_pattern="problem-{nn}.test.js",
    test_arg_prefix="tests/",
    all_tests_glob="tests/*.test.js",
    test_command=("node", "--test", "--test-reporter=tap", "{tests}"),
    tests_run_regex=r"^# tests (\d+)",
    conventions=(
        "- Target Node.js 22, CommonJS, no external packages, 'use strict' semantics.\n"
        "- Use camelCase names and JSDoc comments. No console output, no top-level code other than "
        "definitions.\n"
        "- Do NOT call require() and do NOT write module.exports in the solution: the harness appends "
        "`module.exports = { ...exports }` automatically.\n"
        "- Tests use `describe`/`test` from node:test and `assert` from node:assert/strict. These and every "
        "exported symbol are ALREADY imported by a generated header: do not require anything.\n"
        "- For large-input tests generate data deterministically (e.g. a small seeded LCG) and keep each "
        "test well under one second.\n"
        "- If inputs need helper classes (ListNode, TreeNode, ...) define them in the solution and list them "
        "in exports so tests can construct inputs."
    ),
    starter_hint="Same signatures and JSDoc, function bodies replaced with `throw new Error('Not implemented');` "
    "helper classes (e.g. ListNode) must be complete and working.",
    header=_js_header,
    footer=_js_footer,
    solution_rules=_JS_DANGEROUS,
    test_rules=_JS_DANGEROUS,
)

PROFILES: Dict[str, LanguageProfile] = {p.name: p for p in (PYTHON, JAVASCRIPT)}
ALIASES = {"py": "python", "js": "javascript", "node": "javascript"}


def get_profile(name: str) -> LanguageProfile:
    key = ALIASES.get(name.lower(), name.lower())
    if key not in PROFILES:
        raise ConfigError(f"unsupported language {name!r}; supported: {', '.join(PROFILES)}")
    return PROFILES[key]
