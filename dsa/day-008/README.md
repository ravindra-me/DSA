# Day 8: Big O Notation & Complexity Analysis: Deep Dive & Amortization

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 8 | 2026-10-17 | Fundamentals | Revision (stage 1) | progressive | Python 3.12 |

> **Revision day.** You first studied this topic earlier; today recaps the essentials and gives you brand-new problems. (spaced revision due on day 8 of 'big-o' (learned on day 1))

Mastering complexity analysis means moving beyond counting simple loop iterations to evaluating multi-variable functions, recursive branching, and amortized aggregate bounds. In this revision lesson, we solidify your mental model of asymptotic growth rates and apply strict runtime and auxiliary memory constraints to complex interactions involving arrays, linked lists, and bit manipulation.

## Topic

**Big O Notation & Complexity Analysis**: time complexity, space complexity, best/average/worst case, amortized analysis, growth rates

## Learning Objectives

By the end of this lesson you should be able to:

- Differentiate strictly between worst-case, average-case, and amortized complexity bounds.
- Formulate multi-variable Big O bounds (e.g., O(N + M), O(N log K)) accurately.
- Apply the Aggregate and Potential methods to evaluate operations with non-uniform per-step costs.
- Analyze auxiliary memory usage precisely, taking call-stack frames and data duplication into account.

## Concept Explanation

### What it is

Big O notation describes the upper bound of an algorithm's resource consumption (runtime or memory) as the input size grows toward infinity, ignoring machine-dependent constant factors and lower-order terms. Rather than measuring wall-clock time in milliseconds, it characterizes the scaling curve of fundamental operations.

### Why it exists

Raw execution time varies wildly across CPU architectures, programming languages, and operating system schedulers. Asymptotic complexity provides an invariant mathematical framework to compare algorithms objectively, predicting whether an approach will scale to millions of elements or collapse.

### When to use it

Use complexity analysis during every phase of problem-solving: upfront when translating input constraints into feasible target complexities (e.g., $N \le 10^5 \implies O(N \log N)$ or better), during design to eliminate bottlenecks, and in retrospectives to verify space-time trade-offs.

### When NOT to use it

Do not rely solely on asymptotic analysis when $N$ is small and constant factors dominate (e.g., cache locality makes an $O(N)$ contiguous array scan significantly faster than an $O(1)$ pointer-chasing lookup for $N < 1000$). Big O also does not account for real-time latency deadlines where single worst-case pauses are unacceptable.

### How it works internally

1. **Drop Constants & Lower-Order Terms**: $3N^2 + 50N + 10000 \in O(N^2)$ because as $N \to \infty$, $N^2$ dominates.
2. **Identify Variables**: If an algorithm processes an array of size $N$ and strings of max length $L$, the bound is $O(N \cdot L)$, not simply $O(N)$.
3. **Amortization**: If an expensive operation occurs rarely enough that the cumulative cost over $K$ sequential operations is bounded by $O(K)$, the amortized cost per operation is $O(1)$.
4. **Auxiliary vs Total Space**: Total space includes the input; auxiliary space counts only the additional memory allocated by the algorithm (including recursive stack frames).

### Common mistakes

- Confusing average-case with amortized complexity (amortization guarantees an average over worst-case sequences; average-case assumes a probabilistic input distribution).
- Treating string slicing or concatenation inside loops as $O(1)$ instead of $O(K)$ where $K$ is the slice length.
- Ignoring the recursion stack when calculating space complexity (depth of recursion $D$ requires $O(D)$ stack space).
- Assuming operations on dynamic data structures (e.g., hash map insertion or list appending) are always worst-case $O(1)$.

### Real-world applications

- Database query optimizers estimating computational cost across indices before executing plans.
- Dynamic array implementations (`std::vector`, Python `list`) sizing strategies ensuring $O(1)$ amortized appends.
- Garbage collection engines balancing stop-the-world pauses against throughput over continuous execution cycles.

## Example

Consider dynamic array resizing. Inserting $N$ items into an initially empty array of capacity 1 with doubling:
- Inserts at non-powers-of-two take $1$ write.
- Inserts at $1, 2, 4, 8, \dots, 2^k$ trigger resizing, copying $1, 2, 4, 8, \dots, 2^k$ elements.
- Total copies: $\sum_{i=0}^{\lfloor \log_2 N \rfloor} 2^i = 2^{\lfloor \log_2 N \rfloor + 1} - 1 < 2N$.
- Total operations for $N$ inserts: $N$ writes + $< 2N$ copies $< 3N$ operations.
- Amortized cost per operation: $\frac{3N}{N} = O(1)$.

## Visual Explanation

```text
Dynamic Array Doubling (Aggregate Cost):
Index:   1   2   3   4   5   6   7   8   9
Size:    1   2   3   4   5   6   7   8   9
Cap:     1   2   4   4   8   8   8   8  16
Cost:   [1] [2] [3] [1] [5] [1] [1] [1] [9]   <- spikes at 1, 2, 3, 5, 9
        ------------------------------------
Sum of spikes over N elements <= 3N  ==> Amortized O(1) per append
```

## Complexity

- **Time Complexity:** O(1) amortized: dynamically resizing array append; O(log N): binary search; O(N): linear scan; O(N log N): optimal comparison sort; O(2^N): subset generation.
- **Space Complexity:** O(1) auxiliary: pointers, running accumulators; O(N): frequency maps, call-stack of linear recursion; O(N * M): auxiliary grid storage.

Always analyze constraints before coding. If $N \le 20$, an $O(2^N)$ backtracking search is viable. If $N \le 10^5$, aim for $O(N \log N)$ or $O(N)$. If $N \le 10^9$, expect $O(\log N)$ or $O(1)$ mathematical formulations.

## Interview Perspective

1. **What is the formal difference between Big O, Big Omega, and Big Theta?**
   <details><summary>What a strong answer covers</summary>

   Big O provides an asymptotic upper bound ($f(N) \le c \cdot g(N)$), Big Omega provides an asymptotic lower bound ($f(N) \ge c \cdot g(N)$), and Big Theta provides an asymptotically tight bound where both upper and lower bounds match up to constant factors.

   </details>
2. **Can an algorithm have an $O(1)$ amortized time complexity but an $O(N)$ worst-case time complexity? Provide an example.**
   <details><summary>What a strong answer covers</summary>

   Yes. A classic example is appending to a dynamic array (like Python's `list`). When capacity is reached, it reallocates and copies all $N$ elements ($O(N)$ worst-case), but across $N$ insertions the total copy work is bounded by $2N$, yielding $O(1)$ amortized.

   </details>
3. **Why does Python's `s = s + char` inside an $N$-step loop result in $O(N^2)$ time?**
   <details><summary>What a strong answer covers</summary>

   Strings in Python are immutable. Each concatenation copies the existing string of length $k$, leading to $\sum_{k=1}^N k = \frac{N(N+1)}{2} = O(N^2)$ operations. Using `''.join(list_of_chars)` allocates the needed memory once, operating in $O(N)$ time.

   </details>
4. **How does tail-call optimization affect space complexity, and does Python support it?**
   <details><summary>What a strong answer covers</summary>

   Tail-call optimization allows recursive functions whose recursive call is in tail position to reuse the current stack frame, reducing recursion space from $O(N)$ to $O(1)$. Python intentionally does not support tail-call optimization to preserve complete stack traces for debugging.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Subarray Product Less Than K](exercises/problem-01.md) | Easy/Medium | Two Pointers / Sliding Window amortized complexity analysis | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Continuous Resettable Counter](exercises/problem-02.md) | Medium | Amortized state updates with lazy propagation | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Longest Duplicate Substring Length](exercises/problem-03.md) | Medium/Hard | Multi-variable analysis and binary search with polynomial rolling hash | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Partition Linked List Around Pivot](exercises/problem-04.md) | Medium/Hard | O(N) time and O(1) auxiliary space pointer manipulation | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Minimum Window Subsequence](exercises/problem-05.md) | Hard | Multi-variable dynamic programming / two-pointer complexity analysis | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-008
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: asymptotic-notation, amortized-analysis, space-complexity, time-complexity, growth-rates*
