# Solution 5: K-th Smallest Pair Distance

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Two-pointer feasibility check inside binary search on answer

## Approach

Sort the array and binary search over the possible pair distance range $[0, \max(nums) - \min(nums)]$. For each candidate distance $m$, count how many pairs have a distance $\le m$ using a two-pointer sliding window in $O(N)$ time. The smallest $m$ such that the count is at least $k$ is the $k$-th smallest distance.

## Thought Process

The total number of pairs is $N(N-1)/2$, which can be up to $\approx 2 \times 10^8$. Generating and sorting all pair distances or using a min-heap would require at least $O(N^2)$ time and memory, which exceeds limits for $N = 20,000$.

Instead of finding pairs directly, reframe the question as a decision problem: "How many pairs have distance $\le d$?" Notice that this count is monotonically non-decreasing with respect to $d$. When $d = 0$, the count is the number of identical pairs; when $d = \max(nums) - \min(nums)$, the count is all pairs. This monotonicity allows binary searching for the answer $d$.

To count pairs with distance $\le d$ efficiently, sort `nums` in $O(N \log N)$ time. Then, for each right index $j$, find how many left indices $i < j$ satisfy $nums[j] - nums[i] \le d$. Because `nums` is sorted, as $j$ increases, the minimal valid $i$ never moves backward. A two-pointer sliding window can compute the total count in $O(N)$ time. Combining this with binary search over the distance range $[0, 10^6]$ yields $O(N \log(\max(nums) - \min(nums)))$ time.

## Algorithm

1. Sort `nums` in ascending order.
2. Define `low = 0` and `high = nums[-1] - nums[0]`.
3. Implement a helper function `count_pairs_within(max_dist)`: initialize `count = 0` and `left = 0`. For each `right` from 0 to `len(nums) - 1`, advance `left` while `nums[right] - nums[left] > max_dist`. Add `right - left` to `count`. Return `count`.
4. While `low < high`, compute `mid = (low + high) // 2`.
5. If `count_pairs_within(mid) >= k`, the target distance is at most `mid`, so set `high = mid`.
6. Otherwise, the target distance must be greater than `mid`, so set `low = mid + 1`.
7. When `low == high`, return `low`.

## Complexity Analysis

- **Time:** $O(N \log N + N \log D)$, where $N$ is the length of `nums` and $D = \max(nums) - \min(nums) \le 10^6$. Sorting takes $O(N \log N)$, and binary search does $O(\log D)$ iterations, each taking $O(N)$ time via the two-pointer scan.
- **Space:** $O(1)$ auxiliary space beyond the memory needed for sorting in place (or $O(N)$ depending on Python's Timsort implementation).

## Edge Cases

- Duplicate numbers where pairs have distance 0: handled naturally since $nums[j] - nums[i] = 0 \le mid$.
- Minimum length $N = 2$: binary search runs correctly with $k = 1$, returning $nums[1] - nums[0]$.
- $k = 1$ (minimum distance among all pairs) and $k = N(N-1)//2$ (maximum distance among all pairs): binary search boundaries $[0, \max(nums) - \min(nums)]$ cover the entire range of possible distances.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def smallest_distance_pair(nums: list[int], k: int) -> int:
    """Return the k-th smallest distance among all pairs."""
    nums.sort()
    n = len(nums)

    def count_less_or_equal(dist: int) -> int:
        count = 0
        left = 0
        for right in range(n):
            while nums[right] - nums[left] > dist:
                left += 1
            count += right - left
        return count

    low = 0
    high = nums[-1] - nums[0]

    while low < high:
        mid = (low + high) // 2
        if count_less_or_equal(mid) >= k:
            high = mid
        else:
            low = mid + 1

    return low
```
