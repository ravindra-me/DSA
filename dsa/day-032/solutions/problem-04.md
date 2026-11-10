# Solution 4: Maximum Frequency Stack

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Frequency mapping combined with bucketed stacks

## Approach

We maintain a frequency map `freq` to count occurrences of each element, a dictionary of stacks `group` mapping each frequency level to a stack of values at that frequency, and a `max_freq` integer. Pushing an element increments its frequency count and pushes it onto `group[freq[val]]`. Popping retrieves and removes the top element from `group[max_freq]`, decrements its frequency count, and updates `max_freq` if the stack at `max_freq` becomes empty.

## Thought Process

A naive approach might use a max-heap storing `(frequency, push_timestamp, value)`. Heap push and pop operations take $O(\log N)$ time. We can achieve $O(1)$ amortized time for both `push` and `pop` by realizing that an element appearing $k$ times effectively belongs to frequency levels $1, 2, \dots, k$.

By maintaining a stack for each frequency level (`group[f]` storing elements at the time their frequency reached $f$), the stack at `group[max_freq]` naturally preserves the most recently pushed element among all elements with frequency `max_freq`. Popping from `group[max_freq]` automatically breaks tie-breakers by recency in $O(1)$ time.

## Algorithm

1. Initialize `freq` as a hash map storing the current frequency of each value.
2. Initialize `group` as a hash map of lists/stacks, where key `f` holds elements that have reached frequency `f` in order of insertion.
3. Initialize `max_freq = 0` to track the current maximum frequency.
4. For `push(val)`: Increment `freq[val]`. Update `max_freq = max(max_freq, freq[val])`. Append `val` to `group[freq[val]]`.
5. For `pop()`: Pop `val = group[max_freq].pop()`. Decrement `freq[val]`. If `group[max_freq]` is now empty, decrement `max_freq`. Return `val`.

## Complexity Analysis

- **Time:** $O(1)$ time per `push` and `pop` operation. Dictionary lookups and stack push/pop are all $O(1)$.
- **Space:** $O(N)$ space total where $N$ is the number of elements pushed, since each element pushed is stored in `freq` and inside `group` once per frequency level.

## Edge Cases

- Multiple elements with the same maximum frequency: stack ordering in `group[max_freq]` naturally pops the most recently pushed element.
- Duplicate elements pushed consecutively: handled seamlessly as frequency increases and element is added to subsequent frequency stacks.
- Max frequency dropping after pop: correctly detected when `group[max_freq]` becomes empty, decrementing `max_freq` by 1.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
from collections import defaultdict

class FreqStack:
    """A stack-like data structure that pops the most frequent element, breaking ties by recency."""

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        """Pushes an element onto the frequency stack."""
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.max_freq:
            self.max_freq = f
        self.group[f].append(val)

    def pop(self) -> int:
        """Pops and returns the most frequent element in the stack."""
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val
```
