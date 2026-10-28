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
from problem_01 import is_anagram  # noqa: E402
# ---- End of generated header ----

import random


class TestValidAnagram(TestCase):
    def test_example_1_anagram(self):
        self.assertTrue(is_anagram("anagram", "nagaram"))

    def test_example_2_different_counts(self):
        self.assertFalse(is_anagram("rat", "car"))

    def test_example_3_unequal_lengths(self):
        self.assertFalse(is_anagram("a", "ab"))

    def test_single_character_equal(self):
        self.assertTrue(is_anagram("z", "z"))

    def test_single_character_different(self):
        self.assertFalse(is_anagram("a", "b"))

    def test_same_letters_different_frequency(self):
        self.assertFalse(is_anagram("aabbcc", "abbccc"))

    def test_large_valid_anagram(self):
        rng = random.Random(42)
        chars = [chr(ord('a') + rng.randint(0, 25)) for _ in range(50000)]
        s = "".join(chars)
        shuffled_chars = list(chars)
        rng.shuffle(shuffled_chars)
        t = "".join(shuffled_chars)
        self.assertTrue(is_anagram(s, t))

    def test_large_invalid_anagram_single_difference(self):
        rng = random.Random(1337)
        chars = [chr(ord('a') + rng.randint(0, 24)) for _ in range(50000)]
        s = "".join(chars)
        shuffled_chars = list(chars)
        rng.shuffle(shuffled_chars)
        # Introduce a discrepancy with 'z' which was not in the original set
        shuffled_chars[0] = 'z'
        t = "".join(shuffled_chars)
        self.assertFalse(is_anagram(s, t))
