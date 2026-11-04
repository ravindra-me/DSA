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
from problem_02 import ListNode, split_list_to_parts  # noqa: E402
# ---- End of generated header ----

import unittest

def list_to_array(head: ListNode | None) -> list[int]:
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr

def array_to_list(arr: list[int]) -> ListNode | None:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

class TestSplitListToParts(unittest.TestCase):
    def test_example_1(self):
        head = array_to_list([1, 2, 3])
        k = 5
        parts = split_list_to_parts(head, k)
        res = [list_to_array(p) for p in parts]
        self.assertEqual(res, [[1], [2], [3], [], []])

    def test_example_2(self):
        head = array_to_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        k = 3
        parts = split_list_to_parts(head, k)
        res = [list_to_array(p) for p in parts]
        self.assertEqual(res, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]])

    def test_empty_list(self):
        parts = split_list_to_parts(None, 3)
        res = [list_to_array(p) for p in parts]
        self.assertEqual(res, [[], [], []])

    def test_single_element(self):
        head = array_to_list([42])
        parts = split_list_to_parts(head, 2)
        res = [list_to_array(p) for p in parts]
        self.assertEqual(res, [[42], []])

    def test_k_equals_one(self):
        head = array_to_list([1, 2, 3, 4])
        parts = split_list_to_parts(head, 1)
        res = [list_to_array(p) for p in parts]
        self.assertEqual(res, [[1, 2, 3, 4]])

    def test_duplicates_and_zeros(self):
        head = array_to_list([0, 0, -1, -1, 5])
        parts = split_list_to_parts(head, 2)
        res = [list_to_array(p) for p in parts]
        self.assertEqual(res, [[0, 0, -1], [-1, 5]])

    def test_large_input(self):
        nodes_count = 1000
        k = 37
        vals = list(range(nodes_count))
        head = array_to_list(vals)
        
        parts = split_list_to_parts(head, k)
        res = [list_to_array(p) for p in parts]
        
        # Verification against mathematical division
        width, remainder = divmod(nodes_count, k)
        expected_sizes = [width + (1 if i < remainder else 0) for i in range(k)]
        
        self.assertEqual(len(res), k)
        self.assertEqual([len(p) for p in res], expected_sizes)
        
        flattened = [val for p in res for val in p]
        self.assertEqual(flattened, vals)
