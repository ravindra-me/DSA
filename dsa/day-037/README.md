# Day 37: Day 37: Counting, Bucket & Radix Sort (Non-Comparison Sorts)

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 37 | 2026-11-15 | Sorting | New topic | progressive | Python 3.12 |

Every comparison-based sorting algorithm—like Merge Sort or Quick Sort—is fundamentally bounded by a theoretical lower limit of $\Omega(n \log n)$. Non-comparison sorting breaks this barrier by leveraging the internal representation or value distribution of keys. Today, we will explore Counting Sort, Radix Sort, and Bucket Sort to achieve linear $O(n)$ time complexity when data constraints allow.

## Topic

**Counting, Bucket & Radix Sort**: counting sort, bucket sort, radix sort, linear-time sorting limits

## Learning Objectives

By the end of this lesson you should be able to:

- Understand the information-theoretic lower bound $\Omega(n \log n)$ for comparison sorts and how non-comparison sorts bypass it.
- Implement Counting Sort with cumulative sums to achieve stability for composite keys.
- Implement LSD (Least Significant Digit) Radix Sort across fixed-width integers and strings.
- Apply Bucket Sort for uniformly distributed data and analyze its average-case linear behavior.
- Evaluate constraints to determine when non-comparison sorts are optimal versus when auxiliary memory overhead makes them impractical.

## Concept Explanation

### What it is

Non-comparison sorts are algorithms that sort items without directly asking 'is item A greater than item B?'. Instead, they inspect the mathematical or structural properties of keys (e.g., individual digits, character encodings, or numeric ranges) and place elements directly into pre-allocated positions or bins.

### Why it exists

Any comparison-based sorting algorithm can be modeled as a decision tree where each branch represents an outcome of $A \le B$. Since a list of $n$ elements has $n!$ possible permutations, the decision tree must have at least $n!$ leaves. The minimum depth of such a binary tree is $\lceil \log_2(n!) \rceil = \Omega(n \log n)$. To sort faster than $O(n \log n)$, we must use operations other than binary comparisons, such as array indexing based on element values.

### When to use it

Use non-comparison sorting when keys are integers, fixed-length strings, or uniformly distributed floats within a bounded range. Specifically:
- **Counting Sort**: When the range of integer keys $k$ is small relative to $n$ (i.e., $k = O(n)$).
- **Radix Sort**: When keys are integers or strings with a fixed or bounded number of digits/characters $d$.
- **Bucket Sort**: When inputs are continuous floating-point values uniformly distributed over a known interval $[a, b)$.

### When NOT to use it

Do not use non-comparison sorts when:
- Keys have arbitrarily large ranges with no digit-wise structure (e.g., arbitrary large 64-bit floats or unstructured custom objects).
- The range $k$ is exponentially larger than $n$ (e.g., sorting 10 numbers whose values are up to $10^{15}$; Counting Sort would allocate an array of size $10^{15}$).
- Memory overhead is strictly constrained, as non-comparison sorts generally require $O(n + k)$ auxiliary space.

### How it works internally

1. **Counting Sort**:
   - Count occurrences of each key into a frequency array of size $k$.
   - Convert the frequencies into prefix sums (cumulative counts). The prefix sum at index $i$ tells us the exact ending position of key $i$ in the output array.
   - Iterate backward through the input array and place each element at `output[count[element] - 1]`, decrementing the count. Iterating backward guarantees stability.

2. **Radix Sort (LSD)**:
   - Break multi-digit keys into individual digits (base $b$, typically 10 or $2^{16}$).
   - Sort items stably by the least significant digit (LSD) up to the most significant digit (MSD) using a stable subroutine like Counting Sort.
   - Stability preserves the relative order established by previous passes, guaranteeing correctness after $d$ passes.

3. **Bucket Sort**:
   - Partition the range into $m$ equally sized intervals (buckets).
   - Distribute $n$ elements into their respective buckets based on a mapping function (e.g., $\lfloor n \times x \rfloor$).
   - Sort individual buckets (often with Insertion Sort or Recursion) and concatenate the results.

### Common mistakes

- Ignoring negative numbers in Counting Sort: indices cannot be negative, so values must be shifted by subtracting the minimum value.
- Losing stability in Radix Sort: if the intermediate digit-sorting subroutine is not stable, the sorting of more significant digits destroys the sorting of less significant digits.
- Iterating forward instead of backward during the placement phase of Counting Sort, which breaks stability.
- Assuming Bucket Sort is always $O(n)$: if data clusters heavily in a single bucket, worst-case time degrades to $O(n^2)$.

### Real-world applications

- Suffix Array Construction: Radix Sort is used in DC3 / Skew algorithms to sort suffixes in $O(n)$ time.
- Database Column Sorts: Low-cardinality columns (e.g., status codes, flags, small integer IDs) are sorted using Counting Sort.
- GPU Sorting: Parallel Radix Sort is widely implemented in CUDA (e.g., NVIDIA CUB/Thrust) as it is highly data-parallel without divergence.
- Graphics Pipeline / Z-buffering: Depth sorting of translucent primitives can be done rapidly with bucket sort.

## Example

Suppose we want to stably sort `A = [4, 2, 2, 8, 3, 3, 1]` using Counting Sort:

1. Find range: `min = 1`, `max = 8`, range $k = 8$.
2. Create count array for values 1 through 8:
   Index:  1  2  3  4  5  6  7  8
   Count: [1, 2, 2, 1, 0, 0, 0, 1]
3. Compute cumulative counts (prefix sums):
   Pref:  [1, 3, 5, 6, 6, 6, 6, 7]
   This indicates: '1' goes up to index 0, '2' goes up to index 2, '3' up to index 4, etc.
4. Build output by iterating backwards through `A`:
   - Take 1: `pref[1] = 1` -> place at index 0. `pref[1]` becomes 0.
   - Take 3: `pref[3] = 5` -> place at index 4. `pref[3]` becomes 4.
   - Take 3: `pref[3] = 4` -> place at index 3. `pref[3]` becomes 3.
   - Take 8: `pref[8] = 7` -> place at index 6. `pref[8]` becomes 6.
   - Take 2: `pref[2] = 3` -> place at index 2. `pref[2]` becomes 2.
   - Take 2: `pref[2] = 2` -> place at index 1. `pref[2]` becomes 1.
   - Take 4: `pref[4] = 6` -> place at index 5. `pref[4]` becomes 5.
Result: `[1, 2, 2, 3, 3, 4, 8]`.

## Visual Explanation

```text
Counting Sort Placement:

Input array: [3, 1, 3, 2]

Frequencies: 
  val:   1  2  3
  count: 1  1  2

Prefix sums (1-based positions):
  val:   1  2  3
  pref:  1  2  4

Placement (reading Input backwards):
1. Read 2: pref[2] = 2 -> out[1] = 2; pref[2] becomes 1
   Output: [_, 2, _, _]
2. Read 3: pref[3] = 4 -> out[3] = 3; pref[3] becomes 3
   Output: [_, 2, _, 3]
3. Read 1: pref[1] = 1 -> out[0] = 1; pref[1] becomes 0
   Output: [1, 2, _, 3]
4. Read 3: pref[3] = 3 -> out[2] = 3; pref[3] becomes 2
   Output: [1, 2, 3, 3]
```

## Complexity

- **Time Complexity:** Counting Sort: O(n + k) where k is the range of values. Radix Sort: O(d * (n + b)) where d is the number of digits and b is the base. Bucket Sort: O(n + k) average when uniformly distributed, O(n^2) worst case.
- **Space Complexity:** Counting Sort: O(n + k) auxiliary space for output and count array. Radix Sort: O(n + b). Bucket Sort: O(n + m) for m buckets.

When k = O(n), Counting Sort runs in strictly linear time. In Radix Sort, if keys are 32-bit integers and we choose a base of b = 2^16, d = 32 / 16 = 2 passes, making it O(2 * (n + 2^16)) = O(n) with very low constant factors.

## Interview Perspective

1. **Why does Radix Sort process digits from Least Significant Digit (LSD) to Most Significant Digit (MSD) rather than the other way around?**
   <details><summary>What a strong answer covers</summary>

   LSD works because the underlying sort is stable. When we sort by digit i, all elements with equal digit i retain the relative order determined by digits 0 through i - 1. MSD can also work, but it requires recursive bucket partitioning, which incurs significant recursion and sub-array allocation overhead.

   </details>
2. **Can we sort arbitrary 32-bit floating point numbers with Radix Sort?**
   <details><summary>What a strong answer covers</summary>

   Yes. IEEE 754 floating point numbers are designed such that their binary representations roughly preserve order. For non-negative floats, their bitwise representation sorts identically to unsigned integers. For negative floats, inverting the bits (or flipping the sign bit) aligns them with standard order.

   </details>
3. **How do you handle negative numbers in Counting Sort?**
   <details><summary>What a strong answer covers</summary>

   Find both the minimum and maximum values in the array. Shift all numbers by `-min_val` so that the minimum maps to index 0, allocating an array of size `max_val - min_val + 1`. When writing elements back, add `min_val`.

   </details>
4. **What is the lower bound of comparison-based sorting and why doesn't Counting Sort violate it?**
   <details><summary>What a strong answer covers</summary>

   Comparison sorts require \Omega(n \log n) comparisons because there are n! permutations, requiring a decision tree of depth \log_2(n!). Counting Sort uses direct array indexing (random access memory) instead of comparisons, accessing information beyond binary comparisons.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Sort Colors and Frequencies](exercises/problem-01.md) | Easy | Counting Sort with shift offset and key preservation | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Sort Pairs by Secondary Key Stably](exercises/problem-02.md) | Easy/Medium | Stable Counting Sort using prefix sums | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Radix Sort 32-bit Integers](exercises/problem-03.md) | Medium | LSD Radix Sort with bitwise shifts or base representation | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Uniform Bucket Sort](exercises/problem-04.md) | Medium/Hard | Bucket Sort with uniform distribution normalization | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Maximum Gap in Linear Time](exercises/problem-05.md) | Hard | Pigeonhole Principle with Bucket Partitioning | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-037
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: counting-sort, stable-sorting, radix-sort-lsd, bucket-sort, linear-sorting-limits*
