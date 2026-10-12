# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_05.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_05 import min_window  # noqa: E402
# ---- End of generated header ----

class TestMinWindow(TestCase):
    def test_example_cases(self):
        self.assertEqual(min_window("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(min_window("a", "a"), "a")
        self.assertEqual(min_window("a", "aa"), "")

    def test_no_solution(self):
        self.assertEqual(min_window("abcdef", "z"), "")
        self.assertEqual(min_window("abc", "defg"), "")

    def test_duplicates_in_t(self):
        self.assertEqual(min_window("aaabc", "aa"), "aa")
        self.assertEqual(min_window("aaabc", "aaa"), "aaa")

    def test_all_same_chars(self):
        self.assertEqual(min_window("aaaaa", "a"), "a")
        self.assertEqual(min_window("aaaaa", "aaa"), "aaa")

    def test_s_shorter_than_t(self):
        self.assertEqual(min_window("abc", "abcde"), "")

    def test_large_input_performance(self):
        # Construct a large case to ensure O(N) efficiency
        # s = "abc...abc" (repeated), t = "abc"
        # This ensures the window logic runs efficiently
        n = 50000
        s = "abc" * n
        t = "abc"
        # The min window should be "abc" (length 3)
        result = min_window(s, t)
        self.assertEqual(result, "abc")

    def test_t_not_in_s(self):
        self.assertEqual(min_window("abcde", "fgh"), "")
