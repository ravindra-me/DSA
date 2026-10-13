# Problem 1: Sum of Array

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Base recursion on linear structures | [Day 4: Recursion](../README.md) |

## Problem Statement

Write a recursive function that returns the sum of all elements in a list of integers.

## Input

A list of integers.

## Output

An integer representing the sum.

## Constraints

- 0 <= len(arr) <= 1000
- List elements are integers.

## Examples

**Example 1**

```text
Input:  [1, 2, 3, 4]
Output: 10
```

1 + 2 + 3 + 4 = 10

**Example 2**

```text
Input:  []
Output: 0
```

Empty list sum is 0.

## Function Signature

```python
def recursive_sum(arr: list[int]) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Define a base case for an empty list (return 0). Otherwise, return the first element plus the result of calling the function recursively on the rest of the list.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
