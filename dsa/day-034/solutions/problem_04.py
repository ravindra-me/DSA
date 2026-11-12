import random
import sys

sys.setrecursionlimit(200000)

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    """Return the k closest points to the origin using Quickselect."""
    def dist_sq(p: list[int]) -> int:
        return p[0] * p[0] + p[1] * p[1]

    def partition(left: int, right: int) -> int:
        pivot_idx = random.randint(left, right)
        points[pivot_idx], points[right] = points[right], points[pivot_idx]
        pivot_dist = dist_sq(points[right])
        
        i = left
        for j in range(left, right):
            if dist_sq(points[j]) <= pivot_dist:
                points[i], points[j] = points[j], points[i]
                i += 1
        
        points[i], points[right] = points[right], points[i]
        return i

    left, right = 0, len(points) - 1
    target = k - 1
    while left < right:
        pivot_idx = partition(left, right)
        if pivot_idx == target:
            break
        elif pivot_idx < target:
            left = pivot_idx + 1
        else:
            right = pivot_idx - 1
            
    return points[:k]
