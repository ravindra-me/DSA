# Solution 2: Product of Array Except Self

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Medium | **Concept:** prefix-suffix-products

## Approach

For each index `i`, the product of all elements except `nums[i]` equals the product of all elements to its left multiplied by the product of all elements to its right. We compute the prefix products directly into the result array in a forward pass, and then accumulate suffix products on-the-fly in a backward pass, combining them in $O(1)$ auxiliary space.

## Thought Process

A naive approach is to compute the product of all other elements for each index with nested loops, taking $O(N^2)$ time. A faster approach would be multiplying all elements and dividing by `nums[i]`, but the problem explicitly forbids division (which also fails cleanly handling zeros).

Notice that `answer[i] = (nums[0] * ... * nums[i-1]) * (nums[i+1] * ... * nums[n-1])`. If we precompute prefix products and suffix products into separate arrays, each `answer[i]` is just `prefix[i-1] * suffix[i+1]`, taking $O(N)$ time and $O(N)$ auxiliary space.

To optimize space to $O(1)$ extra space (excluding the output array), we first populate `answer[i]` with the running prefix product up to index `i - 1`. Then, we iterate backwards using a single scalar variable `suffix_prod` (initialized to 1) that accumulates the product of elements to the right of `i`, multiplying `answer[i]` by `suffix_prod` before updating `suffix_prod *= nums[i]`.

## Algorithm

1. Let `n = len(nums)`. Initialize an output array `answer` of length `n` with 1s.
2. Perform a forward pass: maintain a running product `prefix = 1`. For each index `i` from 0 to `n - 1`, set `answer[i] = prefix`, then update `prefix *= nums[i]`.
3. Perform a backward pass: maintain a running product `suffix = 1`. For each index `i` from `n - 1` down to 0, multiply `answer[i] *= suffix`, then update `suffix *= nums[i]`.
4. Return `answer`.

## Complexity Analysis

- **Time:** $O(N)$ because we make exactly two linear passes over the array of length $N$.
- **Space:** $O(1)$ auxiliary space beyond the returned `answer` array, using only two integer accumulator variables.

## Edge Cases

- Single zero: The index with 0 receives the product of all non-zero elements, while all other indices receive 0.
- Multiple zeros: Every index will have a zero in either its prefix or suffix, resulting in an array of all zeros.
- Minimum length array (n = 2): Successfully handles prefix and suffix boundaries using the identity 1.
- Negative numbers: Alternating or negative values correctly maintain their sign through standard integer multiplication.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def product_except_self(nums: list[int]) -> list[int]:
    """Computes product of all array elements except self in O(N) time without division."""
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
```
