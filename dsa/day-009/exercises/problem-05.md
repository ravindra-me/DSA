# Problem 5: Reorder and Interweave List

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Combining midpoint split, in-place reversal, and alternating merge | [Day 9: Linked List Techniques](../README.md) |

## Problem Statement

You are given the `head` of a singly linked list. The list can be represented as:
$L_0 \to L_1 \to \dots \to L_{n-1} \to L_n$

Reorder the list in-place so that it becomes:
$L_0 \to L_n \to L_1 \to L_{n-1} \to L_2 \to L_{n-2} \to \dots$

You must not modify the values in the list's nodes—only node pointers may be changed. The reordering must be completed in $O(N)$ time and $O(1)$ auxiliary space.

## Input

`head`: The head `ListNode` of the list to be reordered.

## Output

`ListNode | None`: The head of the reordered list.

## Constraints

- The number of nodes in the list is between 1 and 5 * 10^4.
- -10^9 <= ListNode.val <= 10^9

## Examples

**Example 1**

```text
Input:  head = [1, 2, 3, 4]
Output: [1, 4, 2, 3]
```

L0=1, L1=2, L2=3, L3=4. Output is L0 -> L3 -> L1 -> L2 = 1 -> 4 -> 2 -> 3.

**Example 2**

```text
Input:  head = [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]
```

L0=1, L1=2, L2=3, L3=4, L4=5. Output is L0 -> L4 -> L1 -> L3 -> L2 = 1 -> 5 -> 2 -> 4 -> 3.

**Example 3**

```text
Input:  head = [1]
Output: [1]
```

A single node list remains unchanged.

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def reorder_list(head: ListNode | None) -> ListNode | None:
    """Reorder the list in-place to L0 -> Ln -> L1 -> Ln-1 -> ..."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Find the middle of the list with fast and slow pointers, split into two halves, reverse the second half in-place, and then interweave the two halves alternately.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
