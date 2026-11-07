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
from problem_04 import ListNode, merge_k_lists  # noqa: E402
# ---- End of generated header ----

import random
from typing import Optional


def build_list(vals: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> list[int]:
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


class TestMergeKSortedLists(TestCase):
    def test_example_1(self):
        raw = [[1, 4, 5], [1, 3, 4], [2, 6]]
        lists = [build_list(sub) for sub in raw]
        merged = merge_k_lists(lists)
        self.assertEqual(to_list(merged), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_empty_lists(self):
        self.assertIsNone(merge_k_lists([]))

    def test_lists_with_none(self):
        lists = [None, build_list([]), None]
        self.assertIsNone(merge_k_lists(lists))

    def test_single_element_and_single_list(self):
        lists = [build_list([42])]
        self.assertEqual(to_list(merge_k_lists(lists)), [42])

    def test_negative_and_zero_values(self):
        raw = [[-10, -5, 0], [-8, -2, 3], [-5, 0, 5]]
        lists = [build_list(sub) for sub in raw]
        merged = merge_k_lists(lists)
        expected = sorted([-10, -5, 0, -8, -2, 3, -5, 0, 5])
        self.assertEqual(to_list(merged), expected)

    def test_duplicate_values_collision(self):
        raw = [[1, 1, 1], [1, 1], [1, 1, 1, 1]]
        lists = [build_list(sub) for sub in raw]
        merged = merge_k_lists(lists)
        self.assertEqual(to_list(merged), [1] * 9)

    def test_large_input_many_lists(self):
        rng = random.Random(42)
        k = 200
        nodes_per_list = 50
        all_vals = []
        lists = []
        for _ in range(k):
            vals = sorted(rng.randint(-10000, 10000) for _ in range(nodes_per_list))
            all_vals.extend(vals)
            lists.append(build_list(vals))
        expected = sorted(all_vals)
        merged = merge_k_lists(lists)
        self.assertEqual(to_list(merged), expected)
