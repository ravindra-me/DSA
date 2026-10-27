# Problem 3: Happy Number

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Cycle detection via a seen-before state set | [Day 18: HashSet](../README.md) |

## Problem Statement

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return `True` if `n` is a happy number, and `False` if not.

## Input

`n: int` - a positive integer.

## Output

`bool` - `True` if `n` is happy, `False` otherwise.

## Constraints

- 1 <= n <= 2^31 - 1

## Examples

**Example 1**

```text
Input:  n = 19
Output: True
```

1^2 + 9^2 = 82; 8^2 + 2^2 = 68; 6^2 + 8^2 = 100; 1^2 + 0^2 + 0^2 = 1.

**Example 2**

```text
Input:  n = 2
Output: False
```

2 leads to 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (cycle detected).

**Example 3**

```text
Input:  n = 1
Output: True
```

1 is already 1.

## Function Signature

```python
def is_happy(n: int) -> bool:
    """Return True if n is a happy number, False otherwise."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Compute the sum of squared digits iteratively. Store visited values in a set to identify cycle repetition.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
