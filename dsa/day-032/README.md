# Day 32: Day 32: Stack Revision & Advanced Patterns

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 32 | 2026-11-10 | Linear Data Structures | Revision (stage 2) | progressive | Python 3.12 |

> **Revision day.** You first studied this topic earlier; today recaps the essentials and gives you brand-new problems. (spaced revision due on day 17 of 'stack' (learned on day 10))

Welcome to Stage 2 Revision for the Stack data structure. A stack operates under the Last-In, First-Out (LIFO) discipline, making it the primary tool for nested context tracking, expression processing, and state restoration. Today we review core stack mechanics and dive into more complex interview challenges combining stacks with hashing, binary search, and mathematical evaluation.

## Topic

**Stack**: LIFO, balanced parentheses, expression evaluation, undo history, stack via array/list

## Learning Objectives

By the end of this lesson you should be able to:

- Master state restoration and nested tracking using LIFO semantics.
- Evaluate complex nested string expressions and algebraic structures using explicit stacks.
- Solve interview-grade problems combining stacks with hash maps, frequency tables, and string manipulation.
- Recognize when an implicit recursive call stack should be converted to an explicit stack to prevent stack overflow.

## Concept Explanation

### What it is

A stack is a linear data structure that adheres to the Last-In, First-Out (LIFO) principle. Elements added most recently are the first to be retrieved or removed. Think of a stack of plates: you place new plates on top and take plates off the top.

### Why it exists

Without a stack, managing nested structures (like matching brackets, nested function calls, or deeply nested HTML/JSON tags) requires manual, error-prone index tracking. Stacks naturally model hierarchical nesting and deferred execution by preserving context until inner operations complete.

### When to use it

Use a stack when:
- The problem involves nested structures, parentheses matching, or scope resolution.
- You need to process sequences in reverse or track dynamic history for undo operations.
- You are evaluating expressions (infix, prefix, postfix).
- You need to convert a recursive depth-first algorithm into an iterative algorithm.

### When NOT to use it

Do not use a stack when:
- You need First-In, First-Out (FIFO) processing order (use a queue/deque instead).
- You need random access to elements by index in $O(1)$ time (use a standard array/dynamic array).
- You need order statistics or fast lookup of arbitrary elements (use a balance search tree or hash table).

### How it works internally

A dynamic array (like Python's `list`) serves as the standard stack implementation.
- `push(item)`: Appends an item to the end of the list in amortized $O(1)$ time.
- `pop()`: Removes and returns the last element in $O(1)$ time.
- `peek()` / `top()`: Inspects the element at index `-1` in $O(1)$ time without modifying the list.
Invariant: The top of the stack always represents the most immediate, unclosed inner context.

### Common mistakes

- Calling `pop()` or inspecting `stack[-1]` on an empty stack (raises an IndexError). Always guard with `if stack:`.
- Conflating LIFO (Stack) with FIFO (Queue) logic, leading to reversed execution order.
- Forgetting to push state snapshot frames when emulating complex recursive call stacks manually.
- Failing to clear accumulated intermediate values or pending multipliers upon exiting scopes in string decoding.

### Real-world applications

- Call Stack management in language runtimes (tracking function frames and local variables).
- Undo/Redo history buffers in text editors and graphics software.
- Syntax parsing and AST generation in compilers (e.g., matching closing braces, operational precedence).
- Browser navigation back-button buffer.

## Example

### Tracing Balanced Nested Scope Matching

Given the string `s = "[(a+b)*{c}]"`:

1. `char = '['`: Push `'['` -> Stack: `['[']`
2. `char = '('`: Push `'('` -> Stack: `['[', '(']`
3. `char = 'a'`, `'+'`, `'b'`: Ignore alphanumeric/operators.
4. `char = ')'`: Top is `'('`, matching pair! Pop `'('` -> Stack: `['[']`
5. `char = '*'`:
6. `char = '{'`: Push `'{'` -> Stack: `['[', '{']`
7. `char = 'c'`: Ignore
8. `char = '}'`: Top is `'{'`, matching pair! Pop `'{'` -> Stack: `['[']`
9. `char = ']'`: Top is `'['`, matching pair! Pop `'['` -> Stack: `[]`  
Result: Stack is empty at the end, string is valid.

## Visual Explanation

```text
Push 'A'    Push 'B'    Pop ('B')   Push 'C'
  |   |       | B |       |   |       | C |
  | A |       | A |       | A |       | A |
  +---+       +---+       +---+       +---+
```

## Complexity

- **Time Complexity:** push: O(1) amortized, pop: O(1), peek: O(1). Overall string/array traversals using a stack are O(N) where N is input size.
- **Space Complexity:** O(N) in the worst case to store elements in the stack.

Dynamic array capacity resizing leads to amortized O(1) push operations, with rare O(N) reallocations.

## Interview Perspective

1. **How do you implement a stack using queues, and what are the time complexities?**
   <details><summary>What a strong answer covers</summary>

   Explain using one or two queues (e.g., using a single queue by re-enqueueing N-1 elements on every push to make push O(N) and pop O(1), or using two queues to make push O(1) and pop O(N)).

   </details>
2. **When would you prefer an explicit stack over recursion in production systems?**
   <details><summary>What a strong answer covers</summary>

   Explain call stack overflow limitations (stack limit in Python/OS), performance overhead of frame creation, and precise control over memory usage.

   </details>
3. **How can you implement a stack with O(1) max/min retrieval?**
   <details><summary>What a strong answer covers</summary>

   Maintain an auxiliary stack alongside the main stack (or store tuples `(val, current_min)`) that tracks the running minimum/maximum at each level.

   </details>
4. **What is the difference between postfix evaluation and infix evaluation using stacks?**
   <details><summary>What a strong answer covers</summary>

   Infix requires managing operator precedence using the Shunting Yard algorithm (two stacks: operators and operands). Postfix (RPN) requires only a single operand stack because operations are unambiguous and do not use parentheses.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Validate Stack Sequences](exercises/problem-01.md) | Easy/Medium | Simulation of LIFO Stack push and pop operations | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Basic Calculator with Parentheses and Addition/Subtraction](exercises/problem-02.md) | Medium | Expression evaluation with unary minus and dynamic nested state using stack | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Remove All Adjacent Duplicates in String II](exercises/problem-03.md) | Medium/Hard | State compression using dynamic dynamic frequency stacks | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Maximum Frequency Stack](exercises/problem-04.md) | Medium/Hard | Frequency mapping combined with bucketed stacks | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Build Binary Tree from Preorder Traversal with Null Tokens](exercises/problem-05.md) | Hard | Iterative tree construction from serialized string using explicit state stack | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-032
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: stack, lifo, expression-evaluation, string-processing, hash-map*
