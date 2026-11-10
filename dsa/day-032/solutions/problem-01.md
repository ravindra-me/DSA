# Solution 1: Validate Stack Sequences

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy/Medium | **Concept:** Simulation of LIFO Stack push and pop operations

## Approach

We simulate the push and pop operations using an explicit stack while consuming the `pushed` array item by item. After pushing each element, we greedily pop from our stack as long as the stack's top element matches the next element needed in `popped`.

## Thought Process

A stack operates on a strict Last-In, First-Out (LIFO) discipline. When simulating, we must push elements in the exact sequence given by `pushed`. However, whenever the element at the top of our stack matches the current target element in `popped`, we are forced to pop it immediately if we want `popped` to match, because pushing more elements would bury this matching top element. By applying this greedy strategy (pushing each element and immediately popping whenever possible), we can determine if the entire `popped` sequence can be matched. If the stack is empty at the end (or all `popped` elements are matched), the sequence is valid.

## Algorithm

1. Initialize an empty list `stack` to simulate stack operations and an integer `i = 0` to track the current index in `popped`.
2. Iterate through each element `val` in `pushed`:
3. Push `val` onto `stack`.
4. While `stack` is not empty and `stack[-1]` equals `popped[i]`:
5. Pop the top element from `stack`.
6. Increment `i` by 1.
7. Return `True` if `i == len(popped)` (or equivalently `not stack`), else `False`.

## Complexity Analysis

- **Time:** O(N) where N is the length of `pushed` (and `popped`). Each element is pushed onto the stack exactly once and popped from the stack at most once, performing O(1) work per push/pop.
- **Space:** O(N) auxiliary space to store the stack elements.

## Edge Cases

- Single element array: The push and immediate pop logic correctly handles len == 1.
- All pops deferred until all pushes complete (e.g., [1, 2, 3] -> [3, 2, 1]): Handled seamlessly as stack pops completely after full push.
- Interleaved push/pop sequences: Handled by greedy inner while-loop.
- Invalid sequences where order breaks (e.g., example 2): Loop finishes leaving non-empty stack, correctly returning False.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def validate_stack_sequences(pushed: list[int], popped: list[int]) -> bool:
    """Validate if popped sequence could result from push/pop operations on pushed sequence."""
    stack = []
    pop_idx = 0
    
    for val in pushed:
        stack.append(val)
        while stack and pop_idx < len(popped) and stack[-1] == popped[pop_idx]:
            stack.pop()
            pop_idx += 1
            
    return pop_idx == len(popped)
```
