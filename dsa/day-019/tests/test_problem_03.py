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
from problem_03 import group_anagrams  # noqa: E402
# ---- End of generated header ----

import random
from collections import Counter


class TestGroupAnagrams(TestCase):
    def test_example_1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(group_anagrams(strs), expected)

    def test_example_2_empty_string(self):
        strs = [""]
        expected = [[""]]
        self.assertEqual(group_anagrams(strs), expected)

    def test_example_3_single_char(self):
        strs = ["a"]
        expected = [["a"]]
        self.assertEqual(group_anagrams(strs), expected)

    def test_tie_breaking_order(self):
        # Both groups have length 2: ["cat", "tac"] and ["act", "cta"]
        # Group 1 starts with "act", Group 2 starts with "bat"
        # Lengths are equal (2), so "act" < "bat" decides the order.
        strs = ["bat", "act", "tab", "cat"]
        # Groups: {"bat": ["bat", "tab"], "act": ["act"], "cat": ["cat"]}
        # Let's create two equal sized groups:
        strs = ["bat", "tab", "act", "cat"]
        # Group 1: ["bat", "tab"], first is "bat"
        # Group 2: ["act", "cat"], first is "act"
        # Both size 2. "act" < "bat", so ["act", "cat"] must precede ["bat", "tab"].
        expected = [["act", "cat"], ["bat", "tab"]]
        self.assertEqual(group_anagrams(strs), expected)

    def test_duplicates_and_empty_strings(self):
        strs = ["", "b", "", "b", "b"]
        # Group 1: ["b", "b", "b"] (len 3)
        # Group 2: ["", ""] (len 2)
        expected = [["b", "b", "b"], ["", ""]]
        self.assertEqual(group_anagrams(strs), expected)

    def test_no_anagrams_all_distinct(self):
        strs = ["z", "y", "x", "w"]
        # All length 1, sorted lexicographically by first word
        expected = [["w"], ["x"], ["y"], ["z"]]
        self.assertEqual(group_anagrams(strs), expected)

    def test_large_input_performance(self):
        rng = random.Random(42)
        words = []
        base_words = ["abcdefghij", "jihgfedcba", "hello", "world", "python"]
        for _ in range(2000):
            w = rng.choice(base_words)
            shuffled = "".join(rng.sample(w, len(w)))
            words.append(shuffled)

        result = group_anagrams(words)
        # Check total count of strings preserved
        total_count = sum(len(group) for group in result)
        self.assertEqual(total_count, 2000)

        # Verify each group is sorted descending by length, then by group[0]
        for i in range(len(result) - 1):
            len_curr, len_next = len(result[i]), len(result[i + 1])
            self.assertTrue(
                len_curr > len_next or (len_curr == len_next and result[i][0] <= result[i + 1][0])
            )

        # Verify each group contains valid anagrams
        for group in result:
            first_counts = Counter(group[0])
            for word in group[1:]:
                self.assertEqual(first_counts, Counter(word))
