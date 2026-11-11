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
from problem_03 import ListNode, sort_list  # noqa: E402
# ---- End of generated header ----

import random
from typing import List, Optional


def build_list(vals: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    res = []
    curr = head
    while curr is not None:
        res.append(curr.val)
        curr = curr.next
    return res


class TestSortList(TestCase):
    def test_example_1(self):
        head = build_list([4, 2, 1, 3])
        sorted_head = sort_list(head)
        self.assertEqual(to_list(sorted_head), [1, 2, 3, 4])

    def test_example_2_negatives_and_zero(self):
        head = build_list([-1, 5, 3, 4, 0])
        sorted_head = sort_list(head)
        self.assertEqual(to_list(sorted_head), [-1, 0, 3, 4, 5])

    def test_empty_list(self):
        sorted_head = sort_list(None)
        self.assertIsNone(sorted_head)

    def test_single_node(self):
        head = build_list([42])
        sorted_head = sort_list(head)
        self.assertEqual(to_list(sorted_head), [42])

    def test_two_nodes(self):
        head = build_list([2, 1])
        sorted_head = sort_list(head)
        self.assertEqual(to_list(sorted_head), [1, 2])

    def test_duplicates(self):
        vals = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        head = build_list(vals)
        sorted_head = sort_list(head)
        self.assertEqual(to_list(sorted_head), sorted(vals))

    def test_large_random_list(self):
        rng = random.Random(42)
        vals = [rng.randint(-100000, 100000) for _ in range(10000)]
        head = build_list(vals)
        sorted_head = sort_list(head)
        self.assertEqual(to_list(sorted_head), sorted(vals))
