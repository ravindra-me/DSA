# Problem 3: Sliding Window Maximum

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Monotonic Decreasing Deque | [Day 15: Deque & Monotonic Queue](../README.md) |

## Problem Statement

You are given an array of integers `nums` and an integer `k`. There is a sliding window of size `k` moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window, which contains the maximum element for each window of size `k`.

## Input

`nums: list[int]` - input integers, `k: int` - window width.

## Output

`list[int]` - list of maximums for each window.

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length

## Examples

**Example 1**

```text
Input:  nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
```

Window [1, 3, -1] -> 3; [3, -1, -3] -> 3; [-1, -3, 5] -> 5; [-3, 5, 3] -> 5; [5, 3, 6] -> 6; [3, 6, 7] -> 7

**Example 2**

```text
Input:  nums = [1], k = 1
Output: [1]
```

Single element window yields the element itself.

**Example 3**

```text
Input:  nums = [9, 8, 7, 6], k = 2
Output: [9, 8, 7]
```

Strictly decreasing sequence: each window max is its first element.

## Function Signature

```python
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Return the maximum element in every contiguous window of size k."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain indices in a monotonic decreasing deque. Discard out-of-window elements from the left and smaller elements from the right before appending. Time complexity must be O(n).

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
