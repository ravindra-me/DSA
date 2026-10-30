# Day 21: Day 21: Prefix & Suffix Techniques

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 21 | 2026-10-30 | Hashing | New topic | progressive | Python 3.12 |

Repeated range queries over an array often lead to wasteful $O(N)$ scans per query. Prefix and suffix techniques preprocess an array in $O(N)$ time to answer range sum queries in $O(1)$ time, isolate exclusions without division, and perform batch interval updates efficiently. By combining cumulative sums with hash maps, we can also count and locate target subarrays containing arbitrary negative and positive numbers in linear time.

## Topic

**Prefix & Suffix Techniques**: prefix sums, suffix products, subarray sum equals k, 2D prefix sums, difference arrays

## Learning Objectives

By the end of this lesson you should be able to:

- Construct and query 1D prefix sum arrays in $O(1)$ time using 1-based indexing conventions.
- Eliminate division operations using dual prefix and suffix running accumulators.
- Combine prefix sums with hash maps to find subarrays with specific target sums in $O(N)$ time.
- Extend prefix concepts into two dimensions to query arbitrary subgrid sums in $O(1)$ time.
- Use difference arrays to execute range update queries in $O(1)$ time per update and reconstruct the final array in $O(N)$ time.

## Concept Explanation

### What it is

A prefix sum array stores cumulative totals of an input array starting from the beginning up to every index. A suffix technique does the mirror image, accumulating values backwards from the end. By caching these running aggregates, any contiguous subsegment can be computed by taking the difference between two cumulative values rather than iterating through the subsegment. Similarly, a difference array captures step-by-step changes rather than cumulative sums, enabling bulk interval additions in $O(1)$ time.

### Why it exists

Without preprocessing, calculating the sum of $Q$ arbitrary subsegments in an array of length $N$ requires $O(Q \cdot N)$ time. When $N, Q \le 10^5$, an $O(Q \cdot N)$ algorithm requires $10^{10}$ operations and times out. Precomputing prefix sums converts each range query into an $O(1)$ calculation, dropping total time to $O(N + Q)$. Furthermore, problems asking for contiguous subarrays matching a condition can avoid $O(N^2)$ brute force sweeps when framed as $prefix[j] - prefix[i] = \text{target}$.

### When to use it

Use prefix and suffix techniques when dealing with static arrays that require repeated range sum queries, contiguous subarray sum evaluations (especially with negative values where sliding windows fail), problems requiring exclusions of elements without division (e.g. product of array except self), 2D matrix region sums, or offline bulk interval modifications.

### When NOT to use it

Do not use standard prefix sums if the array is frequently updated between range queries; each point update in a naive prefix array takes $O(N)$ time. Instead, use a Binary Indexed Tree (Fenwick Tree) or Segment Tree for dynamic range queries. Also avoid prefix sums when finding non-contiguous subsets (subsequences) where order does not matter and dynamic programming or greedy subset-sum strategies apply.

### How it works internally

1. **1D Prefix Sums**: Build an array `pref` of length $n + 1$ where `pref[0] = 0` and `pref[i] = pref[i - 1] + nums[i - 1]`. The sum of subarray `nums[L..R]` (0-indexed, inclusive) is computed as `pref[R + 1] - pref[L]`.
2. **Prefix-Hash Map Pattern**: To find contiguous subarrays summing to $k$, observe that $\sum_{m=i}^{j} nums[m] = S_j - S_{i-1} = k \iff S_{i-1} = S_j - k$. Maintain a running sum $S$ and a hash map of frequencies of previously observed prefix sums initialized with `{0: 1}`.
3. **2D Prefix Sums**: Build `pref[r][c]` representing the sum of rectangle $(0,0)$ to $(r-1, c-1)$. By Inclusion-Exclusion, `pref[r][c] = matrix[r-1][c-1] + pref[r-1][c] + pref[r][c-1] - pref[r-1][c-1]`. Any subgrid $(r_1, c_1)$ to $(r_2, c_2)$ is evaluated in $O(1)$ via `pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1] + pref[r1][c1]`.
4. **Difference Array**: To apply $+v$ to range $[L, R]$, let `diff[L] += v` and `diff[R + 1] -= v`. Taking the prefix sum of `diff` recovers the updated values in $O(N)$ total time.

### Common mistakes

- Off-by-one errors when defining prefix sums: using 0-based prefix sums without an initial 0 entry requires awkward boundary checks for queries starting at index 0.
- Forgetting to initialize the hash map with `{0: 1}` when counting subarrays with sum $k$, which causes valid subarrays starting at index 0 to be missed.
- Attempting to use two pointers/sliding window for subarray sums when negative numbers are present; sliding window requires monotonicity, whereas prefix sum + hash map handles negatives seamlessly.
- Mixing up row and column indices during 2D inclusion-exclusion operations, or adding the overlapping corner instead of subtracting it during prefix table construction.

### Real-world applications

- Image Processing: Summed-area tables (integral images) calculate box blurs and feature detections in real-time computer vision in $O(1)$ time per window.
- Database Systems: Cumulative metrics, rolling aggregations, and window functions (e.g. `SUM(val) OVER (...)`) rely directly on prefix reduction techniques.
- Telemetry & Booking Engines: Difference arrays determine peak concurrent server loads, overlapping flight bookings, or bandwidth usage across time slots.
- Geographic Information Systems (GIS): Fast querying of population or sensor data within bounding rectangular coordinates.

## Example

Let `nums = [3, 4, -2, 5]` and we want the sum of `nums[1..3]` (`[4, -2, 5]`, which equals 7).

1. Build 1-based prefix sum array of size 5:
- `pref[0] = 0`
- `pref[1] = pref[0] + nums[0] = 0 + 3 = 3`
- `pref[2] = pref[1] + nums[1] = 3 + 4 = 7`
- `pref[3] = pref[2] + nums[2] = 7 + (-2) = 5`
- `pref[4] = pref[3] + nums[3] = 5 + 5 = 10`
`pref = [0, 3, 7, 5, 10]`

2. Query `nums[1..3]` (where $L=1, R=3$):
`sum = pref[R + 1] - pref[L] = pref[4] - pref[1] = 10 - 3 = 7`.
Calculation completes in $O(1)$ without touching individual elements.

## Visual Explanation

```text
1D Prefix Sum Subarray Extraction:

Index i:      0     1     2     3
nums:      [  3,    4,   -2,    5 ]

Prefix:    [  0,    3,    7,    5,   10 ]
pref idx:     0     1     2     3     4
                    ^                 ^
                 pref[L]           pref[R+1]

Subarray [1..3] sum = pref[4] - pref[1] = 10 - 3 = 7
---------------------------------------------------------------
2D Prefix Sum (Inclusion-Exclusion):

+---------+---------+          Query rectangle: D
|    A    |    B    |          Sum(D) = Total(A+B+C+D)
+---------+---------+                 - Area(A+B)
|    C    |    D    |                 - Area(A+C)
+---------+---------+                 + Area(A)  (added back because subtracted twice)
```

## Complexity

- **Time Complexity:** Preprocessing 1D or 2D prefix sums: $O(N)$ or $O(R \cdot C)$ where every element is visited once. Range Query: $O(1)$ arithmetic operations. Difference array reconstruction: $O(N)$ cumulative sum pass.
- **Space Complexity:** $O(N)$ extra space to store 1D prefix arrays or difference arrays; $O(R \cdot C)$ for 2D prefix grids. Can be done in $O(1)$ auxiliary space if modifying the input in-place.

Hash map prefix sum lookups have an average-case time complexity of $O(1)$ per element, leading to $O(N)$ overall time and $O(N)$ space. Integer overflow must be accounted for in languages with fixed-width integers, though Python handles arbitrarily large integers automatically.

## Interview Perspective

1. **Why can't we use a two-pointer sliding window to find a subarray summing to k if the array contains negative numbers?**
   <details><summary>What a strong answer covers</summary>

   A sliding window depends on monotonicity: expanding the right pointer must strictly increase (or keep equal) the window sum, and contracting the left pointer must decrease it. With negative numbers, adding an element might decrease the sum, destroying this property. A prefix sum combined with a hash map must be used instead because it checks algebraic differences independent of monotonicity.

   </details>
2. **How do you handle 2D prefix sums without introducing off-by-one boundary checks for the first row and column?**
   <details><summary>What a strong answer covers</summary>

   Pad the prefix grid with an extra row and column of zeros at index 0 (dimensions $(R+1) \times (C+1)$). The matrix coordinate $(r, c)$ maps to prefix index $(r+1, c+1)$, which guarantees that accessing $r-1$ or $c-1$ never falls out of bounds.

   </details>
3. **What is the difference between a prefix sum array and a difference array?**
   <details><summary>What a strong answer covers</summary>

   They are dual inverses of each other. A prefix sum turns $O(N)$ range queries into $O(1)$ after $O(N)$ preprocessing on a static array. A difference array turns $O(N)$ range updates into $O(1)$ endpoint operations, requiring an $O(N)$ prefix sum sweep at the end to materialize the final values.

   </details>
4. **How would you solve the range sum query problem if values were constantly being updated between queries?**
   <details><summary>What a strong answer covers</summary>

   Standard prefix sum arrays require $O(N)$ time per point update. When updates and queries interleave dynamically, a Binary Indexed Tree (Fenwick Tree) or Segment Tree provides $O(\log N)$ updates and $O(\log N)$ queries.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Immutable Range Sum Query](exercises/problem-01.md) | Easy | 1D Prefix Sum | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Product of Array Except Self](exercises/problem-02.md) | Easy/Medium | Prefix-Suffix Accumulation | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Subarray Sum Equals K](exercises/problem-03.md) | Medium | Prefix Sum with Hash Map | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [2D Matrix Block Sum Queries](exercises/problem-04.md) | Medium/Hard | 2D Prefix Sum (Integral Image) | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Corporate Flight Bookings](exercises/problem-05.md) | Hard | Difference Array | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-021
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: 1D Prefix Sum, Prefix-Suffix Accumulation, Prefix Sum with Hash Map, 2D Prefix Sum (Integral Image), Difference Array*
