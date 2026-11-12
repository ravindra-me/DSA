# Day 34: Day 34: Quick Sort & Quickselect

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 34 | 2026-11-12 | Sorting | New topic | progressive | Python 3.12 |

Quick Sort is a divide-and-conquer sorting algorithm that selects a 'pivot' element and partitions the array into elements smaller and larger than the pivot. While Merge Sort guarantees $O(N \log N)$ by using extra memory, Quick Sort works in-place with minimal space overhead and runs exceptionally fast in practice. Its core partitioning logic also powers Quickselect, a algorithm that finds the $k$-th smallest element in linear expected time without fully sorting the array.

## Topic

**Quick Sort & Quickselect**: partitioning (Lomuto/Hoare), pivot choice, randomization, quickselect, Dutch national flag

## Learning Objectives

By the end of this lesson you should be able to:

- Master array partitioning techniques including Lomuto, Hoare, and Dutch National Flag (3-way) schemes.
- Understand pivot selection strategies and why randomization prevents $O(N^2)$ worst-case scenarios.
- Implement Quickselect to solve top-$k$ and $k$-th order statistic problems in $O(N)$ average time.
- Analyze space complexity differences between naive recursion, tail call optimization, and auxiliary arrays.

## Concept Explanation

### What it is

Quick Sort relies on a fundamental operation called **partitioning**. Given an array and a target value called a **pivot**, partitioning rearanges the elements in-place so that all values less than or equal to the pivot end up on its left, and all values greater end up on its right. Once the pivot is in its final sorted position, Quick Sort recursively applies the exact same process to the left and right subarrays.

### Why it exists

Merge Sort guarantees $O(N \log N)$ time but requires $O(N)$ extra memory for merging. Elementary sorts (like Bubble or Insertion sort) run in-place but take $O(N^2)$ time. Quick Sort fills the sweet spot: it sorts in-place ($O(1)$ auxiliary memory besides the recursion stack) and achieves $O(N \log N)$ average-case performance with very low constant factors due to cache-friendly memory access patterns.

### When to use it

Use Quick Sort when you need to sort an array in-place with minimum space overhead. Use **Quickselect** when you need to find the $k$-th smallest (or largest) element, or separate elements into the top-$k$ without paying the cost of a full sort.

### When NOT to use it

Do not use Quick Sort when stable sorting is required (it swaps non-adjacent elements). Avoid naive Quick Sort when inputs may contain many duplicate keys or already-sorted sequences; instead, use Dutch National Flag partitioning or randomized pivots to prevent degenerating into $O(N^2)$.

### How it works internally

1. **Pivot Selection:** Choose a pivot element (e.g., random index, middle, or median-of-three).
2. **Partitioning:**
   - **Lomuto Partition:** Maintains a boundary index `i` for elements smaller than the pivot. Iterates index `j` through the array; whenever `arr[j] <= pivot`, increments `i` and swaps `arr[i]` with `arr[j]`.
   - **Hoare Partition:** Uses two pointers starting at opposite ends moving inward until they find inverted elements, then swaps them. Generally performs fewer swaps than Lomuto.
   - **Dutch National Flag (3-Way):** Partitions into three regions (`< pivot`, `== pivot`, `> pivot`). Crucial for handling arrays with heavy duplicates.
3. **Recursion / Selection:**
   - For **Quick Sort**: Recursively process `[low, pivot_idx - 1]` and `[pivot_idx + 1, high]`.
   - For **Quickselect**: Compare $k$ against the pivot's index. Recurse into *only one half*, discarding the other.

### Common mistakes

- Choosing a deterministic pivot (like always picking the first or last element), which leads to $O(N^2)$ time on sorted/reverse-sorted inputs.
- Off-by-one errors during partitioning causing infinite recursion loops.
- Not handling duplicate elements efficiently, causing unbalanced splits even on simple arrays like `[1, 1, 1, 1]`.
- Using $O(N)$ extra memory by creating new lists (`[x for x in arr if x < pivot]`) instead of partitioning in-place.

### Real-world applications

- Standard library implementations: C's `qsort`, C++ `std::nth_element` (which uses Introsort/Quickselect).
- Finding median values in large streaming datasets or computing order statistics in databases.
- Partitioning elements in graphics pipelines and spatial indexing.

## Example

Tracing Lomuto Partitioning on `[3, 8, 2, 5, 1, 4]` with `pivot = 4` (last element):

Initial: `arr = [3, 8, 2, 5, 1, 4]`, `pivot = 4`, `i = -1` (boundary of elements <= pivot)
- `j = 0`, `arr[0] = 3 <= 4`: `i` becomes 0. Swap `arr[0]` & `arr[0]`. `[3, 8, 2, 5, 1, 4]`
- `j = 1`, `arr[1] = 8 > 4`: No swap.
- `j = 2`, `arr[2] = 2 <= 4`: `i` becomes 1. Swap `arr[1]` (8) & `arr[2]` (2). `[3, 2, 8, 5, 1, 4]`
- `j = 3`, `arr[3] = 5 > 4`: No swap.
- `j = 4`, `arr[4] = 1 <= 4`: `i` becomes 2. Swap `arr[2]` (8) & `arr[4]` (1). `[3, 2, 1, 5, 8, 4]`
- End of loop: Swap pivot `arr[5]` (4) with `arr[i + 1]` (5).
Final Array: `[3, 2, 1, 4, 8, 5]`. Pivot `4` is now at its correct sorted index `3`!

## Visual Explanation

```text
Lomuto Partitioning Visualization (Pivot = 4):

Initial state:
  3   8   2   5   1 | [4]
  ^                 pivot
  j (i = -1)

After scanning 3 (3 <= 4, swap with itself, i=0):
 [3]  8   2   5   1 | [4]
      ^ 
      j

After scanning 8 (8 > 4, do nothing):
 [3]  8   2   5   1 | [4]
          ^
          j

After scanning 2 (2 <= 4, i=1, swap 8 and 2):
 [3   2]  8   5   1 | [4]
              ^
              j

After scanning 1 (1 <= 4, i=2, swap 8 and 1):
 [3   2   1]  5   8 | [4]

Finally swap pivot (4) with element at i+1 (5):
 [3   2   1] (4) [8   5]
  <= pivot   p    > pivot
```

## Complexity

- **Time Complexity:** Quick Sort: Average $O(N \log N)$, Worst $O(N^2)$ (when pivots are poorly chosen). Quickselect: Average $O(N)$, Worst $O(N^2)$.
- **Space Complexity:** $O(\log N)$ average space for the call stack when using tail-recursion optimization (recursing on the smaller partition first). $O(N)$ worst case stack depth.

Randomizing the pivot selection guarantees $O(N \log N)$ expected time for Quick Sort and $O(N)$ expected time for Quickselect regardless of initial array ordering.

## Interview Perspective

1. **What is the difference between Lomuto and Hoare partitioning schemes?**
   <details><summary>What a strong answer covers</summary>

   Lomuto uses a single directional scan with a pivot at the end; it does more swaps and can degrade to O(N^2) on identical elements. Hoare uses two pointers scanning inward from both sides; it does roughly 3x fewer swaps on average and handles identical elements better.

   </details>
2. **How do you avoid the O(N^2) worst-case time complexity in Quick Sort?**
   <details><summary>What a strong answer covers</summary>

   Use randomized pivot selection or the 'median-of-three' rule (median of first, middle, last elements). For arrays with duplicate keys, use 3-way partitioning (Dutch National Flag).

   </details>
3. **How can you guarantee O(log N) auxiliary stack space for Quick Sort?**
   <details><summary>What a strong answer covers</summary>

   Always recurse into the smaller partition first, and use tail-call elimination (or an explicit loop) for the larger partition.

   </details>
4. **Why is Quickselect O(N) on average while Quick Sort is O(N log N)?**
   <details><summary>What a strong answer covers</summary>

   Quick Sort processes both halves after partitioning (N + 2*(N/2) + 4*(N/4) ... = N log N). Quickselect discards one half and only recurses into the side containing target k (N + N/2 + N/4 + ... = 2N = O(N)).

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Lomuto Partition Scheme](exercises/problem-01.md) | Easy | Lomuto Partitioning | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Kth Smallest Element (Quickselect)](exercises/problem-02.md) | Easy/Medium | Quickselect | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Sort Colors (3-Way Partitioning)](exercises/problem-03.md) | Medium | Dutch National Flag Partitioning | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [K Closest Points to Origin](exercises/problem-04.md) | Medium/Hard | Quickselect with Custom Distance Function | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Wiggle Sort II](exercises/problem-05.md) | Hard | 3-Way Partitioning with Index Mapping | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-034
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: Lomuto Partitioning, Hoare Partitioning, Dutch National Flag Partitioning, Randomized Quickselect, In-Place Sorting*
