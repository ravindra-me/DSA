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
from problem_05 import minimum_xor_sum  # noqa: E402
# ---- End of generated header ----

import random
import itertools

class TestMinimumXORSum(TestCase):
    def test_example_1(self):
        self.assertEqual(minimum_xor_sum([1, 2], [2, 3]), 2)

    def test_example_2(self):
        self.assertEqual(minimum_xor_sum([1, 0, 3], [5, 3, 4]), 8)

    def test_example_3(self):
        self.assertEqual(minimum_xor_sum([7], [7]), 0)

    def test_single_element(self):
        self.assertEqual(minimum_xor_sum([10], [5]), 10 ^ 5)

    def test_zero_elements(self):
        self.assertEqual(minimum_xor_sum([0, 0, 0], [0, 0, 0]), 0)

    def test_duplicates(self):
        self.assertEqual(minimum_xor_sum([2, 2, 2], [2, 2, 2]), 0)

    def test_max_n_constraint(self):
        # N = 14 with deterministic random data
        rng = random.Random(42)
        n = 14
        nums1 = [rng.randint(0, 10**7) for _ in range(n)]
        nums2 = [rng.randint(0, 10**7) for _ in range(n)]
        
        res = minimum_xor_sum(nums1, nums2)
        self.assertIsInstance(res, int)
        self.assertGreaterEqual(res, 0)

    def test_small_brute_force_verification(self):
        # Verify against exact brute force permutations for N=5
        rng = random.Random(123)
        n = 5
        nums1 = [rng.randint(0, 1000) for _ in range(n)]
        nums2 = [rng.randint(0, 1000) for _ in range(n)]
        
        expected = min(
            sum(a ^ b for a, b in zip(nums1, p))
            for p in itertools.permutations(nums2)
        )
        self.assertEqual(minimum_xor_sum(nums1, nums2), expected)
