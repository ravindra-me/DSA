# Problem 4: Find Longest Awesome Substring

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Prefix parity bitmask combined with hash map for palindrome eligibility | [Day 23: Bit Manipulation](../README.md) |

## Problem Statement

You are given a string `s` consisting only of digits `'0'` through `'9'`.

An "awesome" substring is a non-empty substring of `s` such that we can make any number of swaps to make it a palindrome.

Return the maximum length of an awesome substring in `s`.

## Input

A string `s` consisting of digits `0`-`9`.

## Output

An integer representing the length of the longest awesome substring.

## Constraints

- 1 <= s.length <= 10^5
- s consists only of digits '0'-'9'.

## Examples

**Example 1**

```text
Input:  s = "3242415"
Output: 5
```

The substring "24241" can be rearranged into "24142", which is a palindrome. Length is 5.

**Example 2**

```text
Input:  s = "12345678"
Output: 1
```

Any single character is a palindrome.

**Example 3**

```text
Input:  s = "00000"
Output: 5
```

All identical digits form a palindrome directly.

## Function Signature

```python
def longest_awesome(s: str) -> int:
    """Find length of longest substring that can be rearranged into a palindrome."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a 10-bit prefix parity mask. Substrings are valid if prefix masks match (all even counts) or differ by exactly one bit (one odd count). Record the earliest index of each mask.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
