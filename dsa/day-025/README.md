# Day 25: Day 25: Linear Search & Sequential Scanning Techniques

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 25 | 2026-11-03 | Searching | New topic | progressive | Python 3.12 |

Linear search is the fundamental technique for finding an element in an unsorted dataset by examining items one by one. While simple, understanding its variations—such as early exits, sentinel searches, and scanning under constraints—builds essential intuition for streaming data and unstructured collections. Today, we master sequential scanning, trade-offs, and optimization tricks.

## Topic

**Linear Search**: sequential scan, sentinel search, early exit, searching unsorted data

## Learning Objectives

By the end of this lesson you should be able to:

- Understand when linear search is optimal versus when preprocessing is required.
- Implement linear search variations, including early exits and sentinel optimization.
- Perform linear searches on multi-dimensional and structured streaming inputs.
- Identify edge cases such as empty collections, missing targets, and duplicate values.

## Concept Explanation

### What it is

Linear search (or sequential scan) iterates through a collection item by item, from start to finish, checking whether each element matches a target condition. It requires no structural order or sorting in the target dataset.

### Why it exists

When data is completely unsorted, random, or streaming sequentially (where indexing is impossible), linear search is the only general approach to locate an element. It avoids the $O(n \log n)$ runtime penalty of sorting data beforehand if you only need a single query.

### When to use it

Use linear search when the array is unsorted, the dataset is very small (where linear memory access beats tree/hash overhead), or you are processing a single-pass stream.

### When NOT to use it

Do not use linear search if the data is already sorted (use Binary Search for $O(\log n)$ time) or if you need to perform multiple lookups on a static dataset (use a Hash Set or Hash Map for $O(1)$ average time per query).

### How it works internally

1. Start at the first element (index 0).
2. Compare the current element against the target criteria.
3. If it matches, return the current index or value (early exit).
4. If it does not match, advance to the next element.
5. If the end of the collection is reached without a match, return a failure signal (e.g., `-1` or `None`).

*Sentinel Optimization Note*: A sentinel search places the target value at the end of the collection before starting. This allows the search loop to eliminate the boundary check (`i < length`) in every iteration, stopping only when the value is found, then checking if the index reached the sentinel.

### Common mistakes

- Forgetting early exit on the first match when only one match is needed.
- Off-by-one errors when managing sentinel elements at the array boundary.
- Accidentally running an $O(n^2)$ search by combining a linear scan with nested slicing or dynamic array lookups.
- Failing to handle empty inputs or collections where the target does not exist.

### Real-world applications

- Scanning raw log files or network packet streams for a specific error signature.
- Finding an element in small arrays where CPU cache prefetching makes sequential access faster than pointer-chasing structures.
- Searching unindexed database columns during a full table scan.

## Example

Tracing Sentinel Linear Search for target `7` in `arr = [4, 2, 9, 1]`:

1. Append sentinel `7` to array: `arr = [4, 2, 9, 1, 7]` (length = 5, sentinel index = 4).
2. Loop without boundary check `i < len`:
   - `i = 0`: `arr[0]` is `4` != `7`
   - `i = 1`: `arr[1]` is `2` != `7`
   - `i = 2`: `arr[2]` is `9` != `7`
   - `i = 3`: `arr[3]` is `1` != `7`
   - `i = 4`: `arr[4]` is `7` == `7` -> Loop terminates!
3. Check if `i < original_length` (`4 < 4` is False).
4. Target `7` was not in the original array. Return `-1`.

## Visual Explanation

```text
Standard Linear Search (Target = 5):
Index:    0    1    2    3    4
Array:  [ 8,   3,   5,   1,   9 ]
          |    |    |
          |    |    +---> Match found at index 2! (Early exit)
          |    +--------> 3 != 5 (Continue)
          +-------------> 8 != 5 (Continue)

Sentinel Linear Search (Target = 5):
Array:  [ 8,   3,   5,   1,   9 ] + [ 5 ]  (Sentinel added at end)
          Check 0, 1, 2 -> Match! Index 2 < Original Length -> Return 2.
```

## Complexity

- **Time Complexity:** Best Case: O(1) when target is at index 0. Worst Case: O(n) when target is absent or at the last index. Average Case: O(n).
- **Space Complexity:** O(1) auxiliary space for iterative scan; O(n) space if sentinel requires copying array.

Sentinel linear search reduces the constant factor by removing loop boundary checks per step, but retains O(n) worst-case time complexity.

## Interview Perspective

1. **When would you prefer Linear Search over Binary Search even if data can be sorted?**
   <details><summary>What a strong answer covers</summary>

   If we only perform a single search query, sorting takes O(n log n) time while linear search takes O(n). Preprocessing with sorting is only worth it for multiple queries.

   </details>
2. **What is the advantage of Sentinel Linear Search?**
   <details><summary>What a strong answer covers</summary>

   It eliminates the array bound check (e.g., `i < n`) inside the main loop loop, reducing instructions per iteration.

   </details>
3. **How does cache locality affect Linear Search compared to Tree or Hash searches?**
   <details><summary>What a strong answer covers</summary>

   Contiguous memory arrays used in linear search leverage hardware CPU cache prefetching, making sequential access significantly faster per element for small input sizes.

   </details>
4. **How do you apply linear search to dynamic streaming data of unknown size?**
   <details><summary>What a strong answer covers</summary>

   Use an iterator-based scan without relying on array length, evaluating items sequentially as they arrive until a match or stream termination.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [First Occurrence Index](exercises/problem-01.md) | Easy | Basic sequential scan with early exit | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Sentinel Target Search](exercises/problem-02.md) | Easy/Medium | Sentinel search technique to eliminate bound checks | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [First Local Minima in Matrix](exercises/problem-03.md) | Medium | Linear scan over 2D grid with conditional early exit | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Longest Equal Element Sequence under Skip Constraint](exercises/problem-04.md) | Medium/Hard | Linear scan state tracking with limited dynamic state | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Stream Peak Detection](exercises/problem-05.md) | Hard | Stateful streaming linear search over infinite dynamic window | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-025
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: linear-search, sentinel-search, early-exit, streaming-scan*
