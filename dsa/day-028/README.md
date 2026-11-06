# Day 28: Day 28: Binary Search Variations

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 28 | 2026-11-06 | Searching | New topic | progressive | Python 3.12 |

Standard binary search finds an exact element in a sorted array, but interview problems rarely ask for just that. This lesson covers powerful variations of binary search: finding boundaries (lower/upper bounds), navigating modified sorted spaces (rotated arrays), searching implicit 2D grids, and finding local extrema (peaks). Mastering these template variations allows you to solve complex searching problems in O(log N) time.

## Topic

**Binary Search Variations**: lower/upper bound, first/last occurrence, rotated sorted array, peak element, search in 2D matrix

## Learning Objectives

By the end of this lesson you should be able to:

- Implement lower bound (first occurrence) and upper bound (last occurrence) cleanly without infinite loops.
- Search efficiently in rotated sorted arrays by identifying sorted halves.
- Find a peak element in an unsorted array using binary search on local gradients.
- Map 2D matrix coordinates to 1D binary search spaces.
- Avoid subtle off-by-one errors and loop termination bugs across all binary search templates.

## Concept Explanation

### What it is

Binary Search Variations extend basic binary search ($O(\log N)$ divide-and-conquer) to solve non-standard search problems. Instead of simply checking `arr[mid] == target`, variations apply binary search to find insertion points, handle shifted/rotated sorted data, navigate 2D sorted matrices, or locate peak elements where a predicate monotonicity condition holds.

### Why it exists

Standard binary search fails when there are duplicate elements and you need a specific occurrence, or when the array is modified (rotated), multidimensional, or not globally sorted. Reverting to linear search ($O(N)$) wastes performance. Variations allow us to maintain optimal $O(\log N)$ time complexity by adapting the search invariant.

### When to use it

Use binary search variations when: 1) The input is sorted or partially sorted (e.g., rotated). 2) You need the boundary of a condition (e.g., first index where `x >= target`). 3) You are searching a 2D matrix with row/column sorted properties. 4) You need a local peak or minimum in $O(\log N)$ time.

### When NOT to use it

Do not use binary search variations when: 1) The data is completely unsorted with no structural invariants or monotonicity. 2) The array requires frequent insertions/deletions (use a Balanced Binary Search Tree or Skip List instead). 3) The input size is tiny (linear search may be faster due to cache locality).

### How it works internally

All variations rely on maintaining a search interval `[left, right]` (or half-open `[left, right)`):

1. **First/Last Occurrence (Bounds)**: Instead of returning early when `arr[mid] == target`, save `mid` as a candidate solution and keep searching left (for first occurrence) or right (for last occurrence).
2. **Rotated Sorted Array**: Compare `arr[mid]` with `arr[left]` or `arr[right]`. At least one half (`[left, mid]` or `[mid, right]`) is guaranteed to be strictly sorted. Determine if the target lies within the sorted half to decide which direction to eliminate.
3. **Peak Finding**: Compare `arr[mid]` with `arr[mid + 1]`. If `arr[mid] < arr[mid + 1]`, a peak must exist to the right because the sequence is increasing. Otherwise, a peak exists at `mid` or to the left.
4. **2D Matrix Search**: Treat an $M \times N$ sorted matrix as a flat 1D array of size $M \times N$. Map index `mid` to matrix cell `(mid // N, mid % N)`.

### Common mistakes

- Integer overflow when calculating `mid = (left + right) // 2` in languages with bounded integers (use `left + (right - left) // 2`).
- Infinite loops caused by incorrect pointer updates (e.g., setting `left = mid` instead of `left = mid + 1` with `while left < right`).
- Failing to handle duplicate values in rotated sorted arrays, which degrades worst-case search time to $O(N)$.
- Incorrect matrix indexing: mixing up rows (`mid // num_cols`) and columns (`mid % num_cols`).

### Real-world applications

- Database Engines: Utilizing B-Tree index lower/upper bounds to execute range queries (e.g., `WHERE age BETWEEN 20 AND 30`).
- C++ STL & Python standard libraries: `std::lower_bound`, `std::upper_bound`, and Python's `bisect_left` / `bisect_right`.
- Git Bisect: Finding the exact commit that introduced a bug using binary search on revision logs.
- Computer Graphics & Gaming: Ray casting and collision detection using bounding volume hierarchies.

## Example

### Tracing First and Last Occurrence

Given sorted array `nums = [1, 2, 4, 4, 4, 5, 7]` and `target = 4`:

#### 1. Find First Occurrence (Lower Bound for exact target)
- Initial: `left = 0`, `right = 6`, `ans = -1`
- `mid = 3`: `nums[3] == 4`. Candidate `ans = 3`. Search left half to find earlier match $\rightarrow$ `right = mid - 1 = 2`.
- `mid = 1`: `nums[1] == 2 < 4`. Search right half $\rightarrow$ `left = mid + 1 = 2`.
- `mid = 2`: `nums[2] == 4`. Candidate `ans = 2`. Search left half $\rightarrow$ `right = mid - 1 = 1`.
- Loop terminates (`left > right`). First occurrence is `2`.

#### 2. Find Last Occurrence (Upper Bound for exact target)
- Initial: `left = 0`, `right = 6`, `ans = -1`
- `mid = 3`: `nums[3] == 4`. Candidate `ans = 3`. Search right half $\rightarrow$ `left = mid + 1 = 4`.
- `mid = 5`: `nums[5] == 5 > 4`. Search left half $\rightarrow$ `right = mid - 1 = 4`.
- `mid = 4`: `nums[4] == 4`. Candidate `ans = 4`. Search right half $\rightarrow$ `left = mid + 1 = 5`.
- Loop terminates (`left > right`). Last occurrence is `4`.

## Visual Explanation

```text
1. Lower Bound (First Occurrence of Target = 4):
   Array: [1, 2, 4, 4, 4, 5, 7]
   Index:  0  1  2  3  4  5  6
   Step 1: L           M           R  -> nums[3] == 4, ans = 3, go left (R = 2)
   Step 2: L  M  R                    -> nums[1] == 2 < 4, go right (L = 2)
   Step 3:    L/M/R                   -> nums[2] == 4, ans = 2, go left (R = 1)
   End: L > R -> Return ans = 2

2. Rotated Sorted Array Search (Target = 0):
   Array: [4, 5, 6, 7, 0, 1, 2]
   Index:  0  1  2  3  4  5  6
   Step 1: L           M           R  (nums[L]=4 <= nums[M]=7 -> Left side sorted! Target 0 not in [4..7] -> L = M + 1)
   Step 2:                L  M     R  (nums[M]=1, compare & shrink space)
   Result: Found target 0 at index 4
```

## Complexity

- **Time Complexity:** O(log N) for 1D arrays and M x N sorted matrices (where size is N or M*N). Each step halves the search space.
- **Space Complexity:** O(1) auxiliary space for iterative binary search implementations.

If duplicates exist in a rotated sorted array, the worst-case time complexity degrades to $O(N)$ because element equality prevents discarding half the array.

## Interview Perspective

1. **What is the difference between finding an exact target and finding lower/upper bounds?**
   <details><summary>What a strong answer covers</summary>

   Finding an exact target returns immediately upon finding `arr[mid] == target`. Lower bound finds the first index where `arr[i] >= target` (or first occurrence), requiring the search to continue to the left after a match. Upper bound finds the first index where `arr[i] > target` (or last occurrence by shifting right).

   </details>
2. **How do you avoid infinite loops in binary search templates?**
   <details><summary>What a strong answer covers</summary>

   Ensure `left` and `right` shrink deterministically on every step. For `while left < right`, use `mid = left + (right - left) // 2` when moving `right = mid`, or `mid = left + (right - left + 1) // 2` when moving `left = mid` to prevent rounding towards `left` indefinitely.

   </details>
3. **How do you perform binary search on a 2D matrix?**
   <details><summary>What a strong answer covers</summary>

   If matrix rows are sequentially sorted end-to-end, treat the matrix as a 1D array of size `M * N`. Index `k` maps to `row = k // N` and `col = k % N`. Perform standard binary search on `k` in range `[0, M*N - 1]`.

   </details>
4. **Why does binary search work to find a local peak in an unsorted array?**
   <details><summary>What a strong answer covers</summary>

   By comparing `nums[mid]` and `nums[mid + 1]`, we observe the local slope. If `nums[mid] < nums[mid + 1]`, an ascending slope guarantees at least one local peak exists in the right half. If descending, a peak exists at `mid` or to the left.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [First and Last Position of Target](exercises/problem-01.md) | Easy | first-last-occurrence | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Search in Rotated Sorted Array](exercises/problem-02.md) | Easy/Medium | rotated-sorted-array | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Find Minimum in Rotated Sorted Array](exercises/problem-03.md) | Medium | rotated-sorted-array | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Find Peak Element](exercises/problem-04.md) | Medium/Hard | peak-finding | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Search a 2D Matrix II](exercises/problem-05.md) | Hard | matrix-binary-search | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-028
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: lower-bound, upper-bound, first-last-occurrence, rotated-sorted-array, peak-finding, matrix-binary-search*
