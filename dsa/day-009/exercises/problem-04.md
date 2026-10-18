# Problem 4: Merge Two Sorted Linked Lists

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Sentinel node pointer splicing for sorted list combination | [Day 9: Linked List Techniques](../README.md) |

## Problem Statement

You are given the heads of two sorted singly linked lists, `list1` and `list2`. Both lists are sorted in non-decreasing order.

Merge the two lists into a single sorted linked list by splicing together the existing nodes. Return the head of the merged linked list.

You must not allocate new `ListNode` instances (except optionally a sentinel head node for splicing) and must achieve $O(1)$ auxiliary space.

## Input

- `list1`: The head `ListNode` of the first sorted list (or `None`).
- `list2`: The head `ListNode` of the second sorted list (or `None`).

## Output

`ListNode | None`: Head of the merged sorted linked list.

## Constraints

- The number of nodes in each list is between 0 and 5 * 10^4.
- -10^9 <= ListNode.val <= 10^9
- Both list1 and list2 are sorted in non-decreasing order.

## Examples

**Example 1**

```text
Input:  list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
```

Nodes are spliced in ascending order: 1 -> 1 -> 2 -> 3 -> 4 -> 4.

**Example 2**

```text
Input:  list1 = [], list2 = []
Output: []
```

Both lists are empty; the merged result is None.

**Example 3**

```text
Input:  list1 = [], list2 = [0]
Output: [0]
```

Merging an empty list with [0] yields [0].

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """Merge two sorted linked lists by splicing nodes in-place."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a dummy head node with a tail pointer. In a loop, attach the smaller node to tail.next and advance pointers until one list is exhausted, then append the remainder.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
