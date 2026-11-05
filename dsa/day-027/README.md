# Day 27: Day 27: Binary Search Basics

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 27 | 2026-11-05 | Searching | New topic | progressive | Python 3.12 |

Binary Search is the foundational algorithm for searching sorted data structures in logarithmic time. Instead of checking elements one by one, Binary Search repeatedly cuts the search space in half by comparing the target with the middle element. Mastering this concept unlocks efficient searching, bound-finding, and binary searching over answers.

## Topic

**Binary Search**: sorted input, search space halving, loop invariants, off-by-one errors, iterative vs recursive

## Learning Objectives

By the end of this lesson you should be able to:

- Understand the core principle of search space halving and why it achieves O(log n) time complexity.
- Formulate and maintain precise loop invariants to prevent off-by-one errors and infinite loops.
- Implement both iterative and recursive standard binary search safely in Python.
- Identify lower-bound and upper-bound variations for finding first and last occurrences of elements.
- Determine when binary search is applicable and when linear search or hashing is preferable.

## Concept Explanation

### What it is

Binary Search is an algorithm that finds the position of a target value within a sorted array. It works by checking the middle element of the array: if the middle element matches the target, the search ends; if the target is smaller, the search continues in the left half; if larger, it continues in the right half. This process repeats until the element is found or the search space becomes empty.

### Why it exists

Linear search checks elements one by one, requiring O(n) time. For an array of 1,000,000,000 elements, linear search could take 1 billion operations. Binary search reduces the search space by half at each step, requiring at most ~30 operations (log2(10^9) ≈ 30). Without binary search, querying large static datasets would be prohibitively slow.

### When to use it

Use binary search when:
- The input array (or search space) is sorted or monotonic.
- You need O(log n) lookups on random-access data structures (like arrays).
- You need to find boundary conditions, such as the first/last instance of a value, or the insertion index for a new element.

### When NOT to use it

Do not use binary search when:
- The data is unsorted and sorting it would take O(n log n) for just a single query (use linear search O(n) or build a hash map O(n) instead).
- The data structure does not support fast random access (e.g., standard singly linked lists where finding the middle node takes O(n) time, invalidating the logarithmic benefit).
- The dataset is extremely small (e.g., n < 10), where linear search overhead is negligible.

### How it works internally

1. Initialize two pointers: `low = 0` and `high = len(nums) - 1` defining the current inclusive search range `[low, high]`.
2. Maintain the loop invariant: *If the target exists in the array, it must lie within the range `[low, high]`*.
3. In a loop while `low <= high`:
   - Compute middle index: `mid = low + (high - low) // 2` (avoids integer overflow in languages with fixed integer sizes).
   - Compare `nums[mid]` with `target`:
     - If `nums[mid] == target`, return `mid`.
     - If `nums[mid] < target`, target must be in the right half, so set `low = mid + 1`.
     - If `nums[mid] > target`, target must be in the left half, so set `high = mid - 1`.
4. If `low > high`, the search space is empty, meaning the target does not exist. Return `-1` (or appropriate default).

### Common mistakes

- Using `low < high` instead of `low <= high` in standard binary search, which misses checking single-element search spaces.
- Updating bounds to `low = mid` or `high = mid` instead of `mid + 1` / `mid - 1` in standard search, causing infinite loops when `low` and `high` are adjacent.
- Off-by-one errors when setting initial `high` index (e.g., setting `high = len(nums)` with `low <= high`).
- Assuming binary search only works for exact key lookup, missing boundary search (bisect_left / bisect_right) patterns.

### Real-world applications

- Database indexing (B-Trees and ISAM indexes use binary search on page blocks).
- Standard library search functions (`bisect` in Python, `std::lower_bound` in C++).
- Git bisect: finding the commit that introduced a bug using binary search over commit history.
- Auto-complete and dictionary lookups in sorted wordlists.

## Example

Trace `binary_search([1, 3, 5, 7, 9, 11], target=7)`:

Array: `[1, 3, 5, 7, 9, 11]`, indices `0..5`.
- Initial: `low = 0`, `high = 5`.
- Step 1: `mid = 0 + (5 - 0) // 2 = 2`. `nums[2] = 5`.
  `5 < 7` -> Target is to the right. Set `low = mid + 1 = 3`.
- Step 2: Range `[3, 5]`. `mid = 3 + (5 - 3) // 2 = 4`. `nums[4] = 9`.
  `9 > 7` -> Target is to the left. Set `high = mid - 1 = 3`.
- Step 3: Range `[3, 3]`. `mid = 3 + (3 - 3) // 2 = 3`. `nums[3] = 7`.
  `nums[3] == 7` -> Target found! Return index `3`.

## Visual Explanation

```text
Target = 7
Array: [ 1,  3,  5,  7,  9, 11 ]
Idx:     0   1   2   3   4   5

Pass 1: low=0, high=5
        [ 1,  3,  5,  7,  9, 11 ]
          ^       ^           ^
         low     mid        high
        nums[mid] = 5 < 7  ==>  low = mid + 1 (3)

Pass 2: low=3, high=5
        [ 1,  3,  5,  7,  9, 11 ]
                      ^   ^   ^
                     low mid high
        nums[mid] = 9 > 7  ==>  high = mid - 1 (3)

Pass 3: low=3, high=3
        [ 1,  3,  5,  7,  9, 11 ]
                      ^
                 low/mid/high
        nums[mid] = 7 == 7 ==> Return index 3!
```

## Complexity

- **Time Complexity:** O(log n) for searching in a sorted array of size n, as the search space size is halved at each step.
- **Space Complexity:** O(1) auxiliary space for iterative implementation; O(log n) stack space for recursive implementation.

Binary Search requires random-access indexing (O(1) element retrieval). If performed on a linked list, step navigation is O(n), destroying the O(log n) time complexity benefit.

## Interview Perspective

1. **Why is `mid = low + (high - low) // 2` preferred over `mid = (low + high) // 2`?**
   <details><summary>What a strong answer covers</summary>

   In languages with fixed-size integer types (like 32-bit integers in C++/Java), `low + high` can exceed the maximum integer limit and overflow, producing a negative number. While Python handles arbitrarily large integers automatically, using `low + (high - low) // 2` is good defensive practice across standard engineering interviews.

   </details>
2. **How do you modify binary search to find the FIRST occurrence of a target element with duplicates?**
   <details><summary>What a strong answer covers</summary>

   When `nums[mid] == target`, instead of returning immediately, record `mid` as a candidate answer and narrow the search space to the left by setting `high = mid - 1` to check for earlier occurrences.

   </details>
3. **What is the key difference between loop termination condition `low <= high` vs `low < high`?**
   <details><summary>What a strong answer covers</summary>

   `low <= high` maintains an inclusive interval `[low, high]` where the loop continues until the search space has 0 elements. `low < high` maintains an interval where loop terminates when 1 element remains (`low == high`), which is commonly used when shrinking boundaries toward a single target element without explicit equality return inside the loop.

   </details>
4. **Can Binary Search be applied to unsorted arrays?**
   <details><summary>What a strong answer covers</summary>

   Standard binary search requires sorted array properties (monotonicity). However, generalized binary search (binary search on answer) can be applied whenever a decision function `f(x)` is monotonic (e.g., `false, false, ..., true, true`).

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Standard Binary Search](exercises/problem-01.md) | Easy | Basic search space halving on a distinct sorted array | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Search Insert Position](exercises/problem-02.md) | Easy/Medium | Finding lower-bound insertion point in a sorted array | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Find First and Last Position of Element in Sorted Array](exercises/problem-03.md) | Medium | Boundary searching (lower bound and upper bound) with duplicate values | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Find Peak Element](exercises/problem-04.md) | Medium/Hard | Binary search on unsorted / locally sorted structure using local monotonicity | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Search in Rotated Sorted Array](exercises/problem-05.md) | Hard | Modified binary search on a shifted/rotated sorted domain | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-027
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: binary-search, search-space-halving, loop-invariants, lower-bound, upper-bound*
