import random

def wiggle_sort(nums: list[int]) -> None:
    """
    Reorders the array in-place such that nums[0] < nums[1] > nums[2] < nums[3]...
    Achieves O(N) average time complexity and O(1) extra space.
    """
    n = len(nums)
    if n <= 1:
        return

    def quickselect(left: int, right: int, k: int) -> int:
        while left <= right:
            pivot_idx = random.randint(left, right)
            pivot_val = nums[pivot_idx]
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            
            store_idx = left
            for i in range(left, right):
                if nums[i] < pivot_val:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1
            nums[store_idx], nums[right] = nums[right], nums[store_idx]
            
            if store_idx == k:
                return nums[store_idx]
            elif store_idx < k:
                left = store_idx + 1
            else:
                right = store_idx - 1
        return nums[k]

    median = quickselect(0, n - 1, n // 2)

    # Virtual index mapping
    # Maps 0, 1, 2, ... to 1, 3, 5, ... 0, 2, 4, ...
    def map_index(i: int) -> int:
        return (1 + 2 * i) % (n | 1)

    # 3-way partitioning using mapped indices
    left, i, right = 0, 0, n - 1
    while i <= right:
        mapped_i = map_index(i)
        if nums[mapped_i] > median:
            mapped_left = map_index(left)
            nums[mapped_i], nums[mapped_left] = nums[mapped_left], nums[mapped_i]
            left += 1
            i += 1
        elif nums[mapped_i] < median:
            mapped_right = map_index(right)
            nums[mapped_i], nums[mapped_right] = nums[mapped_right], nums[mapped_i]
            right -= 1
        else:
            i += 1
