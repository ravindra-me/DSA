# Day 24: Sliding Window: Mastering Contiguous Subarray and Substring Problems

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 24 | 2026-11-02 | Core Array Patterns | New topic | progressive | Python 3.12 |

The sliding window technique converts costly nested-loop searches over contiguous subarrays into efficient linear scans. By maintaining state across adjacent overlapping ranges, we add new elements on the right and remove stale elements on the left instead of recalculating from scratch. This lesson establishes the core mental models for both fixed-size and dynamically sized windows.

## Topic

**Sliding Window**: fixed-size window, variable-size window, window invariants, longest/shortest subarray

## Learning Objectives

By the end of this lesson you should be able to:

- Identify when a problem asks for contiguous segments amenable to sliding window instead of general subsets.
- Formulate and implement fixed-size window algorithms that update state in O(1) time per shift.
- Derive dynamic window invariants to compute longest valid and shortest valid contiguous subarrays.
- Integrate auxiliary state data structures (hash maps, frequency tables, counters) to track window validity in amortized O(1) time.
- Analyze amortized two-pointer time complexity to guarantee O(N) runtime.

## Concept Explanation

### What it is

A sliding window is a subsegment of an array or string defined by two pointers, `left` and `right`. Instead of recomputing properties of every possible subsegment from scratch, the window 'slides' across the sequence. When the window expands to the right, we absorb one new element; when it shrinks from the left, we discard one old element. Because consecutive candidate windows share most of their elements, updating the window's summary state (such as sum, maximum, or character frequencies) takes O(1) time per step rather than O(K) or O(N).

### Why it exists

Evaluating all contiguous subarrays of an array of length $N$ requires examining $\frac{N(N+1)}{2} = O(N^2)$ ranges. Computing a function over each range naively takes up to $O(N)$ time, leading to an overall runtime of $O(N^3)$ or $O(N^2)$. The sliding window technique utilizes overlapping sub-problems: range $[i+1, j+1]$ is identical to range $[i, j]$ except element $i$ is removed and element $j+1$ is added. Exploiting this shared state collapses the runtime from $O(N^2)$ to $O(N)$.

### When to use it

Look for these primary signals:
1. The problem specifies a **contiguous** sequence (subarray, substring, subsegment). Sliding window does *not* apply to arbitrary non-contiguous subsequences or subsets.
2. You are asked for an extremum (maximum sum, minimum length, longest sequence) or count of contiguous segments meeting a condition.
3. Monotonicity holds: expanding the window monotonically moves a condition in one direction (e.g., adding positive numbers always increases the sum), or shrinking the window monotonically reverses it.

### When NOT to use it

Do not use sliding window when:
- Elements are not contiguous (subsequences or subsets; consider dynamic programming or sorting instead).
- The sequence contains negative values when trying to maintain sum constraints (e.g., subarray sum equals $K$ with negative numbers breaks monotonicity; use prefix sums with a hash map instead).
- The window state cannot be updated incrementally in $O(1)$ when shrinking (e.g., finding the median of a sliding window requires an order statistic tree or two heaps rather than a basic two-pointer window).

### How it works internally

There are two fundamental paradigms:

1. **Fixed-size window ($K$):**
   - Initialize the window by processing the first $K$ elements.
   - Slide the window rightward from index $K$ to $N-1$.
   - At each step $i$, add `nums[i]` to the window state, subtract `nums[i - K]` from the state, and update the global answer.

2. **Variable-size window:**
   - Initialize `left = 0` and an empty window state.
   - Iterate `right` from $0$ to $N-1$ (expanding phase).
   - Add `nums[right]` to window state.
   - While the window violates the target invariant (or while seeking a minimal valid window), shrink by removing `nums[left]` from the window state and incrementing `left`.
   - Update the global result (e.g., `max_len = max(max_len, right - left + 1)`).

Both pointers only move forward, guaranteeing that each element is added once and removed at most once, achieving amortized $O(N)$ runtime.

### Common mistakes

- Updating window state after changing pointer indices or using the wrong index during removal (e.g., subtracting `nums[right]` instead of `nums[left]`).
- Confusing 'at most $K$' with 'exactly $K$'. To count windows with exactly $K$ distinct elements, compute `at_most(K) - at_most(K - 1)`.
- Failing to clean up empty keys in frequency dictionaries, which can cause `len(freq_map)` to overcount distinct keys with count 0.
- Attempting to use standard variable sliding windows for sum problems containing negative numbers where monotonicity does not hold.
- Off-by-one errors in window length calculations: the length of a window bounded by indices $[L, R]$ inclusive is $R - L + 1$, not $R - L$.

### Real-world applications

- Network rate limiting: tracking API call counts over a rolling 60-second window (sliding window counter algorithm).
- Network packet transmission: TCP sliding window protocol for flow control and packet acknowledgement.
- Real-time audio and signal processing: Short-Time Fourier Transform (STFT) applying overlapping window functions across time-series data.
- Stock market analytics: computing moving averages (SMA, EMA) and volatility over trailing $N$-day windows.

## Example

Let `nums = [2, 1, 5, 1, 3, 2]` and $K = 3$. Find the maximum sum of any contiguous subarray of size 3.

1. **Initial window:** Indices 0 to 2 (`[2, 1, 5]`).
   - Current sum = $2 + 1 + 5 = 8$.
   - `max_sum = 8`.

2. **Slide to index 3 (`nums[3] = 1`):**
   - Add incoming `nums[3]` (1), drop outgoing `nums[3 - 3] = nums[0]` (2).
   - New sum = $8 + 1 - 2 = 7$.
   - `max_sum = max(8, 7) = 8`.

3. **Slide to index 4 (`nums[4] = 3`):**
   - Add incoming `nums[4]` (3), drop outgoing `nums[4 - 3] = nums[1]` (1).
   - New sum = $7 + 3 - 1 = 9$.
   - `max_sum = max(8, 9) = 9`.

4. **Slide to index 5 (`nums[5] = 2`):**
   - Add incoming `nums[5]` (2), drop outgoing `nums[5 - 3] = nums[2]` (5).
   - New sum = $9 + 2 - 5 = 6$.
   - `max_sum = max(9, 6) = 9`.

Result: 9.

## Visual Explanation

```text
Array: [ 2,  1,  5,  1,  3,  2 ]

Step 1: [ 2   1   5 ] 1   3   2     Sum = 8, Max = 8
          L       R

Step 2:   2 [ 1   5   1 ] 3   2     Sum = 8 - 2 + 1 = 7, Max = 8
              L       R

Step 3:   2   1 [ 5   1   3 ] 2     Sum = 7 - 1 + 3 = 9, Max = 9
                  L       R

Step 4:   2   1   5 [ 1   3   2 ]   Sum = 9 - 5 + 2 = 6, Max = 9
                      L       R
```

## Complexity

- **Time Complexity:** O(N): Both `left` and `right` pointers start at index 0 and increment up to N times. Each element is processed (added and removed) at most once.
- **Space Complexity:** O(1) to O(K): O(1) auxiliary space if tracking a numeric aggregation (sum, min, max); up to O(K) or O(U) space where U is the alphabet size when tracking unique item frequencies.

Even though a variable sliding window has a nested `while` loop to shrink the window, the inner loop pointer `left` never resets or moves backward. Thus, across the entire outer loop, `left` advances at most $N$ times. This guarantees amortized $O(1)$ operations per iteration and an overall $O(N)$ execution time.

## Interview Perspective

1. **How do you distinguish whether a problem requires Two Pointers from opposite ends versus a Sliding Window?**
   <details><summary>What a strong answer covers</summary>

   Two pointers moving inward (opposite ends) are typically used on sorted arrays to find pairs or triplets, or when checking palindromes. Sliding window maintains a contiguous subsegment with both pointers moving in the same direction across an array or string.

   </details>
2. **Can sliding window find a subarray with sum equal to K if the array contains negative numbers?**
   <details><summary>What a strong answer covers</summary>

   No. The sliding window relies on monotonicity: expanding increases sum, shrinking decreases sum. Negative numbers break this property because expanding could decrease sum and shrinking could increase it. For negative numbers, use a Prefix Sum combined with a Hash Map.

   </details>
3. **How can you count the number of subarrays with 'exactly K' distinct elements using sliding window?**
   <details><summary>What a strong answer covers</summary>

   Directly maintaining 'exactly K' is difficult because shrinking can immediately invalidate the count without exploring all valid boundaries. Instead, compute `at_most(K) - at_most(K - 1)`. Counting subarrays with 'at most K' elements is monotonic and easy with sliding window (`ans += right - left + 1`).

   </details>
4. **What is the amortized cost argument for the nested while loop in variable sliding windows?**
   <details><summary>What a strong answer covers</summary>

   Explain that `right` advances from $0$ to $N-1$ ($N$ increments) and `left` advances from $0$ to at most $N$ ($N$ increments). Since neither pointer ever decrements, the inner while loop executes at most $N$ times total across the entire execution of the algorithm, yielding $O(N)$ aggregate time.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Maximum Average Subarray I](exercises/problem-01.md) | Easy | fixed-size window | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Minimum Size Subarray Sum](exercises/problem-02.md) | Easy/Medium | variable-size window (shortest subarray) | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Longest Substring Without Repeating Characters](exercises/problem-03.md) | Medium | variable-size window (longest subarray with hash set/map) | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Longest Repeating Character Replacement](exercises/problem-04.md) | Medium/Hard | window invariants with character frequency | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Subarrays with K Different Integers](exercises/problem-05.md) | Hard | exact-K window via at-most reduction | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-024
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: fixed-size window, variable-size window, window invariants, longest subarray pattern, shortest subarray pattern, at-most to exact reduction*
