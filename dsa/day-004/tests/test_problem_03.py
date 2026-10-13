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
from problem_03 import reverse_string  # noqa: E402
# ---- End of generated header ----

class TestReverseString(unittest.TestCase):
    def test_example_hello(self):
        self.assertEqual(reverse_string('hello'), 'olleh')

    def test_empty_string(self):
        self.assertEqual(reverse_string(''), '')

    def test_single_character(self):
        self.assertEqual(reverse_string('a'), 'a')

    def test_palindrome(self):
        self.assertEqual(reverse_string('racecar'), 'racecar')

    def test_with_spaces_and_symbols(self):
        self.assertEqual(reverse_string('a b!'), '!b a')

    def test_large_input_string(self):
        # Construct a 500 character string to test recursion depth and correctness
        # 500 is safe within standard recursion limits
        input_str = 'a' * 250 + 'b' * 250
        expected = 'b' * 250 + 'a' * 250
        self.assertEqual(reverse_string(input_str), expected)
