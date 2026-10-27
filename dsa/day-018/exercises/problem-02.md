# Problem 2: Intersection of Two Arrays

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Set deduplication and set intersection | [Day 18: HashSet](../README.md) |

## Problem Statement

Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be **unique**, and you may return the result in **sorted ascending order**.

## Input

`nums1: list[int]`, `nums2: list[int]` - two integer arrays.

## Output

`list[int]` - unique common elements sorted in ascending order.

## Constraints

- 1 <= len(nums1), len(nums2) <= 10^4
- 0 <= nums1[i], nums2[i] <= 1000

## Examples

**Example 1**

```text
Input:  nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2]
```

2 is the only number present in both arrays.

**Example 2**

```text
Input:  nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [4, 9]
```

4 and 9 are present in both arrays.

**Example 3**

```text
Input:  nums1 = [1, 3, 5], nums2 = [2, 4, 6]
Output: []
```

No common elements.

## Function Signature

```python
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """Return sorted list of unique common elements between nums1 and nums2."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Convert arrays to sets to remove duplicates, compute their set intersection, and sort the result.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
