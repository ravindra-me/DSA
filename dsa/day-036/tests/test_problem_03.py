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
from problem_03 import heap_sort  # noqa: E402
# ---- End of generated header ----

import random

class TestHeapSort(TestCase):
    def test_example_cases(self) -> None:
        nums1 = [12, 11, 13, 5, 6, 7]
        heap_sort(nums1)
        self.assertEqual(nums1, [5, 6, 7, 11, 12, 13])

        nums2 = [1]
        heap_sort(nums2)
        self.assertEqual(nums2, [1])

        nums3: list[int] = []
        heap_sort(nums3)
        self.assertEqual(nums3, [])

    def test_two_elements(self) -> None:
        pair_ordered = [1, 2]
        heap_sort(pair_ordered)
        self.assertEqual(pair_ordered, [1, 2])

        pair_reversed = [2, 1]
        heap_sort(pair_reversed)
        self.assertEqual(pair_reversed, [1, 2])

    def test_already_sorted_and_reversed(self) -> None:
        sorted_nums = [-10, -5, 0, 3, 9, 21]
        heap_sort(sorted_nums)
        self.assertEqual(sorted_nums, [-10, -5, 0, 3, 9, 21])

        reversed_nums = [21, 9, 3, 0, -5, -10]
        heap_sort(reversed_nums)
        self.assertEqual(reversed_nums, [-10, -5, 0, 3, 9, 21])

    def test_duplicates_and_identical_elements(self) -> None:
        all_identical = [42] * 8
        heap_sort(all_identical)
        self.assertEqual(all_identical, [42] * 8)

        duplicates = [5, 1, 5, 2, 1, 5, 3]
        heap_sort(duplicates)
        self.assertEqual(duplicates, [1, 1, 2, 3, 5, 5, 5])

    def test_negative_and_boundary_values(self) -> None:
        nums = [10**9, -10**9, 0, -(10**9) + 1, 10**9 - 1]
        expected = sorted(nums)
        heap_sort(nums)
        self.assertEqual(nums, expected)

    def test_large_random_input(self) -> None:
        rng = random.Random(1337)
        nums = [rng.randint(-1_000_000, 1_000_000) for _ in range(10_000)]
        expected = sorted(nums)
        heap_sort(nums)
        self.assertEqual(nums, expected)
