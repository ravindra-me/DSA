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
from problem_05 import decode_string  # noqa: E402
# ---- End of generated header ----

class TestDecodeString(TestCase):
    def test_example_one(self) -> None:
        s = "3[a]2[bc]"
        self.assertEqual(decode_string(s), "aaabcbc")

    def test_example_two(self) -> None:
        s = "3[a2[c]]"
        self.assertEqual(decode_string(s), "accaccacc")

    def test_example_three(self) -> None:
        s = "2[abc]3[cd]ef"
        self.assertEqual(decode_string(s), "abcabccdcdcdef")

    def test_no_brackets(self) -> None:
        s = "abcdef"
        self.assertEqual(decode_string(s), "abcdef")

    def test_multi_digit_multiplier(self) -> None:
        s = "12[ab]"
        self.assertEqual(decode_string(s), "ab" * 12)

    def test_deep_nesting(self) -> None:
        s = "2[a2[b2[c]]]"
        # 2[c] -> "cc"
        # 2[b + "cc"] -> "bccbcc"
        # 2[a + "bccbcc"] -> "abccbccabccbcc"
        self.assertEqual(decode_string(s), "abccbccabccbcc")

    def test_single_character_bracketed(self) -> None:
        s = "1[z]"
        self.assertEqual(decode_string(s), "z")

    def test_complex_mixed_structure(self) -> None:
        s = "prefix3[x2[y]]suffix"
        expected = "prefix" + ("x" + "y" * 2) * 3 + "suffix"
        self.assertEqual(decode_string(s), expected)
