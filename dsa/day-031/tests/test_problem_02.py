# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_02.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_02 import selection_sort_tracked  # noqa: E402
# ---- End of generated header ----

import random


class TestSelectionSortTracked(TestCase):
    def test_example_1(self) -> None:
        arr = [4, 3, 2, 1]
        sorted_arr, swaps = selection_sort_tracked(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4])
        self.assertEqual(swaps, [(0, 3), (1, 2)])

    def test_example_2(self) -> None:
        arr = [1, 2, 3]
        sorted_arr, swaps = selection_sort_tracked(arr)
        self.assertEqual(sorted_arr, [1, 2, 3])
        self.assertEqual(swaps, [])

    def test_empty_and_single_element(self) -> None:
        self.assertEqual(selection_sort_tracked([]), ([], []))
        self.assertEqual(selection_sort_tracked([42]), ([42], []))

    def test_duplicates_leftmost_preference(self) -> None:
        # arr has duplicates: [3, 1, 2, 1]
        # i=0: min is 1 at index 1 -> swap (0, 1) -> [1, 3, 2, 1]
        # i=1: min is 1 at index 3 -> swap (1, 3) -> [1, 1, 2, 3]
        # i=2: min is 2 at index 2 -> min_idx == 2 -> no swap
        arr = [3, 1, 2, 1]
        sorted_arr, swaps = selection_sort_tracked(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3])
        self.assertEqual(swaps, [(0, 1), (1, 3)])

    def test_negative_and_zero(self) -> None:
        arr = [0, -5, 3, -5, 2]
        # i=0: min is -5 at index 1 -> swap (0, 1) -> [-5, 0, 3, -5, 2]
        # i=1: min is -5 at index 3 -> swap (1, 3) -> [-5, -5, 3, 0, 2]
        # i=2: min is 0 at index 3 -> swap (2, 3) -> [-5, -5, 0, 3, 2]
        # i=3: min is 2 at index 4 -> swap (3, 4) -> [-5, -5, 0, 2, 3]
        sorted_arr, swaps = selection_sort_tracked(arr)
        self.assertEqual(sorted_arr, [-5, -5, 0, 2, 3])
        self.assertEqual(swaps, [(0, 1), (1, 3), (2, 3), (3, 4)])

    def test_replay_swaps_matches_sorted_and_validates_large_input(self) -> None:
        rng = random.Random(1337)
        arr = [rng.randint(-10000, 10000) for _ in range(300)]
        sorted_arr, swaps = selection_sort_tracked(arr)

        # Check that result is sorted
        self.assertEqual(sorted_arr, sorted(arr))

        # Verify that swaps replayed on original produce the exact sorted array
        replayed = list(arr)
        for i, j in swaps:
            self.assertNotEqual(i, j, "Self-swaps should not be recorded")
            replayed[i], replayed[j] = replayed[j], replayed[i]
        self.assertEqual(replayed, sorted_arr)

        # Selection sort never performs more than n - 1 swaps
        self.assertLessEqual(len(swaps), len(arr) - 1)
