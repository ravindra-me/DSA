# Problem 3: Longest Consecutive Sequence

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | O(1) set/map lookup for connected component discovery | [Day 16: HashMap](../README.md) |

## Problem Statement

Given an unsorted array of integers `nums`, find the length of the longest consecutive elements sequence (e.g., `[1, 2, 3, 4]`). You must write an algorithm that runs in $O(n)$ time.

## Input

`nums: list[int]` - unsorted integers.

## Output

`int` - the maximum length of a consecutive elements sequence.

## Constraints

- 0 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [100, 4, 200, 1, 3, 2]
Output: 4
```

The longest consecutive sequence is [1, 2, 3, 4], length is 4.

**Example 2**

```text
Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
```

Sequence 0 to 8 has length 9.

**Example 3**

```text
Input:  nums = []
Output: 0
```

Empty list has sequence length 0.

## Function Signature

```python
def longest_consecutive_sequence(nums: list[int]) -> int:
    """Return the length of the longest consecutive sequence in O(n) time."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Convert the list into a hash set for O(1) membership testing. Identify streak starters (numbers where `x - 1` is not in the set) and count forward, ensuring each number is visited at most twice.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
