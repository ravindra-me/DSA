# Solution 2: Basic Calculator with Parentheses and Addition/Subtraction

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Medium | **Concept:** Expression evaluation with unary minus and dynamic nested state using stack

## Approach

We can evaluate the expression in a single linear scan using a stack to handle parentheses. We track the `current_sum`, the current `sign` (+1 or -1), and build numbers digit-by-digit. When encountering `(`, we push `current_sum` and `sign` onto the stack and reset them for the inner context. When encountering `)`, we pop the previous sign and previous sum to combine the inner result with the outer context.

## Thought Process

A naive approach might use recursion or build a full Expression Syntax Tree (AST), which overheads memory and can hit recursion limits on deeply nested parentheses (up to 300,000 characters). Since operations are limited to addition and subtraction (which have equal precedence and are left-associative), we don't need a multi-pass shunting-yard algorithm. Instead, we can maintain the running sum and sign. Parentheses simply freeze the outer accumulator and sign onto a stack, allowing us to compute the sub-expression independently, and then fold it back into the running sum upon closing.

## Algorithm

1. Initialize `res = 0`, `sign = 1`, `num = 0`, and an empty stack `stack = []`.
2. Iterate through each character `char` in the string `s`:
3. If `char` is a digit, update `num = num * 10 + int(char)`.
4. If `char` is '+' or '-', add `sign * num` to `res`, set `num = 0`, and update `sign` to +1 or -1 accordingly.
5. If `char` is '(', push `res` and then `sign` onto `stack`. Reset `res = 0` and `sign = 1` for the enclosed expression.
6. If `char` is ')', add `sign * num` to `res`, set `num = 0`. Pop the saved sign from `stack` and multiply `res` by it, then pop the saved outer result and add it to `res`.
7. After the loop, add any remaining `sign * num` to `res` and return `res`.

## Complexity Analysis

- **Time:** O(N) where N is the length of string `s`, as we traverse the string once.
- **Space:** O(N) in the worst case where expressions are deeply nested like `(((...)))`, requiring stack depth proportional to N.

## Edge Cases

- Spaces in expression: skipped automatically as non-digits and non-operators.
- Unary operators / leading signs like `- (3 + 2)` or `+ 5`: handled naturally by initializing `res` to 0 and updating `sign` when encountering operators before numbers.
- Deeply nested parentheses: stack handles up to maximum string length bounds within memory limits without stack overflow from recursion.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def calculate_basic_expression(s: str) -> int:
    """Evaluate a basic expression string containing digits, '+', '-', '(', ')', and spaces."""
    stack = []
    res = 0
    num = 0
    sign = 1
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            res += sign * num
            num = 0
            sign = 1
        elif char == '-':
            res += sign * num
            num = 0
            sign = -1
        elif char == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif char == ')':
            res += sign * num
            num = 0
            prev_sign = stack.pop()
            prev_res = stack.pop()
            res = prev_res + prev_sign * res
            
    res += sign * num
    return res
```
