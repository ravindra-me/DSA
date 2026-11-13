# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_02.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_02 import remove_duplicate_letters  # noqa: E402
# ---- End of generated header ----

import random
import string

class TestRemoveDuplicateLetters(TestCase):
    def test_example_1(self):
        self.assertEqual(remove_duplicate_letters("bcabc"), "abc")

    def test_example_2(self):
        self.assertEqual(remove_duplicate_letters("cbacdcbc"), "acdb")

    def test_single_character(self):
        self.assertEqual(remove_duplicate_letters("a"), "a")

    def test_all_identical(self):
        self.assertEqual(remove_duplicate_letters("aaaaaaa"), "a")

    def test_already_sorted(self):
        self.assertEqual(remove_duplicate_letters("abcde"), "abcde")

    def test_reverse_sorted(self):
        self.assertEqual(remove_duplicate_letters("edcba"), "edcba")

    def test_large_random_input(self):
        rng = random.Random(42)
        # Length 10,000 using full alphabet
        s = "".join(rng.choices(string.ascii_lowercase, k=10000))
        result = remove_duplicate_letters(s)
        self.assertEqual(len(result), 26)
        self.assertEqual(set(result), set(string.ascii_lowercase))
