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
from problem_02 import decode_string  # noqa: E402
# ---- End of generated header ----

class TestDecodeString(TestCase):
    def test_example_1(self) -> None:
        self.assertEqual(decode_string("3[a]2[bc]"), "aaabcbc")

    def test_example_2(self) -> None:
        self.assertEqual(decode_string("3[a2[c]]"), "accaccacc")

    def test_example_3(self) -> None:
        self.assertEqual(decode_string("2[abc]3[cd]ef"), "abcabccdcdcdef")

    def test_no_brackets_plain_string(self) -> None:
        self.assertEqual(decode_string("xyz"), "xyz")

    def test_single_character(self) -> None:
        self.assertEqual(decode_string("a"), "a")
        self.assertEqual(decode_string("1[a]"), "a")

    def test_multi_digit_multiplier(self) -> None:
        self.assertEqual(decode_string("10[a]"), "aaaaaaaaaa")
        self.assertEqual(decode_string("12[ab]"), "ab" * 12)

    def test_deeply_nested_structures(self) -> None:
        # 2[a2[b2[c]]] -> 2[c] = cc -> 2[bcc] = bccbcc -> 2[abccbcc] = abccbccabccbcc
        self.assertEqual(decode_string("2[a2[b2[c]]]"), "abccbccabccbcc")

    def test_large_expansion_deterministic(self) -> None:
        # 300 multiplier with nested 10 repetitions
        # 300[2[ab]] -> 300 * "abab" = 1200 characters
        expected = ("ab" * 2) * 300
        self.assertEqual(decode_string("300[2[ab]]"), expected)
