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
from problem_03 import total_hamming_distance  # noqa: E402
# ---- End of generated header ----

import random

class TestTotalHammingDistance(TestCase):
    def test_example_1(self) -> None:
        self.assertEqual(total_hamming_distance([4, 14, 2]), 6)

    def test_example_2(self) -> None:
        self.assertEqual(total_hamming_distance([4, 14, 4]), 4)

    def test_single_element(self) -> None:
        self.assertEqual(total_hamming_distance([7]), 0)

    def test_all_zeros(self) -> None:
        self.assertEqual(total_hamming_distance([0, 0, 0, 0]), 0)

    def test_all_identical_large_values(self) -> None:
        self.assertEqual(total_hamming_distance([10**9, 10**9, 10**9]), 0)

    def test_all_pairs_different_bits(self) -> None:
        # Powers of two have non-overlapping bits
        # nums = [1, 2, 4]: pairs are (1, 2), (1, 4), (2, 4), each has distance 2 -> total 6
        self.assertEqual(total_hamming_distance([1, 2, 4]), 6)

    def test_alternating_bits_boundary(self) -> None:
        # 0 and 2^30 - 1 (1073741823) have 30 differing bits
        max_val = (1 << 30) - 1
        self.assertEqual(total_hamming_distance([0, max_val]), 30)

    def test_large_input_matches_reference(self) -> None:
        rng = random.Random(42)
        nums = [rng.randint(0, 10**9) for _ in range(5000)]
        
        # Reference calculation for the first 50 elements via brute force
        sub = nums[:50]
        ref_sum = sum(
            (sub[i] ^ sub[j]).bit_count()
            for i in range(len(sub))
            for j in range(i + 1, len(sub))
        )
        self.assertEqual(total_hamming_distance(sub), ref_sum)
        
        # Full 5000-element list completes quickly without error
        result = total_hamming_distance(nums)
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)
