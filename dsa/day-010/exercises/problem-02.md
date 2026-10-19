# Problem 2: Evaluate Reverse Polish Notation

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Postfix expression evaluation with stack | [Day 10: Stack](../README.md) |

## Problem Statement

You are given an array of strings `tokens` that represents an arithmetic expression in Reverse Polish Notation (postfix notation).

Evaluate the expression and return an integer representing its value.

Valid operators are `'+'`, `'-'`, `'*'`, and `'/'`. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero (standard integer truncation in Python: e.g., `int(a / b)`).

## Input

`tokens: list[str]` where each token is an operator `"+"`, `"-"`, `"*"`, `"/"` or an integer string representing an integer in the range `[-200, 200]`.

## Output

`int`: The evaluated result.

## Constraints

- 1 <= len(tokens) <= 10^4
- tokens[i] is either an operator or an integer string in range [-200, 200]
- The given RPN expression is always valid and will never divide by zero.

## Examples

**Example 1**

```text
Input:  tokens = ["2", "1", "+", "3", "*"]
Output: 9
```

((2 + 1) * 3) = 9

**Example 2**

```text
Input:  tokens = ["4", "13", "5", "/", "+"]
Output: 6
```

(4 + (13 / 5)) = 4 + 2 = 6

**Example 3**

```text
Input:  tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
```

Full evaluation evaluates to 22.

## Function Signature

```python
def eval_rpn(tokens: list[str]) -> int:
    """Evaluate Reverse Polish Notation tokens and return the integer result."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Iterate through tokens. When a number is encountered, push it to the stack. When an operator is encountered, pop the right operand then the left operand, apply the operator, and push the result back. Be careful with truncation toward zero on division (e.g. int(b / a)). Target O(n) time and O(n) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
