# Problem 4: Maximum Frequency Stack

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Frequency mapping combined with bucketed stacks | [Day 32: Stack](../README.md) |

## Problem Statement

Design a stack-like data structure that pushes elements and pops the element with the highest frequency.

Implement the `FreqStack` class:
- `FreqStack()` initializes the object with an empty stack.
- `void push(int val)` pushes an integer `val` onto the stack.
- `int pop()` removes and returns the most frequent element in the stack. If there is a tie for the most frequent element, the element closest to the top of the stack (i.e. pushed most recently) is popped.

## Input

Class method invocations with integer arguments.

## Output

`pop()` returns integer.

## Constraints

- 0 <= val <= 10^9
- At most 2 * 10^4 calls will be made to push and pop.
- It is guaranteed that pop will not be called on an empty stack.

## Examples

**Example 1**

```text
Input:  push(5), push(7), push(5), push(7), push(4), push(5), pop(), pop(), pop(), pop()
Output: 5, 7, 5, 4
```

Frequencies: 5 -> 3, 7 -> 2, 4 -> 1. Max freq is 3. Pop returns 5. Max freq becomes 2. Pop returns 7 (pushed after 5). Pop returns 5. Pop returns 4.

**Example 2**

```text
Input:  push(1), push(1), push(2), pop(), pop()
Output: 1, 1
```

1 is popped twice.

## Function Signature

```python
class FreqStack:
    def __init__(self):
        pass
    def push(self, val: int) -> None:
        pass
    def pop(self) -> int:
        pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a frequency hash map (`val -> freq`) and a map of frequency to stacks (`freq -> list[int]`). Also track the global `max_freq`. Target O(1) per push and pop.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
