def power(base: int, exp: int) -> int:
    """Calculates base^exp efficiently using binary exponentiation."""
    if exp == 0:
        return 1
    
    # Divide and conquer approach:
    # If even: (base^2)^(exp/2)
    # If odd: base * (base^2)^((exp-1)/2)
    if exp % 2 == 0:
        return power(base * base, exp // 2)
    else:
        return base * power(base * base, exp // 2)
