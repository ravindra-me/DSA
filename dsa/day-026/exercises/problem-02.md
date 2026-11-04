# Problem 2: Split Linked List into k Consecutive Parts

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | List length computation and chunk slicing with dummy pointers | [Day 26: Linked Lists](../README.md) |

## Problem Statement

Given the head of a singly linked list and an integer `k`, split the list into `k` consecutive parts. The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. Extra length should be distributed to the earlier parts. Return an array of the `k` parts.

## Input

head: Optional[ListNode], k: int

## Output

list[Optional[ListNode]]

## Constraints

- The number of nodes in the list is in the range [0, 1000].
- 0 <= Node.val <= 1000
- 1 <= k <= 50

## Examples

**Example 1**

```text
Input:  head = 1 -> 2 -> 3, k = 5
Output: [1, 2, 3, None, None]
```

The 3 nodes are split into 5 parts, first 3 have size 1, remaining 2 are empty.

**Example 2**

```text
Input:  head = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
Output: [1->2->3->4, 5->6->7, 8->9->10]
```

10 nodes split into 3 parts: sizes 4, 3, 3.

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def split_list_to_parts(head: ListNode | None, k: int) -> list[ListNode | None]:
    """Splits linked list into k consecutive balanced parts."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Calculate total length N. Each part gets size N // k, with the first N % k parts getting 1 extra node. Split by cutting next pointers during traversal. Aim for O(n + k) time and O(k) output space.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
