# Problem 3: Sort Linked List in O(n log n)

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Divide-and-conquer merge sort on singly linked lists with O(1) auxiliary node space | [Day 33: Merge Sort](../README.md) |

## Problem Statement

Given the head of a singly linked list, sort the list in ascending order and return its head. You must achieve $O(n \log n)$ time complexity and $O(\log n)$ stack space without creating duplicate node objects.

## Input

`head: Optional[ListNode]`, the head of an unsorted singly linked list.

## Output

`Optional[ListNode]`, the head of the sorted singly linked list.

## Constraints

- The number of nodes in the list is in the range [0, 5 * 10^4].
- -10^5 <= Node.val <= 10^5

## Examples

**Example 1**

```text
Input:  head = [4, 2, 1, 3]
Output: [1, 2, 3, 4]
```

The unsorted list is divided and merged into ascending order.

**Example 2**

```text
Input:  head = [-1, 5, 3, 4, 0]
Output: [-1, 0, 3, 4, 5]
```

Negative values and zeros sorted properly.

**Example 3**

```text
Input:  head = []
Output: []
```

An empty list returns None.

## Function Signature

```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Sorts a singly linked list in O(n log n) time using merge sort."""
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use the fast and slow pointer technique to find the middle node and disconnect the list into two halves. Recursively sort each half, then merge the two sorted halves by pointer manipulation.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
