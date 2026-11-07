# Problem 3: Sort Linked List in O(n log n)

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | fast-slow-pointers | [Day 29: Linked List Techniques](../README.md) |

## Problem Statement

Given the `head` of a linked list, return the list sorted in ascending order. You must achieve $O(n \log n)$ time complexity and $O(\log n)$ stack space (or $O(1)$ auxiliary space excluding recursion).

## Input

`head: Optional[ListNode]`

## Output

`Optional[ListNode]` representing the head of the sorted list.

## Constraints

- The number of nodes in the list is in the range [0, 5 * 10^4].
- -10^5 <= Node.val <= 10^5

## Examples

**Example 1**

```text
Input:  head = [4, 2, 1, 3]
Output: [1, 2, 3, 4]
```

Standard ascending sort.

**Example 2**

```text
Input:  head = [-1, 5, 3, 4, 0]
Output: [-1, 0, 3, 4, 5]
```

Handles negative numbers and zero correctly.

**Example 3**

```text
Input:  head = []
Output: []
```

An empty list is already sorted.

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Sorts linked list in O(n log n) time using merge sort."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Implement top-down merge sort: use fast/slow pointers to find the midpoint and sever the list into two halves, recursively sort both halves, then merge the two sorted sublists.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
