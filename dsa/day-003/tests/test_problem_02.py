# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_02.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_02 import group_anagrams  # noqa: E402
# ---- End of generated header ----

import random
from collections import defaultdict


class TestGroupAnagrams(TestCase):
    def _normalize(self, groups: list[list[str]]) -> list[list[str]]:
        """Helper to sort groups and items within groups for order-independent equality."""
        return sorted([sorted(g) for g in groups])

    def test_example_1_standard_words(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        result = group_anagrams(words)
        self.assertEqual(self._normalize(result), self._normalize(expected))

    def test_example_2_single_empty_string(self):
        words = [""]
        expected = [[""]]
        result = group_anagrams(words)
        self.assertEqual(self._normalize(result), self._normalize(expected))

    def test_example_3_single_character(self):
        words = ["a"]
        expected = [["a"]]
        result = group_anagrams(words)
        self.assertEqual(self._normalize(result), self._normalize(expected))

    def test_multiple_empty_strings(self):
        words = ["", "", ""]
        expected = [["", "", ""]]
        result = group_anagrams(words)
        self.assertEqual(self._normalize(result), self._normalize(expected))

    def test_duplicate_words(self):
        words = ["abc", "abc", "bca", "cab"]
        expected = [["abc", "abc", "bca", "cab"]]
        result = group_anagrams(words)
        self.assertEqual(self._normalize(result), self._normalize(expected))

    def test_all_distinct_no_anagrams(self):
        words = ["cat", "dog", "bird", "fish"]
        expected = [["cat"], ["dog"], ["bird"], ["fish"]]
        result = group_anagrams(words)
        self.assertEqual(self._normalize(result), self._normalize(expected))

    def test_large_input_performance_and_correctness(self):
        rng = random.Random(42)
        base_words = ["listen", "silent", "enlist", "apple", "banana", "rat", "tar", "art"]
        words = [rng.choice(base_words) for _ in range(5000)]

        # Independently verify using sorted string as reference key
        expected_map = defaultdict(list)
        for w in words:
            expected_map["".join(sorted(w))].append(w)
        expected = list(expected_map.values())

        result = group_anagrams(words)
        self.assertEqual(self._normalize(result), self._normalize(expected))
