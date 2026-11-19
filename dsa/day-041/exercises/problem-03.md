# Problem 3: Amortized Two-Stack Deque

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Potential method and amortized O(1) multi-operation structures | [Day 41: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

Implement a double-ended queue (deque) `TwoStackDeque` using exactly two Python lists acting strictly as LIFO stacks (i.e. only `append()` and `pop()` are permitted on the internal stacks). Your implementation must support `push_front`, `push_back`, `pop_front`, `pop_back`, `peek_front`, and `peek_back`.

All operations must run in $O(1)$ amortized time. If `pop_front`, `pop_back`, `peek_front`, or `peek_back` is invoked on an empty deque, return `None`.

## Input

A sequence of method calls to `TwoStackDeque`.

## Output

Values returned by pop and peek calls.

## Constraints

- Up to 2 * 10^5 total method calls.
- Internal storage must only manipulate two lists via LIFO operations (append and pop from end).

## Examples

**Example 1**

```text
Input:  deque = TwoStackDeque()
deque.push_back(1)
deque.push_back(2)
deque.push_front(0)
deque.peek_front()
deque.pop_back()
deque.pop_front()
Output: 0, then 2, then 0
```

State transitions: [] -> [1] -> [1, 2] -> [0, 1, 2]. peek_front() = 0. pop_back() removes 2. pop_front() removes 0.

**Example 2**

```text
Input:  deque = TwoStackDeque()
deque.pop_front()
Output: None
```

Popping from an empty deque returns None.

## Function Signature

```python
class TwoStackDeque:
    def __init__(self) -> None:
        """Initialize empty deque backed by two stacks."""
        pass

    def push_front(self, val: int) -> None:
        pass

    def push_back(self, val: int) -> None:
        pass

    def pop_front(self) -> int | None:
        pass

    def pop_back(self) -> int | None:
        pass

    def peek_front(self) -> int | None:
        pass

    def peek_back(self) -> int | None:
        pass

    def __len__(self) -> int:
        pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Balance elements between a front-stack and back-stack, redistributing half the elements when either stack becomes empty during a pop/peek.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
