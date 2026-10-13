# Problem 5: Generate Parentheses

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Backtracking / Combinatorial recursion | [Day 4: Recursion](../README.md) |

## Problem Statement

Given `n`, generate all combinations of well-formed parentheses.

## Input

An integer `n` (number of pairs).

## Output

A list of strings containing all combinations.

## Constraints

- 1 <= n <= 8

## Examples

**Example 1**

```text
Input:  3
Output: ['((()))','(()())','(())()','()(())','()()()']
```

All valid combinations.

**Example 2**

```text
Input:  1
Output: ['()']
```

## Function Signature

```python
def generate_parentheses(n: int) -> list[str]:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use recursion to build strings character by character. Maintain count of 'open' and 'closed' brackets used. You can add an '(' if open < n, and ')' if closed < open.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
