# Problem 4: K Closest Points to Origin

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Quickselect with Custom Distance Function | [Day 34: Quick Sort & Quickselect](../README.md) |

## Problem Statement

Given an array of points where `points[i] = [x, y]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`. The distance between two points is Euclidean distance ($\\sqrt{x^2 + y^2}$). You may return the answer in any order. Optimize your algorithm to run in $O(N)$ average time complexity.

## Input

`points`: list[list[int]], `k`: int

## Output

`list[list[int]]`: k closest points

## Constraints

- 1 <= k <= len(points) <= 10^5
- -10^4 <= x_i, y_i <= 10^4

## Examples

**Example 1**

```text
Input:  points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]
```

Distance of (1, 3) is sqrt(10), distance of (-2, 2) is sqrt(8). Since sqrt(8) < sqrt(10), [-2, 2] is closer.

**Example 2**

```text
Input:  points = [[3, 3], [5, -1], [-2, 4]], k = 2
Output: [[3, 3], [-2, 4]]
```

Distances squared are 18, 26, 20. The 2 closest points are [[3, 3], [-2, 4]] (in any order).

## Function Signature

```python
def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use Quickselect based on squared distance $x^2 + y^2$. Partition the array of points around a pivot until the pivot rests at index `k - 1` or `k`. Return the subarray `points[:k]`.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
