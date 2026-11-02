# Solution 1: Maximum Average Subarray I

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** fixed-size window

## Approach

Track the sum of a sliding window of fixed length $k$. Slide the window from left to right across the array by adding the incoming element and subtracting the outgoing element, updating the maximum sum observed, and finally dividing that maximum sum by $k$.

## Thought Process

A brute-force solution would compute the sum of every contiguous subarray of size $k$ independently. There are $n - k + 1$ such windows, and each sum takes $O(k)$ time, yielding an $O(n \cdot k)$ time complexity. For $n, k \le 10^5$, $n \cdot k$ can reach $10^{10}$ operations, which exceeds standard time limits.

Notice that two adjacent windows of size $k$ share $k - 1$ elements. Instead of recomputing the entire sum from scratch, we can compute the sum of the first $k$ elements once. When shifting the window one position to the right, the new sum equals the previous sum minus the element leaving the window (`nums[i - k]`) plus the element entering the window (`nums[i]`).

Since dividing by $k$ is monotonic, maximizing the average is equivalent to maximizing the window sum. We compute the maximum sum using integer addition/subtraction and perform a single floating-point division at the end.

## Algorithm

1. Compute the sum of the first $k$ elements (`nums[0]` through `nums[k - 1]`) and initialize `curr_sum` and `max_sum` to this value.
2. Iterate an index $i$ from $k$ to $n - 1$.
3. In each step, update `curr_sum += nums[i] - nums[i - k]`.
4. Update `max_sum = max(max_sum, curr_sum)`.
5. Return `max_sum / k` as a floating-point number.

## Complexity Analysis

- **Time:** $O(n)$ where $n$ is the length of `nums`. We traverse the array once, performing constant $O(1)$ work at each step.
- **Space:** $O(1)$ auxiliary space. Only a few numeric variables are maintained for the window sum and maximum.

## Edge Cases

- $k = 1$: Each element is its own window; the maximum average is simply the maximum single element.
- $k = n$: The entire array is the only window; the result is the average of all elements.
- All negative numbers: `max_sum` must be initialized to the first window sum (not 0) so that negative sums are correctly compared.
- Negative and positive values mixed: Window sums can increase or decrease freely; standard sliding logic handles all signs correctly without special-casing.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def find_max_average(nums: list[int], k: int) -> float:
    """Finds the maximum average of any contiguous subarray of length k."""
    curr_sum = sum(nums[:k])
    max_sum = curr_sum

    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum / k
```
