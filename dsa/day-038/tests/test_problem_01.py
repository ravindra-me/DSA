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
from problem_01 import StreamFirstUnique  # noqa: E402
# ---- End of generated header ----

import random
import unittest


class TestStreamFirstUnique(unittest.TestCase):
    def test_example_one(self) -> None:
        stream = StreamFirstUnique()
        stream.add("a")
        stream.add("b")
        self.assertEqual(stream.get_first_unique(), "a")
        stream.add("a")
        self.assertEqual(stream.get_first_unique(), "b")
        stream.add("b")
        self.assertEqual(stream.get_first_unique(), "")

    def test_empty_stream(self) -> None:
        stream = StreamFirstUnique()
        self.assertEqual(stream.get_first_unique(), "")

    def test_single_element(self) -> None:
        stream = StreamFirstUnique()
        stream.add("z")
        self.assertEqual(stream.get_first_unique(), "z")
        stream.add("z")
        self.assertEqual(stream.get_first_unique(), "")

    def test_multiple_identical_characters(self) -> None:
        stream = StreamFirstUnique()
        for _ in range(100):
            stream.add("x")
        self.assertEqual(stream.get_first_unique(), "")
        stream.add("y")
        self.assertEqual(stream.get_first_unique(), "y")

    def test_interleaved_duplicates(self) -> None:
        stream = StreamFirstUnique()
        chars = ["a", "b", "c", "d", "a", "c", "b"]
        expected = ["a", "a", "a", "a", "b", "b", "d"]
        for ch, exp in zip(chars, expected):
            stream.add(ch)
            self.assertEqual(stream.get_first_unique(), exp)

    def test_all_alphabet_unique_then_all_duplicated(self) -> None:
        stream = StreamFirstUnique()
        alphabet = [chr(ord("a") + i) for i in range(26)]
        for ch in alphabet:
            stream.add(ch)
            self.assertEqual(stream.get_first_unique(), "a")
        
        # Invalidate from 'a' to 'y'
        for idx, ch in enumerate(alphabet[:-1]):
            stream.add(ch)
            self.assertEqual(stream.get_first_unique(), alphabet[idx + 1])
        
        # Finally invalidate 'z'
        stream.add("z")
        self.assertEqual(stream.get_first_unique(), "")

    def test_large_random_stream(self) -> None:
        stream = StreamFirstUnique()
        rng = random.Random(1337)
        stream_history: list[str] = []
        counts: dict[str, int] = {}

        # Run 5000 operations to test performance and verify correctness against reference
        for step in range(5000):
            ch = chr(ord("a") + rng.randint(0, 25))
            stream.add(ch)
            stream_history.append(ch)
            counts[ch] = counts.get(ch, 0) + 1

            # Check periodically
            if step % 250 == 0:
                ref_unique = ""
                for c in stream_history:
                    if counts[c] == 1:
                        ref_unique = c
                        break
                self.assertEqual(stream.get_first_unique(), ref_unique)
