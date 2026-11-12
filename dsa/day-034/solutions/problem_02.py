import random

def find_kth_smallest(nums: list[int], k: int) -> int:
    """Return the k-th smallest element in nums (1-indexed) using Quickselect."""
    target = k - 1
    left, right = 0, len(nums) - 1
    
    while left <= right:
        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]
        
        # 3-way partitioning around pivot
        lt = left      # nums[left..lt-1] < pivot
        i = left       # nums[lt..i-1] == pivot
        gt = right     # nums[gt+1..right] > pivot
        
        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1
        
        # Now nums[lt..gt] == pivot
        if lt <= target <= gt:
            return nums[target]
        elif target < lt:
            right = lt - 1
        else:
            left = gt + 1
            
    return -1
