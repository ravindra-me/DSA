# Solution 1: Subarray Product Less Than K

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy/Medium | **Concept:** Two Pointers / Sliding Window amortized complexity analysis

## Approach

Use a sliding window with two pointers (`left` and `right`) maintaining the running product of elements in `nums[left..right]`. For each `right`, if the product is $\ge k$, advance `left` and divide out `nums[left]` until the product is strictly less than $k$ (or `left > right`). Every valid window `[left, right]` adds `right - left + 1` new subarrays ending at `right`.

## Thought Process

A naive approach checks all $O(N^2)$ contiguous subarrays and computes their products, requiring $O(N^2)$ or $O(N^3)$ time, which exceeds the limit for $N = 3 \times 10^4$.

Since all numbers in `nums` are strictly positive integers ($\ge 1$), multiplying by another element is monotonically non-decreasing. This monotonic property allows a two-pointer / sliding window technique.

As `right` advances from $0$ to $N - 1$, we maintain `product *= nums[right]`. If `product >= k`, we shrink the window from the left by doing `product //= nums[left]` and incrementing `left`. Once `product < k`, every contiguous subarray ending at `right` that starts at any index from `left` up to `right` is valid. The number of such subarrays is exactly `right - left + 1`.

Regarding amortized complexity: although there is a nested `while` loop, the `left` pointer only moves forward and advances at most $N$ times across the entire algorithm. Thus, the total pointer operations are bounded by $2N$, guaranteeing strictly $O(N)$ runtime.

## Algorithm

1. Check if k <= 1. Because all numbers in nums are >= 1, any product of one or more elements is at least 1, so no subarray product can be strictly less than 1. Return 0 immediately if k <= 1.
2. Initialize left = 0, product = 1, and count = 0.
3. Iterate right from 0 to len(nums) - 1: multiply product by nums[right].
4. While left <= right and product >= k: divide product by nums[left] and increment left by 1.
5. Add (right - left + 1) to count.
6. Return count after iterating through all elements.

## Complexity Analysis

- **Time:** O(N) where N is the length of nums. Both left and right pointers increment at most N times each, yielding an amortized O(1) operations per element.
- **Space:** O(1) auxiliary space as we only store a few integer scalar variables (left, right, product, count).

## Edge Cases

- k <= 1: Handled early by returning 0 since nums contains strictly positive integers (>= 1).
- k = 0: Correctly returns 0 due to early check.
- Single element array: If nums[0] < k, returns 1; otherwise returns 0.
- No valid subarrays: When all elements are >= k, left moves past right at each step, adding 0 subarrays.
- All elements valid: When product never exceeds k, computes the total number of subarrays N * (N + 1) // 2.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    """Return the number of contiguous subarrays with product strictly less than k."""
    if k <= 1:
        return 0

    left = 0
    product = 1
    count = 0

    for right, val in enumerate(nums):
        product *= val
        while product >= k and left <= right:
            product //= nums[left]
            left += 1
        count += right - left + 1

    return count
```
