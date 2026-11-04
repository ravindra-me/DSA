# Day 26: Day 26: Linked Lists Revision & Advanced Patterns

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 26 | 2026-11-04 | Linear Data Structures | Revision (stage 1) | progressive | Python 3.12 |

> **Revision day.** You first studied this topic earlier; today recaps the essentials and gives you brand-new problems. (spaced revision due on day 14 of 'linked-list' (learned on day 7))

Linked list operations require precise pointer management without lost references. In this revision lesson, we solidify fundamentals like dummy nodes and pointer reassignment while taking on complex interview-grade patterns combining linked lists with stack, hash map, and sliding window techniques.

## Topic

**Linked Lists**: singly linked list, doubly linked list, insertion/deletion, dummy head, reversal

## Learning Objectives

By the end of this lesson you should be able to:

- Master defensive pointer reassignment using dummy nodes and temporary variables.
- Solve linked list problems combining sliding windows, stacks, and double-ended references.
- Implement in-place list transformations including multi-pass segment reversals and interleaving.
- Handle delicate edge cases such as empty lists, single-node lists, and cycles.

## Concept Explanation

### What it is

A linked list is a linear data structure where elements (nodes) are stored non-contiguously in memory, each pointing to the next (and optionally previous) node via explicit memory pointers or references.

### Why it exists

Unlike dynamic arrays, linked lists allow $O(1)$ dynamic insertions and deletions at arbitrary positions once a node reference is held, without requiring memory reallocation or shifting elements.

### When to use it

Use linked lists when frequent insertions and deletions at known positions occur, when building queues/deques, or when dynamic sizing without contiguous memory allocation is required.

### When NOT to use it

Avoid linked lists when random access by index ($O(n)$ time) is needed or when cache locality is critical, as node traversal incurs frequent cache misses compared to flat arrays.

### How it works internally

Operations rely on modifying `next` (and `prev`) pointers. A static dynamic dummy node (`dummy = ListNode(0, head)`) simplifies edge cases involving head updates. Reversals maintaining invariants update pointers iteratively: `nxt = curr.next; curr.next = prev; prev = curr; curr = nxt`.

### Common mistakes

- Losing reference to the tail of a list by overwriting `curr.next` before caching it.
- Dereferencing `None` (`AttributeError: 'NoneType' object has no attribute 'next'`).
- Creating infinite loops by introducing cycles during pointer reassignments.
- Forgetting to update both `next` and `prev` pointers in doubly linked lists.

### Real-world applications

- LRU Cache implementations (Doubly Linked List + Hash Map).
- OS memory management (free lists of memory blocks).
- Undo/Redo buffers in text editors and browser history navigation.

## Example

Reversing a list segment from head to tail using a loop:

Given `1 -> 2 -> 3 -> None`:
1. Initialize `prev = None`, `curr = head (1)`.
2. Iteration 1: `nxt = 2`, `1.next = None`, `prev = 1`, `curr = 2`.
3. Iteration 2: `nxt = 3`, `2.next = 1`, `prev = 2`, `curr = 3`.
4. Iteration 3: `nxt = None`, `3.next = 2`, `prev = 3`, `curr = None`.
5. Return `prev` (3), resulting in `3 -> 2 -> 1 -> None`.

## Visual Explanation

```text
Initial: [Dummy] -> [1] -> [2] -> [3] -> None
                  ^ head

Reversing node 1 to 2:
Step 1: Save next pointer (nxt = curr.next)
Step 2: curr.next = prev
Step 3: prev = curr
Step 4: curr = nxt

Result: None <- [1] <- [2] <- [3] (prev points to 3)
```

## Complexity

- **Time Complexity:** Traversal: O(n); Insertion/Deletion (with handle): O(1); Search: O(n).
- **Space Complexity:** O(1) auxiliary space for iterative pointer manipulations.

Recursion can make pointer code elegant but adds O(n) implicit call stack space.

## Interview Perspective

1. **Why is a dummy node useful in linked list problems?**
   <details><summary>What a strong answer covers</summary>

   It eliminates special boundary checks for edge cases such as empty lists, single-node updates, or operations modifying the head node.

   </details>
2. **How do you detect and find the entry point of a cycle in O(1) auxiliary space?**
   <details><summary>What a strong answer covers</summary>

   Use Floyd's Cycle-Finding Algorithm (fast and slow pointers). Once they intersect, reset one pointer to head and move both at step speed 1; their meeting point is the cycle entry.

   </details>
3. **What are the cache efficiency implications of linked lists vs arrays?**
   <details><summary>What a strong answer covers</summary>

   Arrays store elements contiguously, maximizing spatial locality and hardware cache prefetching. Linked list nodes are scattered across heap memory, leading to frequent cache misses during traversal.

   </details>
4. **How do you check if a linked list is a palindrome in O(n) time and O(1) space?**
   <details><summary>What a strong answer covers</summary>

   Find the middle via fast/slow pointers, reverse the second half in-place, compare the two halves node-by-node, and optionally restore the second half.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Partition List around Pivot Value](exercises/problem-01.md) | Easy/Medium | Stable partitioning using dual dummy head chains | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Split Linked List into k Consecutive Parts](exercises/problem-02.md) | Medium | List length computation and chunk slicing with dummy pointers | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Reverse Sub-List Between Positions](exercises/problem-03.md) | Medium/Hard | In-place partial list reversal with local pointer reconnection | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Add Two Numbers II (Most Significant Digit First)](exercises/problem-04.md) | Medium/Hard | Linked list processing with explicit stack or head expansion without reversal | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Flatten a Multilevel Doubly Linked List](exercises/problem-05.md) | Hard | Complex pointer rewiring in hierarchical doubly linked structures | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-026
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: linked-list, singly-linked-list, doubly-linked-list, dummy-head, pointer-reversal, two-pointers*
