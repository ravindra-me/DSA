# Problem 4: Design Min-Stack with Constant Time Minimum

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Auxiliary stack invariant for auxiliary queries | [Day 10: Stack](../README.md) |

## Problem Statement

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant $O(1)$ time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `push(val: int) -> None`: Pushes the element `val` onto the stack.
- `pop() -> None`: Removes the element on the top of the stack.
- `top() -> int`: Gets the top element of the stack. Guaranteed called on non-empty stack.
- `get_min() -> int`: Retrieves the minimum element in the stack. Guaranteed called on non-empty stack.

## Input

Method invocations on `MinStack` instance.

## Output

`top()` and `get_min()` return `int`. `push` and `pop` return `None`.

## Constraints

- -2^31 <= val <= 2^31 - 1
- Methods pop, top and get_min will always be called on non-empty stacks in tests.
- At most 3 * 10^4 calls will be made across all methods.

## Examples

**Example 1**

```text
Input:  ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
ms.get_min() -> -3
ms.pop()
ms.top() -> 0
ms.get_min() -> -2
Output: [-3, 0, -2]
```

After popping -3, the previous minimum -2 is restored.

**Example 2**

```text
Input:  ms = MinStack()
ms.push(5)
ms.get_min() -> 5
ms.top() -> 5
Output: [5, 5]
```

Single element is both top and min.

## Function Signature

```python
class MinStack:
    def __init__(self) -> None:
        """Initialize the stack."""
        pass

    def push(self, val: int) -> None:
        """Push element val onto stack."""
        pass

    def pop(self) -> None:
        """Remove the top element."""
        pass

    def top(self) -> int:
        """Return the top element."""
        pass

    def get_min(self) -> int:
        """Retrieve the minimum element in the stack."""
        pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Pair each pushed value with the current minimum at that depth, or maintain a secondary stack that tracks running minimums. All operations must run in strictly O(1) time and O(n) total space.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
