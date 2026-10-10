# Day 1: Big O Notation & Complexity Analysis

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 1 | 2026-10-10 | Fundamentals | New topic | progressive | Python 3.12 |

Big O notation is the universal language software engineers use to describe how an algorithm behaves as its input grows. Instead of measuring runtime in seconds, Big O characterizes growth rates in time and memory, allowing us to evaluate whether a solution will scale from ten items to ten billion. Mastering this foundation is the prerequisite for designing efficient algorithms and passing technical interviews.

## Topic

**Big O Notation & Complexity Analysis**: time complexity, space complexity, best/average/worst case, amortized analysis, growth rates

## Learning Objectives

By the end of this lesson you should be able to:

- Analyze an algorithm line by line to determine its time and auxiliary space complexity in Big O notation.
- Distinguish between best-case, average-case, and worst-case complexities, and explain when each is relevant.
- Understand the principle of amortized analysis and why certain expensive operations average out over long sequences.
- Order common complexity classes (O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n), O(n!)) by their asymptotic growth rates.
- Select appropriate algorithmic strategies based on input constraints (e.g., n <= 10^5 vs. n <= 20).

## Concept Explanation

### What it is

Big O notation describes the upper bound of an algorithm's growth rate as the input size $n$ approaches infinity. Rather than timing code with a stopwatch—which depends on CPU speed, background processes, and programming language—Big O counts fundamental operations (such as additions, assignments, or array reads). By focusing solely on how operational counts grow relative to $n$, Big O lets us compare algorithms in an abstract, hardware-independent way.

### Why it exists

Without Big O, performance debates devolve into machine-dependent measurements. An inefficient $O(n^2)$ algorithm might run faster than an $O(n)$ algorithm on a supercomputer for $n = 5$, but fail completely on a server when $n = 1,000,000$. Big O provides a rigorous mathematical guarantee about scalability: it tells you if your code will survive real-world scale before you ever write it.

### When to use it

Use complexity analysis at every stage of problem-solving: before writing code to verify if an idea will pass within time limits (typically $10^7$ to $10^8$ operations per second in Python), while choosing between alternative data structures, and during code reviews to spot scalability bottlenecks.

### When NOT to use it

Do not rely exclusively on Big O when constant factors or tiny input bounds dominate. For tiny inputs ($n \le 16$), an $O(n^2)$ insertion sort or linear search often beats an $O(n \log n)$ quicksort or $O(\log n)$ binary search due to CPU cache locality and low overhead. Big O governs asymptotic behavior ($n \to \infty$), not micro-optimizations.

### How it works internally

Complexity analysis works by identifying the dominant terms and dropping constants:
1. **Identify the input variables**: Is runtime driven by array length $n$, string length $m$, or both?
2. **Count elementary operations**: Determine how many loop iterations or recursive calls execute in terms of those variables.
3. **Drop constant coefficients**: $3n^2 + 5n \to n^2$ because as $n \to \infty$, the factor of 3 does not change the quadratic nature of the curve.
4. **Drop non-dominant terms**: $n^2 + 100n \to O(n^2)$ because $n^2$ dwarfs $100n$ for large $n$.
5. **Evaluate Cases**: Identify best case (minimum work), worst case (maximum work), and average case (expected work over uniform inputs).
6. **Amortized Analysis**: When an expensive $O(n)$ operation happens rarely (like dynamic array resizing) while $n-1$ operations take $O(1)$, the total cost across $n$ operations is $O(n)$, giving an amortized cost of $O(1)$ per operation.

### Common mistakes

- Confusing time complexity with space complexity, or failing to distinguish between auxiliary space (extra memory allocated) and input/output space.
- Assuming all nested loops are O(n^2); nested loops where the inner counter is halved or multiplied each step often result in O(n log n) or O(n).
- Treating built-in language operations (such as Python's `list.insert(0, x)`, `x in list`, or string slicing `s[a:b]`) as O(1) when they are actually O(n).
- Confusing worst-case runtime with Big O: Big O is an upper bound on a function, not automatically the worst case. You can have a Big O for the best case, average case, or worst case.
- Overlooking the recursion call stack when calculating space complexity: each active frame on the call stack consumes memory.

### Real-world applications

- Database Query Planners: Using complexity analysis to decide between Index Scans (O(log n)), Hash Joins (O(n + m)), or Nested Loop Joins (O(n * m)).
- Search Engines and High-Frequency Trading: Choosing lock-free ring buffers and O(1) data structures to eliminate latency spikes under heavy traffic.
- Standard Library Collections: Python's `list.append` uses amortized O(1) geometric over-allocation to balance memory efficiency and insertion speed.

## Example

Let us trace the complexity of finding if an array contains any duplicates.

Approach 1: Brute Force (Nested Loops)
```python
def has_duplicate_brute(nums: list[int]) -> bool:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False
```
- Outer loop runs $n$ times.
- Inner loop runs $(n - 1) + (n - 2) + \dots + 1 = \frac{n(n - 1)}{2}$ times in the worst case (no duplicates).
- Expansion: $\frac{1}{2}n^2 - \frac{1}{2}n$.
- Dropping constants and non-dominant terms yields **$O(n^2)$ time**.
- Auxiliary space is **$O(1)$** as we only use index variables.

Approach 2: Hash Set (Linear Pass)
```python
def has_duplicate_set(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```
- Loop runs at most $n$ times.
- Set membership check and insertion run in $O(1)$ average time.
- Total runtime: **$O(n)$ average time**.
- Trade-off: In the worst case, `seen` stores up to $n$ integers, requiring **$O(n)$ auxiliary space**.

This highlights the classic time-space trade-off: spending $O(n)$ space cuts runtime from quadratic to linear.

## Visual Explanation

```text
Growth Rates Comparison (Operations vs Input Size n)

Operations
    ^
    |                                                 . O(2^n)
    |                                             .   .
    |                                          .      . O(n^2)
    |                                      .          .
    |                                  .              . O(n log n)
    |                             .                   .
    |                        .                        . O(n)
    |                   .                             .
    |  .............................................. . O(log n)
    |  ---------------------------------------------- - O(1)
    +----------------------------------------------------> n

Scale of Growth:
  n = 1,000:
  - O(1):       1 op
  - O(log n):   ~10 ops
  - O(n):       1,000 ops
  - O(n log n): ~10,000 ops
  - O(n^2):     1,000,000 ops (10^6)
  - O(2^n):     1.07 x 10^301 ops (exceeds atoms in universe)
```

## Complexity

- **Time Complexity:** O(1): Constant operations; O(log n): Halving problem size each step; O(n): Single pass through input; O(n log n): Efficient divide-and-conquer sorts; O(n^2): Nested iterations over input.
- **Space Complexity:** O(1): Reusing fixed primitive variables; O(n): Hash sets, dynamically allocated copies, or recursion stacks of depth n.

Always verify whether the problem bounds allow an algorithm to run within the ~1-second interview threshold (roughly 50 million basic operations in Python). For example, n = 10^5 immediately disqualifies O(n^2) solutions (10^10 operations) and demands O(n) or O(n log n).

## Interview Perspective

1. **What is the difference between Big O, Big Omega (Ω), and Big Theta (Θ)?**
   <details><summary>What a strong answer covers</summary>

   Big O describes an asymptotic upper bound (f(n) <= c*g(n)), Big Omega describes an asymptotic lower bound (f(n) >= c*g(n)), and Big Theta describes an asymptotically tight bound where both upper and lower bounds match within constant factors (c1*g(n) <= f(n) <= c2*g(n)). In interviews, people often colloquially say 'Big O' when they actually mean 'Big Theta'.

   </details>
2. **What is amortized time complexity, and how does it differ from average-case complexity?**
   <details><summary>What a strong answer covers</summary>

   Average-case complexity averages runtime over all possible random inputs under a probability distribution. Amortized complexity evaluates a sequence of operations on a single data structure, guaranteeing that the average cost per operation across a worst-case sequence is small, even if individual operations are periodically expensive (e.g., dynamic array geometric resizing).

   </details>
3. **Can recursive algorithms have O(1) auxiliary space complexity?**
   <details><summary>What a strong answer covers</summary>

   Generally no, because every active stack frame requires memory proportional to the maximum recursion depth, leading to at least O(depth) auxiliary space. The exception is when a language and compiler support tail-call optimization (TCO), converting tail recursion to an iterative loop in O(1) space. Note that standard Python (CPython) does NOT optimize tail calls.

   </details>
4. **Given an input size of n = 10^5, what time complexities are acceptable in an interview?**
   <details><summary>What a strong answer covers</summary>

   A typical platform allows ~1-2 seconds of CPU time, corresponding to 10^7 - 10^8 operations. For n = 10^5, an O(n) algorithm takes 10^5 operations and O(n log n) takes ~1.7 * 10^6 operations, both easily passing. However, O(n^2) requires 10^10 operations, which will definitely time out (TLE).

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Single Missing Number](exercises/problem-01.md) | Easy | Linear time vs constant space trade-offs | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Sorted Pair Target Sum](exercises/problem-02.md) | Easy/Medium | Two-pointer linear scan vs quadratic brute force | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Amortized Queue via Stacks](exercises/problem-03.md) | Medium | Amortized time complexity analysis | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Logarithmic Peak Finder](exercises/problem-04.md) | Medium/Hard | Logarithmic time complexity O(log n) vs linear scan O(n) | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [First Missing Positive](exercises/problem-05.md) | Hard | In-place cyclic indexing to achieve O(n) time and O(1) auxiliary space | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-001
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: time complexity, space complexity, growth rates, best average worst case, amortized analysis*
