# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_05.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_05 import find_maximum_xor  # noqa: E402
# ---- End of generated header ----

import random


class TestMaximumXor(TestCase):
    def test_example_1(self):
        nums = [3, 10, 5, 25, 2, 8]
        self.assertEqual(find_maximum_xor(nums), 28)

    def test_example_2(self):
        nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
        self.assertEqual(find_maximum_xor(nums), 127)

    def test_example_3_single_element(self):
        self.assertEqual(find_maximum_xor([0]), 0)
        self.assertEqual(find_maximum_xor([42]), 0)

    def test_all_identical_elements(self):
        nums = [7] * 10
        self.assertEqual(find_maximum_xor(nums), 0)

    def test_two_complementary_elements(self):
        # 0b010101 and 0b101010 sum/xor to 0b111111 = 63
        a = 0b010101
        b = 0b101010
        self.assertEqual(find_maximum_xor([a, b]), 63)

    def test_boundary_max_31_bit_integers(self):
        max_val = (1 << 31) - 1
        nums = [0, max_val]
        self.assertEqual(find_maximum_xor(nums), max_val)

    def test_correctness_against_small_brute_force(self):
        rng = random.Random(1337)
        nums = [rng.randint(0, 10000) for _ in range(100)]
        expected = max(x ^ y for x in nums for y in nums)
        self.assertEqual(find_maximum_xor(nums), expected)

    def test_large_input_performance(self):
        # Large input of 20,000 numbers that would be slow for O(n^2)
        # Include two specifically chosen numbers that guarantee a known upper bound
        rng = random.Random(42)
        nums = [rng.randint(0, 10**7) for _ in range(20000)]
        nums.append(0)
        nums.append((1 << 24) - 1)
        result = find_maximum_xor(nums)
        self.assertGreaterEqual(result, (1 << 24) - 1)
