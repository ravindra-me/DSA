# Problem 4: Insertion Sort on Linked List

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Insertion sort adaptation on linked data structures and pointer manipulation | [Day 31: Bubble, Selection & Insertion Sort](../README.md) |

## Problem Statement

Given the head of a singly-linked list, sort the list using **Insertion Sort** and return the head of the sorted list.

The algorithm should maintain a sorted sublist that grows from the head. At each step, remove the next unsorted node from the input list and insert it into its correct position within the sorted portion of the list.

## Input

The head node of a singly-linked list (`ListNode | None`).

## Output

The head node of the sorted singly-linked list (`ListNode | None`).

## Constraints

- The number of nodes in the list is in the range [0, 5000].
- -5000 <= Node.val <= 5000

## Examples

**Example 1**

```text
Input:  head = 4 -> 2 -> 1 -> 3
Output: 1 -> 2 -> 3 -> 4
```

The nodes are detached and reinserted in non-decreasing order.

**Example 2**

```text
Input:  head = -1 -> 5 -> 3 -> 4 -> 0
Output: -1 -> 0 -> 3 -> 4 -> 5
```

Insertion sort maintains relative order and sorts negative numbers correctly.

**Example 3**

```text
Input:  head = None
Output: None
```

An empty list returns None.

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def insertion_sort_list(head: ListNode | None) -> ListNode | None:
    """Sorts a singly-linked list using insertion sort."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a dummy head for the sorted portion. For each node in the unsorted list, find its correct insertion point in the sorted portion starting from the dummy head, update next pointers, and advance.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
