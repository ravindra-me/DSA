# Problem 1: Valid Anagram Parity

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | frequency counting and balance comparison | [Day 19: Frequency Counting](../README.md) |

## Problem Statement

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Input

Two strings `s` and `t` consisting of lowercase English letters.

## Output

`True` if `t` is an anagram of `s`, else `False`.

## Constraints

- 1 <= len(s), len(t) <= 5 * 10^4
- `s` and `t` consist only of lowercase English letters.

## Examples

**Example 1**

```text
Input:  s = "anagram", t = "nagaram"
Output: True
```

Both strings contain 3 'a's, 1 'g', 1 'm', 1 'n', and 1 'r'.

**Example 2**

```text
Input:  s = "rat", t = "car"
Output: False
```

'rat' and 'car' have different character counts.

**Example 3**

```text
Input:  s = "a", t = "ab"
Output: False
```

Strings of unequal lengths cannot be anagrams.

## Function Signature

```python
def is_anagram(s: str, t: str) -> bool:
    """Return True if t is an anagram of s, otherwise False."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Check lengths first; if unequal, return False. Count character occurrences using a frequency map or an array of size 26 and ensure counts match in O(n) time.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
