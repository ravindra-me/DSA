from collections import defaultdict

def max_equal_frequency_with_skips(nums: list[int], k: int) -> int:
    """Find length of longest contiguous subsegment of identical values with at most k skips."""
    if not nums:
        return 0
    
    n = len(nums)
    val_to_indices: dict[int, list[int]] = defaultdict(list)
    for idx, num in enumerate(nums):
        val_to_indices[num].append(idx)
    
    max_len = 0
    for pos in val_to_indices.values():
        left = 0
        for right in range(len(pos)):
            while (pos[right] - pos[left]) - (right - left) > k:
                left += 1
            matching_count = right - left + 1
            subsegment_len = min(n, matching_count + k)
            if subsegment_len > max_len:
                max_len = subsegment_len
                
    return max_len
