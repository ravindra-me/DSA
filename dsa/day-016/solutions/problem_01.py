from collections import defaultdict


def find_difference_pair(nums: list[int], diff: int) -> tuple[int, int] | None:
    """Find (i, j) such that nums[i] - nums[j] == diff."""
    val_to_indices: dict[int, list[int]] = defaultdict(list)
    for idx, num in enumerate(nums):
        # We only need at most the first two indices for any value
        if len(val_to_indices[num]) < 2:
            val_to_indices[num].append(idx)

    for i, num in enumerate(nums):
        target = num - diff
        if target in val_to_indices:
            for j in val_to_indices[target]:
                if j != i:
                    return (i, j)

    return None
