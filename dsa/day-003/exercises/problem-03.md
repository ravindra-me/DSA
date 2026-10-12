# Problem 3: String Compression (Run-Length Encoding)

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | String Building & In-Place Pointer Compacting | [Day 3: Strings](../README.md) |

## Problem Statement

Implement run-length compression on a list of characters `chars`.

For each group of consecutive repeating characters in `chars`:
- If the group's length is `1`, append the character itself.
- If the group's length is greater than `1`, append the character followed by the group's length as individual digit characters.

You must modify the input list `chars` in-place so that the first `k` elements contain the compressed result, and return the new length `k`.

Do not allocate another array for the compressed characters; you must solve this with $O(1)$ extra memory.

## Input

`chars: list[str]` — a mutable list of single-character strings.

## Output

`int` — the length `k` of the compressed prefix in `chars`.

## Constraints

- 1 <= len(chars) <= 2000
- `chars[i]` is a lowercase English letter, uppercase letter, digit, or symbol.
- Must use $O(1)$ extra space.

## Examples

**Example 1**

```text
Input:  chars = ["a", "a", "b", "b", "c", "c", "c"]
Output: 6
```

The compressed list prefix is ["a", "2", "b", "2", "c", "3"], length is 6.

**Example 2**

```text
Input:  chars = ["a"]
Output: 1
```

Edge case: single character. Group length is 1, so no digits are appended. Result is ["a"], length 1.

**Example 3**

```text
Input:  chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
Output: 4
```

Group 'a' has length 1. Group 'b' has length 12. Digits '1' and '2' are written separately: ["a", "b", "1", "2"], length 4.

## Function Signature

```python
def compress_string(chars: list[str]) -> int:
    """Compress consecutive identical characters in-place and return new length."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a read pointer to scan consecutive character blocks and a write pointer to overwrite `chars` in place with character and digit characters. Operates in $O(N)$ time and $O(1)$ extra space.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
