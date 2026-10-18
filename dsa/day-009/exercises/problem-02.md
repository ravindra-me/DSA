# Problem 2: Remove K-th Node From End

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Fixed-gap runner pointers and dummy head node | [Day 9: Linked List Techniques](../README.md) |

## Problem Statement

Given the `head` of a singly linked list and an integer `k`, remove the `k`-th node from the end of the list and return the head of the modified list.

You must accomplish this in a single traversal using $O(1)$ auxiliary space.

## Input

- `head`: The head `ListNode` of a singly linked list.
- `k`: A 1-indexed positive integer representing the position from the end.

## Output

`ListNode | None`: The head of the list after removing the target node.

## Constraints

- The number of nodes in the list is between 1 and 10^5.
- 1 <= k <= length of the list
- -10^9 <= ListNode.val <= 10^9

## Examples

**Example 1**

```text
Input:  head = [1, 2, 3, 4, 5], k = 2
Output: [1, 2, 3, 5]
```

The 2nd node from the end is 4. Removing it results in 1 -> 2 -> 3 -> 5.

**Example 2**

```text
Input:  head = [1], k = 1
Output: []
```

Removing the only node yields an empty list (None).

**Example 3**

```text
Input:  head = [1, 2], k = 2
Output: [2]
```

Removing the 2nd node from end removes the head (1), leaving [2].

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def remove_kth_from_end(head: ListNode | None, k: int) -> ListNode | None:
    """Remove the k-th node from the end and return the head of the modified list."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Create a dummy sentinel pointing to head. Advance an ahead pointer k + 1 steps ahead of behind pointer, then step both forward until ahead reaches None.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
