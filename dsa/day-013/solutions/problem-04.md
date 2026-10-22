# Solution 4: Predict the Winner of the Assembly

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Round-robin queue simulation with priority/elimination dynamics

## Approach

We can model the voting process using two separate FIFO queues containing the indices of active senators for Radiant (`'R'`) and Dire (`'D'`). In each round, the senator with the smaller index acts first and eliminates the rival senator whose index is polled next. The acting senator then re-enters the back of their queue with an offset index (`index + n`) to represent their participation in the next round.

## Thought Process

A naive simulation might iterate through the string repeatedly, marking characters as banned or deleting them. Scanning for the next available rival linearly in an array takes $O(n)$ per turn, leading to an overall $O(n^2)$ time complexity, which is too slow for $n = 10^4$.

Notice that the optimal greedy strategy for any active senator is always to ban the very next rival who would take a turn. If they banned someone who had already voted in the current cycle instead, the upcoming rival would still get to act and ban one of their allies. Therefore, the senator who acts earliest always bans the earliest acting rival.

Because both turns and bans happen in chronological order, queues naturally maintain the voting order. By storing the original 0-indexed positions in two queues (`radiant_queue` and `dire_queue`), at each step we compare the heads: `r_idx` and `d_idx`.
- Whichever index is smaller votes first and bans the other (the larger index is simply discarded).
- The winning senator gets pushed to the back of their queue for the next round with their turn index updated to `idx + n`, preserving relative round-robin order.
- The loop terminates when one queue becomes empty, leaving the other faction as the victor.

## Algorithm

1. Initialize two double-ended queues (or lists/deques): `r_queue` for Radiant indices and `d_queue` for Dire indices.
2. Iterate through the `senate` string by index `i`: push `i` to `r_queue` if `senate[i] == 'R'`, else push to `d_queue`.
3. Let `n = len(senate)`.
4. While both `r_queue` and `d_queue` are non-empty:
5. Pop `r_idx` from `r_queue` and `d_idx` from `d_queue`.
6. If `r_idx < d_idx`, Radiant bans Dire: re-queue `r_idx + n` into `r_queue`.
7. Else, Dire bans Radiant: re-queue `d_idx + n` into `d_queue`.
8. When one queue is empty, return `'Radiant'` if `r_queue` has remaining elements, else return `'Dire'`.

## Complexity Analysis

- **Time:** $O(n)$ where $n$ is the length of `senate`. In each comparison, exactly one senator is permanently eliminated, so at most $n$ eliminations can occur before one party runs out of senators.
- **Space:** $O(n)$ to store the indices of the senators in the two deques.

## Edge Cases

- Single senator (`"R"` or `"D"`): Loop finishes immediately because one queue is empty at the start; correctly returns the sole party.
- All senators from the same party (`"RRRR"` or `"DDDD"`): The opposing queue starts empty; returns the sole party instantly.
- Alternating patterns (`"RDRD"`): First-round bans alternate smoothly until one side dominates; index offset ensures order consistency.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
from collections import deque

def predict_party_victory(senate: str) -> str:
    """Predict which party wins the vote following optimal FIFO ban logic."""
    r_queue: deque[int] = deque()
    d_queue: deque[int] = deque()
    
    for idx, char in enumerate(senate):
        if char == "R":
            r_queue.append(idx)
        else:
            d_queue.append(idx)
            
    n = len(senate)
    while r_queue and d_queue:
        r_idx = r_queue.popleft()
        d_idx = d_queue.popleft()
        
        if r_idx < d_idx:
            r_queue.append(r_idx + n)
        else:
            d_queue.append(d_idx + n)
            
    return "Radiant" if r_queue else "Dire"
```
