# Day 38: Day 38: Queue Revision & Advanced Patterns

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 38 | 2026-11-16 | Linear Data Structures | Revision (stage 2) | progressive | Python 3.12 |

> **Revision day.** You first studied this topic earlier; today recaps the essentials and gives you brand-new problems. (spaced revision due on day 20 of 'queue' (learned on day 13))

In this revision lesson, we revisit the queue data structure through advanced structural invariants and integration with other algorithmic techniques. We explore memory-efficient ring buffers, amortized cost analysis across two stacks, batch-processing producer-consumer dynamics, and state-space exploration.

## Topic

**Queue**: FIFO, circular queue, queue via two stacks, producer/consumer

## Learning Objectives

By the end of this lesson you should be able to:

- Master the invariant tracking of circular buffers and two-stack queue adaptations under dynamic conditions.
- Formulate and evaluate amortized cost guarantees using the aggregate and accounting methods.
- Apply FIFO state machines to multi-producer/multi-consumer dispatch and batching problems.
- Combine queue semantics with hashing, frequency counts, and sliding windows to solve composite interview problems.

## Concept Explanation

### What it is

A queue is an ordered linear collection obeying the First-In, First-Out (FIFO) principle: elements enter at the rear (enqueue) and exit from the front (dequeue). In physical arrays, dynamic circular indexing (`(index + 1) % capacity`) transforms a fixed slice of contiguous memory into an infinite FIFO stream without shifting elements.

### Why it exists

Naively using dynamic arrays (such as Python's `list.pop(0)`) requires shifting every remaining item leftwards, yielding $O(N)$ dequeue operations and degrading queue-heavy workloads to $O(N^2)$. Fixed-size circular queues and doubly linked nodes preserve strictly $O(1)$ enqueue and dequeue times while avoiding memory fragmentation.

### When to use it

Use a queue when element ordering must strictly preserve chronological arrival, when implementing breadth-first step-by-step frontier expansions, or when decoupling asynchronously producing and consuming entities with bounded latency.

### When NOT to use it

Do not use a standard FIFO queue when high-priority tasks must jump the line (use a priority queue/heap), when elements must be accessed or modified by arbitrary index (use an array or hash map), or when inspection needs to occur from both ends with equal frequency (use a deque).

### How it works internally

1. **Circular Queue Invariant:** A fixed-size backing array of size $C$ maintains `head`, `tail` (or `head` and `size`). New items write to `arr[tail]`, advancing `tail = (tail + 1) % C`. Deletions read from `arr[head]`, advancing `head = (head + 1) % C`. Tracking explicit `size` eliminates ambiguity between empty and full states.
2. **Two-Stack Invariant:** Stack $A$ acts as the inbox; Stack $B$ acts as the outbox. An enqueue pushes to $A$. A dequeue pops from $B$; if $B$ is empty, all elements from $A$ are transferred to $B$ sequentially, reversing their order and restoring FIFO discipline.
3. **Amortization:** Each element enters $A$ once, moves to $B$ at most once, and departs $B$ once—guaranteeing 3 operations per item, or strictly $O(1)$ amortized cost.

### Common mistakes

- Using `list.pop(0)` in Python instead of `collections.deque.popleft()` or explicit circular pointers, leading to $O(N)$ operations.
- Conflating `head == tail` as both 'empty' and 'full' in circular queues without maintaining an explicit `size` counter or leaving a sentinel slot.
- Prematurely transferring elements between stacks in a two-stack queue during enqueue rather than deferring the reversal lazily until a dequeue occurs.
- Modifying queue elements in-place while another reference relies on FIFO ordering.

### Real-world applications

- Operating system thread schedulers and interrupt request (IRQ) dispatch queues.
- Asynchronous message brokers and task workers (e.g., RabbitMQ, Celery, AWS SQS).
- Network router packet buffers managing TCP/UDP ingress under load congestion.
- Print spoolers and hardware peripheral command streams.

## Example

Tracing lazy two-stack queue transfers:

1. Operations: `enqueue(1)`, `enqueue(2)`, `dequeue()`, `enqueue(3)`, `dequeue()`
2. `enqueue(1)`: `in_stack = [1]`, `out_stack = []`
3. `enqueue(2)`: `in_stack = [1, 2]`, `out_stack = []`
4. `dequeue()`: `out_stack` is empty, pop all from `in_stack` to `out_stack`.
   - Pop `2` -> push to `out_stack`: `[2]`
   - Pop `1` -> push to `out_stack`: `[2, 1]`
   - Pop `out_stack` top (`1`). Returns `1`. State: `in_stack = []`, `out_stack = [2]`
5. `enqueue(3)`: `in_stack = [3]`, `out_stack = [2]`
6. `dequeue()`: `out_stack` is not empty! Pop `out_stack` top (`2`). Returns `2` without touching `in_stack`. State: `in_stack = [3]`, `out_stack = []`.

## Visual Explanation

```text
Circular Buffer of Capacity 5 (size = 3):

Index:   0     1     2     3     4
Array: [ _  , 'B', 'C', 'D',  _  ]
              ^           ^
             head        tail (next insertion at index 4)

Two-Stack Queue Mechanics:
  ENQUEUE: push to In-Stack     DEQUEUE: pop from Out-Stack (lazy transfer if empty)

  +---+                       +---+
  | 3 |                       | 1 |  --> pop returns 1
  +---+                       +---+
  | 2 |                       | 2 |
  +---+                       +---+
  In-Stack                    Out-Stack
```

## Complexity

- **Time Complexity:** Enqueue: O(1) worst-case (circular buffer) or O(1) amortized (two-stack / dynamic array). Dequeue: O(1) worst-case (circular buffer) or O(1) amortized (two-stack). Peek: O(1) in all implementations.
- **Space Complexity:** O(N) where N is the maximum number of simultaneous items residing in the queue.

While linked-list-based queues offer strict worst-case O(1) operations, contiguous circular arrays provide vastly superior cache locality and lower memory overhead by eliminating node pointer metadata.

## Interview Perspective

1. **Why does a two-stack queue achieve amortized O(1) dequeue even though an individual dequeue can take O(N) time?**
   <details><summary>What a strong answer covers</summary>

   Explain the aggregate or potential method: every element is pushed to in-stack once, popped once and pushed to out-stack once during transfer, and popped from out-stack once. Across the lifetime of N items, exactly 4N stack operations happen, making the average cost per item O(1).

   </details>
2. **How do you distinguish between 'full' and 'empty' conditions in a circular queue implemented via a fixed-size raw array without an auxiliary count variable?**
   <details><summary>What a strong answer covers</summary>

   Either allocate an array of capacity C + 1 where one slot remains unused (empty: head == tail; full: (tail + 1) % (C + 1) == head), or track a boolean flag indicating whether the last operation was an enqueue or dequeue.

   </details>
3. **In a multithreaded producer-consumer queue, how do you prevent busy-waiting when the queue is empty or full?**
   <details><summary>What a strong answer covers</summary>

   Use condition variables or semaphores (e.g., `not_empty` and `not_full` monitors) to put consumer threads to sleep when the buffer is empty, waking them via signal/notify only when a producer enqueues data.

   </details>
4. **When would you prefer an array-based circular queue over a doubly linked list queue in high-performance production systems?**
   <details><summary>What a strong answer covers</summary>

   Array buffers have fixed memory footprints, zero runtime allocations/deallocations (preventing GC pauses or heap fragmentation), and optimal CPU cache line prefetching.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [First Unique Character in Dynamic Stream](exercises/problem-01.md) | Easy/Medium | FIFO queue with frequency counting for streaming order preservation | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [FIFO Task Batcher with Capacity and Timeout](exercises/problem-02.md) | Medium | Queue batch aggregation with timestamp and capacity flushing | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Circular Buffer with Overwrite and Range Read](exercises/problem-03.md) | Medium/Hard | Fixed-capacity circular buffer with overwrite eviction and historical reading | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Card Deck Revealing Order](exercises/problem-04.md) | Medium/Hard | Simulating reverse FIFO transformations using queue state transitions | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Shortest Path in Grid with Obstacle Elimination Budget](exercises/problem-05.md) | Hard | Multi-dimensional state exploration using FIFO BFS queue | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-038
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: FIFO semantics, Circular buffer indices, Amortized analysis via two stacks, Batch processing and rate-limiting queues, State serialization and tracking*
