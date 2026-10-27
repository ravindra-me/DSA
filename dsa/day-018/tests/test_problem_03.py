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
from problem_03 import is_happy  # noqa: E402
# ---- End of generated header ----

class TestHappyNumber(TestCase):
    def test_example_1(self):
        self.assertTrue(is_happy(19))

    def test_example_2(self):
        self.assertFalse(is_happy(2))

    def test_example_3_one(self):
        self.assertTrue(is_happy(1))

    def test_small_happy_numbers(self):
        # Known happy numbers: 7, 10, 13, 23, 28
        happy_list = [7, 10, 13, 23, 28]
        for num in happy_list:
            self.assertTrue(is_happy(num), f"Expected {num} to be happy")

    def test_small_unhappy_numbers(self):
        # Known unhappy numbers: 3, 4, 5, 6, 8, 9
        unhappy_list = [3, 4, 5, 6, 8, 9]
        for num in unhappy_list:
            self.assertFalse(is_happy(num), f"Expected {num} to be unhappy")

    def test_max_constraint(self):
        # 2^31 - 1 = 2147483647
        # 2^2 + 1^2 + 4^2 + 7^2 + 4^2 + 8^2 + 3^2 + 6^2 + 4^2 + 7^2
        # = 4 + 1 + 16 + 49 + 16 + 64 + 9 + 36 + 16 + 49 = 260
        # 260 is not happy
        self.assertFalse(is_happy(2147483647))

    def test_large_happy_number(self):
        # 1000000000 (10^9) is happy -> 1^2 + 0^2... = 1
        self.assertTrue(is_happy(1000000000))
