from collections import deque

def constrained_subset_sum(nums: list[int], k: int) -> int:
    """Compute maximum sum of a non-empty subsequence with distance <= k between indices."""
    n = len(nums)
    dp = [0] * n
    dq = deque()  # stores indices, dp[dq] is strictly decreasing
    max_sum = float('-inf')
    
    for i in range(n):
        # Remove indices outside the k-window
        if dq and dq[0] < i - k:
            dq.popleft()
        
        # Max value in window is dp[dq[0]] if positive
        max_prev = dp[dq[0]] if dq and dp[dq[0]] > 0 else 0
        dp[i] = nums[i] + max_prev
        
        max_sum = max(max_sum, dp[i])
        
        # Maintain monotonic decreasing order in deque
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
            
        dq.append(i)
        
    return max_sum
