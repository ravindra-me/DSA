# Solution 2: Evaluate Reverse Polish Notation

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Postfix expression evaluation with stack

## Approach

Iterate through the tokens while maintaining a stack of operands. Push integer values onto the stack. When an operator is encountered, pop the top two operands (the first popped is the right operand, the second is the left operand), apply the operation, truncate division toward zero using `int(a / b)`, and push the result back onto the stack. The final remaining element in the stack is the answer.

## Thought Process

In postfix notation, operators follow their operands, which removes the need for parentheses or operator precedence rules. A natural way to evaluate postfix expressions is by scanning left to right. When an operator appears, it acts on the two most recently seen operands. A Last-In-First-Out (LIFO) stack precisely mirrors this evaluation order: numbers are pushed as they arrive, and binary operators consume the two topmost numbers and replace them with their result.

A naive approach might involve scanning the list repeatedly to find adjacent operand-operand-operator patterns and replacing them in-place, which takes $O(N^2)$ time due to array shiftings. A stack-based approach evaluates each token in $O(1)$ time, yielding an optimal $O(N)$ solution.

A key detail in Python is integer division: `//` performs floor division (rounding toward negative infinity, e.g., `6 // -132 == -1`), whereas the problem specifies truncation toward zero (e.g., `int(6 / -132) == 0`). Using `int(a / b)` correctly truncates toward zero.

## Algorithm

1. Initialize an empty stack `stack`.
2. For each token in `tokens`:
3. If the token is an operator (`'+'`, `'-'`, `'*'`, `'/'`):
4. Pop the right operand `b = stack.pop()`.
5. Pop the left operand `a = stack.pop()`.
6. Apply the operator: addition `a + b`, subtraction `a - b`, multiplication `a * b`, or truncated division `int(a / b)`.
7. Push the resulting value onto `stack`.
8. Else (the token is an integer string): convert to `int` and push onto `stack`.
9. Return `stack[0]` as the final result.

## Complexity Analysis

- **Time:** O(N) where N is the number of tokens. Each token is pushed and popped at most once, and each arithmetic operation runs in O(1) time.
- **Space:** O(N) to store the operands on the stack in the worst case (e.g., when all numbers precede all operators).

## Edge Cases

- Single element: e.g., tokens = ['42']. No operators are processed; the single number is pushed and returned.
- Negative numbers and truncation: Python's `//` rounds toward -infinity, so `int(a / b)` must be used to truncate toward 0 (e.g., -1 // 2 is -1, but int(-1 / 2) is 0).
- Subtraction order: the first popped item is the subtrahend (`b`) and the second is the minuend (`a`).

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def eval_rpn(tokens: list[str]) -> int:
    """Evaluate Reverse Polish Notation tokens and return the integer result."""
    stack: list[int] = []
    for token in tokens:
        if token == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif token == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif token == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif token == "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]
```
