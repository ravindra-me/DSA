# Problem 4: Uniform Bucket Sort

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Bucket Sort with uniform distribution normalization | [Day 37: Counting, Bucket & Radix Sort](../README.md) |

## Problem Statement

Given a list of floating-point numbers `nums` that are known to be uniformly distributed in the semi-open range $[0.0, 1.0)$, sort the numbers in ascending order.

You should use Bucket Sort: distribute elements into $n$ buckets, sort each individual bucket using insertion sort (or another simple sort), and concatenate the buckets into a single sorted list. If `nums` is empty, return an empty list.

## Input

A list of floats `nums` where $0.0 \le \text{nums}[i] < 1.0$.

## Output

A list of floats sorted in ascending order.

## Constraints

- 0 <= len(nums) <= 10^5
- 0.0 <= nums[i] < 1.0

## Examples

**Example 1**

```text
Input:  nums = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
Output: [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]
```

Floats are placed in buckets according to floor(n * x) and sorted.

**Example 2**

```text
Input:  nums = [0.42]
Output: [0.42]
```

A single element is returned as is.

## Function Signature

```python
def bucket_sort(nums: list[float]) -> list[float]:
    """Sorts floats in [0, 1) in average O(n) time using Bucket Sort."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Create n buckets, hash float x to index int(n * x), sort each bucket, and concatenate.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
