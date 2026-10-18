# Day 9: Linked List Techniques: Two Pointers, Cycles, and Beyond

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 9 | 2026-10-18 | Linear Data Structures | New topic | progressive | Python 3.12 |

Because linked lists do not support random index access, standard array navigation algorithms fail or incur expensive $O(N)$ lookups. By deploying coordinated pointer techniques—such as fast and slow pointers, fixed-gap runners, and dummy sentinel nodes—we can detect cycles, locate specific positional elements, and splice lists together cleanly in $O(N)$ time and $O(1)$ auxiliary space.

## Topic

**Linked List Techniques**: fast/slow pointers, cycle detection, middle node, merging lists, k-th from end

## Learning Objectives

By the end of this lesson you should be able to:

- Apply the fast and slow pointer pattern (Floyd's Tortoise and Hare) to locate middle nodes and detect cycles.
- Derive mathematically why Floyd's cycle-finding algorithm determines the entry point of a loop in $O(N)$ time and $O(1)$ space.
- Use fixed-gap runner pointers to retrieve or remove elements relative to the end of a list in a single pass.
- Leverage sentinel (dummy) head nodes to eliminate edge cases when merging, mutating, or deleting list nodes.

## Concept Explanation

### What it is

Linked list techniques are specialized pointer coordination patterns designed to traverse, inspect, and restructure singly linked chains without knowing their length in advance and without allocating secondary collections (like hash sets or arrays). The most famous of these is the two-pointer technique, where two references advance through the chain at different speeds (fast/slow) or from different offsets (runner/fixed gap).

### Why it exists

In arrays, finding the middle element or the $k$-th element from the end is trivial arithmetic ($A[n // 2]$ or $A[-k]$) in $O(1)$ time. In singly linked lists, links only point forward, and length is unknown unless explicitly counted. A naive solution requires either multiple linear passes or extra memory ($O(N)$ space) to store visited nodes. Linked list techniques allow us to accomplish these goals in a single pass using $O(1)$ auxiliary memory.

### When to use it

Use these techniques when working with singly or doubly linked structures and the problem asks to: find a middle/split point, detect a loop or cycle, find the start of a cycle, find or delete the $k$-th element from the end, or merge sorted lists without allocating new list nodes.

### When NOT to use it

Do not use pointer racing if random-access indexing is natively supported (such as arrays, Python lists, or deques). If the data structure permits backward traversal (like a doubly linked list with a known tail), a simple backward traversal from tail is far simpler than a runner pointer.

### How it works internally

1. **Fast & Slow (Tortoise and Hare)**: Initialize `slow = head` and `fast = head`. In each step, advance `slow` by 1 node and `fast` by 2 nodes. When `fast` reaches the end (`None` or `fast.next is None`), `slow` resides precisely at the middle node.
2. **Cycle Detection & Start Identification**: If a cycle exists, `fast` enters the loop first. Because `fast` reduces the relative gap between itself and `slow` by 1 node on every iteration ($2 - 1 = 1$), they are guaranteed to collide within the loop. To find the cycle entrance, reset one pointer to `head` and keep the other at the collision point, then advance both at 1 step per iteration. By mathematical congruence, they will meet at the cycle's entrance node.
3. **Fixed-Gap Runner**: To find the $k$-th node from the end, advance an `ahead` pointer $k$ steps forward first. Then advance both `ahead` and `behind` by 1 step simultaneously. When `ahead` reaches past the tail (`None`), `behind` points to the $k$-th node from the end.
4. **Sentinel (Dummy) Node**: Allocate a dummy node `dummy = ListNode(0)` and point `tail = dummy`. Spliced or merged nodes are appended directly to `tail.next`, entirely bypassing special-casing for an initially empty list.

### Common mistakes

- Accessing `.next` on a `None` pointer: Failing to guard `while fast and fast.next:` causes an `AttributeError` when `fast` reaches the tail.
- Off-by-one errors when selecting the middle node: Depending on whether `fast` starts at `head` or `head.next`, or whether the loop condition checks `fast.next.next`, you may land on the first middle vs. the second middle in an even-length list.
- Losing node references during pointer reassignment: Overwriting `curr.next` before preserving the remaining chain in a temporary pointer permanently drops the rest of the list.
- Forgetting to advance the runner pointer before beginning the tandem march, which results in finding the wrong offset from the tail.

### Real-world applications

- Memory allocators and garbage collectors (such as mark-and-sweep or reference tracing) use pointer traversal and cycle detection to identify unreachable circular references.
- Operating system thread schedulers and kernel runqueues maintain circular intrusive linked lists; cycle and corruption checks ensure scheduling queues do not enter runaway loops.
- Music and media streaming services model repeat and shuffle playlists as circular linked chains, requiring loop-point resolution and splice operations.

## Example

Finding the middle node of a list: `1 -> 2 -> 3 -> 4 -> 5 -> None`

```python
# Initial state
slow = head (1)
fast = head (1)

# Iteration 1:
slow = slow.next -> (2)
fast = fast.next.next -> (3)

# Iteration 2:
slow = slow.next -> (3)
fast = fast.next.next -> (5)

# Loop termination check:
# fast.next is None, so loop terminates.
# slow points to node 3, the exact middle of the list.
```
For an even-length list `1 -> 2 -> 3 -> 4 -> None`:
- Iter 1: `slow` -> 2, `fast` -> 3
- Iter 2: `slow` -> 3, `fast` -> `None`
- Terminates because `fast` is `None`. `slow` points to 3 (the second middle node).

## Visual Explanation

```text
Finding the Middle Node (Odd Length: 5 nodes)

Step 0:
  [1] -> [2] -> [3] -> [4] -> [5] -> None
  S, F

Step 1:
  [1] -> [2] -> [3] -> [4] -> [5] -> None
          S             F

Step 2:
  [1] -> [2] -> [3] -> [4] -> [5] -> None
                        S             F  (fast.next is None -> STOP)
Result: slow is at node [3].

--------------------------------------------------------------

Fixed-Gap Runner for k-th from End (k = 2):
  List: [10] -> [20] -> [30] -> [40] -> None

1. Advance 'ahead' k=2 steps:
  [10] -> [20] -> [30] -> [40] -> None
   B               A

2. Move both ahead and behind until ahead reaches None:
  [10] -> [20] -> [30] -> [40] -> None
           B               A
  [10] -> [20] -> [30] -> [40] -> None
                   B               A (ahead is None -> STOP)
Result: behind is at node [30] (2nd from end).
```

## Complexity

- **Time Complexity:** Middle node: O(N) since fast visits every second node and slow visits half the nodes; Cycle detection: O(N) because fast catches slow within 1 loop revolution; k-th from end: O(N) single pass.
- **Space Complexity:** O(1) auxiliary space because operations only retain a constant number of pointer references (slow, fast, ahead, behind, dummy).

Fast and slow pointers complete in fewer steps than a two-pass approach ($N/2$ iterations vs $N + N/2$ steps), while retaining strict $O(1)$ space. Sentinel nodes incur $O(1)$ memory overhead and zero asymptotic runtime penalty, but drastically simplify edge-case conditional branches.

## Interview Perspective

1. **Can you prove mathematically why Floyd's Tortoise and Hare algorithm detects the cycle entry point?**
   <details><summary>What a strong answer covers</summary>

   Let $L$ be the distance from head to cycle entry, $C$ the cycle length, and $X$ the distance from entry to collision. Slow travels $d_s = L + X$, Fast travels $d_f = L + X + kC$. Since $d_f = 2 d_s$, $L + X + kC = 2(L + X) \implies L = kC - X = (k - 1)C + (C - X)$. Distance from head to entry ($L$) equals distance from collision to entry ($C - X$ plus complete loops). Moving one pointer from head and one from collision point at identical speed guarantees they meet at the entry.

   </details>
2. **How do you distinguish between returning the first middle node versus the second middle node in an even-length list?**
   <details><summary>What a strong answer covers</summary>

   Starting `fast = head` and checking `while fast and fast.next:` yields the second middle node (e.g. node 3 in a 4-node list). Starting `fast = head.next` with the same loop condition yields the first middle node (node 2 in a 4-node list).

   </details>
3. **Why is using a dummy (sentinel) head node considered a best practice when modifying linked lists?**
   <details><summary>What a strong answer covers</summary>

   A dummy node eliminates conditional checks for head insertion, head deletion, or starting an empty result list. The code does not need `if head is None:` or `if prev is None: head = new_node`. Returning `dummy.next` always safely references the real result head.

   </details>
4. **What happens if a linked list contains a cycle and you run an algorithm that assumes termination at `None`?**
   <details><summary>What a strong answer covers</summary>

   The traversal enters an infinite loop, eventually resulting in a timeout or, if recursive, an out-of-memory or stack overflow error (`RecursionError`). Cycle-safety checks must precede or accompany general traversals when cycle presence is unverified.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Find Middle Node Value](exercises/problem-01.md) | Easy | Fast and slow pointers for finding midpoints | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Remove K-th Node From End](exercises/problem-02.md) | Easy/Medium | Fixed-gap runner pointers and dummy head node | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Find Cycle Entrance Value](exercises/problem-03.md) | Medium | Floyd's Tortoise and Hare cycle detection and entrance resolution | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Merge Two Sorted Linked Lists](exercises/problem-04.md) | Medium/Hard | Sentinel node pointer splicing for sorted list combination | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Reorder and Interweave List](exercises/problem-05.md) | Hard | Combining midpoint split, in-place reversal, and alternating merge | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-009
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: Fast and slow pointers (Tortoise and Hare), Cycle detection and loop-start resolution, Finding middle nodes (odd vs. even handling), Fixed-gap runner pointers (k-th from end), Sentinel / dummy node patterns for list merging and mutation*
