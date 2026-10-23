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
from problem_03 import find_all_anagrams  # noqa: E402
# ---- End of generated header ----

import random
from collections import Counter


class TestFindAllAnagrams(TestCase):
    def test_example_1(self):
        s = "cbaebabacd"
        p = "abc"
        self.assertEqual(find_all_anagrams(s, p), [0, 6])

    def test_example_2(self):
        s = "abab"
        p = "ab"
        self.assertEqual(find_all_anagrams(s, p), [0, 1, 2])

    def test_p_longer_than_s(self):
        s = "a"
        p = "aa"
        self.assertEqual(find_all_anagrams(s, p), [])

    def test_exact_match_single_char(self):
        s = "a"
        p = "a"
        self.assertEqual(find_all_anagrams(s, p), [0])

    def test_equal_length_no_match(self):
        s = "abc"
        p = "def"
        self.assertEqual(find_all_anagrams(s, p), [])

    def test_all_identical_characters(self):
        s = "aaaaa"
        p = "aa"
        self.assertEqual(find_all_anagrams(s, p), [0, 1, 2, 3])

    def test_no_matches_in_long_string(self):
        s = "abcdefghijklm"
        p = "xyz"
        self.assertEqual(find_all_anagrams(s, p), [])

    def test_large_input_efficiency(self):
        rng = random.Random(42)
        # Construct s of length 30000 with occasional exact anagrams inserted
        k = 10
        p = "abcdefghij"
        p_counter = Counter(p)

        # Create background noise with characters outside 'a'..'j'
        s_chars = [rng.choice("klmnopqrstuvwxyz") for _ in range(30000)]
        target_indices = [500, 2500, 10000, 25000]
        for idx in target_indices:
            shuffled_p = list(p)
            rng.shuffle(shuffled_p)
            s_chars[idx : idx + k] = shuffled_p

        s = "".join(s_chars)
        result = find_all_anagrams(s, p)

        # Verify every returned index by verifying Counter matches p
        for idx in result:
            self.assertEqual(Counter(s[idx : idx + k]), p_counter)

        # Verify expected target indices are among the results
        for idx in target_indices:
            self.assertIn(idx, result)
