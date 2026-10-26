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
from problem_03 import decode_string  # noqa: E402
# ---- End of generated header ----

class DecodeStringTests(TestCase):
    def test_example_1(self):
        self.assertEqual(decode_string("3[a]2[bc]"), "aaabcbc")

    def test_example_2(self):
        self.assertEqual(decode_string("3[a2[c]]"), "accaccacc")

    def test_example_3(self):
        self.assertEqual(decode_string("2[abc]3[cd]ef"), "abcabccdcdcdef")

    def test_no_encoding(self):
        self.assertEqual(decode_string("abcdef"), "abcdef")

    def test_single_character(self):
        self.assertEqual(decode_string("z"), "z")

    def test_multi_digit_multiplier(self):
        self.assertEqual(decode_string("10[a]"), "a" * 10)
        self.assertEqual(decode_string("12[ab]"), "ab" * 12)

    def test_deep_nesting(self):
        # 2[a2[b2[c]]] -> 2[a2[bcccc]] -> 2[abccccbcccc] -> abccccbccccabccccbcccc
        # c: repeated 2 times inside b, so bcc
        # Wait: 2[c] = cc -> b2[c] = bcc -> 2[bcc] = bccbcc -> a2[bcc] = abccbcc
        # 2[abccbcc] = abccbccabccbcc
        self.assertEqual(decode_string("2[a2[b2[c]]]"), "abccbccabccbcc")

    def test_large_output_within_constraints(self):
        # k = 300, input len <= 60
        pattern = "300[abc]"
        expected = "abc" * 300
        self.assertEqual(decode_string(pattern), expected)
