import dataclasses
import shutil
import unittest

from helpers import (
    COUNT_PAIRS_SOLUTION,
    COUNT_PAIRS_STARTER,
    COUNT_PAIRS_TESTS,
    TempRepo,
    temp_settings,
)

from dsa_agent.languages import JAVASCRIPT, PYTHON, strip_header
from dsa_agent.sandbox import ProcessSandbox
from dsa_agent.validate_solution import ProblemCode, problem_files, static_issues, validate_problem


def code(solution=COUNT_PAIRS_SOLUTION, tests=COUNT_PAIRS_TESTS, starter=COUNT_PAIRS_STARTER):
    return ProblemCode(1, ["count_pairs"], solution, tests, starter)


class StaticCheckTests(unittest.TestCase):
    def test_clean_code_passes(self):
        self.assertEqual(static_issues(PYTHON, code()), [])

    def test_dangerous_python_is_rejected(self):
        for snippet in ("import os", "import subprocess", "from socket import socket", "open('/etc/passwd')",
                        "eval('1')", "__import__('os')", "x.__subclasses__()", "import urllib.request"):
            with self.subTest(snippet=snippet):
                self.assertTrue(static_issues(PYTHON, code(solution=COUNT_PAIRS_SOLUTION + "\n" + snippet)))

    def test_regex_compile_is_allowed(self):
        self.assertEqual(static_issues(PYTHON, code(solution="import re\nP = re.compile('a')\n" + COUNT_PAIRS_SOLUTION)), [])

    def test_tests_must_not_import_solution(self):
        self.assertTrue(static_issues(PYTHON, code(tests="from problem_01 import count_pairs\n" + COUNT_PAIRS_TESTS)))

    def test_dangerous_javascript_is_rejected(self):
        js = ProblemCode(1, ["f"], "function f() { return require('fs'); }", "test('x', () => {});", "function f() {}")
        self.assertTrue(static_issues(JAVASCRIPT, js))
        js = ProblemCode(1, ["f"], "function f() { return process.env.KEY; }", "test('x', () => {});", "function f() {}")
        self.assertTrue(static_issues(JAVASCRIPT, js))

    def test_header_is_stripped_before_checks(self):
        assembled = problem_files(PYTHON, code())["tests/test_problem_01.py"]
        self.assertIn("import os", assembled)
        self.assertEqual(strip_header(assembled).strip(), COUNT_PAIRS_TESTS.strip())


class SandboxValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._repo = TempRepo()
        cls.settings = temp_settings(cls._repo.__enter__())
        cls.sandbox = ProcessSandbox(cls.settings.sandbox)

    @classmethod
    def tearDownClass(cls):
        cls._repo.__exit__(None, None, None)

    def test_correct_solution_passes(self):
        result = validate_problem(PYTHON, self.sandbox, code(), 6)
        self.assertTrue(result.ok, result.report)
        self.assertEqual(result.tests_run, 6)

    def test_wrong_solution_fails_with_output(self):
        result = validate_problem(PYTHON, self.sandbox, code(solution=COUNT_PAIRS_SOLUTION.replace("pairs += ", "pairs -= ")), 6)
        self.assertFalse(result.ok)
        self.assertIn("FAIL", result.report)

    def test_too_few_tests_fails(self):
        self.assertFalse(validate_problem(PYTHON, self.sandbox, code(), 10).ok)

    def test_vacuous_tests_are_detected(self):
        vacuous = "\n".join(
            f"class T{i}(unittest.TestCase):\n    def test_{i}(self):\n        self.assertTrue(True)\n" for i in range(6)
        )
        result = validate_problem(PYTHON, self.sandbox, code(tests=vacuous), 6)
        self.assertFalse(result.ok)
        self.assertIn("starter stub", result.report)

    def test_infinite_loop_times_out(self):
        sandbox_settings = dataclasses.replace(self.settings.sandbox, timeout_seconds=3)
        slow = COUNT_PAIRS_SOLUTION.replace("seen: Counter = Counter()", "while True:\n        pass")
        result = validate_problem(PYTHON, ProcessSandbox(sandbox_settings), code(solution=slow), 6)
        self.assertFalse(result.ok)
        self.assertIn("timed out", result.report)

    @unittest.skipUnless(shutil.which("node"), "node is not installed")
    def test_javascript_profile_end_to_end(self):
        solution = "function add(a, b) {\n  return a + b;\n}\n"
        starter = "function add(a, b) {\n  throw new Error('Not implemented');\n}\n"
        tests = "describe('add', () => {\n" + "".join(
            f"  test('case {i}', () => {{ assert.equal(add({i}, 1), {i + 1}); }});\n" for i in range(6)
        ) + "});\n"
        result = validate_problem(JAVASCRIPT, self.sandbox, ProblemCode(1, ["add"], solution, tests, starter), 6)
        self.assertTrue(result.ok, result.report)
        self.assertEqual(result.tests_run, 6)


if __name__ == "__main__":
    unittest.main()
