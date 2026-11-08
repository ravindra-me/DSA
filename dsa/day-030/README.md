# Day 30: Binary Search on the Answer

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 30 | 2026-11-08 | Searching | New topic | progressive | Python 3.12 |

Binary search is not just for locating elements in a sorted array; it is a universal optimization technique. Whenever the feasibility of an answer behaves monotonically—if a solution works, every larger (or smaller) value also works—we can binary search over the answer space itself. This unlocks efficient $O(T \log(\text{range}))$ solutions for optimization problems that would otherwise require intractable brute force.

## Topic

**Binary Search on the Answer**: monotonic predicate, minimize maximum, capacity/speed problems, real-valued search

## Learning Objectives

By the end of this lesson you should be able to:

- Identify optimization problems where checking feasibility is monotonic (the monotonic predicate principle).
- Define precise search boundaries `[low, high]` for the answer space rather than array indices.
- Implement the 'minimize the maximum' and 'maximize the minimum' patterns correctly without off-by-one errors.
- Formulate greedy feasibility checks (`can_achieve(x)`) in $O(N)$ time.
- Apply binary search to continuous/floating-point domains using fixed iterations or epsilon bounds.

## Concept Explanation

### What it is

Binary Search on the Answer transforms an optimization problem ('Find the minimum $X$ such that condition $C(X)$ holds') into a decision problem ('Given a fixed $X$, can condition $C(X)$ be satisfied?'). If the boolean decision function $P(X)$ is monotonic—for example, evaluating to `[False, False, False, True, True, True]` across the sorted values of $X$—we can binary search for the first value of $X$ that yields `True`.

### Why it exists

Directly finding the optimal value mathematically or by constructive construction is often impossible or exponentially hard (e.g., trying all possible partitionings of an array). However, checking whether a *given* candidate value $X$ is valid is often straightforward and fast (typically $O(N)$ with a greedy pass). By converting 'find the best' into 'test candidate $X$', we reduce exponential search spaces to logarithmic evaluations.

### When to use it

Look for keywords like 'minimize the maximum', 'maximize the minimum', 'minimum speed/capacity needed to finish within time $T$', or 'maximum items that can fit'. If you notice that 'if $X$ is feasible, then any $X' > X$ is trivially feasible' (or vice versa), binary search on the answer is almost certainly the intended approach.

### When NOT to use it

Do not use this if the feasibility function is non-monotonic (e.g., $X=4$ is valid, $X=5$ is invalid, but $X=6$ is valid again). Also avoid it if finding the optimal answer directly is $O(1)$ or $O(N)$ via a closed-form formula, prefix sums, or two pointers without needing logarithmic search rounds.

### How it works internally

1. **Determine the Search Range**: Identify the absolute minimum possible answer (`low`) and the absolute maximum possible answer (`high`).
2. **Define the Predicate**: Write a helper function `is_feasible(candidate) -> bool`. Ensure it runs efficiently (usually $O(N)$ or $O(N \log N)$).
3. **Verify Monotonicity**: Confirm that as `candidate` increases, the predicate output transitions at most once (e.g., `00001111` or `11110000`).
4. **Run Binary Search**: Compute `mid = low + (high - low) // 2`. Call `is_feasible(mid)`.
   - If looking for the *minimum* valid value and `mid` is valid, record `mid` as a candidate (or set `high = mid`) and search left (`high = mid - 1`).
   - If `mid` is invalid, search right (`low = mid + 1`).
5. **Terminate**: The loop converges on the optimal boundary value.

### Common mistakes

- Setting search bounds `low` and `high` too narrow, excluding the optimal answer (e.g., setting `low = 0` when the minimum capacity cannot be less than `max(weights)`).
- Off-by-one errors in integer division, causing infinite loops when `low + 1 == high` (always use standard templates: either `low <= high` with an explicit `ans` variable, or careful boundary adjustments).
- Using `float` comparison with strict equality `low < high` instead of a fixed number of iterations (e.g., 60-100 iterations) or an epsilon tolerance (`high - low > 1e-7`), causing floating-point precision hangs.
- Assuming the predicate is monotonic when edge cases violate monotonicity.

### Real-world applications

- Autoscaling and Capacity Planning: Determining the minimum server throughput capacity required to handle peak simulated traffic without exceeding latency SLA.
- Network Packet Pacing: Finding the maximum transmission rate (bandwidth) that keeps packet drop rates below a specific threshold.
- Video Game Camera Zoom / Graphics: Finding the minimum bounding box radius or LOD (level of detail) distance that encompasses visible geometry.
- Financial Portfolio Risk: Calculating the internal rate of return (IRR) or implied volatility via numerical root finding.

## Example

### Problem: Shipping Packages within $D$ Days
Weights: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, Days: `D = 5`.
We want to find the **minimum conveyor capacity**.

#### Step 1: Establish Bounds
- `low = max(weights) = 10` (a boat cannot carry less than the heaviest package).
- `high = sum(weights) = 55` (if capacity is 55, all items ship in 1 day).

#### Step 2: Feasibility Function
`can_ship(cap)`: Greedily load packages into the current day's shipment until adding the next package exceeds `cap`. Count total days needed. Return `days_needed <= 5`.

#### Step 3: Binary Search Execution
1. `low = 10, high = 55, mid = 32` -> `days_needed = 2 <= 5` (True). Answer can be $\le 32$. `high = 31`.
2. `low = 10, high = 31, mid = 20` -> `days_needed = 4 <= 5` (True). Answer can be $\le 20$. `high = 19`.
3. `low = 10, high = 19, mid = 14` -> `days_needed = 5 <= 5` (True). Answer can be $\le 14$. `high = 13`.
4. `low = 10, high = 13, mid = 11` -> `days_needed = 8 > 5` (False). Capacity 11 too small! `low = 12`.
5. `low = 12, high = 13, mid = 12` -> `days_needed = 7 > 5` (False). Capacity 12 too small! `low = 13`.
6. `low = 13, high = 13, mid = 13` -> `days_needed = 6 > 5` (False). Capacity 13 too small! `low = 14`.
7. `low = 14, high = 13` -> Loop ends. Minimum capacity is `15`? Wait, let's trace 15: `[1..5]=15, [6,7]=13, [8]=8, [9]=9, [10]=10` -> exactly 5 days. For 14: `[1..4]=10, [5,6]=11, [7]=7, [8]=8, [9]=9, [10]=10` -> 6 days! The loop terminates with `low = 15`. Result is 15.

## Visual Explanation

```text
Monotonic Feasibility Spectrum (Minimize Goal):

Capacity:   10   11   12   13   14   15   16   17 ... 55
Feasible?:   F    F    F    F    F    T    T    T ...  T
                                      ^
                                 Target Answer

Search Iteration Trace:
Range: [10 ........................................ 55]
1. Test 32: Feasible (T) -> Search Left  [10 .... 31]
2. Test 20: Feasible (T) -> Search Left  [10 . 19]
3. Test 14: Infeasible (F) -> Search Right [15 . 19]
4. Test 17: Feasible (T) -> Search Left  [15 . 16]
5. Test 15: Feasible (T) -> Search Left  [15 . 14] -> Terminated! Result = 15
```

## Complexity

- **Time Complexity:** O(T * log(R)), where R is the size of the answer search space (e.g. high - low) and T is the time complexity of the feasibility check.
- **Space Complexity:** O(1) auxiliary space typically, as the search state requires only scalar pointers and greedy checking.

Because log2(10^9) is only ~30 and log2(10^18) is only ~60, binary search over huge answer spaces runs in virtually negligible iterations. The performance bottleneck is almost exclusively the feasibility check function.

## Interview Perspective

1. **How do you distinguish between problems that need binary search on array indices vs. binary search on the answer?**
   <details><summary>What a strong answer covers</summary>

   Standard binary search looks for a target value or boundary inside an explicitly provided sorted collection by index. Binary search on the answer applies when the input is not necessarily sorted, but the candidate solutions form a continuous virtual range [low, high] where a decision predicate f(x) is monotonic.

   </details>
2. **How do you choose `low` and `high` safely to prevent edge-case failures?**
   <details><summary>What a strong answer covers</summary>

   Derive bounds from theoretical extremes. For example, in shipping packages, `low` is max(weights) (since no package can be split) and `high` is sum(weights) (shipping everything in 1 day). If answers can be 0 or negative, ensure `low` accommodates that. Always verify if the extreme bounds themselves could be the answer.

   </details>
3. **What is the difference between integer binary search and real-valued (floating point) binary search?**
   <details><summary>What a strong answer covers</summary>

   Integer binary search divides with `// 2`, updates bounds with `mid +/- 1` (or `high = mid`), and terminates when `low > high`. Floating-point binary search divides with `/ 2.0`, updates with `low = mid` or `high = mid` (no +/- 1), and terminates after a fixed number of iterations (e.g., 60-100) or when `high - low < epsilon`.

   </details>
4. **Can you binary search on the answer if the condition is not monotonic?**
   <details><summary>What a strong answer covers</summary>

   No. Binary search relies strictly on the property that testing mid eliminates half of the remaining search space. If the truth values alternate or fluctuate, binary search can easily eliminate the region containing the global optimum. Monotonicity is the prerequisite.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Koko Eating Bananas](exercises/problem-01.md) | Easy | Basic capacity/rate search on integers | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Magnetic Force Between Balls](exercises/problem-02.md) | Easy/Medium | Maximize the minimum distance pattern | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Split Array Largest Sum](exercises/problem-03.md) | Medium | Minimize the maximum subarray sum (partitioning) | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Square Root and Optimal Fuel Blend](exercises/problem-04.md) | Medium/Hard | Real-valued / continuous binary search with precision threshold | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [K-th Smallest Pair Distance](exercises/problem-05.md) | Hard | Two-pointer feasibility check inside binary search on answer | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-030
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: Monotonic Predicate, Minimize Maximum Pattern, Maximize Minimum Pattern, Capacity and Rate Search, Continuous/Real-valued Binary Search*
