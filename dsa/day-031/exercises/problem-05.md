# Problem 5: Stable Multi-Key Record Sorter

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Sorting stability, composite keys, and in-place stability preservation | [Day 31: Bubble, Selection & Insertion Sort](../README.md) |

## Problem Statement

You are given a list of employee records. Each record is represented as a dictionary with three fields:
- `"id"`: `int` (unique identifier)
- `"department"`: `str`
- `"salary"`: `int`

You are asked to sort these records by multiple criteria sequentially: first by `"salary"` in descending order, then by `"department"` in ascending alphabetical order. 

By exploiting algorithm **stability**, sorting the records first by the secondary key (`"salary"` descending) and then with a **stable sort** by the primary key (`"department"` ascending) will produce the correct final order where within each department, employees appear strictly in descending order of salary, and employees with identical department and salary maintain their original relative input order.

Implement `stable_multikey_sort(records: list[dict]) -> list[dict]` using a stable elementary sort (such as Insertion Sort or Bubble Sort). You must NOT use Python's built-in `sort()` or `sorted()`. Return a new list containing the sorted records.

## Input

A list of dictionaries `records`, where each dictionary has keys `"id"`, `"department"`, and `"salary"`.

## Output

A list of dictionaries sorted by `department` ascending, then `salary` descending, preserving initial order for ties.

## Constraints

- 0 <= len(records) <= 1000
- 1 <= len(department) <= 20
- 0 <= salary <= 10^7
- id is a unique positive integer

## Examples

**Example 1**

```text
Input:  records = [
  {"id": 1, "department": "Engineering", "salary": 90000},
  {"id": 2, "department": "Marketing", "salary": 70000},
  {"id": 3, "department": "Engineering", "salary": 120000},
  {"id": 4, "department": "Marketing", "salary": 70000}
]
Output: [
  {"id": 3, "department": "Engineering", "salary": 120000},
  {"id": 1, "department": "Engineering", "salary": 90000},
  {"id": 2, "department": "Marketing", "salary": 70000},
  {"id": 4, "department": "Marketing", "salary": 70000}
]
```

Engineering comes before Marketing. Within Engineering, 120000 > 90000. Within Marketing, salaries are tied at 70000, so id 2 precedes id 4 because id 2 appeared first in the input.

**Example 2**

```text
Input:  records = []
Output: []
```

Empty input produces empty list.

## Function Signature

```python
def stable_multikey_sort(records: list[dict]) -> list[dict]:
    """Sorts records by department ascending, then salary descending, stably without built-in sort."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Implement a stable insertion sort subroutine. Apply it first on the salary key with reverse comparator (higher salary first), and second on the department key (lexicographical order). Stability ensures the salary ordering is preserved within each department.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
