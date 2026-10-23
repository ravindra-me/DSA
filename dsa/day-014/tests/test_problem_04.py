# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_04.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_04 import remove_duplicate_letters  # noqa: E402
# ---- End of generated header ----

class TestRemoveDuplicateLetters(TestCase):
    def test_example_1(self) -> None:
        self.assertEqual(remove_duplicate_letters("bcabc"), "abc")

    def test_example_2(self) -> None:
        self.assertEqual(remove_duplicate_letters("cbacdcbc"), "acdb")

    def test_single_character(self) -> None:
        self.assertEqual(remove_duplicate_letters("z"), "z")

    def test_all_identical_characters(self) -> None:
        self.assertEqual(remove_duplicate_letters("aaaaaa"), "a")

    def test_already_sorted_unique(self) -> None:
        self.assertEqual(remove_duplicate_letters("abcdef"), "abcdef")

    def test_reverse_sorted_unique(self) -> None:
        self.assertEqual(remove_duplicate_letters("fedcba"), "fedcba")

    def test_duplicates_with_drop_and_no_drop(self) -> None:
        # 'b' can be dropped because it appears later; 'c' cannot be dropped when 'd' comes
        self.assertEqual(remove_duplicate_letters("bbcaac"), "bac")

    def test_complex_pattern(self) -> None:
        self.assertEqual(remove_duplicate_letters("edebbed"), "bed")

    def test_large_input_performance(self) -> None:
        # Construct a large string (10^4 characters) with repeating 'z...a' pattern
        # Expected result should be 'abcdefghijklmnopqrstuvwxyz'
        import string
        alphabet = string.ascii_lowercase
        # 400 repetitions of 26 chars = 10,400 chars
        large_s = (alphabet[::-1] + alphabet) * 150
        result = remove_duplicate_letters(large_s)
        self.assertEqual(result, alphabet)
