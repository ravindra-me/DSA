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
from problem_03 import ListNode, find_cycle_entrance_value  # noqa: E402
# ---- End of generated header ----

def build_linked_list_with_cycle(values: list[int], pos: int) -> ListNode | None:
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


class TestFindCycleEntranceValue(TestCase):
    def test_example_1_general_cycle(self):
        # head = [3, 2, 0, -4], cycle back to index 1 (val = 2)
        head = build_linked_list_with_cycle([3, 2, 0, -4], pos=1)
        self.assertEqual(find_cycle_entrance_value(head), 2)

    def test_example_2_two_node_cycle_to_head(self):
        # head = [1, 2], cycle back to index 0 (val = 1)
        head = build_linked_list_with_cycle([1, 2], pos=0)
        self.assertEqual(find_cycle_entrance_value(head), 1)

    def test_example_3_single_node_acyclic(self):
        head = build_linked_list_with_cycle([1], pos=-1)
        self.assertIsNone(find_cycle_entrance_value(head))

    def test_empty_list(self):
        self.assertIsNone(find_cycle_entrance_value(None))

    def test_single_node_self_loop(self):
        node = ListNode(42)
        node.next = node
        self.assertEqual(find_cycle_entrance_value(node), 42)

    def test_acyclic_multi_node_list(self):
        head = build_linked_list_with_cycle([10, -20, 30, -40, 50], pos=-1)
        self.assertIsNone(find_cycle_entrance_value(head))

    def test_cycle_at_tail(self):
        # Only the last node loops back to itself
        head = build_linked_list_with_cycle([1, 2, 3, 4, 5], pos=4)
        self.assertEqual(find_cycle_entrance_value(head), 5)

    def test_negative_values_and_duplicates(self):
        # Values can be negative or duplicate along the path, entry is distinct
        head = build_linked_list_with_cycle([-5, 0, -5, 100, -5], pos=2)
        self.assertEqual(find_cycle_entrance_value(head), -5)

    def test_large_input_cycle_in_middle(self):
        n = 50_000
        cycle_index = 20_000
        values = list(range(n))
        head = build_linked_list_with_cycle(values, pos=cycle_index)
        self.assertEqual(find_cycle_entrance_value(head), cycle_index)

    def test_large_input_acyclic(self):
        n = 50_000
        values = list(range(n))
        head = build_linked_list_with_cycle(values, pos=-1)
        self.assertIsNone(find_cycle_entrance_value(head))
