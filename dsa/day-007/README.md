# Day 7: Day 7: Linked Lists — Pointers, Dummy Nodes, and In-Place Mutations

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 7 | 2026-10-16 | Linear Data Structures | New topic | progressive | Python 3.12 |

Arrays store items contiguously in memory, making insertions and deletions expensive because existing elements must shift. A **linked list** decouples logical ordering from physical memory addresses by connecting individual nodes via pointers. Today, we will unpack node-pointer mechanics, master dummy heads to eliminate edge cases, and learn how to reverse and restructure chains in-place.

## Topic

**Linked Lists**: singly linked list, doubly linked list, insertion/deletion, dummy head, reversal

## Learning Objectives

By the end of this lesson you should be able to:

- Construct and traverse singly and doubly linked list nodes from scratch in Python.
- Perform O(1) node insertion and deletion given reference pointers without shifting memory.
- Apply the dummy head (sentinel node) pattern to eliminate edge cases when mutating list boundaries.
- Reverse linked lists iteratively and recursively in O(n) time and O(1) auxiliary space.
- Detect cycles and locate split points using two-pointer (fast/slow) runner techniques.

## Concept Explanation

### What it is

A linked list is a linear collection of data elements called **nodes**, where each node contains its payload `val` and one or more reference pointers (`next`, and optionally `prev`) pointing to neighboring nodes in memory.

Unlike an array, which allocates a single contiguous block of memory, linked list nodes can reside anywhere in memory (the heap). They form a chain: you start at the `head` pointer and follow pointers from node to node until reaching `None` (representing the end of the list).

### Why it exists

In static or dynamic arrays, inserting or deleting an element at index 0 requires shifting every subsequent element right or left, taking $O(n)$ time. Furthermore, dynamic arrays require occasional resizing operations that allocate new memory blocks and copy all items.

A linked list solves this: if you already hold a reference to a node, inserting a new node right after it or removing it takes $O(1)$ pointer reassignments without shifting any other data in memory.

### When to use it

Use linked lists when:
- You need frequent $O(1)$ insertions or deletions at the head or at positions where you already maintain a pointer.
- The total collection size is unknown or changes drastically, and you want to avoid dynamic array resizing spikes.
- Implementing underlying structures like queues, stacks, LRU caches (doubly linked list), or graph adjacency lists.

### When NOT to use it

Do not use linked lists when:
- You need frequent random access by index (e.g., getting element $i$). Accessing element $i$ in a linked list requires $O(i)$ traversal, whereas arrays do it in $O(1)$.
- Cache locality and low memory overhead are paramount. Nodes store explicit pointer fields (8 bytes each in 64-bit systems), and scattered heap memory leads to CPU cache misses.

### How it works internally

1. **Node Definition**: Each node is an object instance with fields: `val` and `next` (and `prev` for doubly linked lists).
2. **Traversal Invariant**: Start with `curr = head`. As long as `curr is not None`, process `curr.val` and step forward: `curr = curr.next`.
3. **Insertion**: To insert node $N$ between $A$ and $B$ (where $A.next == B$):
   - Step 1: Set $N.next = A.next$ ($N$ points to $B$).
   - Step 2: Set $A.next = N$ ($A$ points to $N$). Order matters: swapping these steps loses the reference to $B$.
4. **Deletion**: To delete node $B$ between $A$ and $C$ ($A.next == B$ and $B.next == C$):
   - Set $A.next = B.next$ (or $A.next = A.next.next$). Node $B$ is unlinked and reclaimed by garbage collection.
5. **The Dummy Head (Sentinel)**: When operations can insert or remove the first element, maintaining `head` requires tedious `if head is None:` checks. Introducing a pseudo-node `dummy = ListNode(0, head)` ensures the true head always has a preceding node. At the end, return `dummy.next`.

### Common mistakes

- Losing node references during pointer updates: overwriting `curr.next` before caching the downstream node (`nxt = curr.next`) results in permanently lost nodes.
- Dereferencing `None` (`AttributeError: 'NoneType' object has no attribute 'next'`), caused by failing to guard loops with `while curr:` or dereferencing `curr.next.next` when `curr.next` is `None`.
- Creating infinite loops during list reversals by forgetting to set the original head's `next` pointer to `None`.
- Modifying `curr` when you actually needed to modify `curr.next` to re-wire nodes before the target deletion point.

### Real-world applications

- Operating System Process Schedulers: Ready queues and round-robin scheduling algorithms use circular linked lists.
- LRU (Least Recently Used) Cache: Pairs a hash map with a doubly linked list to achieve $O(1)$ lookups and $O(1)$ removals/insertions.
- Undo/Redo Stacks in Text Editors: Implemented via doubly linked lists where the cursor moves forward and backward across modification states.
- Memory Allocation: Dynamic memory allocators (like `malloc` implementations) maintain free lists of available memory blocks using linked chains.

## Example

### Tracing In-Place Singly Linked List Reversal

Given list: `1 -> 2 -> 3 -> None`
Goal: Reverse pointers so that `3 -> 2 -> 1 -> None`.

We maintain three pointers:
- `prev`: tracks the reversed portion (initialized to `None`).
- `curr`: tracks the node currently being redirected (initialized to `head`, pointing to `1`).
- `nxt`: temporarily saves the rest of the list so it isn't lost.

```python
prev = None
curr = head
while curr:
    nxt = curr.next  # 1. Save future
    curr.next = prev  # 2. Reverse link
    prev = curr  # 3. Advance prev
    curr = nxt  # 4. Advance curr
return prev  # New head
```

**Step-by-step trace:**
- **Initial State**: `prev = None`, `curr = Node(1)`
- **Iteration 1**:
  - `nxt = Node(2)`
  - `curr.next = None` (Node 1 points to `None`)
  - `prev = Node(1)`
  - `curr = Node(2)`
- **Iteration 2**:
  - `nxt = Node(3)`
  - `curr.next = Node(1)` (Node 2 points to Node 1)
  - `prev = Node(2)`
  - `curr = Node(3)`
- **Iteration 3**:
  - `nxt = None`
  - `curr.next = Node(2)` (Node 3 points to Node 2)
  - `prev = Node(3)`
  - `curr = None`
- **Loop ends**: `curr` is `None`. Return `prev` (`Node(3)`), which is the head of `3 -> 2 -> 1 -> None`.

## Visual Explanation

```text
Initial:
  head -> [1 | next] -> [2 | next] -> [3 | next] -> None
  prev = None, curr = [1]

Step 1: Save next (2), redirect 1 -> None
  None <- [1 | next]    [2 | next] -> [3 | next] -> None
          ^             ^
         prev          curr (nxt)

Step 2: Save next (3), redirect 2 -> 1
  None <- [1 | next] <- [2 | next]    [3 | next] -> None
                        ^             ^
                       prev          curr (nxt)

Step 3: Save next (None), redirect 3 -> 2
  None <- [1 | next] <- [2 | next] <- [3 | next]
                                      ^
                                     prev (new head!)
```

## Complexity

- **Time Complexity:** Prepend: O(1) (reassign head); Append: O(n) without tail pointer or O(1) with tail; Insertion/Deletion at given node: O(1); Access/Search by index: O(n) (linear scan required).
- **Space Complexity:** O(1) auxiliary space for iterative mutations; O(n) heap memory to store n individual nodes.

Unlike arrays where appending is amortized $O(1)$ and worst-case $O(n)$ due to geometric resizing, appending to a linked list with a tail pointer is strictly $O(1)$ in the worst case.

## Interview Perspective

1. **Why would someone choose a doubly linked list over a singly linked list?**
   <details><summary>What a strong answer covers</summary>

   A doubly linked list allows bidirectional traversal and $O(1)$ deletion of a node when given only a pointer to that node (since `node.prev` gives direct access to the predecessor). Singly linked lists require $O(n)$ traversal to find the node prior to the one being deleted unless you use the value-copy trick.

   </details>
2. **What is the dummy head (sentinel) pattern and when is it most useful?**
   <details><summary>What a strong answer covers</summary>

   A dummy head is an auxiliary node created before the actual head of the list (`dummy.next = head`). It eliminates edge cases where the head itself needs to be removed, replaced, or merged, avoiding repetitive `if head is None` or special handling for index 0.

   </details>
3. **How do you find the middle node of a linked list in a single pass?**
   <details><summary>What a strong answer covers</summary>

   Use Floyd's fast and slow pointer pattern (tortoise and hare). Move `slow` by 1 step and `fast` by 2 steps. When `fast` reaches the end (`None` or `fast.next is None`), `slow` is guaranteed to be at the middle.

   </details>
4. **What is the memory and CPU performance trade-off between an array and a linked list?**
   <details><summary>What a strong answer covers</summary>

   Arrays enjoy contiguous memory layout, providing spatial locality that leverages CPU cache lines effectively. Linked lists store nodes unpredictably across the heap, leading to cache misses. Additionally, linked lists incur metadata overhead (8-16 bytes per node for pointers).

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Reverse a Linked List](exercises/problem-01.md) | Easy | Basic pointer manipulation and iterative reversal | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Remove Elements by Value](exercises/problem-02.md) | Easy/Medium | Dummy head pattern for deletion | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Merge Two Sorted Lists](exercises/problem-03.md) | Medium | Two-pointer list merging with dummy head | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Remove N-th Node From End of List](exercises/problem-04.md) | Medium/Hard | Fast and slow runner pointers with gap | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Reverse Nodes in k-Group](exercises/problem-05.md) | Hard | Complex multi-pointer block reversal | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-007
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: singly-linked-list, doubly-linked-list, dummy-head, pointer-manipulation, fast-and-slow-pointers, list-reversal*
