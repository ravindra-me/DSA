# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_04.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_04 import sort_colors  # noqa: E402
# ---- End of generated header ----

import random


class TestSortColors(TestCase):
    def test_example_1(self) -> None:
        nums = [2, 0, 2, 1, 1, 0]
        sort_colors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_example_2(self) -> None:
        nums = [2, 0, 1]
        sort_colors(nums)
        self.assertEqual(nums, [0, 1, 2])

    def test_single_element(self) -> None:
        for val in [0, 1, 2]:
            nums = [val]
            sort_colors(nums)
            self.assertEqual(nums, [val])

    def test_all_same_elements(self) -> None:
        nums_zeros = [0, 0, 0, 0]
        sort_colors(nums_zeros)
        self.assertEqual(nums_zeros, [0, 0, 0, 0])

        nums_twos = [2, 2, 2]
        sort_colors(nums_twos)
        self.assertEqual(nums_twos, [2, 2, 2])

    def test_two_colors_only(self) -> None:
        nums = [2, 0, 2, 0, 0, 2]
        sort_colors(nums)
        self.assertEqual(nums, [0, 0, 0, 2, 2, 2])

    def test_already_sorted_and_reversed(self) -> None:
        already_sorted = [0, 0, 1, 1, 2, 2]
        sort_colors(already_sorted)
        self.assertEqual(already_sorted, [0, 0, 1, 1, 2, 2])

        reversed_nums = [2, 2, 1, 1, 0, 0]
        sort_colors(reversed_nums)
        self.assertEqual(reversed_nums, [0, 0, 1, 1, 2, 2])

    def test_large_random_input(self) -> None:
        rng = random.Random(1337)
        nums = [rng.choice([0, 1, 2]) for _ in range(300)]
        expected = sorted(nums)
        sort_colors(nums)
        self.assertEqual(nums, expected)
