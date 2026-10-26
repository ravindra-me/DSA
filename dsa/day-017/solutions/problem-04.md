# Solution 4: Find K-th Symbol in Grammar

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Divide-and-conquer on virtual binary trees with logarithmic recursion

## Approach

Each row `n` has length $2^{n-1}$. The first half of row `n` is identical to row `n-1`, while the second half is the bitwise complement (inverted) of row `n-1`. Using recursion, we check if $k$ falls in the first half or second half. If $k$ is in the first half, the answer is the same as $k$ in row $n-1$. If $k$ is in the second half, the answer is the complement of symbol at $k - 2^{n-2}$ in row $n-1$.

## Thought Process

Generating the table row by row takes $O(2^n)$ time and memory, which exceeds time and memory limits for $n = 30$ ($2^{29} \approx 5.36 \times 10^8$ elements). Instead, observe the self-similar tree structure: element $k$ in row $n$ comes from element $\lceil k / 2 \rceil$ in row $n-1$. Specifically, the mid-point of row $n$ is $mid = 2^{n-2}$. If $k \le mid$, symbol $(n, k) = \text{symbol}(n-1, k)$. If $k > mid$, symbol $(n, k) = 1 - \text{symbol}(n-1, k - mid)$. This reduces the problem to $O(n)$ recursive calls.

## Algorithm

1. Base case: If n == 1, return 0.
2. Calculate the length of the previous row (or half of current row): mid = 2^(n-2).
3. If k <= mid, recursively call kth_grammar(n - 1, k).
4. If k > mid, recursively call kth_grammar(n - 1, k - mid) and return 1 - result (flip the bit).

## Complexity Analysis

- **Time:** $O(n)$ because the recursion depth is at most $n$, doing $O(1)$ arithmetic operations per step.
- **Space:** $O(n)$ auxiliary stack space due to the call stack of depth $n$.

## Edge Cases

- n = 1, k = 1: Base case, returns 0 directly.
- k at boundary (k = 1 or k = 2^(n-1)): Correctly handled by half-size checks.
- n = 30 (maximum constraint): Handled efficiently in 30 recursive calls without integer overflow.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def kth_grammar(n: int, k: int) -> int:
    """Return the k-th symbol in the n-th row of the grammar table."""
    if n == 1:
        return 0
    mid = 1 << (n - 2)
    if k <= mid:
        return kth_grammar(n - 1, k)
    else:
        return 1 - kth_grammar(n - 1, k - mid)
```
