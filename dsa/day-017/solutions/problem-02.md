# Solution 2: Reverse a Stack Using Pure Recursion

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Medium | **Concept:** Auxiliary stack frame state preservation without loops or external collections

## Approach

To reverse a stack using only recursion and without external data structures or loops, we use the call stack to hold elements. The reversal decomposes into two recursive functions: `reverse_stack`, which pops the top element, recursively reverses the remaining stack, and inserts the popped element at the bottom; and `insert_at_bottom`, which recursively empties the stack until base case, pushes the target element, and then restores the previously popped items on unwind.

## Thought Process

When loop constructs and auxiliary data structures are forbidden, the execution call stack is the only place we can temporarily preserve state.

Consider the top element `top = stack.pop()`. If we assume `reverse_stack(stack)` correctly reverses the remaining `n - 1` elements, our problem reduces to placing `top` at the very bottom of the reversed stack. Normal stack operations (`append`) place elements at the top, not the bottom.

To place an element at the bottom using only recursion, we can define a second recursive helper `insert_at_bottom(stack, item)`: pop an element, recursively call `insert_at_bottom(stack, item)` on the smaller stack until the stack is empty, push `item` onto the now-empty stack, and push back the popped elements as the recursion unwinds.

Since `insert_at_bottom` takes $O(k)$ steps for a stack of size $k$, calling it for each element from $n$ down to $1$ results in an overall time complexity of $O(n^2)$ and auxiliary space of $O(n)$ call frames.

## Algorithm

1. Define a recursive helper `insert_at_bottom(stack, item)`.
2. Inside `insert_at_bottom`: if `stack` is empty, `stack.append(item)` and return.
3. Otherwise, pop `temp = stack.pop()`, recursively call `insert_at_bottom(stack, item)`, and then `stack.append(temp)`.
4. Inside `reverse_stack(stack)`: if `stack` is empty, return.
5. Otherwise, pop `top = stack.pop()`.
6. Recursively call `reverse_stack(stack)` to reverse the rest of the stack.
7. Call `insert_at_bottom(stack, top)` to place `top` at the bottom of the reversed stack.

## Complexity Analysis

- **Time:** O(n^2), where n is the number of elements in the stack. Each insertion at the bottom takes O(k) time on a stack of size k, summing to 1 + 2 + ... + n = O(n^2).
- **Space:** O(n) auxiliary space on the call stack due to recursion depth reaching at most n.

## Edge Cases

- Empty stack (len == 0): Base case triggers immediately, leaves stack empty.
- Single element stack (len == 1): Element popped, recursive call on empty stack returns, element re-inserted at bottom (which is also top).
- Duplicate elements: Handled naturally; order of identical elements is inverted identically without corruption.
- Negative numbers and zero: Handled transparently as Python integers are treated uniformly.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def _insert_at_bottom(stack: list[int], item: int) -> None:
    """Recursively insert an element at the bottom of the stack."""
    if not stack:
        stack.append(item)
        return
    top = stack.pop()
    _insert_at_bottom(stack, item)
    stack.append(top)


def reverse_stack(stack: list[int]) -> None:
    """Reverse a stack in-place using only recursion."""
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    _insert_at_bottom(stack, top)
```
