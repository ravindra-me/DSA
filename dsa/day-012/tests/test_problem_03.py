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
from problem_03 import next_greater_elements  # noqa: E402
# ---- End of generated header ----

import random


class TestNextGreaterElements(TestCase):
    def test_example_1(self) -> None:
        nums = [1, 2, 1]
        expected = [2, -1, 2]
        self.assertEqual(next_greater_elements(nums), expected)

    def test_example_2(self) -> None:
        nums = [5, 4, 3, 2, 1]
        expected = [-1, 5, 5, 5, 5]
        self.assertEqual(next_greater_elements(nums), expected)

    def test_single_element(self) -> None:
        self.assertEqual(next_greater_elements([42]), [-1])
        self.assertEqual(next_greater_elements([-10]), [-1])

    def test_all_identical_elements(self) -> None:
        nums = [7, 7, 7, 7]
        expected = [-1, -1, -1, -1]
        self.assertEqual(next_greater_elements(nums), expected)

    def test_strictly_increasing(self) -> None:
        nums = [1, 2, 3, 4]
        expected = [2, 3, 4, -1]
        self.assertEqual(next_greater_elements(nums), expected)

    def test_negative_numbers_and_zeros(self) -> None:
        nums = [-2, 0, -1, -3]
        expected = [0, -1, 0, -2]
        self.assertEqual(next_greater_elements(nums), expected)

    def test_large_descending_input(self) -> None:
        n = 100000
        nums = list(range(n, 0, -1))
        expected = [-1] + [n] * (n - 1)
        self.assertEqual(next_greater_elements(nums), expected)

    def test_randomized_against_naive_reference(self) -> None:
        rng = random.Random(1337)
        nums = [rng.randint(-50, 50) for _ in range(200)]
        n = len(nums)
        expected = []
        for i in range(n):
            found = -1
            for step in range(1, n):
                nxt = nums[(i + step) % n]
                if nxt > nums[i]:
                    found = nxt
                    break
            expected.append(found)
        self.assertEqual(next_greater_elements(nums), expected)
