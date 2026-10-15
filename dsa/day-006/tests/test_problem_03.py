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
from problem_03 import reverse_bits  # noqa: E402
# ---- End of generated header ----

import random


class TestReverseBits(TestCase):
    def test_example_1(self):
        self.assertEqual(reverse_bits(43261596), 964176192)

    def test_example_2_zero(self):
        self.assertEqual(reverse_bits(0), 0)

    def test_example_3_one(self):
        self.assertEqual(reverse_bits(1), 2147483648)

    def test_all_ones_boundary(self):
        max_32bit = (1 << 32) - 1
        self.assertEqual(reverse_bits(max_32bit), max_32bit)

    def test_high_bit_only(self):
        high_bit = 1 << 31
        self.assertEqual(reverse_bits(high_bit), 1)

    def test_alternating_bits(self):
        # 0b1010...1010 (32 bits)
        n = 0xAAAAAAAA
        expected = 0x55555555
        self.assertEqual(reverse_bits(n), expected)
        self.assertEqual(reverse_bits(expected), n)

    def test_involution_property(self):
        # Reversing twice should yield the original 32-bit number
        rng = random.Random(1337)
        for _ in range(50):
            val = rng.randint(0, (1 << 32) - 1)
            self.assertEqual(reverse_bits(reverse_bits(val)), val)

    def test_against_string_reversal_reference(self):
        rng = random.Random(42)
        for _ in range(100):
            val = rng.randint(0, (1 << 32) - 1)
            binary_str = f"{val:032b}"
            expected = int(binary_str[::-1], 2)
            self.assertEqual(reverse_bits(val), expected)
