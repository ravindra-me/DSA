# Day 15: Deque & Monotonic Queue

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 15 | 2026-10-24 | Linear Data Structures | New topic | progressive | Python 3.12 |

A deque (double-ended queue) generalizes both stacks and queues by supporting constant-time additions and removals at both ends. When combined with monotonicity invariants, deques power the Monotonic Queue pattern—an essential tool for computing sliding window extrema in linear time instead of quadratic or logarithmic time.

## Topic

**Deque & Monotonic Queue**: double-ended operations, sliding window maximum, monotonic deque, palindrome checking

## Learning Objectives

By the end of this lesson you should be able to:

- Understand the deque abstraction, its underlying implementations, and standard double-ended operations.
- Implement two-pointer and double-ended algorithms such as palindrome validation and sliding buffer tracking.
- Master the Monotonic Queue pattern to maintain order invariants across dynamic sliding windows.
- Analyze amortized $O(1)$ operations in monotonic structures through aggregate push/pop accounting.

## Concept Explanation

### What it is

A **deque** (pronounced 'deck', short for *double-ended queue*) is a sequential container allowing $O(1)$ insertions and deletions at both the front and the back. While standard stacks restrict access to one end (LIFO) and standard queues enforce FIFO ordering from back to front, a deque grants full access to both ends.

A **Monotonic Queue** is not a different physical data structure, but rather an *algorithmic technique* implemented using a deque. It maintains elements in strictly increasing or decreasing order. As elements enter and leave a sliding window, elements that can never become the optimal answer (e.g., smaller elements arriving before larger elements in a maximum query) are pruned from the back, while expired elements slide out from the front.

### Why it exists

Consider finding the maximum value in every contiguous window of size $k$ across an array of length $n$. 
- A naive scan takes $O(k)$ per window, totaling $O(n \cdot k)$ time (which degrades to $O(n^2)$ when $k \approx n/2$).
- A balanced BST or a max-heap with lazy deletion achieves $O(n \log k)$ time, which is better but carries non-trivial overhead.

The monotonic queue achieves an optimal $O(n)$ total time ($O(1)$ amortized per element). It avoids redundant checks by maintaining the invariant: *if element $y$ is newer than element $x$ and $y \ge x$, $x$ can never be the maximum of any current or future window containing $y$*. Thus, $x$ can be discarded immediately.

### When to use it

Look for these triggers:
- Sliding window queries requiring the running minimum, maximum, or optimal value within a fixed or variable-length range $[i - k + 1, i]$.
- Tracking recent history where elements expire after a certain lifetime or index delta.
- Dynamic programming state optimization (e.g., $dp[i] = \max_{j \in [i-k, i-1]} (dp[j] + \text{cost})$), where the transition depends on a range extremum.
- Symmetrical manipulation where data needs to be inspected or peeled from both ends simultaneously (e.g., palindrome validation, reordering).

### When NOT to use it

Do not reach for a monotonic queue when:
- Arbitrary random-access indexing or arbitrary insertions into the middle are required (use balanced search trees or arrays).
- The window is not strictly contiguous or moves arbitrarily forward and backward (monotonic queues rely on the sliding window moving forward unidirectionally).
- Queries require sum or count rather than extrema (a simple running prefix sum or hash map suffices in $O(1)$).

### How it works internally

In Python, `collections.deque` is implemented as a doubly linked list of fixed-size blocks (providing $O(1)$ appends and pops on either side).

To implement a **Monotonic Decreasing Deque** (for sliding window maximum):
1. **Index tracking**: Store array *indices* in the deque rather than raw values, so you can check both values and window expiration.
2. **Evict expired elements (Front)**: If `deque[0] <= current_index - k`, pop from the left because that element has exited the sliding window.
3. **Maintain monotonicity (Back)**: While the deque is non-empty and `nums[deque[-1]] <= nums[current_index]`, pop from the right. The incoming value dominates older, smaller values.
4. **Insert**: Push `current_index` to the back.
5. **Query**: The index at `deque[0]` represents the maximum element for the current window.

### Common mistakes

- Storing only values instead of indices in the deque, making it impossible or cumbersome to detect when an element has fallen out of the sliding window.
- Using a Python `list` as a queue or deque: `list.pop(0)` and `list.insert(0, val)` are $O(n)$ operations, leading to hidden quadratic time complexity.
- Incorrect inequality comparison when popping from the back (e.g., using `<` instead of `<=` or vice versa), which may retain duplicate elements unnecessarily or drop valid ties.
- Miscalculating when the first window becomes valid (e.g., recording results before index $k - 1$).
- Forgetting that amortized $O(1)$ requires each index to be pushed at most once and popped at most once.

### Real-world applications

- Sliding window rate limiters (e.g., leaky/token bucket variants tracking request timestamps within rolling time windows).
- Stock market real-time ticker feeds computing rolling highs and lows over 5-minute or 1-hour intervals.
- Audio digital signal processing (DSP) for dynamic range compression and rolling peak-meter calculations.
- Browser navigation and undo/redo histories with fixed maximum buffer sizes.

## Example

### Worked Example: Sliding Window Maximum

Given `nums = [1, 3, -1, -3, 5, 3, 6, 7]`, $k = 3$.
We maintain a monotonic decreasing deque of **indices**.

- **Index 0 (`val=1`)**: Deque is empty. Push `0`. Deque: `[0]`.
- **Index 1 (`val=3`)**: `nums[1] (3) > nums[0] (1)`. Pop `0`. Push `1`. Deque: `[1]`.
- **Index 2 (`val=-1`)**: `nums[2] (-1) < nums[1] (3)`. Push `2`. Deque: `[1, 2]`. Window $[0..2]$ complete. Max is `nums[deque[0]] = nums[1] = 3`.
- **Index 3 (`val=-3`)**: Push `3`. Deque: `[1, 2, 3]`. Window $[1..3]$ complete. Max is `nums[1] = 3`.
- **Index 4 (`val=5`)**: Expired? `deque[0] == 1 <= 4 - 3 = 1` -> Pop left (`1`). Now check back: `5 > -3` (pop `3`), `5 > -1` (pop `2`). Push `4`. Deque: `[4]`. Window $[2..4]$ complete. Max is `nums[4] = 5`.
- **Index 5 (`val=3`)**: Push `5`. Deque: `[4, 5]`. Window $[3..5]$ complete. Max is `nums[4] = 5`.
- **Index 6 (`val=6`)**: `6 > nums[5] (3)` (pop `5`), `6 > nums[4] (5)` (pop `4`). Push `6`. Deque: `[6]`. Window $[4..6]$ complete. Max is `nums[6] = 6`.
- **Index 7 (`val=7`)**: `7 > nums[6] (6)` (pop `6`). Push `7`. Deque: `[7]`. Window $[5..7]$ complete. Max is `nums[7] = 7`.

Final Output: `[3, 3, 5, 5, 6, 7]`.

## Visual Explanation

```text
Incoming array: [1, 3, -1, -3, 5] | Window size k = 3

Step 1 (i=0, val=1):  Deque: [idx 0 (1)]
Step 2 (i=1, val=3):  3 > 1 -> pop 0.
                      Deque: [idx 1 (3)]
Step 3 (i=2, val=-1): -1 < 3 -> push 2.
                      Deque: [idx 1 (3), idx 2 (-1)]
                      Window [1, 3, -1] -> Max = nums[deque[front]] = 3

Step 4 (i=3, val=-3): -3 < -1 -> push 3.
                      Deque: [idx 1 (3), idx 2 (-1), idx 3 (-3)]
                      Window [3, -1, -3] -> Max = nums[deque[front]] = 3

Step 5 (i=4, val=5):  Expired check: idx 1 <= 4 - 3 -> pop front (1).
                      Pop back: 5 > -3 (pop 3), 5 > -1 (pop 2).
                      Push 4.
                      Deque: [idx 4 (5)]
                      Window [-1, -3, 5] -> Max = nums[deque[front]] = 5
```

## Complexity

- **Time Complexity:** Deque append/popleft/pop/appendleft: O(1). Sliding Window Max: O(n) total because each index enters the deque exactly once and is removed at most once.
- **Space Complexity:** O(k) auxiliary space, where k is the window size, as the deque stores at most k indices at any point.

Even though a single step might pop multiple elements in a `while` loop (taking up to $O(k)$ steps in a single iteration), the amortized cost per element is $O(1)$ across all $n$ iterations.

## Interview Perspective

1. **Why should we store indices rather than values in the monotonic deque during sliding window problems?**
   <details><summary>What a strong answer covers</summary>

   Indices allow constant-time verification of whether an element has slipped outside the active window boundary (`deque[0] <= i - k`). We can always retrieve the value from `nums[index]`, but recovering the original window position from just a raw value is ambiguous when duplicates exist.

   </details>
2. **How does a Monotonic Queue differ from a Monotonic Stack?**
   <details><summary>What a strong answer covers</summary>

   A monotonic stack operates strictly on one end (LIFO) and is ideal for finding the next or previous greater/smaller element across an unbounded sequence. A monotonic queue operates on both ends (FIFO + LIFO pruning) and is ideal for sliding ranges where the oldest elements must expire from the front while non-optimal elements are purged from the back.

   </details>
3. **Could we use a Heap (Priority Queue) instead of a Monotonic Queue for sliding window maximum? What is the trade-off?**
   <details><summary>What a strong answer covers</summary>

   Yes, with lazy deletion: elements stay in the heap until they appear at the root and are out-of-bounds. However, the time complexity is $O(n \log n)$ (or $O(n \log k)$ if heap elements are actively removed), whereas the monotonic queue is strictly $O(n)$ with lower constant factors.

   </details>
4. **How does `collections.deque` achieve $O(1)$ operations on both ends in Python compared to a standard `list`?**
   <details><summary>What a strong answer covers</summary>

   A Python `list` is a contiguous dynamic array, so deleting or inserting at index 0 shifts all $n$ elements ($O(n)$). In contrast, `collections.deque` is structured as a doubly linked list of fixed-size contiguous blocks (chunks of 64 elements), allowing pointer updates at either end in $O(1)$.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Validate Deque Palindrome](exercises/problem-01.md) | Easy | Double-ended queue operations | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Recent Calls Counter](exercises/problem-02.md) | Easy/Medium | Fixed time-window eviction using deque | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Sliding Window Maximum](exercises/problem-03.md) | Medium | Monotonic Decreasing Deque | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Longest Continuous Subarray With Absolute Diff <= Limit](exercises/problem-04.md) | Medium/Hard | Dual Monotonic Deques (Min & Max) | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Shortest Subarray with Sum at Least K](exercises/problem-05.md) | Hard | Prefix Sums with Monotonic Queue Optimization | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-015
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: collections.deque, Double-ended operations, Monotonic Deque, Sliding Window Extrema, Amortized O(1) analysis*
