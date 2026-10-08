import json
import unittest

from helpers import TempRepo, lesson, progress_of, roadmap, temp_settings

from dsa_agent.config import load_settings
from dsa_agent.errors import ConfigError
from dsa_agent.progress import recompute, upsert_lesson, validate_progress
from dsa_agent.prompts import TEMPLATES, render


class ConfigTests(unittest.TestCase):
    def test_repository_config_and_roadmap_load(self):
        with TempRepo() as tmp:
            settings = temp_settings(tmp)
            rm = roadmap(settings)
        self.assertGreaterEqual(len(rm), 50)
        self.assertEqual(rm.topics[0].id, "big-o")
        self.assertEqual(settings.lessons_dir, tmp.resolve() / "dsa")

    def test_env_overrides_and_validation(self):
        with TempRepo() as tmp:
            settings = load_settings(tmp, {"DSA_LANGUAGE": "JavaScript", "DSA_SANDBOX": "process", "DSA_AI_PROVIDER": ""})
            self.assertEqual((settings.language, settings.ai.provider), ("javascript", "auto"))
            with self.assertRaises(ConfigError):
                load_settings(tmp, {"DSA_AI_PROVIDER": "nope"})
            with self.assertRaises(ConfigError):
                load_settings(tmp, {"DSA_TIMEZONE": "Mars/Base"})
            with self.assertRaises(ConfigError):
                load_settings(tmp, {"OPENAI_BASE_URL": "http://evil.example"})

    def test_all_prompt_templates_render(self):
        with TempRepo() as tmp:
            settings = temp_settings(tmp)
        for name in TEMPLATES:
            text = (settings.prompts_dir / f"{name}.md").read_text()
            import re

            keys = set(re.findall(r"\{\{\s*([a-z_]+)\s*\}\}", text))
            rendered = render(settings.prompts_dir, name, {k: f"<{k}>" for k in keys})
            self.assertNotIn("{{", rendered)
        with self.assertRaises(ConfigError):
            render(settings.prompts_dir, "lesson", {})


class ProgressTests(unittest.TestCase):
    def setUp(self):
        self._repo = TempRepo()
        self.settings = temp_settings(self._repo.__enter__())
        self.roadmap = roadmap(self.settings)

    def tearDown(self):
        self._repo.__exit__(None, None, None)

    def test_recompute_derives_summary(self):
        p = recompute(progress_of(lesson(1, "big-o", problemsCompleted=2, status="completed"), lesson(2, "arrays")), self.roadmap, self.settings)
        self.assertEqual(p["currentDay"], 2)
        self.assertEqual(p["topicsCompleted"], ["big-o", "arrays"])
        self.assertEqual(p["nextRoadmapTopic"], "strings")
        self.assertEqual(p["stats"]["problemsCompleted"], 2)
        self.assertTrue(p["lessons"][0]["revisionRequired"])
        json.dumps(p)

    def test_upsert_replaces_and_clears_revision_request(self):
        p = progress_of(lesson(1, "big-o", requestRevision=True), lesson(2, "arrays"))
        p = upsert_lesson(p, lesson(3, "big-o", kind="revision", revisionStage=0))
        self.assertFalse(p["lessons"][0]["requestRevision"])
        p = upsert_lesson(p, lesson(3, "strings"))
        self.assertEqual([l["topic"] for l in p["lessons"]], ["big-o", "arrays", "strings"])

    def test_invalid_progress_is_rejected(self):
        bad = [
            {"schemaVersion": 2, "lessons": []},
            progress_of(lesson(1, "a"), lesson(1, "b")),
            progress_of(lesson(1, "a", date="01-01-2026")),
            progress_of(lesson(1, "a", status="done")),
            progress_of(lesson(1, "a", problemsCompleted=9)),
        ]
        for data in bad:
            with self.subTest(data=data), self.assertRaises(ConfigError):
                validate_progress(data)


if __name__ == "__main__":
    unittest.main()
