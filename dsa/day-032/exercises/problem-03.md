# Problem 3: Remove All Adjacent Duplicates in String II

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | State compression using dynamic dynamic frequency stacks | [Day 32: Stack](../README.md) |

## Problem Statement

You are given a string `s` and an integer `k`. A `k`-duplicate removal consists of choosing `k` adjacent and equal letters from `s` and removing them, causing the left and right side of the deleted substring to concatenate together.

We repeatedly make `k`-duplicate removals on `s` until we no longer can. Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

## Input

`s: str`, `k: int`

## Output

`str`

## Constraints

- 1 <= len(s) <= 10^5
- 2 <= k <= 10^4
- `s` consists of lowercase English letters.

## Examples

**Example 1**

```text
Input:  s = "abcd", k = 2
Output: "abcd"
```

No duplicates of length 2 exist.

**Example 2**

```text
Input:  s = "deeedbbcccbdaa", k = 3
Output: "aa"
```

Remove "eee" -> "ddbbcccbdaa", remove "ccc" -> "ddbbbdaa", remove "bbb" -> "ddbdaa", remove "ddd" -> "aa".

## Function Signature

```python
def remove_k_duplicates(s: str, k: int) -> str:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a stack of pairs `[char, count]`. Increment the top pair's count if the character matches, or push `[char, 1]` if it differs. When count reaches `k`, pop the pair from the stack. Target O(N) time and O(N) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
