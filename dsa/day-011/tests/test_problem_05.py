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
from problem_05 import largest_rectangle_area  # noqa: E402
# ---- End of generated header ----

class TestLargestRectangleArea(TestCase):
    def test_examples(self) -> None:
        self.assertEqual(largest_rectangle_area([2, 1, 5, 6, 2, 3]), 10)
        self.assertEqual(largest_rectangle_area([2, 4]), 4)

    def test_single_element(self) -> None:
        self.assertEqual(largest_rectangle_area([7]), 7)
        self.assertEqual(largest_rectangle_area([0]), 0)

    def test_all_zeros(self) -> None:
        self.assertEqual(largest_rectangle_area([0, 0, 0, 0]), 0)

    def test_all_equal_heights(self) -> None:
        self.assertEqual(largest_rectangle_area([3, 3, 3, 3, 3]), 15)

    def test_strictly_increasing(self) -> None:
        self.assertEqual(largest_rectangle_area([1, 2, 3, 4, 5]), 9)

    def test_strictly_decreasing(self) -> None:
        self.assertEqual(largest_rectangle_area([5, 4, 3, 2, 1]), 9)

    def test_valley_and_mountain(self) -> None:
        # Mountain shape: [1, 3, 5, 3, 1]
        self.assertEqual(largest_rectangle_area([1, 3, 5, 3, 1]), 9)
        # Valley shape: [5, 2, 1, 2, 5]
        self.assertEqual(largest_rectangle_area([5, 2, 1, 2, 5]), 5)

    def test_large_input_performance(self) -> None:
        # 100,000 elements forming a repeated staircase
        # Repeating [1, 2, 3, 4, 5] 20,000 times
        # The max area across the whole array is height 1 across all 100,000 bars = 100,000
        # or within any block height 3 * 3 = 9, etc.
        heights = [1, 2, 3, 4, 5] * 20_000
        expected = 100_000
        self.assertEqual(largest_rectangle_area(heights), expected)
