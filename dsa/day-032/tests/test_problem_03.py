# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_03.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_03 import remove_k_duplicates  # noqa: E402
# ---- End of generated header ----

import unittest
import random

class TestRemoveKDuplicates(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(remove_k_duplicates("abcd", 2), "abcd")

    def test_example_2(self):
        self.assertEqual(remove_k_duplicates("deeedbbcccbdaa", 3), "aa")

    def test_entire_string_removed(self):
        self.assertEqual(remove_k_duplicates("aaabbbccc", 3), "")

    def test_cascading_removals(self):
        # "baaabbb" with k=3 -> "bbbb"? No: "b" + "aaa" + "bbb" -> remove "aaa" -> "bbbb" -> remove "bbb" -> "b"
        self.assertEqual(remove_k_duplicates("baaabbb", 3), "b")

    def test_no_removals_possible(self):
        self.assertEqual(remove_k_duplicates("aabbcc", 3), "aabbcc")

    def test_k_larger_than_string(self):
        self.assertEqual(remove_k_duplicates("abc", 5), "abc")

    def test_single_character_repeated(self):
        self.assertEqual(remove_k_duplicates("aaaaa", 2), "a")

    def test_large_input_performance(self):
        # Construct a large string with nested duplicates
        # Pattern: 'a' * 9999 + 'b' * 10000 + 'a' * 1 with k=10000
        # 'b'*10000 should vanish, leaving 'a'*10000 which also vanishes
        s = "a" * 9999 + "b" * 10000 + "a" * 1
        self.assertEqual(remove_k_duplicates(s, 10000), "")
