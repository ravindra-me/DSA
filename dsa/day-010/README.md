# Day 10: Day 10: Stacks — Intuition, Mechanics, and Core Patterns

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 10 | 2026-10-19 | Linear Data Structures | New topic | progressive | Python 3.12 |

The stack is one of the most fundamental data structures in computer science, modeling the principle of Last-In, First-Out (LIFO). Whenever a problem involves nested structures, backtracking to the most recent context, or reversing an order of operations, a stack is almost always the key. Today we cover how stacks operate under the hood, how to build them via dynamic arrays or linked lists, and how to apply them to parsing, matching, and evaluation problems.

## Topic

**Stack**: LIFO, balanced parentheses, expression evaluation, undo history, stack via array/list

## Learning Objectives

By the end of this lesson you should be able to:

- Understand the Last-In, First-Out (LIFO) property and identify problems with nested or deferred dependencies.
- Implement a stack with O(1) push, pop, and peek using dynamic arrays or linked lists.
- Solve bracket matching and balance verification problems using stack invariants.
- Evaluate postfix (Reverse Polish Notation) expressions and manage undo/redo state histories.
- Recognize when a monotonic stack or auxiliary tracking stack is required for optimization.

## Concept Explanation

### What it is

A stack is a linear collection of elements with a restricted interface: elements can only be added to or removed from one end, traditionally called the **top**. Think of a physical stack of cafeteria trays or a deck of cards: you place a new item on the top, and you take items off the top. The most recently added element is the first one removed. This behavior is formally referred to as **LIFO** (Last-In, First-Out).

### Why it exists

Without stacks, handling nested structures or restoring recent states requires complex manual indexing and state tracking. For example, when evaluating mathematical expressions with parentheses, you cannot compute outer operations until the innermost expressions finish. When a function calls another function in code, the runtime must pause the caller, execute the callee, and resume the caller right where it left off. Stacks provide an elegant, zero-overhead mechanism to pause, descend into a sub-problem, and resume the exact previous context once the sub-problem finishes.

### When to use it

Look for these problem cues:
- **Matching pairs with nesting**: e.g., matching parentheses, brackets, or HTML/XML tags.
- **Undo/Redo operations**: returning to the immediately preceding state.
- **Deferred processing**: an element cannot be processed until subsequent elements are inspected or resolved (e.g., operator precedence in math expressions).
- **Reversal**: inspecting or outputting elements in reverse order of discovery.
- **Monotonic properties**: finding the 'next greater' or 'previous smaller' element in an array.

### When NOT to use it

Avoid using a stack when:
- You need to access elements at arbitrary indices in $O(1)$ time (use an array/hash map).
- You need to process items in the order they arrived (FIFO) — use a Queue instead.
- You frequently insert or remove elements from both ends or from the middle — use a deque or linked list.

### How it works internally

A stack supports three primary operations, all operating in $O(1)$ time:
1. **push(x)**: Place element `x` onto the top.
2. **pop()**: Remove and return the top element. An error/underflow occurs if empty.
3. **peek()** (or `top()`): Inspect the top element without removing it.

In Python, a standard `list` functions as an amortized $O(1)$ stack using `append()` for push and `pop()` for pop. Alternatively, a singly linked list can implement a stack by maintaining a `head` pointer: push is prepending a new node (`new_node.next = head; head = new_node`), and pop is advancing the head (`head = head.next`). Both methods ensure strictly $O(1)$ operations.

### Common mistakes

- Popping or peeking from an empty stack without checking `if not stack:`, causing `IndexError`.
- Using `list.pop(0)` or `list.insert(0, x)` in Python instead of `append()` and `pop()`, which degrades time complexity from $O(1)$ to $O(n)$ due to shifting elements.
- Failing to check whether the stack is empty at the end of a bracket validation algorithm (e.g., input `'((('` leaves unclosed brackets).
- Confusing FIFO (Queue) and LIFO (Stack) when designing history tracking or simulation logic.

### Real-world applications

- Call Stack in language runtimes (managing function frames, local variables, and recursion).
- Browser Navigation History (Back button pushes/pops visited URLs).
- Undo/Redo buffers in text editors like VS Code and graphic design tools.
- Syntax parsing and AST (Abstract Syntax Tree) generation in compilers.

## Example

### Validating Balanced Parentheses
Consider the string `s = "{[()]}"`.

1. Initialize empty stack `st = []`.
2. Character `'{'`: It is an opening bracket. `st.append('{')` -> `['{']`
3. Character `'['`: Opening bracket. `st.append('[')` -> `['{', '[']`
4. Character `'('`: Opening bracket. `st.append('(')` -> `['{', '[', '(']`
5. Character `')'`: Closing bracket. Peek top: `'('`. Matches `')'`. Pop `'('` -> `['{', '[']`
6. Character `']'`: Closing bracket. Peek top: `'['`. Matches `']'`. Pop `'['` -> `['{']`
7. Character `'}'`: Closing bracket. Peek top: `'{'`. Matches `'}'`. Pop `'{'` -> `[]`
8. String iteration finished. Stack is empty -> Return `True`.

Now consider `s = "([)]"`:
- Push `'('`, push `'['`. Stack is `['(', '[']`.
- Next is `')'`. Top is `'['`, which does not match `')'`. Immediately return `False`.

## Visual Explanation

```text
Push 'A', Push 'B', Pop, Push 'C':

  1. Push 'A'      2. Push 'B'       3. Pop -> 'B'     4. Push 'C'
  +---------+      +---------+      +---------+      +---------+
                   |    B    | <--Top                |    C    | <--Top
  +---------+      +---------+      +---------+      +---------+
  |    A    | <--Top |  A    |      |    A    | <--Top|    A    |
  +---------+      +---------+      +---------+      +---------+
  | (bottom)|      | (bottom)|      | (bottom)|      | (bottom)|
```

## Complexity

- **Time Complexity:** push: O(1) amortized (Python list) or strictly O(1) (linked list node prepend); pop: O(1); peek: O(1); is_empty: O(1).
- **Space Complexity:** O(n) auxiliary space to store n elements.

Python's dynamic array (`list`) reallocates with geometric growth factor ~1.125x to amortize append costs to $O(1)$. When absolute worst-case latency matters (e.g. real-time embedded systems), a linked-list-based stack guarantees non-amortized $O(1)$ push at the cost of pointer overhead.

## Interview Perspective

1. **How would you implement a stack with an O(1) get_min() operation?**
   <details><summary>What a strong answer covers</summary>

   Maintain an auxiliary stack alongside the main stack (or store tuples `(val, current_min)`). Whenever pushing, push the value to the main stack and `min(val, current_min)` to the min-stack. On pop, pop from both.

   </details>
2. **What is the difference between implementing a stack using a dynamic array vs. a singly linked list?**
   <details><summary>What a strong answer covers</summary>

   A dynamic array offers better cache locality and less memory per element, but suffers from occasional $O(n)$ resize pauses (amortized $O(1)$). A linked list offers guaranteed $O(1)$ per operation without resize spikes, but has higher memory overhead per node due to pointers and poor cache locality.

   </details>
3. **Why does recursion use a stack, and what causes a 'stack overflow'?**
   <details><summary>What a strong answer covers</summary>

   Each recursive call pushes an execution frame containing local variables and return address onto the runtime call stack. Deep recursion exceeding the pre-allocated stack memory limit triggers a stack overflow.

   </details>
4. **Can you implement a queue using two stacks?**
   <details><summary>What a strong answer covers</summary>

   Yes. Use an `in_stack` for enqueue and an `out_stack` for dequeue. When `out_stack` is empty, pop all elements from `in_stack` and push them to `out_stack`, reversing their order to FIFO. This achieves amortized $O(1)$ time per operation.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Valid Parentheses and Brackets](exercises/problem-01.md) | Easy | Bracket matching using LIFO stack invariant | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Evaluate Reverse Polish Notation](exercises/problem-02.md) | Easy/Medium | Postfix expression evaluation with stack | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Text Editor with Undo History](exercises/problem-03.md) | Medium | State restoration and history management via dual stacks | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Design Min-Stack with Constant Time Minimum](exercises/problem-04.md) | Medium/Hard | Auxiliary stack invariant for auxiliary queries | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Decode String with Nested Multipliers](exercises/problem-05.md) | Hard | Nested context resolution with dual stacks | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-010
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: LIFO (Last-In, First-Out), Stack operations (push, pop, peek), Bracket / Parentheses matching, Reverse Polish Notation (RPN), Undo / State history tracking, Min Stack auxiliary tracking*
