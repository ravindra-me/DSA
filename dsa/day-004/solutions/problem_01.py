import sys

# Increase recursion depth to handle constraints up to 1000 safely.
sys.setrecursionlimit(2000)

def recursive_sum(arr: list[int]) -> int:
    """Calculates the sum of a list recursively using an index helper."""
    def _helper(index: int) -> int:
        if index == len(arr):
            return 0
        return arr[index] + _helper(index + 1)

    return _helper(0)
