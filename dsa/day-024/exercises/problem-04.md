# Problem 4: Longest Repeating Character Replacement

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | window invariants with character frequency | [Day 24: Sliding Window](../README.md) |

## Problem Statement

You are given a string `s` consisting of uppercase English letters and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the operations.

## Input

A string `s: str` and an integer `k: int`.

## Output

An integer representing the maximum length possible.

## Constraints

- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length

## Examples

**Example 1**

```text
Input:  s = "ABAB", k = 2
Output: 4
```

Replace the two 'A's with 'B's or vice versa to get "BBBB" or "AAAA".

**Example 2**

```text
Input:  s = "AABABBA", k = 1
Output: 4
```

Replace the one 'A' in the middle to get "AABBBBA". The substring "BBBB" has length 4.

## Function Signature

```python
def character_replacement(s: str, k: int) -> int:
    """Calculates maximum length of repeating character substring after at most k replacements."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a frequency count of characters in the window and track the count of the most frequent character. A window [L, R] is valid if (window_len - max_freq) <= k. Shrink when invalid. Target O(N) time and O(1) space (alphabet size <= 26).

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
