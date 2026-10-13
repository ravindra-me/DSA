# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_01 import recursive_sum  # noqa: E402
# ---- End of generated header ----

class TestRecursiveSum(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(recursive_sum([1, 2, 3, 4]), 10)

    def test_example_2(self):
        self.assertEqual(recursive_sum([]), 0)

    def test_single_element(self):
        self.assertEqual(recursive_sum([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(recursive_sum([-1, -2, -3]), -6)
        self.assertEqual(recursive_sum([-1, 1, -1]), -1)

    def test_duplicates(self):
        self.assertEqual(recursive_sum([2, 2, 2, 2]), 8)

    def test_large_input(self):
        # 1000 elements is exactly the upper bound constraint.
        arr = list(range(1000))
        expected = sum(range(1000))
        self.assertEqual(recursive_sum(arr), expected)
