# Problem 3: Longest Substring Without Repeating Characters

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | variable-size window (longest subarray with hash set/map) | [Day 24: Sliding Window](../README.md) |

## Problem Statement

Given a string `s`, find the length of the longest substring without duplicate characters.

## Input

A string `s: str`.

## Output

An integer representing the length of the longest non-repeating substring.

## Constraints

- 0 <= len(s) <= 10^5
- s consists of English letters, digits, symbols, and spaces.

## Examples

**Example 1**

```text
Input:  s = "abcabcbb"
Output: 3
```

The answer is "abc", with the length of 3.

**Example 2**

```text
Input:  s = ""
Output: 0
```

Empty string has length 0.

**Example 3**

```text
Input:  s = "bbbbb"
Output: 1
```

The answer is "b", with the length of 1.

## Function Signature

```python
def length_of_longest_substring(s: str) -> int:
    """Returns the length of the longest substring without repeating characters."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a dynamic sliding window tracking character frequencies or last seen indices. Advance the right pointer, and shrink left when duplicates occur. Target O(N) time and O(min(N, Alphabet)) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
