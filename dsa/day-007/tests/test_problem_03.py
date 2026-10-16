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
from problem_03 import ListNode, merge_two_lists  # noqa: E402
# ---- End of generated header ----

class TestMergeTwoLists(unittest.TestCase):
    def _list_to_arr(self, node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res

    def _arr_to_list(self, arr):
        dummy = ListNode()
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def test_example_1(self):
        l1 = self._arr_to_list([1, 2, 4])
        l2 = self._arr_to_list([1, 3, 4])
        merged = merge_two_lists(l1, l2)
        self.assertEqual(self._list_to_arr(merged), [1, 1, 2, 3, 4, 4])

    def test_example_2(self):
        l1 = self._arr_to_list([])
        l2 = self._arr_to_list([0])
        merged = merge_two_lists(l1, l2)
        self.assertEqual(self._list_to_arr(merged), [0])

    def test_both_empty(self):
        self.assertIsNone(merge_two_lists(None, None))

    def test_single_elements(self):
        l1 = self._arr_to_list([5])
        l2 = self._arr_to_list([1])
        merged = merge_two_lists(l1, l2)
        self.assertEqual(self._list_to_arr(merged), [1, 5])

    def test_duplicate_values(self):
        l1 = self._arr_to_list([1, 1, 1])
        l2 = self._arr_to_list([1, 1, 1])
        merged = merge_two_lists(l1, l2)
        self.assertEqual(self._list_to_arr(merged), [1, 1, 1, 1, 1, 1])

    def test_negative_numbers(self):
        l1 = self._arr_to_list([-10, -5, 0])
        l2 = self._arr_to_list([-7, -2, 5])
        merged = merge_two_lists(l1, l2)
        self.assertEqual(self._list_to_arr(merged), [-10, -7, -5, -2, 0, 5])

    def test_large_input(self):
        # 50 nodes as per constraint
        arr1 = list(range(0, 100, 2))
        arr2 = list(range(1, 100, 2))
        l1 = self._arr_to_list(arr1)
        l2 = self._arr_to_list(arr2)
        merged = merge_two_lists(l1, l2)
        self.assertEqual(self._list_to_arr(merged), list(range(0, 100)))
