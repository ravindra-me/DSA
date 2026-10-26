# Problem 2: Reverse a Stack Using Pure Recursion

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Auxiliary stack frame state preservation without loops or external collections | [Day 17: Recursion](../README.md) |

## Problem Statement

Given a Python list representing a stack `stack` (where the end of the list is the top of the stack), reverse the elements of the stack in-place using **only recursion**.

You are **not** allowed to use any loop constructs (`for`, `while`, list comprehensions), nor are you allowed to use auxiliary data structures (no additional lists, dicts, or deques). You may only use recursion and standard `stack.pop()` and `stack.append()` operations.

## Input

`stack`: A `list[int]` acting as a stack.

## Output

Modify `stack` in-place so that its order is reversed. Returns `None`.

## Constraints

- 0 <= len(stack) <= 100
- -10^4 <= stack[i] <= 10^4
- No iterative loops (while/for) or helper data structures allowed.

## Examples

**Example 1**

```text
Input:  stack = [1, 2, 3, 4, 5] (top is 5)
Output: [5, 4, 3, 2, 1] (top is 1)
```

The entire stack order is inverted in-place.

**Example 2**

```text
Input:  stack = []
Output: []
```

An empty stack remains empty.

## Function Signature

```python
def reverse_stack(stack: list[int]) -> None:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use two recursive functions: one to pop all elements until the stack is empty, and a helper recursive function `insert_at_bottom` to insert each popped element at the very bottom of the stack without loops.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
