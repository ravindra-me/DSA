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
from problem_02 import single_number_ii  # noqa: E402
# ---- End of generated header ----

import random
from collections import Counter


class TestSingleNumberII(TestCase):
    def test_example_1(self) -> None:
        self.assertEqual(single_number_ii([2, 2, 3, 2]), 3)

    def test_example_2(self) -> None:
        self.assertEqual(single_number_ii([0, 1, 0, 1, 0, 1, 99]), 99)

    def test_single_element(self) -> None:
        self.assertEqual(single_number_ii([-4]), -4)
        self.assertEqual(single_number_ii([0]), 0)
        self.assertEqual(single_number_ii([42]), 42)

    def test_negative_numbers(self) -> None:
        nums = [-2, -2, 1, 1, 4, 1, -2]
        self.assertEqual(single_number_ii(nums), 4)

        nums_all_neg = [-5, -10, -5, -5, -7, -10, -10]
        self.assertEqual(single_number_ii(nums_all_neg), -7)

    def test_boundary_32bit_integers(self) -> None:
        min_int = -(2**31)
        max_int = 2**31 - 1
        nums = [min_int, max_int, min_int, min_int, max_int, max_int, 0]
        self.assertEqual(single_number_ii(nums), 0)

        nums_min_unique = [max_int, max_int, max_int, min_int]
        self.assertEqual(single_number_ii(nums_min_unique), min_int)

    def test_large_random_input(self) -> None:
        rng = random.Random(1337)
        triplets = [rng.randint(-100_000, 100_000) for _ in range(3000)]
        unique_val = 999_999

        nums = []
        for val in triplets:
            nums.extend([val, val, val])
        nums.append(unique_val)
        rng.shuffle(nums)

        # Reference verification using Counter
        counts = Counter(nums)
        expected = next(val for val, count in counts.items() if count == 1)
        self.assertEqual(expected, unique_val)

        self.assertEqual(single_number_ii(nums), unique_val)
