# Problem 5: Parse and Evaluate Boolean Expressions

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Complex multi-branch recursive AST evaluation | [Day 17: Recursion](../README.md) |

## Problem Statement

A boolean expression is given as a string `expression`, consisting of the following characters:
- `'t'`: Evaluates to `True`.
- `'f'`: Evaluates to `False`.
- `'!(subExpr)'`: Evaluates to the logical NOT of the inner expression.
- `'&(subExpr1, subExpr2, ..., subExprN)'`: Evaluates to the logical AND of 2 or more inner sub-expressions.
- `'|(subExpr1, subExpr2, ..., subExprN)'`: Evaluates to the logical OR of 2 or more inner sub-expressions.

Return the result of evaluating the given expression as a Python `bool`.

You must implement a purely recursive parser that handles arbitrary nesting of expressions.

## Input

`expression`: A valid string containing only characters `t`, `f`, `!`, `&`, `|`, `(`, `)`, and `,`.

## Output

A boolean (`True` or `False`) representing the evaluated result.

## Constraints

- 1 <= len(expression) <= 2 * 10^4
- `expression` is guaranteed to be syntactically valid according to the grammar.

## Examples

**Example 1**

```text
Input:  expression = "&(|(f))"
Output: False
```

|(f) is False, &(False) is False.

**Example 2**

```text
Input:  expression = "|(f,f,f,t)"
Output: True
```

Logical OR of [False, False, False, True] is True.

**Example 3**

```text
Input:  expression = "!(&(f,t))"
Output: True
```

&(False, True) is False. !(False) is True.

## Function Signature

```python
def parse_bool_expr(expression: str) -> bool:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Parse recursively using pointer movement or recursive decomposition: identify the operator, skip the opening parenthesis, parse comma-separated sub-expressions recursively until the matching closing parenthesis, then apply the logical operator.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
