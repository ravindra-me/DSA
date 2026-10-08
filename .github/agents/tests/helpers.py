"""Shared fixtures for the agent self-tests: import path setup, settings for a
throwaway repository, and a scripted fake AI provider."""

from __future__ import annotations

import datetime
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")

from dsa_agent.ai import Provider  # noqa: E402
from dsa_agent.config import Settings, load_settings  # noqa: E402
from dsa_agent.roadmap import Roadmap, load_roadmap  # noqa: E402


def temp_settings(tmp: Path, **env: str) -> Settings:
    return load_settings(repo_root=tmp, env={"DSA_SANDBOX": "process", **env})


def roadmap(settings: Settings) -> Roadmap:
    return load_roadmap(settings.roadmap_path)


def lesson(day: int, topic: str, kind: str = "new", date: Optional[str] = None, **extra: Any) -> Dict[str, Any]:
    entry = {
        "day": day,
        "date": date or (datetime.date(2026, 1, 1) + datetime.timedelta(days=day - 1)).isoformat(),
        "topic": topic,
        "kind": kind,
        "status": "generated",
        "problemsGenerated": 3,
        "problemsCompleted": 0,
        "problems": [{"number": 1, "title": f"{topic} problem {day}", "difficulty": "Easy"}],
    }
    entry.update(extra)
    return entry


def progress_of(*lessons: Dict[str, Any]) -> Dict[str, Any]:
    return {"schemaVersion": 1, "lessons": list(lessons)}


class TempRepo:
    def __enter__(self) -> Path:
        self._tmp = tempfile.TemporaryDirectory(prefix="dsa-agent-test-")
        return Path(self._tmp.name)

    def __exit__(self, *exc: object) -> None:
        self._tmp.cleanup()


# --------------------------------------------------------------------------- fake AI

COUNT_PAIRS_SOLUTION = '''from collections import Counter
from typing import List


def count_pairs(nums: List[int], target: int) -> int:
    """Count index pairs i < j with nums[i] + nums[j] == target in O(n)."""
    seen: Counter = Counter()
    pairs = 0
    for value in nums:
        pairs += seen[target - value]
        seen[value] += 1
    return pairs
'''

COUNT_PAIRS_STARTER = '''from typing import List


def count_pairs(nums: List[int], target: int) -> int:
    """Count index pairs i < j with nums[i] + nums[j] == target."""
    raise NotImplementedError
'''

COUNT_PAIRS_TESTS = '''class TestCountPairs(unittest.TestCase):
    def test_example(self):
        self.assertEqual(count_pairs([1, 2, 3, 4], 5), 2)

    def test_empty(self):
        self.assertEqual(count_pairs([], 3), 0)

    def test_single_element(self):
        self.assertEqual(count_pairs([3], 6), 0)

    def test_duplicates(self):
        self.assertEqual(count_pairs([2, 2, 2], 4), 3)

    def test_negatives_and_zero(self):
        self.assertEqual(count_pairs([-1, 1, 0, 0], 0), 2)

    def test_large_input(self):
        self.assertEqual(count_pairs([1] * 2000, 2), 2000 * 1999 // 2)
'''

FIRST_DUP_BUGGY = '''from typing import List, Optional


def first_duplicate(nums: List[int]) -> Optional[int]:
    """Return the value whose second occurrence comes first, or None."""
    seen = set()
    for value in nums:
        if value in seen:
            return value
        seen.add(value)
    return -1
'''

FIRST_DUP_FIXED = FIRST_DUP_BUGGY.replace("return -1", "return None")

FIRST_DUP_STARTER = '''from typing import List, Optional


def first_duplicate(nums: List[int]) -> Optional[int]:
    """Return the value whose second occurrence comes first, or None."""
    raise NotImplementedError
'''

FIRST_DUP_TESTS = '''class TestFirstDuplicate(unittest.TestCase):
    def test_example(self):
        self.assertEqual(first_duplicate([2, 1, 3, 5, 3, 2]), 3)

    def test_no_duplicate(self):
        self.assertIsNone(first_duplicate([1, 2, 3]))

    def test_empty(self):
        self.assertIsNone(first_duplicate([]))

    def test_single(self):
        self.assertIsNone(first_duplicate([7]))

    def test_negatives(self):
        self.assertEqual(first_duplicate([-5, 0, -5]), -5)

    def test_all_same(self):
        self.assertEqual(first_duplicate([4, 4, 4]), 4)

    def test_large_input(self):
        self.assertEqual(first_duplicate(list(range(10000)) + [9999]), 9999)
'''


def _problem_spec(title: str, export: str) -> Dict[str, Any]:
    return {
        "title": title,
        "concept": "hash-based counting",
        "statement": f"Solve **{title}** for an integer array as described in the lesson examples below.",
        "input": "`nums`: list of integers",
        "output": "see statement",
        "constraints": ["0 <= len(nums) <= 10^5"],
        "examples": [{"input": "nums = [1, 2]", "output": "...", "explanation": ""}, {"input": "nums = []", "output": "...", "explanation": "empty"}],
        "expectedApproach": "Use a hash map to avoid the quadratic scan.",
        "signature": f"def {export}(nums: List[int]) -> ...:",
        "exports": [export],
    }


LESSON = {
    "title": "Big O Notation",
    "summary": "Big O lets you predict how an algorithm scales before you run it, which is the foundation of every later lesson.",
    "objectives": ["Explain Big O", "Compare growth rates", "Analyse loops"],
    "concept": {
        "whatItIs": "Big O describes an upper bound on how running time grows with input size n, ignoring constants.",
        "whyItExists": "Wall-clock timings depend on hardware; growth rates let us compare algorithms independent of machines.",
        "whenToUse": "Whenever you choose between algorithms or data structures, or estimate if a solution fits the limits.",
        "whenNotToUse": "For tiny inputs or when constant factors dominate, measure instead of relying on asymptotics alone.",
        "howItWorks": "Count the dominant operations as a function of n, drop constants and lower-order terms, keep the fastest-growing term.",
        "commonMistakes": ["Ignoring hidden loops in library calls", "Confusing best and worst case"],
        "realWorldApplications": ["Database query planning", "Capacity planning"],
    },
    "example": "Summing an array touches each element once, so it is O(n): `total += x` runs n times.",
    "visual": "n=1  *\nn=2  **\nn=4  ****",
    "complexity": {"time": "O(n) for a single pass", "space": "O(1) extra", "notes": "Amortised analysis averages occasional expensive steps."},
    "interview": [
        {"question": "What is Big O?", "answerHint": "Upper bound on growth"},
        {"question": "O(n log n) vs O(n^2)?", "answerHint": "Crossover point"},
        {"question": "Amortised O(1)?", "answerHint": "Dynamic array append"},
    ],
    "conceptsCovered": ["time complexity", "space complexity"],
    "problems": [_problem_spec("Count Pairs With Target Sum", "count_pairs"), _problem_spec("First Duplicate", "first_duplicate")],
}


def _problem_payload(solution: str, tests: str, starter: str) -> Dict[str, Any]:
    return {
        "approach": "Use a hash structure to remember what we have already seen.",
        "reasoning": "Brute force compares every pair in O(n^2); remembering seen values makes each check O(1).",
        "algorithm": ["Create an empty map", "Scan once, updating the answer"],
        "complexity": {"time": "O(n)", "space": "O(n)"},
        "edgeCases": ["Empty input", "All duplicates"],
        "solutionCode": solution,
        "testCode": tests,
        "starterCode": starter,
    }


class FakeProvider(Provider):
    """Returns scripted responses based on which prompt it receives.

    Problem 2's first solution is buggy, so the repair loop is exercised.
    """

    name = "fake"

    def __init__(self, lesson: Optional[Dict[str, Any]] = None, fail_repairs: bool = False) -> None:
        super().__init__("fake-model")
        self.lesson = lesson or LESSON
        self.fail_repairs = fail_repairs
        self.calls: List[str] = []

    def complete(self, system: str, user: str) -> str:
        if user.startswith("Create Day"):
            self.calls.append("lesson")
            return json.dumps(self.lesson)
        if "failed automated validation" in user:
            self.calls.append("repair")
            fixed = FIRST_DUP_BUGGY if self.fail_repairs else FIRST_DUP_FIXED
            return json.dumps({"diagnosis": "returned -1 instead of None", **{k: v for k, v in _problem_payload(fixed, FIRST_DUP_TESTS, FIRST_DUP_STARTER).items() if k in ("solutionCode", "testCode", "starterCode")}})
        if "## Problem 1 " in user:
            self.calls.append("problem1")
            return "```json\n" + json.dumps(_problem_payload(COUNT_PAIRS_SOLUTION, COUNT_PAIRS_TESTS, COUNT_PAIRS_STARTER)) + "\n```"
        if "## Problem 2 " in user:
            self.calls.append("problem2")
            return json.dumps(_problem_payload(FIRST_DUP_BUGGY, FIRST_DUP_TESTS, FIRST_DUP_STARTER))
        raise AssertionError(f"unexpected prompt: {user[:200]}")
