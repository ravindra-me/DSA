"""End-to-end: plan -> generate (fake AI, real sandboxed tests, repair loop)
-> validate -> apply -> idempotent re-runs."""

import json
import unittest
from datetime import date

from helpers import FakeProvider, TempRepo, roadmap, temp_settings

from dsa_agent.errors import ConfigError, ValidationFailed
from dsa_agent.generate_lesson import generate_lesson
from dsa_agent.progress import load_progress
from dsa_agent.sandbox import ProcessSandbox
from dsa_agent.select_topic import Request, plan_lesson
from dsa_agent.update_progress import apply_staging
from dsa_agent.validate_solution import run_practice, validate_lesson_dir


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self._repo = TempRepo()
        self.root = self._repo.__enter__()
        self.settings = temp_settings(self.root)
        self.roadmap = roadmap(self.settings)
        self.sandbox = ProcessSandbox(self.settings.sandbox)

    def tearDown(self):
        self._repo.__exit__(None, None, None)

    def generate(self, on="2026-10-08", provider=None, **kw):
        progress = load_progress(self.settings.progress_path)
        plan, reason = plan_lesson(progress, self.roadmap, self.settings, Request(date=date.fromisoformat(on), problems=2, **kw))
        if plan is None:
            return None, reason
        self.runs = getattr(self, "runs", 0) + 1
        staging = self.root / f"staging-{self.runs}"
        record = generate_lesson(self.settings, plan, provider or FakeProvider(), self.sandbox, staging)
        return staging, record

    def test_full_day_generation(self):
        provider = FakeProvider()
        staging, record = self.generate(provider=provider)
        self.assertEqual(provider.calls, ["lesson", "problem1", "problem2", "repair"])
        self.assertEqual(record["entry"]["topic"], "big-o")

        day_dir = staging / "day-001"
        expected = [
            "README.md", "lesson.json",
            "exercises/problem-01.md", "exercises/problem-02.md",
            "solutions/problem-01.md", "solutions/problem_01.py", "solutions/problem-02.md", "solutions/problem_02.py",
            "tests/test_problem_01.py", "tests/test_problem_02.py",
            "practice/problem_01.py", "practice/problem_02.py",
        ]
        for rel in expected:
            self.assertTrue((day_dir / rel).is_file(), rel)
        readme = (day_dir / "README.md").read_text()
        for heading in ("## Topic", "## Learning Objectives", "## Concept Explanation", "### When NOT to use it",
                        "## Example", "## Visual Explanation", "## Complexity", "## Interview Perspective"):
            self.assertIn(heading, readme)
        exercise = (day_dir / "exercises/problem-02.md").read_text()
        self.assertNotIn("seen.add", exercise)  # no solution leak
        self.assertIn("return None", (day_dir / "solutions/problem_02.py").read_text())  # repaired version
        self.assertEqual(json.loads((day_dir / "lesson.json").read_text())["problems"][1]["repairs"], 1)

        self.assertTrue(validate_lesson_dir(day_dir, self.sandbox, 6).ok)
        self.assertFalse(self.settings.progress_path.exists(), "generation must not touch the repository")

        result = apply_staging(self.settings, self.roadmap, staging)
        self.assertTrue(result.applied)
        self.assertEqual(result.commit_message, "chore(dsa): add day 1 - Big O Notation & Complexity Analysis")
        progress = load_progress(self.settings.progress_path)
        self.assertEqual((progress["currentDay"], progress["topicsCompleted"]), (1, ["big-o"]))
        self.assertEqual(progress["upcomingRevisions"][0], {"topic": "big-o", "dueDay": 8, "stage": 1, "requested": False})
        self.assertTrue((self.settings.lessons_dir / "day-001" / "README.md").is_file())
        self.assertIn("day-001/README.md", (self.settings.lessons_dir / "README.md").read_text())

        # Re-applying the same staging (e.g. a retried publish job) is a no-op.
        self.assertFalse(apply_staging(self.settings, self.roadmap, staging).applied)
        # A second run on the same date generates nothing.
        self.assertEqual(self.generate()[0], None)
        # The next day moves on to the next roadmap topic.
        _, record2 = self.generate(on="2026-10-09")
        self.assertEqual((record2["entry"]["day"], record2["entry"]["topic"]), (2, "arrays"))

    def test_practice_detects_attempts(self):
        staging, _ = self.generate()
        apply_staging(self.settings, self.roadmap, staging)
        day_dir = self.settings.lessons_dir / "day-001"
        self.assertEqual([r["attempted"] for r in run_practice(day_dir, self.sandbox)], [False, False])
        from helpers import COUNT_PAIRS_SOLUTION

        (day_dir / "practice/problem_01.py").write_text(COUNT_PAIRS_SOLUTION)
        rows = run_practice(day_dir, self.sandbox)
        self.assertEqual((rows[0]["attempted"], rows[0]["passed"]), (True, True))

    def test_force_regeneration_replaces_day(self):
        staging, _ = self.generate()
        apply_staging(self.settings, self.roadmap, staging)
        staging2, record = self.generate(force=True)
        self.assertEqual((record["mode"], record["entry"]["day"]), ("replace", 1))
        self.assertTrue(apply_staging(self.settings, self.roadmap, staging2).applied)
        self.assertEqual(len(load_progress(self.settings.progress_path)["lessons"]), 1)

    def test_concurrent_publish_of_same_day_is_rejected(self):
        staging_a, _ = self.generate()
        staging_b, _ = self.generate(extra=True)  # also planned as day 1 against empty progress
        apply_staging(self.settings, self.roadmap, staging_a)
        with self.assertRaises(ConfigError):
            apply_staging(self.settings, self.roadmap, staging_b)

    def test_unrepairable_code_fails_without_touching_repo(self):
        with self.assertRaises(ValidationFailed):
            self.generate(provider=FakeProvider(fail_repairs=True))
        self.assertFalse(self.settings.progress_path.exists())
        self.assertFalse(self.settings.lessons_dir.exists())


if __name__ == "__main__":
    unittest.main()
