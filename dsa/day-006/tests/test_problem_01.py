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
from problem_01 import analyze_bits  # noqa: E402
# ---- End of generated header ----

class TestAnalyzeBits(TestCase):
    def test_examples(self):
        self.assertEqual(analyze_bits(16), (True, 1))
        self.assertEqual(analyze_bits(0), (False, 0))
        self.assertEqual(analyze_bits(11), (False, 3))

    def test_edge_zero(self):
        self.assertEqual(analyze_bits(0), (False, 0))

    def test_edge_one(self):
        # 2^0 = 1
        self.assertEqual(analyze_bits(1), (True, 1))

    def test_all_powers_of_two_up_to_30(self):
        for exp in range(31):
            val = 1 << exp
            is_pow2, bits = analyze_bits(val)
            self.assertTrue(is_pow2, f"{val} should be a power of two")
            self.assertEqual(bits, 1, f"{val} should have exactly 1 set bit")

    def test_non_powers_of_two(self):
        test_values = [3, 5, 6, 7, 9, 10, 12, 15, 100, 1023]
        for val in test_values:
            is_pow2, bits = analyze_bits(val)
            self.assertFalse(is_pow2, f"{val} is not a power of two")
            # Mathematical check for bit count
            expected_bits = sum((val >> i) & 1 for i in range(32))
            self.assertEqual(bits, expected_bits)

    def test_upper_boundary(self):
        # 2^31 - 1: all 31 lower bits set
        val = (1 << 31) - 1
        self.assertEqual(analyze_bits(val), (False, 31))

    def test_large_deterministic_batch(self):
        import random
        rng = random.Random(42)
        for _ in range(500):
            val = rng.randint(0, (1 << 31) - 1)
            expected_pow2 = (val > 0) and ((val & (val - 1)) == 0)
            expected_bits = sum((val >> i) & 1 for i in range(32))
            self.assertEqual(analyze_bits(val), (expected_pow2, expected_bits))
