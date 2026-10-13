# Problem 2: Power Function

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Divide and conquer (Exponentiation) | [Day 4: Recursion](../README.md) |

## Problem Statement

Implement a function `power(base, exp)` that calculates `base` raised to `exp` efficiently. You should reduce the problem size by half in each step (O(log N)).

## Input

An integer base and a non-negative integer exp.

## Output

An integer representing the result.

## Constraints

- 0 <= exp <= 1000
- -100 <= base <= 100

## Examples

**Example 1**

```text
Input:  base=2, exp=10
Output: 1024
```

2^10 = 1024

**Example 2**

```text
Input:  base=5, exp=0
Output: 1
```

Any number to the power of 0 is 1.

## Function Signature

```python
def power(base: int, exp: int) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

If exp is 0, return 1. If exp is even, compute `half = power(base, exp // 2)` and return `half * half`. If odd, return `base * power(base, exp - 1)`.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
