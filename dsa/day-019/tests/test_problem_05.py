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
from problem_05 import find_anagrams  # noqa: E402
# ---- End of generated header ----

import random
from collections import Counter


class TestFindAnagrams(TestCase):
    def test_example_one(self) -> None:
        s = "cbaebabacd"
        p = "abc"
        self.assertEqual(find_anagrams(s, p), [0, 6])

    def test_example_two(self) -> None:
        s = "abab"
        p = "ab"
        self.assertEqual(find_anagrams(s, p), [0, 1, 2])

    def test_p_longer_than_s(self) -> None:
        s = "a"
        p = "aa"
        self.assertEqual(find_anagrams(s, p), [])

    def test_single_characters(self) -> None:
        self.assertEqual(find_anagrams("a", "a"), [0])
        self.assertEqual(find_anagrams("a", "b"), [])

    def test_identical_repeated_characters(self) -> None:
        s = "aaaaa"
        p = "aaa"
        self.assertEqual(find_anagrams(s, p), [0, 1, 2])

    def test_no_matches(self) -> None:
        s = "abcdef"
        p = "gh"
        self.assertEqual(find_anagrams(s, p), [])

    def test_exact_full_string_match(self) -> None:
        s = "anagram"
        p = "nagaram"
        self.assertEqual(find_anagrams(s, p), [0])

    def test_large_input_performance(self) -> None:
        rng = random.Random(42)
        # s of length 30,000 using only 'a' and 'b'
        chars = [rng.choice("ab") for _ in range(30000)]
        s = "".join(chars)
        p = "ab"

        # Exact reference computation for p = 'ab': indices where window of size 2 is "ab" or "ba"
        expected = [i for i in range(len(s) - 1) if s[i : i + 2] in ("ab", "ba")]
        self.assertEqual(find_anagrams(s, p), expected)
