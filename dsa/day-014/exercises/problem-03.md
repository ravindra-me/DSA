# Problem 3: Find All Anagrams in a String

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Fixed sliding window with character frequency signature | [Day 14: Strings](../README.md) |

## Problem Statement

Given two strings `s` and `p`, return a list of all start indices of `p`'s anagrams in `s`. The indices may be returned in any order.

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Input

Two strings `s` and `p` consisting of lowercase English letters.

## Output

A list of integers `list[int]` representing starting indices.

## Constraints

- 1 <= len(s), len(p) <= 3 * 10^4
- `s` and `p` consist of lowercase English letters.

## Examples

**Example 1**

```text
Input:  s = "cbaebabacd", p = "abc"
Output: [0, 6]
```

The substring with start index = 0 is "cba", which is an anagram of "abc". The substring with start index = 6 is "bac", which is an anagram of "abc".

**Example 2**

```text
Input:  s = "abab", p = "ab"
Output: [0, 1, 2]
```

Substrings starting at 0 ("ab"), 1 ("ba"), and 2 ("ab") are all anagrams of "ab".

**Example 3**

```text
Input:  s = "a", p = "aa"
Output: []
```

p is longer than s, so no anagram exists.

## Function Signature

```python
def find_all_anagrams(s: str, p: str) -> list[int]:
    """Find all start indices in s that form anagrams of p."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a sliding window of length len(p) over s. Use frequency count arrays (or match counters) of size 26 and slide the window one character at a time in O(1) per step.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
