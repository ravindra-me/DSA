# Problem 5: Minimum Window Subsequence

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Multi-variable dynamic programming / two-pointer complexity analysis | [Day 8: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

Given two strings `s1` and `s2`, find the shortest contiguous substring `w` of `s1` such that `s2` is a subsequence of `w`.

If there are multiple such minimum-length windows, return the one that starts at the smallest index in `s1`. If no such window exists, return an empty string `""`.

Target complexity: Must run in $O(|s1| \cdot |s2|)$ time and $O(1)$ auxiliary space beyond input strings.

## Input

`s1: str`, `s2: str`

## Output

`str`: the minimum window substring

## Constraints

- 1 <= len(s1) <= 2 * 10^4
- 1 <= len(s2) <= 100
- `s1` and `s2` consist of lowercase English letters only

## Examples

**Example 1**

```text
Input:  s1 = "abcdebdde", s2 = "bde"
Output: "bcde"
```

"bcde" contains "bde" as a subsequence and is shorter than "bdde" (both length 4, but "bcde" starts at index 1 while "bdde" starts at index 5).

**Example 2**

```text
Input:  s1 = "jmeqqaqapq", s2 = "at"
Output: ""
```

't' is not present in s1, so no window exists.

## Function Signature

```python
def min_window_subsequence(s1: str, s2: str) -> str:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Forward scan to match s2 as a subsequence, followed by backward scan from the matched end to find the optimal start point. O(|s1| * |s2|) time and O(1) auxiliary space.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
