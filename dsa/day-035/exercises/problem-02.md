# Problem 2: Remove Duplicate Letters Lexicographically

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Monotonic Stack with Hash Map / Frequency Count | [Day 35: Monotonic Stack](../README.md) |

## Problem Statement

Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the **lexicographically smallest** among all possible results while preserving the original relative order of non-removed characters.

## Input

s: str

## Output

str

## Constraints

- 1 <= s.length <= 10^4
- s consists of lowercase English letters.

## Examples

**Example 1**

```text
Input:  s = "bcabc"
Output: "abc"
```

Removing duplicates leaves unique letters 'a', 'b', 'c'. The lexicographically smallest sequence is "abc".

**Example 2**

```text
Input:  s = "cbacdcbc"
Output: "acdb"
```

"acdb" preserves character order requirements while minimizing lexicographical value.

## Function Signature

```python
def remove_duplicate_letters(s: str) -> str:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Track last occurrences or remaining counts of each character. Maintain a monotonic increasing stack of characters. Pop the stack top if it is greater than the current char AND will appear later in the string.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
