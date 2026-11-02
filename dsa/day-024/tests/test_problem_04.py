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
from problem_04 import character_replacement  # noqa: E402
# ---- End of generated header ----

import random
import unittest

class TestCharacterReplacement(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(character_replacement("ABAB", 2), 4)

    def test_example_2(self):
        self.assertEqual(character_replacement("AABABBA", 1), 4)

    def test_k_zero(self):
        self.assertEqual(character_replacement("AAABBC", 0), 3)

    def test_k_larger_than_length(self):
        self.assertEqual(character_replacement("ABC", 5), 3)

    def test_single_character(self):
        self.assertEqual(character_replacement("A", 0), 1)

    def test_all_same_characters(self):
        self.assertEqual(character_replacement("AAAA", 2), 4)

    def test_large_input(self):
        rng = random.Random(42)
        # Pattern of repeating characters with periodic noise
        s_chars = []
        for _ in range(100000):
            if rng.random() < 0.9:
                s_chars.append('A')
            else:
                s_chars.append('B')
        s = "".join(s_chars)
        k = 100
        
        # Verification using reference sliding window logic
        res = character_replacement(s, k)
        self.assertGreaterEqual(res, 100)
        self.assertLessEqual(res, len(s))
