# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py
import os
import sys
import unittest

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_01 import find_missing_number  # noqa: E402
# ---- End of generated header ----

import random


class TestFindMissingNumber(unittest.TestCase):
    def test_example_one(self) -> None:
        self.assertEqual(find_missing_number([3, 0, 1]), 2)

    def test_example_two(self) -> None:
        self.assertEqual(find_missing_number([0, 1]), 2)

    def test_example_three(self) -> None:
        self.assertEqual(find_missing_number([1]), 0)

    def test_single_element_missing_one(self) -> None:
        self.assertEqual(find_missing_number([0]), 1)

    def test_missing_zero(self) -> None:
        self.assertEqual(find_missing_number([1, 2, 3, 4, 5]), 0)

    def test_missing_last_element(self) -> None:
        self.assertEqual(find_missing_number([0, 1, 2, 3, 4]), 5)

    def test_unsorted_middle_missing(self) -> None:
        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        self.assertEqual(find_missing_number(nums), 8)

    def test_large_input(self) -> None:
        n = 100_000
        missing_target = 42_424
        rng = random.Random(1337)
        nums = [x for x in range(n + 1) if x != missing_target]
        rng.shuffle(nums)
        self.assertEqual(find_missing_number(nums), missing_target)
