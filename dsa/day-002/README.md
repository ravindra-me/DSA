# Day 2: Arrays: Memory Layout, Dynamic Resizing, and Multi-Dimensional Grids

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 2 | 2026-10-11 | Fundamentals | New topic | progressive | Python 3.12 |

Arrays are the most fundamental building block in computer science, storing elements in contiguous memory blocks. Because memory is laid out sequentially, arrays grant instantaneous $O(1)$ random access by index, but require deliberate trade-offs when inserting or resizing. Mastering array manipulation, in-place updates, and multi-dimensional grid traversals forms the foundation for nearly all advanced data structures.

## Topic

**Arrays**: indexing, traversal, in-place updates, dynamic arrays, 2D arrays

## Learning Objectives

By the end of this lesson you should be able to:

- Explain how contiguous memory allocation enables $O(1)$ constant-time random access via index arithmetic.
- Understand the internal resizing mechanics and amortized $O(1)$ push behavior of dynamic arrays (such as Python lists).
- Perform in-place mutations and element traversals without allocating auxiliary memory.
- Navigate 2D arrays (matrices) using row-major indexing, boundary manipulation, and coordinate transformations.

## Concept Explanation

### What it is

An array is a linear collection of elements stored side-by-side in a contiguous block of physical memory. Imagine a row of numbered lockers on a wall: if you know where locker 0 starts and the width of each locker, you can jump directly to locker 42 with a single calculation (`base_address + index * element_size`). In Python, the built-in `list` is actually a **dynamic array** that stores contiguous references (pointers) to objects and automatically expands its capacity when full.

### Why it exists

Without arrays, storing related data would require tracking disconnected memory addresses independently (like a treasure hunt where every item tells you where the next one is). This would eliminate the ability to jump directly to the $k$-th item in constant time. Contiguous storage also leverages hardware-level CPU caching: fetching an element automatically loads adjacent elements into the high-speed CPU cache, vastly accelerating sequential traversal.

### When to use it

Use arrays when you need direct, instantaneous access by index ($O(1)$ lookup), when the total collection size is relatively stable or elements are mostly appended to the end, or when you need cache-friendly sequential scans over numeric or ordered sequences.

### When NOT to use it

Avoid basic arrays when you frequently insert or delete elements at arbitrary positions (especially the beginning or middle), because this forces every subsequent element to shift, taking $O(n)$ time. For frequent head insertions, use a doubly-linked list or `collections.deque`. If you need fast key-based lookups rather than index-based access, use a hash map (`dict`) or hash set (`set`).

### How it works internally

1. **Static Memory Allocation**: When allocated, an array claims a fixed contiguous slice of memory: `address(i) = base + (i * size)`. This formula executes in $O(1)$ time regardless of $i$.
2. **Dynamic Array Resizing**: A dynamic array maintains a `capacity` (allocated slots) and a `size` (occupied slots). When `size == capacity`, appending requires allocating a new memory block (typically $1.5\times$ to $2\times$ the size), copying all existing elements, freeing the old memory, and updating the pointer. While a single resize costs $O(n)$, resizing happens infrequently enough that appending averages to $O(1)$ amortized time.
3. **2D Arrays (Matrices)**: A 2D array of dimensions $R \times C$ represents a grid. In contiguous row-major layout, cell $(r, c)$ maps to index `r * C + c`. In Python, a 2D array is typically a list of list references: `matrix[r][c]` accesses row `r` then column `c`.

### Common mistakes

- Creating 2D arrays using shallow copies (e.g., `[[0] * c] * r`), which replicates references to the *same* inner list; mutating one row mutates every row. Always use list comprehensions: `[[0] * c for _ in range(r)]`.
- Modifying an array's length (inserting or deleting with `.pop()` or `.remove()`) while iterating over it with a `for` loop, causing skipped elements or out-of-bounds indexing.
- Assuming operations like `list.insert(0, val)` or `val in list` are $O(1)$. Shifting elements takes $O(n)$, and linear search in unsorted lists is $O(n)$.
- Off-by-one errors during boundary traversal (e.g., stopping at `len(arr) - 1` vs `len(arr)`).

### Real-world applications

- Operating System Page Tables: Using virtual page numbers as array indices to map virtual memory to physical addresses.
- Computer Graphics & Image Processing: Storing pixels as 2D and 3D arrays of RGB values for matrix transformations and rendering.
- Database Execution Engines: Columnar storage formats (like Apache Parquet) store column values contiguously for lightning-fast vectorized CPU operations.

## Example

Let us trace dynamic array resizing. Suppose an empty dynamic array starts with capacity 2:
1. Append 10: `[10, _]`, size = 1, capacity = 2.
2. Append 20: `[10, 20]`, size = 2, capacity = 2. Array is full.
3. Append 30: Capacity is doubled to 4. A new block of size 4 is allocated. 10 and 20 are copied over. 30 is inserted: `[10, 20, 30, _]`. Size = 3, capacity = 4.
Notice that step 3 incurred 2 element copies. However, the next append (40) will take exactly 1 operation without copying.

## Visual Explanation

```text
Contiguous 1D Array in Memory:
Index:      0       1       2       3
Memory:  [0x100] [0x104] [0x108] [0x10C]
Value:   |  42  |  15  |  88  |   7  |
Address Formula: Address(i) = 0x100 + i * 4 bytes

Dynamic Array Doubling:
Step 1: [ A | B ] (Full: size=2, cap=2)
Step 2: Allocate [ _ | _ | _ | _ ] (New cap=4)
Step 3: Copy:    [ A | B | _ | _ ]
Step 4: Append C:[ A | B | C | _ ] (size=3, cap=4)

2D Array (3x3 Grid) Row-Major Layout:
Row 0: [ (0,0), (0,1), (0,2) ]
Row 1: [ (1,0), (1,1), (1,2) ]
Row 2: [ (2,0), (2,1), (2,2) ]
Flat Index = row * num_cols + col
```

## Complexity

- **Time Complexity:** Random Access: $O(1)$ via direct address calculation; Append: Amortized $O(1)$ ($O(n)$ worst-case resize); Arbitrary Insertion/Deletion: $O(n)$ due to shifting elements; Traversal: $O(n)$ to visit every element once.
- **Space Complexity:** $O(n)$ auxiliary space to store $n$ elements in contiguous memory. Dynamic arrays typically allocate up to $2n$ slots (a constant factor overhead).

Amortized analysis proves that over any sequence of $N$ appends starting from an empty array, the total number of element moves is at most $2N$. Therefore, the average cost per append is $O(1)$, despite sporadic $O(n)$ spikes during reallocation.

## Interview Perspective

1. **Why does a dynamic array double its size upon reaching capacity instead of growing by a fixed constant amount (e.g., adding 50 slots)?**
   <details><summary>What a strong answer covers</summary>

   Doubling ensures amortized $O(1)$ appends because resizing costs are spread geometrically across exponentially growing numbers of cheap operations. Adding a constant size $K$ causes $O(n^2)$ total work over $n$ appends, degrading average append time to $O(n)$.

   </details>
2. **What is the difference between a Python list and a NumPy array under the hood?**
   <details><summary>What a strong answer covers</summary>

   A Python list is a dynamic array of object pointers (adding memory overhead and cache misses due to pointer indirection). A NumPy array stores raw, uniform C primitive data types (like 32-bit floats) directly contiguous in memory without pointer boxing, enabling SIMD vectorization and cache locality.

   </details>
3. **How do you delete an element from the middle of an array in $O(1)$ time if order does not need to be preserved?**
   <details><summary>What a strong answer covers</summary>

   Swap the element to be deleted with the very last element of the array, then call `.pop()` to remove the last element. This avoids the $O(n)$ shift of subsequent elements.

   </details>
4. **Why does traversing a 2D matrix row-by-row execute significantly faster than column-by-column in languages like C or Python?**
   <details><summary>What a strong answer covers</summary>

   Row-major storage aligns row elements contiguously in physical memory. Traversing row-by-row exploits spatial locality, loading multiple contiguous elements into CPU cache lines. Column-by-column jumps across rows, causing frequent cache misses.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Remove Element In-Place](exercises/problem-01.md) | Easy | in-place updates and overwrite pointers | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Rotate Array by K Steps](exercises/problem-02.md) | Easy/Medium | in-place array reversal and index wrapping | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Spiral Matrix Traversal](exercises/problem-03.md) | Medium | 2D array boundary simulation | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Set Matrix Zeroes](exercises/problem-04.md) | Medium/Hard | 2D array state encoding and memory optimization | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [First Missing Positive](exercises/problem-05.md) | Hard | index-as-hash-key / cycle placement in-place | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-002
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: contiguous-memory, indexing, dynamic-arrays, amortized-complexity, in-place-mutation, 2d-arrays*
