# Problem 5: Minimum Window Substring

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Sliding Window with Character Multi-Sets | [Day 3: Strings](../README.md) |

## Problem Statement

Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window.

If there is no such substring, return the empty string `""`.

If there are multiple answers of the same minimum length, return the one that starts at the smallest index.

## Input

`s: str`, `t: str` — strings containing uppercase and lowercase English letters.

## Output

`str` — the shortest substring of `s` containing all characters of `t`.

## Constraints

- 1 <= len(s), len(t) <= 10^5
- `s` and `t` consist of uppercase and lowercase English letters.

## Examples

**Example 1**

```text
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

The substring "BANC" includes 'A', 'B', and 'C', and is length 4. No shorter valid substring exists.

**Example 2**

```text
Input:  s = "a", t = "a"
Output: "a"
```

Edge case: the entire string is the minimum window.

**Example 3**

```text
Input:  s = "a", t = "aa"
Output: ""
```

Edge case: 't' requires two 'a's, but 's' only has one, so no window is possible.

## Function Signature

```python
def min_window(s: str, t: str) -> str:
    """Find the minimum window in s containing all characters of t."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a sliding window with two pointers (`left` and `right`) and a frequency map. Expand `right` until all required characters are satisfied, then shrink `left` to minimize the window while maintaining validity. Target $O(|s| + |t|)$ time.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
