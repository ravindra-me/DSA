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
from problem_04 import find_length  # noqa: E402
# ---- End of generated header ----

import random


class TestMaximumLengthOfRepeatedSubarray(TestCase):
    def test_example_1(self) -> None:
        nums1 = [1, 2, 3, 2, 1]
        nums2 = [3, 2, 1, 4, 7]
        self.assertEqual(find_length(nums1, nums2), 3)

    def test_example_2_all_identical(self) -> None:
        nums1 = [0, 0, 0, 0, 0]
        nums2 = [0, 0, 0, 0, 0]
        self.assertEqual(find_length(nums1, nums2), 5)

    def test_no_common_elements(self) -> None:
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        self.assertEqual(find_length(nums1, nums2), 0)

    def test_single_element_cases(self) -> None:
        self.assertEqual(find_length([1], [1]), 1)
        self.assertEqual(find_length([1], [2]), 0)

    def test_repeats_and_disjoint_segments(self) -> None:
        # Common segments: [1, 2] (len 2), [7, 8, 9] (len 3)
        nums1 = [1, 2, 5, 7, 8, 9, 3]
        nums2 = [7, 8, 9, 1, 2, 0]
        self.assertEqual(find_length(nums1, nums2), 3)

    def test_different_lengths_and_boundary_values(self) -> None:
        nums1 = [0, 100, 0, 100, 0]
        nums2 = [100, 0, 100]
        self.assertEqual(find_length(nums1, nums2), 3)

    def test_large_input_performance(self) -> None:
        rng = random.Random(42)
        # Create two lists of length 1000
        # Embed a known unique common segment of length 150
        base1 = [rng.randint(1, 50) for _ in range(400)]
        shared = [100] * 150
        base2 = [rng.randint(1, 50) for _ in range(450)]

        nums1 = base1 + shared + base2
        nums2 = [rng.randint(1, 50) for _ in range(300)] + shared + [rng.randint(1, 50) for _ in range(550)]

        # Expected is at least 150
        result = find_length(nums1, nums2)
        self.assertGreaterEqual(result, 150)
