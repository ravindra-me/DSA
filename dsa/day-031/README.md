# Day 31: Day 31: Elementary Sorting Algorithms (Bubble, Selection, and Insertion Sort)

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 31 | 2026-11-09 | Sorting | New topic | progressive | Python 3.12 |

Sorting organizes data into a monotonic order so search, deduplication, and aggregation become fast. Bubble, Selection, and Insertion Sort are foundational $O(n^2)$ comparison-based algorithms that teach crucial concepts: in-place mutations, loop invariants, algorithm stability, and adaptive performance on nearly-sorted data.

## Topic

**Bubble, Selection & Insertion Sort**: bubble sort, selection sort, insertion sort, stability, in-place sorting, nearly-sorted input

## Learning Objectives

By the end of this lesson you should be able to:

- Distinguish between in-place algorithms and stable sorting algorithms, giving examples where stability matters.
- Implement Bubble Sort with early exit optimization, analyzing why it runs in $O(n)$ time on sorted arrays.
- Implement Selection Sort and explain why its number of memory writes is minimal ($O(n)$ swaps) but inherently unstable in array form.
- Implement Insertion Sort, proving its loop invariant and demonstrating its optimal $O(n + k)$ performance on arrays with $k$ inversions.
- Select the right elementary sorting algorithm when constrained by write endurance, input size, or partial ordering.

## Concept Explanation

### What it is

Comparison sorting rearranges an array of elements using pairwise comparisons (`<` or `>`). The three elementary sorts take three distinct approaches to this task:

1. **Bubble Sort**: Compares adjacent elements repeatedly, swapping them if out of order. With each full pass, the largest remaining element 'bubbles up' to its correct final index at the end of the array.
2. **Selection Sort**: Scans the unsorted suffix to find the absolute minimum value, then swaps it once into its designated position at the beginning of the unsorted suffix.
3. **Insertion Sort**: Mimics how people arrange playing cards in hand. It maintains a sorted prefix on the left and takes the next unsorted card, sliding it leftward into its correct relative position among the already-sorted cards.

### Why it exists

Without an understanding of elementary sorting, the core mechanics of algorithmic efficiency and trade-offs remain opaque. While modern systems often use hybrid $O(n \log n)$ algorithms like Timsort or Introsort, those very algorithms use Insertion Sort as their base case for small arrays (typically $n \le 32$ or $64$). Elementary sorts also introduce two pivotal computer science concepts:
- **Stability**: Elements with equal keys retain their original relative order. (Crucial when sorting records with multiple criteria, like sorting by name, then by age).
- **Adaptivity**: Algorithms that run faster when the input is already or nearly sorted.

### When to use it

- **Very small arrays ($n \le 32$ to $64$)**: Insertion sort has minimal constant factor overhead, no recursion, and excellent cache locality.
- **Nearly sorted arrays**: Insertion sort runs in $O(n + k)$ time where $k$ is the number of inversions. If every element is at most $c$ positions away from its target, Insertion sort runs in $O(n \cdot c)$ which is $O(n)$ for constant $c$.
- **Minimizing flash memory / EEPROM writes**: Selection sort performs at most $O(n)$ total swaps/writes, compared to up to $O(n^2)$ for Bubble and Insertion sort.

### When NOT to use it

- **Large arbitrary collections ($n > 100$)**: The average and worst-case time complexity is $O(n^2)$, which is far too slow for large inputs ($10^5$ items would take $\approx 10^{10}$ operations). Use Merge Sort, Quick Sort, or Heap Sort instead.
- **Data streams with unknown length**: Comparison sorts on fixed arrays require all elements up front. For streaming data, use min-heaps, balanced BSTs, or insertion into linked structures.

### How it works internally

All three algorithms maintain a boundary dividing the array into a sorted portion and an unsorted portion, but each updates the boundary differently:

- **Bubble Sort**:
  - Loop variable `i` goes from $0$ to $n - 1$. An inner loop compares pairs $(A[j], A[j+1])$ for $j \in [0, n - 1 - i)$.
  - If $A[j] > A[j+1]$, swap them.
  - Optimization: Track whether any swap occurred in the inner loop. If none occurred, the array is already sorted, and we break immediately (yielding $O(n)$ best-case time).
  - **Stable**: We only swap if $A[j] > A[j+1]$, never if equal.

- **Selection Sort**:
  - Outer loop `i` advances from $0$ to $n - 1$. The prefix $A[0 \dots i-1]$ is completely sorted and contains the smallest $i$ elements in their final positions.
  - Inner loop finds $\text{min\_idx} = \arg\min_{j \in [i, n-1]} A[j]$.
  - Swap $A[i]$ with $A[\text{min\_idx}]$.
  - **Unstable**: A distant swap can jump an identical element past another equal element (e.g., in `[2a, 2b, 1]`, swapping `2a` with `1` produces `[1, 2b, 2a]`).

- **Insertion Sort**:
  - Outer loop `i` advances from $1$ to $n - 1$. The subarray $A[0 \dots i-1]$ is sorted, but not necessarily in its final global positions.
  - Save `key = A[i]`. Shift all elements in $A[0 \dots i-1]$ that are greater than `key` one position to the right.
  - Place `key` into the empty spot created by the shift.
  - **Stable**: By stopping shifts when an element is $\le$ `key`, equal elements preserve relative order.

### Common mistakes

- Failing to add the early-exit boolean flag in Bubble Sort, causing it to run in $\Omega(n^2)$ even on fully sorted inputs.
- Assuming Selection Sort is stable; standard array-based Selection Sort is unstable because long-distance swaps can reorder duplicate values.
- Using swaps instead of shifts in Insertion Sort: swapping requires three assignments per step; shifting requires only one assignment per step.
- Off-by-one errors in inner loop bounds: e.g., accessing index $j+1$ when $j = n-1$ in Bubble Sort.

### Real-world applications

- Timsort (the default sorting algorithm in Python `sorted()` and Java `Arrays.sort()`): Uses Insertion Sort as its sub-routine for small runs.
- Embedded microcontrollers with write-wear flash storage: Selection Sort minimizes physical write cycles because it performs at most $n$ write swaps.
- Online sorting of real-time feeds: Insertion sort handles live streaming data inserted one item at a time into an already sorted list in $O(n)$ per item.

## Example

Consider the array: `[5, 2, 4, 6, 1, 3]`

**Tracing Insertion Sort**:
- Initial: `[5 | 2, 4, 6, 1, 3]` (prefix `[5]` is trivially sorted)
- Step $i=1$, key = 2:
  - Compare 2 with 5: 5 > 2, shift 5 right -> `[5, 5, 4, 6, 1, 3]`
  - Insert 2 at index 0 -> `[2, 5 | 4, 6, 1, 3]`
- Step $i=2$, key = 4:
  - Compare 4 with 5: 5 > 4, shift 5 right -> `[2, 5, 5, 6, 1, 3]`
  - Compare 4 with 2: 2 <= 4, stop.
  - Insert 4 at index 1 -> `[2, 4, 5 | 6, 1, 3]`
- Step $i=3$, key = 6:
  - Compare 6 with 5: 5 <= 6, stop immediately (0 shifts) -> `[2, 4, 5, 6 | 1, 3]`
- Step $i=4$, key = 1:
  - 1 is smaller than 6, 5, 4, 2. Shift all right -> `[1, 2, 4, 5, 6 | 3]`
- Step $i=5$, key = 3:
  - Shift 6, 5, 4 right. Stop at 2. Insert 3 -> `[1, 2, 3, 4, 5, 6]`

Total operations closely mirror the number of elements out of order (inversions).

## Visual Explanation

```text
Bubble Sort (Pass 1):
[ 5,  1,  4,  2,  8 ]
 (5 > 1) -> swap -> [ 1,  5,  4,  2,  8 ]
      (5 > 4) -> swap -> [ 1,  4,  5,  2,  8 ]
           (5 > 2) -> swap -> [ 1,  4,  2,  5,  8 ]
                (5 <= 8) -> keep -> [ 1,  4,  2,  5, | 8 ] (8 is locked)

Selection Sort (Step 1):
[ 5,  1,  4,  2,  8 ]
  ^                   Find min in remaining suffix [5, 1, 4, 2, 8] -> min is 1 at index 1
  Swap A[0] with A[1]:
[ 1 | 5,  4,  2,  8 ] (1 is locked)

Insertion Sort (Step i=3, inserting 2 into [1, 4, 5]):
Sorted Prefix: [ 1,  4,  5 ]   Key to insert: 2
               [ 1,  4, __,  5 ]  (5 shifted right)
               [ 1, __,  4,  5 ]  (4 shifted right)
               [ 1,  2,  4,  5 ]  (2 inserted because 1 <= 2)
```

## Complexity

- **Time Complexity:** Bubble Sort: Best $O(n)$ with swap flag, Avg/Worst $O(n^2)$. Selection Sort: $O(n^2)$ in all cases (always scans entire suffix). Insertion Sort: Best $O(n)$, Avg/Worst $O(n^2)$, specifically $O(n + k)$ for $k$ inversions.
- **Space Complexity:** All three are in-place: $O(1)$ auxiliary space, modifying the array without allocating extra collections.

Insertion sort dominates both Bubble and Selection sort in virtually every practical metric: it is stable, adaptive ($O(n)$ for sorted data), and requires approximately $n^2 / 4$ comparisons on average, compared to $n^2 / 2$ comparisons for Selection and Bubble sort.

## Interview Perspective

1. **What is sorting algorithm stability, and give a practical example where choosing an unstable sort produces a bug?**
   <details><summary>What a strong answer covers</summary>

   Stability preserves the relative order of items with identical keys. If a user sorts a table of employees by First Name and subsequently by Department using an unstable sort, the alphabetical order of First Names within the same Department is scrambled.

   </details>
2. **Why is standard array-based Selection Sort unstable, and how could it be made stable?**
   <details><summary>What a strong answer covers</summary>

   Selection sort swaps the found minimum with the current element. Swapping jumps an element across intermediate items, potentially placing an identical key after its twin. It can be made stable by shifting intermediate elements instead of swapping (similar to insertion), but that increases writes to $O(n^2)$.

   </details>
3. **If you are writing firmware for a hardware sensor that writes to EEPROM with very low write endurance, which elementary sort would you pick and why?**
   <details><summary>What a strong answer covers</summary>

   Selection Sort, because it guarantees at most $n - 1$ swaps (memory writes). Bubble Sort and Insertion Sort can perform up to $O(n^2)$ writes.

   </details>
4. **Under what condition does Insertion Sort execute in $O(n)$ time?**
   <details><summary>What a strong answer covers</summary>

   When the array is already sorted, or when each element is at most a constant distance $k = O(1)$ from its sorted position (a $k$-sorted array), or when the total number of inversions is $O(n)$.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Optimized Bubble Pass Counter](exercises/problem-01.md) | Easy | Bubble sort mechanics, early termination, and swap tracking | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Minimal Write Selection Sort](exercises/problem-02.md) | Easy/Medium | Selection sort write minimization and tracking index updates | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Sort Nearly-Sorted Array (k-Sorted)](exercises/problem-03.md) | Medium | Insertion sort efficiency on inputs with bounded inversion distance | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Insertion Sort on Linked List](exercises/problem-04.md) | Medium/Hard | Insertion sort adaptation on linked data structures and pointer manipulation | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Stable Multi-Key Record Sorter](exercises/problem-05.md) | Hard | Sorting stability, composite keys, and in-place stability preservation | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-031
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: bubble sort, selection sort, insertion sort, stability, in-place sorting, nearly-sorted input, loop invariants*
