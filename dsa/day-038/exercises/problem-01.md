# Problem 1: First Unique Character in Dynamic Stream

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | FIFO queue with frequency counting for streaming order preservation | [Day 38: Queue](../README.md) |

## Problem Statement

Design a data structure `StreamFirstUnique` that reads characters from an incoming stream one by one and efficiently reports the first non-repeating character seen so far in the stream.

Implement the class:
- `__init__()`: Initializes the stream reader.
- `add(ch: str) -> None`: Ingests a new lowercase English letter `ch`.
- `get_first_unique() -> str`: Returns the first character that has appeared exactly once so far. If no such character exists, return `""`.

## Input

Class method invocations. `add` takes a single lowercase character string `ch`. `get_first_unique` takes no arguments.

## Output

For `get_first_unique()`, a single-character string or `""`.

## Constraints

- Characters are strictly lowercase English letters ('a' - 'z').
- At most 10^5 calls to `add` and `get_first_unique` in total.

## Examples

**Example 1**

```text
Input:  stream = StreamFirstUnique()
stream.add('a')
stream.add('b')
stream.get_first_unique()  # 'a'
stream.add('a')
stream.get_first_unique()  # 'b'
stream.add('b')
stream.get_first_unique()  # ''
Output: 'a', 'b', ''
```

After adding 'a' and 'b', 'a' is the first unique. Adding another 'a' makes 'a' duplicate, leaving 'b' as the first unique. Adding another 'b' leaves no unique characters.

**Example 2**

```text
Input:  stream = StreamFirstUnique()
stream.get_first_unique()
Output: ''
```

Stream is empty initially.

## Function Signature

```python
class StreamFirstUnique:
    def __init__(self) -> None:
        """Initialize the stream data structure."""
        pass

    def add(self, ch: str) -> None:
        """Add character ch to the stream."""
        pass

    def get_first_unique(self) -> str:
        """Return the first unique character in the stream, or empty string."""
        pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain an arrival queue along with a frequency counter or occurrence state. Lazily dequeue elements from the head that have duplicate counts when querying.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
