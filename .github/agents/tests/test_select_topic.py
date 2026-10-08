import dataclasses
import unittest
from datetime import date

from helpers import TempRepo, lesson, progress_of, roadmap, temp_settings

from dsa_agent.errors import ConfigError
from dsa_agent.select_topic import Request, difficulty_ladder, plan_lesson


class SelectTopicTests(unittest.TestCase):
    def setUp(self):
        self._repo = TempRepo()
        self.settings = temp_settings(self._repo.__enter__())
        self.roadmap = roadmap(self.settings)

    def tearDown(self):
        self._repo.__exit__(None, None, None)

    def plan(self, progress, on="2026-03-01", **kw):
        return plan_lesson(progress, self.roadmap, self.settings, Request(date=date.fromisoformat(on), **kw))

    def test_first_lesson_is_first_roadmap_topic(self):
        plan, _ = self.plan(progress_of())
        self.assertEqual((plan.day, plan.topic.id, plan.kind, plan.mode), (1, "big-o", "new", "append"))
        self.assertEqual(plan.slug, "day-001")

    def test_follows_roadmap_order(self):
        plan, _ = self.plan(progress_of(lesson(1, "big-o"), lesson(2, "arrays")))
        self.assertEqual((plan.day, plan.topic.id), (3, "strings"))

    def test_same_date_is_skipped_idempotently(self):
        progress = progress_of(lesson(1, "big-o", date="2026-03-01"))
        plan, reason = self.plan(progress)
        self.assertIsNone(plan)
        self.assertIn("already exists", reason)

    def test_force_regenerates_same_day_and_topic(self):
        progress = progress_of(lesson(1, "big-o", date="2026-02-28"), lesson(2, "arrays", date="2026-03-01"))
        plan, _ = self.plan(progress, force=True)
        self.assertEqual((plan.day, plan.topic.id, plan.mode), (2, "arrays", "replace"))

    def test_extra_lesson_appends_on_same_date(self):
        progress = progress_of(lesson(1, "big-o", date="2026-03-01"))
        plan, _ = self.plan(progress, extra=True)
        self.assertEqual((plan.day, plan.topic.id, plan.mode), (2, "arrays", "append"))

    def test_manual_topic_new_and_revision(self):
        plan, _ = self.plan(progress_of(lesson(1, "big-o")), topic="binary-search")
        self.assertEqual((plan.topic.id, plan.kind), ("binary-search", "new"))
        plan, _ = self.plan(progress_of(lesson(1, "big-o")), topic="Big O Notation & Complexity Analysis")
        self.assertEqual((plan.topic.id, plan.kind), ("big-o", "revision"))

    def test_unknown_topic_is_rejected(self):
        with self.assertRaises(ConfigError):
            self.plan(progress_of(), topic="quantum-sort")

    def test_spaced_revision_becomes_due(self):
        topics = ["big-o", "arrays", "strings", "recursion", "math-basics", "bit-manipulation", "linked-list"]
        history = progress_of(*(lesson(i + 1, t) for i, t in enumerate(topics)))
        plan, _ = self.plan(history)  # day 8 = big-o learned day 1 + 7
        self.assertEqual((plan.day, plan.topic.id, plan.kind, plan.revision_stage), (8, "big-o", "revision", 1))
        self.assertIn("big-o problem 1", plan.previous_problems)

    def test_revisions_respect_minimum_gap(self):
        topics = ["big-o", "arrays", "strings", "recursion", "math-basics", "bit-manipulation", "linked-list"]
        lessons = [lesson(i + 1, t) for i, t in enumerate(topics)]
        lessons.append(lesson(8, "big-o", kind="revision", revisionStage=1))
        plan, _ = self.plan(progress_of(*lessons))  # arrays is due (2+7=9) but gap is 0 < 2
        self.assertEqual((plan.topic.id, plan.kind), ("linked-list-techniques", "new"))

    def test_requested_revision_skips_gap(self):
        lessons = [lesson(1, "big-o", requestRevision=True), lesson(2, "arrays", kind="new")]
        lessons.append(lesson(3, "arrays", kind="revision", revisionStage=0))
        plan, _ = self.plan(progress_of(*lessons))
        self.assertEqual((plan.topic.id, plan.kind, plan.revision_stage), ("big-o", "revision", 0))

    def test_late_revision_satisfies_all_due_stages(self):
        lessons = [lesson(1, "big-o")] + [lesson(d, f"x-{d}") for d in range(2, 30)]
        plan, _ = self.plan(progress_of(*lessons), on="2026-06-01")
        self.assertEqual((plan.topic.id, plan.revision_stage), ("big-o", 2))  # day 30 >= 1+7 and 1+21

    def test_refuses_to_go_back_in_time(self):
        with self.assertRaises(ConfigError):
            self.plan(progress_of(lesson(1, "big-o", date="2026-03-05")), on="2026-03-01")

    def test_roadmap_complete_falls_back_to_stalest_topic(self):
        all_topics = [t.id for t in self.roadmap.topics]
        lessons = [lesson(i + 1, t, revisionStage=0) for i, t in enumerate(all_topics)]
        settings = dataclasses.replace(self.settings, revision=dataclasses.replace(self.settings.revision, intervals=()))
        plan, _ = plan_lesson(progress_of(*lessons), self.roadmap, settings, Request(date=date(2027, 1, 1)))
        self.assertEqual((plan.topic.id, plan.kind), (all_topics[0], "revision"))

    def test_invalid_inputs(self):
        with self.assertRaises(ConfigError):
            self.plan(progress_of(), problems=50)
        with self.assertRaises(ConfigError):
            self.plan(progress_of(), difficulty="insane")


class DifficultyLadderTests(unittest.TestCase):
    def test_progressive_five(self):
        self.assertEqual(difficulty_ladder(5, "progressive"), ("Easy", "Easy/Medium", "Medium", "Medium/Hard", "Hard"))

    def test_single_and_levels(self):
        self.assertEqual(difficulty_ladder(1, "progressive"), ("Medium",))
        self.assertEqual(set(difficulty_ladder(4, "hard")), {"Medium/Hard", "Hard"})
        self.assertEqual(difficulty_ladder(3, "progressive", "revision")[0], "Easy/Medium")


if __name__ == "__main__":
    unittest.main()
