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
from problem_04 import ListNode, merge_two_sorted_lists  # noqa: E402
# ---- End of generated header ----

import random


def to_linked_list(values: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    result = []
    curr = head
    while curr is not None:
        result.append(curr.val)
        curr = curr.next
    return result


class TestMergeTwoSortedLists(TestCase):
    def test_example_1(self):
        l1 = to_linked_list([1, 2, 4])
        l2 = to_linked_list([1, 3, 4])
        merged = merge_two_sorted_lists(l1, l2)
        self.assertEqual(to_list(merged), [1, 1, 2, 3, 4, 4])

    def test_example_2_both_empty(self):
        l1 = to_linked_list([])
        l2 = to_linked_list([])
        merged = merge_two_sorted_lists(l1, l2)
        self.assertIsNone(merged)

    def test_example_3_one_empty(self):
        l1 = to_linked_list([])
        l2 = to_linked_list([0])
        merged = merge_two_sorted_lists(l1, l2)
        self.assertEqual(to_list(merged), [0])

        l1_rev = to_linked_list([0])
        l2_rev = to_linked_list([])
        merged_rev = merge_two_sorted_lists(l1_rev, l2_rev)
        self.assertEqual(to_list(merged_rev), [0])

    def test_single_element_lists(self):
        l1 = to_linked_list([2])
        l2 = to_linked_list([1])
        merged = merge_two_sorted_lists(l1, l2)
        self.assertEqual(to_list(merged), [1, 2])

    def test_negative_values_and_duplicates(self):
        l1 = to_linked_list([-10, -5, 0, 0, 7])
        l2 = to_linked_list([-7, -5, 1, 9])
        merged = merge_two_sorted_lists(l1, l2)
        self.assertEqual(to_list(merged), [-10, -7, -5, -5, 0, 0, 1, 7, 9])

    def test_disjoint_ranges(self):
        l1 = to_linked_list([1, 2, 3])
        l2 = to_linked_list([10, 20, 30])
        merged = merge_two_sorted_lists(l1, l2)
        self.assertEqual(to_list(merged), [1, 2, 3, 10, 20, 30])

    def test_large_input_performance(self):
        rng = random.Random(42)
        arr1 = sorted(rng.randint(-1_000_000, 1_000_000) for _ in range(15_000))
        arr2 = sorted(rng.randint(-1_000_000, 1_000_000) for _ in range(15_000))
        expected = sorted(arr1 + arr2)

        l1 = to_linked_list(arr1)
        l2 = to_linked_list(arr2)
        merged = merge_two_sorted_lists(l1, l2)
        self.assertEqual(to_list(merged), expected)
