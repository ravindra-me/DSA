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
from problem_03 import sort_k_sorted  # noqa: E402
# ---- End of generated header ----

import random


class TestSortKSorted(TestCase):
    def test_example_1(self):
        arr = [3, 2, 1, 5, 4, 7, 6]
        k = 2
        expected = [1, 2, 3, 4, 5, 6, 7]
        result = sort_k_sorted(arr, k)
        self.assertEqual(result, expected)
        self.assertIs(result, arr)

    def test_example_2_single_element(self):
        arr = [10]
        k = 0
        expected = [10]
        self.assertEqual(sort_k_sorted(arr, k), expected)

    def test_empty_list(self):
        arr = []
        k = 0
        self.assertEqual(sort_k_sorted(arr, k), [])

    def test_already_sorted_k_zero(self):
        arr = [1, 2, 3, 4, 5]
        k = 0
        self.assertEqual(sort_k_sorted(arr, k), [1, 2, 3, 4, 5])

    def test_with_duplicates_and_negatives(self):
        arr = [-3, -5, -1, 0, -1, 4, 2]
        k = 2
        expected = sorted(arr)
        self.assertEqual(sort_k_sorted(arr, k), expected)

    def test_k_equals_one_adjacent_swaps(self):
        # Elements are at most 1 swap away from sorted position
        arr = [2, 1, 4, 3, 6, 5, 8, 7]
        k = 1
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(sort_k_sorted(arr, k), expected)

    def test_large_input_efficiency(self):
        # Generate a large k-sorted array (n = 20,000, k = 5)
        # A full O(n^2) sort would take ~4 * 10^8 ops, but O(n*k) takes ~10^5 ops.
        rng = random.Random(42)
        n = 20000
        k = 5
        sorted_arr = list(range(n))
        arr = list(sorted_arr)

        # Permute each element within distance k
        for i in range(0, n - k, k):
            window = arr[i : i + k]
            rng.shuffle(window)
            arr[i : i + k] = window

        # Verify that arr is indeed k-sorted relative to sorted_arr
        result = sort_k_sorted(arr, k)
        self.assertEqual(result, sorted_arr)
