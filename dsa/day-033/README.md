# Day 33: Merge Sort: Divide, Conquer, and Inversion Counting

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 33 | 2026-11-11 | Sorting | New topic | progressive | Python 3.12 |

Merge Sort is the canonical divide-and-conquer sorting algorithm that achieves an optimal $O(n \log n)$ time complexity in all cases. By recursively breaking an array into halves and merging sorted subarrays using a linear two-pointer scan, it delivers guaranteed performance and stable ordering. Mastering merge sort also unlocks fundamental algorithms for counting inversions, external sorting of massive datasets, and sorting linked structures.

## Topic

**Merge Sort**: divide and conquer, merging sorted halves, stability, counting inversions, external sorting

## Learning Objectives

By the end of this lesson you should be able to:

- Implement the recursive divide-and-conquer merge sort algorithm from scratch without memory leaks.
- Explain why merge sort is guaranteed $O(n \log n)$ time in best, worst, and average cases.
- Identify and leverage the stability property of merge sort in composite data sorts.
- Modify the merge step to solve cross-subarray counting problems like inversion counting in $O(n \log n)$.
- Understand the external merge sort paradigm used for sorting datasets that exceed RAM capacity.

## Concept Explanation

### What it is

Merge Sort is a comparison-based sorting algorithm built on the **divide-and-conquer** algorithmic paradigm. Instead of repeatedly shifting or swapping elements locally (like bubble sort or insertion sort), merge sort splits an unsorted list into two equal halves, recursively sorts both halves, and then merges the two independently sorted halves into a single unified sorted sequence using two pointers.

### Why it exists

Elementary sorts like insertion sort, selection sort, and bubble sort suffer from $O(n^2)$ worst-case time complexity, making them completely unviable for large datasets ($n > 10^4$). Furthermore, while Quick Sort averages $O(n \log n)$, its worst case degrades to $O(n^2)$ on unfavorable pivot selections. Merge Sort was designed by John von Neumann in 1945 to provide a rigorous, mathematically guaranteed $O(n \log n)$ bound regardless of initial input order, while preserving the relative ordering of equal elements (stability).

### When to use it

Use Merge Sort when you need a guaranteed worst-case time bound of $O(n \log n)$ and stability is required. It is especially ideal for sorting singly linked lists (where merging can be done in $O(1)$ extra memory by rearranging pointers) and external sorting (when datasets are too large to fit in physical RAM and must be streamed from disk). It is also the classic foundation for counting inversions or reverse pairs in arrays.

### When NOT to use it

Avoid Merge Sort on contiguous arrays when auxiliary memory is strictly constrained ($O(1)$ extra memory required), as standard array merge sort requires $O(n)$ auxiliary space to stage merged elements. In pure in-memory cache-sensitive array sorting where stability is not strictly required, introsort or dual-pivot quicksort often exhibit better constant-factor speeds due to in-place partition cache locality. For tiny arrays ($n < 20$), insertion sort is faster due to negligible overhead.

### How it works internally

1. **Divide**: Calculate the midpoint `mid = (left + right) // 2` and split the range `[left, right]` into two subranges: `[left, mid]` and `[mid + 1, right]`.
2. **Conquer**: Recursively call merge sort on each half until the base case is reached: a subarray of length 0 or 1, which is inherently sorted.
3. **Combine (Merge)**: Allocate temporary space (or use an auxiliary buffer). Place pointer `i` at the start of the left half and pointer `j` at the start of the right half. Compare `arr[i]` and `arr[j]`. Append the smaller element (or the left element if equal, to preserve stability) into the merged result and advance that pointer. Once one half is exhausted, append all remaining items from the other half.
4. **Invariance**: At the end of each merge step, the merged range `[left, right]` is guaranteed to be in non-decreasing order.

### Common mistakes

- Breaking stability by taking `arr[j]` when `arr[i] == arr[j]`. Always favor the left element on equality (`arr[i] <= arr[j]`) to preserve original relative order.
- Allocating new list slices (`arr[:mid]`, `arr[mid:]`) at every single recursive stack frame. This creates excessive garbage collection pressure; allocate one reusable auxiliary array upfront instead.
- Off-by-one errors when computing indices: ensure the division partitions `[left, mid]` and `[mid + 1, right]` without overlaps or infinite recursion when `right = left + 1`.
- Forgetting to copy remaining elements after the two-pointer loop terminates when one side is exhausted.

### Real-world applications

- Timsort: The default sorting algorithm in Python (`list.sort()`) and Java (`Arrays.sort()` for objects) is a hybrid of merge sort and insertion sort designed to exploit pre-existing ordered runs.
- External Merge Sort: Database management systems (e.g., PostgreSQL, MySQL) sort terabytes of index or query data exceeding RAM capacity by sorting chunk runs on disk and merging them with a k-way merge.
- Linked List Sorting: Used in standard libraries and kernel data structures (e.g., Linux kernel linked lists) to achieve guaranteed $O(n \log n)$ without requiring $O(n)$ extra auxiliary buffer.

## Example

Let's trace sorting `[38, 27, 43, 3, 9, 82, 10]`:

1. **Divide Phase**:
   - `[38, 27, 43, 3, 9, 82, 10]` splits into `L: [38, 27, 43, 3]` and `R: [9, 82, 10]`.
   - `L` splits into `[38, 27]` and `[43, 3]`. Sub-splits yield singletons `[38]`, `[27]`, `[43]`, `[3]`.
   - `R` splits into `[9, 82]` and `[10]`. Sub-splits yield `[9]`, `[82]`, `[10]`.

2. **Conquer & Merge Phase**:
   - Merge `[38]` and `[27]`: compare 38 and 27 -> `[27, 38]`.
   - Merge `[43]` and `[3]`: compare 43 and 3 -> `[3, 43]`.
   - Merge `[27, 38]` and `[3, 43]`:
     - Compare 27 and 3: take 3. Remaining: `[27, 38]`, `[43]`.
     - Compare 27 and 43: take 27. Remaining: `[38]`, `[43]`.
     - Compare 38 and 43: take 38. Exhausted left half.
     - Copy remaining: take 43 -> `[3, 27, 38, 43]`.
   - Similarly, merge `[9]` and `[82]` -> `[9, 82]`. Merge with `[10]` -> `[9, 10, 82]`.
   - Final merge of `[3, 27, 38, 43]` and `[9, 10, 82]`:
     - Compare 3 and 9 -> 3
     - Compare 27 and 9 -> 9
     - Compare 27 and 10 -> 10
     - Compare 27 and 82 -> 27
     - Compare 38 and 82 -> 38
     - Compare 43 and 82 -> 43
     - Copy remaining 82 -> `[3, 9, 10, 27, 38, 43, 82]`.

## Visual Explanation

```text
DIVIDE (Recursion Tree):
                 [38, 27, 43, 3, 9, 82, 10]
                        /          \
             [38, 27, 43, 3]      [9, 82, 10]
                /      \             /      \
            [38, 27]  [43, 3]     [9, 82]   [10]
             /   \     /   \       /   \
           [38] [27] [43]  [3]   [9]  [82]

MERGE (Two-pointer merge step):
  Left:  [ 27, 38 ]       Right: [ 3, 43 ]
           ^                       ^
         ptrL                    ptrR
  Compare 27 vs 3 -> pick 3 from Right, advance ptrR
  Left:  [ 27, 38 ]       Right: [ 3, 43 ]
           ^                          ^
         ptrL                       ptrR
  Compare 27 vs 43 -> pick 27 from Left, advance ptrL
  Result buffer: [ 3, 27, 38, 43 ]
```

## Complexity

- **Time Complexity:** Merge step takes $O(n)$ work per recursion level; the tree depth is $\lceil\log_2 n\rceil$. Total time is $O(n \log n)$ for all best, average, and worst cases.
- **Space Complexity:** $O(n)$ auxiliary array space to stage merged elements during merging, plus $O(\log n)$ stack frames for recursion depth.

Unlike Quicksort, Merge Sort's time complexity does not depend on lucky pivot choices: it splits strictly at the middle index, ensuring a balanced recursion tree of height $\log_2 n$. For arrays, the $O(n)$ space requirement is its primary drawback; for linked lists, merge sort requires only $O(\log n)$ stack space and $O(1)$ extra node allocations.

## Interview Perspective

1. **What is sorting stability, why does Merge Sort possess it, and when does it matter?**
   <details><summary>What a strong answer covers</summary>

   A sorting algorithm is stable if elements with identical keys maintain their original relative order. Merge Sort is stable as long as the merge step chooses the left element whenever `arr[left_ptr] <= arr[right_ptr]`. This is critical when multi-pass sorting records (e.g. sorting students by grade, then by last name).

   </details>
2. **How can Merge Sort be modified to count the number of inversions in an array?**
   <details><summary>What a strong answer covers</summary>

   An inversion is a pair $(i, j)$ such that $i < j$ and $arr[i] > arr[j]$. During the merge step, if an element from the right subarray $arr[j]$ is smaller than $arr[i]$ from the left subarray, then all remaining elements in the left subarray from $i$ through $mid$ are also greater than $arr[j]$. Hence, exactly $(mid - i + 1)$ inversions are formed and can be accumulated in $O(1)$ per right-element pick.

   </details>
3. **Why is Merge Sort preferred over Quicksort for sorting singly linked lists?**
   <details><summary>What a strong answer covers</summary>

   Linked lists lack $O(1)$ random access, making Quicksort partitioning slow and awkward. In contrast, finding the middle of a linked list takes $O(n)$ with slow/fast pointers, and merging two sorted lists requires only pointer rewiring with $O(1)$ auxiliary memory without copying values.

   </details>
4. **What is External Merge Sort and how does it handle datasets larger than main memory?**
   <details><summary>What a strong answer covers</summary>

   External merge sort splits massive data from disk into chunks that fit into memory, sorts each chunk in RAM (e.g., using quicksort or mergesort), and writes them back to disk as 'runs'. It then uses a k-way merge (often powered by a min-heap) to stream the sorted runs into a final sorted output file with bounded RAM.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Merge Two Sorted Lists](exercises/problem-01.md) | Easy | Core merging operation of Merge Sort applied to linked structures | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Stable Merge Sort on Key-Value Pairs](exercises/problem-02.md) | Easy/Medium | Implementing out-of-place merge sort while preserving stability | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Sort Linked List in O(n log n)](exercises/problem-03.md) | Medium | Divide-and-conquer merge sort on singly linked lists with O(1) auxiliary node space | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Count Global Inversions](exercises/problem-04.md) | Medium/Hard | Augmenting the merge step to count cross-inversions in O(n log n) | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Simulate External K-Way Merge Sort](exercises/problem-05.md) | Hard | Chunk-based external sorting and multiway merging with bounded memory buffer | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-033
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: divide-and-conquer, merging-sorted-arrays, sorting-stability, inversion-counting, external-sorting-simulation*
