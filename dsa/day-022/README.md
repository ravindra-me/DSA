# Day 22: Day 22: Two Pointers

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 22 | 2026-10-31 | Core Array Patterns | New topic | progressive | Python 3.12 |

The Two Pointers pattern coordinates two indices across one or more linear sequences to search, partition, or transform data in linear time. Instead of testing all pairs with nested loops in $O(n^2)$, two pointers exploit structural invariants—such as sorting or monotonic conditions—to eliminate large swaths of redundant search space. Mastering both opposite-direction and same-direction traversal forms the bedrock for advanced array and sequence manipulation.

## Topic

**Two Pointers**: opposite-direction pointers, same-direction pointers, pair sum in sorted array, partitioning, removing duplicates in place

## Learning Objectives

By the end of this lesson you should be able to:

- Identify when an array's structural order allows eliminating brute-force nested loops using two pointers.
- Implement opposite-direction pointer patterns for pair finding, palindromes, and container optimization.
- Implement same-direction (slow/fast) pointer patterns for in-place deduplication and array partitioning.
- Formulate and maintain explicit pointer invariants to prevent off-by-one errors and infinite loops.
- Analyze exact time and space complexity, demonstrating optimal $O(n)$ time with $O(1)$ auxiliary space.

## Concept Explanation

### What it is

Two Pointers is an algorithmic technique where two reference markers (indices) traverse a sequence simultaneously. Pointers may move toward each other from opposite ends (convergent/opposite-direction) or in the same direction at varying rates (read/write or fast/slow). By carefully deciding which pointer to advance based on local comparisons, we avoid exhaustive search and process linear data structures in $O(n)$ time.

### Why it exists

Examining all pairs or contiguous regions in an array of size $n$ naively takes $\binom{n}{2} \approx O(n^2)$ operations. Hash tables can sometimes reduce pair searches to $O(n)$ time, but they incur $O(n)$ extra space and cannot easily answer relative ordering or bounded range constraints. Two pointers operate in-place with $O(1)$ additional memory while achieving optimal $O(n)$ time by exploiting properties like sortedness or monotonicity.

### When to use it

Consider Two Pointers when:
- The array is sorted (or sorting it in $O(n \log n)$ is acceptable).
- You need to find pairs or triplets satisfying an exact sum, difference, or comparison condition.
- You must modify an array in-place (e.g., removing duplicates, partitioning by pivot, filtering elements) without allocating a new buffer.
- You are checking symmetry (e.g., valid palindrome strings) or computing bounded geometrical envelopes (e.g., container with most water).

### When NOT to use it

Avoid Two Pointers when:
- The collection is unsorted and sorting breaks the required answer (e.g., returning original indices where hashing is $O(n)$ vs sorting $O(n \log n)$).
- Moving a pointer does not provide a monotonic guarantee (i.e., advancing a pointer could unpredictably either increase or decrease the outcome).
- Non-contiguous arbitrary combinations are required (use backtracking instead).

### How it works internally

1. **Opposite-Direction (Inward)**: Place `left = 0` and `right = len(arr) - 1`. Evaluate `arr[left]` and `arr[right]`. Because the array is sorted, if their combined property (e.g., sum) is too small, incrementing `left` is the *only* move that can increase it; advancing `right` inward would only decrease it further. We safely discard an entire row of candidates in $O(1)$. Repeat while `left < right`.
2. **Same-Direction (Read/Write)**: Place a `write` pointer at the boundary of processed valid elements and a `read` pointer scanning through the collection. When `arr[read]` satisfies a retention condition, write it to `arr[write]` and increment `write`. This maintains the invariant that `arr[0...write-1]` contains only valid elements.

### Common mistakes

- Using `left <= right` instead of `left < right` (or vice-versa), causing index errors or examining the same element twice when distinct pair elements are required.
- Advancing pointers without checking boundary conditions, leading to `IndexError` when searching duplicates.
- Failing to handle duplicate values in sorted pair/triplet problems, resulting in duplicate results in the output.
- Assuming an unsorted array works with opposite-direction pointers without establishing monotonicity first.

### Real-world applications

- Quicksort Partitioning (Hoare and Lomuto partition schemes reorganize arrays in-place around a pivot using two pointers).
- Memory Defragmentation & Compaction (Garbage collectors use read/write compacting pointers to slide live objects to one end of the heap).
- Database Merge Joins (Joining two pre-sorted tables on matching keys in $O(N + M)$ time by stepping two cursor pointers).
- Network Packet Processing (Reassembling and filtering out-of-order or duplicate sequence chunks in-place).

## Example

### Tracing Two Sum on a Sorted Array
Target: `target = 9`, Array: `nums = [2, 3, 5, 7, 11]`

```python
left = 0  # nums[0] = 2
right = 4 # nums[4] = 11

# Iteration 1:
current_sum = nums[left] + nums[right] = 2 + 11 = 13
# 13 > 9. Since the array is sorted, pairing nums[4] with ANY element >= nums[0]
# will yield a sum >= 13 > 9. Therefore, nums[4] cannot be part of the solution.
right -= 1 # right is now 3 (nums[3] = 7)

# Iteration 2:
current_sum = nums[left] + nums[right] = 2 + 7 = 9
# 9 == target! Match found at indices (0, 3).
```
Every step eliminates at least one element permanently from consideration. In the worst case, we do at most $n$ comparisons.

## Visual Explanation

```text
Opposite-Direction Pointers (e.g., Two Sum Sorted / Palindrome):
  left ->                                <- right
  [  2,     3,     5,     7,    11  ]
     ^                           ^
  sum = 2 + 11 = 13 > 9  ==>  right moves left

  [  2,     3,     5,     7,    11  ]
     ^                    ^
  sum = 2 + 7 = 9 == 9   ==>  Target matched!

Same-Direction Pointers (e.g., Remove Duplicates In-Place):
  write (tail of unique prefix)
  read  (scout scanning forward)

  [ 1,  1,  2,  2,  3 ]    nums[read] == nums[write]: skip
    w   r

  [ 1,  1,  2,  2,  3 ]    nums[read] != nums[write]:
    w       r              write += 1; nums[write] = nums[read]

  [ 1,  2,  2,  2,  3 ]
        w   r
```

## Complexity

- **Time Complexity:** O(n): Each step advances at least one pointer (either `left += 1`, `right -= 1`, or `read += 1`), bounding total loop iterations strictly by n.
- **Space Complexity:** O(1): Only two integer index variables are maintained, requiring constant auxiliary memory.

If the input array is not sorted, sorting it first takes $O(n \log n)$ time. This is still faster than naive $O(n^2)$ brute force and uses $O(1)$ extra space if sorted in-place.

## Interview Perspective

1. **When should you prefer Two Pointers over a Hash Map for pair-sum problems?**
   <details><summary>What a strong answer covers</summary>

   If the array is already sorted, Two Pointers requires $O(1)$ auxiliary space versus $O(n)$ for a hash map, and has better cache locality. If the array is unsorted and you must preserve original indices, a Hash Map allows $O(n)$ time while sorting takes $O(n \log n)$ and extra work to track indices.

   </details>
2. **How do you avoid duplicate triplets in 3Sum when using Two Pointers?**
   <details><summary>What a strong answer covers</summary>

   First sort the array. When fixing the first element `nums[i]`, skip if `i > 0 and nums[i] == nums[i-1]`. Inside the two-pointer loop, after finding a valid pair `(left, right)`, advance `left` and decrement `right` past all consecutive matching values.

   </details>
3. **Can two pointers be used on linked lists? How does that differ from arrays?**
   <details><summary>What a strong answer covers</summary>

   Yes, but linked lists lack random access (no backward traversal without doubly linked lists). Therefore, opposite-direction pointers are impractical unless reversed, but same-direction fast and slow pointers (e.g., Floyd's cycle detection, finding the middle) are standard.

   </details>
4. **Why is the Dutch National Flag problem solved with three pointers instead of two?**
   <details><summary>What a strong answer covers</summary>

   Because there are three categories (0s, 1s, 2s). One pointer tracks the boundary of 0s (`low`), another tracks the boundary of 2s (`high`), and a `mid` pointer scans the unknown middle region.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Valid Palindrome with Alphanumeric Filtering](exercises/problem-01.md) | Easy | Opposite-direction pointers with conditional filtering | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Remove Duplicates from Sorted Array II](exercises/problem-02.md) | Easy/Medium | Same-direction read/write pointers with frequency thresholding | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Two Sum II - Input Array Is Sorted](exercises/problem-03.md) | Medium | Opposite-direction convergent search on sorted sequences | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Sort Colors (Dutch National Flag)](exercises/problem-04.md) | Medium/Hard | Three-way partitioning using multi-pointer invariants | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Container With Most Water](exercises/problem-05.md) | Hard | Greedy area maximization via inward converging pointers | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-022
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: Opposite-direction two pointers, Same-direction two pointers (read/write), In-place array partitioning, Duplicate handling with two pointers, Greedy area maximization via inward pointers*
