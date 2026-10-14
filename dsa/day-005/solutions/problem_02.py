import math
from typing import Sequence

def array_gcd_lcm(nums: Sequence[int]) -> tuple[int, int]:
    """Computes the overall GCD and LCM of an array of positive integers."""
    if not nums:
        raise ValueError("nums must not be empty")

    current_gcd = nums[0]
    current_lcm = nums[0]

    for x in nums[1:]:
        if current_gcd != 1:
            current_gcd = math.gcd(current_gcd, x)
        
        # lcm(a, b) = (a * b) // gcd(a, b)
        # Dividing first keeps intermediate numbers smaller
        current_lcm = (current_lcm // math.gcd(current_lcm, x)) * x

    return current_gcd, current_lcm
