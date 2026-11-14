# Day 36: Day 36: Heap Sort

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 36 | 2026-11-14 | Sorting | New topic | progressive | Python 3.12 |

Heap Sort bridges tree-based thinking and array manipulation to achieve deterministic $O(n \log n)$ time with $O(1)$ auxiliary space. By viewing an ordinary array as an implicit complete binary tree, it builds a max-heap and systematically extracts elements into place. Today, you will master the mechanics of heapify, sift-down, and the in-place sorting loop.

## Topic

**Heap Sort**: heapify, sift down, in-place heap sort, complexity guarantees

## Learning Objectives

By the end of this lesson you should be able to:

- Map parent-child relationships in an array-represented complete binary tree using 0-based indexing arithmetic.
- Implement the sift-down (`heapify`) routine iteratively and recursively to restore the max-heap invariant.
- Construct a max-heap in linear $O(n)$ time using bottom-up building.
- Execute the full in-place Heap Sort algorithm in $O(n \log n)$ time and $O(1)$ auxiliary space.
- Analyze the trade-offs of Heap Sort compared to Quick Sort and Merge Sort regarding cache locality and stability.

## Concept Explanation

### What it is

Heap Sort is a comparison-based sorting algorithm that organizes an array into a specialized binary tree structure called a **Max-Heap**, then repeatedly moves the maximum element to the back of the array. The magic lies in the fact that no actual nodes, pointers, or tree objects are created: the complete binary tree is completely implicit inside the existing contiguous array.

### Why it exists

Merge Sort guarantees $O(n \log n)$ time in all cases, but requires $O(n)$ auxiliary memory for temporary buffers. Quick Sort sorts in place with $O(1)$ extra space (discounting the call stack), but suffers from an $O(n^2)$ worst-case time complexity. Heap Sort gives you the best of both theoretical worlds: an unconditional $O(n \log n)$ worst-case time guarantee paired with strictly $O(1)$ auxiliary space.

### When to use it

Use Heap Sort when you need a guaranteed $O(n \log n)$ runtime bound without the risk of quadratic degradation, and where memory is severely constrained such that an $O(n)$ allocation (like in Merge Sort) is unacceptable (e.g., embedded systems, operating system kernels, or real-time systems).

### When NOT to use it

Do not use Heap Sort if stability is required (Heap Sort scrambles equal keys). Furthermore, in typical modern desktop/server hardware, Quick Sort and introsort variants significantly outperform Heap Sort in practice because Heap Sort jumps around array indices non-sequentially, destroying CPU cache locality.

### How it works internally

1. **Implicit Tree Representation**: For an element at index `i` (0-based):
   - Left child is at `2 * i + 1`
   - Right child is at `2 * i + 2`
   - Parent is at `(i - 1) // 2`

2. **Max-Heap Property**: For every index `i`, `arr[i] >= arr[2*i + 1]` and `arr[i] >= arr[2*i + 2]` (whenever children exist). The largest element is always at index `0`.

3. **Phase 1: Build Max-Heap**: Transform the unsorted array into a max-heap. Rather than inserting elements one by one, we run `sift_down` starting from the last internal node `(n // 2) - 1` backwards down to index `0`. This runs in $O(n)$ time.

4. **Phase 2: Extract & Shrink**: 
   - Swap `arr[0]` (the current max) with `arr[end]`, where `end` initially is `n - 1`.
   - Now the largest element is placed in its final sorted position at index `end`.
   - Reduce the active heap size by 1 (the heap is now `arr[0 ... end - 1]`).
   - The new root `arr[0]` likely violates the max-heap property, so call `sift_down` on index `0` within the range `0 ... end - 1`.
   - Repeat until the heap size reduces to 1.

### Common mistakes

- Calculating child indices using 1-based indexing formulas (`2*i` and `2*i + 1`) instead of 0-based indexing (`2*i + 1` and `2*i + 2`).
- Building the heap top-down via insertions ($O(n \log n)$) rather than bottom-up via sift-down ($O(n)$).
- Forgetting to pass the dynamic heap boundary size `heap_size` to `sift_down`, causing the routine to overwrite or compare against elements already sorted at the end of the array.
- Assuming Heap Sort is stable; elements with equal keys can be jumped over large distances during child-parent swaps.

### Real-world applications

- Linux Kernel: Used in sorting tasks where dynamic memory allocation could fail or cause memory fragmentation.
- Introsort (Standard C++ `std::sort`): Used as a fallback whenever Quick Sort exceeds a recursion depth of $2 \lfloor \log_2 n \rfloor$, guaranteeing worst-case $O(n \log n)$ performance.
- Embedded Systems: Ideal for microcontrollers with strict RAM limits where $O(n)$ auxiliary buffer allocation is impossible.

## Example

Let's trace sorting `arr = [4, 10, 3, 5, 1]`.

### Step 1: Build Max-Heap
- Array length $n = 5$. Last non-leaf index is `(5 // 2) - 1 = 1`.
- Sift-down at index 1 (`arr[1] = 10`): Children are `arr[3] = 5`, `arr[4] = 1`. 10 is greater than both. Heap property holds.
- Sift-down at index 0 (`arr[0] = 4`): Children are `arr[1] = 10`, `arr[2] = 3`. Largest child is 10 at index 1. Swap `arr[0]` and `arr[1]`. `arr` becomes `[10, 4, 3, 5, 1]`. Sift-down continues at index 1 with value 4: children are `5` and `1`. Largest child is 5 at index 3. Swap 4 and 5. `arr` becomes `[10, 5, 3, 4, 1]`.
- Array is now a valid max-heap: `[10, 5, 3, 4, 1]`.

### Step 2: Extract Maximum Elements
- **Iteration 1 (end = 4)**:
  - Swap `arr[0]` (10) and `arr[4]` (1): `[1, 5, 3, 4, 10]`. (10 is sorted!)
  - Sift-down index 0 in heap range `[0..3]`: 1 swaps with 5 at index 1 -> `[5, 1, 3, 4, 10]`. Then 1 swaps with 4 at index 3 -> `[5, 4, 3, 1, 10]`.
- **Iteration 2 (end = 3)**:
  - Swap `arr[0]` (5) and `arr[3]` (1): `[1, 4, 3, 5, 10]`. (5 is sorted!)
  - Sift-down index 0 in range `[0..2]`: 1 swaps with 4 at index 1 -> `[4, 1, 3, 5, 10]`.
- **Iteration 3 (end = 2)**:
  - Swap `arr[0]` (4) and `arr[2]` (3): `[3, 1, 4, 5, 10]`. (4 is sorted!)
  - Sift-down index 0 in range `[0..1]`: 3 is larger than child 1. Heap intact.
- **Iteration 4 (end = 1)**:
  - Swap `arr[0]` (3) and `arr[1]` (1): `[1, 3, 4, 5, 10]`.

Sorted result: `[1, 3, 4, 5, 10]`.

## Visual Explanation

```text
Array: [4, 10, 3, 5, 1]
Implicit Tree Indices:
        0
      /   \
     1     2
    / \
   3   4

Build Max-Heap:
       10
      /  \
     5    3       Array: [10, 5, 3, 4, 1]
    / \
   4   1

Swap root 10 with last element 1; shrink heap range to 4:
       1                  Array: [1, 5, 3, 4 | 10]
      / \
     5   3
    /
   4

Sift down 1:
       5                  Array: [5, 4, 3, 1 | 10]
      / \
     4   3
    /
   1
```

## Complexity

- **Time Complexity:** Build-heap takes O(n) because most nodes reside near the leaves with small heights; extracting n-1 elements takes (n-1) * O(log n) = O(n log n). Total time is O(n log n) across all best, average, and worst cases.
- **Space Complexity:** O(1) auxiliary space because transformations and sift-downs occur directly via in-place swaps inside the input array without allocating extra buffers.

Unlike Quick Sort, Heap Sort has no bad pivot choice and never degrades to $O(n^2)$. However, while Quick Sort accesses elements sequentially with high cache locality, Heap Sort constantly jumps by powers of 2 (indices $i \to 2i+1$), causing frequent CPU cache misses. Therefore, Quick Sort is usually faster in wall-clock time on modern hardware.

## Interview Perspective

1. **Why does building a heap from an array run in O(n) time instead of O(n log n)?**
   <details><summary>What a strong answer covers</summary>

   Explain that nodes at lower levels have shorter sift-down paths. Roughly n/2 nodes are leaves (height 0), n/4 have height 1, n/8 have height 2. The summation sum_{h=0}^{log n} (n / 2^{h+1}) * h converges mathematically to O(n).

   </details>
2. **Is Heap Sort a stable sorting algorithm? Why or why not?**
   <details><summary>What a strong answer covers</summary>

   No. Explain that during both sift-down and root-with-tail swapping, equal elements can jump across each other without preserving their relative original order.

   </details>
3. **How does Introsort leverage Heap Sort?**
   <details><summary>What a strong answer covers</summary>

   Introsort begins with Quick Sort for high cache performance, monitors the recursion depth, and switches to Heap Sort if the depth exceeds 2 * floor(log2(n)). This prevents Quick Sort's worst-case O(n^2) degradation while preserving its average-case speed.

   </details>
4. **Can you implement Heap Sort without using recursion for sift-down?**
   <details><summary>What a strong answer covers</summary>

   Yes, sift-down is inherently tail-recursive, so it can trivially be expressed as a simple `while` loop that terminates when the current node is larger than all its children or has no children left.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Validate Max-Heap Array](exercises/problem-01.md) | Easy | Implicit Tree Representation & Max-Heap Invariant | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [In-Place Max-Heapify Subtree](exercises/problem-02.md) | Easy/Medium | Sift-Down / Heapify Routine | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Classic In-Place Heap Sort](exercises/problem-03.md) | Medium | Full Heap Sort Algorithm | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Sort K-Messed Array](exercises/problem-04.md) | Medium/Hard | Bounded Heap Sorting Window | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [In-Place Partial Selection Sort via Heap](exercises/problem-05.md) | Hard | Partial Heap Sort for Top-K Elements | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-036
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: Implicit Binary Tree Array Indexing, Max-Heap Property, Sift-Down (Heapify), Linear-Time Heap Construction, In-Place Sorting, Comparative Cache Locality Analysis*
