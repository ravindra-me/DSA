# Day 13: Day 13: Queues, Circular Buffers, and the Producer-Consumer Pattern

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 13 | 2026-10-22 | Linear Data Structures | New topic | progressive | Python 3.12 |

While stacks enforce Last-In, First-Out (LIFO), many computing systems require fairness and ordering where tasks are handled in the exact sequence they arrive. A **Queue** enforces First-In, First-Out (FIFO) semantics, serving as the foundational synchronization mechanism for scheduling, buffering, and breadth-first search. In this lesson, we explore queue mechanics, array-based circular buffers, queue emulation via stacks, and classic queue patterns.

## Topic

**Queue**: FIFO, circular queue, queue via two stacks, producer/consumer

## Learning Objectives

By the end of this lesson you should be able to:

- Differentiate FIFO behavior from LIFO behavior and identify when FIFO ordering is required.
- Implement an efficient, fixed-capacity circular queue using modular arithmetic to prevent array shifting.
- Emulate a queue using two stacks and analyze the amortized $O(1)$ cost of enqueue and dequeue operations.
- Model rate-limiting and producer-consumer buffering using sliding time windows and queue state machines.

## Concept Explanation

### What it is

A Queue is a linear data structure that operates on a **First-In, First-Out (FIFO)** discipline. Imagine a line of customers waiting at a grocery store checkout: the first person to join the line is the first person served. Adding an element is known as **enqueue** (appended at the back or *tail*), and removing an element is known as **dequeue** (extracted from the front or *head*).

### Why it exists

Using a standard dynamic array (like Python's `list`) as a FIFO queue by calling `.append()` and `.pop(0)` is disastrous for performance. Removing the first element of an array requires shifting every subsequent element left by one position, leading to an $O(n)$ cost per dequeue. In systems processing millions of events, this turns an $O(N)$ pipeline into an unviable $O(N^2)$ bottleneck. Queues provide true $O(1)$ operations at both ends.

### When to use it

Use a queue when:
- Elements must be processed in the exact temporal order they were received (fairness).
- You are decoupling producers generating data from consumers processing data at varying speeds (buffering).
- Traversing trees or graphs level-by-level (Breadth-First Search, introduced later).
- Maintaining a rolling window of recent events indexed by timestamp.

### When NOT to use it

Do not use a basic queue if:
- You need to access elements by arbitrary indices or search for items quickly (use an array or hash map; queues require $O(n)$ scan).
- Newer items must take precedence over older items (use a Stack).
- Items have varying priorities rather than strict arrival ordering (use a Priority Queue / Heap).

### How it works internally

There are three primary implementations of a queue:
1. **Singly Linked List with Head and Tail Pointers**: Enqueue appends to `tail.next` and advances `tail`. Dequeue captures `head.val` and advances `head`. Both run in $O(1)$ time without resizing overhead.
2. **Circular Buffer (Array-based Queue)**: A fixed-size array of capacity $C$ with two pointers `head` and `tail`. Advancing a pointer wraps around using modulo arithmetic: `idx = (idx + 1) % C`. An explicit `size` counter distinguishes between an empty queue (`size == 0`) and a full queue (`size == C`).
3. **Two Stacks (`in_stack` and `out_stack`)**: Enqueue pushes onto `in_stack`. Dequeue checks `out_stack`; if empty, it pops all elements from `in_stack` and pushes them onto `out_stack`, reversing their order to restore FIFO ordering. Each element is pushed twice and popped twice, yielding an amortized cost of $O(1)$ per operation.

### Common mistakes

- Using `list.pop(0)` in Python: this is an $O(n)$ operation because all remaining elements shift left. Use `collections.deque` or a pointer-based structure.
- Circular buffer pointer ambiguity: conflating `head == tail` as both 'full' and 'empty'. Always track a separate `size` counter or reserve one slot as a sentinel.
- Off-by-one errors in modulo operations: forgetting that array indices run from `0` to `capacity - 1`, leading to index-out-of-bounds errors before wrapping.
- Prematurely transferring elements between stacks in a two-stack queue: transferring `in_stack` to `out_stack` on every dequeue ruins the amortized $O(1)$ guarantee. Only transfer when `out_stack` is completely empty.

### Real-world applications

- Operating System CPU Scheduling: Round-robin schedulers maintain a queue of ready processes, allocating time slices in FIFO sequence.
- Asynchronous Message Brokers: Systems like RabbitMQ, Apache Kafka, and Amazon SQS buffer events between microservices.
- Print Spoolers: Print jobs submitted by multiple network clients are queued and printed in the sequence received.
- Network Packet Buffers: Network switches and routers buffer incoming Ethernet frames or IP packets before forwarding them across saturated links.

## Example

Let's trace a **Circular Queue** of capacity 3.

1. Initial state: `buffer = [None, None, None]`, `head = 0`, `tail = 0`, `size = 0`.
2. `enqueue('A')`: write to `buffer[tail]` -> `buffer[0] = 'A'`. Update `tail = (0 + 1) % 3 = 1`, `size = 1`.
3. `enqueue('B')`: write to `buffer[1] = 'B'`. Update `tail = (1 + 1) % 3 = 2`, `size = 2`.
4. `dequeue()`: read `buffer[head]` -> `'A'`. Clear slot (optional) and update `head = (0 + 1) % 3 = 1`, `size = 1`.
5. `enqueue('C')`: write to `buffer[2] = 'C'`. Update `tail = (2 + 1) % 3 = 0`, `size = 2` (wrapped around!).
6. `enqueue('D')`: write to `buffer[0] = 'D'`. Update `tail = (0 + 1) % 3 = 1`, `size = 3` (now full).
7. `is_full()` returns `True`. Any further `enqueue` fails until another `dequeue` frees space.

## Visual Explanation

```text
Circular Buffer of Capacity 4:

1. Enqueue A, B, C:
   Indices:   [  0  |  1  |  2  |  3  ]
   Buffer:    [ 'A' | 'B' | 'C' |  .  ]
                ^                 ^
               head              tail     (size = 3)

2. Dequeue -> returns 'A':
   Indices:   [  0  |  1  |  2  |  3  ]
   Buffer:    [  .  | 'B' | 'C' |  .  ]
                      ^           ^
                     head        tail     (size = 2)

3. Enqueue D, E (wraps around to index 0):
   Indices:   [  0  |  1  |  2  |  3  ]
   Buffer:    [ 'E' | 'B' | 'C' | 'D' ]
                      ^     
                   head, tail             (size = 4, FULL)
```

## Complexity

- **Time Complexity:** Enqueue: O(1) amortized/worst-case appending to back. Dequeue: O(1) popping from front. Peek/Front: O(1) direct inspection.
- **Space Complexity:** O(k) where k is the maximum number of simultaneous elements held in the queue.

In a dynamic queue or Python's `collections.deque` (implemented as a doubly linked list of blocks), enqueue and dequeue are strictly $O(1)$. In a two-stack queue, individual dequeue operations can take $O(n)$ in the worst case when transferring elements, but every element is pushed and popped at most twice, guaranteeing an amortized $O(1)$ complexity over any sequence of operations.

## Interview Perspective

1. **Why does Python's standard `list` perform poorly when used as a queue, and what does `collections.deque` do differently?**
   <details><summary>What a strong answer covers</summary>

   Explain that `list.pop(0)` is $O(n)$ because contiguous memory requires shifting all remaining elements. Contrast this with `collections.deque`, which uses a doubly-linked list of fixed-size contiguous memory blocks (chunks), offering $O(1)$ push and pop operations from both ends without mass data movement.

   </details>
2. **How do you distinguish between an empty queue and a full queue in a circular buffer without a size variable?**
   <details><summary>What a strong answer covers</summary>

   Mention either: 1) Reserving one slot as a sentinel (a buffer of capacity $N$ can only hold $N-1$ elements; empty is `head == tail`, full is `(tail + 1) % N == head`), or 2) Maintaining a boolean flag that tracks the last operation performed (enqueue vs dequeue).

   </details>
3. **Can you implement a queue using two stacks? What is the time complexity of the enqueue and dequeue operations?**
   <details><summary>What a strong answer covers</summary>

   Detail the two-stack architecture (`in_stack` and `out_stack`). Explain that enqueue pushes to `in_stack` ($O(1)$), while dequeue pops from `out_stack`. If `out_stack` is empty, elements are transferred from `in_stack` to `out_stack`. Even though a single dequeue might take $O(n)$, each element is moved at most three times across its lifetime, resulting in amortized $O(1)$.

   </details>
4. **How does a bounded queue help prevent cascading failures in distributed producer-consumer architectures?**
   <details><summary>What a strong answer covers</summary>

   Discuss backpressure: an unbounded queue will consume all available system memory if producers outpace consumers, causing Out-Of-Memory (OOM) crashes. A bounded queue forces producers to either block, reject (shed load), or drop old events, keeping memory consumption bounded and deterministic.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Design Circular Queue](exercises/problem-01.md) | Easy | Fixed-capacity circular buffer with modular arithmetic | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Implement Queue using Stacks](exercises/problem-02.md) | Easy/Medium | Emulating FIFO behavior using two LIFO stacks | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Recent Calls Rate Limiter](exercises/problem-03.md) | Medium | Sliding window time-series queue | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Predict the Winner of the Assembly](exercises/problem-04.md) | Medium/Hard | Round-robin queue simulation with priority/elimination dynamics | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Bounded Producer-Consumer Buffer Simulator](exercises/problem-05.md) | Hard | Bounded queue simulation with buffer overflow shedding and consumer latency | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-013
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: FIFO principle, Circular buffer (circular queue), Modular arithmetic wrap-around, Two-stack queue and amortized analysis, Bounded queues and backpressure, Sliding-window time queues*
