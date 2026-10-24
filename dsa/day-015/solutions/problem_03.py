from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Return the maximum element in every contiguous window of size k."""
    if not nums or k <= 0:
        return []
    
    window_indices: deque[int] = deque()
    result: list[int] = []
    
    for i, val in enumerate(nums):
        # Evict indices that have slipped out of the window
        while window_indices and window_indices[0] <= i - k:
            window_indices.popleft()
        
        # Maintain monotonic decreasing order by value
        while window_indices and nums[window_indices[-1]] <= val:
            window_indices.pop()
            
        window_indices.append(i)
        
        # Once window has reached size k, record the maximum
        if i >= k - 1:
            result.append(nums[window_indices[0]])
            
    return result
