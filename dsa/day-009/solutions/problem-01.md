# Solution 1: Find Middle Node Value

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Fast and slow pointers for finding midpoints

## Approach

Use the two-pointer 'tortoise and hare' technique: advance a `slow` pointer by one step and a `fast` pointer by two steps in each iteration. When `fast` reaches the end of the list (or moves past it), `slow` will be situated at the middle node (or second middle node for an even-length list).

## Thought Process

A naive approach counts the total number of nodes $N$ in a first pass, computes the middle index $\lfloor N / 2 \rfloor$, and traverses again to reach that index. While $O(N)$ time, this requires two passes over the list.

To achieve a single pass with $O(1)$ extra space, we observe the relationship between speeds: if pointer `fast` travels twice as fast as pointer `slow`, then at any point `slow` has traversed half the distance of `fast`. When `fast` reaches the end of the list (index $N-1$ or $N$), `slow` has traversed $\lfloor N / 2 \rfloor$ steps, pointing precisely at the middle node (or the second middle node when $N$ is even).

## Algorithm

1. Initialize `slow = head` and `fast = head`.
2. Loop while `fast` is not `None` and `fast.next` is not `None`.
3. Inside the loop, advance `slow` by one step: `slow = slow.next`.
4. Advance `fast` by two steps: `fast = fast.next.next`.
5. When the loop terminates, return `slow.val`.

## Complexity Analysis

- **Time:** $O(N)$ because the fast pointer takes $N/2$ steps, traversing the list in a single pass.
- **Space:** $O(1)$ auxiliary space since only two pointer references (`slow` and `fast`) are maintained.

## Edge Cases

- Single node: `fast.next` is initially `None`, loop does not run, returns the single node's value correctly.
- Two nodes: loop runs once; `slow` moves to the second node, `fast` becomes `None`, returning the second node's value as required.
- Even number of nodes: `fast` eventually reaches `None`, leaving `slow` at index $N/2$ (the second middle node).
- Odd number of nodes: `fast.next` eventually reaches `None`, leaving `slow` at index $(N-1)/2$.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


def find_middle_value(head: ListNode) -> int:
    """Return the value of the middle node (second middle if even)."""
    slow: ListNode | None = head
    fast: ListNode | None = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.val
```
