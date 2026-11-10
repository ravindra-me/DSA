# Problem 1: Validate Stack Sequences

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Simulation of LIFO Stack push and pop operations | [Day 32: Stack](../README.md) |

## Problem Statement

Given two integer arrays `pushed` and `popped` each with distinct values, return `True` if this could have been the result of a sequence of push and pop operations on an initially empty stack, or `False` otherwise.

## Input

`pushed: list[int]`, `popped: list[int]`

## Output

`bool`

## Constraints

- 1 <= len(pushed) <= 1000
- len(popped) == len(pushed)
- All elements in pushed and popped are distinct.

## Examples

**Example 1**

```text
Input:  pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
Output: True
```

Push 1, 2, 3, 4, pop 4, push 5, pop 5, pop 3, pop 2, pop 1.

**Example 2**

```text
Input:  pushed = [1, 2, 3, 4, 5], popped = [4, 3, 5, 1, 2]
Output: False
```

1 cannot be popped before 2.

## Function Signature

```python
def validate_stack_sequences(pushed: list[int], popped: list[int]) -> bool:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Simulate the push sequence element by element. After each push, greedily pop from the stack while the top of the stack matches the current element in popped. Target O(N) time and O(N) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
