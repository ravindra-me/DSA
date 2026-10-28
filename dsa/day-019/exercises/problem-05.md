# Problem 5: Minimum Window Anagram Substring

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | dynamic frequency matching over sliding windows | [Day 19: Frequency Counting](../README.md) |

## Problem Statement

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in ascending order.

An anagram of string `p` is another string that contains the same characters with the exact same frequencies.

## Input

Two strings `s` and `p` consisting of lowercase English letters.

## Output

A list of integer start indices where an anagram of `p` begins in `s`.

## Constraints

- 1 <= len(s), len(p) <= 3 * 10^4
- `s` and `p` consist of lowercase English letters.

## Examples

**Example 1**

```text
Input:  s = "cbaebabacd", p = "abc"
Output: [0, 6]
```

The substring starting at index 0 is "cba", which is an anagram of "abc". The substring starting at index 6 is "bac", which is an anagram of "abc".

**Example 2**

```text
Input:  s = "abab", p = "ab"
Output: [0, 1, 2]
```

Substrings at 0 ("ab"), 1 ("ba"), and 2 ("ab") are all anagrams of "ab".

**Example 3**

```text
Input:  s = "a", p = "aa"
Output: []
```

`p` is longer than `s`, so no anagram can exist.

## Function Signature

```python
def find_anagrams(s: str, p: str) -> list[int]:
    """Return start indices of all anagrams of p in s."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a fixed-size sliding window of length len(p) using frequency counts. Track matching character counts or compare frequency maps in O(1) time per step, achieving O(len(s)) total time.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
