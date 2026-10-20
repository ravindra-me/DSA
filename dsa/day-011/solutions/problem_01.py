def sort_array_by_parity_ii(nums: list[int]) -> list[int]:
    """Sorts array in-place such that even indices have even values and odd indices have odd values."""
    n = len(nums)
    even_idx = 0
    odd_idx = 1

    while even_idx < n and odd_idx < n:
        while even_idx < n and nums[even_idx] % 2 == 0:
            even_idx += 2
        while odd_idx < n and nums[odd_idx] % 2 == 1:
            odd_idx += 2
        
        if even_idx < n and odd_idx < n:
            nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
            even_idx += 2
            odd_idx += 2

    return nums
