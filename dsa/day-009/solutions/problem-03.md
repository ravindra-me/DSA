# Solution 3: Find Cycle Entrance Value

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Floyd's Tortoise and Hare cycle detection and entrance resolution

## Approach

Use Floyd's Cycle-Finding Algorithm (Tortoise and Hare) with two pointers moving at speeds of 1 and 2. Once they meet inside the loop, reset one pointer to the list's head and advance both pointers one node at a time; their next meeting point is guaranteed to be the entrance of the cycle.

## Thought Process

A naive approach uses a hash set to store visited node identities (`id(node)`). While this runs in $O(N)$ time, it requires $O(N)$ auxiliary space, violating the strict $O(1)$ memory constraint.

To achieve $O(1)$ space, we use two pointers: `slow` advancing one step and `fast` advancing two steps per iteration. If `fast` or `fast.next` reaches `None`, the list is acyclic. If a cycle exists, `fast` must eventually lap `slow` inside the cycle.

Let the distance from the head to the cycle entrance be $L$, and the distance from the cycle entrance to the meeting point be $k$. Let the cycle length be $C$. When they meet:
- Distance traveled by `slow` = $L + k$
- Distance traveled by `fast` = $L + k + m \cdot C$ (where $m \ge 1$)

Since `fast` travels twice as fast as `slow`:
$$2(L + k) = L + k + m \cdot C \implies L + k = m \cdot C \implies L = m \cdot C - k = (m - 1)C + (C - k)$$

Notice that $(C - k)$ is exactly the distance from the meeting point to the cycle entrance continuing along the cycle. Therefore, if we place one pointer at the list head and keep the other at the meeting point, advancing both by one step at a time, they will meet after exactly $L$ steps at the cycle entrance.

## Algorithm

1. Check if `head` is `None` or `head.next` is `None`. If so, return `None` immediately because no cycle is possible.
2. Initialize two pointers: `slow = head` and `fast = head`.
3. While `fast` and `fast.next` are not `None`, advance `slow = slow.next` and `fast = fast.next.next`.
4. If `slow == fast`, a cycle is detected; break the loop.
5. If the loop terminated because `fast` or `fast.next` became `None`, return `None` (acyclic).
6. Reset one pointer: set `slow = head` while leaving `fast` at the meeting point.
7. Advance both `slow` and `fast` one step at a time (`slow = slow.next`, `fast = fast.next`) until `slow == fast`.
8. Return `slow.val`, which is the value at the entrance of the cycle.

## Complexity Analysis

- **Time:** $O(N)$ where $N$ is the total number of nodes. The slow pointer takes at most $N$ steps before meeting the fast pointer, and at most $N$ steps from the head to find the entrance.
- **Space:** $O(1)$ auxiliary space as only two pointer references are maintained.

## Edge Cases

- Empty list (`head is None`): Handled immediately by returning `None`.
- Single node without cycle (`head.next is None`): Handled by fast pointer loop condition, returning `None`.
- Single node pointing to itself (cycle of length 1 at head): Pointers meet quickly, entrance is the head node.
- Two-node cycle: Fast pointer laps slow pointer within 2 steps, correctly identifies entry.
- Cycle starts at head node ($L = 0$): Both pointers start at head and meet at head again in phase 2.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


def find_cycle_entrance_value(head: ListNode | None) -> int | None:
    """Return the value of the cycle's entrance node, or None if acyclic."""
    if head is None or head.next is None:
        return None

    slow: ListNode | None = head
    fast: ListNode | None = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None

    slow = head
    while slow is not fast:
        assert slow is not None and fast is not None
        slow = slow.next
        fast = fast.next

    return slow.val
```
