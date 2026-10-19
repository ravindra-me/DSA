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
from problem_01 import is_valid_brackets  # noqa: E402
# ---- End of generated header ----

class TestValidBrackets(TestCase):
    def test_examples(self):
        self.assertTrue(is_valid_brackets("()[]{}"))
        self.assertFalse(is_valid_brackets("(]"))
        self.assertFalse(is_valid_brackets("([)]"))
        self.assertTrue(is_valid_brackets(""))

    def test_single_characters(self):
        self.assertFalse(is_valid_brackets("("))
        self.assertFalse(is_valid_brackets(")"))
        self.assertFalse(is_valid_brackets("["))
        self.assertFalse(is_valid_brackets("}"))

    def test_nested_valid(self):
        self.assertTrue(is_valid_brackets("((({{[[]]}})))"))
        self.assertTrue(is_valid_brackets("{[()]}"))

    def test_closing_first_and_unmatched_leftovers(self):
        self.assertFalse(is_valid_brackets(")("))
        self.assertFalse(is_valid_brackets("()("))
        self.assertFalse(is_valid_brackets("(()"))
        self.assertFalse(is_valid_brackets("())("))

    def test_large_valid_nested(self):
        # 50,000 '(' followed by 50,000 ')'
        depth = 50_000
        s = "(" * depth + ")" * depth
        self.assertTrue(is_valid_brackets(s))

    def test_large_valid_concatenated(self):
        # 50,000 pairs of "()"
        s = "()" * 50_000
        self.assertTrue(is_valid_brackets(s))

    def test_large_invalid_mismatch_at_end(self):
        depth = 40_000
        # Perfectly balanced except the very last closing bracket is mismatched
        s = "[" * depth + "]" * (depth - 1) + ")"
        self.assertFalse(is_valid_brackets(s))
