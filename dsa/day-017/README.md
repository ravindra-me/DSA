# Day 17: Day 17: Recursion Mastery & Structural Decomposition

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 17 | 2026-10-26 | Fundamentals | Revision (stage 1) | progressive | Python 3.12 |

> **Revision day.** You first studied this topic earlier; today recaps the essentials and gives you brand-new problems. (spaced revision due on day 11 of 'recursion' (learned on day 4))

Recursion is the foundational mental model behind divide-and-conquer, backtracking, and structural traversal. In this revision lesson, we solidify the core invariants: designing robust base cases, visualizing call stacks and recursion trees, analyzing auxiliary stack space, and refactoring toward accumulator-driven tail calls. We then apply these principles to challenging multi-concept problems spanning linked structures, monotonic stacks, and combinatorial searches.

## Topic

**Recursion**: base case, recursive case, call stack, recursion trees, tail recursion

## Learning Objectives

By the end of this lesson you should be able to:

- Identify and enforce strict base-case and recursive-step invariants to guarantee termination without stack overflow.
- Derive time and space complexities using recursion trees, depth analysis, and auxiliary frame counting.
- Formulate tail-recursive functions with accumulator arguments and recognize language-level limitations (e.g., Python's lack of TCO).
- Combine recursion with previously learned structures such as singly-linked lists, stacks, and hash maps to solve non-trivial decomposition problems.

## Concept Explanation

### What it is

Recursion is a programming technique where a function solves a problem by calling itself with strictly smaller sub-instances of the same problem. Every recursive formulation relies on two pillars: a **base case** (the minimal stopping condition that returns directly without further self-calls) and a **recursive case** (which reduces the input toward the base case and aggregates sub-results).

### Why it exists

Many fundamental structures—such as nested hierarchical data, inductive mathematical definitions, divide-and-conquer partitions, and combinatorial spaces—are intrinsically self-similar. Without recursion, traversing or transforming these structures requires manual stack simulation, which frequently introduces complex state-tracking boilerplate and error-prone loop controls.

### When to use it

Use recursion when a problem exhibits optimal substructure (the solution to the whole depends directly on solutions to smaller subproblems of identical shape), when traversing inductively defined structures (linked lists, trees, nested expressions), or when exploring branching combinatorial state spaces (backtracking, permutations, subsets).

### When NOT to use it

Avoid recursion when the maximum call depth exceeds the system stack limit (typically $10^3$ to $10^4$ frames in Python), when subproblems overlap heavily without memoization leading to exponential runtime (e.g., naive Fibonacci), or when a trivial iterative loop (such as simple two-pointer traversal) achieves $O(1)$ auxiliary space without stack overhead.

### How it works internally

When a function executes a self-call, the runtime environment allocates an activation record (stack frame) on the call stack containing local variables, parameters, and the return instruction address. Execution suspends at the call site until the child frame completes. Once the base case is hit, values bubble up the call stack via return expressions, popping frames sequentially until the root invocation resolves.

### Common mistakes

- Omitting or incorrectly ordering base cases, leading to unbounded recursion and `RecursionError`.
- Failing to make strictly monotonic progress toward the base case in every branch (e.g., calling `f(n)` instead of `f(n - 1)`).
- Ignoring the call stack overhead in auxiliary space complexity analysis (a recursive tree of depth $D$ requires at least $O(D)$ stack space).
- Performing expensive operations (such as list slicing `arr[1:]` which costs $O(N)$ time and memory) inside the recursive step rather than passing index pointers.
- Assuming Python optimizes tail recursion: Python does not perform Tail Call Optimization (TCO), so tail calls still consume $O(N)$ stack frames.

### Real-world applications

- Recursive descent parsers and AST interpreters used in compilers (e.g., Python's `ast` module, GCC, Clang).
- JSON, YAML, and XML serialization and deserialization engines parsing deeply nested hierarchical objects.
- Divide-and-conquer sorting and computational geometry engines (Merge Sort, Quickselect, Convex Hull).
- Filesystem crawlers and permission reconcilers walking hierarchical directory trees.

## Example

### Tracing Reversing a Singly-Linked List Recursively

Given list `1 -> 2 -> 3 -> None`. We wish to reverse it recursively by returning the new head and re-wiring backwards during the unwind phase.

```python
def reverse_list(head: ListNode | None) -> ListNode | None:
    # Base case: empty or single node
    if head is None or head.next is None:
        return head
    
    # Recursive step: reverse the tail
    new_head = reverse_list(head.next)
    
    # Unwind phase: flip pointer of the immediate successor
    head.next.next = head
    head.next = None
    
    return new_head
```

**Step-by-step Trace:**
1. `reverse_list(1)`: calls `reverse_list(2)`.
2. `reverse_list(2)`: calls `reverse_list(3)`.
3. `reverse_list(3)`: base case triggered (`head.next is None`). Returns node `3`.
4. Unwind to frame `2`: `head` is `2`. `head.next` is `3`. Sets `3.next = 2`, `2.next = None`. Returns `3`.
5. Unwind to frame `1`: `head` is `1`. `head.next` is `2`. Sets `2.next = 1`, `1.next = None`. Returns `3`.
6. Final returned structure: `3 -> 2 -> 1 -> None`.

## Visual Explanation

```text
Call Stack Trace during Unwind:

[ Frame 1: head=1 ] -> waits for reverse_list(2)
  [ Frame 2: head=2 ] -> waits for reverse_list(3)
    [ Frame 3: head=3 ] -> returns node 3 (Base Case)
  [ Frame 2 resumes ] -> 3.next = 2, 2.next = None -> returns 3
[ Frame 1 resumes ] -> 2.next = 1, 1.next = None -> returns 3

Recursion Tree for Divide-and-Conquer (e.g. merge / split):
                     T(n)
                  /        \
             T(n/2)        T(n/2)
            /     \        /     \
         T(n/4)  T(n/4)  T(n/4)  T(n/4)
         
Height: O(log n) levels. Total work per level: O(n). Overall: O(n log n).
```

## Complexity

- **Time Complexity:** Determined by (Total Recursive Calls) × (Non-recursive Work per Call). For linear recursion: O(N); for balanced binary divide-and-conquer: O(N log N) or O(N).
- **Space Complexity:** O(D) auxiliary space, where D is the maximum depth of the call stack corresponding to the height of the recursion tree.

Even if tail calls are employed, runtimes without TCO (such as standard CPython) allocate one frame per invocation, retaining O(D) auxiliary stack space. Unbalanced divide-and-conquer can degrade to O(N) stack depth in the worst case.

## Interview Perspective

1. **What is tail recursion, and does Python optimize tail-recursive calls?**
   <details><summary>What a strong answer covers</summary>

   Explain that a tail call is a recursive call performed as the very last operation of a function, returning the result directly without post-processing. Mention that while languages like Scheme or Haskell reuse the current stack frame (TCO), standard CPython intentionally does not implement TCO to preserve full, uncorrupted stack tracebacks for debugging.

   </details>
2. **How do you systematically convert any recursive function into an iterative one?**
   <details><summary>What a strong answer covers</summary>

   Discuss using an explicit heap-allocated stack (or queue depending on traversal order) to store local variable snapshots and program states. Explain how the call stack is simulated by pushing child frames and popping them when processing results.

   </details>
3. **How do you detect whether recursion will cause a stack overflow before running your code in production?**
   <details><summary>What a strong answer covers</summary>

   Assess input size upper bounds against `sys.getrecursionlimit()`. If the recursion depth scales linearly with input size $N$ and $N > 1000$, standard recursion is unsafe unless refactored iteratively or tree depth is guaranteed logarithmic $O(\log N)$.

   </details>
4. **What is the difference between top-down recursion (head recursion) and bottom-up recursion (accumulators)?**
   <details><summary>What a strong answer covers</summary>

   Explain that top-down/standard recursion computes solutions on the return path after subcalls resolve, while accumulator-based recursion carries intermediate state forward through parameters, computing the answer as it descends.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Pairwise Swap Linked List Nodes](exercises/problem-01.md) | Easy/Medium | Recursive structural rewiring on singly linked lists | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Reverse a Stack Using Pure Recursion](exercises/problem-02.md) | Medium | Auxiliary stack frame state preservation without loops or external collections | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Decode String with Nested Multipliers](exercises/problem-03.md) | Medium/Hard | Recursive descent parsing with call-stack index tracking | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Find K-th Symbol in Grammar](exercises/problem-04.md) | Medium/Hard | Divide-and-conquer on virtual binary trees with logarithmic recursion | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Parse and Evaluate Boolean Expressions](exercises/problem-05.md) | Hard | Complex multi-branch recursive AST evaluation | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-017
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: Base cases and termination proofs, Call stack frame mechanics, Recursion trees and depth analysis, Accumulators and tail call structuring, Recursive linked structure mutation, Divide and conquer decomposition*
