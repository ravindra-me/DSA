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
from problem_04 import ListNode, remove_nth_from_end  # noqa: E402
# ---- End of generated header ----

class TestRemoveNthFromEnd(unittest.TestCase):
    def _list_to_arr(self, node):
        res = []
        curr = node
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

    def _arr_to_list(self, arr):
        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def test_example_one(self):
        head = self._arr_to_list([1, 2, 3, 4, 5])
        result = remove_nth_from_end(head, 2)
        self.assertEqual(self._list_to_arr(result), [1, 2, 3, 5])

    def test_single_node_removal(self):
        head = self._arr_to_list([1])
        result = remove_nth_from_end(head, 1)
        self.assertEqual(self._list_to_arr(result), [])

    def test_remove_head(self):
        head = self._arr_to_list([1, 2])
        result = remove_nth_from_end(head, 2)
        self.assertEqual(self._list_to_arr(result), [2])

    def test_remove_last_node(self):
        head = self._arr_to_list([1, 2, 3])
        result = remove_nth_from_end(head, 1)
        self.assertEqual(self._list_to_arr(result), [1, 2])

    def test_large_list(self):
        # Test removing from a list of size 30 (max constraint)
        vals = list(range(1, 31))
        head = self._arr_to_list(vals)
        # Remove 15th from end, which is 16
        result = remove_nth_from_end(head, 15)
        expected = [i for i in vals if i != 16]
        self.assertEqual(self._list_to_arr(result), expected)

    def test_duplicates(self):
        head = self._arr_to_list([1, 2, 1, 2])
        result = remove_nth_from_end(head, 3)
        # The 3rd from end is 2 (index 1)
        self.assertEqual(self._list_to_arr(result), [1, 1, 2])
