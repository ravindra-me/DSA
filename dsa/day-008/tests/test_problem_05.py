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
from problem_05 import min_window_subsequence  # noqa: E402
# ---- End of generated header ----

class TestMinWindowSubsequence(TestCase):
    def test_example_1(self):
        s1 = "abcdebdde"
        s2 = "bde"
        self.assertEqual(min_window_subsequence(s1, s2), "bcde")

    def test_example_2_no_match(self):
        s1 = "jmeqqaqapq"
        s2 = "at"
        self.assertEqual(min_window_subsequence(s1, s2), "")

    def test_s2_longer_than_s1(self):
        self.assertEqual(min_window_subsequence("abc", "abcd"), "")

    def test_single_character_match(self):
        self.assertEqual(min_window_subsequence("a", "a"), "a")
        self.assertEqual(min_window_subsequence("b", "a"), "")

    def test_tie_breaking_prefers_earliest_start(self):
        s1 = "abaca"
        s2 = "aa"
        self.assertEqual(min_window_subsequence(s1, s2), "aba")

    def test_repeated_characters(self):
        s1 = "aaaaa"
        s2 = "aa"
        self.assertEqual(min_window_subsequence(s1, s2), "aa")

    def test_whole_string_match(self):
        s1 = "abcdefg"
        s2 = "abcdefg"
        self.assertEqual(min_window_subsequence(s1, s2), "abcdefg")

    def test_partial_match_at_end_only(self):
        s1 = "xyzabcde"
        s2 = "bde"
        self.assertEqual(min_window_subsequence(s1, s2), "bcde")

    def test_large_input_performance(self):
        pattern = "abcdefghij"
        s1 = (pattern * 2000) + "xyz"
        s2 = "aj" * 50

        expected_len = 50 * len(pattern)
        result = min_window_subsequence(s1, s2)
        self.assertEqual(len(result), expected_len)
        self.assertTrue(result.startswith("a"))
        self.assertTrue(result.endswith("j"))
