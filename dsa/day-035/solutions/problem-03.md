# Solution 3: Maximum Subarray Min-Product

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium/Hard | **Concept:** Previous/Next Smaller Element with Prefix Sums

## Approach

To maximize `min(subarray) * sum(subarray)`, we treat each element `nums[i]` as the candidate minimum for a range `[L, R]`. Using a monotonic increasing stack, we find the largest range `[L, R]` where `nums[i]` remains the minimum element. We calculate the sum of this range efficiently in $O(1)$ time using a prefix sum array.

## Thought Process

A naive solution checks all $O(N^2)$ subarrays, taking $O(N)$ to find the minimum and sum for each, leading to $O(N^3)$ or $O(N^2)$ with prefix sums. To optimize, shift focus from 'evaluating each subarray' to 'evaluating each element as the minimum'. For a given `nums[i]`, the range where it acts as the minimum extends to the left until the previous smaller element and to the right until the next smaller element. Finding these boundaries for all elements takes $O(N)$ time using a monotonic increasing stack. The sum of any range `[L, R]` can then be calculated in $O(1)$ using prefix sums. Note: maximum min-product calculations must be performed before taking the modulo $10^9 + 7$, applying the modulo only at the final step.

## Algorithm

1. Compute a prefix sum array `prefix` of length `N + 1` where `prefix[k]` is the sum of the first `k` elements.
2. Initialize an empty monotonic increasing stack to store indices, and set `max_product = 0`.
3. Iterate through the array up to index `N` (treating an implicit boundary element of value 0 at index `N`).
4. While the stack is not empty and the current element `nums[i]` (or 0 at index `N`) is less than `nums[stack[-1]]`:
5. Pop the index `idx` from the stack. It represents the minimum element for a subarray.
6. The right bound `R` of this subarray is `i - 1`.
7. The left bound `L` is `stack[-1] + 1` if the stack is not empty, else `0`.
8. Calculate the subarray sum using `prefix[R + 1] - prefix[L]`.
9. Update `max_product = max(max_product, nums[idx] * total_sum)`.
10. Push the current index `i` onto the stack.
11. Return `max_product % (10^9 + 7)`.

## Complexity Analysis

- **Time:** $O(N)$ because each index is pushed to and popped from the monotonic stack at most once, and prefix sums take $O(N)$ to precompute.
- **Space:** $O(N)$ to store the prefix sum array of size $N+1$ and the monotonic stack of size up to $N$.

## Edge Cases

- Single element array: The stack handles this gracefully, evaluating the only element over the range [0, 0].
- Array with duplicate elements: The monotonic stack allows equal values to remain or be popped sequentially, correctly covering the maximal range for equal elements across iterations.
- Strictly increasing/decreasing arrays: Handled via the boundary clearing loop at index `N`.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
class Solution:
    pass

def max_min_product(nums: list[int]) -> int:
    """Calculates the maximum min-product among all non-empty subarrays modulo 10^9 + 7."""
    MOD = 10**9 + 7
    n = len(nums)
    
    # Precompute prefix sums
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
        
    max_product = 0
    stack: list[int] = []  # Monotonic increasing stack storing indices
    
    for i in range(n + 1):
        # Use 0 as a sentinel value at index n
        current_val = nums[i] if i < n else 0
        
        while stack and nums[stack[-1]] > current_val:
            idx = stack.pop()
            min_val = nums[idx]
            
            right_bound = i - 1
            left_bound = stack[-1] + 1 if stack else 0
            
            total_sum = prefix[right_bound + 1] - prefix[left_bound]
            max_product = max(max_product, min_val * total_sum)
            
        stack.append(i)
        
    return max_product % MOD
```
