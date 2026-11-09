# Solution 5: Stable Multi-Key Record Sorter

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Sorting stability, composite keys, and in-place stability preservation

## Approach

We implement a stable sorting algorithm—specifically Insertion Sort—to sort the records. We can either perform a single-pass insertion sort with a composite comparison function (comparing `department` ascending, then `salary` descending, and preserving relative order on exact ties) or perform two sequential passes (first by salary descending, then by department ascending). Using a single-pass stable insertion sort with a custom comparator achieves the desired ordering directly in $O(n^2)$ time and $O(n)$ space without mutating the input.

## Thought Process

A key concept in sorting is stability: elements with equal keys preserve their initial relative order. 

When sorting by composite keys (Primary: `department` ascending, Secondary: `salary` descending), there are two approaches using elementary sorts:
1. **Radix-style two-pass sort**: First stably sort by secondary key (`salary` descending). Then stably sort by primary key (`department` ascending). Because the second sort is stable, it will not disrupt the relative order of elements that have the same primary key, leaving them ordered by the secondary key.
2. **Single-pass composite comparison**: Directly compare `record_a` and `record_b`. Record A precedes Record B if `record_a["department"] < record_b["department"]`, or if `record_a["department"] == record_b["department"]` and `record_a["salary"] > record_b["salary"]`.

In Insertion Sort, an element is shifted to the left as long as it strictly compares as 'less than' the predecessor. If we use strict inequality (`key(x) < key(y)`), elements that are completely equal will not cross each other, strictly maintaining stability. Insertion sort is chosen over Bubble sort because it has lower constant factors and minimal overhead, easily processing $n = 1000$ in a fraction of a second.

## Algorithm

1. Create a shallow copy of the input list of dictionaries so the input is not mutated.
2. Define a comparator function or composite key logic: a record $u$ strictly precedes $v$ if $u[\text{'department'}] < v[\text{'department'}]$, or ($u[\text{'department'}] == v[\text{'department'}]$ and $u[\text{'salary'}] > v[\text{'salary'}])$.
3. Iterate through the copied list with index $i$ from 1 to $n - 1$.
4. Store the current record in a variable `current`.
5. Compare `current` with the record at $j = i - 1$. While $j \ge 0$ and `current` strictly precedes `records[j]`, shift `records[j]` to `records[j + 1]` and decrement $j$.
6. Insert `current` into `records[j + 1]`.
7. Return the sorted list.

## Complexity Analysis

- **Time:** O(n^2) in the worst and average cases, where n is the number of records, due to the nested shift loop of insertion sort. For n <= 1000, 10^6 comparisons and shifts execute well within a few tens of milliseconds in Python.
- **Space:** O(n) auxiliary space to return a new list containing references to the records without modifying the original input list.

## Edge Cases

- Empty input (`records = []`): loop bounds handle this naturally and return an empty list.
- Single element (`len(records) == 1`): loop for $i$ from 1 to 0 does not run; returns a new list with the single element.
- All elements have identical department and salary: strict precedence condition (`current < item`) evaluates to False, so no elements shift, perfectly preserving initial input order.
- Reverse sorted or identical records: handles descending/ascending correctly according to composite criteria.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def stable_multikey_sort(records: list[dict]) -> list[dict]:
    """Sorts records by department ascending, then salary descending, stably without built-in sort."""
    # Create a copy so we do not mutate the input list
    arr = list(records)
    n = len(arr)

    def precedes(a: dict, b: dict) -> bool:
        """Returns True if record `a` strictly precedes record `b`."""
        if a["department"] != b["department"]:
            return a["department"] < b["department"]
        return a["salary"] > b["salary"]

    # Stable insertion sort
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        while j >= 0 and precedes(current, arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

    return arr
```
