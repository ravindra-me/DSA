# Solution 2: Product of Array Except Self

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Prefix-Suffix Accumulation

## Approach

For any index `i`, the product of all elements except `nums[i]` equals `(product of elements before i) * (product of elements after i)`. We compute the running prefix products in a first pass into the output array, and then multiply by running suffix products in a second, reverse pass using $O(1)$ auxiliary space.

## Thought Process

A naive approach calculates the product of all elements in the entire array, then divides by `nums[i]` for each index. However, division is explicitly forbidden, and division fails when `nums[i] == 0` without handling zero counts explicitly.

Another naive approach is to loop over all $j \ne i$ for each index $i$, leading to $O(N^2)$ time, which times out for $N = 10^5$.

To achieve $O(N)$ time without division, decompose the problem: for each index $i$, the result is $\prod_{j=0}^{i-1} nums[j] \times \prod_{j=i+1}^{N-1} nums[j]$.
By maintaining a prefix product array where `prefix[i]` stores the product of elements strictly to the left of $i$, and a suffix product array where `suffix[i]` stores the product of elements strictly to the right, we can answer each query in $O(1)$ time.

To optimize memory to $O(1)$ auxiliary space (ignoring the output list), we can populate the output array directly with prefix products, then sweep backward from right to left maintaining a single running suffix product accumulator and multiplying it into each output position.

## Algorithm

1. Initialize an array `result` of length $N$ where `result[0] = 1`.
2. Perform a forward pass from index 1 to $N - 1$: set `result[i] = result[i - 1] * nums[i - 1]`. At the end of this pass, `result[i]` contains the product of all elements strictly to the left of index $i$.
3. Initialize a scalar variable `suffix_prod = 1`.
4. Perform a backward pass from index $N - 1$ down to 0: multiply `result[i]` by `suffix_prod`, then update `suffix_prod = suffix_prod * nums[i]`.
5. Return `result`.

## Complexity Analysis

- **Time:** $O(N)$ because the algorithm consists of two sequential single passes over the array of size $N$.
- **Space:** $O(1)$ auxiliary space (excluding the returned output array) as only a single scalar `suffix_prod` is tracked.

## Edge Cases

- Minimum length array ($N = 2$): Prefix for index 1 is `nums[0]` and suffix for index 0 is `nums[1]`, correctly handled by base cases.
- Array with a single zero: Every position except the zero's position receives 0, while the zero's index receives the non-zero product of the rest.
- Array with multiple zeros: All outputs evaluate to 0 because every index excludes at most one zero.
- Negative numbers: Signs naturally balance out across prefix and suffix multiplications without needing special branch logic.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def product_except_self(nums: list[int]) -> list[int]:
    """Compute product of all elements except nums[i] without division."""
    n = len(nums)
    result = [1] * n

    # Prefix products: result[i] contains product of elements to the left of i
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    # Suffix products: multiply with running product of elements to the right
    suffix_prod = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix_prod
        suffix_prod *= nums[i]

    return result
```
