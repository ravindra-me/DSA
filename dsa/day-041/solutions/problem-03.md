# Solution 3: Amortized Two-Stack Deque

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium/Hard | **Concept:** Potential method and amortized O(1) multi-operation structures

## Approach

Maintain two stacks, `front` and `back`. The top of `front` represents the front of the deque, and the top of `back` represents the back of the deque. When one stack becomes empty and a pop or peek is requested on that side, rebalance the contents by splitting the non-empty stack approximately in half between `front` and `back` using only stack operations.

## Thought Process

In a standard queue, two stacks suffice because elements only move from input stack to output stack once: when the output stack is empty, the entire input stack is reversed into the output stack, yielding amortized $O(1)$ time. For a deque, alternating between operations on both ends (e.g. repeated `push_front` followed by alternating `pop_back` and `pop_front`) could cause naive full transfers to trigger $O(n)$ shifts repeatedly, degrading to $O(n^2)$.

To achieve amortized $O(1)$ per operation for a deque, whenever an operation needs an element from an empty stack while the other stack has $k$ elements, we split the non-empty stack into two halves of size $\lfloor k / 2 \rfloor$ and $\lceil k / 2 \rceil$. Using the potential function $\Phi = |len(front) - len(back)|$, each push or pop changes $\Phi$ by at most 1. Rebalancing takes $O(k)$ work and reduces the potential difference from $k$ to at most $1$, releasing $\approx k$ units of potential. Thus, the amortized cost of every operation remains $O(1)$. Because we must use only stack operations (append and pop from end), rebalancing can be performed by popping into a temporary list and splitting elements into `front` and `back` in proper order.

## Algorithm

1. Initialize two internal lists, `_front` and `_back`.
2. `push_front(val)` appends `val` to `_front`.
3. `push_back(val)` appends `val` to `_back`.
4. Define a helper `_rebalance()`: when one stack is empty and the other has $k$ elements, pop all elements from the non-empty stack into a temporary list (which reverses their order). Re-distribute the elements so that half go to `_front` and half go to `_back`, preserving their relative order using only append operations.
5. For `pop_front()`: if `_front` is empty, call `_rebalance()`. If `_front` is still empty (meaning both were empty), return `None`. Otherwise, pop and return from `_front`.
6. For `pop_back()`: if `_back` is empty, call `_rebalance()`. If `_back` is still empty, return `None`. Otherwise, pop and return from `_back`.
7. For `peek_front()` and `peek_back()`: follow the same logic as pop but read the top element without removing it.
8. `__len__()` returns `len(_front) + len(_back)`.

## Complexity Analysis

- **Time:** Amortized $O(1)$ for all operations (`push_front`, `push_back`, `pop_front`, `pop_back`, `peek_front`, `peek_back`). By the potential method with potential $\Phi = ||front| - |back||$, rebalancing costs $O(k)$ but decreases potential by $\Theta(k)$.
- **Space:** $O(N)$ auxiliary space where $N$ is the number of elements currently stored in the deque.

## Edge Cases

- Empty deque on peek or pop: rebalancing does nothing and returns None without raising exceptions.
- Single element deque: rebalancing correctly moves the single element to the requesting side.
- Heavy bias on one side (e.g. only pushing front and popping back): rebalancing divides the elements in half, ensuring each element is rebalanced at most $O(\log N)$ times.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
class TwoStackDeque:
    def __init__(self) -> None:
        """Initialize empty deque backed by two stacks."""
        self._front: list[int] = []
        self._back: list[int] = []

    def push_front(self, val: int) -> None:
        self._front.append(val)

    def push_back(self, val: int) -> None:
        self._back.append(val)

    def _rebalance(self) -> None:
        if not self._front and not self._back:
            return

        source = self._front if self._front else self._back
        from_front = bool(self._front)
        n = len(source)
        half = n // 2

        temp: list[int] = []
        while source:
            temp.append(source.pop())

        # temp now has elements popped from source.
        # If source was front: temp[0] was front top (first deque element),
        # temp[-1] was front bottom (middle of deque).
        # If source was back: temp[0] was back top (last deque element),
        # temp[-1] was back bottom (middle of deque).
        if from_front:
            # Elements that stay in front should end up with temp[0] at top of front.
            # Elements going to back should have temp[-1] near back bottom.
            # The back part corresponds to temp[half:], which must be pushed to back.
            for i in range(half, n):
                self._back.append(temp[i])
            for i in range(half - 1, -1, -1):
                self._front.append(temp[i])
        else:
            # Elements that stay in back should end up with temp[0] at top of back.
            # Elements going to front should have temp[-1] near front bottom.
            for i in range(half, n):
                self._front.append(temp[i])
            for i in range(half - 1, -1, -1):
                self._back.append(temp[i])

    def pop_front(self) -> int | None:
        if not self._front:
            self._rebalance()
        if not self._front:
            return None
        return self._front.pop()

    def pop_back(self) -> int | None:
        if not self._back:
            self._rebalance()
        if not self._back:
            return None
        return self._back.pop()

    def peek_front(self) -> int | None:
        if not self._front:
            self._rebalance()
        if not self._front:
            return None
        return self._front[-1]

    def peek_back(self) -> int | None:
        if not self._back:
            self._rebalance()
        if not self._back:
            return None
        return self._back[-1]

    def __len__(self) -> int:
        return len(self._front) + len(self._back)
```
