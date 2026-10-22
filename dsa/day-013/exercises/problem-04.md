# Problem 4: Predict the Winner of the Assembly

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Round-robin queue simulation with priority/elimination dynamics | [Day 13: Queue](../README.md) |

## Problem Statement

In an assembly of voters, two factions are competing for dominance: the Radicals (`'R'`) and the Democrats (`'D'`). There are `n` senators lined up in a given string `senate` of length `n`, where each character represents a senator's faction.

The voting proceeds in rounds. In each round, each senator who is still active gets a turn to exercise their right, starting from the left of the senate to the right:
1. **Ban a Senator's Right**: A senator can cancel the right of one senator from the rival party for this round and all subsequent rounds.
2. **Announce Victory**: If all remaining senators belong to the same faction, that faction wins.

Every senator exercises their voting right optimally and strategically: each senator will always ban the *next available rival senator* who has yet to vote in the current or subsequent cycle. Once a senator votes in the current cycle, they move to the back of the queue to vote in the next round.

Return `'Radiant'` if the Radicals win, or `'Dire'` if the Democrats win.

## Input

`senate: str`: A string consisting only of characters 'R' and 'D'.

## Output

`str`: Either `'Radiant'` or `'Dire'`.

## Constraints

- 1 <= len(senate) <= 10^4
- senate[i] is either 'R' or 'D'.

## Examples

**Example 1**

```text
Input:  senate = "RD"
Output: "Radiant"
```

Senator R (index 0) bans Senator D (index 1). In round 2, only R remains, so Radiant wins.

**Example 2**

```text
Input:  senate = "RDD"
Output: "Dire"
```

R bans the first D (index 1). The second D (index 2) bans R (index 0). Next round, only D remains, so Dire wins.

## Function Signature

```python
from collections import deque

def predict_party_victory(senate: str) -> str:
    """Predict which party wins the vote following optimal FIFO ban logic."""
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain two queues storing the indices of active 'R' and 'D' senators. Compare the front indices; the smaller index votes first and bans the larger index, re-entering the queue with index + n.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
