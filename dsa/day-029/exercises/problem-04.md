# Problem 4: Merge K Sorted Linked Lists

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | k-way-merge | [Day 29: Linked List Techniques](../README.md) |

## Problem Statement

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return its head.

## Input

`lists: list[Optional[ListNode]]`

## Output

`Optional[ListNode]`

## Constraints

- k == len(lists)
- 0 <= k <= 10^4
- 0 <= total number of nodes across all lists <= 5 * 10^4
- -10^4 <= Node.val <= 10^4
- `lists[i]` is sorted in ascending order.

## Examples

**Example 1**

```text
Input:  lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
Output: [1, 1, 2, 3, 4, 4, 5, 6]
```

The three sorted lists are merged into a single non-decreasing list.

**Example 2**

```text
Input:  lists = []
Output: []
```

No lists provided.

**Example 3**

```text
Input:  lists = [[]]
Output: []
```

A single empty list yields an empty result.

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """Merges k sorted linked lists into one sorted linked list."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a min-heap tracking `(node.val, tie_breaker_id, node)` with size at most k, or divide-and-conquer pairwise merge to achieve O(N log k) time complexity.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
