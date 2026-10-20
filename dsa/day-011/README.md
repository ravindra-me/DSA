# Day 11: Arrays Mastery: Invariants, Reorganizations, and Matrix Manipulations

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 11 | 2026-10-20 | Fundamentals | Revision (stage 1) | progressive | Python 3.12 |

> **Revision day.** You first studied this topic earlier; today recaps the essentials and gives you brand-new problems. (spaced revision due on day 9 of 'arrays' (learned on day 2))

This revision deepens your mastery of arrays by transitioning from basic indexing to advanced array invariants, boundary controls, and multi-dimensional coordinate projections. We combine arrays with stacks, two-pointer invariants, and prefix calculations to solve complex transformation problems in optimal space and time.

## Topic

**Arrays**: indexing, traversal, in-place updates, dynamic arrays, 2D arrays

## Learning Objectives

By the end of this lesson you should be able to:

- Leverage array invariants to perform complex in-place data transformations without supplementary memory allocations.
- Manipulate 2D grids via coordinate mappings, in-place diagonal/transposition sweeps, and boundary shrinkage.
- Formulate prefix/suffix accumulations and combine them with dynamic arrays to achieve optimal O(N) runtimes.
- Apply monotonic stack techniques over array indices to resolve complex range-extrema challenges.

## Concept Explanation

### What it is

An array is a contiguous block of allocated memory holding elements of uniform size (or references to objects), accessible in O(1) time via base address offset calculation: `Address(i) = Base + i * ElementSize`. In dynamic arrays (such as Python's `list`), this contiguous memory buffer dynamically resizes via geometric reallocation amortizing append operations to O(1).

### Why it exists

Without contiguous memory allocation, CPU data caches cannot exploit spatial locality, leading to significant cache misses when traversing sequences. Dynamic arrays balance random-access performance with the flexibility of non-fixed collections.

### When to use it

Use arrays when you need instantaneous random access by index, sequential iteration benefiting from CPU prefetching, cache-efficient operations, or when performing in-place rearrangements without extra memory overhead.

### When NOT to use it

Avoid basic arrays when you require frequent arbitrary insertions or deletions in the middle of large sequences (which cost O(N) due to element shifting; use balanced trees or linked nodes instead) or when maintaining sparse, high-dimensional matrices where hash maps or coordinate lists conserve memory.

### How it works internally

Array operations maintain explicit structural invariants:
1. **Index Alignment**: Element `A[i]` is stored adjacent to `A[i-1]` and `A[i+1]`.
2. **In-place Two-Pointer Invariants**: Two indices scan the array (either bidirectionally from extremes or simultaneously from the start) partitioning the sequence into processed and unprocessed segments.
3. **Amortized Resizing**: A dynamic array with capacity `C` doubles or expands by a growth factor (e.g., ~1.125x in CPython) when full, ensuring that $N$ sequential appends cost $O(N)$ total time ($O(1)$ amortized per append).
4. **2D Row-Major Layout**: In 2D arrays of dimensions $R \times C$, element $(r, c)$ maps linearly to index $r \times C + c$.

### Common mistakes

- Mutating an array's length while iterating forward across its indices, which causes skipped elements or out-of-range index traps.
- Allocating 2D arrays via shallow row replication (e.g., `[[0] * c] * r`), causing every row to reference the exact same memory instance.
- Misidentifying amortized $O(1)$ dynamic array appends as worst-case $O(1)$, which can be catastrophic in hard real-time latency-sensitive systems.
- Off-by-one errors during nested 2D matrix rotations, boundary shrinks, or prefix calculation offsets.

### Real-world applications

- Memory buffers and framebuffers in graphics pipelines for direct pixel manipulation.
- Relational database query engines evaluating columnar data blocks via SIMD vectorization.
- CPython list implementation (`PyListObject`), managing dynamic arrays of PyObject pointers.
- Operating system page tables indexing physical memory frames.

## Example

Consider partitioning an array into two sections: evens before odds in-place.

Input: `nums = [3, 2, 4, 1, 5, 6]`
- Initialize two pointers: `left = 0` (boundary for even items), `right = len(nums) - 1` (boundary for odd items).
- While `left < right`:
  1. If `nums[left] % 2 == 0`, increment `left`.
  2. Else if `nums[right] % 2 != 0`, decrement `right`.
  3. Else, swap `nums[left]` and `nums[right]`, then advance both.

Trace:
- `left=0` (val 3, odd), `right=5` (val 6, even) -> Swap: `[6, 2, 4, 1, 5, 3]`, `left=1`, `right=4`.
- `nums[1] = 2` (even) -> `left=2`.
- `nums[2] = 4` (even) -> `left=3`.
- `nums[4] = 5` (odd) -> `right=3`.
- `left == right == 3` -> Loop terminates.
Result: `[6, 2, 4, 1, 5, 3]` partitioned in O(N) time and O(1) space.

## Visual Explanation

```text
Initial: [ 3, 2, 4, 1, 5, 6 ]
          ^                 ^
         left             right  -> nums[left] odd, nums[right] even -> SWAP

Step 1:  [ 6, 2, 4, 1, 5, 3 ]
             ^           ^
            left       right     -> nums[left] even -> advance left

Step 2:  [ 6, 2, 4, 1, 5, 3 ]
                ^        ^
               left    right     -> nums[left] even -> advance left

Step 3:  [ 6, 2, 4, 1, 5, 3 ]
                   ^     ^
                  left right     -> nums[right] odd -> decrement right

Terminates when left == right. Invariant: all items < left are even.
```

## Complexity

- **Time Complexity:** Index lookup: O(1) via direct arithmetic address offset. Append: Amortized O(1), Worst O(N) when buffer reallocates. Arbitrary insert/delete: O(N) due to required element shifting. Linear scan: O(N) visiting each element once.
- **Space Complexity:** O(1) auxiliary space for pure in-place algorithms; O(N) storage for holding N elements in contiguous dynamic array buffers.

Dynamic arrays over-allocate capacity to guarantee amortized O(1) insertions. In Python, list over-allocation follows the formula `(newsize >> 3) + (3 if newsize < 9 else 6) + newsize`.

## Interview Perspective

1. **Why is resizing a dynamic array by a constant factor (e.g., doubling) amortized O(1), whereas resizing by a fixed constant addition (e.g., adding 100 slots) is O(N) per insertion?**
   <details><summary>What a strong answer covers</summary>

   Doubling capacity spreads the cost of copy operations geometrically ($N/2 + N/4 + ... = O(N)$ total work across $N$ inserts, giving $O(1)$ amortized per append). Fixed constant addition requires reallocating every $K$ steps, summing to $\sum (i \cdot K) = O(N^2)$ across $N$ inserts, which is $O(N)$ amortized per append.

   </details>
2. **How does spatial locality affect modern CPU performance during row-major versus column-major iterations of a 2D array?**
   <details><summary>What a strong answer covers</summary>

   In row-major order (standard in C and Python internal contiguous buffers), elements of a row sit consecutively in memory. Iterating row-by-row loads entire cache lines into L1/L2 caches, causing minimal cache misses. Iterating column-by-column causes strides equal to the row width, repeatedly missing the cache for large matrices.

   </details>
3. **Can you describe how to rotate an N x N matrix by 90 degrees clockwise in-place using O(1) auxiliary memory?**
   <details><summary>What a strong answer covers</summary>

   First transpose the matrix (swap `matrix[i][j]` with `matrix[j][i]` for all `i < j`), then reverse each row individually. Alternatively, reverse the matrix upside-down and then transpose.

   </details>
4. **When can prefix sums turn an O(N^2) or O(N^3) array range query into O(1)? What are the trade-offs?**
   <details><summary>What a strong answer covers</summary>

   Prefix sums precompute cumulative totals in $O(N)$ time, allowing range sum query `sum(i..j)` to be computed as `prefix[j+1] - prefix[i]` in $O(1)$. The trade-off is $O(N)$ auxiliary space and the cost of maintaining the prefix array if elements are updated dynamically.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Sort Array by Parity II](exercises/problem-01.md) | Easy/Medium | two-pointers-invariants | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Product of Array Except Self](exercises/problem-02.md) | Medium | prefix-suffix-products | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Diagonal Matrix Traverse](exercises/problem-03.md) | Medium/Hard | 2d-matrix-manipulation | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Maximum Length of Repeated Subarray](exercises/problem-04.md) | Medium/Hard | dynamic-arrays | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Largest Rectangle in Histogram](exercises/problem-05.md) | Hard | monotonic-stack-over-indices | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-011
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: dynamic-arrays, two-pointers-invariants, prefix-suffix-products, 2d-matrix-manipulation, monotonic-stack-over-indices*
