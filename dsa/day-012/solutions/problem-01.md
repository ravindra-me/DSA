# Solution 1: Daily Temperatures

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Next greater element distance using a monotonic decreasing stack

## Approach

Maintain a monotonic decreasing stack of indices representing days whose next warmer temperature has not yet been found. As we iterate through each day, pop elements from the stack while the current day's temperature is strictly warmer than the temperature at the top index, recording the distance in the result array.

## Thought Process

A naive brute-force approach checks every subsequent day for each index $i$ until finding a higher temperature, which takes $O(N^2)$ time in the worst case (e.g., when temperatures are strictly descending). 

To optimize to $O(N)$, observe that when a warmer temperature arrives, it simultaneously resolves the wait time for all prior pending days that are cooler than it. By keeping unresolved day indices in a stack ordered by descending temperature (monotonic decreasing stack), the top of the stack is always the coolest unresolved day seen so far. When the current temperature exceeds the top of the stack, we pop that index $j$, calculate the difference $i - j$, and record it. Once no cooler days remain on top, we push the current day $i$ onto the stack to await its own warmer day.

## Algorithm

1. Initialize an output array `answer` of length $N$ filled with zeros.
2. Initialize an empty stack `stack` to store indices of days.
3. Iterate through the array with index `i` and temperature `temp` from $0$ to $N - 1$.
4. While `stack` is not empty and `temp > temperatures[stack[-1]]`:
5. Pop the index `prev_day = stack.pop()`.
6. Compute the difference `answer[prev_day] = i - prev_day`.
7. Push the current index `i` onto `stack`.
8. Return `answer`.

## Complexity Analysis

- **Time:** O(N) where N is the length of `temperatures`. Each index is pushed onto the stack exactly once and popped at most once.
- **Space:** O(N) auxiliary space for the monotonic stack in the worst case (e.g., strictly decreasing temperatures where all indices remain on the stack).

## Edge Cases

- Single element: The loop runs once, no pop occurs, and [0] is returned correctly.
- Strictly decreasing temperatures: No element is warmer than previous elements, all remain unresolved, and all zeros are returned.
- Strictly increasing temperatures: Every day resolves the immediately preceding day, giving [1, 1, ..., 0].
- Duplicate temperatures: A day is only warmer if its temperature is strictly greater; duplicate values remain on the stack until a strictly higher value is found.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Return the number of days until a warmer temperature."""
    n = len(temperatures)
    answer = [0] * n
    stack: list[int] = []  # stores indices of unresolved days

    for current_day, current_temp in enumerate(temperatures):
        while stack and current_temp > temperatures[stack[-1]]:
            prev_day = stack.pop()
            answer[prev_day] = current_day - prev_day
        stack.append(current_day)

    return answer
```
