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
from problem_01 import counting_sort  # noqa: E402
# ---- End of generated header ----

import random


class TestCountingSort(TestCase):
    def test_example_one(self) -> None:
        nums = [4, -1, 2, 0, -1, 3]
        expected = [-1, -1, 0, 2, 3, 4]
        self.assertEqual(counting_sort(nums), expected)

    def test_example_two_empty(self) -> None:
        self.assertEqual(counting_sort([]), [])

    def test_single_element(self) -> None:
        self.assertEqual(counting_sort([-5]), [-5])
        self.assertEqual(counting_sort([42]), [42])

    def test_all_identical_elements(self) -> None:
        self.assertEqual(counting_sort([-7, -7, -7, -7]), [-7, -7, -7, -7])
        self.assertEqual(counting_sort([0, 0, 0]), [0, 0, 0])

    def test_extremes_boundary_values(self) -> None:
        nums = [10000, -10000, 0, 10000, -10000]
        expected = [-10000, -10000, 0, 10000, 10000]
        self.assertEqual(counting_sort(nums), expected)

    def test_already_sorted_and_reverse_sorted(self) -> None:
        sorted_arr = [-10, -5, 0, 5, 10]
        self.assertEqual(counting_sort(sorted_arr), sorted_arr)
        self.assertEqual(counting_sort([10, 5, 0, -5, -10]), sorted_arr)

    def test_large_random_input(self) -> None:
        rng = random.Random(42)
        # 100,000 integers in the range [-10000, 10000]
        nums = [rng.randint(-10000, 10000) for _ in range(100_000)]
        expected = sorted(nums)
        self.assertEqual(counting_sort(nums), expected)
