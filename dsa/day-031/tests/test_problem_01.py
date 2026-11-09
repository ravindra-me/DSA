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
from problem_01 import bubble_sort_analysis  # noqa: E402
# ---- End of generated header ----

import random


class TestBubbleSortAnalysis(TestCase):
    def test_example_1_reverse_order(self):
        arr = [3, 2, 1]
        sorted_arr, swaps, passes = bubble_sort_analysis(arr)
        self.assertEqual(sorted_arr, [1, 2, 3])
        self.assertEqual(swaps, 3)
        self.assertEqual(passes, 2)
        self.assertEqual(arr, [3, 2, 1], "Input list must not be mutated")

    def test_example_2_already_sorted(self):
        arr = [1, 2, 3, 4]
        sorted_arr, swaps, passes = bubble_sort_analysis(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4])
        self.assertEqual(swaps, 0)
        self.assertEqual(passes, 1)

    def test_example_3_empty_list(self):
        arr: list[int] = []
        sorted_arr, swaps, passes = bubble_sort_analysis(arr)
        self.assertEqual(sorted_arr, [])
        self.assertEqual(swaps, 0)
        self.assertEqual(passes, 0)

    def test_single_element(self):
        arr = [42]
        sorted_arr, swaps, passes = bubble_sort_analysis(arr)
        self.assertEqual(sorted_arr, [42])
        self.assertEqual(swaps, 0)
        self.assertEqual(passes, 0)

    def test_duplicates_and_negatives(self):
        arr = [0, -5, 2, -5, 0, 1]
        sorted_arr, swaps, passes = bubble_sort_analysis(arr)
        self.assertEqual(sorted_arr, [-5, -5, 0, 0, 1, 2])
        # Inversion count for [0, -5, 2, -5, 0, 1]:
        # Pairs (i, j) with i < j and arr[i] > arr[j]:
        # (0, -5), (0, -5), (2, -5), (2, 0), (2, 1) -> 5 inversions = 5 swaps
        self.assertEqual(swaps, 5)
        self.assertTrue(1 <= passes <= 5)

    def test_all_identical_elements(self):
        arr = [7, 7, 7, 7, 7]
        sorted_arr, swaps, passes = bubble_sort_analysis(arr)
        self.assertEqual(sorted_arr, [7, 7, 7, 7, 7])
        self.assertEqual(swaps, 0)
        self.assertEqual(passes, 1)

    def test_large_already_sorted_early_exit(self):
        arr = list(range(1000))
        sorted_arr, swaps, passes = bubble_sort_analysis(arr)
        self.assertEqual(sorted_arr, arr)
        self.assertEqual(swaps, 0)
        self.assertEqual(passes, 1)

    def test_large_random_matches_inversion_count(self):
        rng = random.Random(42)
        arr = [rng.randint(-1000, 1000) for _ in range(150)]
        
        # Count inversions directly as independent reference
        expected_swaps = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    expected_swaps += 1

        sorted_arr, swaps, passes = bubble_sort_analysis(arr)
        self.assertEqual(sorted_arr, sorted(arr))
        self.assertEqual(swaps, expected_swaps)
        self.assertTrue(1 <= passes <= len(arr) - 1)
