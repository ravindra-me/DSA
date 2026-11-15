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
from problem_03 import radix_sort  # noqa: E402
# ---- End of generated header ----

import random


class TestRadixSort(TestCase):
    def test_example_1(self):
        nums = [170, 45, 75, 90, 802, 24, 2, 66]
        expected = [2, 24, 45, 66, 75, 90, 170, 802]
        self.assertEqual(radix_sort(nums), expected)

    def test_example_2_all_zeros(self):
        nums = [0, 0, 0]
        self.assertEqual(radix_sort(nums), [0, 0, 0])

    def test_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_single_element(self):
        self.assertEqual(radix_sort([42]), [42])

    def test_already_sorted_and_reversed(self):
        sorted_nums = [1, 5, 10, 50, 100, 500, 1000]
        reversed_nums = [1000, 500, 100, 50, 10, 5, 1]
        self.assertEqual(radix_sort(sorted_nums), sorted_nums)
        self.assertEqual(radix_sort(reversed_nums), sorted_nums)

    def test_duplicate_values(self):
        nums = [5, 2, 8, 2, 5, 9, 1, 8, 2]
        expected = sorted(nums)
        self.assertEqual(radix_sort(nums), expected)

    def test_large_32_bit_values(self):
        nums = [(1 << 31) - 1, 0, (1 << 30), (1 << 16), (1 << 8), 255, 65535]
        expected = sorted(nums)
        self.assertEqual(radix_sort(nums), expected)

    def test_large_random_dataset(self):
        rng = random.Random(42)
        n = 50_000
        nums = [rng.randint(0, (1 << 31) - 1) for _ in range(n)]
        expected = sorted(nums)
        self.assertEqual(radix_sort(nums), expected)
