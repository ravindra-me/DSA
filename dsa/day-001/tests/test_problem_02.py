# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_02.py
import os
import sys
import unittest

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_02 import two_sum_sorted  # noqa: E402
# ---- End of generated header ----

class TestTwoSumSorted(unittest.TestCase):
    def test_example_one(self) -> None:
        self.assertEqual(two_sum_sorted([2, 7, 11, 15], 9), (1, 2))

    def test_example_two(self) -> None:
        self.assertEqual(two_sum_sorted([2, 3, 4], 6), (1, 3))

    def test_example_three_no_pair(self) -> None:
        self.assertIsNone(two_sum_sorted([1, 2, 3], 10))

    def test_minimum_length_array_match(self) -> None:
        self.assertEqual(two_sum_sorted([5, 12], 17), (1, 2))

    def test_minimum_length_array_no_match(self) -> None:
        self.assertIsNone(two_sum_sorted([5, 12], 10))

    def test_duplicate_values(self) -> None:
        self.assertEqual(two_sum_sorted([1, 2, 2, 4], 4), (2, 3))

    def test_negative_numbers_and_zero(self) -> None:
        # Unique pair (-5, 2) at indices (2, 4) sums to -3
        self.assertEqual(two_sum_sorted([-10, -5, -1, 2, 8], -3), (2, 4))
        # Unique pair (-3, 4) at indices (2, 4) sums to 1
        self.assertEqual(two_sum_sorted([-7, -3, 0, 4, 9], 1), (2, 4))

    def test_extreme_values(self) -> None:
        numbers = [-1_000_000_000, 0, 1_000_000_000]
        self.assertEqual(two_sum_sorted(numbers, 0), (1, 3))
        self.assertEqual(two_sum_sorted(numbers, -1_000_000_000), (1, 2))

    def test_large_input_linear_time(self) -> None:
        # Construct an array where only (3, 7) can sum to 10,
        # forcing pointers to move across thousands of elements before meeting.
        numbers = [1] * 50_000 + [3, 7] + [10] * 49_998
        self.assertEqual(two_sum_sorted(numbers, 10), (50_001, 50_002))

    def test_large_input_no_pair(self) -> None:
        size = 50_000
        numbers = [2 * i for i in range(size)]
        # Sum of any two even numbers is even; an odd target cannot exist.
        self.assertIsNone(two_sum_sorted(numbers, 99_999))
