# Problem 4: Remove Duplicate Letters to Form Smallest Subsequence

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Monotonic stack with character frequency and seen tracking | [Day 14: Strings](../README.md) |

## Problem Statement

Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is **the smallest in lexicographical order** among all possible results.

A string `a` is lexicographically smaller than a string `b` if at the first position where they differ, string `a` has a letter that appears earlier in the alphabet than the corresponding letter in `b`.

## Input

A single string `s` consisting of lowercase English letters.

## Output

A string containing unique characters of `s` in lexicographically smallest order while preserving relative order.

## Constraints

- 1 <= len(s) <= 10^4
- `s` consists of lowercase English letters.

## Examples

**Example 1**

```text
Input:  s = "bcabc"
Output: "abc"
```

Possible unique subsequences are "bca", "cab", and "abc". "abc" is the lexicographically smallest.

**Example 2**

```text
Input:  s = "cbacdcbc"
Output: "acdb"
```

Removing duplicates while preserving relative ordering yields "acdb" as the smallest lexicographical choice.

**Example 3**

```text
Input:  s = "z"
Output: "z"
```

Single character string remains unchanged.

## Function Signature

```python
def remove_duplicate_letters(s: str) -> str:
    """Return the lexicographically smallest subsequence containing every unique letter once."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Track the last occurrence index or remaining counts of each character. Use a monotonic stack along with a 'seen' set: pop characters larger than the current character if they will appear again later.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
