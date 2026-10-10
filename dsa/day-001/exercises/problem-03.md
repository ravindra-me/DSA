# Problem 3: Amortized Queue via Stacks

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Amortized time complexity analysis | [Day 1: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

Implement a First-In-First-Out (FIFO) queue using only two standard LIFO stacks (modeled via Python `list` using only `append()` and `pop()`).

The queue must support `push(x)`, `pop()`, `peek()`, and `empty()`.

Analyze and ensure that each operation runs in $O(1)$ amortized time complexity, even though an individual `pop` or `peek` may occasionally take $O(n)$ steps when transferring elements between stacks.

## Input

Method calls on `AmortizedQueue`: `push(val: int)`, `pop() -> int`, `peek() -> int`, `empty() -> bool`

## Output

Values returned by `pop()`, `peek()`, and `empty()` according to FIFO semantics.

## Constraints

- 1 <= x <= 10^6
- At most 10^5 calls will be made across push, pop, peek, and empty.
- Calls to pop and peek are guaranteed to be made only when the queue is non-empty.

## Examples

**Example 1**

```text
Input:  q = AmortizedQueue()
q.push(1)
q.push(2)
q.peek() -> 1
q.pop() -> 1
q.empty() -> False
Output: peek() returns 1, pop() returns 1, empty() returns False
```

Elements maintain FIFO ordering. Moving elements from push_stack to pop_stack occurs lazily.

**Example 2**

```text
Input:  q = AmortizedQueue()
q.empty() -> True
q.push(5)
q.pop() -> 5
q.empty() -> True
Output: empty() -> True, pop() -> 5, empty() -> True
```

Edge case: Queue starts empty, receives one element, and empties completely.

## Function Signature

```python
class AmortizedQueue:
    def __init__(self) -> None:
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def peek(self) -> int:
        pass

    def empty(self) -> bool:
        pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain two stacks: an input stack for pushes and an output stack for pops/peeks. Transfer elements from input to output only when output is empty so each element is moved at most twice.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
