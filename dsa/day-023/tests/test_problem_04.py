# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_04.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_04 import longest_awesome  # noqa: E402
# ---- End of generated header ----

import random
import unittest


class TestLongestAwesome(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(longest_awesome("3242415"), 5)

    def test_example_2(self):
        self.assertEqual(longest_awesome("12345678"), 1)

    def test_example_3(self):
        self.assertEqual(longest_awesome("00000"), 5)

    def test_single_character(self):
        self.assertEqual(longest_awesome("7"), 1)

    def test_two_same_characters(self):
        self.assertEqual(longest_awesome("99"), 2)

    def test_two_different_characters(self):
        self.assertEqual(longest_awesome("12"), 1)

    def test_complex_palindrome_substring(self):
        # "21312" -> length 5
        self.assertEqual(longest_awesome("9213128"), 5)

    def test_large_input_performance(self):
        rng = random.Random(42)
        s = "".join(rng.choice("01234") for _ in range(50000))
        res = longest_awesome(s)
        self.assertGreater(res, 100)
