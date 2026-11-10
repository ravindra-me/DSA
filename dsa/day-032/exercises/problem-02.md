# Problem 2: Basic Calculator with Parentheses and Addition/Subtraction

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Expression evaluation with unary minus and dynamic nested state using stack | [Day 32: Stack](../README.md) |

## Problem Statement

Given a string `s` representing a valid mathematical expression containing non-negative integers, `+`, `-`, `(`, `)`, and spaces ` `, evaluate and return the result of the calculation.

Do not use Python's built-in `eval()` function.

## Input

`s: str`

## Output

`int`

## Constraints

- 1 <= len(s) <= 3 * 10^5
- `s` consists of digits, '+', '-', '(', ')', and ' '.

## Examples

**Example 1**

```text
Input:  s = "1 + 1"
Output: 2
```

**Example 2**

```text
Input:  s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

## Function Signature

```python
def calculate_basic_expression(s: str) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Iterate through the string maintaining a running total and sign. Push the total and current sign onto the stack when encountering '(' and pop/combine when encountering ')'. Target O(N) time and O(N) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
