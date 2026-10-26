# Problem 4: Find K-th Symbol in Grammar

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Divide-and-conquer on virtual binary trees with logarithmic recursion | [Day 17: Recursion](../README.md) |

## Problem Statement

We build a table of `n` rows (1-indexed). We start by writing `0` in the 1st row (`row 1 = "0"`). Now in every subsequent row, we look at the previous row and replace each occurrence of `0` with `"01"`, and each occurrence of `1` with `"10"`.

- Row 1: `0`
- Row 2: `01`
- Row 3: `0110`
- Row 4: `01101001`

Given two integers `n` and `k`, return the `k`-th (1-indexed) symbol in the `n`-th row of a table of `n` rows.

Your solution must run in $O(n)$ time and $O(n)$ stack space, operating strictly recursively without generating strings.

## Input

`n`: int, the row index (1-indexed).
`k`: int, the column index in row `n` (1-indexed).

## Output

Returns `0` or `1` as an integer representing the symbol.

## Constraints

- 1 <= n <= 30
- 1 <= k <= 2^(n - 1)

## Examples

**Example 1**

```text
Input:  n = 1, k = 1
Output: 0
```

Row 1 is simply "0".

**Example 2**

```text
Input:  n = 2, k = 1
Output: 0
```

Row 2 is "01", first symbol is 0.

**Example 3**

```text
Input:  n = 2, k = 2
Output: 1
```

Row 2 is "01", second symbol is 1.

**Example 4**

```text
Input:  n = 4, k = 5
Output: 1
```

Row 4 is "01101001", the 5th character is '1'.

## Function Signature

```python
def kth_grammar(n: int, k: int) -> int:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use divide-and-conquer: observe that the first half of row n is identical to row n-1, while the second half is the bitwise inversion of row n-1. Recurse toward n=1.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
