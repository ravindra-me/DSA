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
    def test_example_one(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
        self.assertEqual(group_anagrams(words), expected)

    def test_empty_input(self):
        self.assertEqual(group_anagrams([]), [])

    def test_single_element(self):
        self.assertEqual(group_anagrams(["hello"]), [["hello"]])
        self.assertEqual(group_anagrams([""]), [[""]])

    def test_all_same_anagram_with_duplicates(self):
        words = ["a", "a", "a"]
        self.assertEqual(group_anagrams(words), [["a", "a", "a"]])

    def test_no_anagrams(self):
        words = ["cat", "dog", "bird"]
        # Each group has size 1; tie-broken by first element
        expected = [["bird"], ["cat"], ["dog"]]
        self.assertEqual(group_anagrams(words), expected)

    def test_tie_breaking_equal_sizes(self):
        # Sizes: ["xyz"], ["abc"], ["mno"] all size 1
        # ["ab", "ba"], ["cd", "dc"] both size 2
        words = ["ba", "dc", "ab", "cd", "xyz", "abc", "mno"]
        expected = [
            ["ab", "ba"],
            ["cd", "dc"],
            ["abc"],
            ["mno"],
            ["xyz"],
        ]
        self.assertEqual(group_anagrams(words), expected)

    def test_large_input(self):
        # 10,000 words generated deterministically
        rng = random.Random(1337)
        base_words = ["".join(rng.choices("abcdefghij", k=8)) for _ in range(200)]
        words = []
        for _ in range(10000):
            base = rng.choice(base_words)
            chars = list(base)
            rng.shuffle(chars)
            words.append("".join(chars))

        # Reference calculation using canonical signatures
        ref_groups = defaultdict(list)
        for w in words:
            ref_groups["".join(sorted(w))].append(w)
        expected = []
        for g in ref_groups.values():
            g.sort()
            expected.append(g)
        expected.sort(key=lambda g: (-len(g), g[0]))

        self.assertEqual(group_anagrams(words), expected)
