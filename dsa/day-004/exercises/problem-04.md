# Problem 4: Nested List Sum

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Tree traversal | [Day 4: Recursion](../README.md) |

## Problem Statement

You are given a list that may contain integers or other lists (arbitrary depth). Calculate the sum of all integers in the structure.

## Input

A nested list (list[int | list]).

## Output

An integer representing the total sum.

## Constraints

- Depth can be arbitrary.
- Elements are either integers or lists of the same structure.

## Examples

**Example 1**

```text
Input:  [1, [2, 3], [[4]]]
Output: 10
```

1 + 2 + 3 + 4 = 10

**Example 2**

```text
Input:  []
Output: 0
```

Empty list is 0.

## Function Signature

```python
def nested_sum(nested_list: list) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Iterate through the elements. If an element is an integer, add it to sum. If it is a list, call the function recursively on that sub-list and add the result.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
