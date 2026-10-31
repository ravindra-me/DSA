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
from problem_03 import two_sum_sorted  # noqa: E402
# ---- End of generated header ----

class TestTwoSumSorted(TestCase):
    def test_example_one(self) -> None:
        self.assertEqual(two_sum_sorted([2, 7, 11, 15], 9), [1, 2])

    def test_example_two(self) -> None:
        self.assertEqual(two_sum_sorted([2, 3, 4], 6), [1, 3])

    def test_example_three(self) -> None:
        self.assertEqual(two_sum_sorted([-1, 0], -1), [1, 2])

    def test_minimum_length_two_elements(self) -> None:
        self.assertEqual(two_sum_sorted([5, 10], 15), [1, 2])

    def test_duplicate_values(self) -> None:
        self.assertEqual(two_sum_sorted([1, 2, 2, 4], 4), [2, 3])

    def test_all_negatives(self) -> None:
        self.assertEqual(two_sum_sorted([-10, -8, -5, -2], -13), [2, 3])

    def test_target_at_extremes(self) -> None:
        numbers = [-500, -100, 0, 100, 500]
        self.assertEqual(two_sum_sorted(numbers, 0), [1, 5])

    def test_large_input_performance(self) -> None:
        # Construct an array of 30,000 numbers with guaranteed unique target pair
        # Flat prefix of -1000s, specific values at known positions, flat suffix of 1000s
        numbers = [-1000] * 10000 + [-500] + [0] * 9998 + [300] + [1000] * 10000
        # Target is (-500) + 300 = -200
        # Check that -1000 + 1000 = 0 != -200, -1000 + 300 = -700, -500 + 1000 = 500, etc.
        # Pair (-500, 300) is at 1-based indices 10001 and 20000
        self.assertEqual(two_sum_sorted(numbers, -200), [10001, 20000])
