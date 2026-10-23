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
from problem_01 import valid_palindrome_after_one_removal  # noqa: E402
# ---- End of generated header ----

class TestValidPalindromeAfterOneRemoval(TestCase):
    def test_examples(self) -> None:
        self.assertTrue(valid_palindrome_after_one_removal("aba"))
        self.assertTrue(valid_palindrome_after_one_removal("abca"))
        self.assertFalse(valid_palindrome_after_one_removal("abc"))

    def test_single_character(self) -> None:
        self.assertTrue(valid_palindrome_after_one_removal("a"))

    def test_two_characters(self) -> None:
        self.assertTrue(valid_palindrome_after_one_removal("ab"))
        self.assertTrue(valid_palindrome_after_one_removal("aa"))

    def test_removal_at_extremes(self) -> None:
        # Extra character at the very beginning
        self.assertTrue(valid_palindrome_after_one_removal("xracecar"))
        # Extra character at the very end
        self.assertTrue(valid_palindrome_after_one_removal("racecarx"))

    def test_removal_in_middle(self) -> None:
        # Extra character right in the middle
        self.assertTrue(valid_palindrome_after_one_removal("deeee"))
        self.assertTrue(valid_palindrome_after_one_removal("eedee"))
        self.assertTrue(valid_palindrome_after_one_removal("abccbxa"))

    def test_two_mismatches_fails(self) -> None:
        # Needs at least 2 removals
        self.assertFalse(valid_palindrome_after_one_removal("abcdefba"))
        self.assertFalse(valid_palindrome_after_one_removal("tebbem"))

    def test_large_input_valid(self) -> None:
        # 100,000 characters: 50,000 'a's, one 'b', then 49,999 'a's
        s = "a" * 50000 + "b" + "a" * 49999
        self.assertTrue(valid_palindrome_after_one_removal(s))

    def test_large_input_invalid(self) -> None:
        # 100,000 characters with two misplaced characters
        s = "a" * 25000 + "b" + "a" * 25000 + "c" + "a" * 49998
        self.assertFalse(valid_palindrome_after_one_removal(s))
