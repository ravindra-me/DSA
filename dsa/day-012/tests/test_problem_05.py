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
from problem_05 import sum_subarray_mins  # noqa: E402
# ---- End of generated header ----

import random


class TestSumSubarrayMins(TestCase):
    def test_example_1(self) -> None:
        self.assertEqual(sum_subarray_mins([3, 1, 2, 4]), 17)

    def test_example_2(self) -> None:
        self.assertEqual(sum_subarray_mins([11, 81, 94, 43, 3]), 444)

    def test_single_element(self) -> None:
        self.assertEqual(sum_subarray_mins([42]), 42)

    def test_all_identical_elements(self) -> None:
        # For [5, 5, 5]: subarrays are [5], [5], [5], [5, 5], [5, 5], [5, 5, 5]
        # Counts: 3 + 2 + 1 = 6 subarrays, each with min 5 -> 30
        self.assertEqual(sum_subarray_mins([5, 5, 5]), 30)

    def test_strictly_increasing(self) -> None:
        # arr = [1, 2, 3]
        # [1]->1, [2]->2, [3]->3, [1,2]->1, [2,3]->2, [1,2,3]->1
        # sum = 1 + 2 + 3 + 1 + 2 + 1 = 10
        self.assertEqual(sum_subarray_mins([1, 2, 3]), 10)

    def test_strictly_decreasing(self) -> None:
        # arr = [3, 2, 1]
        # [3]->3, [2]->2, [1]->1, [3,2]->2, [2,1]->1, [3,2,1]->1
        # sum = 3 + 2 + 1 + 2 + 1 + 1 = 10
        self.assertEqual(sum_subarray_mins([3, 2, 1]), 10)

    def test_duplicates_with_variation(self) -> None:
        arr = [71, 55, 82, 55]
        # Subarrays:
        # len 1: 71, 55, 82, 55
        # len 2: min(71,55)=55, min(55,82)=55, min(82,55)=55
        # len 3: min(71,55,82)=55, min(55,82,55)=55
        # len 4: min(71,55,82,55)=55
        # Total: 71 + 55 + 82 + 55 + 55*3 + 55*2 + 55 = 71 + 82 + 55*8 = 153 + 440 = 593
        self.assertEqual(sum_subarray_mins(arr), 593)

    def test_large_input_efficiency_and_correctness(self) -> None:
        rng = random.Random(42)
        arr = [rng.randint(1, 1000) for _ in range(5000)]

        # Reference calculation on a small prefix to guarantee consistency
        prefix = arr[:50]
        expected_prefix_sum = 0
        for i in range(len(prefix)):
            curr_min = prefix[i]
            for j in range(i, len(prefix)):
                curr_min = min(curr_min, prefix[j])
                expected_prefix_sum += curr_min
        expected_prefix_sum %= 1_000_000_007

        self.assertEqual(sum_subarray_mins(prefix), expected_prefix_sum)
        # Ensure the 5000-element list runs within milliseconds
        large_result = sum_subarray_mins(arr)
        self.assertIsInstance(large_result, int)
        self.assertTrue(0 <= large_result < 1_000_000_007)
