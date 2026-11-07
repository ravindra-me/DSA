# Day 29: Linked List Techniques (Revision & Advanced Synthesis)

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 29 | 2026-11-07 | Linear Data Structures | Revision (stage 1) | progressive | Python 3.12 |

> **Revision day.** You first studied this topic earlier; today recaps the essentials and gives you brand-new problems. (spaced revision due on day 16 of 'linked-list-techniques' (learned on day 9))

This revision session consolidates essential singly linked list patterns: two-pointer techniques (fast/slow runner, fixed-gap separation), cycle analysis, list restructuring, and merge operations. We focus on pointer-level invariants, edge-case mitigation (dummy heads), and integrating lists with external primitives like min-heaps, hash tables, and divide-and-conquer strategies.

## Topic

**Linked List Techniques**: fast/slow pointers, cycle detection, middle node, merging lists, k-th from end

## Learning Objectives

By the end of this lesson you should be able to:

- Execute two-pointer strategies (tortoise/hare, fixed-distance gap) without off-by-one errors or dereferencing null pointers.
- Utilize dummy head sentinel nodes to eliminate special-case branching at the head of a list.
- Formally reason about pointer rewiring invariants and in-place list reversal/reordering.
- Combine linked list operations with heaps and divide-and-conquer for multi-way merging and complex transformations.

## Concept Explanation

### What it is

Linked list techniques leverage structural pointers rather than index arithmetic to traverse, partition, and modify sequential data in $O(1)$ auxiliary space. Key patterns include the **fast and slow pointer** (Floyd's Tortoise and Hare) for cycle detection and midpoint discovery, the **fixed-distance gap pointer** for $k$-th from end queries, and **sentinel (dummy) nodes** to homogenize boundary mutations.

### Why it exists

Because singly linked lists only support $O(1)$ traversal via `.next` references, indexing is $O(n)$ and length is generally unknown up front. Without two-pointer techniques, finding midpoints or nodes relative to the end requires multiple passes, and mutating the list head requires special-case branching that frequently introduces `AttributeError: 'NoneType' object has no attribute 'next'`.

### When to use it

Apply these techniques when you must inspect or modify singly linked lists in a single pass, find topological cycles, locate midpoints without counting length first, remove elements relative to the end, or interleave/merge sequences in $O(1)$ extra memory.

### When NOT to use it

Do not force linked lists when random access ($O(1)$ lookup by index) is required, or when cache locality is critical (contiguous arrays perform orders of magnitude faster due to prefetching). If elements must be indexed frequently, convert to an array first.

### How it works internally

1. **Sentinel/Dummy Node**: Allocate `dummy = ListNode(0, head)`. All modifications to `head` become updates to `dummy.next`, avoiding special cases for empty lists or head deletions.
2. **Fast & Slow (Midpoint / Cycle)**: `slow` steps 1 node, `fast` steps 2 nodes. If `fast` and `slow` meet, a cycle exists. When `fast` reaches the tail/null, `slow` sits precisely at the midpoint.
3. **Fixed Window**: To locate the $k$-th node from the end, advance a leading pointer by $k$ steps. Then advance both leading and trailing pointers in lockstep until the leader reaches the terminal null.
4. **In-place Reversal**: Maintain three pointers (`prev = None`, `curr = head`, `nxt = curr.next`), swing `curr.next = prev`, and advance until `curr` is null.

### Common mistakes

- Accessing `fast.next.next` without first validating that both `fast` and `fast.next` are non-null.
- Losing reference to the remaining list during node detachment because `next` was overwritten before caching it in a temporary pointer.
- Off-by-one errors choosing between `while fast and fast.next:` (first middle on even length) versus `while fast.next and fast.next.next:` (last node of the first half).
- Failing to sever cycles after detection or modification, leading to infinite loops during subsequent traversals.

### Real-world applications

- Memory allocators (e.g., free lists in `malloc`/`jemalloc`) maintaining chains of free memory blocks.
- Garbage collection algorithms tracking reference cycles and unreachability graphs.
- Lock-free and concurrent data structures (e.g., Michael-Scott Queues) using atomic compare-and-swap pointer rewiring.
- Kernel scheduling queues managing task states and transition rings.

## Example

Consider detecting a cycle and finding the loop entrance in $1 \to 2 \to 3 \to 4 \to 5 \to 3$ (loop length $L=3$, non-loop $F=2$):
1. Initialize `slow = head (1)`, `fast = head (1)`.
2. Step 1: `slow -> 2`, `fast -> 3`.
3. Step 2: `slow -> 3`, `fast -> 5`.
4. Step 3: `slow -> 4`, `fast -> 4` (Intersection found at node 4).
5. Mathematical invariant: Distance from head to cycle entrance is $F$. Distance from intersection point around the cycle to entrance is also $F \pmod L$.
6. Reset `p1 = head (1)`, keep `p2 = intersection (4)`.
7. Advance both 1 step at a time: `p1 -> 2`, `p2 -> 5`; then `p1 -> 3`, `p2 -> 3`. They meet at node 3, the cycle entrance.

## Visual Explanation

```text
1. Two-Pointer Midpoint Discovery:
   Step 0: S, F at [1] -> [2] -> [3] -> [4] -> None
   Step 1:      [1] -> S[2] -> [3] -> F[4] -> None
   Step 2:      [1] -> [2] -> S[3] -> [4] -> F: None (Terminated, S is at 3)

2. Fixed-Gap k-th Node (k=2):
   Start:       T at [1], L advanced by 2 to [3]
   Advance:     [1] -> T[2] -> [3] -> L[4]
   Advance:     [1] -> [2] -> T[3] -> [4] -> L: None (T is 2nd from end)
```

## Complexity

- **Time Complexity:** O(n) for single and double pointer traversals; O(n log k) for merging k lists using a min-heap or divide-and-conquer.
- **Space Complexity:** O(1) auxiliary space for pointer manipulations; O(k) for heap-assisted k-way merge.

In-place pointer manipulation achieves optimal O(1) space, but recursion stacks (e.g., recursive reversal or recursive merges) consume O(n) space and risk stack overflow in Python (default recursion limit 1000).

## Interview Perspective

1. **How do you mathematically prove that Floyd's cycle-finding algorithm guarantees slow and fast will meet if a cycle exists?**
   <details><summary>What a strong answer covers</summary>

   Once both pointers enter a cycle of length L, the relative distance between them decreases by exactly 1 step per iteration modulo L. Since distance decreases by 1 each step, it must reach 0 (congruent to 0 mod L) in at most L steps.

   </details>
2. **Why is a dummy (sentinel) head node considered best practice in interview code?**
   <details><summary>What a strong answer covers</summary>

   It eliminates conditional logic for edge cases where the head node itself is deleted, replaced, or prepended to, ensuring invariants apply uniformly across every node.

   </details>
3. **What is the trade-off between merging k sorted lists with a min-heap vs divide-and-conquer?**
   <details><summary>What a strong answer covers</summary>

   Both achieve O(N log k) time. The min-heap takes O(k) space for heap state and processes node-by-node. Divide-and-conquer merges pairs in-place with O(log k) recursion depth (or O(1) iterative space) without node-tuple comparisons.

   </details>
4. **How do you handle Python's heapq when storing ListNode objects that may have equal values?**
   <details><summary>What a strong answer covers</summary>

   Tuple comparison falls through to the next element if keys match. Store (node.val, unique_id, node) or define `__lt__` on ListNode to avoid comparing memory addresses or unorderable nodes.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Partition List Around Pivot](exercises/problem-01.md) | Easy/Medium | pointer-partitioning | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Swap Nodes in Pairs](exercises/problem-02.md) | Medium | in-place-reversal | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Sort Linked List in O(n log n)](exercises/problem-03.md) | Medium/Hard | fast-slow-pointers | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Merge K Sorted Linked Lists](exercises/problem-04.md) | Medium/Hard | k-way-merge | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Reverse Nodes in K-Group](exercises/problem-05.md) | Hard | in-place-reversal | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-029
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: fast-slow-pointers, cycle-detection, dummy-sentinel, in-place-reversal, k-way-merge, pointer-partitioning*
