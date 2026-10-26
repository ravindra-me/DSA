# Solution 5: Parse and Evaluate Boolean Expressions

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Complex multi-branch recursive AST evaluation

## Approach

We can parse and evaluate the boolean expression recursively by tracking the current index as we traverse the string. Simple expressions `'t'` and `'f'` evaluate directly to `True` and `False`. Operator expressions `!`, `&`, and `|` consume their enclosed sub-expressions (delimited by commas and matching parentheses) and recursively combine their evaluated boolean values.

## Thought Process

The grammar of the expression forms a tree structure (Abstract Syntax Tree). Since the string is guaranteed to be syntactically valid, a recursive descent approach naturally matches the structure of nested operations. By advancing a pointer through the string, whenever we encounter an operator (`!`, `&`, `|`), we skip the opening parenthesis, recursively evaluate all comma-separated sub-expressions until reaching the matching closing parenthesis, and then apply the boolean operator.

## Algorithm

1. Maintain an index `i` representing the current position in the expression string.
2. Define a recursive helper function `parse()` that evaluates and returns the boolean result of the sub-expression starting at index `i`.
3. If `expression[i]` is `'t'` or `'f'`, increment `i` and return `True` or `False` respectively.
4. Otherwise, `expression[i]` is an operator (`!`, `&`, or `|`). Record the operator and advance `i` past the operator and its immediate opening parenthesis `'('`.
5. Recursively parse inner sub-expressions in a loop: call `parse()`, append the result to a list of sub-results, and check the character at index `i`. If it is a comma `','`, advance `i` and parse the next sub-expression.
6. When encountering the closing parenthesis `')'`, advance `i` past it.
7. Apply the recorded operator to the gathered sub-results (`not` for `!`, `all` for `&`, `any` for `|`) and return the resulting boolean.

## Complexity Analysis

- **Time:** O(N) where N is the length of the string, because every character is processed a constant number of times.
- **Space:** O(N) due to the call stack depth and memory allocated for sub-expression evaluation lists in deeply nested expressions.

## Edge Cases

- Single literal expressions like 't' or 'f' are handled at the base case without processing operators.
- Deeply nested operators like '!(!(!(...)))' are handled within the call stack limit.
- Multi-operand expressions with varying number of operands are handled by loop termination on ')'.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
import sys

sys.setrecursionlimit(30000)

def parse_bool_expr(expression: str) -> bool:
    """Parses and evaluates a boolean expression string recursively."""
    i = 0
    
    def parse() -> bool:
        nonlocal i
        char = expression[i]
        i += 1
        
        if char == 't':
            return True
        if char == 'f':
            return False
            
        op = char
        i += 1  # Skip '(' 
        
        children = []
        while True:
            children.append(parse())
            if expression[i] == ')':
                i += 1  # Skip ')'
                break
            elif expression[i] == ',':
                i += 1  # Skip ','
                
        if op == '!':
            return not children[0]
        elif op == '&':
            return all(children)
        else:  # op == '|'
            return any(children)
            
    return parse()
```
