# Solution 1: Single Missing Number

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Linear time vs constant space trade-offs

## Approach

We can determine the missing number by utilizing the XOR bitwise operator (or Gauss's summation formula). By XORing all indices from $0$ to $n$ with all values present in `nums`, every number present in both sets cancels itself out ($x \oplus x = 0$), leaving only the single missing number. This requires a single linear scan and $O(1)$ auxiliary space without mutating the input list.

## Thought Process

A brute-force solution would search for each number in the range $[0, n]$ using linear search, taking $O(n^2)$ time and $O(1)$ space. Alternatively, sorting the array takes $O(n \log n)$ time, or storing elements in a hash set takes $O(n)$ time but $O(n)$ auxiliary space, which violates the $O(1)$ space constraint.

To achieve both $O(n)$ time and $O(1)$ space without mutating the input array, we look for aggregate invariants:
1. **Summation (Gauss's Formula)**: The expected sum of all numbers from $0$ to $n$ is $\frac{n(n+1)}{2}$. Subtracting the sum of all elements in `nums` directly yields the missing number.
2. **Bitwise XOR**: XOR is associative and commutative, with identities $x \oplus x = 0$ and $x \oplus 0 = x$. If we compute $(0 \oplus 1 \oplus \dots \oplus n) \oplus (nums[0] \oplus nums[1] \oplus \dots \oplus nums[n-1])$, every number present in `nums` appears twice and evaluates to zero, leaving strictly the missing number. XOR avoids potential integer overflow concerns in fixed-precision languages and operates in optimal linear time.

## Algorithm

1. Initialize an accumulator variable `missing` to $n$, since the loop over indices will run from $0$ to $n-1$.
2. Iterate through the array with both the index `i` and element `num`.
3. Update `missing ^= i ^ num` at each iteration.
4. Return `missing` after the loop completes.

## Complexity Analysis

- **Time:** $O(n)$ because we iterate over the $n$-element array exactly once, performing constant-time bitwise operations at each step.
- **Space:** $O(1)$ auxiliary space because we only allocate a single integer variable `missing` regardless of input size, and the input array is not modified.

## Edge Cases

- Smallest input ($n = 1$): Handled correctly. If `nums = [0]`, result is $1$. If `nums = [1]`, result is $0$.
- Missing number is $0$: When $0$ is missing, all numbers $1$ to $n$ are present; the XOR logic correctly yields $0$.
- Missing number is $n$: When $n$ is missing, all numbers $0$ to $n-1$ are present; the XOR logic correctly yields $n$.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def find_missing_number(nums: list[int]) -> int:
    """Return the single missing number from the range [0, len(nums)]."""
    missing = len(nums)
    for index, value in enumerate(nums):
        missing ^= index ^ value
    return missing
```
