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
from problem_01 import ListNode, merge_two_lists  # noqa: E402
# ---- End of generated header ----

import random
from typing import List, Optional

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_python_list(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr is not None:
        result.append(curr.val)
        curr = curr.next
    return result

class TestMergeTwoLists(TestCase):
    def test_example_1_interleaved(self):
        l1 = build_linked_list([1, 2, 4])
        l2 = build_linked_list([1, 3, 4])
        merged = merge_two_lists(l1, l2)
        self.assertEqual(to_python_list(merged), [1, 1, 2, 3, 4, 4])

    def test_example_2_both_empty(self):
        merged = merge_two_lists(None, None)
        self.assertIsNone(merged)

    def test_example_3_one_empty(self):
        l1 = None
        l2 = build_linked_list([0])
        merged = merge_two_lists(l1, l2)
        self.assertEqual(to_python_list(merged), [0])

    def test_single_element_lists(self):
        l1 = build_linked_list([2])
        l2 = build_linked_list([1])
        merged = merge_two_lists(l1, l2)
        self.assertEqual(to_python_list(merged), [1, 2])

    def test_negative_and_duplicates(self):
        l1 = build_linked_list([-10, -5, 0, 3, 3])
        l2 = build_linked_list([-7, -5, 2, 4])
        merged = merge_two_lists(l1, l2)
        self.assertEqual(to_python_list(merged), [-10, -7, -5, -5, 0, 2, 3, 3, 4])

    def test_disjoint_ranges(self):
        l1 = build_linked_list([1, 2, 3])
        l2 = build_linked_list([4, 5, 6])
        merged = merge_two_lists(l1, l2)
        self.assertEqual(to_python_list(merged), [1, 2, 3, 4, 5, 6])

    def test_large_deterministic_lists(self):
        rng = random.Random(42)
        raw1 = sorted([rng.randint(-100, 100) for _ in range(500)])
        raw2 = sorted([rng.randint(-100, 100) for _ in range(500)])
        expected = sorted(raw1 + raw2)
        l1 = build_linked_list(raw1)
        l2 = build_linked_list(raw2)
        merged = merge_two_lists(l1, l2)
        self.assertEqual(to_python_list(merged), expected)
