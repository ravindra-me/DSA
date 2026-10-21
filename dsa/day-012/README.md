# Day 12: Day 12: Monotonic Stack

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 12 | 2026-10-21 | Linear Data Structures | New topic | progressive | Python 3.12 |

Many interview problems ask you to find the 'next greater', 'previous smaller', or span of elements in an array. While nested loops take $O(n^2)$ time, a **monotonic stack** maintains elements in strict sorted order as you scan, resolving relationships in linear $O(n)$ time via amortized popping.

## Topic

**Monotonic Stack**: next greater element, previous smaller element, histogram area, stock span

## Learning Objectives

By the end of this lesson you should be able to:

- Identify problems that reduce to finding the nearest greater or smaller elements to the left or right.
- Maintain monotonic increasing and decreasing invariants across array traversals.
- Store indices rather than raw values to compute spans, widths, and distances easily.
- Analyze the amortized $O(n)$ time complexity using aggregate push/pop accounting.
- Formulate solutions for classic patterns: Stock Span, Next Greater Element, and Largest Rectangle in Histogram.

## Concept Explanation

### What it is

A **monotonic stack** is a standard stack (LIFO) data structure that enforces a monotonicity invariant: its elements are always strictly increasing or strictly decreasing from bottom to top.

Whenever a newly examined element would violate this invariant, elements are popped from the top of the stack until inserting the new element preserves the required order. Popped elements are processed at the exact moment their boundary or 'dominant' neighbor arrives.

### Why it exists

Consider finding the next element strictly greater than each item in an array of size $n$. The naive approach checks every subsequent element with a nested loop, taking $O(n^2)$ in the worst case (e.g., sorted descending inputs). A monotonic stack avoids redundant comparisons: each item is pushed once and popped at most once. This brings the time complexity down to $O(n)$, which is optimal.

### When to use it

Look for these key signals in a problem statement:
- Finding the **next greater / next smaller** element to the left or right.
- Finding the **previous greater / previous smaller** element.
- Calculating **spans, visible boundaries, or bounded areas** (such as bounding rectangles under histograms or trapping rainwater).
- When resolving an element's query depends strictly on the first element that exceeds or falls below its value.

### When NOT to use it

Do not use a monotonic stack when:
- You need the $k$-th largest element or global extrema across arbitrary windows without structural order (use heaps or quickselect).
- You need to query arbitrary ranges dynamically while items are modified (use Segment Trees or Fenwick Trees).
- The problem depends on elements non-monotonically, such as finding pairs with a specific sum (use hash maps or two pointers on sorted arrays).

### How it works internally

1. **Determine the invariant:**
   - To find the *next greater element*, maintain a **monotonic decreasing** stack (bottom to top). When a larger element arrives, it pops smaller elements; the arriving element is their 'next greater'.
   - To find the *next smaller element*, maintain a **monotonic increasing** stack.
2. **Store indices instead of values:** Storing indices allows you to calculate both distance (`current_index - stack[-1]`) and look up the value (`nums[stack[-1]]`).
3. **Traverse the array:** For each element:
   - While the stack is not empty and the current element violates the monotonicity condition relative to `stack[-1]`, pop the top element and record its answer.
   - Push the current index onto the stack.
4. **Handle remaining elements:** Elements still left in the stack after processing have no valid greater/smaller element in the scanned direction (assign a default like `-1` or sentinel bounds).

### Common mistakes

- Storing values instead of indices: storing only values makes it impossible to compute spans or distinguish between duplicate values.
- Confusing strict inequality (`<` vs `<=`) when popping, which causes bugs when duplicate values exist in the input.
- Misidentifying whether to use a monotonically increasing or decreasing stack for 'greater' vs 'smaller' targets.
- Forgetting to handle elements that remain on the stack after the loop terminates.
- Assuming the loop inside the scan makes the algorithm $O(n^2)$: each index is pushed once and popped at most once, guaranteeing amortized $O(n)$ time.

### Real-world applications

- Financial market microstructure: computing real-time price spans, resistance levels, and volume-weighted breakouts.
- Rendering engines and CAD software: computing silhouette contours, visible horizon horizons, and largest unblocked bounding boxes in raster grids.
- Compiler design: parsing expressions with operator precedence and syntax-directed AST construction.

## Example

### Tracing Next Greater Element

Given `nums = [2, 1, 2, 4, 3]`:
We want an array `res` where `res[i]` is the next element to the right strictly greater than `nums[i]`, or `-1` if none exists.
We maintain a **monotonic decreasing stack** of indices.

- `i = 0, val = 2`: Stack empty. Push index `0`. `stack = [0]` (values: `[2]`)
- `i = 1, val = 1`: `1 < 2`. Monotonicity holds. Push `1`. `stack = [0, 1]` (values: `[2, 1]`)
- `i = 2, val = 2`: `2 > nums[stack[-1]] (1)`.
  - Pop index `1`: `res[1] = 2`.
  - `2 <= nums[stack[-1]] (2)`: Stop popping.
  - Push `2`. `stack = [0, 2]` (values: `[2, 2]`)
- `i = 3, val = 4`: `4 > nums[stack[-1]] (2)`.
  - Pop index `2`: `res[2] = 4`.
  - `4 > nums[stack[-1]] (2)`.
  - Pop index `0`: `res[0] = 4`.
  - Stack empty. Push `3`. `stack = [3]` (values: `[4]`)
- `i = 4, val = 3`: `3 < 4`. Push `4`. `stack = [3, 4]` (values: `[4, 3]`)

End of array: remaining indices `3` and `4` have no next greater element (`res[3] = -1`, `res[4] = -1`).
Final Result: `[4, 2, 4, -1, -1]`.

## Visual Explanation

```text
Array: [2, 1, 2, 4, 3]

i=0 (2):  | 0 (val 2) |  <- pushed
          +----------+

i=1 (1):  | 1 (val 1) |
          | 0 (val 2) |  <- 1 < 2, push 1
          +----------+

i=2 (2):  2 > top (1) -> POP 1 -> res[1] = 2
          2 <= top (2) -> push 2
          | 2 (val 2) |
          | 0 (val 2) |
          +----------+

i=3 (4):  4 > top (2) -> POP 2 -> res[2] = 4
          4 > top (2) -> POP 0 -> res[0] = 4
          | 3 (val 4) |  <- stack was empty, push 3
          +----------+

i=4 (3):  | 4 (val 3) |
          | 3 (val 4) |  <- 3 < 4, push 4
          +----------+

Done! Stack elements left: res[3] = -1, res[4] = -1
```

## Complexity

- **Time Complexity:** O(n) total: each element is pushed onto the stack exactly once and popped at most once across the entire iteration.
- **Space Complexity:** O(n) auxiliary space: in the worst case (e.g. strictly decreasing array in a monotonic decreasing stack), all n indices reside in the stack.

Although there is a `while` loop nested inside the `for` loop, the inner loop's pops are bounded by the total number of pushes ($n$). Thus, the work amortizes to $O(1)$ per element.

## Interview Perspective

1. **Why do we almost always store indices instead of values in the stack?**
   <details><summary>What a strong answer covers</summary>

   Storing indices gives dual information: the value at `nums[i]` and the position `i`. The position is necessary to compute spans, distances, and widths, and uniquely distinguishes duplicate values.

   </details>
2. **How do you handle circular arrays when finding the next greater element?**
   <details><summary>What a strong answer covers</summary>

   Simulate looping through the array twice by iterating index `i` from `0` to `2 * n - 1` and accessing values via `nums[i % n]`. Do not push indices on the second pass if only resolving queries.

   </details>
3. **How do you decide between a monotonic increasing stack vs a monotonic decreasing stack?**
   <details><summary>What a strong answer covers</summary>

   If you are looking for the next/previous smaller element, you need smaller elements to trigger the pop, so maintain an increasing stack. If you are looking for the next/previous greater element, maintain a decreasing stack.

   </details>
4. **What is the amortized cost argument for the inner while loop?**
   <details><summary>What a strong answer covers</summary>

   Use aggregate analysis: each of the $n$ elements enters the stack at most once and leaves at most once. The total number of pop operations across the entire execution cannot exceed $n$, yielding an amortized $O(1)$ cost per step and $O(n)$ total.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Daily Temperatures](exercises/problem-01.md) | Easy | Next greater element distance using a monotonic decreasing stack | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Online Stock Span](exercises/problem-02.md) | Easy/Medium | Previous greater element tracking across a streaming sequence | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Next Greater Element II (Circular Array)](exercises/problem-03.md) | Medium | Monotonic stack on circular / wrapped arrays | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Largest Rectangle in Histogram](exercises/problem-04.md) | Medium/Hard | Finding left and right smaller boundaries to calculate maximal area | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Sum of Subarray Minimums](exercises/problem-05.md) | Hard | Counting subarrays where each element is the minimum using PSE and NSE | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-012
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: Monotonic Stack, Next Greater Element, Previous Smaller Element, Stock Span Problem, Amortized Complexity Analysis, Histogram Maximum Area*
