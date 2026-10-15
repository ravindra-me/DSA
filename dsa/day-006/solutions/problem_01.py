def analyze_bits(n: int) -> tuple[bool, int]:
    """Return whether n is a power of two and its number of set bits."""
    is_power_of_two = n > 0 and (n & (n - 1)) == 0
    
    # Count set bits using Brian Kernighan's algorithm
    count = 0
    current = n
    while current > 0:
        current &= current - 1
        count += 1
        
    return is_power_of_two, count
