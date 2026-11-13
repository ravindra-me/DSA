# Day 35: Day 35: Monotonic Stack Revision & Advanced Patterns

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 35 | 2026-11-13 | Linear Data Structures | Revision (stage 2) | progressive | Python 3.12 |

> **Revision day.** You first studied this topic earlier; today recaps the essentials and gives you brand-new problems. (spaced revision due on day 19 of 'monotonic-stack' (learned on day 12))

Welcome back to the Monotonic Stack pattern. Today we consolidate your understanding of maintaining ordered stacks to query nearest elements in $O(1)$ amortized time. You will move beyond standard next-greater-element problems into advanced applications involving lexicographical bounds, optimization over range constraints, and multi-pass rectangular geometry.

## Topic

**Monotonic Stack**: next greater element, previous smaller element, histogram area, stock span

## Learning Objectives

By the end of this lesson you should be able to:

- Identify when a linear scan requires maintaining nearest smaller/greater neighbors in $O(N)$ time.
- Formulate correct stack invariants for strictly vs. non-strictly monotonic stacks to prevent duplicate counting.
- Solve lexicographical optimization problems using monotonic stack techniques paired with frequency counting.
- Apply monotonic stack techniques to 2D grid matrix problems efficiently.

## Concept Explanation

### What it is

A Monotonic Stack is a standard stack data structure whose elements are strictly increasing or non-decreasing (or decreasing / non-increasing) from bottom to top. As you iterate through an array, elements that violate the monotonicity condition are popped before the current element is pushed.

### Why it exists

A naive approach to finding the next or previous greater/smaller element for every item in an array takes $O(N^2)$ time via nested loops. A monotonic stack resolves all such nearest-neighbor queries in $O(N)$ total time because every element is pushed onto the stack exactly once and popped at most once.

### When to use it

Use a monotonic stack when a problem asks for:
- The next/previous smaller or larger element for every index.
- The range $[L, R]$ where an element $A[i]$ acts as the minimum or maximum.
- Lexicographically smallest/largest sub-sequences under frequency constraints.
- Max rectangle area in a histogram or 2D binary matrix.

### When NOT to use it

Do not use a monotonic stack when you need queries over arbitrary range intervals (use Segment Trees or Fenwick Trees), when order does not matter (use standard Priority Queue / Hash Map), or when sliding window max/min with fixed window size $K$ is required (use a Monotonic Deque instead).

### How it works internally

1. Initialize an empty stack (often storing indices rather than values).
2. Iterate through the array from left to right (or right to left).
3. While the stack is not empty and the current element violates the stack's monotonicity invariant (e.g., current value < stack top value for an increasing stack):
   - Pop the top element from the stack.
   - Process the popped element (e.g., record the current element as its 'next smaller element').
4. Push the current element's index onto the stack.
5. Popping an element establishes its boundary, guaranteeing $O(1)$ amortized time per element.

### Common mistakes

- Storing raw values instead of indices when index distance is needed for width/distance calculations.
- Using strictly less `<` when non-strict `<=` is required to handle duplicate elements correctly without overcounting or undercounting.
- Forgetting to clear or flush remaining elements on the stack after the main loop finishes.
- Confusing monotonic increasing stack (used to find smaller elements) with monotonic decreasing stack (used to find greater elements).

### Real-world applications

- Stock market technical analysis (calculating stock span and local trend reversals).
- Parsing and optimizing terrain height maps or hydrology watershed simulations.
- Text processing engines (e.g., maintaining layout constraints during continuous document rendering).

## Example

Consider finding the Previous Smaller Element for `nums = [4, 2, 7, 3]`.
We maintain a Monotonic Increasing Stack of indices.

1. i=0, num=4: Stack empty. Previous smaller for index 0 is None. Push index 0 (val 4). Stack: `[0(4)]`.
2. i=1, num=2: Pop index 0 because 4 >= 2. Stack empty. Previous smaller for index 1 is None. Push index 1 (val 2). Stack: `[1(2)]`.
3. i=2, num=7: 7 > 2, no pop. Stack top is index 1 (val 2). Previous smaller for index 2 is index 1 (val 2). Push index 2 (val 7). Stack: `[1(2), 2(7)]`.
4. i=3, num=3: Pop index 2 (7 >= 3). Stack top is index 1 (val 2). Previous smaller for index 3 is index 1 (val 2). Push index 3 (val 3). Stack: `[1(2), 3(3)]`.

Result Previous Smaller Indices: `[None, None, 1, 1]`.

## Visual Explanation

```text
Array: [4, 2, 7, 3]

i=0 (4): Stack: [4]
i=1 (2): 4 >= 2 -> Pop 4. Stack: [2]
i=2 (7): 7 > 2  -> Push 7. Stack: [2, 7]  (Prev smaller of 7 is 2)
i=3 (3): 7 >= 3 -> Pop 7. Stack: [2, 3]  (Prev smaller of 3 is 2)
```

## Complexity

- **Time Complexity:** Push/Pop operations: O(1) amortized per element. Full array scan: O(N) total time.
- **Space Complexity:** O(N) aux space to store stack indices in the worst case (e.g., monotonic input).

Amortized $O(1)$ per element holds because every element index enters the stack once and leaves at most once across the entire algorithm execution.

## Interview Perspective

1. **How do you avoid double counting when calculating sum of subarray minimums when duplicate elements exist in the array?**
   <details><summary>What a strong answer covers</summary>

   Use a strict inequality `<` for the Previous Smaller Element boundary and a non-strict inequality `<=` for the Next Smaller Element boundary (or vice-versa). This breaks symmetry deterministically and assigns responsibility for identical elements to a unique canonical subarray.

   </details>
2. **What is the key difference between using a Monotonic Stack vs a Monotonic Deque?**
   <details><summary>What a strong answer covers</summary>

   A monotonic stack pushes/pops from one end (top) and is ideal for unbounded range queries like next greater element. A monotonic deque allows pops from both ends (front and back), making it suitable for sliding window maximum/minimum queries where old elements expire after a fixed window size $K$.

   </details>
3. **When would you iterate right-to-left instead of left-to-right with a Monotonic Stack?**
   <details><summary>What a strong answer covers</summary>

   Right-to-left iteration is often more intuitive when you need to populate the Next Greater/Smaller Element array directly during the pass, as the stack naturally represents the candidate answers strictly to the right of the current element.

   </details>
4. **How do you extend the 1D Largest Rectangle in Histogram to 2D Maximal Rectangle in a binary matrix?**
   <details><summary>What a strong answer covers</summary>

   Treat each row in the 2D grid as the base of a histogram. Update consecutive height counts row by row ($O(W)$ per row), then invoke the 1D monotonic stack histogram algorithm for each row, resulting in $O(R \times C)$ overall time.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Visible Mountains Count](exercises/problem-01.md) | Easy/Medium | Next Greater Element with distance thresholding | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Remove Duplicate Letters Lexicographically](exercises/problem-02.md) | Medium | Monotonic Stack with Hash Map / Frequency Count | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Maximum Subarray Min-Product](exercises/problem-03.md) | Medium/Hard | Previous/Next Smaller Element with Prefix Sums | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Maximal Rectangle of Ones in Binary Grid](exercises/problem-04.md) | Medium/Hard | 2D Grid reduction to Monotonic Stack Histogram | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Constrained Subsequence Sum with Width Limit](exercises/problem-05.md) | Hard | Monotonic Stack/Deque with Dynamic Programming | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-035
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: monotonic-stack, next-greater-element, previous-smaller-element, histogram-2d, lexicographical-stack*
