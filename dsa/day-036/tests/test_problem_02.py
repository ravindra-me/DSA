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
from problem_02 import sift_down  # noqa: E402
# ---- End of generated header ----

import random


class TestSiftDown(TestCase):
    def test_example_1(self) -> None:
        nums = [1, 14, 10, 8, 7, 9, 3, 2, 4, 6]
        sift_down(nums, 10, 0)
        self.assertEqual(nums, [14, 8, 10, 4, 7, 9, 3, 2, 1, 6])

    def test_example_2_no_swaps_needed(self) -> None:
        nums = [5, 4, 3, 2, 1]
        sift_down(nums, 5, 0)
        self.assertEqual(nums, [5, 4, 3, 2, 1])

    def test_leaf_node(self) -> None:
        nums = [10, 9, 8, 7, 6]
        # Index 3 is a leaf in a heap of size 5 (left child would be 7 >= 5)
        sift_down(nums, 5, 3)
        self.assertEqual(nums, [10, 9, 8, 7, 6])

    def test_single_element_and_boundary(self) -> None:
        nums = [42]
        sift_down(nums, 1, 0)
        self.assertEqual(nums, [42])

        # heap_size smaller than len(nums): elements past heap_size must not be touched
        nums = [1, 10, 5, 999]
        sift_down(nums, 3, 0)
        self.assertEqual(nums, [10, 1, 5, 999])

    def test_single_child_boundary(self) -> None:
        # Node 1 has left child at index 3, but no right child at index 4
        nums = [20, 2, 15, 8]
        sift_down(nums, 4, 1)
        self.assertEqual(nums, [20, 8, 15, 2])

    def test_duplicate_values_and_negatives(self) -> None:
        nums = [-10, -5, -5, -20, -6]
        sift_down(nums, 5, 0)
        # -10 should swap with the left child -5
        self.assertEqual(nums, [-5, -6, -5, -20, -10])

    def test_large_sift_down_depth(self) -> None:
        # Construct a complete binary tree of depth 16 where the root is minimum
        # and every other node satisfies the max heap property.
        depth = 16
        size = (1 << depth) - 1
        # Build a valid max heap by assigning values from size down to 2
        nums = [0] * size
        for idx in range(1, size):
            # Ensure parent is always strictly greater than children
            nums[idx] = size - idx
        nums[0] = -1  # Minimal value at root to force sift-down to a leaf

        sift_down(nums, size, 0)

        # Verify that the subtree at index 0 now satisfies the max-heap property
        for idx in range(size // 2):
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < size:
                self.assertGreaterEqual(nums[idx], nums[left])
            if right < size:
                self.assertGreaterEqual(nums[idx], nums[right])
